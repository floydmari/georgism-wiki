# BACKLOG.md — Wiki Improvement Queue

## ⟳ RESUME HERE (checkpoint 2026-07-04, evidence build-out in progress)
State: 174 pages, lint green, coverage **41/65** (gauge prints on every `lint_wiki.py` run).
Waves 1–2 of the 50-paper build-out are done (15 pages: PFD cluster, capitalization cluster,
incidence trio, efficiency trio, Knoll, Cunningham, Hsieh-Moretti, De Loecker). A fresh session resumes with:
0a. **FLYWHEEL NOW ACTIVE** (see LOOP.md "growth flywheel"): every loop stubs its discoveries in
   ALL categories; `[PRIORITIZE] tier:T1` ranks the Stub queue each wave; backfills re-mine the
   corpus via tasks/backfill-page-task.md. Lint prints a STUBS gauge.
0. **FIRST: [SYNTHESIS] tier:T1 — catch-up harvest over waves 1-2, CREATE STUBS** (the discovery channel was
   missing while 16 sources were ingested). Known candidates already surfaced by agents:
   outcomes/corporate-profits-increasingly-rents (queued below; De Loecker+Barkai+Furman evidence);
   objections/cash-transfers-reduce-work (Jones-Marinescu counters it); objections/zoning-not-lvt-
   is-the-binding-constraint (Hsieh-Moretti implies; pairs with housing-affordability honesty);
   concepts/land-credit-cycle (Hudson+Ryan-Collins+Knoll mechanism); concepts/option-value-of-land
   (Cunningham); possibly concepts/benefit-view-of-property-tax (Hamilton/Tiebout cluster).
   Triage each: create, queue, or reject-with-reason. Then:
1. `git status` — commit any straggler agent output (a Brueckner site-value draft may be in the
   working tree or missing; if missing, redraft from the queue below). Check for neutralized
   forward-links to restore (grep the last commits for "neutralized").
2. Run the next waves from the unchecked `[DRAFT]` items below via `tasks/research-page-task.md`
   (8-9 parallel T2 agents on disjoint files; T1 reviews each: registry row + bidirectional
   supported_by/challenged_by + inbound links + lint green + commit per batch).
   Priority order: speculation cluster (2/5), split-rate (2/5), affordability (3/5),
   land-value scale (3/5), progressivity (3/5), then the tech-rents cluster + its NEW outcome
   page outcomes/corporate-profits-increasingly-rents.md (T1 writes that one).
3. Per-wave wrap-up: registry delta → Drive Sheet snapshot (mandatory-loud rule), LOOPLOG entry,
   preview rebuild + artifact redeploy (same URL).
4. Stop when the COVERAGE gauge reads 14/14 ≥5 (incl. the new tech-rents outcome).
Done so far (checked off below): jones-marinescu, widerquist-howard, hartwick, segal, oates-1969,
gibbons-machin, mohammad, hsieh-moretti, de-loecker, oecd-taxation, arnold-ej, mieszkowski,
hamilton (challenger), zodrow, knoll, cunningham.

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
here). Last synced: **2026-07-03 (wave 3 delta pushed same day)** — full snapshot "Georgism Wiki — Source Registry (git sync 2026-07-03)" + delta sheet "Wave 3 delta"
created in Floyd's Drive (166 rows; Δ column marks 13 NEW + 4 UPDATED/CORRECTED from loops 1–7).
- [ ] [SHEET-SYNC] tier:T3 status:todo — durable write-back: once a Google service-account JSON is
      in the Emma vault (per the 1Password/op plumbing) and the master Sheet is shared with that
      service account as Editor, write `scripts/sync_registry_to_sheet.py` to update the master
      Sheet in place via the Sheets API each REVIEW-loop iteration (replaces dated snapshots).

- [ ] [SHEET-SYNC] tier:T3 status:todo — push registry export to the master Google Sheet (last synced: 2026-07-03 wave-3 delta; ~18 rows added since — run scripts/export_registry_for_sheet.py --base 34b56cf and upload via Drive)

