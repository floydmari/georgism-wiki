#!/usr/bin/env python3
"""
build_intext_manifest.py — Option 2, stage 1 (deterministic, no LLM, no writes anywhere).

Builds the RAW candidate manifest for in-text wiki links inside legacy /articles/ posts:
    (article -> phrase found -> wiki page it would link to -> context sentence)

Inputs:
    scratchpad/cache/legacy-articles.jsonl   (from scripts/fetch_legacy_articles.py)
    wiki content dirs (frontmatter titles)

Outputs:
    scratchpad/cache/intext_phrases.json     term -> {slug, title, folder}
    scratchpad/cache/intext_manifest.json    per-article candidates + existing /wiki/ links

Rules (recreates the 2026-07-13 session's approach, plus href-aware dedup):
  * Terms = frontmatter titles <= 4 words from non-research dirs (natural phrases:
    people, concepts, places, organizations, events, books, narratives, guides),
    minus a generic-word blacklist, plus a curated alias map validated against files.
  * Research paper titles ("Author (Year): ...") are noise, excluded.
  * Case-insensitive match on word boundaries; ALL-CAPS acronyms match case-sensitively.
  * Text inside existing <a>, <blockquote>, <h1>-<h6>, <code>, <pre> is unlinkable/off-limits.
  * An article never gets a candidate for a slug it ALREADY links to (href dedup).
  * One candidate per term per article (first occurrence).
NEXT STAGE: LLM pruning of wrong-sense/noise matches, then the human-review manifest.
Nothing is applied to Ghost until Floyd approves the manifest.
"""
import glob, html, json, os, re, sys, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "scratchpad", "cache")
ARTICLES = os.path.join(CACHE, "legacy-articles.jsonl")

TERM_DIRS = ["concepts", "people", "places", "events", "organizations",
             "objections", "problems", "benefits", "narratives", "books", "guides", "texts"]

# Titles that are real words but would link promiscuously or wrong-sense too often.
BLACKLIST = {
    "land", "rent", "tax", "taxation", "economics", "poverty", "housing", "wealth",
    "progress", "justice", "interest", "wages", "capital", "labor", "labour", "money",
    "value", "commons", "socialism", "china", "denmark", "australia", "canada", "taiwan",
    "singapore", "estonia", "kenya", "namibia", "start here", "united states",
}

# phrase -> repo-relative target ("folder/slug"); validated below, bad entries are fatal.
ALIASES = {
    "land value tax":            "concepts/land-value-tax",
    "land value taxation":       "concepts/land-value-tax",
    "land-value tax":            "concepts/land-value-tax",
    "single tax":                "concepts/single-tax",
    "citizens dividend":         "concepts/citizens-dividend",
    "citizen's dividend":        "concepts/citizens-dividend",
    "henry george theorem":      "concepts/henry-george-theorem",
    "economic rent":             "concepts/economic-rent",
    "ground rent":               "concepts/ground-rent",
    "ground rents":              "concepts/ground-rent",
    "split-rate tax":            "concepts/split-rate-taxation",
    "split rate tax":            "concepts/split-rate-taxation",
    "land speculation":          "concepts/land-speculation",
    "deadweight loss":           "concepts/deadweight-loss",
    "all taxes come out of rent": "concepts/atcor",
    "progress and poverty":      "books/progress-and-poverty",
    "sovereign wealth fund":     "concepts/sovereign-wealth-fund",
    "sovereign wealth funds":    "concepts/sovereign-wealth-fund",
    "community land trust":      "concepts/community-land-trust",
    "community land trusts":     "concepts/community-land-trust",
    "georgist":                  "concepts/georgism",
    "georgists":                 "concepts/georgism",
    "geoism":                    "concepts/georgism",
    "geoist":                    "concepts/georgism",
    "land value capture":        "concepts/land-value-capture",
    "value capture":             "concepts/land-value-capture",
    "congestion pricing":        "concepts/congestion-pricing",
    "resource rents":            "concepts/resource-rents",
    "rent seeking":              "concepts/rent-seeking",
    "rent-seeking":              "concepts/rent-seeking",
    "18-year cycle":             "concepts/18-year-land-cycle",
    "18-year land cycle":        "concepts/18-year-land-cycle",
    "18 year cycle":             "concepts/18-year-land-cycle",
    "law of rent":               "concepts/law-of-rent",
}


