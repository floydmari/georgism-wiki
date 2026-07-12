# BACKLOG.md — Wiki Improvement Queue

*Regenerated 2026-07-10 (branch `claude/georgism-wiki-campaign-h3n8qd`). The work queue for
the mission in EDITORIAL.md §0: the definitive, honest reference on Geoism and LVT.*

**Motions** (LOOP.md): `FIND` · `READ&MINE` · `SYNTHESIZE` · `VERIFY` · `EXPAND` — plus, per
the problems/benefits split (PLAN-problems-and-benefits.md, EDITORIAL §5b):
**`PROBLEM-BUILD`** (evidence-backed diagnosis pages) and **`BENEFIT-BUILD`** (evidence-backed
policy-effect pages). Tiers: T1 editor · T2 staff writers · T3 copy desk.

Task format, one per line — append follow-ups, never silently drop scope:
`- [ ] [MOTION] tier:T1|T2|T3 status:todo|in-progress|blocked|done — description`

**Ground truth, always fresher than this file:** `sources/verification-queue.md` (regenerate
with `python3 scripts/verification_queue.py`) for VERIFY work; `scripts/lint_wiki.py`
COVERAGE block for evidence gauges; `sources/hermes-workorder.md` for Hermes's lane.

**Standing rules live in LOOP.md/EDITORIAL.md, not here**: lint green before commit, debt
ratchet, campsite rule (≥5 fixes/shift), delta rule, evidence ordering, accept bar + stub
quota, registry edit ⇒ committed dated export, commit+push per shift. Loop ends at
commit+push+preview — publishing is Floyd's process.

---

## NOW (in flight today, 2026-07-10)

### Problems/benefits Phase 2 — stub waves (the main event; acceptance rule EDITORIAL §5b:
### ≥2 big-name anchors claim-level verified before leaving stub, counter-evidence mandatory)
- [~] [PROBLEM-BUILD] tier:T2 status:in-progress — problems 1–6 (PLAN §Gap analysis):
      (1) rising land values/housing costs drive poverty; (2) homelessness is a housing-cost
      problem (Colburn-Aldern anchor); (3) housing unaffordability is a land problem
      (KSS/Glaeser-Gyourko/Hsieh-Moretti — first stub landed this shift:
      problems/housing-unaffordability-is-a-land-problem.md); (4) rent-seeking drags growth
      (Murphy-Shleifer-Vishny, Baumol); (5) the young are locked out of land wealth;
      (6) land underuse / speculative vacancy in high-demand cities.