## Stub queue (flywheel intake — stubs created at discovery, ranked by [PRIORITIZE])
- [ ] [PRIORITIZE] tier:T1 status:recurring — each wave: rank stubs below by (a) inbound-link
      demand from existing pages, (b) evidence already in the ingested corpus, (c) citing-source
      tier; move the top 3-5 into [BACKFILL] tasks (tasks/backfill-page-task.md).
(queue currently empty — the wave 1-2 catch-up synthesis seeds it; see RESUME step 0)

## Evidence-base build-out: 50 research pages until every outcome has ≥5 papers
Standard task file: `tasks/research-page-task.md`. Format: slug — Author Year *Title* (tier) → supports_outcomes.
Progress gauge: `lint_wiki.py` COVERAGE block. Termination: 14/14 outcomes ≥5.
**Capitalization** (→ public-investment-capitalizes-into-land):
- [ ] [DRAFT] tier:T2 — oates-1969-capitalization — Oates 1969 (core)
- [ ] [DRAFT] tier:T2 — gibbons-machin-rail-access — Gibbons & Machin 2005 (important)
- [ ] [DRAFT] tier:T2 — mohammad-rail-meta-analysis — Mohammad et al. 2013 (important)
- [ ] [DRAFT] tier:T2 — albouy-what-are-cities-worth — Albouy 2016 (core; also land-rent-could-fund-government)
- [ ] [DRAFT] tier:T2 — davis-heathcote-us-land — Davis & Heathcote 2007 (important)
**Land value scale** (→ land-rent-could-fund-government):
- [ ] [DRAFT] tier:T2 — larson-us-land-value — Larson 2015 BEA (core)
- [ ] [DRAFT] tier:T2 — albouy-ehrlich-shin-metro-land — Albouy, Ehrlich & Shin 2018 (important)
**Capital share** (→ capital-share-rise-is-land):
- [ ] [DRAFT] tier:T2 — knoll-schularick-steger-house-prices — Knoll et al. 2017 AER (core)
- [ ] [DRAFT] tier:T2 — la-cava-housing-capital-share — La Cava 2016 (important)
- [ ] [DRAFT] tier:T2 — piketty-capital-21st-century — Piketty 2014 (core; context for Rognlie)
- [ ] [DRAFT] tier:T2 — barkai-declining-shares — Barkai 2020 (important; also challenged_by on capital-share + supports corporate-profits-increasingly-rents)
**Efficiency** (→ lvt-can-replace-capital-taxes-without-efficiency-loss):
- [ ] [DRAFT] tier:T2 — oecd-taxation-economic-growth — Johansson et al. 2008 (core)
- [ ] [DRAFT] tier:T2 — arnold-tax-growth-ej — Arnold et al. 2011 EJ (important)
- [ ] [DRAFT] tier:T2 — brueckner-site-value-taxation — Brueckner 1986 (core)
**Construction/split-rate** (→ split-rate-increases-construction):
- [ ] [DRAFT] tier:T2 — banzhaf-lavery-pa-sprawl — Banzhaf & Lavery 2010 (important; also anti-sprawl)
- [ ] [DRAFT] tier:T2 — gemmell-grimes-skidmore-nz — Gemmell, Grimes & Skidmore 2019 (important)
- [ ] [DRAFT] tier:T2 — yang-split-rate-tax-base — Yang 2018/2021 Lincoln (important; registry row exists)
**Affordability** (→ lvt-improves-housing-affordability):
- [ ] [DRAFT] tier:T2 — saiz-housing-supply-elasticity — Saiz 2010 (core)
- [ ] [DRAFT] tier:T2 — glaeser-gyourko-housing-supply — Glaeser & Gyourko 2018 JEP (core)
- [ ] [DRAFT] tier:T2 — hilber-vermeulen-england-supply — Hilber & Vermeulen 2016 (important)
**Productivity** (→ high-land-rents-suppress-productivity):
- [ ] [DRAFT] tier:T2 — hsieh-moretti-spatial-misallocation — Hsieh & Moretti 2019 (core)
- [ ] [DRAFT] tier:T2 — duranton-puga-urban-growth — Duranton & Puga 2020 (important)
**Incidence** (→ landlords-cannot-pass-lvt-to-tenants):
- [ ] [DRAFT] tier:T2 — mieszkowski-property-tax-incidence — Mieszkowski 1972 (core)
- [ ] [DRAFT] tier:T2 — zodrow-three-views — Zodrow 2001 (important)
- [ ] [DRAFT] tier:T2 — hamilton-benefit-tax — Hamilton 1976 (important; challenged_by — benefit-view counter-tradition)
- [ ] [DRAFT] tier:T2 — palmon-smith-capitalization — Palmon & Smith 1998 (important)
**Speculation/cycles** (→ lvt-dampens-land-speculation):
- [ ] [DRAFT] tier:T2 — hoyt-chicago-land-values — Hoyt 1933 (important; registry row exists)
- [ ] [DRAFT] tier:T2 — foldvary-business-cycle-synthesis — Foldvary 1997 AJES (important; registry row exists)
- [ ] [DRAFT] tier:T2 — cunningham-seattle-options — Cunningham 2006 (important)
- [ ] [DRAFT] tier:T2 — glaeser-real-estate-bubbles — Glaeser 2017 (important)
- [ ] [DRAFT] tier:T2 — case-shiller-2003-bubble — Case & Shiller 2003 (important)
**HGT/public goods** (→ public-goods-fundable-from-land-rent):
- [ ] [DRAFT] tier:T2 — arnott-hgt-practical-guide — Arnott 2004 (important)
- [ ] [DRAFT] tier:T2 — kanemoto-hgt-cite — best verified Kanemoto/second HGT empirical cite (agent verifies)
**Progressivity** (→ land-value-tax-can-be-progressive):
- [ ] [DRAFT] tier:T2 — plummer-lvt-distribution — Plummer 2010 (important)
- [ ] [DRAFT] tier:T2 — bowman-bell-lvt-distribution — Bowman & Bell (agent verifies best cite)
**Developing world** (→ property-tax-raises-welfare-developing):
- [ ] [DRAFT] tier:T2 — world-bank-changing-wealth — World Bank 2021 Changing Wealth of Nations (important)
**Resource dividends** (→ resource-rent-dividends-work):
- [ ] [DRAFT] tier:T2 — jones-marinescu-alaska-pfd — Jones & Marinescu 2022 AEJ (core)
- [ ] [DRAFT] tier:T2 — widerquist-howard-pfd — Widerquist & Howard 2012 (important)
- [ ] [DRAFT] tier:T2 — hartwick-rule — Hartwick 1977 (core)
- [ ] [DRAFT] tier:T2 — segal-resource-dividend — Segal 2011 (important; also developing-world)
**Tech/corporate rents** (→ NEW outcome corporate-profits-increasingly-rents + rentier narrative):
- [ ] [JUDGE] tier:T1 — outcomes/corporate-profits-increasingly-rents.md — new outcome page (T1 writes; evidence_strength calibrated)
- [ ] [DRAFT] tier:T2 — de-loecker-eeckhout-unger-markups — De Loecker, Eeckhout & Unger 2020 QJE (core)
- [ ] [DRAFT] tier:T2 — furman-orszag-firm-rents — Furman & Orszag 2015 (important)
- [ ] [DRAFT] tier:T2 — bessen-regulatory-rents — Bessen 2016 (important)
- [ ] [DRAFT] tier:T2 — philippon-great-reversal — Philippon 2019 (important)
- [ ] [DRAFT] tier:T2 — crouzet-eberly-intangibles — Crouzet & Eberly 2019 (important; challenged_by side)
- [ ] [DRAFT] tier:T2 — korinek-ng-digital-superstars — Korinek & Ng (important)
- [ ] [DRAFT] tier:T2 — haskel-westlake-capitalism-without-capital — Haskel & Westlake 2017 (important)
- [ ] [DRAFT] tier:T2 — zingales-political-theory-firm — Zingales 2017 (important)
- [ ] [DRAFT] tier:T2 — akcigit-ates-business-dynamism — Akcigit & Ates 2021 (important)
- [ ] [DRAFT] tier:T2 — eeckhout-profit-paradox — Eeckhout 2021 (important)
- [ ] [DRAFT] tier:T2 — rochet-tirole-two-sided — Rochet & Tirole 2003 (important)
- [ ] [DRAFT] tier:T2 — data-as-labor — Arrieta-Ibarra et al. 2018 (supplementary)
- [ ] [DRAFT] tier:T2 — hazlett-spectrum-rents — Hazlett spectrum property rights (supplementary)
- [ ] [DRAFT] tier:T2 — cea-2016-market-power — CEA 2016 brief (supplementary)

