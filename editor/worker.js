/**
 * worker.js — the wiki's public diff editor (Stage 3 §3.1, Tier 1).
 *
 * One Cloudflare Worker, no build step, no external dependencies:
 *   GET  /wiki/:slug/edit        → the editor UI (inline HTML/CSS/JS below)
 *   GET  /api/page/:slug         → { path, markdown, sections[] } from GitHub raw
 *   POST /api/submit             → branch + commit + PR via the GitHub API
 *
 * Design rules carried in from docs/ARCHITECTURE-COMMUNITY.md:
 *   - Git is the source of truth; this Worker NEVER writes to Ghost.
 *   - Tier 1 edits ONE `##` section at a time (frontmatter and H1 excluded).
 *   - A source is required when the edit touches a factual claim; the evidence
 *     standard is stated in the UI, not hidden in a contributing doc.
 *   - Every submission becomes a PR (never a direct commit); lint + diff_guard
 *     run there, and T1 review is the gate to main.
 *
 * Secrets (Worker env):
 *   GITHUB_TOKEN — fine-grained PAT or App token; needs contents:write + pull_requests:write
 *                  on OWNER/REPO only.
 * Vars (wrangler.toml): OWNER, REPO, BASE_BRANCH.
 *
 * Abuse controls in v1: honeypot field, per-IP token bucket (in-isolate; KV can
 * replace it later), 20KB body cap, section-must-differ check. Turnstile is left
 * as a TODO wired-but-disabled: add the site key + secret and flip REQUIRE_TURNSTILE.
 */

const RATE = { capacity: 5, refillMs: 60_000 };      // 5 submits/min/IP per isolate
const buckets = new Map();

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const { pathname } = url;

    try {
      let m;
      if ((m = pathname.match(/^\/wiki\/([a-z0-9-]+)\/edit\/?$/)))
        return htmlResponse(EDITOR_HTML.replaceAll("__SLUG__", m[1]));
      if ((m = pathname.match(/^\/api\/page\/([a-z0-9-]+)$/)))
        return apiPage(m[1], env);
      if (pathname === "/api/submit" && request.method === "POST")
        return apiSubmit(request, env);
      if (pathname === "/") return htmlResponse(INDEX_HTML);
      return json({ error: "not found" }, 404);
    } catch (e) {
      return json({ error: `internal: ${e.message}` }, 500);
    }
  },
};

/* ── GitHub helpers ─────────────────────────────────────────────────────── */

const GH = "https://api.github.com";
const ghHeaders = (env) => ({
  Authorization: `Bearer ${env.GITHUB_TOKEN}`,
  Accept: "application/vnd.github+json",
  "User-Agent": "georgism-wiki-editor",
  "X-GitHub-Api-Version": "2022-11-28",
});

async function gh(env, method, path, body) {
  const res = await fetch(`${GH}${path}`, {
    method,
    headers: { ...ghHeaders(env), ...(body ? { "Content-Type": "application/json" } : {}) },
    body: body ? JSON.stringify(body) : undefined,
  });
  if (!res.ok) throw new Error(`GitHub ${method} ${path} → ${res.status}: ${(await res.text()).slice(0, 300)}`);
  return res.json();
}

/* ── slug → repo path, via the inventory census (cached per isolate) ────── */

let inventoryCache = { at: 0, map: null };

async function slugToPath(slug, env) {
  const now = Date.now();
  if (!inventoryCache.map || now - inventoryCache.at > 10 * 60_000) {
    const res = await fetch(
      `https://raw.githubusercontent.com/${env.OWNER}/${env.REPO}/${env.BASE_BRANCH}/sources/wiki-inventory.csv`,
      { headers: { "User-Agent": "georgism-wiki-editor" } },
    );
    if (!res.ok) throw new Error(`inventory fetch ${res.status}`);
    const map = new Map();
    for (const line of (await res.text()).split("\n").slice(1)) {
      const [s, , category] = line.split(",");   // slug,title,category,... (slug/category never contain commas)
      if (s && category) map.set(s.trim(), `${category.trim()}/${s.trim()}.md`);
    }
    inventoryCache = { at: now, map };
  }
  return inventoryCache.map.get(slug) || null;
}

/* ── sectioning: frontmatter + H1 are locked; each `## ` heading opens one ── */

