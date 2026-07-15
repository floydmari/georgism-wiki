#!/usr/bin/env python3
"""
generate_related_boxes.py — Option 1 REPLACEMENT prototype (Floyd 2026-07-15):
precompiled per-article "From the Georgism Wiki" boxes, curated by GLM-5.2 on Ollama
Cloud with the FULL wiki catalog in context, instead of the theme's runtime
{{#get}} topic-tag query.

Why: runtime boxes are topic-coarse (7 buckets, newest-4) and cost a Ghost query on
every cache miss. Precompiled boxes are article-specific (the model reads the actual
essay against the whole wiki) and serve as static HTML.

Context strategy: the full wiki CATALOG (every page's slug | category | title |
excerpt — ~800 pages) fits comfortably in GLM-5.2's 1M window alongside the article.
(The wiki's full TEXT is ~1.6M+ tokens, beyond even 1M — the catalog's excerpts are
the right granularity: they say what each page argues, which is what relevance
selection needs.)

Delivery = Option A (Floyd's pick, 2026-07-15): the box lives in each post's
codeinjection_foot — per-post METADATA in the Ghost CMS, never in the body. Ghost's
{{ghost_foot}} emits it before </body> wrapped in an inert <template>; a 3-line inline
script relocates it into the theme's #wikiRelatedSlot (theme PR). Until the theme PR
merges there is no slot, so boxes stay invisible and the old runtime box keeps showing —
zero-downtime cutover. Existing codeinjection content (e.g. republished-by meta tags) is
preserved: only the marker-delimited segment is ever replaced.

Modes:
  --sample N / --slugs  generate previews to scratchpad/related-box-samples/ (no writes)
  --apply               write/refresh the marker segment in codeinjection_foot
  --changed             only articles new or updated since their last applied box
Cadence when live: daily --apply --changed; weekly --apply (full refresh, boxes surface
newly published wiki pages). CCR Routines for now; port to Hermes webmaster agents later.
"""
import argparse, glob, html, json, os, re, sys, threading, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "scratchpad", "cache")
ARTICLES = os.path.join(CACHE, "legacy-articles.jsonl")
SAMPLES = os.path.join(ROOT, "scratchpad", "related-box-samples")
STATE = os.path.join(ROOT, "sources", "related-box-state.jsonl")   # committed: Routine
                                                                   # sessions need it to
                                                                   # know what's current
MODEL = os.environ.get("RELATED_MODEL", "glm-5.2")
KEY = os.environ.get("OLLAMA_API_KEY")   # required only for generation, not --apply-existing

MARK_START = "<!-- wiki-related-precompiled v1 -->"
MARK_END = "<!-- /wiki-related-precompiled -->"

WIKI_DIRS = ["concepts", "people", "places", "events", "organizations", "objections",
             "problems", "benefits", "narratives", "books", "guides", "research", "texts"]


def catalog():
    import yaml
    rows = []
    for d in WIKI_DIRS:
        for p in sorted(glob.glob(os.path.join(ROOT, d, "*.md"))):
            slug = os.path.splitext(os.path.basename(p))[0]
            if slug.startswith("_"):
                continue
            m = re.match(r"^---\n(.*?)\n---\n", open(p, encoding="utf-8").read(), re.S)
            meta = yaml.safe_load(m.group(1)) if m else {}
            rows.append({"slug": slug, "cat": d, "title": meta.get("title", slug),
                         "excerpt": (meta.get("excerpt") or "")[:220]})
    return rows


def article_text(html_body, cap=20000):
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html_body, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()[:cap]


PROMPT = """You curate the "From the Georgism Wiki" box shown under an essay on progress.org.

FULL WIKI CATALOG ({n} pages), format: slug | category | title | excerpt
{catalog}

ESSAY: {title}
{text}

Pick the 4 or 5 wiki pages a reader of THIS essay would most want next — pages that deepen,
evidence, or honestly challenge what this essay argues. Prefer specificity over popularity:
an essay on Pittsburgh's split-rate tax wants the Pittsburgh/Oates-Schwab pages, not the
generic Georgism page. Include at most one person/place page unless the essay is a profile.
If the essay is genuinely off-topic for the wiki (no meaningful matches), return an empty list.
Reply ONLY JSON: {{"picks": [{{"slug": "...", "reason": "one reader-facing clause, max 15 words"}}]}}"""


