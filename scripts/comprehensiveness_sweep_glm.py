#!/usr/bin/env python3
"""Phase 1 of LOOP-COMPREHENSIVENESS.md executed on a near-free external model (GLM on
Ollama Cloud via the local ollama server) instead of Claude subagents — session-quota cost: zero.

Per source (external registry row): fetch the source document directly (HTML or PDF via
pdftotext), read its research/ page for what's already extracted (orientation only), then ask
GLM for DISCOVERED candidates across all 8 categories + the authors channel, as strict JSON.

Honesty guard (LOOP.md external-model rule): the model is instructed to ground every candidate
in the supplied text; when the document could not be fetched, it may only propose
metadata-level candidates and must set confidence="low". Everything it returns is a CANDIDATE
for T1 triage — nothing is written to the wiki by this script.

Usage:
  python3 scripts/comprehensiveness_sweep_glm.py            # resume/run all
  python3 scripts/comprehensiveness_sweep_glm.py --limit 5  # smoke test
Output: preview/comprehensiveness_sweep_results.jsonl (one JSON object per source; resumable).
Requires: local `ollama` signed in to Ollama Cloud with the glm cloud model available;
`pdftotext` (poppler) optional but recommended.
"""
import json, os, re, subprocess, sys, tempfile, threading, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL = os.environ.get("SWEEP_MODEL", "glm-5.2:cloud")
OLLAMA = os.environ.get("OLLAMA_LOCAL", "http://localhost:11434")
BATCHES = os.path.join(ROOT, "preview/comprehensiveness_batches.json")
OUT = os.path.join(ROOT, "preview/comprehensiveness_sweep_results.jsonl")
WORKERS = int(os.environ.get("SWEEP_WORKERS", "3"))
MAX_DOC_CHARS = 45000            # light mode
DEEP_DOC_CHARS = 900000          # deep mode: whole books (GLM 1M-token window)
NUM_CTX = int(os.environ.get("SWEEP_NUM_CTX", "65536"))
DEEP_NUM_CTX = int(os.environ.get("SWEEP_DEEP_NUM_CTX", "1000000"))  # verified: 1M accepted, needles at 635k chars pass
DEEP = False

CATS = ["concepts", "people", "places", "organizations", "objections", "events", "outcomes", "narratives"]


def slug_list() -> str:
    out = []
    for c in CATS:
        for f in sorted(os.listdir(os.path.join(ROOT, c))):
            if f.endswith(".md"):
                out.append(f"{c}/{f[:-3]}")
    return "\n".join(out)


def corpus_digest() -> str:
    """Title + excerpt of every wiki page (~40k chars) — real-content dedupe for deep mode."""
    import glob
    out = []
    for c in CATS + ["research"]:
        for p in sorted(glob.glob(os.path.join(ROOT, c, "*.md"))):
            txt = open(p).read()
            m = re.search(r'^excerpt:\s*"?(.*?)"?\s*$', txt, re.M)
            out.append(f"{c}/{os.path.basename(p)[:-3]} — {(m.group(1) if m else '')[:180]}")
    return "\n".join(out)


def fetch(url: str) -> str:
    if not url:
        return ""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (georgism-wiki sweep)"})
        r = urllib.request.urlopen(req, timeout=30)
        data = r.read(6_000_000)
        ctype = (r.headers.get("Content-Type") or "").lower()
        if "pdf" in ctype or url.lower().endswith(".pdf"):
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tf:
                tf.write(data)
                path = tf.name
            try:
                txt = subprocess.run(["pdftotext", "-l", "400" if DEEP else "60", path, "-"], capture_output=True, timeout=180)
                return txt.stdout.decode("utf-8", "ignore")
            finally:
                os.unlink(path)
        text = data.decode("utf-8", "ignore")
        text = re.sub(r"<script.*?</script>|<style.*?</style>", " ", text, flags=re.S | re.I)
        text = re.sub(r"<[^>]+>", " ", text)
        return re.sub(r"\s+", " ", text)
    except Exception as e:
        return f"__FETCH_FAILED__ {e}"


def research_page(wiki_url: str) -> str:
    m = re.search(r"/wiki/([a-z0-9\-]+)/?$", wiki_url or "")
    if not m:
        return ""
    p = os.path.join(ROOT, "research", m.group(1) + ".md")
    return open(p).read()[:5000] if os.path.exists(p) else ""


