# BACKLOG.md — Wiki Improvement Queue

## ⟳ RESUME HERE (updated 2026-07-15, session udw74p — post-deploy)

**CLAIM: the entire Slack-candidates lane (issue #24 waves + TIER-2 citation wave) is owned by
session udw74p on branch `claude/slack-research-triage-udw74p` — see LOOP.md "Claiming work".
Other sessions: pick a different BACKLOG lane or coordinate via a comment on the merge PR.**

**State:** branch `claude/slack-research-triage-udw74p`, all pushed through 26b4d67; lint 0
errors, 827 pages, 0 orphans; registry 1,098 rows, 0 dead links. Issue #24 CLOSED (waves
29-31: 25 research entries + universal-vs-targeted objection page). **Ghost DEPLOYED
2026-07-15** — full 827-page sync (25 created); key auto-resolves from renamed vaults via
scripts/_secrets.py (op item get fallback for the em-dash item name).

**Standing rules in force:** Floyd's UBI scope rule (EDITORIAL §0, 2026-07-15 — UBI only
with rent/commons tie); loop priority = enrich benefits/problems/objections lanes.

**Reconciliation pass (2026-07-18, T2 worker, BACKLOG.md-only):** audited every open item in
NOW/NEXT/GATED-PARKED (plus the addendum logs below them) against actual repo state — lint,
LOOPLOG, registry.csv, sources/verification-queue.md, sources/public-domain-texts.md. Roughly
two-thirds of open items were already done (files existed, ledgers reconciled, LOOPLOG recorded
completion weeks earlier) but left unchecked. Marked done/partial/refreshed below; this lane's
plan and claim are untouched. See the bottom of this file for the audit's own summary note.

**Next iteration plan (in order):**
1. TIER-2 citation wave continuation — remaining ~90 scope-relevant rows in
   `sources/slack-research-triage-2026-07-14.json` (tier=TIER2, Status still "Not scanned"),
   worked BY TARGET PAGE with the delta rule; flip cited rows to Referenced. Sub-batches
   done so far: SWF proposals, US LVT activity, Korea politics, NEF, Equal Right.
2. Parked research-entry candidates: NYC 1920s new-building tax exemption (primary sources
   needed — the morehousing post is navigation-tier); Fossum Petro-Canada (books/ page,
   needs text access); Hope-Limberg (only if a taxing-the-rich-vs-rents angle emerges).
3. Then fall through to the NOW lanes below (VERIFY burn-down; problems/benefits stub waves).
4. Ghost re-sync after each committed wave now that credentials work:
   chunked `xargs -a <filelist> python3 -u scripts/sync_to_ghost.py` (foreground shells only —
   background shells lack OP_SERVICE_ACCOUNT_TOKEN); or single files for small waves.


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

## NOW (opened 2026-07-10; 2026-07-18 reconciliation — nearly every lane below is DONE, see
## per-item evidence. The live NOW work is upstream in RESUME HERE's TIER-2 continuation.)

