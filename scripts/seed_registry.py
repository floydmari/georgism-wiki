#!/usr/bin/env python3
"""
seed_registry.py — build sources/registry.csv from the repo + known external sources.

Run once to seed; thereafter the wiki loop maintains the CSV directly (and mirrors it to the
Google Sheet). Regenerating is safe — it rebuilds repo-derived rows and re-appends the curated
external rows below. Idempotent.

Columns mirror the master Google Sheet:
  Title, Category, Author(s), Status, Wiki Page, Scan Depth, In-Wiki Citations, Year, Tier, Format, URL
"""
import os, csv, glob, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lint_wiki import parse_frontmatter, aslist  # reuse the stdlib frontmatter reader

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "sources", "registry.csv")
COLS = ["Title", "Category", "Author(s)", "Status", "Wiki Page", "Scan Depth",
        "In-Wiki Citations", "Year", "Tier", "Format", "URL"]

# Only these page categories represent EXTERNAL WORKS and belong in the sources
# file. Synthesis pages (concepts, people, events, outcomes, objections, places,
# narratives) are wiki-authored — they live in the page census (wiki-inventory.csv,
# built by scripts/build_inventory.py), never in registry.csv.
SOURCE_CATS = {"research": "Academic/Research", "organizations": "Website/Org",
               "books": "Modern Book", "texts": "Primary Text"}
FORMAT_BY_CAT = {"research": "Paper", "organizations": "Website/Org",
                 "books": "Book", "texts": "Text"}


def wiki_url(slug):
    return f"https://www.progress.org/wiki/{slug}/"


def count_citations(slug, all_text):
    return sum(t.count(f"/wiki/{slug}/") for t in all_text)


def repo_rows():
    files = {}
    texts = []
    for cat in SOURCE_CATS:
        for path in glob.glob(os.path.join(ROOT, cat, "*.md")):
            slug = os.path.splitext(os.path.basename(path))[0]
            text = open(path, encoding="utf-8").read()
            meta, _ = parse_frontmatter(text)
            files[slug] = (cat, meta or {}, path)
            texts.append(text)

    rows = []
    for slug, (cat, meta, path) in sorted(files.items()):
        # Source rows only (SOURCE_CATS). The URL comes from the page's own
        # frontmatter provenance; a source with no free copy keeps an empty URL
        # (acquisition backlog) but is still a source, never a wiki-inventory row.
        rows.append({
            "Title": meta.get("title", slug),
            "Category": SOURCE_CATS[cat],
            "Author(s)": "; ".join(aslist(meta.get("authors"))) if meta.get("authors") else "",
            "Status": "Scanned",
            "Wiki Page": wiki_url(slug),
            "Scan Depth": "Medium",
            "In-Wiki Citations": count_citations(slug, texts),
            "Year": meta.get("year", ""),
            "Tier": meta.get("tier", ""),
            "Format": meta.get("format", FORMAT_BY_CAT[cat]),
            "URL": meta.get("source_url") or meta.get("url") or "",
        })
    return rows