SYSTEM = """You are a comprehensiveness scanner for a Georgism wiki. You receive ONE source
(metadata, what the wiki already extracted from it, and the document text when available).
Enumerate wiki-page candidates this source SUBSTANTIVELY treats (a section, recurring argument,
or documented case — never a passing name-drop) in these categories: concepts, people, places,
organizations, objections, events, outcomes, narratives.

Rules:
- A candidate must NOT already exist: check the provided existing-slug list (treat synonyms as
  existing) and the provided rejected/queued list.
- People bar: multiple contributions to the land-economics literature over time, or one core
  contribution plus sustained influence, or substantive discussion as a subject in this source.
- Ground every candidate in the supplied text; cite where (chapter/section/page). If document
  text is missing/failed, you may only propose metadata-level candidates with confidence "low".
- NEVER invent content, quotes, or page numbers.
Return STRICT JSON only:
{"discovered":[{"slug":"category/kebab-slug","category":"...","rationale":"1 line",
"where":"chapter/section/page or 'metadata-only'","confidence":"high|medium|low"}],
"authors_channel":[{"name":"...","why":"1 line"}],
"under_mined":{"flag":true/false,"why":"1 line"},
"near_misses":["1-line rejected considerations"]}
Maximum 6 discovered items, ranked. Empty arrays are fine and often correct."""


def glm(prompt: str) -> dict:
    body = json.dumps({
        "model": MODEL,
        "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}],
        "stream": False,
        "format": "json",
        "options": {"temperature": 0.2, "num_ctx": DEEP_NUM_CTX if DEEP else NUM_CTX},
    }).encode()
    for attempt in range(3):
        try:
            req = urllib.request.Request(OLLAMA + "/api/chat", data=body,
                                         headers={"Content-Type": "application/json"})
            r = urllib.request.urlopen(req, timeout=300)
            content = json.load(r)["message"]["content"]
            try:
                return json.loads(content)
            except Exception:
                m = re.search(r"\{.*\}", content, re.S)
                if m:
                    return json.loads(m.group(0))
                raise ValueError(f"unparseable content: {content[:300]!r}")
        except Exception as e:
            if attempt == 2:
                return {"error": str(e)[:300]}
            time.sleep(5 * (attempt + 1))


def main() -> None:
    global DEEP, OUT
    limit = None
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])
    DEEP = "--deep" in sys.argv
    data = json.load(open(BATCHES))
    sources = [s for b in data["batches"] for s in b]
    if DEEP:
        OUT = os.path.join(ROOT, "preview/comprehensiveness_sweep_deep.jsonl")
        under = {u["title"] for u in data.get("under_mined", [])}
        sources = [s for s in sources
                   if s["Title"] in under or (s.get("Tier", "").strip().lower() == "core")]
    done = set()
    if os.path.exists(OUT):
        for line in open(OUT):
            try:
                done.add(json.loads(line)["title"])
            except Exception:
                pass
    todo = [s for s in sources if s["Title"] not in done]
    if limit:
        todo = todo[:limit]
    slugs = slug_list()
    global DIGEST
    DIGEST = corpus_digest() if DEEP else ""
    backlog = open(os.path.join(ROOT, "BACKLOG.md")).read()
    queued = "\n".join(l for l in backlog.splitlines()
                       if re.search(r"\[(STUB|BACKFILL|DRAFT)\]|Rejected \(do not re-propose", l))[:6000]
    lock = threading.Lock()
    idx = {"i": 0}

    def worker():
        while True:
            with lock:
                if idx["i"] >= len(todo):
                    return
                s = todo[idx["i"]]
                idx["i"] += 1
            doc = fetch(s.get("URL", ""))
            fetched = not doc.startswith("__FETCH_FAILED__") and len(doc) > 500
            rp = research_page(s.get("Wiki Page", ""))
            prompt = (
                f"SOURCE METADATA: {json.dumps(s)}\n\n"
                + (f"FULL WIKI CORPUS DIGEST (title+excerpt of every page — use for real dedupe):\n{DIGEST}\n\n" if DEEP else "")
                + f"EXISTING WIKI SLUGS (do not re-propose):\n{slugs}\n\n"
                f"ALREADY QUEUED/REJECTED IN BACKLOG (do not re-propose):\n{queued}\n\n"
                f"WHAT THE WIKI ALREADY EXTRACTED (research page, orientation only):\n{rp or '(no dedicated research page)'}\n\n"
                f"DOCUMENT TEXT ({'fetched' if fetched else 'FETCH FAILED — metadata-only mode'}):\n"
                f"{doc[:(DEEP_DOC_CHARS if DEEP else MAX_DOC_CHARS)] if fetched else '(unavailable)'}"
            )
            res = glm(prompt)
            rec = {"title": s["Title"], "url": s.get("URL", ""), "fetched": fetched, "result": res}
            with lock:
                with open(OUT, "a") as f:
                    f.write(json.dumps(rec) + "\n")
                print(f"[{len(done) + idx['i']}/{len(sources)}] {s['Title'][:60]} "
                      f"fetched={fetched} discovered={len(res.get('discovered', []))}", flush=True)

    threads = [threading.Thread(target=worker) for _ in range(WORKERS)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    print("sweep complete ->", OUT)


if __name__ == "__main__":
    main()
