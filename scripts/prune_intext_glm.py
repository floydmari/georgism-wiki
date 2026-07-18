#!/usr/bin/env python3
"""
prune_intext_glm.py — entity-link pruning on GLM-5.2 (Ollama Cloud), replacing the
2026-07-14 Haiku fan-out. Crucial difference (Floyd, 2026-07-15, after the 18.6-year
article spot-check): NO numeric cap. The Haiku pass's "keep at most 6" threw away 197
genuine entity links fleet-wide (Patel, Gaffney, Ryan-Collins, Gordon Brown ... all
over-cap in that one article). Drop ONLY genuine noise:
  wrong-sense | byline/credit | footnote/citation | inside-quote | incidental-place | garbled
Everything else keeps. People/organizations/books/events links are the point — a reader
should be able to click every substantive name.

Reads  scratchpad/cache/intext_manifest.json  (raw candidates, already deduped against
live links), writes  scratchpad/cache/pruned-delta/chunk-glm.json  in the same format
the Haiku chunks used, so render_intext_manifest.py consumes it via PRUNED_DIR.

Usage:
  export OLLAMA_API_KEY=...
  python3 scripts/prune_intext_glm.py [--workers 4] [--limit N]
Resumable per-article (skips slugs already in the output).
"""
import argparse, json, os, re, sys, threading, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "scratchpad", "cache")
RAW = os.path.join(CACHE, "intext_manifest.json")
OUTDIR = os.path.join(CACHE, "pruned-delta")
OUT = os.path.join(OUTDIR, "chunk-glm.json")
MODEL = os.environ.get("PRUNE_MODEL", "glm-5.2")
KEY = os.environ.get("OLLAMA_API_KEY") or sys.exit("OLLAMA_API_KEY not set")

PROMPT = """You are vetting candidate hyperlinks for a progress.org article (Georgist economics site).
Article: {title}
Candidates (phrase | wiki target | context sentence):
{cands}

KEEP every genuine link — especially people, organizations, books, and events with wiki
pages; readers should be able to click every substantive name. There is NO limit on keeps.
DROP only real noise:
- wrong-sense: the phrase means something else here (e.g. "Progress and Poverty" as a
  newsletter name, not the 1879 book)
- byline: author bylines, bio blurbs, "originally published on...", event boilerplate
- footnote: the sentence is a footnote/endnote/bibliography citation
- quote: the phrase sits inside quoted matter
- incidental-place: place names where the article does not substantively discuss that
  place's land/tax/economy ("he moved to Chicago" — drop; "Chicago's 1836 land boom" — keep)
- garbled: context too broken to judge

Reply ONLY JSON: {{"keep": [{{"phrase": "...", "target": "..."}}],
"dropped": [{{"phrase": "...", "target": "...", "why": "wrong-sense|byline|footnote|quote|incidental-place|garbled"}}]}}
Every candidate must appear in exactly one list."""


def glm(prompt):
    body = json.dumps({"model": MODEL, "stream": False, "think": False,
                       "messages": [{"role": "user", "content": prompt}],
                       "options": {"temperature": 0.1}}).encode()
    req = urllib.request.Request("https://ollama.com/api/chat", data=body, headers={
        "Content-Type": "application/json", "Authorization": f"Bearer {KEY}"})
    content = json.loads(urllib.request.urlopen(req, timeout=600).read())["message"]["content"]
    m = re.search(r"\{.*\}", content, re.S)
    if not m:
        raise ValueError(f"no JSON: {content[:100]!r}")
    return json.loads(m.group(0))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--limit", type=int)
    args = ap.parse_args()

    os.makedirs(OUTDIR, exist_ok=True)
    done, results = set(), []
    if os.path.exists(OUT):
        results = json.load(open(OUT))
        done = {r["slug"] for r in results}

    arts = [a for a in json.load(open(RAW)) if a["candidates"] and a["slug"] not in done]
    if args.limit:
        arts = arts[: args.limit]
    print(f"pruning {len(arts)} articles ({len(done)} already done); model={MODEL}")

    lock = threading.Lock()
    stats = {"ok": 0, "err": 0, "keep": 0, "drop": 0}

    def work(chunk):
        for a in chunk:
            cands = "\n".join(f"{c['matched']} | {c['target']} | {c['sentence'][:180]}"
                              for c in a["candidates"])
            try:
                out = glm(PROMPT.format(title=a["title"], cands=cands))
                keep = [k for k in out.get("keep", []) if isinstance(k, dict)]
                drop = [d for d in out.get("dropped", []) if isinstance(d, dict)]
                with lock:
                    results.append({"slug": a["slug"], "keep": keep, "dropped": drop})
                    stats["ok"] += 1; stats["keep"] += len(keep); stats["drop"] += len(drop)
                    json.dump(results, open(OUT, "w"), indent=1)
                    if stats["ok"] % 25 == 0:
                        print(f"  … {stats['ok']} articles ({stats['keep']} keep / {stats['drop']} drop)", flush=True)
            except Exception as e:
                with lock:
                    stats["err"] += 1
                    print(f"  ERR {a['slug']}: {str(e)[:100]}", flush=True)
                time.sleep(2)

    n = max(1, args.workers)
    chunks = [arts[i::n] for i in range(n)]
    threads = [threading.Thread(target=work, args=(c,)) for c in chunks if c]
    for t in threads: t.start()
    for t in threads: t.join()
    print(json.dumps(stats))


if __name__ == "__main__":
    main()
