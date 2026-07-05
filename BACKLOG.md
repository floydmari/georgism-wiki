# BACKLOG.md — Wiki Improvement Queue

## ⟳ RESUME HERE (checkpoint 2026-07-05 Hermes overnight w1)
HERMES OVERNIGHT DELTA: 4 books scanned (Harrison Boom Bust, Harrison Power in the Land,
Anderson Secret Life of Real Estate, Patel Secret Wealth Advantage) → 4 new research pages +
5 existing pages enriched with book findings. 12 VERIFY/CITATION NEEDED markers cleared
(Hsieh-Moretti, Glaeser-Gyourko, IMF Building Tax Capacity, Knoll-Schularick-Steger, Progress
18.6-year cycle). 1 CORRECTED item: Hsieh-Moretti Caplan correction figures were LARGER not
smaller. 33 markers remain (mostly paywalled). Ricardo's Law research page still needed.
Branch hermes/enrichment-w1, PR #6, 11 commits, lint green (0 errors, 485 warnings).

Previous checkpoint follows — still accurate for environment notes.
## ⟳ RESUME HERE (checkpoint 2026-07-05 loop 2, WS2 COMPLETE 12/12 + surveys triaged)
LOOP-3 DELTA (Floyd directives, 2026-07-05 evening): (1) GHOST/1PASSWORD DE-SCOPED — deployment
is Floyd's separate process; the loop ends at commit+push+preview; never chase the token again
(LOOP.md step 11 rewritten). (2) NEW LINT GATE `BODY-PARITY` — frontmatter evidence must be
walked through in the body; first corpus scan caught 11 drifted outcome pages, all fixed with
generated paper-by-paper sections (from reviewed excerpts) — a T1 prose-polish pass over those
sections is queued below. (3) Synthesis de-referencing is now a T1 review gate (LOOP.md step 5).
(4) landlords outcome expanded to 7 supports + 2 challenged_by incl. the Danish land-tax study.
- [x] [DEEPEN] tier:T1 status:done 2026-07-06 — all 11 generated "Evidence — Paper by Paper"
      sections woven into narrative prose ("The Evidence in Detail"); capital-share gained a
      dedicated counter-evidence section; progressive-LVT page now presents its England-Zhao vs
      Bowman-Bell dispute openly as jurisdiction-dependent.

EXA DELTA (Floyd directive, 2026-07-06): Exa API key delivered — stored in env only (this
container's shell profile + to be added as `EXA_API_KEY` in the cloud environment settings for
future sessions); NEVER committed. New standing rule in LOOP.md step 3: every people/ page
creation or backfill starts with `python3 scripts/exa_enrich.py "<Name>"` (report-only; T1
verifies and cites what it finds). Current blocker: the egress proxy 403s api.exa.ai — until
allowlisted, fall back to WebSearch and leave pages in the sweep below. The key works
immediately from Hermes's unblocked environment.
- [ ] [ENRICH] tier:T2 status:blocked-on-allowlist — Exa enrichment sweep over ALL existing
      people/ pages (~35+): per page run scripts/exa_enrich.py, T1 verifies/cites findings,
      upgrade thin bios, resolve [VERIFY] markers where Exa's text extracts settle them.
      Unblock = api.exa.ai in the proxy allowlist OR delegate the sweep to Hermes (its
      environment is unblocked; same report-only + T1-gate protocol applies).

LOOP-2 DELTA (same day, after the block below was written): stubs 17→15
(john-bates-clark, superstar-firms, fire-sector backfilled; karl-widerquist stub added);
citdiv.org + progress.org surveys DONE and triaged — both full scans now sit in the
Site-scan queue as status:blocked on the SAME two unblocks: (a) OP_SERVICE_ACCOUNT_TOKEN
(gives the Ghost API for progress.org Batch 0 AND publishing) or proxy allowlist, and
(b) Floyd downloading the citdiv eBook. Next wave order: remaining top backfills
(mass-appraisal-methods, 2008-financial-crisis, public-land-leasing) → progress.org TOP-16
extraction candidates (LOOPLOG 2026-07-05b) which need only WebSearch, not the blocked
Batch 0 → WS8 [CITE] retrofit. (Drive [SHEET-SYNC] refresh dropped — de-scoped 2026-07-06.)