function splitSections(markdown) {
  const lines = markdown.split("\n");
  const sections = [];
  let start = null, heading = null;
  lines.forEach((line, i) => {
    if (/^## /.test(line)) {
      if (start !== null) sections.push({ heading, start, end: i });
      start = i;
      heading = line.replace(/^## /, "").trim();
    }
  });
  if (start !== null) sections.push({ heading, start, end: lines.length });
  return sections;
}

async function apiPage(slug, env) {
  const path = await slugToPath(slug, env);
  if (!path) return json({ error: `no wiki page for slug '${slug}'` }, 404);
  const res = await fetch(
    `https://raw.githubusercontent.com/${env.OWNER}/${env.REPO}/${env.BASE_BRANCH}/${path}`,
    { headers: { "User-Agent": "georgism-wiki-editor" } },
  );
  if (!res.ok) return json({ error: `page fetch ${res.status}` }, 502);
  const markdown = await res.text();
  const sections = splitSections(markdown).map((s) => ({
    heading: s.heading,
    text: markdown.split("\n").slice(s.start, s.end).join("\n"),
  }));
  return json({ slug, path, sections });
}

/* ── submit: validate → branch → commit → PR ────────────────────────────── */

function rateLimited(ip) {
  const now = Date.now();
  let b = buckets.get(ip);
  if (!b) { b = { tokens: RATE.capacity, at: now }; buckets.set(ip, b); }
  b.tokens = Math.min(RATE.capacity, b.tokens + ((now - b.at) / RATE.refillMs) * RATE.capacity);
  b.at = now;
  if (b.tokens < 1) return true;
  b.tokens -= 1;
  return false;
}

async function apiSubmit(request, env) {
  const ip = request.headers.get("CF-Connecting-IP") || "local";
  if (rateLimited(ip)) return json({ error: "rate limited — try again in a minute" }, 429);

  const raw = await request.text();
  if (raw.length > 20_000) return json({ error: "submission too large" }, 413);
  let b;
  try { b = JSON.parse(raw); } catch { return json({ error: "bad JSON" }, 400); }

  // Honeypot: real UI never fills this.
  if (b.website) return json({ ok: true, pr: null });

  const { slug, sectionHeading, newText, rationale, factual, source, name } = b;
  if (!slug || !sectionHeading || typeof newText !== "string")
    return json({ error: "missing slug/sectionHeading/newText" }, 400);
  if (!rationale || rationale.trim().length < 10)
    return json({ error: "a rationale of at least 10 characters is required" }, 400);
  if (factual && !/^https?:\/\/\S+/.test(source || ""))
    return json({ error: "edits to factual claims require a source URL — we can't publish a claim we can't verify" }, 400);

  const path = await slugToPath(slug, env);
  if (!path) return json({ error: `no wiki page for slug '${slug}'` }, 404);

  // Re-fetch the CURRENT file via the API (fresh, and we need the blob sha).
  const file = await gh(env, "GET", `/repos/${env.OWNER}/${env.REPO}/contents/${path}?ref=${env.BASE_BRANCH}`);
  const current = atob(file.content.replace(/\n/g, ""));
  const decoded = new TextDecoder().decode(Uint8Array.from(current, (c) => c.charCodeAt(0)));

  const sections = splitSections(decoded);
  const target = sections.find((s) => s.heading === sectionHeading);
  if (!target)
    return json({ error: `section '${sectionHeading}' no longer exists — the page changed since you loaded it; reload and re-apply` }, 409);

  const lines = decoded.split("\n");
  const oldSection = lines.slice(target.start, target.end).join("\n");
  if (oldSection.trim() === newText.trim())
    return json({ error: "no change detected in the section" }, 400);

  const updated = [...lines.slice(0, target.start), ...newText.replace(/\n+$/, "").split("\n"), "", ...lines.slice(target.end)]
    .join("\n").replace(/\n{3,}/g, "\n\n");

  // Branch from the current tip of base.
  const ref = await gh(env, "GET", `/repos/${env.OWNER}/${env.REPO}/git/ref/heads/${env.BASE_BRANCH}`);
  const branch = `suggest/${slug}-${Date.now().toString(36)}`;
  await gh(env, "POST", `/repos/${env.OWNER}/${env.REPO}/git/refs`, {
    ref: `refs/heads/${branch}`, sha: ref.object.sha,
  });

  const trailer = name ? `\n\nSuggested-by: ${String(name).slice(0, 80)}` : "";
  const b64 = btoa(String.fromCharCode(...new TextEncoder().encode(updated)));
  await gh(env, "PUT", `/repos/${env.OWNER}/${env.REPO}/contents/${path}`, {
    message: `suggest(${slug}): edit section "${sectionHeading}"${trailer}`,
    content: b64, sha: file.sha, branch,
  });

  const pr = await gh(env, "POST", `/repos/${env.OWNER}/${env.REPO}/pulls`, {
    title: `Suggestion: ${slug} — ${sectionHeading}`,
    head: branch, base: env.BASE_BRANCH,
    body: [
      `**Community suggestion** via the wiki diff editor (Tier 1).`,
      ``, `**Page:** \`${path}\``, `**Section:** ${sectionHeading}`,
      ``, `**Rationale:**`, rationale.trim(),
      factual ? `\n**Source for the factual change:** ${source}` : ``,
      name ? `\n*Submitted by: ${String(name).slice(0, 80)}*` : `\n*Submitted anonymously*`,
      ``, `---`, `_Review per EDITORIAL.md — lint + diff_guard run in CI; T1 is the gate to main._`,
    ].join("\n"),
  });

  try {
    await gh(env, "POST", `/repos/${env.OWNER}/${env.REPO}/issues/${pr.number}/labels`, { labels: ["suggestion", "from-web"] });
  } catch { /* labels are cosmetic; never fail the submission over them */ }

  return json({ ok: true, pr: { number: pr.number, url: pr.html_url } });
}

/* ── plumbing ───────────────────────────────────────────────────────────── */

const json = (obj, status = 200) =>
  new Response(JSON.stringify(obj), { status, headers: { "Content-Type": "application/json" } });
const htmlResponse = (html) =>
  new Response(html, { headers: { "Content-Type": "text/html; charset=utf-8" } });

/* ── the UI ─────────────────────────────────────────────────────────────── */

const INDEX_HTML = `<!doctype html><meta charset=utf-8><title>Wiki editor</title>
<body style="font-family:system-ui;max-width:40em;margin:4em auto;line-height:1.5">
<h1>Georgism Wiki — suggestion editor</h1>
<p>Open any article's editor at <code>/wiki/&lt;slug&gt;/edit</code> —
e.g. <a href="/wiki/land-value-tax/edit">/wiki/land-value-tax/edit</a>.</p>`;

const EDITOR_HTML = `<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Suggest an edit — __SLUG__</title>
<style>
  :root { --red:#fdd; --green:#dfd; --ink:#1a202c; --line:#e2e8f0; --accent:#2b6cb0; }
  * { box-sizing:border-box }
  body { font-family:system-ui,sans-serif; color:var(--ink); margin:0; background:#f7fafc }
  header { background:#fff; border-bottom:1px solid var(--line); padding:.8em 1.2em; display:flex; gap:1em; align-items:baseline; flex-wrap:wrap }
  header h1 { font-size:1.05em; margin:0 }
  header .std { font-size:.8em; color:#555; max-width:46em }
  main { max-width:1100px; margin:1em auto; padding:0 1em }
  select,textarea,input[type=text],input[type=url] { width:100%; font:inherit; padding:.5em; border:1px solid var(--line); border-radius:6px }
  textarea#src { font-family:ui-monospace,Menlo,Consolas,monospace; font-size:.85em; min-height:16em; resize:vertical }
  .cols { display:grid; grid-template-columns:1fr 1fr; gap:1em }
  @media (max-width:900px){ .cols{grid-template-columns:1fr} }
  .panel { background:#fff; border:1px solid var(--line); border-radius:8px; padding:1em; margin-top:1em }
  .panel h2 { font-size:.85em; text-transform:uppercase; letter-spacing:.05em; color:#666; margin:0 0 .6em }
  #diff { font-family:ui-monospace,Menlo,Consolas,monospace; font-size:.8em; white-space:pre-wrap; overflow-x:auto; max-height:24em; overflow-y:auto }
  #diff .d { background:var(--red); text-decoration:line-through; display:block }
  #diff .a { background:var(--green); display:block }
  #diff .c { color:#888; display:block }
  .meta label { display:block; margin-top:.8em; font-size:.9em; font-weight:600 }
  .meta .hint { font-weight:400; color:#666; font-size:.85em }
  .evidence { border-left:3px solid var(--accent); background:#ebf4ff; padding:.6em .8em; font-size:.85em; margin-top:.8em; border-radius:0 6px 6px 0 }
  button#submit { margin-top:1em; background:var(--accent); color:#fff; border:0; padding:.7em 1.6em; border-radius:6px; font:inherit; cursor:pointer }
  button#submit:disabled { background:#a0aec0; cursor:not-allowed }
  #status { margin-top:.8em; font-size:.9em }
  #status a { color:var(--accent) }
  .hp { position:absolute; left:-9999px }
</style></head><body>
<header>
  <h1>Suggest an edit — <code>__SLUG__</code></h1>
  <div class="std">Changes open a <b>pull request</b> reviewed by an editor before anything publishes. Frontmatter and the page's evidence wiring aren't editable here.</div>
</header>
<main>
  <div class="panel">
    <h2>1 · Pick the section to edit</h2>
    <select id="section"><option>Loading…</option></select>
  </div>
  <div class="cols">
    <div class="panel"><h2>2 · Edit (Markdown)</h2><textarea id="src" spellcheck="true"></textarea></div>
    <div class="panel"><h2>Your change (live diff)</h2><div id="diff"><span class="c">Edit the text to see the diff…</span></div></div>
  </div>
  <div class="panel meta">
    <h2>3 · About this change</h2>
    <label>Why this change? <span class="hint">(required)</span>
      <input type="text" id="rationale" maxlength="500" placeholder="e.g. The 2024 figure is out of date — the 2026 report revises it to…"></label>
    <label><input type="checkbox" id="factual" style="width:auto"> This edit changes a factual claim (a number, a finding, who-said-what)</label>
    <div id="srcwrap" style="display:none">
      <label>Source URL for the correction <span class="hint">(required for factual changes)</span>
        <input type="url" id="source" placeholder="https://…"></label>
      <div class="evidence"><b>Our standard:</b> we cite every substantive claim. A suggestion without a
        source can still flag a problem — but we can't publish a claim we can't verify.</div>
    </div>
    <label>Your name <span class="hint">(optional — credited in the change record)</span>
      <input type="text" id="name" maxlength="80"></label>
    <input class="hp" type="text" id="website" tabindex="-1" autocomplete="off">
    <button id="submit">Submit suggestion</button>
    <div id="status"></div>
  </div>
</main>
<script>
const slug = "__SLUG__";
let sections = [], original = "";

async function load() {
  const r = await fetch("/api/page/" + slug);
  const d = await r.json();
  if (!r.ok) { document.getElementById("status").textContent = d.error; return; }
  sections = d.sections;
  const sel = document.getElementById("section");
  sel.innerHTML = sections.map((s,i)=>'<option value="'+i+'">'+esc(s.heading)+'</option>').join("");
  sel.onchange = pick; pick();
}
function pick() {
  const i = +document.getElementById("section").value || 0;
  original = sections[i].text;
  document.getElementById("src").value = original;
  renderDiff();
}
function esc(s){return s.replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]))}

/* line-level LCS diff — small inputs (one section), O(n·m) is fine */
function diffLines(a, b) {
  const A=a.split("\\n"), B=b.split("\\n"), n=A.length, m=B.length;
  const L=Array.from({length:n+1},()=>new Uint16Array(m+1));
  for(let i=n-1;i>=0;i--)for(let j=m-1;j>=0;j--)
    L[i][j]=A[i]===B[j]?L[i+1][j+1]+1:Math.max(L[i+1][j],L[i][j+1]);
  const out=[];let i=0,j=0;
  while(i<n&&j<m){
    if(A[i]===B[j]){out.push(["c",A[i]]);i++;j++;}
    else if(L[i+1][j]>=L[i][j+1])out.push(["d",A[i++]]);
    else out.push(["a",B[j++]]);
  }
  while(i<n)out.push(["d",A[i++]]);
  while(j<m)out.push(["a",B[j++]]);
  return out;
}
function renderDiff(){
  const now=document.getElementById("src").value;
  const ops=diffLines(original,now);
  const changed=ops.some(o=>o[0]!=="c");
  const el=document.getElementById("diff");
  if(!changed){el.innerHTML='<span class="c">No changes yet.</span>';return;}
  // context-collapse: show changed lines with 2 lines of context
  const keep=new Set();
  ops.forEach((o,k)=>{if(o[0]!=="c")for(let d=-2;d<=2;d++)keep.add(k+d);});
  let html="",gap=false;
  ops.forEach((o,k)=>{
    if(!keep.has(k)){if(!gap){html+='<span class="c">⋮</span>';gap=true;}return;}
    gap=false;
    html+='<span class="'+o[0]+'">'+(o[0]==="d"?"− ":o[0]==="a"?"+ ":"  ")+esc(o[1]||" ")+'</span>';
  });
  el.innerHTML=html;
}
document.getElementById("src").addEventListener("input",renderDiff);
document.getElementById("factual").addEventListener("change",e=>{
  document.getElementById("srcwrap").style.display=e.target.checked?"":"none";
});
document.getElementById("submit").addEventListener("click",async()=>{
  const btn=document.getElementById("submit"),st=document.getElementById("status");
  btn.disabled=true;st.textContent="Submitting…";
  const i=+document.getElementById("section").value||0;
  const body={slug,sectionHeading:sections[i].heading,
    newText:document.getElementById("src").value,
    rationale:document.getElementById("rationale").value,
    factual:document.getElementById("factual").checked,
    source:document.getElementById("source").value,
    name:document.getElementById("name").value,
    website:document.getElementById("website").value};
  const r=await fetch("/api/submit",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(body)});
  const d=await r.json();
  if(r.ok&&d.pr){st.innerHTML='✅ Thank you! Your suggestion is now <a target="_blank" href="'+d.pr.url+'">pull request #'+d.pr.number+"</a> awaiting editorial review.";}
  else{st.textContent="⚠️ "+(d.error||"submission failed");btn.disabled=false;}
});
load();
</script></body></html>`;