def glm(prompt):
    if not KEY:
        sys.exit("OLLAMA_API_KEY not set (needed for box generation)")
    body = json.dumps({"model": MODEL, "stream": False, "think": False,
                       "messages": [{"role": "user", "content": prompt}],
                       "options": {"temperature": 0.1, "num_ctx": 262144}}).encode()
    req = urllib.request.Request("https://ollama.com/api/chat", data=body, headers={
        "Content-Type": "application/json", "Authorization": f"Bearer {KEY}"})
    content = json.loads(urllib.request.urlopen(req, timeout=900).read())["message"]["content"]
    m = re.search(r"\{.*\}", content, re.S)
    if not m:
        raise ValueError(f"no JSON in reply: {content[:120]!r}")
    return json.loads(m.group(0))


def render_box(picks, bytitle):
    lis = "\n".join(
        f'    <li><a href="https://www.progress.org/wiki/{p["slug"]}/">'
        f'{html.escape(bytitle[p["slug"]])}</a>'
        + (f' — {html.escape(p["reason"])}' if p.get("reason") else "") + "</li>"
        for p in picks)
    return f"""{MARK_START}
<aside class="wiki-related-card" data-precompiled="1">
  <h4>From the Georgism Wiki</h4>
  <ul>
{lis}
  </ul>
  <p class="wiki-related-more">
    <a href="/wiki/start-here/">Start here</a> ·
    <a href="/wiki/evidence-dashboard/">Evidence dashboard</a> ·
    <a href="/wiki/how-we-verify/">How we verify</a>
  </p>
</aside>
{MARK_END}"""


def deliverable(box_html):
    """Wrap the box for codeinjection_foot: inert <template> + relocation script.
    Ghost emits this before </body>; the script moves it into the theme's slot
    (theme PR adds <div id="wikiRelatedSlot"></div> where the runtime box was).
    Before the theme change ships, no slot exists and nothing is shown."""
    return (f"{MARK_START}<template data-wiki-related-pre>{box_html}</template>"
            "<script>(function(){var t=document.querySelector('template[data-wiki-related-pre]'),"
            "s=document.getElementById('wikiRelatedSlot');"
            "if(t&&s){s.appendChild(t.content.cloneNode(true));}})();</script>"
            f"{MARK_END}")


def replace_marker_segment(existing, segment):
    """Idempotently install/refresh our segment, preserving any other content
    (some posts carry republished-by meta tags in the same field)."""
    existing = existing or ""
    pat = re.compile(re.escape(MARK_START) + r".*?" + re.escape(MARK_END), re.S)
    if pat.search(existing):
        return pat.sub(lambda _: segment, existing)
    return (existing + "\n" if existing.strip() else "") + segment


def ghost_headers():
    from _secrets import require_ghost as _rg
    key, _ = _rg()
    kid, sec = key.split(":")
    import jwt as _jwt
    iat = int(time.time())
    tok = _jwt.encode({"iat": iat, "exp": iat + 300, "aud": "/admin/"},
                      bytes.fromhex(sec), algorithm="HS256",
                      headers={"alg": "HS256", "typ": "JWT", "kid": kid})
    return {"Authorization": f"Ghost {tok}"}


def apply_box(gurl, art_slug, segment, stats, lock):
    import requests
    r = requests.get(f"{gurl}/ghost/api/admin/posts/slug/{art_slug}/",
                     headers=ghost_headers(), timeout=60)
    if r.status_code != 200:
        with lock: stats["errors"].append(f"{art_slug}: GET {r.status_code}")
        return False
    p = r.json()["posts"][0]
    new_foot = replace_marker_segment(p.get("codeinjection_foot"), segment)
    if new_foot == (p.get("codeinjection_foot") or ""):
        with lock: stats["unchanged"] += 1
        return True
    pr = requests.put(f"{gurl}/ghost/api/admin/posts/{p['id']}/",
                      json={"posts": [{"codeinjection_foot": new_foot,
                                       "updated_at": p["updated_at"]}]},
                      headers=ghost_headers(), timeout=60)
    if pr.status_code != 200:
        with lock: stats["errors"].append(f"{art_slug}: PUT {pr.status_code} {pr.text[:80]}")
        return False
    # verify: body untouched, field carries our segment
    v = requests.get(f"{gurl}/ghost/api/admin/posts/{p['id']}/",
                     headers=ghost_headers(), timeout=60).json()["posts"][0]
    if MARK_START not in (v.get("codeinjection_foot") or ""):
        with lock: stats["errors"].append(f"{art_slug}: verify failed")
        return False
    with lock: stats["applied"] += 1
    return True