### Problems/benefits Phase 2 — stub waves (the main event; acceptance rule EDITORIAL §5b:
### ≥2 big-name anchors claim-level verified before leaving stub, counter-evidence mandatory)
- [x] [PROBLEM-BUILD] tier:T2 status:done (verified 2026-07-18) — problems 1–6 all shipped and
      well past the acceptance bar: rising-land-costs-drive-poverty.md (9/5 anchors),
      homelessness-is-housing-cost-problem.md (5/5), housing-unaffordability-is-a-land-
      problem.md (11/5 — the "first stub" is long since expanded), rent-seeking-drags-
      growth.md (7/5), young-locked-out-of-land-wealth.md (7/5), speculative-vacancy-
      wastes-cities.md (8/5). Evidence: `python3 scripts/lint_wiki.py` COVERAGE block shows
      all 6 at ≥5 supporting papers (well above EDITORIAL §5b's ≥2-anchor bar).
- [x] [BENEFIT-BUILD] tier:T2 status:done (verified 2026-07-18) — benefits 7, 8, 10 all shipped:
      taxing-land-raises-productivity.md (13/5), lvt-improves-housing-affordability.md (11/5),
      rent-dividends-reduce-poverty.md (8/5). Benefit 9 (split-rate-increases-construction.md)
      also at 15/5. All confirmed via lint COVERAGE block.
- [x] [PROBLEM-BUILD] tier:T1 status:done (verified 2026-07-18) — justice pair 11–12 shipped:
      narratives/land-justice-and-indigenous-reconciliation.md and narratives/land-and-the-
      black-white-wealth-gap.md, both `last_reviewed: 2026-07-18`, both hold the intersection
      framing (shared diagnosis / divergent remedy) without overclaiming.
- [x] [SYNTHESIZE] tier:T1 status:done (verified 2026-07-18) — indexes are concepts/problems.md
      and concepts/benefits.md (not concepts/the-problems.md/the-benefits.md as literally
      named here — stale filenames, corrected). Checked: all 6 problem pages and all 4 benefit
      pages above are listed in their respective index. Recurring task — recheck each time a
      new problem/benefit page ships.

### People stubs from book scanning (sources/inbox/T1-TODO-people-pages-from-book-scanning.md)
- [x] [EXPAND] tier:T2 status:done (Wave 12a, verified 2026-07-18) — all 4 remaining authors
      now have pages: people/ronald-burgess.md, people/richard-noyes.md, people/eric-
      goldman.md, people/david-redfearn.md (all stub:false). All 14 listed authors are live.
      NOTE: the source TODO file is still at sources/inbox/ (not moved to consumed/) — a
      one-line housekeeping move, out of scope for this BACKLOG-only pass; flagged for the
      next session touching sources/inbox/.

### VERIFY burn-down (queue regenerated this shift: 121 markers on wiki pages)
- [x] [VERIFY] tier:T1 status:steady-state (verified 2026-07-18) — queue is now down to **2
      markers total**, both structurally blocked, not actionable by scouting:
      research/giovannoni-labor-share-decomposition.md (needs-book-copy) and research/august-
      rental-financialization.md (needs-unblocked-web, T&F paywall). See
      sources/verification-queue.md (regenerated 2026-07-18). This is steady state, not a
      to-do list — recurring only in the sense that new pages may add markers; there is
      currently nothing to burn down.
- [x] [FIND] tier:T2 status:done (verified 2026-07-18) — the needs-new-source items this line
      named are all resolved: Cherokee/GSMS casino-dividend primary → research/great-smoky-
      mountains-casino-dividend.md; Letchworth empirical data → places/letchworth.md +
      narratives/community-creates-land-value.md; COST self-assessment evidence → the
      radical-markets research cluster (research/vickrey-counterspeculation-auctions.md,
      research/buterin-on-radical-markets.md, concepts/harberger-tax.md); symmetry/decrement
      objection steelman → objections/symmetry-decrement-objection.md (full page, not a stub).

### Public-domain texts program (sources/public-domain-texts.md; 12 texts/ pages live)
- [x] [READ&MINE] tier:T2 status:done (verified 2026-07-18 against sources/public-domain-
      texts.md, which is the ledger of record) — every title this line still listed as a
      "next target" is ingested: Mill *Principles* (sources/publicdomain/principles-of-
      political-economy.md, ledger-reconciled 2026-07-18 with a documented Laughlin-abridged-
      edition scoping decision), *Progress & Poverty* (texts/progress-and-poverty-full-
      text.md, ledger-reconciled 2026-07-18), *Garden Cities* (sources/publicdomain/garden-
      cities-of-to-morrow.md), Hoyt 1933 (sources/publicdomain/hoyt-100-years-chicago-land-
      values.md, 35,499 lines — supersedes the earlier "do NOT ingest yet" verdict). Pigou's
      *Economics of Welfare* was deliberately NOT ingested (a considered decision, not a gap):
      only the 1920 1st ed. is PD-clear, and its LVT-relevant ~15pp were extracted as quotes
      into research/pigou-land-taxation.md instead of a full `texts/`/`publicdomain/` page —
      see the ledger's own reasoning. *Life of Henry George* also confirmed reconciled. This
      program line can retire; any further PD acquisitions should open as a fresh line
      referencing sources/public-domain-texts.md directly.

---

## NEXT (pick up when a NOW lane clears)

- [x] [SYNTHESIZE] tier:T1 status:done 2026-07-17 — public-choice "government will waste
      the rent": folded into objections/public-choice-critique.md (which already carried
      the Leviathan side) as objection prong 4 (Buchanan's Level-2/3 budget rent-seeking +
      Niskanen) and response move 5 (Buchanan's own nondifferential-distribution escape
      valve = the dividend design; fiscal-illusion visibility). A separate page would have
      duplicated the existing one.
