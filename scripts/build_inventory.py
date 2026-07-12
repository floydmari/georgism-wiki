#!/usr/bin/env python3
"""
build_inventory.py — regenerate sources/wiki-inventory.csv as a full page census.

This file is NOT a source list (that is sources/registry.csv). It is a census of
every page the wiki contains, one row each, computed live from the repo — for
analysis: which pages are most linked (demand), which are orphans, how big each
is, what is still a stub. It carries no "scanned / scan-depth" bookkeeping — those
belong to sources, not to a page inventory (Floyd, 2026-07-06).

Because it is a pure function of the repo, it is fully regenerable and safe for a
GitHub Action to rebuild on every push (outside the drafting loops). Run:

    python3 scripts/build_inventory.py            # rewrite the census
    python3 scripts/build_inventory.py --check     # exit 1 if it is stale (CI)

Columns:
    slug, title, category, url, inbound_links, outbound_links, words, stub,
    orphan, last_reviewed
  - inbound_links  : number of DISTINCT other pages that link to this page
                     (the backlink / demand metric)
  - outbound_links : number of DISTINCT pages this page links to (self excluded)
  - words          : body word count (a size/depth proxy that needs no judgement)
  - orphan         : inbound_links == 0
"""
import csv
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "sources", "wiki-inventory.csv")
CATEGORIES = ["concepts", "people", "places", "events", "problems", "benefits", "research",
              "organizations", "objections", "narratives", "books", "texts", "guides"]
COLS = ["slug", "title", "category", "url", "inbound_links", "outbound_links",
        "words", "stub", "orphan", "last_reviewed"]
LINK_RE = re.compile(r"/wiki/([a-z0-9\-]+)/")
TITLE_RE = re.compile(r'^title:\s*"?(.*?)"?\s*$', re.M)
STUB_RE = re.compile(r'^stub:\s*(true|false)\s*$', re.M | re.I)
REVIEWED_RE = re.compile(r'^last_reviewed:\s*"?([0-9\-]+)"?\s*$', re.M)


def load_pages():
    pages = {}
    for cat in CATEGORIES:
        for path in glob.glob(os.path.join(ROOT, cat, "*.md")):
            slug = os.path.splitext(os.path.basename(path))[0]
            if slug.startswith("_"):
                continue
            text = open(path, encoding="utf-8").read()
            fm_end = text.find("\n---", 3)
            body = text[fm_end + 4:] if text.startswith("---") and fm_end != -1 else text
            head = text[:fm_end] if fm_end != -1 else ""
            t = TITLE_RE.search(head)
            s = STUB_RE.search(head)
            r = REVIEWED_RE.search(head)
            pages[slug] = {
                "cat": cat,
                "title": t.group(1) if t else slug,
                "stub": (s.group(1).lower() == "true") if s else False,
                "last_reviewed": r.group(1) if r else "",
                "out": {tgt for tgt in LINK_RE.findall(text) if tgt != slug},
                "words": len(body.split()),
            }
    return pages


def build_rows(pages):
    inbound = {s: set() for s in pages}
    for slug, p in pages.items():
        for tgt in p["out"]:
            if tgt in inbound:
                inbound[tgt].add(slug)
    rows = []
    for slug in sorted(pages):
        p = pages[slug]
        ins = len(inbound[slug])
        rows.append({
            "slug": slug,
            "title": p["title"],
            "category": p["cat"],
            "url": f"https://www.progress.org/wiki/{slug}/",
            "inbound_links": ins,
            "outbound_links": len([t for t in p["out"] if t in pages]),
            "words": p["words"],
            "stub": "true" if p["stub"] else "false",
            "orphan": "true" if ins == 0 else "false",
            "last_reviewed": p["last_reviewed"],
        })
    return rows


def render(rows):
    import io
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=COLS)
    w.writeheader()
    w.writerows(rows)
    return buf.getvalue()


def main():
    rows = build_rows(load_pages())
    text = render(rows)
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        stale = cur.replace("\r\n", "\n") != text.replace("\r\n", "\n")
        print("build_inventory --check:",
              "STALE (run scripts/build_inventory.py)" if stale else "current")
        sys.exit(1 if stale else 0)
    with open(OUT, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    orphans = sum(1 for r in rows if r["orphan"] == "true")
    print(f"wiki-inventory.csv -> {len(rows)} pages ({orphans} orphans)")


if __name__ == "__main__":
    main()
