#!/usr/bin/env python3
"""
build_concept_manifest.py — Option 3, stage 1 (external model, no Claude quota, NO edits).

Conceptual interlinking: Option 2 linked simple entities (people, places, concepts, orgs).
This maps each legacy article to the CLAIM pages — problems/, benefits/, objections/ (+
narratives/) — it substantively bears on, which needs reading comprehension, not phrase
matching. Runs on Floyd's Ollama Cloud (key: 1Password item 'ollama cloud'), model
glm-4.7 by default (his pick: "Gemma or GLM 4.7 flash" — override with CONCEPT_MODEL).

Per article: article text (truncated) + the full claim-page catalog -> the model returns
up to 4 mappings {claim slug, relation supports|illustrates|counters, anchor phrase (exact
words from the article), anchor sentence, why}. Output is a JSONL of candidates for the
stage-2 review manifest (render_concept_manifest.py). Per LOOP.md's external-model rule,
nothing from this script touches the wiki or Ghost without review.

Usage:
  export OLLAMA_API_KEY=$(op read "op://<vault>/<item>/credential")
  python3 scripts/build_concept_manifest.py [--limit N] [--workers 8]
Resumable: skips article slugs already present in the output JSONL.
"""
import argparse, glob, json, os, re, sys, threading, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "scratchpad", "cache")
ARTICLES = os.path.join(CACHE, "legacy-articles.jsonl")
OUT = os.path.join(CACHE, "concept-candidates.jsonl")
MODEL = os.environ.get("CONCEPT_MODEL", "glm-4.7")
API = os.environ.get("OLLAMA_HOST", "https://ollama.com")
KEY = os.environ.get("OLLAMA_API_KEY") or sys.exit("OLLAMA_API_KEY not set")

CLAIM_DIRS = ["problems", "benefits", "objections", "narratives"]


def frontmatter(path):
    import yaml
    m = re.match(r"^---\n(.*?)\n---\n", open(path, encoding="utf-8").read(), re.S)
    return yaml.safe_load(m.group(1)) if m else {}


def claim_catalog():
    rows = []
    for d in CLAIM_DIRS:
        for p in sorted(glob.glob(os.path.join(ROOT, d, "*.md"))):
            slug = os.path.splitext(os.path.basename(p))[0]
            if slug.startswith("_") or slug in ("the-problems", "the-benefits"):
                continue
            meta = frontmatter(p) or {}
            t, ex = meta.get("title", slug), (meta.get("excerpt") or "")[:180]
            rows.append(f"{d}/{slug} | {t} | {ex}")
    return rows


def article_text(html_body, cap=9000):
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html_body, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    import html as h
    t = re.sub(r"\s+", " ", h.unescape(t)).strip()
    return t[:cap]


PROMPT = """You are mapping an essay from progress.org to the claim pages of the Georgism wiki.

CLAIM PAGE CATALOG (id | title | summary), one per line:
{catalog}

ESSAY TITLE: {title}
ESSAY TEXT (may be truncated):
{text}

Task: identify AT MOST 4 claim pages this essay SUBSTANTIVELY bears on — where the essay
argues, evidences, illustrates, or disputes that page's claim. Substantive means a reader
of that passage would genuinely benefit from the wiki page; do not map on shared topic
alone. For each mapping give:
- "claim": the catalog id exactly as written (e.g. "benefits/lvt-improves-housing-affordability")
- "relation": "supports" | "illustrates" | "counters"
- "anchor_phrase": 2-8 EXACT CONSECUTIVE WORDS copied verbatim from the essay text where a
  hyperlink would sit naturally (the conceptual heart of the passage, not a heading)
- "anchor_sentence": the full sentence containing that phrase, verbatim
- "why": one short clause explaining the bearing
Fewer, stronger mappings beat many weak ones. Zero mappings is a valid answer.

Reply with ONLY a JSON object: {{"mappings": [ ... ]}}"""


def call_model(prompt):
    # glm-4.7 is a thinking model: format:"json" leaves content empty (it all goes to
    # .thinking), so ask for plain output with think off and extract the JSON block.
    body = json.dumps({
        "model": MODEL, "stream": False, "think": False,
        "messages": [{"role": "user", "content": prompt}],
        "options": {"temperature": 0.1, "num_ctx": 16384},
    }).encode()
    req = urllib.request.Request(API + "/api/chat", data=body, headers={
        "Content-Type": "application/json", "Authorization": f"Bearer {KEY}"})
    r = urllib.request.urlopen(req, timeout=600)
    content = json.loads(r.read())["message"]["content"]
    m = re.search(r"\{.*\}", content, re.S)
    if not m:
        raise ValueError(f"no JSON object in model reply: {content[:120]!r}")
    return m.group(0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int)
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()

    catalog = claim_catalog()
    print(f"claim catalog: {len(catalog)} pages; model={MODEL}")
    cat_ids = {r.split(" | ")[0] for r in catalog}
    cat_str = "\n".join(catalog)

    done = set()
    if os.path.exists(OUT):
        for line in open(OUT):
            try:
                done.add(json.loads(line)["slug"])
            except Exception:
                pass

    arts = [json.loads(l) for l in open(ARTICLES)]
    todo = [a for a in arts if a["slug"] not in done]
    if args.limit:
        todo = todo[: args.limit]
    print(f"articles: {len(todo)} to process ({len(done)} already done)")

    lock = threading.Lock()
    counters = {"ok": 0, "err": 0, "maps": 0}

    def work(chunk):
        for a in chunk:
            try:
                raw = call_model(PROMPT.format(catalog=cat_str, title=a["title"],
                                               text=article_text(a["html"])))
                data = json.loads(raw)
                maps = data.get("mappings", []) or []
                clean = []
                text_l = article_text(a["html"], cap=100000).lower()
                for m in maps[:4]:
                    if not isinstance(m, dict) or m.get("claim") not in cat_ids:
                        continue
                    ph = (m.get("anchor_phrase") or "").strip()
                    grounded = bool(ph) and ph.lower() in text_l
                    clean.append({"claim": m["claim"],
                                  "relation": m.get("relation", "supports"),
                                  "anchor_phrase": ph, "grounded": grounded,
                                  "anchor_sentence": (m.get("anchor_sentence") or "")[:400],
                                  "why": (m.get("why") or "")[:200]})
                with lock:
                    with open(OUT, "a") as f:
                        f.write(json.dumps({"slug": a["slug"], "title": a["title"],
                                            "url": a["url"], "model": MODEL,
                                            "mappings": clean}) + "\n")
                    counters["ok"] += 1; counters["maps"] += len(clean)
                    if counters["ok"] % 25 == 0:
                        print(f"  {counters['ok']} articles, {counters['maps']} mappings")
            except Exception as e:
                with lock:
                    counters["err"] += 1
                    print(f"  ERR {a['slug']}: {str(e)[:120]}")
                time.sleep(2)

    n = max(1, args.workers)
    chunks = [todo[i::n] for i in range(n)]
    threads = [threading.Thread(target=work, args=(c,)) for c in chunks if c]
    for t in threads: t.start()
    for t in threads: t.join()
    print(json.dumps(counters))


if __name__ == "__main__":
    main()
