# BACKLOG.md — Wiki Improvement Queue

The loop's work source and persistent memory. One task per line:
`- [ ] [TYPE] tier:T1|T2|T3 status:todo|in-progress|needs-review|done — description`

TYPEs: `RECONCILE` `CROSSLINK` `BULK` `DRAFT` `DEEPEN` `CITE` `DESIGN` `JUDGE` `REVIEW` `UPDATE` `AUDIT`.
Work top-down within your tier. Append discovered follow-ups; never silently drop scope.
Target metrics: articles 139→300+, research 47→100+, concepts 22→40+, outcomes 13→25+,
narratives 0→12+, thin→0, claim-level citations→100%, cross-links 3+out/2+in.

---

## Phase 0 — Foundation (infrastructure) ✅ built this session
- [x] [DESIGN] tier:T1 status:done — EDITORIAL.md constitution (claim taxonomy, source hierarchy, templates, WS8)
- [x] [DESIGN] tier:T1 status:done — QUALITY_RUBRIC.md
- [x] [BULK] tier:T3 status:done — scripts/lint_wiki.py (stdlib-only quality gate)
- [x] [BULK] tier:T3 status:done — scripts/build_preview.py (local review surface)
- [x] [BULK] tier:T3 status:done — sources/registry.csv seeded (scripts/seed_registry.py)
- [x] [BULK] tier:T3 status:done — sync_to_ghost.py narratives category; .gitignore; narratives/ dir
- [x] [DESIGN] tier:T1 status:done — LOOP.md tier-aware loop prompt

## Standing rule — Google Sheet mirror of the source registry
Any task that edits `sources/registry.csv` must sync the master Google Sheet per LOOP.md step 3
(export via `scripts/export_registry_for_sheet.py`, then Drive snapshot or a loud [SHEET-SYNC] task
here). Last synced: **2026-07-03** — snapshot "Georgism Wiki — Source Registry (git sync 2026-07-03)"
created in Floyd's Drive (166 rows; Δ column marks 13 NEW + 4 UPDATED/CORRECTED from loops 1–7).
- [ ] [SHEET-SYNC] tier:T3 status:todo — durable write-back: once a Google service-account JSON is
      in the Emma vault (per the 1Password/op plumbing) and the master Sheet is shared with that
      service account as Editor, write `scripts/sync_registry_to_sheet.py` to update the master
      Sheet in place via the Sheets API each REVIEW-loop iteration (replaces dated snapshots).

## Phase 0 — remaining (needs credentials, not Fable)
- [ ] [RECONCILE] tier:T3 status:todo — Backfill the 6 Common Wealth Canada pages missing from git
      (common-wealth-canada, natural-common-wealth-economic-rent-canada, british-columbia,
      cwc-distributional-impacts-lvt, cwc-lvt-price-reaction-model, common-wealth-fund) via
      `scripts/pull_from_ghost.py` once GHOST_ADMIN_KEY is set; then review frontmatter/citations,
      update registry Status Scanned, and remove the drift rows from seed_registry EXTERNAL list.

## Phase 1 — Raw material (research + concepts)  [depends on: Phase 0]
- [ ] [DRAFT] tier:T2 status:todo — research: Mirrlees Review "Tax by Design" (2011) evidence page
- [ ] [DRAFT] tier:T2 status:todo — research: Foldvary, *Public Revenue Without Taxation* (1994)
- [ ] [DRAFT] tier:T2 status:todo — research: Ryan-Collins et al., *Rethinking … Land and Housing* (2017)
- [ ] [DRAFT] tier:T2 status:todo — research: OECD land/property tax reports (recent)
- [ ] [DRAFT] tier:T2 status:todo — research: "Not scanned" registry rows — Effects of Split-Rate
      Taxation (2022), Building Tax Capacity for Development (IMF 2025), Arbitrary Lines, Order
      Without Design, Escaping the Housing Trap  (one page each)
