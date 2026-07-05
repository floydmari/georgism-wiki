# BACKLOG.md — Wiki Improvement Queue

## ⟳ RESUME HERE (checkpoint 2026-07-05, WS2 NARRATIVES COMPLETE — 12/12)
State: 240 pages, lint green (0 errors), COVERAGE 14/14. **All twelve narratives are now shipped**
(2026-07-05 session: 7 written T1-direct — single-tax, community-creates-land-value,
housing-crisis-is-a-land-crisis, citizens-dividend, ecological-rent, the-corruption-of-economics,
the-great-land-robbery) plus 4 prerequisite research pages (barnes-who-owns-the-sky,
fairlie-enclosure-history, blaug-henry-george-rebel [the anti-Gaffney counter-source],
song-zenou-property-tax-sprawl). Registry ~231→260 rows. Branch
claude/georgism-wiki-campaign-xz5anj (note: earlier w5 branch/PR were merged as PR #3; this is the
successor working branch).

Environment notes for successors: (a) no local ollama/GLM in this container — T1/T2 work runs on
Claude; volume drafting via subagents, max 3-4 concurrent; (b) the egress proxy 403s most direct
fetches — forage agents corroborate via WebSearch snippets and pages ship conservative at Light
scan with [VERIFY] flags; (c) this session's WebSearch quota ran out mid-session — budget searches.

A fresh session resumes with, in order:
1. `git status` + lint.
2. **Floyd's new site-scan queue** (Comprehensiveness section below): citdiv.org + all of
   progress.org except /wiki/. Survey pass first; needs web access.
3. **Flywheel continues** (LOOP.md): [PRIORITIZE] the Stub queue below (17 stubs), run top 3-5
   [BACKFILL]s per wave — john-bates-clark and fire-sector now have narrative dependencies live.
4. Remaining evidence depth (queue below): 8 unchecked tech-rents papers; loffler-siegloch and
   england-zhao counter-evidence pages; hilber-vermeulen; davis-heathcote.