## (superseded same-day checkpoint follows — still accurate for environment notes)
State: 240 pages, lint green (0 errors), COVERAGE 14/14. **All twelve narratives are now shipped**
(2026-07-05 session: 7 written T1-direct — single-tax, community-creates-land-value,
housing-crisis-is-a-land-crisis, citizens-dividend, ecological-rent, the-corruption-of-economics,
the-great-land-robbery) plus 4 prerequisite research pages (barnes-sky-trust,
fairlie-short-history-enclosure, blaug-henry-george-rebel [the anti-Gaffney counter-source],
song-zenou-property-tax-sprawl). Registry ~231→260 rows. Branch
claude/georgism-wiki-campaign-xz5anj (note: earlier w5 branch/PR were merged as PR #3; this is the
successor working branch).

Environment notes for successors: (a) no local ollama/GLM in this container — T1/T2 work runs on
Claude; volume drafting via subagents, max 3-4 concurrent; (b) the egress proxy 403s most direct
fetches — forage agents corroborate via WebSearch snippets and pages ship conservative at Light
scan with [VERIFY] flags; (c) this session's WebSearch quota ran out mid-session — budget searches.

HISTORICAL NOTE from the w5/PR-#4 branch (merged 2026-07-05): NOTE 2026-07-05 (post GLM waves 1-5): main loop runs T2 volume on GLM (LOOP.md 'GLM IS THE
DEFAULT T2/T3 EXECUTOR'; worker: scripts/glm_draft_worker.py). 281 pages. Concepts queue COMPLETE
(22->40+). Stub queue 43->8 (remaining: floyd-marinescu [owner to supply bio], radical-markets,
land-value-increment-tax, land-value-increment/margin leftovers per gauge). Counter-evidence
wired: england-zhao + loffler-siegloch (challenged_by) + gochenour-caplan primary read in full
(Foldvary 2014 reply queued). PR #4 open and growing; PR #3 merged+live.
[Merge resolution: the three-narrative gap the note describes was closed on this branch the same day — 12/12 via T1-direct drafts; parallel GLM drafts of 4 narratives + fire-sector/superstar-firms/john-bates-clark superseded by T1 versions; barnes/fairlie/loffler duplicate research pages deduped, unique content grafted.]

A fresh session resumes with, in order:
1. `git status` + lint.
2. **Floyd's new site-scan queue** (Comprehensiveness section below): citdiv.org + all of
   progress.org except /wiki/. Survey pass first; needs web access.
3. **Flywheel continues** (LOOP.md): [PRIORITIZE] the Stub queue below (17 stubs), run top 3-5
   [BACKFILL]s per wave — john-bates-clark and fire-sector now have narrative dependencies live.
4. Remaining evidence depth (queue below): 8 unchecked tech-rents papers; loffler-siegloch and
   england-zhao counter-evidence pages; hilber-vermeulen; davis-heathcote.
