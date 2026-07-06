#!/usr/bin/env python3
"""
split_registry.py — separate the SOURCES registry from the WIKI INVENTORY.

Background (Floyd, 2026-07-06): sources/registry.csv had drifted into a hybrid —
part list of external sources scanned to build the wiki, part inventory of the
wiki's own pages. The tell: ~82 rows were synthesis pages (Concepts, People,
Events, Outcomes, Objections, Places, Narratives) with NO external URL, their only
link a progress.org/wiki self-reference and their "In-Wiki Citations" really a
backlink count. A source registry must not cite the wiki as its own source.

This script partitions the combined data into two physical files:

  sources/registry.csv        — SOURCES ONLY: the external works (papers, books,
                                primary texts, datasets, gov/inst reports, org
                                sites) that were read to build the wiki. This is
                                the regeneration-critical artifact: point a fresh
                                loop at it to rebuild — or re-build differently —
                                the wiki from the same inputs. The "Wiki Page"
                                column is a *where-it-ended-up* annotation, never
                                part of a source's identity (Title+Author+Year+URL).

  sources/wiki-inventory.csv  — the wiki's own pages: slug, category, inbound-
                                citation (backlink) count, scan depth, drift status.
                                This is where page-level bookkeeping lives.

Both files keep the same 11-column header so lint_wiki.load_registry() can read
them as one logical registry (no check changes). The split is about human
navigability and the regenerate-from-sources use case, not about hiding data.

IDEMPOTENT + RE-RUNNABLE: reads registry.csv AND (if present) wiki-inventory.csv,
re-pools every row, re-classifies, and rewrites both. Running twice is a no-op;
running after a content branch appends rows in the old hybrid shape re-sorts them
correctly. Run it at merge time whenever the campaign branch lands.

Classification rule (deterministic — 0 ambiguous rows as of 2026-07-06):
    a row is WIKI INVENTORY iff  Category in SYNTHESIS_CATS  AND  URL is empty.
    every other row is a SOURCE (including Historical/Primary Text and books or
    papers that simply lack a free e-copy — those are real works, just unlinked).

Usage:  python3 scripts/split_registry.py [--check]
        --check : exit 1 if a re-split would change either file (for CI)
"""
import csv
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY = os.path.join(ROOT, "sources", "registry.csv")
INVENTORY = os.path.join(ROOT, "sources", "wiki-inventory.csv")

COLS = ["Title", "Category", "Author(s)", "Status", "Wiki Page", "Scan Depth",
        "In-Wiki Citations", "Year", "Tier", "Format", "URL"]

# Synthesis page types the wiki AUTHORS (not external sources). A row in one of
# these categories with no external URL is the wiki citing itself — inventory.
SYNTHESIS_CATS = {"Concepts", "Outcomes", "Objections", "People", "Places",
                  "Events", "Narratives"}


def read_rows(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        return [dict(r) for r in csv.DictReader(fh)]


def is_wiki_inventory(row):
    cat = (row.get("Category") or "").strip()
    url = (row.get("URL") or "").strip()
    return cat in SYNTHESIS_CATS and not url


def normalize(row):
    return {c: (row.get(c) or "").strip() for c in COLS}


def dedupe(rows):
    """Collapse rows sharing (Title, Author). Prefer the variant that carries a
    URL, then the one with the more thorough Scan Depth."""
    depth_rank = {"heavy": 3, "medium": 2, "light": 1, "": 0, "—": 0}
    best = {}
    order = []
    for r in rows:
        key = (r["Title"].lower(), r["Author(s)"].lower())
        if key not in best:
            best[key] = r
            order.append(key)
        else:
            cur = best[key]
            cand_better = (bool(r["URL"]) > bool(cur["URL"])) or (
                bool(r["URL"]) == bool(cur["URL"]) and
                depth_rank.get(r["Scan Depth"].lower(), 0) >
                depth_rank.get(cur["Scan Depth"].lower(), 0))
            if cand_better:
                best[key] = r
    return [best[k] for k in order]


def write_csv(path, rows):
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)


def main():
    pool = [normalize(r) for r in read_rows(REGISTRY) + read_rows(INVENTORY)]
    sources = dedupe([r for r in pool if not is_wiki_inventory(r)])
    inventory = dedupe([r for r in pool if is_wiki_inventory(r)])
    sources.sort(key=lambda r: r["Title"].lower())
    inventory.sort(key=lambda r: r["Wiki Page"].lower() or r["Title"].lower())

    if "--check" in sys.argv:
        def current(path):
            # compare row content, newline-agnostic (avoid \r\n vs \n false positives)
            return read_rows(path)
        want_src = [dict(r) for r in sources]
        want_inv = [dict(r) for r in inventory]
        changed = (current(REGISTRY) != want_src) or (current(INVENTORY) != want_inv)
        print("split_registry --check:", "CHANGES NEEDED" if changed else "clean")
        sys.exit(1 if changed else 0)

    write_csv(REGISTRY, sources)
    write_csv(INVENTORY, inventory)
    print(f"sources/registry.csv     -> {len(sources)} source rows")
    print(f"sources/wiki-inventory.csv -> {len(inventory)} wiki-page rows")


if __name__ == "__main__":
    main()
