# BACKLOG.md — Wiki Improvement Queue

## ⟳ RESUME HERE (checkpoint 2026-07-04, EVIDENCE CAMPAIGN COMPLETE — 14/14)
State: 227 pages, lint green (0 errors), **COVERAGE 14/14 outcomes ≥5 supporting papers — the
50-paper campaign's termination condition was reached 2026-07-04** (was 1/13 at wave-2 checkpoint).
Also done that day: Task 0 DISCOVERY-SWEEP (10 report-only agents over the whole corpus → 29
candidates → 20 sourced stubs created + 10 rejected-with-reason), the 14th outcome
(corporate-profits-increasingly-rents, T1-written), first flywheel BACKFILL round
(homer-hoyt, vancouver done; david-lloyd-george verify), registry 193→~228 rows, Drive snapshot
"Georgism Wiki — Source Registry (git sync 2026-07-04)". Branch claude/wiki-improvement-w5; PR open.

NOTE 2026-07-05 (post GLM waves 1-5): main loop runs T2 volume on GLM (LOOP.md 'GLM IS THE
DEFAULT T2/T3 EXECUTOR'; worker: scripts/glm_draft_worker.py). 281 pages. Concepts queue COMPLETE
(22->40+). Stub queue 43->8 (remaining: floyd-marinescu [owner to supply bio], radical-markets,
land-value-increment-tax, land-value-increment/margin leftovers per gauge). Counter-evidence
wired: england-zhao + loffler-siegloch (challenged_by) + gochenour-caplan primary read in full
(Foldvary 2014 reply queued). PR #4 open and growing; PR #3 merged+live.

A fresh session resumes with, in order (SUPERSEDES the numbered list below where they conflict):
A. NARRATIVES LAYER — the 7 remaining pages per narratives/_framework.md. This is T1-heavy
   persuasive-framing work: GLM may draft from the framework + corpus, but Fable must rework
   framing, sourcing density per the unearned-increment exemplar. Start fresh-context.
B. Remaining 8 stubs + [COHESION] tasks (BC/Vancouver scope split, terminology pass).
C. [SHEET-SYNC] loud todo below; WS8 [CITE] retrofit; staleness sweep.

Original resume list:
1. `git status` + lint (all three first-round backfills are done: homer-hoyt, vancouver, david-lloyd-george).
2. **Flywheel continues** (LOOP.md): [PRIORITIZE] the Stub queue below (18 stubs remain), run top
   3-5 [BACKFILL]s per wave, harvest DISCOVERED candidates into new stubs. STUBS gauge in lint.
3. Remaining evidence depth (queue below): the 8 unchecked tech-rents papers (korinek-ng,
   haskel-westlake, zingales, akcigit-ates, rochet-tirole, data-as-labor, hazlett, cea-2016) enrich
   the new outcome beyond 5; Follow-ups section (esp. loffler-siegloch and england-zhao — HONEST
   COUNTER-EVIDENCE pages the outcomes need for NPOV); hilber-vermeulen (affordability margin);
   davis-heathcote (capitalization margin).
4. Next structural work per ROADMAP: WS2 narratives (7 remaining), WS6 concepts expansion (queue in
   Phase 1), WS8 [CITE] retrofit (Phase 3), staleness sweep (BC SVT rates follow-up).
5. Per-wave wrap-up unchanged: registry flip in-iteration → Sheet snapshot (mandatory-loud, one
   [SHEET-SYNC] todo is pending) → LOOPLOG → preview rebuild + artifact redeploy (same URL:
   https://claude.ai/code/artifact/71d156a4-a38a-4de8-be83-4e3ef69df163). Ghost publish still
   gated on GHOST_ADMIN_KEY (1Password service token) — everything stays commit-only until then.

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

## Standing rule — Google Sheet mirror of the source registry
Any task that edits `sources/registry.csv` must sync the master Google Sheet per LOOP.md step 3
(export via `scripts/export_registry_for_sheet.py`, then Drive snapshot or a loud [SHEET-SYNC] task
here). Last synced: **2026-07-03 (wave 3 delta pushed same day)** — full snapshot "Georgism Wiki — Source Registry (git sync 2026-07-03)" + delta sheet "Wave 3 delta"
created in Floyd's Drive (166 rows; Δ column marks 13 NEW + 4 UPDATED/CORRECTED from loops 1–7).
- [ ] [SHEET-SYNC] tier:T3 status:todo — durable write-back: once a Google service-account JSON is
      in the Emma vault (per the 1Password/op plumbing) and the master Sheet is shared with that
      service account as Editor, write `scripts/sync_registry_to_sheet.py` to update the master
      Sheet in place via the Sheets API each REVIEW-loop iteration (replaces dated snapshots).

- [x] [SHEET-SYNC] done 2026-07-04 — full snapshot "Georgism Wiki — Source Registry (git sync 2026-07-04)" pushed to Floyd's Drive (215 rows, Δ 23 NEW + 3 UPDATED vs main).
- [ ] [SHEET-SYNC] tier:T3 status:todo — ~13 wave-D rows (Arnott, Kanemoto, Herkenhoff, Goldsmith, Carroll-Yinger, Franzsen, Furman, Barkai, Philippon, Eeckhout, Crouzet, Piketty + IMF row fix) added AFTER the 2026-07-04 snapshot — push a fresh export next iteration

## Comprehensiveness loop (LOOP-COMPREHENSIVENESS.md — invokable audit, separate from the main loop)
comprehensiveness watermark: 136 external-source rows (first invocation completed 2026-07-04; next invocation sweeps rows added after #136 unless --full)
- [x] [COMPREHENSIVENESS-SWEEP] status:done 2026-07-04 — full sweep of 136 sources via GLM
      (zero Claude quota): light pass + deep pass (46 full-text Core/under-mined scans at 1M ctx).
      ~200 raw candidates -> 29 stubs accepted (11+ people incl. Arnott/Oates/Rognlie/Glaeser/
      Piketty/Ely), 4 backfilled same-day (alaska, canada, wallace-oates, edward-glaeser).
      Cohesion audit (whole corpus, 1 call): 25 findings, 12 fixed same-day, rest queued below.
- [ ] [COHESION] tier:T2 status:todo — BC/Vancouver scope split (audit: heavy duplication;
      give british-columbia the provincial/CWC scope, vancouver the city single-tax story)
- [ ] [COHESION] tier:T3 status:todo — terminology normalization pass (citizen's dividend /
      18-year cycle / single-tax variants; audit lists pages) + land-value-capture vs
      public-land-leasing overlap trim
- [ ] [DRAFT] tier:T2 status:todo — concepts: carbon pricing / Pigouvian taxation within the
      Georgist frame (audit corpus-gap; ecological-georgism cites it) and outcomes/lvt-reduces-sprawl
      (Banzhaf-Lavery evidence)
- [x] [DRAFT] tier:T2 status:done — research/great-mortgaging — Jordà-Schularick-Taylor 2014 — GLM wave 1 (full text read; honest supports_outcomes:[] — credit-side complement)

## Stub queue (flywheel intake — stubs created at discovery, ranked by [PRIORITIZE])
- [ ] [PRIORITIZE] tier:T1 status:recurring — each wave: rank stubs below by (a) inbound-link
      demand from existing pages, (b) evidence already in the ingested corpus, (c) citing-source
      tier; move the top 3-5 into [BACKFILL] tasks (tasks/backfill-page-task.md).
Stubs created by the 2026-07-04 DISCOVERY-SWEEP (Task 0, 20 accepted / 10 rejected-with-reason in LOOPLOG):
- [x] [BACKFILL] tier:T2 status:done — people/homer-hoyt backfilled 2026-07-04 (FHA/redlining role addressed with Ware 2021 RSF cite)
- [x] [BACKFILL] tier:T2 status:done — people/david-lloyd-george backfilled 2026-07-04 (226 lines; Limehouse venue disambiguated, Dreadnoughts/Green-Book misattributions corrected)
- [x] [BACKFILL] tier:T2 status:done — people/winston-churchill (GLM wave 3) (People's Rights corpus page live; 2 chunks)
- [x] [BACKFILL] tier:T2 status:done — places/vancouver backfilled 2026-07-04 (note: british-columbia.md still cites STALE 0.5%/2% SVT rates — see follow-up below)
- [x] [BACKFILL] tier:T2 status:done — concepts/superstar-firms (GLM wave 2) (pairs with tech-rents cluster + new outcome)
- [x] [BACKFILL] tier:T2 status:done — concepts/fire-sector (GLM wave 2) (rentier-economy narrative dependency)
- [x] [BACKFILL] tier:T2 status:done — concepts/mass-appraisal-methods (GLM wave 3) (assessment objection's practical answer)
- [x] [BACKFILL] tier:T2 status:done — events/2008-financial-crisis (GLM wave 3) (cycle narrative proof-point)
- [ ] [BACKFILL] tier:T2 status:todo — concepts/public-land-leasing (HK/Singapore mechanism)
- [x] [BACKFILL] tier:T2 status:done — people/john-bates-clark (GLM wave 3) (corruption-of-economics narrative dependency)
- [x] [BACKFILL] tier:T2 status:done — charles-tiebout, murray-rothbard (wave 3); michael-davitt, l-d-taylor (wave 4)
- [x] [BACKFILL] tier:T2 status:done — events/irish-land-war, organizations/fairhope-single-tax-corporation (GLM wave 4)
- [~] [BACKFILL] tier:T2 status:partial — holdout-problem + production-boundary done (waves 3-4); radical-markets, land-value-increment-tax remain
Rejected (do not re-propose without new evidence): concepts/hartwick-rule + genuine-savings (research page suffices), concepts/fisim (too far afield), concepts/property-tax-incidence-views (covered by zodrow + queued benefit-view), organizations/land-tenure-reform-association (one subsection), people/john-rawls (one paper), people/phillip-j-anderson (sourcing thin), Tullock/Krueger combined bio (malformed; rent-seeking covers), concepts/land-price-capitalization-of-taxes (fold into tax-capitalization), places/estonia-tallinn-case (estonia.md suffices).

## Evidence-base build-out: 50 research pages until every outcome has ≥5 papers
Standard task file: `tasks/research-page-task.md`. Format: slug — Author Year *Title* (tier) → supports_outcomes.
Progress gauge: `lint_wiki.py` COVERAGE block. Termination: 14/14 outcomes ≥5.
**Capitalization** (→ public-investment-capitalizes-into-land):
- [x] [DRAFT] tier:T2 — oates-1969-capitalization — Oates 1969 (core)
- [x] [DRAFT] tier:T2 — gibbons-machin-rail-access — Gibbons & Machin 2005 (important)
- [x] [DRAFT] tier:T2 — mohammad-rail-meta-analysis — Mohammad et al. 2013 (important)
- [x] [DRAFT] tier:T2 — albouy-what-are-cities-worth — Albouy 2016 (core) — agent kept only public-investment-capitalizes-into-land; dropped the fund-government wiring as unsupported
- [x] [DRAFT] tier:T2 — davis-heathcote-us-land — Davis & Heathcote 2007 (important) — GLM wave 1, conservative draft (source paywalled; Light scan)
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
- [x] [DRAFT] tier:T2 — hilber-vermeulen-england-supply — Hilber & Vermeulen 2016 (important) — GLM wave 1, conservative draft (source paywalled; [VERIFY]-heavy, Light scan)
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
- [x] [DRAFT] tier:T2 — korinek-ng-digital-superstars — Korinek & Ng (important) — GLM wave 2, conservative (source paywalled; supports stripped to [] per T1)
- [ ] [DRAFT] tier:T2 — haskel-westlake-capitalism-without-capital — Haskel & Westlake 2017 (important)
- [x] [DRAFT] tier:T2 — zingales-political-theory-firm — Zingales 2017 (important) — GLM wave 1
- [x] [DRAFT] tier:T2 — akcigit-ates-business-dynamism — Akcigit & Ates 2021 (important) — GLM wave 1
- [x] [DRAFT] tier:T2 — eeckhout-profit-paradox — Eeckhout 2021 (important)
- [x] [DRAFT] tier:T2 — rochet-tirole-two-sided — Rochet & Tirole 2003 (important) — GLM wave 2 (context page, supports [])
- [ ] [DRAFT] tier:T2 — data-as-labor — Arrieta-Ibarra et al. 2018 (supplementary)
- [ ] [DRAFT] tier:T2 — hazlett-spectrum-rents — Hazlett spectrum property rights (supplementary)
- [x] [DRAFT] tier:T2 — cea-2016-market-power — CEA 2016 brief (supplementary) — GLM wave 1

## Follow-ups discovered by the 2026-07-04 session (wave 5)
- [ ] [DRAFT] tier:T2 status:todo — research/foldvary-reply-gochenour-caplan — Foldvary 2014 RAE 27(4) 451-461, the direct peer-reviewed reply (exists, verified; text 403'd this session) — completes the objection's dialectic
- [ ] [UPDATE] tier:T3 status:todo — places/british-columbia.md cites stale BC Speculation & Vacancy Tax rates (0.5%/2%); current: 1%/3% for 2026, 4% foreign from 2027 (vancouver.md has fresh cites) — refresh + registry
- [x] [DRAFT] tier:T2 status:done — research/loffler-siegloch-german-pass-through — wired as challenged_by on the incidence outcome; page explains why Grundsteuer (land+structure) pass-through does not refute pure-LVT incidence (2026-07-05)
- [x] [DRAFT] tier:T2 status:done — research/england-zhao-lvt-distribution — Dover NH regressive finding, wired as challenged_by on the progressivity outcome (2026-07-05)
- [ ] [STUB] tier:T2 status:todo — concepts/sector-model (Hoyt's urban-structure model; discovered by homer-hoyt backfill; no coverage anywhere)
- [ ] [STUB] tier:T3 status:todo — candidates from backfills, triage next [PRIORITIZE]: organizations/bc-assessment-authority; events/1913-bc-real-estate-crash; people/henry-george-jr; events/parliament-act-1911; organizations/land-enquiry-committee (the 1913-14 'The Land' reports); events/1925-green-book-campaign (people/arthur-balfour surfaced too but likely fails the substantive-discussion bar — reject unless more corpus demand appears)
- [ ] [DEEPEN-SCAN] tier:T2 status:todo — research/hoyt-chicago-land-values Heavy re-pass (519pp on archive.org) to resolve its 6 [VERIFY] markers incl. the 1836/1856/1872/1890/1925 peak-year list

## New outcome evidence queue — outcomes/lvt-reduces-sprawl (created 2026-07-05, 1/5 supporters)
- [ ] [DRAFT] tier:T2 status:todo — research/song-zenou-property-tax-sprawl — Song & Zenou 2006 JUE "Property tax and urban sprawl" (verify) — the direct second study
- [ ] [DRAFT] tier:T2 status:todo — research/brueckner-kim-sprawl — Brueckner & Kim 2003 "Urban sprawl and the property tax" (verify) — the theory anchor
- [ ] [DRAFT] tier:T2 status:todo — 2 further sprawl-evidence papers (agent verifies best: Burchfield et al. 2006 causes-of-sprawl; McGrath 2005) to reach 5/5

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
- [x] [DRAFT] tier:T2 status:done — concepts queue COMPLETE 2026-07-05 (GLM waves 1-2): Site Value,
      Law of Rent, Boom-Bust Cycle, Tiebout Model, Rentier, Land Speculation, Betterment Levy,
      EBCOR, Land Bubble, Marginal Productivity, Land as Commons — concepts 22 -> 40
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