- [~] [BENEFIT-BUILD] tier:T2 status:in-progress — benefits 7, 8, 10 (PLAN):
      (7) taxing land/rents increases productivity (OECD WP620 w/ Xing caveat, HGT, ATCOR as
      attributed theory); (8) LVT reduces the cost of housing (land PRICES well-supported vs
      RENTS paid weaker — say so); (10) rent dividends reduce poverty/inequality
      (Jones-Marinescu, Segal, WITH the Goldsmith correction from this shift's purge).
      Benefit 9 (construction/density) already exists — [EXPAND] split-rate-increases-
      construction with Oates-Schwab + Song-Zenou at next touch, don't duplicate.
- [~] [PROBLEM-BUILD] tier:T1 status:in-progress — justice pair 11–12 (T1 drafts personally,
      highest editorial sensitivity): (11) land justice & Indigenous reconciliation;
      (12) land & the Black-white wealth gap. Rule: document the intersection (shared
      diagnosis, divergent remedies), do NOT overclaim geoism = reconciliation/reparations.
- [ ] [SYNTHESIZE] tier:T1 status:todo — as each new page ships: add it to
      concepts/the-problems.md / concepts/the-benefits.md indexes (lint requires claim_type;
      indexes must stay current per EDITORIAL §5b).

### People stubs from book scanning (sources/inbox/T1-TODO-people-pages-from-book-scanning.md)
- [~] [EXPAND] tier:T2 status:in-progress — 10 of the listed authors already have pages
      (Andelson, Barnes, Daly, Daniel, Barker, Neeson, Banner, Bryson, Howard, Adams).
      Remaining this wave, standard triage bar applies: K.W. Burgess, John Noyes,
      Eric Goldman, William Redfearn. Then move the TODO file to sources/inbox/consumed/.

### VERIFY burn-down (queue regenerated this shift: 121 markers on wiki pages)
- [ ] [VERIFY] tier:T1 status:recurring — the **unclassified channel (82 markers)** is the
      biggest lane: triage each into a channel or resolve directly. Recent pace: 4–8
      markers/wave (waves 10–11). Channels snapshot: owner-input 2 · book-copy 8 ·
      unblocked-web 23 · new-source 6 · unclassified 82. Queue file is ground truth.
- [ ] [FIND] tier:T2 status:todo — the 6 **needs-new-source** markers each want a forage
      task; top: Cherokee casino-dividend primary (Costello/Akee line — do NOT cite from
      memory; feeds resource-rent-dividends-work AND benefit 10), Letchworth empirical data,
      COST self-assessment evidence, symmetry/decrement objection's best academic statement.

### Public-domain texts program (sources/public-domain-texts.md; 12 texts/ pages live)
- [ ] [READ&MINE] tier:T2 status:todo — NEXT TARGET: Henry George Jr., *The Life of Henry
      George* (1900), archive.org lifeofhenrygeorg00geor — book-length, so
      `sources/publicdomain/` channel (not texts/); already cited as primary on 3+ pages.
      Then per the file's list: Mill Principles (Gutenberg 30107), Progress & Poverty
      (55308), Garden Cities (46134), Pigou Welfare (Econlib), Hoyt 1933 (check renewal).

---

## NEXT (pick up when a NOW lane clears)

- [ ] [SYNTHESIZE] tier:T1 status:todo — the last missing objection steelman from the 9→15
      build-out: public-choice "government will waste the rent" (Buchanan lens). The other
      five shipped (revenue insufficiency, transition shock, homevoter, credit-cycles,
      assessment critique) — objections now 13 pages.
- [ ] [FIND] tier:T2 status:todo — WS-TECH-RENTS remaining discovery, in order:
      (a) DSTs-as-tried (France/UK/India incidence; Amazon UK pass-through as the
      badly-aimed-rent-tax failure case; Pillar One/Two); (b) attention/ad rents (Romer's
      progressive digital ad tax); (c) rent DISSOLUTION vs capture (antitrust/DMA/interop);
      (d) is-it-rent diagnosis update (Furman Review, Korinek-Stiglitz AI rents). THEN the
      gated synthesis: concepts/taxing-tech-rents instrument comparison (ACE/DBCFT vs DST vs
      ad tax vs data dividend vs antitrust, graded). Rent-gradient rule applies hardest here.
- [ ] [FIND] tier:T2 status:todo — WS-GEOISM remaining domain sweep: financial rents &
      seigniorage (Hudson, Bezemer, Philippon, BIS/Borio steelman — honest FIRE grading);
      plus the IP-rents remainder (Boldrin-Levine, prize-vs-patent) to finish the
      platform/data/IP lane (concepts/data-rents already live).
- [ ] [READ&MINE] tier:T2 status:todo — research/foldvary-reply-gochenour-caplan (RAE 27(4),
      verified to exist; completes the Austrian-objection dialectic).
- [ ] [EXPAND] tier:T2 status:todo — lvt-reduces-sprawl toward 5/5 supporters: check the
      COVERAGE gauge first (song-zenou + taranu-verbeeck now live), then brueckner-kim-sprawl
      and one of Burchfield 2006/McGrath 2005 if still short.
- [ ] [READ&MINE] tier:T2 status:todo — Doucet ACX de-referencing Parts 1 & 3 (enumerate
      actual citations, diff vs registry, ingest missing); landlords-outcome Ch. 21 cluster
      (Borge-Rattsø, Capozza-Green-Hendershott, Hilber 2017, Buettner, Choi-Sjoquist).
- [ ] [FIND] tier:T2 status:todo — research/raley-citizens-dividend candidate (verify
      author/venue before drafting; would give citizens-dividend its first scholarly source
      beyond George + Alaska).
- [ ] [EXPAND] tier:T3 status:recurring — mechanical debt, batched: annotate unannotated
      Sources (~25/wave, oldest pages first); thin-article burn-down (3–5/wave by inbound
      links); trim/attribute over-cap quotes; UPDATE places/british-columbia.md stale SVT
      rates (0.5%/2% → 1%/3% for 2026; vancouver.md has fresh cites).
- [ ] [EXPAND] tier:T2 status:todo — cohesion items from the 2026-07-04 audit:
      BC/Vancouver scope split; terminology normalization pass (citizen's dividend /
      18-year cycle / single-tax variants).
- [ ] [EXPAND] tier:T3 status:todo — stub-queue leftovers at next [PRIORITIZE]:
      concepts/sector-model, margin-of-production, progress-and-poverty-institute;
      candidate events/orgs from the lloyd-george/BC backfills (accept bar applies).

---

## GATED / PARKED (surface these, don't chase)

- ~~Phase 3 directory split~~ EXECUTED 2026-07-10 on Floyd's sign-off (`outcomes/` → `problems/` + `benefits/`, indexes at /wiki/problems/ + /wiki/benefits/, lint + scripts + EDITORIAL updated). Old line kept for record:
- **Phase 3 directory split** (`outcomes/` → `problems/` + `benefits/`, redirects, inbound
  link rewrite, registry/inventory rebuild) — **GATED on Floyd's sign-off** of the Phase-1
  grouping. Do not start early; the split touches 400+ pages of links.
- **learning-paths** — **PARKED by Floyd.** Do not start.
- **Provenance attestation** (books/economic-theory-in-retrospect, books/rethinking-
  economics-land-housing) — blocked on Floyd confirming legal copies; scan-depth upgrades
  stay frozen until then (the 2 needs-owner-input markers).
- **needs-book-copy channel (8 markers)** + wanted-books DEEPEN-SCANs (sources/
  wanted-books.md, ~20 titles incl. Rothstein *Color of Law* for justice page 12) —
  unblock as Floyd supplies copies; spawn one [READ&MINE] per title as they land.
- **needs-unblocked-web channel (23 markers)** + Exa people-enrichment sweep — proxy
  allowlist (api.exa.ai, ssrn, nber, worldbank, etc.) or route via Hermes.
- **Hermes lane** — sources/hermes-workorder.md (31 items, regenerated this shift); T1
  reviews deliveries against provenance rules before merge.
- **progress.org full scan** — blocked on Ghost Content API key or allowlist (TOP-16
  triage is COMPLETE 16/16). **gameofrent.com + Progress & Poverty Substack** — future
  loops per Floyd, do not scan yet.
- **Registry one-time import from the old master Sheet** — needs Floyd to share the CSV
  once; low priority (repo registry + dated exports are the registry of record).

---


### Late-shift addendum (2026-07-10 evening, T1)

Everything in the NOW lanes above completed or advanced this evening; verified state at close:

- **Phase 2 COMPLETE and Phase 3 EXECUTED** (Floyd sign-off): `outcomes/` split into
  `problems/` (13) + `benefits/` (15); indexes live at `/wiki/problems/` + `/wiki/benefits/`;
  lint + all scripts + EDITORIAL updated. First Ghost sync will create the
  `wiki-problems`/`wiki-benefits` tags.
- **Justice pair live** (T1 line-reviewed): land-justice-and-indigenous-reconciliation,
  land-and-the-black-white-wealth-gap.
- **Objections build-out complete**: public-choice-critique added (14 objection pages).
- **VERIFY burn-down**: raw wiki-dir marker count 55 at close (121 at queue regen this
  afternoon; ~660 campaign start). Actionable tail exhausted — the remainder is honest
  blocks (paywalled/print/owner-input/2026-calendar-gated).
- **Corrections propagated this shift**: Bakker (2023) mischaracterization fixed wiki-wide
  (measurement, not misallocation); Tullock/England attribution corrected (Olson framework);
  Harrison/Busey chapter fix; Goldman paraphrase-as-quote; fabricated "Andelson 1991
  biography" removed; Ozdilek author fix; Paine pension age 50 (not 55); Ralston-Nolan
  = H.R. 12397; Doucet's Almy/Hefferan-Boyd figure conflations flagged on the new pages.
- **PD program**: 5 new full texts this shift — Life of Henry George (books+publicdomain),
  Agrarian Justice (upgraded, tables rebuilt), Saratoga George-Seligman exchange,
  Deportations Delirium (books+publicdomain, via Harvard IIIF), Irish Land Question
  full proofread (~130 fixes). In flight at close: Johnson 1914 critique, Limehouse 1909.
- **Research ingests**: WS-TECH-RENTS cluster complete (5 pages incl. Korinek-Stiglitz AI
  rents + DMA); financial-rents (Greenwood-Scharfstein, Bazot); mass-appraisal trio
  (Kolbe/Almy/Hefferan-Boyd — Doucet Part-3 gap closed); Hornbeck-Moretti (double-edged,
  wired honestly); Kuminoff-Pope + Hudson (measurement cluster).
- **SPN sweep**: 176/~330 registry URLs archived at close; resumable
  (scripts/spn_sweep.sh, log sources/exports/spn-sweep.log).
- **Floyd-only items surfaced**: CWC founding date/legal form; Ryan-Collins + Blaug
  provenance attestations; the CWC Table 5 "24% HGFC royalty" appears to be a
  back-calculation (fn 32 sourceless) — his paper, his call.

## DONE this shift (2026-07-10) — retired from the queue

- **Phase 1 of the problems/benefits split** (commit 8ecde77): `claim_type: problem|benefit`
  on all 20 outcomes pages; reader indexes `/wiki/problems/` + `/wiki/benefits/`
  live; lint rule active (outcomes missing claim_type = ERROR); EDITORIAL §5b written.
- **sources/verification-queue.md regenerated**: 121 markers (raw `grep -rc '\[VERIFY'`
  across all .md is 214, but ~90 of those live in meta files — inbox reports, LOOPLOG,
  this file — the queue script's wiki-page count is the real number). Waves 9–11 resolved
  ~20 markers incl. Banzhaf-Lavery, Schularick, Hamilton/Foldvary, Clark, Ely; **fabricated
  Alaska PFD poverty figures purged from 4 pages** (Goldsmith correction now the cited line).
- **Old-backlog items verified shipped and retired**: objections 9→13 (credit-cycles,
  homevoter, revenue-insufficiency, transition-shock, assessment steelmen all live);
  WS-TECH-RENTS follow-up research pages (meade-report, schwerhoff ×2); concepts/
  public-land-leasing + concepts/data-rents backfilled; texts/ program at 12 pages
  (Agrarian Justice → Crime of Poverty → Irish Land Question → People's Budget cluster …);
  people waves from PR #14 book scanning (10 of 14 author pages live); spectrum/congestion/
  resource/carbon FINDs (geoism table has 5 evidenced rent domains); TOP-16 16/16; all 10
  Hermes w1 discovery reports triaged and consumed.
- **SPN Wayback sweep script** added (scripts/spn_sweep.sh — link-rot insurance).

## Addendum — loop session 2026-07-11 (waves 1–5 on claude/wiki-loop-2026-07-11)

**Done (see wave commits 75b4503 / 620c8e5 / 46a806b / ed8f40b + this one):** taxing-tech-rents
synthesis; finance-rents + IP-rents lanes CLOSED (WS-GEOISM complete); landlords page 10/5;
Doucet Parts 1&3 de-referenced + shortlist ingested; GSMS casino-dividend primary; symmetry-
decrement objection steelman; BC/Vancouver scope split + vancouver-empty-homes-tax (EHT 3%,
never 5% — the 5% was reversed May 2023 pre-levy); Feldstein-1977/Tideman-2002 incidence pair;
Wertzuwachssteuer + Kiautschou→Sun lineage (Silagi-sourced, caveated); site-value GE cluster;
mohammad-rail 7 markers resolved via the Imperial PhD-thesis route; terminology house style
ruled (EDITORIAL §6). **PD program:** Garden Cities (43.7k w), Progress & Poverty (177k w,
Memorial Ed. 1898), **Wealth of Nations (381.9k w, Georgist-lens book page)** all in
sources/publicdomain/.

**New queue items:**
- [ ] [READ&MINE] tier:T2 status:todo — DEEPEN-SCAN Progress & Poverty: mine the full text
      systematically into argument pages (Scan Depth currently Medium; target Heavy).
- [ ] [READ&MINE] tier:T2 status:todo — DEEPEN-SCAN Wealth of Nations beyond Book V Ch. II /
      Book I (Light outside the mined chapters); candidate: Smith on primogeniture/entails
      (Book III) for the land-concentration pages.
- [ ] [SYNTHESIZE] tier:T3 status:todo — concepts/canons-of-taxation stub (two linking pages
      now exist: books/wealth-of-nations, concepts/land-value-tax).
- [ ] [FIND] tier:T2 status:todo — Doucet Part-1 minors still unregistered: Steven Cord ~24%
      estimate, Ebeling federal-lands figure, PLACES Lab ML estimate.
- [ ] [VERIFY] tier:T1 status:recurring — remaining channels: needs-book-copy 6 (incl. Daniel
      Francis L.D. Taylor bio), Foldvary-reply Springer paywall (needs institutional access),
      natural-common-wealth independent assessment (genuine forage).
- SPN sweep: retry pass running (first pass 163 archived / 205 retryable overload fails).
- [ ] [READ&MINE] tier:T2 status:todo — Hoyt 1933 One Hundred Years of Land Values in Chicago:
      PD CONFIRMED 2026-07-11 (no CCE renewal 1959-62; IA scan open) — now eligible for the
      sources/publicdomain/ channel (xxxii+519pp; the 18-year cycle chapter is the priority mine).

## Steady state — end of loop session 2026-07-11 (16 waves)
All workable queues cleared. What remains needs inputs beyond this environment:
- [ ] [VERIFY] tier:Floyd — book-copy channel (~10 items): Harrison Boom Bust Ch.7 / Ricardo's
      Law Ch.11 / Power in the Land pagination, Reid Secondary Banking Crisis, Cannon Land
      Boomers, Jackson Crabgrass Frontier, Samuelson Economics editions, Daniel Francis L.D.
      biography, Barnes/Widerquist-Howard book texts (see hermes-workorder + queue).
- [ ] [VERIFY] tier:Floyd — institutional access: Foldvary RAE 27(4) reply full text;
      Cunningham JUE regression tables; Light JUH 2010.
- [ ] [VERIFY] status:calendar-gated — 2026-forecast markers (year-end); Duggan governor race
      (Nov 2026) for the Detroit LVT revival; Oxford Review cycle piece.
- [ ] Publishing: merge claude/wiki-loop-2026-07-11 (carries BOTH campaigns, 770 pages,
      lint 0/0) then Ghost-sync; wiki-problems/wiki-benefits tags exist on Ghost already.