def frontmatter(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return yaml.safe_load(m.group(1)) if m else {}


def build_dictionary():
    pages = {}          # "folder/slug" -> title
    for d in TERM_DIRS + ["research"]:
        for p in glob.glob(os.path.join(ROOT, d, "*.md")):
            slug = os.path.splitext(os.path.basename(p))[0]
            if slug.startswith("_"):
                continue
            t = (frontmatter(p) or {}).get("title") or ""
            if t:
                pages[f"{d}/{slug}"] = t

    terms = {}          # phrase(lower unless acronym) -> target key
    for key, title in pages.items():
        folder = key.split("/")[0]
        if folder == "research":
            continue                                   # paper-title noise
        words = title.split()
        if not (1 <= len(words) <= 4):
            continue
        if re.search(r"\(\d{4}\)", title):
            continue
        phrase = title.strip().rstrip("?.").strip()
        if phrase.lower() in BLACKLIST:
            continue
        if len(phrase) < 4:                            # 'Rey', ambiguous ultra-shorts
            continue
        if phrase in terms:
            continue                                   # first dir wins (TERM_DIRS order):
                                                       # people/henry-george beats the
                                                       # Barker biography book page whose
                                                       # title is also "Henry George"
        terms[phrase] = key

    missing = [a for a, tgt in ALIASES.items() if tgt not in pages]
    for a in missing:
        print(f"  (alias skipped, no such page: {a} -> {ALIASES[a]})")
    for a, tgt in ALIASES.items():
        if tgt in pages:
            terms[a] = tgt
    return pages, terms


# NOTE: existing <a> tags are NOT stripped — their inner text stays so context sentences
# read naturally. Same-target duplicates are prevented by href dedup below; text already
# inside a (different-target) link is skipped again at APPLY time by the lexical surgery,
# which only touches plain text nodes.
STRIP_TAGS = re.compile(
    r"<blockquote\b[^>]*>.*?</blockquote>|<h[1-6][^>]*>.*?</h[1-6]>"
    r"|<code[^>]*>.*?</code>|<pre[^>]*>.*?</pre>|<figcaption[^>]*>.*?</figcaption>",
    re.S | re.I)


def linkable_text(html_body):
    t = re.sub(STRIP_TAGS, " ", html_body)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    return re.sub(r"[ \t]+", " ", t)


def existing_wiki_slugs(html_body):
    return sorted(set(re.findall(r'href="[^"]*?/wiki/([a-z0-9-]+)/?[#"?]', html_body)))


def sentence_around(text, start, end):
    left = max(text.rfind(". ", 0, start), text.rfind("\n", 0, start),
               text.rfind("? ", 0, start), text.rfind("! ", 0, start))
    right_candidates = [i for i in (text.find(". ", end), text.find("\n", end),
                                    text.find("? ", end), text.find("! ", end)) if i != -1]
    right = min(right_candidates) if right_candidates else min(len(text), end + 200)
    return text[left + 1:right + 1].strip()[:400]


def main():
    pages, terms = build_dictionary()
    print(f"dictionary: {len(terms)} phrases -> {len(set(terms.values()))} wiki pages")
    json.dump({t: {"target": k, "title": pages[k]} for t, k in sorted(terms.items())},
              open(os.path.join(CACHE, "intext_phrases.json"), "w"), indent=1)

    # compile one regex per phrase; acronyms (all-caps) stay case-sensitive
    compiled = []
    for phrase, key in terms.items():
        if phrase.isupper():
            rx = re.compile(rf"\b{re.escape(phrase)}\b")
        else:
            rx = re.compile(rf"\b{re.escape(phrase)}(s)?\b", re.I)
        compiled.append((phrase, key, rx))
    compiled.sort(key=lambda x: -len(x[0]))            # longest phrase wins overlaps

    manifest, total = [], 0
    for line in open(ARTICLES, encoding="utf-8"):
        art = json.loads(line)
        text = linkable_text(art["html"])
        already = existing_wiki_slugs(art["html"])
        already_set = set(already)
        claimed = []                                   # (start,end) spans already used
        cands = []
        for phrase, key, rx in compiled:
            slug = key.split("/", 1)[1]
            if slug in already_set:
                continue
            m = rx.search(text)
            if not m:
                continue
            if any(s < m.end() and m.start() < e for s, e in claimed):
                continue                               # inside a longer phrase already taken
            if key.split("/")[0] != "people":
                pass
            claimed.append((m.start(), m.end()))
            already_set.add(slug)                      # one candidate per target per article
            cands.append({
                "phrase": phrase, "matched": m.group(0),
                "target": key, "wiki_title": pages[key],
                "sentence": sentence_around(text, m.start(), m.end()),
            })
            total += 1
        manifest.append({
            "slug": art["slug"], "url": art["url"], "title": art["title"],
            "published_at": art.get("published_at"),
            "existing_wiki_links": already,
            "candidates": cands,
        })

    out = os.path.join(CACHE, "intext_manifest.json")
    json.dump(manifest, open(out, "w"), indent=1)
    withc = [a for a in manifest if a["candidates"]]
    counts = sorted(len(a["candidates"]) for a in withc)
    med = counts[len(counts)//2] if counts else 0
    print(f"raw manifest: {total} candidates across {len(withc)}/{len(manifest)} articles "
          f"(median {med}/article) -> {out}")


if __name__ == "__main__":
    main()