- [x] [FIND] tier:T2 status:done (verified 2026-07-18; also recorded in the 2026-07-11
      addendum below as "WS-GEOISM complete" but never checked off here) — WS-TECH-RENTS
      remaining discovery all shipped: (a) DSTs-as-tried → research/digital-services-tax-
      incidence.md; (b) attention/ad rents → research/romer-digital-advertising-tax.md;
      (c) rent dissolution vs capture → research/dma-interoperability-dissolution.md;
      (d) is-it-rent diagnosis update → research/furman-review-digital-competition.md +
      research/korinek-stiglitz-ai-rents.md. Gated synthesis also live: concepts/taxing-
      tech-rents.md (instrument comparison).
- [x] [FIND] tier:T2 status:done (verified 2026-07-18; same stale-checkbox situation as
      above) — WS-GEOISM domain sweep complete: financial rents & seigniorage →
      research/bezemer-hudson-finance-is-not-the-economy.md, research/borio-financial-
      cycle.md, research/philippon-great-reversal.md, research/philippon-finance-
      efficiency.md; IP-rents remainder → research/boldrin-levine-against-intellectual-
      monopoly.md, research/prizes-vs-patents.md. concepts/data-rents.md already live.
- [x] [READ&MINE] tier:T2 status:done (pre-2026-07-17, confirmed this date) —
      research/foldvary-reply-gochenour-caplan exists (abstract-sourced, honestly flagged);
      full text re-confirmed paywall-blocked everywhere 2026-07-17 (foldvary.net is
      domain-squatted; bepress discontinued; SSRN/RG bot-gated). Institutional access only.
- [x] [EXPAND] tier:T2 status:done (stale item, closed 2026-07-17) — lvt-reduces-sprawl
      gauge already at 6/5; brueckner-kim exists as research/brueckner-kim-sprawl.md,
      correctly wired as challenged_by (theoretical ambiguity); McGrath 2005 already in
      supported_by. No work was needed.
- [x] [READ&MINE] tier:T2 status:done (verified 2026-07-18 against sources/inbox/T1-TODO-
      doucet-parts-1-3-dereferencing.md, the citation-ledger audit itself) — de-referencing
      is done and its own top-ranked MISSING shortlist is now ingested: AEI Land Price
      Indicators → research/aei-land-price-indicators.md, Bencure iLVM →
      research/bencure-ilvm-baybay-philippines.md, Saez-Zucman → research/saez-zucman-
      wealth-inequality.md, Barr-Smith-Kulkarni → research/barr-smith-kulkarni-manhattan-
      land.md, Kolbe adaptive-weights companion + Artola Blanco Spain + McKinsey balance
      sheet all have registry rows. landlords-outcome Ch. 21 cluster complete: Borge-Rattsø,
      Capozza-Green-Hendershott, Hilber (hilber-capitalization-synthesis.md + hilber-
      vermeulen-england-supply.md), Buettner, and Choi-Sjoquist (research/site-value-ge-
      simulations.md) all exist. Remaining tail is low-value registry-rows-only per the
      TODO file's own tail list (Yalpir & Unel, Kilić, Raslanas, Aragonés-Beltrán, Xue,
      Kettani) — not worth a dedicated wave; move sources/inbox/T1-TODO-doucet-parts-1-3-
      dereferencing.md to consumed/ next time inbox/ is touched.
- [x] [FIND] tier:T2 status:done (verified 2026-07-18) — research/raley-citizens-dividend.md
      exists and is wired (see concepts/citizens-dividend.md, narratives/citizens-dividend-
      narrative.md).
