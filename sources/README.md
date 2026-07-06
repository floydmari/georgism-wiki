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

## `wiki-inventory.csv` — THE WIKI'S OWN PAGES

The synthesis pages the wiki *authored* — concepts, people, places, events,
outcomes, objections, narratives — with their inbound-citation (backlink) count,
scan depth, and drift status. This is page-level bookkeeping, and the right home
for "measure backlinks and such." It is **not** a list of sources; these rows
have no external URL by construction.

## How they relate

`lint_wiki.py` reads **both** files as one logical registry for its
duplicate / drift / broken-link checks, so nothing is lost by the split — but the
two are kept physically separate so `registry.csv` stays a clean, portable input
set. The classifier lives in one place (`scripts/split_registry.py`): a row is
wiki-inventory iff its Category is a synthesis type **and** it has no external URL.

## Tools

- `python3 scripts/split_registry.py` — re-partition both files from their
  current combined contents. **Idempotent** and **re-runnable**: run it after a
  content branch merges (which appends source rows in the old combined shape) to
  re-sort everything correctly. `--check` exits non-zero if a re-split would
  change anything (CI-friendly).
- `python3 scripts/seed_registry.py` — regenerate from scratch by walking the
  repo; it now partitions into both files at the end, so it cannot recreate the
  hybrid.
- `python3 scripts/export_registry_for_sheet.py` — dated export of `registry.csv`
  for the Google-Sheet mirror (the repo file remains the registry of record).

## Provenance

The registry began as a Google Sheet
(`docs.google.com/spreadsheets/d/1RhL17YCzqNKmUf1IfLFOJyuF3c5DZ1YSCljdHv2RQQY`)
whose original rows were sources with a "where used" annotation. The git file is
now the source of truth; this README restores that original intent after the
hybrid drift.