# Curated external sources / drift not (yet) in git. Keep this list in sync with the Sheet.
# CWC cluster = live on Ghost per the source Sheet but MISSING from git (Status marks drift so
# lint warns rather than errors until the [RECONCILE] task pulls them back via pull_from_ghost.py).
EXTERNAL = [
    # --- Common Wealth Canada cluster: DRIFT — live on Ghost, absent from git ---
    ("Common Wealth Canada", "Website/Org", "", "MISSING_FROM_GIT (drift)",
     "https://www.progress.org/wiki/common-wealth-canada/", "Medium", 0, "ongoing",
     "Important", "Website", "https://commonwealth.ca/"),
    ("Natural Common Wealth and Economic Rent in Canada", "Online Writing", "", "MISSING_FROM_GIT (drift)",
     "https://www.progress.org/wiki/natural-common-wealth-economic-rent-canada/", "Medium", 0,
     "2023", "Important", "Report", "https://commonwealth.ca/report"),
    ("B.C. Has Been Here Before: Land Value Taxation in British Columbia", "Online Writing", "",
     "MISSING_FROM_GIT (drift)", "https://www.progress.org/wiki/british-columbia/", "Medium", 0,
     "2026", "Important", "Article", "https://commonwealth.ca/blog/history-of-bc"),
    ("Assessing the Distributional Impacts of a Land Value Tax", "Online Writing", "",
     "MISSING_FROM_GIT (drift)", "https://www.progress.org/wiki/cwc-distributional-impacts-lvt/",
     "Medium", 0, "2024", "Supplementary", "Report", "https://commonwealth.ca/research/distributional-impacts"),
    ("Modeling the Price Reaction to the Implementation of a Land Value Tax", "Online Writing", "",
     "MISSING_FROM_GIT (drift)", "https://www.progress.org/wiki/cwc-lvt-price-reaction-model/",
     "Medium", 0, "2024", "Supplementary", "Report", "https://commonwealth.ca/research/lvt-sensitivity-analysis"),
    ("The Common Wealth Fund", "Online Writing", "", "MISSING_FROM_GIT (drift)",
     "https://www.progress.org/wiki/common-wealth-fund/", "Medium", 0, "2024",
     "Supplementary", "Report", "https://commonwealth.ca/fund"),
    # --- "Not scanned" sources from the Sheet: integration backlog, no page yet ---
    ("Effects of Split-Rate Taxation on Tax Base", "Academic Paper", "", "Not scanned",
     "", "—", 0, "2022", "Important", "Paper", ""),
    ("Building Tax Capacity for Development", "Academic Paper", "IMF", "Not scanned",
     "", "—", 0, "2025", "Supplementary", "Paper",
     "https://www.imf.org/-/media/files/publications/dp/2025/english/btcgdea.pdf"),
    ("Arbitrary Lines: How Zoning Broke the American City", "Modern Book", "M. Nolan Gray",
     "Not scanned", "", "—", 0, "2022", "Supplementary", "Book",
     "https://islandpress.org/books/arbitrary-lines"),
    ("Order Without Design: How Markets Shape Cities", "Modern Book", "Alain Bertaud",
     "Not scanned", "", "—", 0, "2018", "Supplementary", "Book",
     "https://mitpress.mit.edu/9780262550970/order-without-design/"),
    ("Escaping the Housing Trap: The Strong Towns Response", "Modern Book",
     "Charles Marohn; Daniel Herriges", "Not scanned", "", "—", 0, "2024",
     "Supplementary", "Book", ""),
    ("The Mirrlees Review: Tax by Design", "Academic Paper", "IFS / James Mirrlees et al.",
     "Not scanned", "", "—", 0, "2011", "Core", "Report",
     "https://ifs.org.uk/books/tax-design"),
    ("Public Revenue Without Taxation", "Modern Book", "Fred Foldvary", "Not scanned",
     "", "—", 0, "1994", "Important", "Book", ""),
    ("Rethinking the Economics of Land and Housing", "Modern Book",
     "Josh Ryan-Collins; Toby Lloyd; Laurie Macfarlane", "Not scanned", "", "—", 0, "2017",
     "Important", "Book", "https://neweconomics.org/2017/02/rethinking-economics-land-housing"),
]


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    rows = repo_rows()
    for e in EXTERNAL:
        rows.append(dict(zip(COLS, e)))
    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)
    print(f"seed_registry: wrote {len(rows)} source rows to {os.path.relpath(OUT, ROOT)}")
    # The page census is a separate, regenerated artifact — rebuild it too so a
    # from-scratch reseed leaves both files current. See sources/README.md.
    # NOTE: texts/ pages carry provenance as prose (`provenance:`); confirm each
    # Text row has an external URL after a reseed — lint's texts-source-row check
    # flags any gap.
    import build_inventory
    build_inventory.main()


if __name__ == "__main__":
    main()