5. WS8 [CITE] retrofit (Phase 3), staleness sweep (BC SVT rates follow-up), WS6 concepts.
6. Per-wave wrap-up: registry flip in-iteration → committed dated export in sources/exports/
   (repo-only rule, 2026-07-06 — no Drive/Sheet sync) → LOOPLOG → preview rebuild + artifact
   redeploy (same URL: https://claude.ai/code/artifact/71d156a4-a38a-4de8-be83-4e3ef69df163).
   Publishing to progress.org is Floyd's separate process (loop ends at commit+push).
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

## Standing rule — registry mirror (repo-only; Drive/Sheet DE-SCOPED, Floyd 2026-07-06)
Any task that edits `sources/registry.csv` must, per LOOP.md step 3, run
`scripts/export_registry_for_sheet.py` and **commit the dated export to
`sources/exports/registry-export-YYYY-MM-DD.csv`** — the definitive, GitHub-viewable snapshot
of all ingested sources (GitHub renders CSVs as sortable tables). Google Drive/Sheet snapshots
are no longer part of the loop: do not push Drive exports or file [SHEET-SYNC] tasks. The two
Drive snapshots pushed 2026-07-04/05 are historical artifacts, not maintained mirrors.
Latest export: `sources/exports/registry-export-2026-07-06.csv` (325 rows).

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

### Site-scan queue (added by Floyd 2026-07-05 — whole-site ingest targets)
- [x] [SCAN-SURVEY] tier:T2 status:done 2026-07-05 — citdiv.org surveyed (snippet-based; proxy
      blocks the domain). VERDICT: small advocacy microsite (~10-25 pages, Oct 2021–2024) founded
      by Phillip J. Anderson as a lead funnel for Property Sharemarket Economics; standard
      rent-funded-UBI advocacy, no novel scholarship; its one concrete number (cumulative Alaska
      PFD total) is a stale ~2006 Wikipedia figure. NO organizations page warranted. Registry row
      added (level-6 advocate source); cited as advocate framing on citizens-dividend-narrative.
- [ ] [SCAN] tier:T2 status:blocked — citdiv.org REMAINDER: the email-gated eBook ("Citizen's
      Dividend", presumably Anderson; also FR/中文/Thai versions) is the only high-value unread
      item. UNBLOCK: Floyd downloads the eBook and drops it in the repo/Drive, OR the egress
      proxy allowlists citdiv.org + realestate.propertysharemarketeconomics.com. Then: sitemap
      fetch → 2 articles + eBook + category archives.
- NOTE: people/phillip-j-anderson — rejection OVERRIDDEN 2026-07-05. Anderson is author of a wiki book (Secret Life of Real Estate), cited by Patel, runs PSE + citdiv.org. People page created with publisher, PSE, and citdiv.org sources.
- [ ] [DRAFT] tier:T2 status:todo — research/raley-citizens-dividend candidate: Bill Raley, "The
      Citizen's Dividend" (32-pp paper, basicincome.org, 2018) — surfaced during the citdiv survey;
      verify author/venue/content before drafting; would give the citizens-dividend concept page
      its first scholarly-tier source beyond George + Alaska.

### Standing rule — synthesis sources get de-referenced (Floyd, 2026-07-05)
Wherever the wiki cites a SYNTHESIS (Doucet's ACX series, Andelson's compendium, review articles),
the wiki must itself work through the underlying literature: every research paper the synthesis
cites gets its own ingestion pass (registry row; research/ page where it carries weight). The
synthesis then becomes navigation, not load-bearing evidence.
- [~] [SCAN] tier:T2 status:mostly-done 2026-07-05 — de-reference Doucet ACX Part 2: forage
      verified the incidence cluster; 4 research pages shipped (tsoodle-turner-rents +
      loffler-siegloch-property-tax as challenged_by; schwegman-yinger-homestead +
      dors-land-taxes-housing-prices as supports; Orr/Heinberg-Oates/Dusansky registered as
      context rows). HONEST FLAG: could NOT confirm Doucet Part 2 actually cites the Orr line —
      snippets indicate his empirical core is the land-tax CAPITALIZATION literature culminating
      in the Danish DØRS study (~13 papers per one secondary source). REMAINING: open the ACX
      article with unblocked access, enumerate the actual 13 citations, diff vs registry, ingest
      the missing; settle Dusansky 1981 full-vs-partial magnitude; Hyman & Pasour 1973 rents
      paper could not be verified (only their property-VALUES paper) — do not cite until
      confirmed.
- [ ] [SCAN] tier:T2 status:todo — de-reference Doucet ACX Parts 1 & 3 (land value scale;
      assessment) the same way — enumerate citations, diff against registry, ingest the missing.
- [x] [DRAFT] tier:T2 status:done 2026-07-05 — research/loffler-siegloch-property-tax shipped
      (IZA DP 14195; full pass-through in 3 years; supply-elasticity heterogeneity noted as
      cutting toward the land-tax case); wired challenged_by on the landlords outcome.
- [x] [SCAN-SURVEY] tier:T2 status:done 2026-07-05 — progress.org (non-wiki) surveyed
      (snippet-based; proxy blocks the domain). FINDINGS: independent publication, editors Floyd
      Marinescu + Martin Adams (NOT run by PPI — that's the renamed Schalkenbach Foundation);
      Progress Report lineage since 1997 (Foldvary wrote weekly 1997–2021, 307 essays migrated);
      ~700–1,500 articles across 59 contributors; 16 top-value extraction candidates identified
      (list in LOOPLOG 2026-07-05b); "Progress LLM" byline (139 AI-authored essays) is
      NON-CITABLE for this zero-fabrication wiki — inventory only.
- [ ] [SCAN] tier:T2 status:blocked — progress.org FULL SCAN, Batch 0 first: enumerate all
      non-wiki posts via the repo's own Ghost Content API (one /posts/ call — needs the same
      OP_SERVICE_ACCOUNT_TOKEN/GHOST key that gates publishing) OR proxy allowlist for
      progress.org. Then by-author batches: 1=Foldvary (307, split ~3), 2=core Georgists
      (Gaffney/JJ-Smith-46/Doucet-21/Harrison/Anderson/Widerquist/Davies), 3=editors+institutional
      (Adams, HGS), 4=Progress-LLM inventory-only, 5=tags/static sweep.
- [ ] [STUB-CREATE] tier:T2 status:todo — people candidates from the progress.org authors channel,
      pending per-person verification: martin-adams (co-editor; *Land: A New Paradigm*),
      jeffery-j-smith (46 essays, long-time Progress Report figure), hanno-t-beck (Banneker
      Center, ran the 1997-era Progress Report infrastructure), lindy-davies (Henry George
      Institute). karl-widerquist stub created 2026-07-05 (already twice in registry).
- FUTURE LOOPS (queued by Floyd — do NOT scan yet): **gameofrent.com** (Lars Doucet) and the
      **Progress and Poverty Substack** — to be addressed in later loops.

### progress.org TOP-16 status (2026-07-06 overnight triage of batch 1: 6 of 16)
INGESTED: johnson-1914-single-tax-critique (Johnson Atlantic 1914 + Foldvary 2017 rebuttal pair),
foldvary-kinetic-potential-rent. REGISTRY+CITED: Gaffney AJES-2015 China paper (on 18-year-cycle),
Counting Bounty ch.20 advocate estimate (on fund-government), Exporting the Alaska Model book
(row; cite on widerquist-howard-pfd BLOCKED — page carries 2 markers, Hermes lane). SKIPPED with
reason: five-stages-of-the-georgist-movement (2 of 5 stages unrecoverable from snippets; one
advocate's original periodization — re-check when progress.org is fetchable).
- [x] [SCAN] tier:T2 status:done 2026-07-06 — TOP-16 batch 2 (10/10 triaged): INGESTED
      real-estate-4-ransom (film page). REGISTRY+CITE ×7: Bonner documentary (on
      video-explainers), Baker $11T Fed-Z.1 extrapolation (fund-government table), Anderson
      Trump/cycle piece (18-year-cycle), Adams+unattributed corruption popularizations (rows;
      page-cites deferred to Hermes's book page at merge), Monbiot cluster (rows: Smith article,
      Schumacher lecture 2020, Guardian 21-Jan-2013 primary; page-cite deferred —
      churchill-peoples-rights carries 14 markers/Hermes lane). SKIPPED ×2 with reason:
      DiMare 4-taxes (personal legal theory, 4th tax unrecoverable), Foldvary geo-lib reply
      (Cuneo original untraced). FLAG from forage: Foldvary's Michigan piece claims a Michigan
      gross-receipts tax that was largely repealed in 2012 — do not reuse that claim.
      **TOP-16 COMPLETE (16/16 triaged: 3 ingests, 10 registry+cite, 3 skips).**
- [x] [STUB-CREATE] tier:T2 status:done 2026-07-06 — people/george-monbiot shipped (first page
      under the new Exa people-rule: api.exa.ai still 403 → WebSearch fallback used, page stays
      in the [ENRICH] sweep). Bio corroborated (Orwell Prize 2022; Land for the Many 2019 report
      to Labour, PDF URL locked; Schumacher Lecture 2020). Wired into housing-crisis +
      ecological-rent narratives (Who Promotes It). Registry: Land for the Many row added,
      Monbiot cluster rows repointed to the bio page; export 2026-07-06 committed.
      One [VERIFY] left: Land for the Many exact proposal wording (full text proxy-blocked).

### Book-scan comprehensiveness (Floyd, 2026-07-06): extraction pass over Hermes's book scans
Hermes's overnight DEEPEN-SCANs (Land is a Big Deal, Corruption of Economics, Radical Markets,
Rethinking Economics of Land & Housing, Economic Theory in Retrospect, +ongoing) produced summary
pages + marker fixes but NOT the discovery channel the comprehensiveness loop requires: each book
must ALSO be mined for (a) research papers it cites -> registry/ingestion candidates, (b) people,
(c) events, (d) places, (e) concepts warranting wiki pages. Per LOOP-COMPREHENSIVENESS.md this is
the DISCOVERED-candidates channel; Floyd is sending Hermes a supplementary extraction prompt.
- [ ] [COMPREHENSIVENESS-SWEEP] tier:T2 status:todo — for EVERY book Hermes scans: produce a
      structured extraction report (citations list with full bib data; people/events/places/
      concepts candidates each with 1-line why + where-in-book locator) committed to its branch
      as sources/inbox/BOOKSCAN-<slug>.report.md. T1 then triages -> stubs/registry per the
      standard accept/reject-with-reason discipline. Applies retroactively to the 5 books
      already scanned and as a standing requirement for the rest of wanted-books.
      **GENERALIZED 2026-07-06 (Floyd):** discovery now applies to EVERY source Hermes
      processes (not just books) and covers ALL wiki categories INCLUDING the new books
      category — spec moved to sources/inbox/README.md ("Discovery is universal";
      DISCOVERY-<slug>.report.md, BOOKSCAN- name still accepted for books).

### books/ category (ratified 2026-07-06 — Hermes's PR created it; Floyd approved)
`books` is now a first-class wiki category: added to lint/preview/ghost category lists,
frontmatter standard in EDITORIAL.md §5, page template in §6. Book pages are the on-wiki
citable anchor for privately-held books (files never committed; quotes ≤50 words page-cited).
- [ ] [RECONCILE] tier:T1 status:todo — at Hermes-PR merge review: normalize the 5+ existing
      books/*.md pages from Hermes's native schema (type/scan_tier/scanned_by, no category/
      stub/excerpt) to the EDITORIAL.md standard (add category: books, stub: false, excerpt,
      authors as list; keep publisher/isbn/page_count/scanned_by/scan_date); wire >=2 inbound
      links per book page (the wiki pages that cite each book); add registry rows/flip Status
      for scanned books; lint must be green post-merge.

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
- [x] [BACKFILL] tier:T2 status:done — people/winston-churchill (GLM wave 3) (People's Rights corpus page live; 2 chunks)
- [x] [BACKFILL] tier:T2 status:done — places/vancouver backfilled 2026-07-04 (note: british-columbia.md still cites STALE 0.5%/2% SVT rates — see follow-up below)
- [x] [BACKFILL] tier:T2 status:done — concepts/superstar-firms backfilled 2026-07-05 (T1 rewrite supersedes GLM wave-2 draft in merge; efficiency-vs-market-power dispute mapped via Philippon/Barkai/Furman-Orszag)
- [x] [BACKFILL] tier:T2 status:done — concepts/fire-sector backfilled 2026-07-05 (T1 rewrite supersedes GLM wave-2 draft in merge; verified scale data + Cochrane counter-view; ecosystem links from GLM version retained)
- [x] [BACKFILL] tier:T2 status:done — people/john-bates-clark backfilled 2026-07-05 (T1 rewrite supersedes GLM wave-3 draft in merge; both historiographies, Clark 1899 preface quote)
- [x] [BACKFILL] tier:T2 status:done — concepts/mass-appraisal-methods (GLM wave 3); events/2008-financial-crisis (GLM wave 3)
- [x] [BACKFILL] tier:T2 status:done — charles-tiebout, murray-rothbard (wave 3); michael-davitt, l-d-taylor (wave 4); events/irish-land-war, organizations/fairhope-single-tax-corporation (GLM wave 4); holdout-problem + production-boundary (waves 3-4)
- [ ] [BACKFILL] tier:T2 status:todo — concepts/public-land-leasing (HK/Singapore mechanism)
- [x] [BACKFILL] status:done (stale line corrected 2026-07-05 overnight) — radical-markets and land-value-increment-tax were already backfilled by the GLM waves; actual remaining stubs: margin-of-production, public-land-leasing (in progress), search-theoretic-critique, progress-and-poverty-institute
Rejected (do not re-propose without new evidence): concepts/hartwick-rule + genuine-savings (research page suffices), concepts/fisim (too far afield), concepts/property-tax-incidence-views (covered by zodrow + queued benefit-view), organizations/land-tenure-reform-association (one subsection), people/john-rawls (one paper), people/phillip-j-anderson ✓ created 2026-07-05, Tullock/Krueger combined bio (malformed; rent-seeking covers), concepts/land-price-capitalization-of-taxes (fold into tax-capitalization), places/estonia-tallinn-case (estonia.md suffices).

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
- [ ] [DEEPEN] tier:T2 status:todo — land-value-increment-tax page: forage 2026-07-05 verified
      facts awaiting integration (page carries 10 markers — Hermes lane): Land Tax Act statutory
      basis (law.moj.gov.tw G0340096), rates 20/30/40% + 10% self-use (unit is ARES not acres —
      translation artifact), ROC Constitution Art. 143 confirmed, 2002 two-year reduction weakly
      corroborated, 40/50/60->20/30/40 2005 history UNVERIFIED, Lam & Tsui 1998 as the
      assessed-value-lag critique reference. German Wertzuwachssteuer 1911-13 comparator verified
      (Backhaus 1997 free PDF at cooperative-individualism).
- [ ] [DRAFT] tier:T2 status:todo — research/yang-lvt-sprawl candidate: Zhou Yang, "Differential
      Effects of Land Value Taxation," J. Housing Economics 39 (2018) 33-39 — reportedly the first
      quasi-experimental estimate of split-rate effects on PA sprawl (four decades of
      adoptions/rescissions). FINDING DIRECTION UNVERIFIED from snippets — read the abstract
      (Lincoln WP: lincolninst.edu/app/uploads/legacy-files/pubfiles/yang_wp21zy1.pdf) BEFORE
      citing; would strengthen (or honestly qualify) lvt-reduces-sprawl beyond 5/5.
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

## Registry — one-time historical import from the old master Sheet
(NOT a sync — Drive/Sheet mirroring is de-scoped 2026-07-06; the repo registry + committed
exports are the registry of record. This is a single backfill of rows the old Sheet had that
the repo seeding missed.)
- [ ] [RECONCILE] tier:T3 status:todo — one-time import of the old master Google Sheet's
      per-source rows into sources/registry.csv, keyed by Title; keep the Sheet's Scan
      Depth/Status where richer (e.g. Killing the Host [Heavy], The Power in the Land, Boom
      Bust, Land and Liberty). NOTE 2026-07-06: several named titles now have Hermes books/
      pages (Land Is a Big Deal, Radical Markets) — reconcile against those at merge review
      rather than the Sheet. Needs Floyd to share the Sheet/CSV once; low priority.

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