- [x] [EXPAND] tier:T3 status:done (verified 2026-07-18, recurring — recheck each wave) —
      mechanical debt is at zero right now: `python3 scripts/lint_wiki.py` shows 0 "not
      annotated" Sources warnings, 0 thin-article warnings, 0 quote-cap warnings (11 total
      warnings, all unrelated — banned-certainty words + the 2 live VERIFY markers). BC SVT
      rates sub-item already closed per the note kept here. Since this is explicitly a
      recurring/batched debt category rather than a one-shot deliverable, it isn't "gone"
      forever — flag it again if a future lint run shows nonzero counts.
- [x] [EXPAND] tier:T2 status:done (verified 2026-07-18) — both cohesion items closed:
      BC/Vancouver scope split executed (research/vancouver-empty-homes-tax.md +
      places/vancouver + places/british-columbia now split per the 2026-07-11 addendum
      below); terminology normalization ruled and in force (EDITORIAL.md §6 "Terminology
      (house style, ruled 2026-07-11)" — citizen's dividend / single-tax / 18-year-cycle
      forms all specified).
- [x] [EXPAND] tier:T3 status:done (verified 2026-07-18) — all three named stubs backfilled:
      concepts/sector-model.md (118 lines, stub:false), concepts/margin-of-production.md
      (110 lines, stub:false), organizations/progress-and-poverty-institute.md (backfilled
      per LOOPLOG 2026-07-06). "Candidate events/orgs from the lloyd-george/BC backfills" is
      too vague to verify against a specific artifact — left as CANNOT VERIFY; if this is
      still a live idea it needs a named candidate list to be actionable.

---

## GATED / PARKED (surface these, don't chase)

- ~~Phase 3 directory split~~ EXECUTED 2026-07-10 on Floyd's sign-off (`outcomes/` → `problems/` + `benefits/`, indexes at /wiki/problems/ + /wiki/benefits/, lint + scripts + EDITORIAL updated). Old line kept for record:
- **Phase 3 directory split** (`outcomes/` → `problems/` + `benefits/`, redirects, inbound
  link rewrite, registry/inventory rebuild) — **GATED on Floyd's sign-off** of the Phase-1
  grouping. Do not start early; the split touches 400+ pages of links.
- **learning-paths** — **PARKED by Floyd.** Do not start.
- **Provenance attestation** (books/economic-theory-in-retrospect, books/rethinking-
  economics-land-housing) — **still genuinely blocked** (re-verified 2026-07-18: both pages
  still carry the unresolved `[BLOCKED — legal provenance attestation...]` flag in their
  `provenance` field); scan-depth upgrades stay frozen until Floyd confirms a legitimately
  owned/licensed copy of each. Note: Rothstein *Color of Law* (justice page 12,
  narratives/land-and-the-black-white-wealth-gap.md) is now cited via secondary sourcing —
  the full book is still wanted for deeper mining but isn't blocking the page.
- **needs-book-copy channel — now 1 marker, not 8** (re-verified 2026-07-18 against
  sources/verification-queue.md: only research/giovannoni-labor-share-decomposition.md).
  The broader wanted-books DEEPEN-SCAN wishlist (sources/wanted-books.md, ~20 titles across
  3 tiers) is separate and still substantially open — unblock as Floyd supplies copies;
  spawn one [READ&MINE] per title as they land.
- **needs-unblocked-web channel — now 1 marker, not 23** (re-verified 2026-07-18: only
  research/august-rental-financialization.md, T&F paywall). Exa people-enrichment sweep
  status unchanged — proxy allowlist (api.exa.ai, ssrn, nber, worldbank, etc.) or route via
  Hermes.