## Deepen-scan queue (Tier ≥ Important currently at Light — per EDITORIAL.md Scan Depth policy)
- [x] [DEEPEN-SCAN] tier:T2 status:done — ALL SIX below completed 2026-07-03 (wave 3): dedicated
      research/ pages created, Scan Depths →Medium (Heavy withheld pending primary-text access —
      the egress proxy blanket-blocks WebFetch; queue Heavy re-passes when access improves).
- [x] [DEEPEN-SCAN] tier:T2 status:done — Churchill, *The People's Rights* (1910, important): mine the
      land-monopoly chapters beyond the one Edinburgh quote; candidate dedicated research/ page.
- [x] [DEEPEN-SCAN] tier:T2 status:done — Hudson, *Killing the Host* (2015, important): NOTE master
      Sheet already records this Heavy via people/michael-hudson — reconcile first, then mine the
      rent/financialization argument into the-rentier-economy + a dedicated research/ page.
- [x] [DEEPEN-SCAN] tier:T2 status:done — Mazzucato, *The Value of Everything* (2018, important):
      value-extraction vs value-creation framework; dedicated research/ page.
- [x] [DEEPEN-SCAN] tier:T2 status:done — Autor et al., *Fall of the Labor Share* (2020, important):
      superstar-firms mechanism vs land-rent explanation; strengthens the-rentier-economy honesty section.