- [ ] [DRAFT] tier:T2 status:todo — research: complete Gaffney / Tideman / Hudson / Stiglitz coverage
      against the registry (fill gaps toward research 47→100+)
- [ ] [DRAFT] tier:T2 status:todo — concepts: Site Value, Law of Rent, Boom-Bust Cycle, Betterment
      Levy, Tiebout Model, Land Value Capture, EBCOR, Rentier, Land Speculation, Land Bubble,
      Marginal Productivity, Land as Commons  (toward concepts 22→40+)
- [ ] [BULK] tier:T3 status:todo — scan remaining registry sources; set Scan Depth / Status / citations

## Phase 2 — Linkage (outcomes + narratives)  [depends on: Phase 1]
- [x] [DESIGN] tier:T1 status:done — Narrative framework designed (narratives/_framework.md): 12-narrative
      taxonomy, evidence-status map, slug convention, deployment notes. Exemplar shipped:
      narratives/unearned-increment-narrative.md.
- [ ] [DRAFT] tier:T2 status:todo — narratives: 11 remaining pages per narratives/_framework.md
      (tax-land-not-labor; the-rentier-economy; community-creates-land-value; land-speculation-causes-cycles;
      the-housing-crisis-is-a-land-crisis; citizens-dividend-narrative; ecological-rent; the-tax-you-cant-dodge;
      the-corruption-of-economics; the-great-land-robbery; single-tax-narrative). Follow the exemplar's
      structure/sourcing density. NOTE per framework: `ecological-rent` needs sprawl/carbon-as-rent SOURCES
      first (T2 research); `the-corruption-of-economics` + `the-great-land-robbery` need a counter-source /
      enclosure-history page before drafting.
- [ ] [BULK] tier:T3 status:todo — wire inbound links INTO narrative pages as they ship (concept twins,
      relevant people/events/outcomes → "Narrative that uses this evidence" See Also links) so none orphan.
- [ ] [JUDGE] tier:T1 status:todo — For all 13 existing outcomes: set evidence_strength, add
      challenged_by where counter-evidence exists, verify supported_by resolves + is bidirectional
- [ ] [DRAFT] tier:T2 status:todo — 12 new outcome/evidence pages (reduces inequality; prevents
      boom-bust; funds Citizens Dividend; eliminates deadweight loss; progressive incidence;
      reduces speculation; funds public goods (HGT); hard to evade; reduces sprawl; …)
- [ ] [BULK] tier:T3 status:todo — wire supports_outcomes back-references across research pages

## Phase 3 — Depth, citations & polish
- [ ] [CITE] tier:T2 status:todo — Citation retrofit DRAFT pass, prioritized: all 8 objections, then
      13 outcomes, then theory concepts (ATCOR, deadweight-loss, henry-george-theorem,
      tax-capitalization), then flagships. Produce A–E report per page.
- [ ] [CITE] tier:T1 status:todo — Citation retrofit REVIEW pass: verify strength calibration,
      objection-steelmanning, theory-page framing on every [CITE tier:T2] output before publish.
- [ ] [DEEPEN] tier:T2 status:todo — expand the ~15 thin (<30-line) articles to full depth:
      alfred-russel-wallace, ground-rent, community-land-trust, common-ground-usa,
      earthsharing-australia, alanna-hartzok, dominic-frisby, akhil-patel, and the ~23-line
      research/podcast index pages
- [ ] [BULK] tier:T3 status:todo — complete cross-link graph (every page 3+ outbound / 2+ inbound);
      integrate the ~40 orphan pages (esp. orphaned research/ entries into narrative pages)
- [ ] [BULK] tier:T3 status:todo — add References/External-links sections + last_reviewed to every page
- [ ] [UPDATE] tier:T2 status:todo — staleness sweep: events/detroit-lvt-proposal.md and any
      "as of 202x" claims (current date 2026-07)
- [ ] [AUDIT] tier:T1 status:todo — rubric-score against success metrics; reprioritize this backlog
