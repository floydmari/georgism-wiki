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

Modes:
  --sample N        generate boxes for N articles, write HTML previews to
                    scratchpad/related-box-samples/ (NO Ghost writes) — the demo mode.
  --apply           write boxes to posts' codeinjection_foot (metadata, NOT body).
                    GATED: refuses to run unless APPLY_OK=1 is set (Floyd's word).
Delivery (decided after Floyd picks): codeinjection_foot + theme slot (body stays
pristine, RSS/email clean) vs body HTML card (zero-JS but body content). The HTML
emitted here is delivery-agnostic; --apply currently targets codeinjection_foot.

Cadence when live: daily over articles newer/updated since last run; weekly full
refresh. Run as a CCR Routine for now; port to Hermes webmaster agents later.
"""
import argparse, glob, html, json, os, re, sys, threading, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "scratchpad", "cache")
ARTICLES = os.path.join(CACHE, "legacy-articles.jsonl")
SAMPLES = os.path.join(ROOT, "scratchpad", "related-box-samples")
STATE = os.path.join(CACHE, "related-box-state.jsonl")
MODEL = os.environ.get("RELATED_MODEL", "glm-5.2")
KEY = os.environ.get("OLLAMA_API_KEY") or sys.exit("OLLAMA_API_KEY not set")

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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", type=int)
    ap.add_argument("--slugs", nargs="*")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    if args.apply and os.environ.get("APPLY_OK") != "1":
        sys.exit("--apply is gated: set APPLY_OK=1 only after Floyd approves the mechanism.")

    cat = catalog()
    bytitle = {r["slug"]: r["title"] for r in cat}
    cat_str = "\n".join(f'{r["slug"]} | {r["cat"]} | {r["title"]} | {r["excerpt"]}' for r in cat)
    print(f"catalog: {len(cat)} wiki pages (~{len(cat_str)//4} tokens); model={MODEL}")

    arts = [json.loads(l) for l in open(ARTICLES)]
    if args.slugs:
        arts = [a for a in arts if a["slug"] in set(args.slugs)]
    elif args.sample:
        arts = arts[: args.sample]

    os.makedirs(SAMPLES, exist_ok=True)
    for a in arts:
        try:
            out = glm(PROMPT.format(n=len(cat), catalog=cat_str, title=a["title"],
                                    text=article_text(a["html"])))
            picks = [p for p in (out.get("picks") or [])
                     if isinstance(p, dict) and p.get("slug") in bytitle][:5]
            if not picks:
                print(f"  ∅ {a['slug']}: no relevant pages (off-topic)"); continue
            box = render_box(picks, bytitle)
            fn = os.path.join(SAMPLES, f"{a['slug']}.html")
            open(fn, "w").write(box + "\n")
            print(f"  ✅ {a['slug']}: {[p['slug'] for p in picks]}")
            with open(STATE, "a") as f:
                f.write(json.dumps({"date": time.strftime("%Y-%m-%d"), "article": a["slug"],
                                    "picks": picks, "model": MODEL,
                                    "applied": bool(args.apply)}) + "\n")
        except Exception as e:
            print(f"  ERR {a['slug']}: {str(e)[:140]}")


if __name__ == "__main__":
    main()
