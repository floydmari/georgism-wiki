# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

The Markdown **source of truth** for the Georgism & Land Value Taxation wiki at
[progress.org/wiki](https://www.progress.org/wiki/). It is a content repo, not a software
project: ~725 wiki pages in category folders, a source registry, and Python tooling
(stdlib-only where it matters) to lint, preview, and publish to Ghost CMS.

**Read `EDITORIAL.md` before writing or editing any wiki page.** It is the editorial
constitution — mission, claim taxonomy, citation rules, frontmatter schema, page
templates — and this file does not duplicate it. The other governance files:

- `LOOP.md` — the shift-by-shift improvement procedure (tiers, the flywheel, guardrails)
- `BACKLOG.md` — the prioritized task queue and persistent memory; start any work session
  from its **⟳ RESUME HERE** block
- `ROADMAP.md` — vision, work-stream status, exit criteria
- `QUALITY_RUBRIC.md` — 6-dimension scoring used in T1 review and audits
- `LOOPLOG.md` — descriptive history of what each loop iteration changed

## Commands

```bash
python3 scripts/lint_wiki.py                       # quality gate (zero deps); --strict promotes warnings to errors (CI mode)
python3 scripts/build_preview.py                   # render the branch to preview/
python3 -m http.server -d preview 8000             # browse the preview locally
python3 scripts/verification_queue.py              # rebuild sources/verification-queue.md + sources/hermes-workorder.md
python3 scripts/build_inventory.py                 # regenerate sources/wiki-inventory.csv (page census; CI checks it's current)
python3 scripts/export_registry_for_sheet.py       # dated registry export — required in any shift that edits registry.csv
python3 scripts/exa_enrich.py "<Name>"             # report-only enrichment pass; required before creating/backfilling people/ pages
python3 scripts/pull_from_ghost.py <folder> <slug> # reconcile a page that drifted on Ghost
python3 scripts/sync_to_ghost.py                   # PUBLISH to Ghost — Floyd's process, not the loop's; needs GHOST_ADMIN_KEY
```

There are no tests; `lint_wiki.py` is the gate. Run it before every commit — lint errors
block publish and CI (`.github/workflows/wiki-inventory.yml` runs lint + a census-currency
check on PRs).

## Architecture

### Content categories (folder = `category` frontmatter field, enforced by lint)

`concepts/` `people/` `places/` `events/` `organizations/` `objections/` `narratives/`
`books/` `texts/` — plus the three that form the evidence spine:

- `research/` — one page per external paper/study/dataset (the source index)
- `problems/` — evidence-backed diagnosis claims (`claim_type: problem`)
- `benefits/` — evidence-backed policy-effect claims (`claim_type: benefit`)

(`problems/` and `benefits/` replaced the old `outcomes/` in 2026-07-10; never create
`outcomes/` pages.)

### The linked-evidence graph

Claim pages (`problems/`, `benefits/`) carry `supported_by:` / `challenged_by:` lists of
research slugs; research pages carry the reverse `supports_outcomes:` link. **Lint enforces
bidirectionality** — adding one side without the other is an error. Evidence lists are
ordered strongest-first (EDITORIAL §3). Every page ends with `## See Also` (3+ cross-links)
and an annotated `## Sources` section, and needs ≥2 inbound links from other pages.

### The source registry

- `sources/registry.csv` — every external work used, one row each (identity =
  Title+Author+Year+URL; the `Wiki Page` column is only a "where used" note). Every source
  cited on any page must have a row. See `sources/README.md` for the full contract.
- `sources/wiki-inventory.csv` — the page census (backlinks, stubs, orphans); regenerated
  by CI on main.
- `sources/inbox/` — deliveries from the Hermes lane (book scans, verified quotes).
  **Process unconsumed inbox items before drafting anything new** (LOOP.md step 1).
- `sources/verification-queue.md` / `sources/hermes-workorder.md` — generated files; edit
  via `scripts/verification_queue.py`, not by hand.

## Non-negotiable editorial rules (full text: EDITORIAL.md §1)

1. **GitHub is the master record.** Commit and push first; Ghost publishing happens only
   afterward and only via `scripts/sync_to_ghost.py`.
2. **Never fabricate** a source, quote, author, date, DOI, or URL. Unverifiable claims get
   `[CITATION NEEDED: …]` or `[VERIFY: …]` markers — visible flags, never guesses.
3. **Never delete an article.** Mark it for review instead.
4. Neutral, encyclopedic tone (Wikipedia NPOV); citations are claim-level, not page-level.
5. ≤50 words quoted from any copyrighted work (public-domain `texts/` pages are exempt);
   free/legal source links only.
6. Banned-certainty words (`proves`, `always`, `clearly`, `undeniable`, …) unless the cited
   source justifies that strength — lint flags them.
7. **The rent gradient:** land is the clean, well-evidenced case; every step toward
   resource/monopoly/IP rents is more contested. Never let the land case's certainty bleed
   into frontier claims.

## Workflow conventions

- **Tiers are roles** (LOOP.md): T1 frontier model = editor and the only gate to main;
  T2 = drafting; T3 = mechanical bulk work. BACKLOG tasks are tagged `tier:T1|T2|T3`.
- **One task per shift, one task per commit**: `content: <what> (<TYPE> tier:T<n>)`.
- A shift ends at commit + push + preview. **Publishing to progress.org is Floyd's separate
  process** — never run `sync_to_ghost.py` as part of the loop.
- **Campsite rule:** every shift also resolves or routes ≥5 items of standing debt (open
  fact-check flags, thin pages, unannotated sources).
- **Before creating any stub**, check for existing coverage both ways: `ls <category>/` for
  slug variants AND a repo-wide grep for surname/title keywords (slugs lie; grep the words).
  Cap ~8 new stubs per shift. A stub needs full frontmatter, a 2–4 sentence sourced
  overview, ≥2 outbound links, ≥1 inbound link, and a real citation.
- **Delta rule:** before enriching an existing page, read it (and its linked evidence
  pages); add only what is genuinely new. One finding, one home, many links.
- Concurrency: ≤3–4 concurrent Claude subagents.

## Publishing to Ghost — the three silent-failure gotchas

Handled by `scripts/sync_to_ghost.py`; never hand-roll Admin API calls:

1. Append `?source=html` to create/update URLs when sending an `html` field, or Ghost
   silently drops the body.
2. Set `custom_template: "custom-wiki-entry"` on every wiki post, or it renders with the
   plain article template.
3. Primary tag must be `wiki` (first in the list) plus a `wiki-<category>` tag, or the post
   won't route to `/wiki/{slug}/`. Reference tags by Ghost `id`, never by name.

Credentials: `.claude/hooks/session-start.sh` loads `GHOST_ADMIN_KEY` from 1Password when
`OP_SERVICE_ACCOUNT_TOKEN` is set in the environment; without it the session is commit-only.