- [x] [DEEPEN-SCAN] tier:T2 status:done — Mill, *Principles of Political Economy* (1848, core):
      Book V land-taxation chapters beyond the one §5 quote; candidate research/ page.
- [x] [DEEPEN-SCAN] tier:T2 status:done — Rothbard, *The Single Tax* (1957, important): mine the full
      critique into objections/lvt-austrian-critique (currently cites it only indirectly).
      (Friedman 1978 symposium stays Light — a two-paragraph remark, fully extracted.)

- [ ] [DEEPEN-SCAN] tier:T2 status:todo — George, *Social Problems* follow-up: chapter-by-chapter
      mine of the remaining ~17 chapters once direct primary-text access is available (current pass
      covered 4 chapters via search corroboration; Core tier targets Heavy).

- [ ] [DRAFT] tier:T2 status:todo — objections: "cycles are chiefly monetary/credit, not land" —
      the counter-position page the cycles narrative flags as missing (Borio/BIS as steelman source).

## Registry ↔ master Sheet reconciliation
- [ ] [RECONCILE] tier:T3 status:todo — Merge the master Google Sheet's per-source rows into
      sources/registry.csv: the registry was seeded from repo frontmatter + a curated list, so some
      Sheet rows (e.g. Killing the Host [Heavy], The Power in the Land, Boom Bust, Land Is a Big
      Deal, Radical Markets, Land and Liberty) are missing or wrongly flagged NEW in exports.
      One-time import keyed by Title; keep the Sheet's Scan Depth/Status where richer.

## Phase 0 — remaining (needs credentials, not Fable)
- [x] [RECONCILE] tier:T3 status:done — CWC drift RESOLVED 2026-07-03 by fresh git-master authorship
      (wave 3): common-wealth-canada, natural-common-wealth-economic-rent-canada, british-columbia,
      cwc-distributional-impacts-lvt created; common-wealth-fund + price-reaction covered within the
      org/report pages (create dedicated pages only if needed). NOTE: if the live Ghost versions
      contain material beyond these, a credentialed pull_from_ghost.py diff can merge later.
- [ ] [RECONCILE-superseded] (original task, kept for record) — Backfill the 6 Common Wealth Canada pages missing from git
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