def load_state():
    state = {}
    if os.path.exists(STATE):
        for line in open(STATE):
            try:
                d = json.loads(line); state[d["article"]] = d
            except Exception:
                pass
    return state


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", type=int)
    ap.add_argument("--slugs", nargs="*")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--apply-existing", action="store_true",
                    help="apply already-generated previews from related-box-samples/ "
                         "without re-calling the model")
    ap.add_argument("--changed", action="store_true")
    ap.add_argument("--workers", type=int, default=6)
    args = ap.parse_args()

    if args.apply_existing:
        from _secrets import require_ghost
        _, gurl = require_ghost(); gurl = gurl.rstrip("/")
        lock = threading.Lock()
        stats = {"applied": 0, "unchanged": 0, "errors": []}
        files = sorted(glob.glob(os.path.join(SAMPLES, "*.html")))
        if args.slugs:
            files = [f for f in files
                     if os.path.splitext(os.path.basename(f))[0] in set(args.slugs)]
        print(f"applying {len(files)} pre-generated boxes")
        for i, fn in enumerate(files, 1):
            slug = os.path.splitext(os.path.basename(fn))[0]
            apply_box(gurl, slug, deliverable(open(fn).read().strip()), stats, lock)
            if i % 50 == 0:
                print(f"  … {i}/{len(files)} ({stats['applied']} applied)")
            time.sleep(0.3)
        print(json.dumps({k: (len(v) if isinstance(v, list) else v)
                          for k, v in stats.items()}))
        for e in stats["errors"][:10]:
            print("ERR:", e)
        return

    cat = catalog()
    bytitle = {r["slug"]: r["title"] for r in cat}
    cat_str = "\n".join(f'{r["slug"]} | {r["cat"]} | {r["title"]} | {r["excerpt"]}' for r in cat)
    print(f"catalog: {len(cat)} wiki pages (~{len(cat_str)//4} tokens); model={MODEL}")

    arts = [json.loads(l) for l in open(ARTICLES)]
    if args.slugs:
        arts = [a for a in arts if a["slug"] in set(args.slugs)]
    elif args.sample:
        arts = arts[: args.sample]
    if args.changed:
        state = load_state()
        arts = [a for a in arts if a["slug"] not in state
                or (a.get("updated_at") or "") > state[a["slug"]].get("article_updated_at", "")]
        print(f"--changed: {len(arts)} articles new/updated since last box")

    gurl = None
    if args.apply:
        from _secrets import require_ghost
        _, gurl = require_ghost(); gurl = gurl.rstrip("/")

    os.makedirs(SAMPLES, exist_ok=True)
    lock = threading.Lock()
    stats = {"ok": 0, "empty": 0, "applied": 0, "unchanged": 0, "errors": []}

    def work(chunk):
        for a in chunk:
            try:
                out = glm(PROMPT.format(n=len(cat), catalog=cat_str, title=a["title"],
                                        text=article_text(a["html"])))
                picks = [p for p in (out.get("picks") or [])
                         if isinstance(p, dict) and p.get("slug") in bytitle][:5]
                if not picks:
                    with lock:
                        stats["empty"] += 1
                        print(f"  ∅ {a['slug']}: off-topic, no box")
                    continue
                box = render_box(picks, bytitle)
                open(os.path.join(SAMPLES, f"{a['slug']}.html"), "w").write(box + "\n")
                if args.apply:
                    apply_box(gurl, a["slug"], deliverable(box), stats, lock)
                with lock:
                    stats["ok"] += 1
                    with open(STATE, "a") as f:
                        f.write(json.dumps({"date": time.strftime("%Y-%m-%d"),
                                            "article": a["slug"],
                                            "article_updated_at": a.get("updated_at"),
                                            "picks": picks, "model": MODEL,
                                            "applied": bool(args.apply)}) + "\n")
                    if stats["ok"] % 25 == 0:
                        print(f"  … {stats['ok']} boxes ({stats['applied']} applied)")
            except Exception as e:
                with lock: stats["errors"].append(f"{a['slug']}: {str(e)[:120]}")
                time.sleep(2)

    n = max(1, args.workers)
    chunks = [arts[i::n] for i in range(n)]
    threads = [threading.Thread(target=work, args=(c,)) for c in chunks if c]
    for t in threads: t.start()
    for t in threads: t.join()
    print(json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in stats.items()}))
    for e in stats["errors"][:10]:
        print("ERR:", e)


if __name__ == "__main__":
    main()
