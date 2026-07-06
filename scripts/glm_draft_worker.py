#!/usr/bin/env python3
"""Main-loop T2 drafting on GLM (Ollama Cloud) — replaces Claude subagents for volume work.

Reads a task file (JSON list) and, per task, drafts ONE wiki page with the 1M window used
strategically: full fetched source text (HTML/pdftotext, local egress) + the whole-corpus
digest (title+excerpt of every page, for real dedupe/cross-linking) + the category template
+ a quality exemplar. Runs N tasks in parallel threads at zero Claude session quota.
Output is DRAFTS ONLY (preview/glm_drafts/<slug>.md + report JSONL) — per LOOP.md's
external-model rule, T1 reviews (with grounding checks) before anything enters the wiki.

Task JSON schema (list of objects):
  {"path": "research/foo.md",            # file the draft targets
   "kind": "research|backfill|concept|narrative",
   "title": "...", "authors": "...", "year": "...", "tier": "...",
   "urls": ["https://..."],              # sources to fetch (first that yields text wins; all tried)
   "supports_outcomes": ["slug"],        # research only; [] if none/unsure
   "notes": "orchestrator guidance",
   "related": ["research/bar.md"]}       # corpus pages to include FULL TEXT of

Usage: python3 scripts/glm_draft_worker.py tasks.json [--workers 6]
"""
import json, os, re, subprocess, sys, tempfile, threading, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL = os.environ.get("SWEEP_MODEL", "glm-5.2:cloud")
OLLAMA = os.environ.get("OLLAMA_LOCAL", "http://localhost:11434")
NUM_CTX = int(os.environ.get("DRAFT_NUM_CTX", "300000"))
OUTDIR = os.path.join(ROOT, "preview/glm_drafts")
REPORT = os.path.join(ROOT, "preview/glm_drafts/report.jsonl")
CATS = ["concepts", "people", "places", "organizations", "objections", "events", "outcomes",
        "narratives", "research"]


def fetch(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (georgism-wiki)"})
        r = urllib.request.urlopen(req, timeout=30)
        data = r.read(8_000_000)
        if "pdf" in (r.headers.get("Content-Type") or "").lower() or url.lower().endswith(".pdf"):
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tf:
                tf.write(data); p = tf.name
            try:
                return subprocess.run(["pdftotext", "-l", "300", p, "-"], capture_output=True,
                                      timeout=120).stdout.decode("utf-8", "ignore")
            finally:
                os.unlink(p)
        t = re.sub(r"<script.*?</script>|<style.*?</style>", " ", data.decode("utf-8", "ignore"),
                   flags=re.S | re.I)
        return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t))
    except Exception as e:
        return f"__FETCH_FAILED__ {e}"


def digest():
    import glob as g
    out = []
    for c in CATS:
        for p in sorted(g.glob(os.path.join(ROOT, c, "*.md"))):
            m = re.search(r'^excerpt:\s*"?(.*?)"?\s*$', open(p).read(), re.M)
            out.append(f"{c}/{os.path.basename(p)[:-3]} — {(m.group(1) if m else '')[:150]}")
    return "\n".join(out)


SYSTEM = """You are a staff writer building the definitive, honest reference on Georgism and
land value taxation (progress.org/wiki) — read by skeptics as well as supporters, persuasive
only because it is accurate, sourced, and fair: evidence at its true strength, counterarguments
at theirs. You draft ONE page, per the supplied EDITORIAL rules, template
section, and exemplar. Ground EVERY substantive claim in the supplied source text or supplied
corpus pages; cite external sources (real URLs supplied only) at claim level; NEVER invent
findings, numbers, quotes, page numbers, or URLs — use [CITATION NEEDED: ...] / [VERIFY: ...].
If source text is missing, draft conservatively from metadata + corpus and mark markers heavily.
Quotes <=50 words. Wiki links: [Title](/wiki/slug/) — NO category prefix — only slugs from the
supplied corpus digest. Frontmatter per the schema for the category; research pages:
supports_outcomes exactly as assigned (drop with a note in 'REPORT' if the source honestly does
not support — honesty beats coverage). End page with ## See Also (3+) and annotated ## Sources.
Return STRICT JSON: {"content": "<full file>", "report": {"lint_expect": "...", "registry_row":
"Title,Category,Author(s),Status,Wiki Page,Scan Depth,In-Wiki Citations,Year,Tier,Format,URL",
"supports_outcomes_confirmed": [...], "markers": n, "inbound_link_suggestions": [...],
"discovered_candidates": [...]}}"""


def main():
    tasks = json.load(open(sys.argv[1]))
    workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 6
    os.makedirs(OUTDIR, exist_ok=True)
    done = set()
    if os.path.exists(REPORT):
        done = {json.loads(l)["path"] for l in open(REPORT)}
    todo = [t for t in tasks if t["path"] not in done]
    ed = open(os.path.join(ROOT, "EDITORIAL.md")).read()
    dig = digest()
    exemplar = open(os.path.join(ROOT, "research/mirrlees-review.md")).read()
    lock = threading.Lock(); idx = {"i": 0}

    def work():
        while True:
            with lock:
                if idx["i"] >= len(todo): return
                t = todo[idx["i"]]; idx["i"] += 1
            srcs = ""
            for u in t.get("urls", []):
                x = fetch(u)
                if not x.startswith("__FETCH_FAILED__") and len(x) > 800:
                    srcs += f"\n===== SOURCE TEXT ({u}) =====\n{x[:250000]}"
            rel = "".join(f"\n===== CORPUS PAGE: {r} =====\n{open(os.path.join(ROOT, r)).read()}"
                          for r in t.get("related", []) if os.path.exists(os.path.join(ROOT, r)))
            prompt = (f"TASK: {json.dumps({k: v for k, v in t.items() if k != 'related'})}\n\n"
                      f"EDITORIAL RULES (sections 1-6):\n{ed[:14000]}\n\nQUALITY EXEMPLAR"
                      f" (match depth/structure):\n{exemplar}\n\nCORPUS DIGEST (all pages —"
                      f" for links and dedupe):\n{dig}\n{rel}\n"
                      f"{srcs if srcs else chr(10) + '(no source text fetched — conservative mode)'}")
            body = json.dumps({"model": MODEL, "messages": [
                {"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}],
                "stream": False, "options": {"temperature": 0.3, "num_ctx": NUM_CTX}}).encode()
            res = {"error": "exhausted"}
            for a in range(3):
                try:
                    r = urllib.request.urlopen(urllib.request.Request(
                        OLLAMA + "/api/chat", data=body,
                        headers={"Content-Type": "application/json"}), timeout=900)
                    c = json.load(r)["message"]["content"]
                    try:
                        res = json.loads(c)
                    except Exception:
                        m = re.search(r"\{.*\}", c, re.S)
                        res = json.loads(m.group(0))
                    break
                except Exception as e:
                    res = {"error": str(e)[:200]}; time.sleep(8 * (a + 1))
            with lock:
                if "content" in res:
                    slug = os.path.basename(t["path"])
                    open(os.path.join(OUTDIR, slug), "w").write(res["content"])
                with open(REPORT, "a") as f:
                    f.write(json.dumps({"path": t["path"], "fetched": bool(srcs),
                                        "report": res.get("report", res.get("error"))}) + "\n")
                print(f"[{idx['i']}/{len(todo)}] {t['path']} fetched={bool(srcs)} "
                      f"ok={'content' in res}", flush=True)

    th = [threading.Thread(target=work) for _ in range(workers)]
    [x.start() for x in th]; [x.join() for x in th]
    print("drafting complete ->", OUTDIR)


if __name__ == "__main__":
    main()