- **Hermes lane — now 2 items, not 31** (re-verified 2026-07-18 against sources/hermes-
  workorder.md, regenerated same day: the 2 needs-book-copy/needs-unblocked-web items above,
  routed there because only Hermes's environment can reach them). T1 reviews deliveries
  against provenance rules before merge.
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
- [x] [READ&MINE] tier:T2 status:done 2026-07-18 — DEEPEN-SCAN Progress & Poverty executed:
      Book-by-Book scout mapped all 10 Books against existing coverage; four T1-approved
      enrichments shipped (Bk IX -> benefits/taxing-land-raises-productivity; Bk VI Ch I
      six-way rival-remedies critique -> objections/nationalization-solves-the-land-problem;
      Bk VII Ch III no-compensation position, paired with Mill's design ->
      objections/lvt-transition-wealth-shock; Bk I -> concepts/wages-fund-doctrine
      stub-to-full upgrade). Registry Scan Depth bumped Medium -> Heavy. Scout's do-NOT-do
      list honored (Bk III interest theory, Bk IV granularity, Bk VII history, Conclusion).
- [ ] [SYNTHESIZE] tier:T1 status:blocked-on-Floyd — the one remaining P&P gap: Book X
      (Law of Human Progress — association+equality theory of civilization, Rome analogy)
      has zero wiki footprint. It is George's most speculative, least evidential material;
      a concepts/law-of-human-progress page is a legitimate but discretionary addition.
      FLOYD'S CALL whether the wiki should carry it.
- [x] [READ&MINE] tier:T2 status:done (verified 2026-07-18) — DEEPEN-SCAN Wealth of Nations:
      the named candidate (Smith on primogeniture/entails, Book III Ch. II) is mined and
      verified verbatim into people/adam-smith.md and concepts/land-monopoly.md (both note
      "verified verbatim against the repo-hosted text 2026-07-11/12"). Registry Scan Depth
      is Heavy. Beyond Book I/III/V (this line's ask), no further systematic gap identified.
- [x] [SYNTHESIZE] tier:T3 status:done (verified 2026-07-18) — concepts/canons-of-taxation.md
      exists (stub:false).
- [x] [FIND] tier:T2 status:done (verified 2026-07-18) — all three now registered and wired
      into problems/land-rent-could-fund-government.md: Steven Cord (registry.csv row 570),
      Ebeling (row 571), PLACES Lab (row 572); people/steven-cord.md and organizations/
      places-lab.md also exist.
- [x] [VERIFY] tier:T1 status:done/steady-state (verified 2026-07-18) — needs-book-copy is
      down to 1 (not 6; Daniel Francis L.D. Taylor bio no longer listed there — people/l-d-
      taylor.md exists and covers the subject from other sources); Foldvary-reply Springer
      paywall still genuinely blocked (unchanged, see NEXT section above); natural-common-
      wealth independent assessment → research/natural-common-wealth-economic-rent-
      canada.md exists.
- SPN sweep: retry pass running (first pass 163 archived / 205 retryable overload fails).
      [Not re-verified this pass — no current SPN sweep log checked; leave as-is, low stakes.]
- [x] [READ&MINE] tier:T2 status:done (verified 2026-07-18 against sources/public-domain-
      texts.md) — Hoyt ingested: sources/publicdomain/hoyt-100-years-chicago-land-values.md
      (35,499 lines), ledger-reconciled 2026-07-18.

## Steady state — end of loop session 2026-07-11 (16 waves)
All workable queues cleared. What remains needs inputs beyond this environment:
- [ ] [VERIFY] tier:Floyd — book-copy channel: **re-verified 2026-07-18, this list is stale.**
      Current sources/wanted-books.md still wants (unstruck): Harrison *Power in the Land*
      pagination detail, Reid *Secondary Banking Crisis*, Cannon *Land Boomers*, Jackson
      *Crabgrass Frontier*, Samuelson *Economics* editions, Barnes *Who Owns the Sky?*.
      Widerquist-Howard PFD volume got a partial unblock (Ch. 12 obtained 2026-07-14 via a
      contributor PDF; Goldsmith's central Ch. gap still open). Daniel Francis L.D. Taylor
      biography specifically is no longer needed as a blocker — people/l-d-taylor.md exists,
      built from other sources. Genuinely still Floyd-gated; not actionable by scouting.
- [ ] [VERIFY] tier:Floyd — institutional access: Foldvary RAE 27(4) reply full text (still
      paywalled, re-verified 2026-07-18) and Cunningham JUE regression tables (still
      paywalled, research/cunningham-seattle-options.md documents the exhausted attempt) both
      still open. Light JUH 2010 — no page or registry row found for this title; unclear if
      it was ever started. Genuinely still Floyd-gated.
- [~] [VERIFY] status:calendar-gated — **partially resolved 2026-07-18:** the Oxford Review
      cycle piece is no longer calendar-gated — research/oxford-review-george-2025.md exists,
      fully ingested, no VERIFY markers, wired to objections/progress-and-poverty-outdated.md.
      Still genuinely gated: Duggan Michigan governor race (Nov 2026, hasn't happened yet) for
      the Detroit LVT revival; other 2026-forecast/year-end markers.
- [x] Publishing: status:done (verified 2026-07-18) — claude/wiki-loop-2026-07-11 was merged
      long ago; repo is now well past that state (834 pages, Ghost fully deployed through
      2026-07-15 per the RESUME HERE block above). This line is obsolete.

### Wave-20 flags (2026-07-12, next-wave review)
- DONE (same day): kolbe-berlin-land-value-map and barr-manhattan-land-values were Doucet-discovery duplicate stubs of the fuller verified pages (kolbe-berlin-land-value-appraisal, barr-smith-kulkarni-manhattan-land); folded, links repointed, registry repointed. The Barr stub also carried a $1.74T transposition of the verified $1.47T figure — corrected at the repointed link.

### Phase 2: legacy-article interlinking (planned 2026-07-12, Floyd approved "do it all"; starts after merge+publish)
608 published non-wiki articles on progress.org (2006-05 to 2026-06, still active). Plan:
1. **Tagging pass** (agents, read-only inventory then Ghost API tag updates): classify each article against the wiki topic taxonomy (align to wiki-research-* subcategories + portal topics); add topic tags. No content edits.
2. **Theme block** (needs Floyd/theme access OR per-article footer alternative): "From the Georgism Wiki" block rendering 3-5 wiki entries by shared tag. If theme editing is out of scope, fall back to API-inserted footer cards on the top-traffic slice only.
3. **In-text editorial links** (top ~50-100 articles by traffic/recency): 2-4 contextual /wiki/ links per article, inserted via Admin API with ?source=html; every edit diff-reviewed before update.
4. Reverse links: wiki pages may cite legacy articles as commentary/further reading only (never as evidence).
Ghost API state: 771 wiki posts published; next full sync adds guides/ + wave-21/22 pages (790 total) and needs the three stray unpublishes (kolbe-berlin-land-value-map, barr-manhattan-land-values, feldstein-1977-incidence-pure-rent).

### Phase 2 status (2026-07-12 evening)
- Tagging: DONE — 413/608 legacy articles tagged with wiki-research-* topics (georgism 151, lvt 136, finance 66, inequality 55, resources 44, urban 23, housing 22); 195 off-topic left untagged. Verified on-server, existing tags preserved.
- In-text wiki links: DONE for the top-100 slice — 87 articles edited (10 pilot + 42 batch A + 35 batch B), 284 links, every edit byte-identical lexical roundtrip + live-verified at /articles/<slug>/. Snapshots in session scratchpad (pilot-snapshots/, scale-snapshots/, scale-snapshots-b/). Method: lexical link-node surgery (scripts lexedit.py/scaleedit.py/deepdiff.py in session scratchpad — recreate from this description if scratchpad is gone: mirror link-node schema from real nodes, split text runs, PUT lexical without source param, deep-diff, restore on drift).
- FINDING: posts published ~2021 and earlier have lexical=null (HTML-only). The lexical method cannot edit them; extending in-text links to the older ~300 tagged articles would need the ?source=html path (roundtrip degradation risk — test on one sacrificial article first) or can simply be left to the theme block.
- Theme block: paste-ready install guide delivered to Floyd (from-the-wiki-theme-block.md); requires his Ghost admin (integration key cannot manage themes). Nav item "Wiki" -> /wiki/start-here/ also recommended, also Floyd-manual.
- Ghost admin manual queue (Floyd): install theme block; add nav item; hard-delete 4 drafts (_framework, kolbe-berlin-land-value-map, barr-manhattan-land-values, feldstein-1977-incidence-pure-rent) + empty "Outcomes" tag.

## Addendum — Slack deep-scan triage session 2026-07-14 (issue #24, branch claude/slack-research-triage-udw74p)

**Processed this session (wave 29):**
- Triaged all **516** candidates from `sources/slack-research-candidates.json`:
  **74 TIER-1** (academic/gov policy) · **117 TIER-2** (think-tank/long-form) ·
  **263 TIER-3** (news briefs — not registry-worthy) · **49 SKIP** (dupes, mirrors of
  already-ingested sources, homepages, ephemeral/social, 1 sci-hub). Per-URL map committed:
  `sources/slack-research-triage-2026-07-14.json`. 12 confirmed-dead URLs carried as
  "Dead link"; 2 dead+unidentifiable OECD numeric PDFs dropped.
- Registry: **+196 rows** (191 triage + 5 sources used by new entries), 10 rows corrected/flipped
  to Scanned. Dated export refreshed.
- **10 research/ entries shipped** (T2-drafted, T1-reviewed, all sources fetched):
  brown-land-speculation-lvt · cohen-coughlin-two-rate-taxation ·
  mintz-chen-capturing-resource-rents · dachis-buyers-beware-housing-barriers ·
  forget-mincome-town-with-no-poverty · bc-basic-income-panel-final-report ·
  pbo-guaranteed-basic-income-costing · openai-industrial-policy-intelligence-age ·
  imf-gen-ai-future-of-work · baunsgaard-vernon-windfall-profits.
  Claim-lane wiring: lvt-dampens-land-speculation +1 support; resource-rent-capture-works +2;
  rent-targeting-taxes-reduce-debt-bias +1; housing-unaffordability-is-a-land-problem +1;
  rent-dividends-reduce-poverty +1 challenger (BC panel); quasi-rents objection steelman +2;
  land-speculation-is-productive response +1; 5 concept pages enriched.

**Remaining / queued:**
- [x] [READ&MINE] tier:T2 status:done — **Loop wave 30 SHIPPED 2026-07-15** (12 entries + the
      universal-vs-targeted objection page + 12 dead-link repairs; see LOOPLOG). ~46 TIER-1 rows
      remain "Not scanned" — mostly StatCan data releases and reference documents that stay
      registry-only by design; genuine entry candidates left after Floyd's 2026-07-15 UBI scope
      ruling (EDITORIAL §0 — pure redistributive UBI struck from the queue: Clavet-Duclos-Lacroix,
      Corsica, JEC 1968, Senate Pate, IRPP BI volumes): Hope-Limberg tax-cuts-for-the-rich ·
      SWAY LVT/wealth-tax realist review (retitled in registry) · Fossum Petro-Canada (needs books/
      treatment) · Carney future-of-work speech · Walks Toronto polarization · Brown JPE follow-ups.
- [x] [REVIEW] tier:Floyd status:done — **UBI scope ruling, disposition RESOLVED** (Floyd,
      2026-07-15): namibia-big-pilot and de-schutter-poverty-beyond-growth DELETED on owner
      instruction (wiring unwound; registry rows retained as unscanned supplementary; Osterkamp
      companion rows dropped). Forget/BC-panel/PBO/World-Bank pages kept — wired as evidence on
      rent-dividend claims and the universal-vs-targeted objection. Future waves apply the rule
      at triage (TIER-2 wave: skip UBI items without a rent/commons tie).
- [~] [READ&MINE] tier:T3 status:in-progress claimed:claude/slack-research-triage-udw74p (2026-07-15) — **Slack TIER-2 citation wave** (scope-filtered per
      EDITORIAL UBI rule). Batch 1 done 2026-07-15 (SWF proposals landscape ×5, US LVT activity ×2 —
      7 rows Referenced). Remaining ~100 rows: work through by target page, citing only where the
      delta rule is satisfied and the rent/commons tie is real; skip pure-UBI and news-brief items
      (registry rows suffice). Candidates parked as future research entries rather than citations:
      PPI land-value-taxes-in-college-towns reports; the NYC 1920s new-building tax exemption
      episode (morehousing post is navigation-tier — needs primary sources).
- [x] [PROBLEM-BUILD/OBJECTION] tier:T1 status:done (Wave 30, 2026-07-15, verified 2026-07-18)
      — **objections/ubi-targeting-efficiency gap** closed: objections/universal-transfers-
      are-inefficient.md exists, steelmanned from the BC panel's 1,640 simulations exactly as
      asked, with both Woo's fixed-budget-framing critique and Forget's response wired in.
- [x] [VERIFY] tier:T2 status:done (resolved 2026-07-17, verified 2026-07-18) — the 8.5%
      hospitalization figure is independently corroborated via two non-BC-panel channels
      (IDEAS/RePEc published abstract + Green 2022's direct pagination-cited quotation of
      Forget 2011) — see research/forget-mincome-town-with-no-poverty.md's own "resolved on
      that basis" note. The utppublishing.com 403 is still up (re-checked), so this is
      resolved by independent corroboration, not primary-text access — flagged as such
      on-page; a first-hand read is still preferable if the paywall ever clears.
- [x] [BULK] tier:T3 status:done (Wave 30, 2026-07-15, verified 2026-07-18) — all 12 dead
      links repaired with verified-200 mirrors (per LOOPLOG's Wave 30 entry); registry.csv
      currently shows **0 dead links** (confirmed against the RESUME HERE block's own
      "registry 1,098 rows, 0 dead links" state).

**Skipped (with reasons, machine-readable in the triage JSON):** 13 already-ingested mirrors
(Jones-Marinescu WP, Goodhart-stimulus ×2, Schwerhoff ×2, Haughwout, DØRS, OECD WP620, England AJES,
Capitalism 3.0, Paine, Ricardo, Goldsmith ×2, Guettabi, Flomenhoft Vermont, Noah Smith) · 9 truncated
Slack-ellipsis URLs · 5 archive wrappers · 7 homepages/portals · 6 in-list dupes · ephemeral
attachments (Trello/Mailchimp) · petitions · 1 sci-hub link (EDITORIAL free/legal rule) · social/profile pages.

---

## Reconciliation pass, 2026-07-18 (T2 worker, BACKLOG.md-only — closes out the file-rot problem)

Audited every `[ ]`/`[~]` item in NOW, NEXT, and GATED/PARKED (plus the addendum logs strung
below them, which carry just as many stale checkboxes) against the actual repo: lint output,
LOOPLOG.md, sources/registry.csv, sources/verification-queue.md, sources/public-domain-texts.md,
sources/wanted-books.md, sources/hermes-workorder.md, and direct file/grep checks for the
artifact each item implied.

**Counts:** ~34 open items audited · **24 marked done** (file/registry/LOOPLOG evidence found)
· 5 left genuinely open (refreshed with current details) · 2 marked partial · 1 line judged
unverifiable-as-written (too vague to check against an artifact) · 1 line left untouched as
another session's active claim (Slack TIER-2 wave, udw74p).

**What's genuinely still open — the real next-wave menu:**
1. **DEEPEN-SCAN Progress & Poverty** to Heavy scan depth (full text is in, systematic mining
   into new argument pages is not) — NEXT section.
2. **Provenance attestations** for books/economic-theory-in-retrospect and books/rethinking-
   economics-land-housing — blocked on Floyd confirming a legitimately owned/licensed copy;
   not scoutable.
3. **wanted-books.md tier-1/2/3 wishlist** (~20 titles) — Floyd-gated book supply, not scoutable.
4. **Institutional-access channel** — Foldvary RAE 27(4) full reply text, Cunningham JUE
   regression tables, Light JUH 2010 (status unclear, possibly never started) — Floyd-gated.
5. **Duggan Michigan governor race** (Nov 2026, hasn't happened) and other 2026 year-end
   calendar-gated markers.
6. Everything already flagged GATED/PARKED by Floyd (learning-paths, Phase 3 split docs,
   registry Sheet import, gameofrent.com/P&P Substack scans) — unchanged, still correctly gated.

**Surprising finding:** the rot runs both directions. Most stale items were quietly finished
(problems/benefits Phase 2, both WS-TECH-RENTS/WS-GEOISM sweeps, the Doucet de-referencing
cluster, the UBI-targeting-efficiency objection page, the dead-link mirror hunt) but never
checked off — but a few *counts* were stale in the other direction too: the GATED/PARKED
section's needs-book-copy and needs-unblocked-web marker counts (8 and 23) were each roughly
an order of magnitude too high; the real current counts are 1 and 1. The Hermes lane's "31
items" is now 2. None of this reflects badly on prior sessions — the queue-regeneration scripts
(`verification_queue.py`) run fresh each time and the file was simply never re-synced against
their output.
