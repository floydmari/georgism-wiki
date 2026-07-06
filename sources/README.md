# sources/ — the registry of what built the wiki

This directory separates two things that had drifted into one CSV (Floyd,
2026-07-06):

## `registry.csv` — SOURCES ONLY

Every **external work scanned to build the wiki**: academic papers, books,
public-domain primary texts, datasets, government/institutional reports, and
organization sites. Nothing the wiki itself authored belongs here.

This is the **regeneration-critical artifact**. A source's identity is
`Title + Author(s) + Year + URL` — *not* any wiki slug. The `Wiki Page` column
is a **"where it ended up" annotation** for the current build, never part of a
source's identity. That page-agnosticism is deliberate: point a fresh loop at
`registry.csv` and it can rebuild — or rebuild *differently*, to compare loop
strategies — the wiki from the same inputs, even though the new build's slugs
will differ. A well-maintained sources file is the experiment's control group.

Columns: `Title, Category, Author(s), Status, Wiki Page, Scan Depth,
In-Wiki Citations, Year, Tier, Format, URL`.

- **Status** — `Scanned` / `Not scanned` / `Referenced` / drift markers.
- **Scan Depth** — how thoroughly the source was mined (`Heavy`/`Medium`/`Light`);
  tracks Tier per EDITORIAL §3's Scan-Depth policy.
- **Tier** — `Core` / `Important` / `Supplementary`.
- **URL** — the free/legal external location. **Empty URL = a real work with no
  reachable free copy** (the acquisition backlog), *not* a wiki self-reference.
- Rows lacking a URL are still sources (a book we haven't got a free e-copy of);
  they are never wiki pages.

Public-domain **`texts/` pages are sources** and must each have a row here, with
their external provenance URL (Gutenberg / Internet Archive / Hansard /
cooperative-individualism.org, …) — the wiki reproduces the work, so the work is
a primary source. `lint_wiki.py` enforces one source row per `texts/` page.

## `wiki-inventory.csv` — A PAGE CENSUS (generated)

A **census of every page the wiki contains** — one row per page, across all
categories — computed live from the repo for analysis. It is **generated**, not
hand-maintained: run `scripts/build_inventory.py` to (re)build it. It carries no
source/provenance bookkeeping (no "scanned", no scan-depth); those belong to
sources. Columns:

`slug, title, category, url, inbound_links, outbound_links, words, stub, orphan,
last_reviewed`

- **inbound_links** — distinct other pages that link here (the backlink / demand
  metric). **outbound_links** — distinct pages this page links to.
- **words** — body word count, an objective size/depth proxy.
- **orphan** — `inbound_links == 0`.

Because it is a pure function of the repo, it is fully regenerable and safe for a
GitHub Action to rebuild on every push, outside the drafting loops
(`.github/workflows/wiki-inventory.yml`).

## How they relate

The two files are **independent**. `registry.csv` (sources) is the provenance /
regeneration input; `wiki-inventory.csv` (census) is page-level analytics. A page
that is itself a source — a `research/`, `books/`, or `texts/` page — appears in
both: as a source row in `registry.csv` and as a page row in the census. That
overlap is intended; they answer different questions.

`lint_wiki.py` reads only `registry.csv` for its source checks, plus it:
- **guards against the hybrid** — warns if any `registry.csv` row is a synthesis
  category with no external URL (a wiki page masquerading as a source);
- **checks census completeness** — warns if a page is missing from the census
  (run `build_inventory.py`).

## Tools

- `python3 scripts/build_inventory.py` — rebuild the page census. `--check`
  exits non-zero if it is stale (CI-friendly).
- `python3 scripts/seed_registry.py` — regenerate `registry.csv` from scratch by
  walking source-category pages (research / organizations / books / texts) plus
  the curated external list, then rebuilds the census. It only ever writes source
  rows to `registry.csv`, so it cannot recreate the hybrid.
- `python3 scripts/export_registry_for_sheet.py` — dated export of `registry.csv`
  for the Google-Sheet mirror (the repo file remains the registry of record).

## Provenance

The registry began as a Google Sheet
(`docs.google.com/spreadsheets/d/1RhL17YCzqNKmUf1IfLFOJyuF3c5DZ1YSCljdHv2RQQY`)
whose original rows were sources with a "where used" annotation. The git file is
now the source of truth; this README restores that original intent after the
hybrid drift.