5. WS8 [CITE] retrofit (Phase 3), staleness sweep (BC SVT rates follow-up), WS6 concepts.
6. Per-wave wrap-up unchanged: registry flip in-iteration → Sheet snapshot (mandatory-loud; TWO
   [SHEET-SYNC] todos now pending) → LOOPLOG → preview rebuild + artifact redeploy (same URL:
   https://claude.ai/code/artifact/71d156a4-a38a-4de8-be83-4e3ef69df163). Ghost publish still
   gated on GHOST_ADMIN_KEY (1Password service token) — everything stays commit-only until then.
7. **Wanted-books channel**: sources/wanted-books.md lists ~20 books awaiting e-copies from Floyd;
   when one lands, spawn its [DEEPEN-SCAN] and upgrade the citing pages past Light.

Wiring conventions proven this campaign (keep following): supports_outcomes only when honestly
earned (null results get [], e.g. gemmell; context-only sources get [], e.g. piketty); counter
-evidence goes in challenged_by (autor, barkai, crouzet-eberly, martinez); premise-level vs
mechanism vs policy evidence distinguished in outcome bodies (see lvt-dampens-land-speculation's
three-tier evidence map).

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

## Standing rule — registry mirrors (GitHub exports + Google Sheet)
Any task that edits `sources/registry.csv` must, per LOOP.md step 3: (1) run
`scripts/export_registry_for_sheet.py` and **commit the dated export to
`sources/exports/registry-export-YYYY-MM-DD.csv`** (the definitive, GitHub-viewable snapshot —
Floyd's request 2026-07-05; GitHub renders CSVs as sortable tables), AND (2) push a Drive snapshot
spreadsheet (or leave a loud [SHEET-SYNC] task here if Drive is unreachable).
Last synced: **2026-07-05** — repo export `sources/exports/registry-export-2026-07-05.csv` + Drive
snapshot "Georgism Wiki — Source Registry (git sync 2026-07-05)" (259 rows, 29 NEW in Δ column;
covers the previously-pending wave-D delta).
- [ ] [SHEET-SYNC] tier:T3 status:todo — durable write-back: once a Google service-account JSON is
      in the Emma vault (per the 1Password/op plumbing) and the master Sheet is shared with that
      service account as Editor, write `scripts/sync_registry_to_sheet.py` to update the master
      Sheet in place via the Sheets API each REVIEW-loop iteration (replaces dated snapshots).

- [x] [SHEET-SYNC] done 2026-07-04 — full snapshot "Georgism Wiki — Source Registry (git sync 2026-07-04)" pushed to Floyd's Drive (215 rows, Δ 23 NEW + 3 UPDATED vs main).
- [x] [SHEET-SYNC] done 2026-07-05 — wave-D delta + this session's 29 new rows all covered by the 2026-07-05 full snapshot (Drive + repo export in sources/exports/).

## Comprehensiveness loop (LOOP-COMPREHENSIVENESS.md — invokable audit, separate from the main loop)
comprehensiveness watermark: 0 external-source rows (never run — first invocation 2026-07-04 in progress)
- [ ] [COMPREHENSIVENESS-SWEEP] tier:T2 status:in-progress — first full sweep of all 136 external
      registry sources (13 batches; prepass: 42 author candidates, 46 under-mined sources).
      On completion: T1 triage -> stubs -> Phase 3 content development -> update watermark here.

### Site-scan queue (added by Floyd 2026-07-05 — whole-site ingest targets)
- [ ] [SCAN] tier:T2 status:todo — **https://citdiv.org/** — full-site scan: survey pass first
      (site not yet inspected — this session's web quota ran out before it could be fetched), then
      extract citable claims/sources, add registry rows, create/extend pages, harvest DISCOVERED
      candidates into stubs.
- [ ] [SCAN] tier:T2 status:todo — **progress.org, ALL sections EXCEPT /wiki/** (the wiki is this
      repo's own output — do not re-ingest it). Articles, archives, static pages. Survey pass to
      map sections, then batch the extract→register→stub pipeline.
- FUTURE LOOPS (queued by Floyd — do NOT scan yet): **gameofrent.com** (Lars Doucet) and the
      **Progress and Poverty Substack** — to be addressed in later loops.

### Wanted books (curated list: `sources/wanted-books.md`, 2026-07-05)
- [ ] [DEEPEN-SCAN] tier:T2 status:blocked — ~20 influential books stuck at Light/no scan because
      no free e-copy is reachable from this environment (proxy blocks archive.org lending too).
      Each unblocks as Floyd supplies an electronic version; spawn one [DEEPEN-SCAN] per title as
      copies land. Top of the list: The Corruption of Economics (full book), Who Owns the Sky,
      England's Land and Liberty (2023), Harrison's Power in the Land / Boom Bust,
      Rethinking the Economics of Land and Housing.

## Stub queue (flywheel intake — stubs created at discovery, ranked by [PRIORITIZE])
- [ ] [PRIORITIZE] tier:T1 status:recurring — each wave: rank stubs below by (a) inbound-link
      demand from existing pages, (b) evidence already in the ingested corpus, (c) citing-source
      tier; move the top 3-5 into [BACKFILL] tasks (tasks/backfill-page-task.md).
Stubs created by the 2026-07-04 DISCOVERY-SWEEP (Task 0, 20 accepted / 10 rejected-with-reason in LOOPLOG):
- [x] [BACKFILL] tier:T2 status:done — people/homer-hoyt backfilled 2026-07-04 (FHA/redlining role addressed with Ware 2021 RSF cite)
- [x] [BACKFILL] tier:T2 status:done — people/david-lloyd-george backfilled 2026-07-04 (226 lines; Limehouse venue disambiguated, Dreadnoughts/Green-Book misattributions corrected)
- [ ] [BACKFILL] tier:T2 status:todo — people/winston-churchill (People's Rights corpus page live; 2 chunks)
- [x] [BACKFILL] tier:T2 status:done — places/vancouver backfilled 2026-07-04 (note: british-columbia.md still cites STALE 0.5%/2% SVT rates — see follow-up below)
- [ ] [BACKFILL] tier:T2 status:todo — concepts/superstar-firms (pairs with tech-rents cluster + new outcome)
- [ ] [BACKFILL] tier:T2 status:todo — concepts/fire-sector (rentier-economy narrative dependency)
- [ ] [BACKFILL] tier:T2 status:todo — concepts/mass-appraisal-methods (assessment objection's practical answer)
- [ ] [BACKFILL] tier:T2 status:todo — events/2008-financial-crisis (cycle narrative proof-point)
- [ ] [BACKFILL] tier:T2 status:todo — concepts/public-land-leasing (HK/Singapore mechanism)
- [x] [BACKFILL] tier:T2 status:done — people/john-bates-clark backfilled 2026-07-05 (T1-direct from session-verified sources; both historiographies carried, Clark 1899 preface quote, Leonard 2003 + Blaug 2000 counter-sources)
- [ ] [BACKFILL] tier:T2 status:todo — people/charles-tiebout, people/murray-rothbard, people/michael-davitt, people/l-d-taylor
- [ ] [BACKFILL] tier:T2 status:todo — events/irish-land-war, organizations/fairhope-single-tax-corporation
- [ ] [BACKFILL] tier:T2 status:todo — concepts/holdout-problem, concepts/production-boundary, concepts/radical-markets, concepts/land-value-increment-tax
Rejected (do not re-propose without new evidence): concepts/hartwick-rule + genuine-savings (research page suffices), concepts/fisim (too far afield), concepts/property-tax-incidence-views (covered by zodrow + queued benefit-view), organizations/land-tenure-reform-association (one subsection), people/john-rawls (one paper), people/phillip-j-anderson (sourcing thin), Tullock/Krueger combined bio (malformed; rent-seeking covers), concepts/land-price-capitalization-of-taxes (fold into tax-capitalization), places/estonia-tallinn-case (estonia.md suffices).

## Evidence-base build-out: 50 research pages until every outcome has ≥5 papers
Standard task file: `tasks/research-page-task.md`. Format: slug — Author Year *Title* (tier) → supports_outcomes.
Progress gauge: `lint_wiki.py` COVERAGE block. Termination: 14/14 outcomes ≥5.
**Capitalization** (→ public-investment-capitalizes-into-land):
- [x] [DRAFT] tier:T2 — oates-1969-capitalization — Oates 1969 (core)
- [x] [DRAFT] tier:T2 — gibbons-machin-rail-access — Gibbons & Machin 2005 (important)
- [x] [DRAFT] tier:T2 — mohammad-rail-meta-analysis — Mohammad et al. 2013 (important)
- [x] [DRAFT] tier:T2 — albouy-what-are-cities-worth — Albouy 2016 (core) — agent kept only public-investment-capitalizes-into-land; dropped the fund-government wiring as unsupported
- [ ] [DRAFT] tier:T2 — davis-heathcote-us-land — Davis & Heathcote 2007 (important)
**Land value scale** (→ land-rent-could-fund-government):
- [x] [DRAFT] tier:T2 — larson-us-land-value — Larson 2015 BEA (core)
- [x] [DRAFT] tier:T2 — albouy-ehrlich-shin-metro-land — Albouy, Ehrlich & Shin 2018 (important)
**Capital share** (→ capital-share-rise-is-land):
- [x] [DRAFT] tier:T2 — knoll-schularick-steger-house-prices — Knoll et al. 2017 AER (core)
- [x] [DRAFT] tier:T2 — la-cava-housing-capital-share — La Cava 2016 (important)
- [x] [DRAFT] tier:T2 — piketty-capital-21st-century — Piketty 2014 (core) — T1 honesty call: CONTEXT-ONLY (supports_outcomes: []); the land-specific decomposition is Rognlie/Bonnet/La Cava's, not Piketty's
- [x] [DRAFT] tier:T2 — barkai-declining-shares — Barkai 2020 (important) — wired as designed: challenged_by on capital-share-rise-is-land + supports corporate-profits-increasingly-rents
**Efficiency** (→ lvt-can-replace-capital-taxes-without-efficiency-loss):
- [x] [DRAFT] tier:T2 — oecd-taxation-economic-growth — Johansson et al. 2008 (core)
- [x] [DRAFT] tier:T2 — arnold-tax-growth-ej — Arnold et al. 2011 EJ (important)
- [x] [DRAFT] tier:T2 — brueckner-site-value-taxation — Brueckner 1986 (core)
**Construction/split-rate** (→ split-rate-increases-construction):
- [x] [DRAFT] tier:T2 — banzhaf-lavery-pa-sprawl — Banzhaf & Lavery 2010 (important; also anti-sprawl)
- [x] [DRAFT] tier:T2 — gemmell-grimes-skidmore-nz — Gemmell, Grimes & Skidmore 2019 (important) — NULL RESULT for new construction (Auckland, confounded reform, short window); supports_outcomes:[] per honesty rule; cited as caveat in the outcome body instead
- [x] [DRAFT] tier:T2 — yang-split-rate-tax-base — Yang 2018/2021 Lincoln (important; registry row exists)
**Affordability** (→ lvt-improves-housing-affordability):
- [x] [DRAFT] tier:T2 — saiz-housing-supply-elasticity — Saiz 2010 (core)
- [x] [DRAFT] tier:T2 — glaeser-gyourko-housing-supply — Glaeser & Gyourko 2018 JEP (core)
- [ ] [DRAFT] tier:T2 — hilber-vermeulen-england-supply — Hilber & Vermeulen 2016 (important)
**Productivity** (→ high-land-rents-suppress-productivity):
- [x] [DRAFT] tier:T2 — hsieh-moretti-spatial-misallocation — Hsieh & Moretti 2019 (core)
- [x] [DRAFT] tier:T2 — duranton-puga-urban-growth — Duranton & Puga 2020 (important)
**Incidence** (→ landlords-cannot-pass-lvt-to-tenants):
- [x] [DRAFT] tier:T2 — mieszkowski-property-tax-incidence — Mieszkowski 1972 (core)
- [x] [DRAFT] tier:T2 — zodrow-three-views — Zodrow 2001 (important)
- [x] [DRAFT] tier:T2 — hamilton-benefit-tax — Hamilton 1976 (important; challenged_by — benefit-view counter-tradition)
- [x] [DRAFT] tier:T2 — palmon-smith-capitalization — Palmon & Smith 1998 (important)
**Speculation/cycles** (→ lvt-dampens-land-speculation):
- [x] [DRAFT] tier:T2 — hoyt-chicago-land-values — Hoyt 1933 (important; registry row exists)
- [x] [DRAFT] tier:T2 — foldvary-business-cycle-synthesis — Foldvary 1997 AJES (important; registry row exists)
- [x] [DRAFT] tier:T2 — cunningham-seattle-options — Cunningham 2006 (important)
- [x] [DRAFT] tier:T2 — glaeser-real-estate-bubbles — Glaeser 2017 (important)
- [x] [DRAFT] tier:T2 — case-shiller-2003-bubble — Case & Shiller 2003 (important)
**HGT/public goods** (→ public-goods-fundable-from-land-rent):
- [x] [DRAFT] tier:T2 — arnott-hgt-practical-guide — Arnott 2004 (important)
- [x] [DRAFT] tier:T2 — kanemoto-hgt-cite — verified as Kanemoto, Ohkawara & Suzuki 1996 JJIE (slug: kanemoto-ohkawara-suzuki-optimal-city-size; primary text read)
**Progressivity** (→ land-value-tax-can-be-progressive):
- [x] [DRAFT] tier:T2 — plummer-lvt-distribution — Plummer 2010 (important)
- [x] [DRAFT] tier:T2 — bowman-bell-lvt-distribution — Bowman & Bell (agent verifies best cite)
**Developing world** (→ property-tax-raises-welfare-developing):
- [x] [DRAFT] tier:T2 — world-bank-changing-wealth — World Bank 2021 Changing Wealth of Nations (important) — honest re-wiring: supports land-rent-could-fund-government (wealth-accounting scale), NOT the developing-world welfare outcome
**Resource dividends** (→ resource-rent-dividends-work):
- [x] [DRAFT] tier:T2 — jones-marinescu-alaska-pfd — Jones & Marinescu 2022 AEJ (core)
- [x] [DRAFT] tier:T2 — widerquist-howard-pfd — Widerquist & Howard 2012 (important)
- [x] [DRAFT] tier:T2 — hartwick-rule — Hartwick 1977 (core)
- [x] [DRAFT] tier:T2 — segal-resource-dividend — Segal 2011 (important; also developing-world)
**Tech/corporate rents** (→ NEW outcome corporate-profits-increasingly-rents + rentier narrative):
- [x] [JUDGE] tier:T1 status:done — outcomes/corporate-profits-increasingly-rents.md written by T1 2026-07-04; evidence_strength 'Moderate–strong for the profit rise; contested on rent vs efficiency'; challenged_by crouzet-eberly
- [x] [DRAFT] tier:T2 — de-loecker-eeckhout-unger-markups — De Loecker, Eeckhout & Unger 2020 QJE (core)
- [x] [DRAFT] tier:T2 — furman-orszag-firm-rents — Furman & Orszag 2015 (important) — bonus: its Fig 4 decomposition also supports capital-share-rise-is-land
- [ ] [DRAFT] tier:T2 — bessen-regulatory-rents — Bessen 2016 (important)
- [x] [DRAFT] tier:T2 — philippon-great-reversal — Philippon 2019 (important)
- [x] [DRAFT] tier:T2 — crouzet-eberly-intangibles — Crouzet & Eberly 2019 (important; challenged_by on the new outcome, as designed; Heavy scan, primary text read)
- [ ] [DRAFT] tier:T2 — korinek-ng-digital-superstars — Korinek & Ng (important)
- [ ] [DRAFT] tier:T2 — haskel-westlake-capitalism-without-capital — Haskel & Westlake 2017 (important)
- [ ] [DRAFT] tier:T2 — zingales-political-theory-firm — Zingales 2017 (important)
- [ ] [DRAFT] tier:T2 — akcigit-ates-business-dynamism — Akcigit & Ates 2021 (important)
- [x] [DRAFT] tier:T2 — eeckhout-profit-paradox — Eeckhout 2021 (important)
- [ ] [DRAFT] tier:T2 — rochet-tirole-two-sided — Rochet & Tirole 2003 (important)
- [ ] [DRAFT] tier:T2 — data-as-labor — Arrieta-Ibarra et al. 2018 (supplementary)
- [ ] [DRAFT] tier:T2 — hazlett-spectrum-rents — Hazlett spectrum property rights (supplementary)
- [ ] [DRAFT] tier:T2 — cea-2016-market-power — CEA 2016 brief (supplementary)

## Follow-ups discovered by the 2026-07-04 session (wave 5)
- [ ] [UPDATE] tier:T3 status:todo — places/british-columbia.md cites stale BC Speculation & Vacancy Tax rates (0.5%/2%); current: 1%/3% for 2026, 4% foreign from 2027 (vancouver.md has fresh cites) — refresh + registry
- [ ] [DRAFT] tier:T2 status:todo — research/loffler-siegloch-german-pass-through — German property-tax pass-through to rents (the strongest counter-evidence to landlords-cannot-pass-lvt-to-tenants; carroll-yinger page flags it [VERIFY]; likely belongs in challenged_by when verified)
- [ ] [DRAFT] tier:T2 status:todo — research/england-zhao-2005 — the Dover NH study Bowman & Bell replicate (regressive finding — honest counterweight for land-value-tax-can-be-progressive)
- [ ] [STUB] tier:T2 status:todo — concepts/sector-model (Hoyt's urban-structure model; discovered by homer-hoyt backfill; no coverage anywhere)
- [ ] [STUB] tier:T3 status:todo — candidates from backfills, triage next [PRIORITIZE]: organizations/bc-assessment-authority; events/1913-bc-real-estate-crash; people/henry-george-jr; events/parliament-act-1911; organizations/land-enquiry-committee (the 1913-14 'The Land' reports); events/1925-green-book-campaign (people/arthur-balfour surfaced too but likely fails the substantive-discussion bar — reject unless more corpus demand appears)
- [ ] [DEEPEN-SCAN] tier:T2 status:todo — research/hoyt-chicago-land-values Heavy re-pass (519pp on archive.org) to resolve its 6 [VERIFY] markers incl. the 1836/1856/1872/1890/1925 peak-year list

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
