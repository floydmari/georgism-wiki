# LOOPLOG.md — What each loop actually did

`LOOP.md` is the *prescriptive* prompt (how to run a loop). This file is the *descriptive*
record: the concrete changes each loop made to get the wiki (and its browsable preview) to its
current state. Source of truth is the git history on the working branch
(`git log --stat origin/main..HEAD`); every commit hash below is real and inspectable with
`git show <hash> --stat`.

---

## The anatomy of one loop

Every content loop is the same generator–critic shape:

1. **Pick** the top actionable task from `BACKLOG.md` (tier-matched).
2. **Generate** — a T2/T3 subagent (Sonnet/Haiku) drafts **one file**, self-lints, and *reports*
   the new sources it used + suggested inbound links. It does **not** edit shared files
   (`sources/registry.csv`, other articles) and does **not** commit. Cheap output is never trusted
   blind.
3. **Review** — the T1 orchestrator (Fable, or Opus as stand-in) verifies claim-level citations and
   that each claim's *language matches its source's strength*, registers the new sources in
   `sources/registry.csv`, and wires **bidirectional + inbound links** so the new page isn't an
   orphan.
4. **Gate** — `python3 scripts/lint_wiki.py` must exit 0 (broken links, missing fields, one-way
   links, banned-certainty words, registry drift all block).
5. **Preview** — `python3 scripts/build_preview.py` re-renders the branch; the new page shows a
   "changed vs main" badge.
6. **Commit** — one task per commit, message `content: … (TYPE tier:Tn, reviewed)`, pushed to the
   branch (PR #2). Publishing to Ghost is a separate, credential-gated step (not run this session).

Honest markers (`[CITATION NEEDED]` / `[VERIFY]`) are left in place rather than fabricating a
source — several academic hosts (`ifs.org.uk`, gutenberg, even wikipedia) return 403 through this
environment's egress proxy, so some primary quotes couldn't be fetched first-hand.

---

## Phase 0 — the infrastructure that built the preview itself

These commits aren't content loops; they built the machine (including `build_preview.py`, the
preview you're looking at). Baseline before any loop: **139 articles**.

| Commit | What it added |
|--------|---------------|
| `355d179` | The whole system: `EDITORIAL.md`, `QUALITY_RUBRIC.md`, `BACKLOG.md`, `LOOP.md`, `scripts/lint_wiki.py`, **`scripts/build_preview.py`**, `sources/registry.csv` (seeded, 154 rows), narratives category wiring |
| `e9ed0c1` | `build_preview.py` single-file mode (`preview/wiki-preview.html`, the shareable artifact) |
| `ba3aedf` | Preview design: dual light/dark theme, serif titling, subject-grounded palette |
| `50d3213` | `scripts/_secrets.py` — resolve Ghost creds from env or 1Password (`op`) |
| `220535b` | `.claude/hooks/session-start.sh` + `settings.json` — install deps + load Ghost key per session |

---

## The content loops

Each row is one iteration of the loop above. File lists are exactly what changed in that commit.

| Loop | Commit | Tier / model | Task | Files changed | Effect on the preview |
|------|--------|--------------|------|---------------|-----------------------|
| **1** | `dcc4841` | T2 Sonnet → T1 review | Mirrlees Review research page | **+**`research/mirrlees-review.md`; reviewer edits to `concepts/deadweight-loss.md`, `concepts/land-value-tax.md`, `outcomes/land-rent-could-fund-government.md`, `outcomes/lvt-can-replace-capital-taxes-without-efficiency-loss.md` (bidirectional links); `sources/registry.csv` | research 47→48; one new page with a "changed" badge |
| **2** | `b756805` (+ `c725634` backlog) | **T1 Fable** | Narrative framework + *Unearned Increment* exemplar | **+**`narratives/_framework.md` (internal index), **+**`narratives/unearned-increment-narrative.md`; `scripts/lint_wiki.py` + `scripts/sync_to_ghost.py` (skip `_`-prefixed files); inbound links from `concepts/unearned-increment.md`, `events/1909-peoples-budget.md`; `sources/registry.csv` (+6 sources); `BACKLOG.md` | **the entire `narratives` category appears** in the preview; +1 public page |
| **3** | `07929b8` | T2 Sonnet → T1 review | Narrative: *Tax Land, Not Labor* | **+**`narratives/tax-land-not-labor.md`; inbound link from `narratives/unearned-increment-narrative.md`; `sources/registry.csv` (+Friedman) | narratives 1→2 |
| **4–7** | `c27e3aa` | T2 Sonnet ×4 (parallel) → T1 review | Wave A batch | **+**`narratives/the-rentier-economy.md`, **+**`narratives/the-tax-you-cant-dodge.md`, **+**`research/ryan-collins-rethinking-land-housing.md`, **+**`research/foldvary-public-revenue.md`; inbound links from `people/fred-foldvary.md`, `people/michael-hudson.md`, `people/josh-ryan-collins.md`, `objections/land-cannot-be-assessed.md`; `sources/registry.csv` (+6, incl. Foldvary/Burgess correction) | narratives 2→4, research 48→50 |

**Notes on individual loops:**
- **Loop 2** was the keystone T1 job: it *designed* the 12-narrative taxonomy (the blueprint the T2
  loops then fill) and wrote one fully-worked exemplar. It also caught a slug collision
  (`unearned-increment` already existed as a concept) and introduced the `-narrative` suffix
  convention + the `_`-prefix "internal, don't publish" rule.
- **Loops 4–7** ran as **five parallel subagents on disjoint files** (one of the five,
  `tax-land-not-labor`, landed first as Loop 3). This is why they share one commit: the orchestrator
  reviewed them together, batch-registered sources, and de-orphaned all four at once.
- **Loop 7** caught a **data error in the source registry**: "Public Revenue Without Taxation" was
  mis-attributed to Fred Foldvary (it's Ronald Burgess). The agent refused to fabricate around it,
  wrote the page about Foldvary's *real* 1994 book, and flagged it; the registry row was corrected.

---

## Net effect (baseline → now)

| Metric | Before loops | After Loop 7 |
|--------|--------------|--------------|
| Public articles | 139 | 146 |
| `narratives/` | 0 | 4 (+1 internal `_framework` index) |
| `research/` | 47 | 50 |
| `sources/registry.csv` rows | ~154 | 166 |
| Lint errors | 0 | 0 (green after every loop) |
| Orphan pages among the new set | — | 0 (all de-orphaned in review) |

Every new page is cited at claim level, cross-linked in both directions, and lint-green. Honest
`[CITATION NEEDED]`/`[VERIFY]` markers remain where the egress proxy blocked a primary source —
these are transparent to-dos, not gaps hidden by fabrication.

## Wave 3 — loops 8–22 (2026-07-03, "deep-scan originals + commonwealth.ca + 18.6-yr cycle")

15 loops run as parallel T2 subagents on disjoint files, orchestrator (T1) reviewing each:
commits `ad60457`…`a9167c7` + the loop-15 cross-linking commit.

| Loops | What | Files |
|-------|------|-------|
| 8–13 (deepen-scans) | Dedicated research pages for Hudson *Killing the Host*, Churchill *The People's Rights*, Mazzucato *Value of Everything*, Autor et al. *Superstar Firms*, Mill *Principles* Book V, Rothbard *Single Tax* | +6 `research/` pages; Scan Depths Light→Medium (Heavy honestly withheld — primary texts proxy-blocked) |
| 14–15 (George originals) | *The Land Question* (→Heavy) and *Social Problems* deepened in place from thin stubs | 2 rewrites |
| 16–19 (commonwealth.ca) | Org page, *Natural Common Wealth* flagship report, distributional-impacts study, British Columbia place page — **resolves the CWC git↔Ghost drift with git as master** | +4 pages |
| 20–21 (18.6-yr cycle) | `research/progress-18-6-year-cycle` + `narratives/land-speculation-causes-cycles` (5th narrative) | +2 pages |
| 22 | Bulk orphan cross-linking pass — **orphans 24 → 0**, warnings 319→290, incl. one pre-existing mislabeled-link fix (ebenezer-howard) | 28 files, link edits only |

Notable judgment calls the loop made: Autor et al. wired as `challenged_by` on the capital-share
outcome (first use of the field — the honest-counterweight pattern working); the CWC distributional
agent **declined** to claim `supports_outcomes: [land-value-tax-can-be-progressive]` because the
study's raw finding (LVT alone regressive by income, progressive only with the credit design)
nuances rather than supports it. Net: 146→158+ pages; registry 166→173 rows.

## Process fixes discovered by running the loops

- **2026-07-03 — Google Sheet mirror went silently stale.** Loops 1–7 correctly updated
  `sources/registry.csv` in git, but the write-back to the master Google Sheet (the source index
  Floyd actually reads) never ran: the environment's Drive tooling can create files but cannot edit
  cells in the existing Sheet, and the loop's "sheet sync pending" log line was invisible. Floyd
  caught it. Fixes: (1) a dated snapshot spreadsheet with a Δ column was created in Drive
  ("Georgism Wiki — Source Registry (git sync 2026-07-03)"); (2) `scripts/export_registry_for_sheet.py`
  now derives the delta mechanically from `git diff` of the registry, so the report can't depend on
  memory; (3) `LOOP.md` step 3 makes the sheet mirror mandatory-and-loud — every registry-touching
  iteration must either push a snapshot or add a visible `[SHEET-SYNC]` task to `BACKLOG.md`;
  (4) a durable in-place write-back via a Sheets-API service account is queued in the backlog.
  Also caught in the same review: the Ryan-Collins registry row hadn't been flipped to
  `Complete` when its page shipped — LOOP.md now states the registry-row flip is part of the same
  iteration, not a follow-up.


## Wave 4 — evidence build-out, waves 1-2 of the 50-paper campaign (2026-07-03/04)

Goal: every outcome >= 5 supporting papers (gauge in lint_wiki.py COVERAGE block). 16 new
research pages committed across two 8-9-agent parallel waves + salvage after a session-limit
interruption (recovered entirely from git state — proof the loop survives context resets):
PFD/dividends cluster (Jones-Marinescu, Widerquist-Howard, Hartwick, Segal), capitalization
cluster (Oates 1969, Gibbons-Machin, Mohammad meta-analysis), incidence trio (Mieszkowski,
Zodrow, Hamilton-as-challenger), efficiency trio (OECD 2008, Arnold EJ 2011, + Mirrlees),
Knoll AER 2017, Cunningham 2006, Hsieh-Moretti 2019, De Loecker-Eeckhout-Unger 2020.
Coverage 19/65 -> 41/65. Pattern proven: concurrent forward-links get temporarily neutralized
to keep lint green, restored when the sibling lands. Remaining queue + resume protocol at the
top of BACKLOG.md.


## Wave 5 — Task 0 discovery sweep + campaign completion: COVERAGE 14/14 (2026-07-04)

The session that closed the evidence campaign. Three phases, ~45 subagents, orchestrated from a
single T1 session (survived one session-limit interruption mid-wave; recovered from git + agent
output files):

**Task 0 — one-time full-corpus DISCOVERY-SWEEP.** 10 report-only T2 agents over all 176 pages in
chunks; 29 deduped candidates; T1 triage accepted 20 / rejected 9 with reasons (recorded in
BACKLOG's stub queue). 5 stub-writer agents created all 20 sourced stubs per EDITORIAL's standard
with inbound links wired. All three known misses confirmed and fixed (homer-hoyt, david-lloyd-george,
vancouver). First flywheel round then backfilled homer-hoyt and vancouver to full pages.

**Evidence waves 3–5.** 32 new research pages across three 9-16-agent waves, every outcome wired
to ≥5 supporting papers. Coverage 1/13 → 14/14 (incl. the new 14th outcome
outcomes/corporate-profits-increasingly-rents, T1-written, supported by the tech-rents cluster:
De Loecker-Eeckhout-Unger, Furman-Orszag, Barkai, Philippon, Eeckhout; challenged by
Crouzet-Eberly intangibles + superstar-firms efficiency reading).

**Honesty calls the loop made (the pattern holding under pressure):**
- Gemmell-Grimes-Skidmore NZ verified as a NULL result for new construction → supports_outcomes:[],
  written into the split-rate outcome as a caveat instead of coverage.
- Piketty reclassified context-only by its own drafting agent's recommendation (the land
  decomposition is Rognlie's, not Piketty's) — the 5th capital-share slot went to Furman-Orszag's
  housing decomposition instead.
- Barkai wired as challenged_by on capital-share-rise-is-land while supporting the corporate-rents
  outcome — the same paper honestly cuts both ways.
- World Bank CWON 2021 re-wired by its agent from the developing-world outcome to
  land-rent-could-fund-government (wealth-accounting is scale evidence, not welfare evidence).
- The speculation outcome got a three-tier evidence map (phenomenon / mechanism / policy) so its
  6 supporting papers can't be misread as six tests of LVT.
- Norway explicitly REJECTED as a dividends cite (no per-capita dividend — a save-and-budget fund).

**Registry:** 193 → 228 rows; 3 corrections including a wrong URL on Foldvary 1997 (both circulating
SJSU links resolve to unrelated documents; corrected to JSTOR 3487330 + free mirror, and the two
citing pages fixed). Drive snapshot "Georgism Wiki — Source Registry (git sync 2026-07-04)" pushed;
a post-snapshot delta (~13 wave-D rows) is a loud [SHEET-SYNC] todo.

**Process notes for future loops:** (1) Two draft agents initially stopped claiming to "wait for a
background agent" — a SendMessage nudge ("YOU are the drafting agent") fixed both; one backfill
agent looped without editing and needed a fresh relaunch with "do not delegate or wait" up front —
now baked into backfill prompts. (2) Frontmatter references to not-yet-existing outcome slugs fail
lint, so the tech-rents drafts shipped with supports_outcomes:[] + prose notes, wired by T1 in the
same commit as the outcome page. (3) Concurrent agents must not share file ownership — disjoint
edit sets per agent worked with zero conflicts across ~45 agents.


## [COMPREHENSIVENESS] Invocation 1 — the source-corpus audit loop, built and run (2026-07-04)

New invokable loop (LOOP-COMPREHENSIVENESS.md) per Floyd's directive: re-mine the SOURCES (not the
wiki pages) so the wiki is cohesive with respect to everything its corpus substantively treats,
with a dedicated people channel for repeat contributors. Built after 13 concurrent Sonnet scanners
exhausted the session quota with all reports lost — the replacement architecture runs on GLM via
local ollama at ZERO Claude quota: local fetch (HTML/pdftotext) + GLM extraction, resumable JSONL.
Claude concurrency now capped at 3-4 everywhere (LOOP.md guardrail).

Numbers: 136 sources swept (64 full texts) + 46 deep re-reads at the verified 1M-token
window (needle tests: 273k and 635k chars pass; num_ctx raised from 262144 after T1 caught the
truncation risk). ~200 raw candidates -> T1 triage -> 29 stubs (11 researcher people pages closing
the authors-channel gap, 5 places, 7 concepts, 2 events, 1 org, 1 objection + earlier batch),
4 backfilled to full pages same-day via corpus-aware single-call GLM drafting (grounding check:
every number verified against supplied corpus; 3 flagged were correct constitutional facts).

Whole-corpus cohesion audit (257 pages, one 592k-char call, 36s): 25 findings — the high-severity
one (BC page's stale SVT rates contradicting the fresh Vancouver page) plus a Hoyt date error,
a Harrison forecast-lead-time conflation, an Estonia date vagueness, and 6 missing cross-links all
FIXED same-day; scope-split, terminology, and gap items queued as [COHESION]/[DRAFT] tasks.

T1-gate catches on GLM output this invocation (external-model rule working): a factual inversion
(NZ stub claiming Gemmell supports construction effects — it's our recorded null result), a
systematic /wiki/<category>/ link-format bug in 23 drafts, an 'entire secular rise' overstatement,
an uncertain Book-V attribution, 12 over-length excerpts, and an objection missing its enforced
template sections. Cost profile: entire invocation used ~6 GLM calls' worth of Claude context for
review; all scanning/drafting tokens were external.


## Waves 6-8 — the main loop on the GLM executor (2026-07-04/05)

LOOP.md now runs T2 volume on glm-5.2:cloud (scripts/glm_draft_worker.py: local source fetch,
full corpus digest in the 1M window, template+exemplar, parallel workers, zero Claude quota);
Claude subagents (capped 3-4) only for open-web forage; Fable is the T1 gate.

- Wave 1 (12 drafts): Great Mortgaging (full text; honest supports:[]), Zingales, Akcigit-Ates,
  CEA 2016 (corporate-rents outcome -> 8 supporters); conservative no-figure drafts for paywalled
  Hilber-Vermeulen + Davis-Heathcote; concepts site-value, law-of-rent, boom-bust-cycle,
  tiebout-model, rentier, land-speculation.
- Wave 2 (12): Phase-1 concepts queue COMPLETE (22->40 incl. betterment-levy, ebcor, land-bubble,
  marginal-productivity, land-as-commons); 5 stubs backfilled (arnott, rognlie, spencer,
  superstar-firms, fire-sector); Korinek-Ng + Rochet-Tirole as context pages — T1 stripped
  Korinek's supports_outcomes (fetch failed; no-source pages don't count as outcome evidence).
- Claude forage pair: england-zhao-lvt-distribution and loffler-siegloch-german-pass-through —
  the two honest COUNTER-EVIDENCE pages, wired as challenged_by on the progressivity and
  incidence outcomes. Both outcomes now show jurisdiction-dependence/counter-readings in
  frontmatter, not just support.
- Wave 3: 10 more stub backfills (churchill, clark, tiebout, rothbard, mass-appraisal, 2008,
  production-boundary, NZ, chicago, norway).

T1-gate pattern holding: every GLM draft passes automated structural + grounding checks; fetch-
failed research drafts ship conservative (years/DOIs only) at Light scan or lose their
supports_outcomes claim. people/floyd-marinescu created at the subject's request (NPOV, [VERIFY]
for backfill).

Update this log at the end of each loop (or wave) so the descriptive record stays in step with
`git log`.

---

## 2026-07-05 — WS2 completion wave (narratives 5/12 → 12/12) + Floyd's scan-queue & export-policy changes

**Environment:** fresh remote container on branch `claude/georgism-wiki-campaign-xz5anj` (successor
to the merged w5/PR-#3 line). No local ollama/GLM here — all drafting was T1-direct (Fable), with
3 concurrent Claude forage subagents for web verification. Egress proxy 403'd nearly every direct
fetch; all three foragers fell back to multi-source WebSearch corroboration (4-6 independent
snippets per claim, exact-phrase matches for quotes). Session WebSearch quota ran out mid-wave.

**Shipped (3 commits):**
1. Four well-evidenced narratives, T1-written per the unearned-increment exemplar:
   single-tax-narrative, community-creates-land-value, the-housing-crisis-is-a-land-crisis,
   citizens-dividend-narrative. Inbound links wired from concept twins + outcome pages.
2. The three source-gap narratives + their prerequisite research pages:
   ecological-rent ← barnes-sky-trust + song-zenou-property-tax-sprawl;
   the-corruption-of-economics ← blaug-henry-george-rebel (the anti-Gaffney counter-source);
   the-great-land-robbery ← fairlie-short-history-enclosure (with Clark & Clark 2001 revisionist
   counter-evidence on the same page). **WS2 COMPLETE: 12/12.** Registry +29 rows (~231→260).
3. Wrap-up: BACKLOG resume block, ROADMAP WS2 ✅, sheet snapshot, this entry.

**Honesty calls this wave:**
- All fetch-blocked sources shipped at Scan Depth **Light** with explicit verification notes;
  [VERIFY] flags left where a primary read is still needed (Barnes free-copy, Blaug names-Gaffney
  question, Milgate page numbers, Paine URL).
- Forager corrected the brief's numbers before they entered the wiki: Fairlie says ONE SIXTH of
  England (not one-fifth — that figure is UK Parliament's, different period/definition); the 2019
  carbon-dividend statement is 3,500+/27 Nobels (not 3,600/28); both distinctions are cited to
  their actual sources.
- Song & Zenou is property-tax (not LVT) anti-sprawl evidence — its page and the ecological
  narrative both state the mechanism difference explicitly; never cite interchangeably with
  Banzhaf & Lavery.
- the-great-land-robbery opens by acknowledging Newkirk's 2019 Atlantic use of the title and
  draws the rent-capture-is-not-land-back line explicitly.
- supports_outcomes kept honest: Barnes/Fairlie/Blaug/Song-Zenou all ship with
  supports_outcomes:[] (proposal, history, historiography, adjacent-mechanism evidence).

**Floyd's mid-session directives (both queued in BACKLOG):**
- Site-scan queue: citdiv.org + all of progress.org except /wiki/; gameofrent.com and the
  Progress & Poverty Substack explicitly deferred to future loops.
- Wanted-books channel created: `sources/wanted-books.md` (~20 titles, tiered, each with its wiki
  target) — unblocks as e-copies arrive.
- NEW STANDING RULE: dated registry exports now COMMIT to `sources/exports/` (GitHub-viewable,
  definitive) in addition to the Drive snapshot. First one: registry-export-2026-07-05.csv.

**Registry:** ~231→260 rows. Drive snapshot "Georgism Wiki — Source Registry (git sync 2026-07-05)"
pushed (259 data rows, 29 NEW in Δ column; also covers the previously-pending wave-D delta).

**Next wave:** Floyd's site scans (needs web quota), stub backfills (john-bates-clark and
fire-sector now have live narrative dependencies), WS8 [CITE] retrofit, comprehensiveness sweep
completion.

---

## 2026-07-05b — Loop 2: site surveys + 3 stub backfills (Floyd: "continue looping")

**Shipped (4 commits):** people/john-bates-clark (full backfill, both historiographies),
concepts/superstar-firms (corpus re-mine, no web needed), concepts/fire-sector (forage-fed:
honest acronym origin, verified scale numbers, Hudson thesis + Cochrane counter-view),
people/karl-widerquist (new sourced stub). Stubs 17→15 net. citdiv.org + progress.org surveys
triaged into BACKLOG.

**Survey verdicts:**
- citdiv.org: Anderson advocacy microsite/lead-funnel; level-6 source only; NO org page; eBook
  email-gated — blocked follow-up filed (needs Floyd download or proxy allowlist). Anderson
  person-page rejection STANDS (new evidence all self-published).
- progress.org: independent publication (editors Floyd Marinescu + Martin Adams; NOT PPI — that's
  the renamed Schalkenbach Foundation). ~700–1,500 articles, 59 contributors. Batch 0 = one Ghost
  Content API call (same credential that gates publishing) or proxy allowlist. Batches 1-5 by
  author: Foldvary(307)→core Georgists→editors/institutional→Progress-LLM(139, AI-authored,
  NON-CITABLE, inventory only)→tags/static.
- progress.org TOP-16 extraction candidates (URLs under progress.org/articles/):
  the-case-against-the-case-against-the-single-tax · mason-gaffney-predicted-the-china-crash ·
  the-corruption-of-economics (Adams) · how-land-barons-industrialists-and-bankers-corrupted-economics ·
  kinetic-rent-and-potential-rent (Foldvary) · exporting-the-alaska-model (Widerquist) ·
  bounty-true-total-trillions-yanks-spend-on-land (JJ Smith) · take-the-donald-seriously (Anderson) ·
  five-stages-of-the-georgist-movement (DiMare) · real-estate-4-ransom (Adams) ·
  henry-george-and-the-single-tax-documentary-and-interview · the-4-major-land-gain-income-taxes… ·
  guardian-columnist-george-monbiot-land-acts · michigans-government-failure (Foldvary) ·
  land-worth-more-than-enough · geo-libertarianism-gets-criticized (Foldvary).

**Honesty calls:** FIRE page prints only forage-verified numbers (Greenwood-Scharfstein 2.8→8.3%;
JST 30→60%; Krippner 5x) — the unverified 1950 FIRE share and Hudson's "80% of bank loans" claim
were EXCLUDED; FRED current value marked [VERIFY]. Hudson quotes paraphrased, not quoted (no
in-situ read). citdiv's stale 2006-era Alaska figure documented as why it's never an empirical
source. Widerquist progress.org article marked [VERIFY] (survey-surfaced, unfetched).

**Registry:** 260→267 rows (citdiv + 7 FIRE). Repo export refreshed; Drive snapshot 8 rows behind
— loud [SHEET-SYNC] filed per rule.

---

## 2026-07-06a (overnight, ~08:00-09:30 UTC) — COVERAGE 15/15 + stub burn-down

Scheduling bug owned & fixed: first overnight wake-up was set for the wrong DAY (Jul 6 not Jul 5);
Floyd's ping caught it ~2h late; trigger rebuilt, re-arming chain now at 11:15Z/16:15Z/21:15Z.

**Shipped (4 commits):**
- lvt-reduces-sprawl 1/5 -> 5/5 = **COVERAGE 15/15**: Tomson + Brueckner-1986 wired; NEW pages
  cho-two-rate-density (simulation, +18%/+83%, Nashville cluster counted as ONE evidence line),
  taranu-verbeeck-property-tax-sprawl (literature review, design-conditional),
  bentick-mills-timing-neutrality (COUNTER-evidence: market-value assessment can hasten fringe
  conversion; Tideman-1982 assessment-basis rebuttal carried). Song-Zenou deliberately kept
  adjacent-UNWIRED (opposite mechanism). Yang 2018 JHE queued with UNVERIFIED-FINDING guard.
- Stubs 6 -> 4: margin-of-production (Ricardo/George two-laws structure + the Clark-preface
  connection verified earlier this session) and public-land-leasing (HK 13-24% revenue range,
  Singapore ~90%/Past-Reserves, Canberra 1924, and the honest core: Hong-Lam's 39%-of-increment
  capture + post-1997 no-premium extensions — leasing's structural gap vs annual LVT).
- LVIT forage facts (Art. 143 confirmed; rates 20/30/40+10; ares-not-acres flag; 2005 history
  UNVERIFIED) filed in BACKLOG for the marker lane rather than editing a 10-marker page in
  Hermes's territory overnight.
- Registry 289 -> 297; exports refreshed. Hermes active on hermes/enrichment-w1 (not reviewed —
  Floyd reviews trigger in the morning).

**Remaining stubs (4):** search-theoretic-critique, progress-and-poverty-institute (both next
wake-up), floyd-marinescu (owner-input), karl-widerquist (needs independent bio sources).

---

## 2026-07-06b (overnight wake #2, 11:15-12:30 UTC) — stub queue cleared + TOP-16 batch 1

**Shipped (4 commits):** search-theoretic-critique objection backfilled from the full primary read
(steelman + 4 response lines + honest Net Assessment); progress-and-poverty-institute backfilled
(2025 Schalkenbach centennial renaming verified, ED Josie Faass, PPI≠progress.org disambiguation);
TOP-16 batch-1 triage executed — 2 INGESTs (johnson-1914-single-tax-critique pairing the 1914
Atlantic attack with Foldvary's 2017 rebuttal; foldvary-kinetic-potential-rent anchored to the
2012 paper with venue honestly flagged), 3 REGISTRY+CITE (Gaffney AJES-2015 China prediction on
the cycle page; Counting Bounty as attributed advocate-estimate row on fund-government; Exporting
the Alaska Model book row), 1 SKIP with reason (DiMare five-stages — unrecoverable enumeration).
**Backfillable stub queue now EMPTY** (2 remain, both input-gated). Registry 298→306.
Lane discipline: widerquist-howard-pfd cite deferred (2 markers = Hermes lane).
Wake #3 armed 16:15Z; stops re-arming when Floyd returns.

---

## 2026-07-06c (wake #3 wave, started early on Floyd's "keep looping", ~15:35-16:20 UTC)

**TOP-16 COMPLETE (16/16):** batch 2 triaged 10/10 — 1 ingest (real-estate-4-ransom film page:
advocacy-media treatment, deployment-not-evidence framing, director-spelling variant flagged),
7 registry+cite (incl. Monbiot primary locked: Guardian 21-Jan-2013; Baker's Fed-Z.1 $11T as
attributed advocate row beside Larson benchmark; Anderson's Trump/cycle piece as attributed
period application), 2 skips with reasons. Prose-polish: 3 of 11 outcome evidence sections woven
to narrative (capital-share gains a full counter-evidence section). Lane discipline held twice
(churchill-peoples-rights 14 markers; corruption book-page cites deferred to Hermes merge).
Monbiot logged as DISCOVERED people-candidate. Registry 306→318.

---

## 2026-07-06d (wake #3 continuation, ~16:15-17:30 UTC) — Doucet de-reference cycle 1 complete

Prose-polish DONE (all 11/11 outcome evidence sections now narrative; England-Zhao vs Bowman-Bell
dispute surfaced as jurisdiction-dependent on the progressive page). Doucet Parts 1&3 citation
skeletons recovered: INGESTED gwartney-estimating-land-values + davis-larson-oliner-shui-fhfa-land
(the FHFA tract-level project — doubles as the strongest institutional counter-exhibit to the
assessment objection, and honestly flagged [VERIFY] on specific magnitudes pending direct read);
4 more sources registered (Davis-Palumbo, Lincoln dataset, McKinsey 2021, Yglesias 2013).
Key finding for future editors: 5 of Part 1's 12 land-value datapoints route through Smith's
Counting Bounty (incl. Tideman's $31T via private correspondence) — attribute through Smith.
Unblock routes for full texts documented (danwahl transcripts, gameofrent mirrors).
Registry 318→324. All three Doucet parts now have de-reference passes; cycle 1 of the standing
rule closed pending complete source confirmations.

---

## 2026-07-05 — Hermes overnight w1: verification queue + book scans

**Branch:** hermes/enrichment-w1 (PR #6)
**Agent:** Hermes (glm-5.2:cloud), running overnight 2026-07-04/05
**Scope:** Task A (verification queue burn-down) + Task B (book scans and synthesis)

### Tally
- Markers resolved: 12 (Hsieh-Moretti x3, Glaeser-Gyourko x3, IMF Building Tax Capacity x1, Knoll-Schularick-Steger x6, Progress 18.6-year cycle x2, Anderson CITATION NEEDED x1)
- Markers corrected (primary contradicted wiki): 1 — Hsieh-Moretti Caplan correction: the corrected GDP impact is LARGER than originally published (~14% not 3.7%), confirmed against Caplan Econlib article
- Markers not found / left in place: 33 (mostly paywalled journal articles still inaccessible)
- Books scanned: 4 (Harrison Boom Bust, Harrison Power in the Land, Anderson Secret Life of Real Estate, Patel Secret Wealth Advantage)
- New research pages created: 4
- Existing pages enriched with book findings: 5
- Existing pages cleared of VERIFY markers: 5
- Registry rows added: 5
- Registry export committed: sources/exports/registry-export-2026-07-05-hermes.csv
- Total commits: 11
- Lint: 0 errors, 485 warnings (down from 490)

### CORRECTED items (primary contradicted wiki)
1. Hsieh-Moretti — Verified against Caplan Econlib article (April 5, 2021): the corrected figures are +36% for Table 4 (not +8.9%) and +14% for Table 5 (not +3.7%). The corrected GDP impact is LARGER, not smaller.

### Papers downloaded and verified against primary text
- Hsieh and Moretti (2019) — author-copy PDF from UC Berkeley / Chicago Booth
- Glaeser and Gyourko (2017) — Wharton working paper 802
- IMF Building Tax Capacity (2025) — full PDF from IMF
- Caplan (2021) — full article from Econlib

### What was NOT done
- Ricardo Law research page not yet created (subagent was still running at wrap-up time)
- Many VERIFY markers on paywalled papers could not be cleared (ScienceDirect, Wiley, SAGE return HTTP 403)
- No new wiki category books-publications was created (lint script CATEGORIES cannot be edited per spec); book pages placed in research/ with books-publications tag
- verification_queue.py script mentioned in spec does not exist; markers tracked via grep

---

## 2026-07-06b — T1 REVIEW: Hermes PR #6 approved & merged + reconciliation

**Verdict: APPROVED.** Review-first items checked: the CORRECTED Hsieh-Moretti/Caplan figures
re-derived independently (1.0149^45/1.00795^45 ≈ +36%; Table-5 variant ≈ +14% — arithmetic
correct); marker clearances spot-checked against the diffs (Glaeser-Gyourko via Wharton WP #802,
KSS abstract 80% figure, IMF DP 2025/007 Heavy, 18.6-cycle); Hermes also FIXED a committed
conflict-marker block on main (hsieh-moretti). Books: 10 pages + 10 discovery reports (locator-
cited, all categories — the universal-discovery rule ran retroactively). No book files committed;
no protected files touched.

**Merged to main** (merge commit 30358c1), then main merged into the campaign branch with
conflicts resolved (BACKLOG/LOOPLOG union; registry union + Patel dedupe).

**Reconciliation fixes applied on this branch:** books frontmatter normalized (5 pages);
slug-collision renames (posner-weyl-radical-markets, gaffney-harrison-corruption-of-economics);
30 [[books/…]] wikilinks repaired; 2 committed conflict-marker blocks on main fixed (arnott,
bowman-bell); anderson NPOV trim; DØRS cross-links added to the two Danish-experiment sections;
Harrison Victoria data C-claim relabel; 4 over-cap Blaug quotes trimmed to ≤50 words.

**FLAG for Floyd:** two book scans (Blaug; Ryan-Collins et al.) named .vg as procurement
source — provenance-pending [VERIFY] flags placed, provenance checks now enforced in
sources/inbox/README.md, owner attestation task filed in BACKLOG.

State post-merge: 319 pages, lint 0 errors / ~509 warnings, registry ~330 rows.

---

## 2026-07-06c — FIRST-PRINCIPLES REVIEW of the looping system (Floyd's ask)

**Is it achieving what we want? Largely yes** — 319 pages, 15/15 outcome coverage, 12/12
narratives, honest correction record (Caplan figures, Fairlie one-sixth, Foldvary Michigan),
and the multi-agent structure held under fire (Hermes PR review caught  provenance,
NPOV drift, broken links BEFORE main). **Three real gaps found in the data:**
(1) debt grows, never shrinks (520 warnings, 613 markers) because most of it is structurally
unpayable from this container → answer is ROUTING (debt ratchet + Hermes channel), not
diligence; (2) discovery outruns triage (one book scan = 40+ candidates) → accept bar +
stub quota; (3) category imbalance: 9 objections vs 15 outcomes/13 narratives — the
steelman pillar is the thinnest, which is a credibility risk for an advocacy-adjacent wiki.
**Simplifications shipped:** every process failure that bit us this week became a lint check
(conflict markers, [[wikilinks]], quote cap, registry dupes, provenance ban) — rules that
live in code don't need to live in anyone's memory. GLM section marked environment-
conditional (it was dead text in this container). Drive sync already de-scoped.
**New:** docs/loop-diagram.md — Mermaid visual of iteration/flywheel/lanes/honesty machinery,
with a same-commit sync rule.

---

## 2026-07-06d — Loop reframed in mission language + gap-1/gap-2 machinery (Floyd's ask)

LOOP.md rewritten mission-first: opens with WHAT we're building (the definitive, honest
Georgism reference) and the domain verbs — FIND the literature, READ & MINE each source,
SYNTHESIZE into the case pages, VERIFY (Fact-Check Desk), EXPAND the map. Steps renamed as
an editorial shift; tiers as roles (editor / staff writers / copy desk); technical executor
notes moved to an appendix. Diagram re-synced in the same language.

GAP 1 shipped as machinery: verification_queue.py now ALSO generates
sources/hermes-workorder.md — the routed field assignment (60-item cap) of blocked-web +
book-copy fact-checks only Hermes's environment can work. Plus the campsite rule: every
shift clears or routes ≥5 standing debts regardless of its main work.

GAP 2 shipped as machinery: digest-before-you-scan — no new site/book scans while ≥2
discovery reports sit untriaged; ≤8 stubs/shift; accept bar ≥2 demanding pages; and a
name-variant grep before creating people pages (lesson: today's richard-ely duplicate of
richard-t-ely — merged, my wave-1 corroboration resolved 4 of the old page's open
fact-checks, duplicate deleted, links repointed).

---

## 2026-07-06e — Mission framing propagated into every executor prompt (Floyd's ask)

The reframe now reaches the prompts the models actually consume, not just LOOP.md:
EDITORIAL.md gains §0 The Mission (canonical statement); llm_worker.py + glm_draft_worker.py
system prompts open as "staff writer on the research desk building the definitive, honest
reference…"; comprehensiveness_sweep_glm.py opens with the source-isn't-done-until-mined rule;
tasks/research-page-task.md re-titled as the READ & MINE step; tasks/backfill-page-task.md as
the EXPAND/BUILD OUT step; sources/inbox/README.md (Hermes's contract) opens with the mission
+ its standing assignment (the auto-generated work order); BACKLOG header states what the
queue is FOR; ROADMAP points at §0 as the canonical short form. One mission, quoted
everywhere — no executor works from process jargon alone.

---

## 2026-07-06f — Three editorial policies from Floyd: delta rule, evidence ordering, PD full texts

(1) DELTA RULE — honest answer to "are enrichments checked for duplication?": partially, and
now explicitly: read the target page first, add only what's new, one finding one home, link
don't restate (LOOP mission + editor-review check; the Danish experiment's three restatements
in w1 are the named lesson; duplication-sweep audit queued).
(2) EVIDENCE ORDERING — supporting-research lists now read strongest-first by evidential
weight (EDITORIAL §3): quasi-experimental/top-journal > peer-reviewed > institutional >
working papers > advocacy. Demonstrated on the landlords outcome (Danish natural experiment
now leads; Doucet's synthesis demoted to last). Reorder pass over all 15 outcomes queued.
(3) PUBLIC-DOMAIN FULL TEXTS (EDITORIAL §3b) — pre-1931 works may be held IN FULL: new
texts/ category wired into lint/preview/ghost (public_domain: true exempts the quote cap),
sources/publicdomain/ for whole books, Hermes PD delivery channel opened with a priority
list (George's works, Saratoga 1890 proceedings, Agrarian Justice, Johnson 1914, Post 1923).
Diagram re-synced same commit.

---

## 2026-07-06g — END OF CAMPAIGN DAY: branch merged to main (Floyd's direction)

Day's totals on this branch (44 commits): Hermes PR #6 T1-reviewed, merged, reconciled
(3 duplicate slugs caught+merged,  provenance flagged+policy'd); loop redesigned
first-principles in mission language (Fact-Check Desk + work order, debt ratchet, accept bar,
digest-before-you-scan, delta rule, evidence ordering, PD full texts, 6 new lint gates,
loop diagram with sync rule); coverage: 307→336 pages, 14 new stubs (all demand-justified),
2 objections (homevoter new — rated the wiki's strongest; revenue deepened with Krugman/Blaug
locators), 6 thin pages rebuilt, ~30 Sources annotated, all 15 outcomes reordered
strongest-first; warnings 493→478 with growth absorbed. Directives for the next session in
the BACKLOG checkpoint above.

---

## 2026-07-06h — SCOPE EXPANSION: Georgism → Geoism (Floyd's directive)

The wiki's mission now covers ALL economic rents and their capture instruments, not land
alone: EDITORIAL §0 rewritten (with the new RENT GRADIENT honesty rule — land is the clean
case, the frontier is contested, quasi-rent/incentive caveats mandatory); LOOP.md mission,
ROADMAP vision, and the diagram synced; concepts/geoism created as the umbrella page with
the domain/instrument table. WS-GEOISM workstream opened in BACKLOG: five [FIND] discovery
sweeps (resources/severance, spectrum/auctions, congestion pricing — likely the strongest
non-land evidence, platform/data/IP, financial rents) + the Schumpeterian quasi-rents
objection as the expansion's mandatory steelman + instrument-concept queue. The existing
tech-rents/FIRE cluster (Mazzucato, superstar-firms, corporate-profits outcome) is the
expansion's seed corpus, already carried with counter-positions.

---

## 2026-07-06i — WS-TECH-RENTS opened (Floyd): the monopolistic-tech-firms question

Dedicated workstream on the expansion's hardest case: diagnosis track (how much of big-tech
profit is rent — expect CONTESTED), instrument track (ACE/cash-flow rent-only corporate taxes
as the mainstream core with Belgium/Italy quasi-experiments — best new-outcome candidate;
DSTs honestly graded as turnover taxes that shifted, per the Amazon UK pass-through; Romer's
ad tax; data dividends; antitrust as rent-dissolution vs capture), synthesis track gated on
the finds. Every page links the Schumpeterian steelman. Session handoff prompt delivered to
Floyd; morning successor trigger deleted in favor of the immediately-started session.

---

## 2026-07-06j — WS-TECH-RENTS shift 1 (session vy8k5i): rent-targeting corporate taxes [FIND] complete

Three forage agents (ACE · cash-flow/DBCFT · framing+critiques), ~100 sources; proxy 403'd
all direct fetches so everything ships snippet-corroborated at Light scan with [VERIFY]
flags routed to the Hermes work order. Durable triage record:
reports/ws-tech-rents-rent-targeting-taxes.find.md.

Shipped (5 pages + 1 enrichment): concepts/quasi-rent (the rent gradient's load-bearing
distinction — Marshall/Blaug/Gochenour-Caplan corpus material was already on the wiki);
concepts/allowance-for-corporate-equity; concepts/cash-flow-tax (Meade/Brown/DBCFT/Norway
2022/PRRT failure mode); research/hebous-ruf-ace; research/branzoli-caiumi-italy-ace;
mirrlees-review gained its ACE section (the Review endorses rent-only bases for BOTH land
and corporate — the single best bridge between the land core and the corporate frontier).
24 registry rows + dated export.

EDITORIAL FINDINGS THAT CORRECT THE TASK PREMISE: (1) quasi-experiments show ACE reliably
cuts LEVERAGE; real-investment evidence is MIXED (Hebous-Ruf JPubE null on MNE production
investment + double-dip arbitrage vs Konings et al. CJE positive) — the planned outcome
page must be reframed toward debt-bias + marginal-investment neutrality with the
MNE caveat, not "avoids investment distortion" flat; (2) every full European ACE has been
repealed — political fragility is a finding; (3) no published ACE↔Georgism framing exists —
the analogy ships only as labeled analysis; (4) rent-sharing in wage bargaining
(Fuest-Peichl-Siegloch AER 2018) partially shifts even rent-only taxes — must appear on
any incidence claim; (5) the "Stiglitz 2015 Tax Law Review" citation is garbled — real
trio is NTJ 68(2) 2015 / NBER 21189-92 / EJ 125(583).

Campsite: 13 debt items (12 Sources annotations, Mazzucato venue corrected to CJE on the
corporate-profits outcome). Warnings 478→472 net of 5 new pages' honest flags; 342 pages;
lint green; preview links verified.

---

## 2026-07-06k — WS-TECH-RENTS shift 2 (session vy8k5i): the Schumpeterian steelman shipped

objections/taxing-quasi-rents-kills-innovation — the gate page Floyd's directive named as
blocking the whole workstream — is live: Schumpeter's "spectacular prizes" (locator
[VERIFY]-flagged), Akcigit-Grigsby-Nicholas-Stantcheva QJE 2022 with its scope caveat
carried INSIDE the steelman, Domar-Musgrave 1944 loss-offset asymmetry as the analytic
hinge, Reynolds-Neubig OECD 2016 on the normal-return benchmark. Responses concede the
frontier and hold the core: no purchase on land/commons charges; design answer (rent-only
bases + full loss refundability, Norway 2022 as existence proof, no economy-wide system has
it); persistence diagnostic (Schumpeterian prizes are temporary — decades-long moats look
like entrenched rent, with the superstar counter-reading carried); the objection's own
overreach against the status quo (Treasury: ~63-75% of the corporate base is already
supernormal and taxed haphazardly). Net assessment: substantially valid at the frontier —
and the standing rule is now in force: any non-land efficiency claim links this page.
Wired from geoism, quasi-rent, ACE, cash-flow-tax. Objections pillar 11→12.

Campsite: 5 places Sources annotated (harrisburg, denmark, singapore, hong-kong, estonia)
+ 1 banned-certainty fix. Warnings 472→469; 343 pages; lint green; preview links verified.

---

## 2026-07-06l — Shift 3 (session vy8k5i): Ghost IDs merged (PR #10) + WS-TECH-RENTS evidence base built out

INTERLUDE, Floyd present: openclaw/add-books-sync T1-reviewed and merged as PR #10 at
Floyd's direction (wiki-books 6a4affad… + wiki-texts 6a4b01d7… into TAG_IDS; texts/.keep) —
the Ghost-IDs blocker is RESOLVED; books/ and texts/ can sync. Theme-repo PR
(progress-org-theme → openclaw/add-wiki-books-category) is outside this session's repo
scope — deploy decision left with Floyd. Campaign branch merged up from main. Blocked-on-
Floyd list refreshed (Exa key never persisted to env; citdiv.org proxy-blocked — Drive
drop suggested; allowlist wishlist expanded; 6 bio questions delivered).

SHIFT 3 MAIN WORK — five research pages from the find report, the reframed synthesis
outcome's future supported_by base: power-frerick-excess-returns (40%→25% normal-return
share; NOW WIRED into corporate-profits-increasingly-rents supported_by with body parity),
fuest-peichl-siegloch-incidence (rent-sharing channel; the landlord-pass-through contrast
drawn explicitly), domar-musgrave-risk (the loss-offset hinge), akcigit-taxation-innovation
(the objection's empirical core, inference gap carried inside), zwick-mahon-expensing
(expensing→investment, the instrument-family distinction vs ACE's mixed record). All Light
scan, snippet-corroborated, [VERIFY]-flagged. Registry rows re-pointed to the research
pages; dated export.

Campsite: 5 more Sources annotated (pennsylvania, new-south-wales, pittsburgh,
detroit-lvt-proposal, 1886-nyc). 348 pages; warnings 469→470 net of 5 new pages' honest
flags (baseline 478 still beaten); lint green; preview links verified.

---

## 2026-07-06m — Shift 4 (session vy8k5i): Exa key + citdiv eBook delivered; eBook consumed

Floyd delivered: (1) the Exa API key in-chat — tested inline; api.exa.ai STILL 403'd by the
egress proxy, so the sweep stays blocked on the network-policy entry (key value lives in the
conversation + BACKLOG points at the environment-settings fix; never committed; profile
persistence policy-blocked); (2) the citdiv eBook PDF uploaded directly — the site-scan
blocker cleared.

EBOOK CONSUMED (READ & MINE, full 16 pp): books/anderson-your-citizens-dividend shipped —
advocacy-graded program statement of the Crown-Estate/SPV capture design (George III 1760,
Temasek as politically insulated collector, ATCOR-family "all gains end up in land value"
claim marked contested, UBI-capitalization argument). Accuracy notes carried on-page: PFD
given as US$1,022 (2016-vintage) in a ©2024 edition; Swiss "no paid politicians" self-
corrected in the eBook's own footnote; housing-shortage aside contradicts the wiki's supply
literature. Deltas per the delta rule: phillip-j-anderson cover-title correction +
sharpened staleness note; Churchill toll-bridge story (capitalization in miniature) added
to churchill-peoples-rights with primary-locator [VERIFY]; citizens-dividend concept wired.
DISCOVERY: Great Smoky Mountains casino-dividend study queued as [FIND] (verify primary
before citing — do not write from memory). Registry: eBook row at Heavy scan.

349 pages; warnings 470→473 (3 honest flags on the new book page; baseline 478 still
beaten); lint green; preview links verified. GitHub MCP disconnected mid-session (needs
re-auth via claude.ai connector settings) — git push unaffected; PR #9 description refresh
deferred until re-auth.

---

## 2026-07-06n — Shift 5 (session vy8k5i): the SYNTHESIS outcome ships — 16th outcome, first non-land one

outcomes/rent-targeting-taxes-reduce-debt-bias — the wiki's 16th outcome and its first
outside the land core, written to the reframed scope the find report demanded (debt bias +
marginal-investment neutrality, NOT "avoids investment distortion"). Evidence walked
strongest-first with body parity: Zwick-Mahon (expensing→investment, AER) >
Branzoli-Caiumi (incremental-ACE leverage) > Power-Frerick (base composition) >
Domar-Musgrave (conditional risk-neutrality — support AND boundary); challenged_by
Hebous-Ruf (double-dip, null MNE real investment; Konings counter carried). Both mandatory
caveats wired in their own section: FPS rent-sharing incidence + the Schumpeterian gate.
Rent-gradient closing: the design motion generalizes; the land case stays cleaner on every
margin; no published Georgist framing exists — analogy labeled as analysis. Bidirectional
supports_outcomes added on 4 research pages; inbound links from ACE, cash-flow-tax, and the
objection. Hermes check: no PRs, no new inbox.

Campsite: 5 more Sources annotated (alaska-permanent-fund, 1909-peoples-budget,
single-tax-colonies, lvt-improves-housing-affordability, resource-rent-dividends-work).
350 pages; warnings 470 (baseline 478); lint green; preview links verified.

---

## 2026-07-06o — Shift 6 (session vy8k5i): inbox triage COMPLETE (10/10 consumed); egress still gated

Floyd set the environment to allow-all egress; this RUNNING container's upstream gateway
still answers 403 (policy is applied at container creation) — poller armed; if it never
opens, the successor session inherits open egress and should run a VERIFICATION SWEEP over
this session's [VERIFY] flags first thing. Exa remains blocked from here for the same
reason.

Main work — digest-before-you-scan cleared: the last 5 discovery reports triaged
(economic-theory-in-retrospect deep-read; boom-bust/ricardos-law/anderson/patel candidate
sweeps). 3 stubs accepted per the accept bar: von Thünen (people), Land Tenure Reform
Association (organizations — already name-checked on 4 pages), Town and Country Planning
Act 1947 (events). 2 wanted-books rows (Riley Taken for a Ride, Christophers Rentier
Capitalism); rejections reasoned in BACKLOG. All 10 inbox reports now consumed/ — the WIP
gate for new scans (congestion-pricing FIND next) is open.

353 pages; warnings 473 (3 new stubs' honest flags absorbed; baseline 478); lint green;
preview links verified.
- 2026-07-12 (Floyd's ruling, codified in EDITORIAL §0): the loop's standing priority is ENRICHMENT of benefits/, problems/, and objections/ pages — assemble the research, wire every new source into the claim lanes it bears on, honestly including support FOR objections. Waves 18-19 (warning cleanup) and 20-21 (objections wiring, benefits reinforcement) are the model: every future wave closes by asking which claim pages it enriched.

## 2026-07-14 — PUBLISH: waves 23–28 live on progress.org/wiki (134 pages, 0 errors)

Ghost sync executed on Floyd's explicit go-ahead: 11 created, 123 updated, 0 failures
(scratchpad/sync-log-2026-07-14.txt). New pages: the 10 wave-28 research entries
(berman-alaska, bezemer-samarina-zhang, he-sun, kerspien-madsen-strulik, kozminski-baek,
letwin, pretis-bc-carbon-tax, sachs-warner, sen-poverty-and-famines, stewart-canadian-land)
plus progress-and-poverty-full-text (not previously on Ghost despite the a84a6b8 recategorize).
Spot-checked live: bodies render (645–177,443 words), titles correct, wiki-entry template applied.

Publish had been blocked on credentials: root cause was the 1Password vault display name
("Emma / Floyd Agent") containing " / ", which op:// reference parsing treats as path
separators — op read could never resolve by name. scripts/_secrets.py and the SessionStart
hook now default to vault/item IDs; future sessions load the Ghost key automatically.

## 2026-07-14 — Verification retry wave: 4 backlog rows closed, 1 narrowed, 2 documented dead ends

Worked sources/verification-backlog.md RETRYABLE table (paid/library access approved but
none needed — all closures via free legitimate channels):
- world-bank-changing-wealth CLOSED: CWON 2021 chapters 5+9 read via the openknowledge
  DSpace REST API (the SPA hides per-chapter PDFs); Box 9.1 rent-vs-revenue read directly.
- vickrey + myerson-satterthwaite CLOSED: Princeton UP's official free Radical Markets
  Ch. 1 sample PDF pins both cites (pp. 49-50 en.29; pp. 50-51 en.32, p. 66 en.56).
- phelps-brown-weber CLOSED: the June 1953 Economic Journal issue is freely digitized on
  archive.org (sim_economic-journal_1953-06_63_250) — figures confirmed (10-11% -> ~7%,
  pp. 266-271) AND an editorial finding: the paper never discusses land returns; Harrison's
  "scissors" is his own synthesis, now said explicitly on the page.
- pistor-code-of-capital: page cites resolved via Pistor's own 2021 S&LS rejoinder + Gordon's
  Jotwell review (verbatim quotes w/ pages); honest note that the book itself is still unread.
- widerquist-howard-pfd NARROWED: contributor PDF gave front matter, full ToC page numbers,
  and Ch. 12 complete; Goldsmith Ch. 4 (the key empirics) still unverified — row updated.
- lewis-building-cycles NO ACCESS: archive.org copy is lending-restricted (search-inside 403);
  Google Books confirms "17.4" occurs once but shows no snippet. Dead end documented.
- modelewska NO ACCESS: UCL Discovery + EThOS now behind Cloudflare bot-challenges.
Remaining retryable rows: tideman-plassmann, widerquist-howard (Ch. 4), modelewska,
lewis, miller — all genuinely blocked on book copies / bot-walled repositories.

## 2026-07-15 — Phase 2 interlinking: Option 2 DEPLOYED site-wide, Option 3 manifest ready

Option 2 (in-text entity links), Floyd-approved manifest applied: 966 links across ~395
/articles/ posts — lexical surgery on post-2021 posts (200/71) + NEW mobiledoc surgery on
pre-2021 posts (762/323 + 4/1 sacrificial test), unblocking the ~330 articles previously
ruled un-editable. Every edit verified (plain text byte-identical, links present), 0 drift,
0 errors; snapshots in scratchpad/cache/apply-backups/; permanent record in
sources/interlink-ledger.jsonl. Manifest pruning: Haiku fan-out (12 agents) + deterministic
footnote/quote filter added after Floyd's Sun Yat-sen spot-check (69 citation-placement drops).
Option 3 (conceptual proof-point links): GLM-4.7 on Ollama Cloud mapped 607/608 articles to
problems/benefits/objections/narratives — 2,236 candidate mappings (97.7% grounded), review
manifest at scratchpad/concept-link-manifest*.md, NOT applied pending Floyd.
Option 1 confirmed already live in the theme (all 7 topic boxes verified rendering).
Standing maintenance: scripts/interlink_wave.py + docs/interlinking-maintenance.md —
bulk review-gated waves for new articles; no publish-time auto-injection.

## 2026-07-15 (later) — Option A SHIPPED: precompiled per-article wiki boxes, site-wide

Floyd picked delivery (A): box HTML lives in each post's codeinjection_foot (metadata,
never body). GLM-5.2 on Ollama Cloud curated all 608 articles against the full 801-page
wiki catalog in context: 603 boxes (5 correctly off-topic). Theme PR #51 merged+deployed
(runtime {{#get}} chain -> #wikiRelatedSlot + relocation script); legacy PR #15 closed.
Incident caught & fixed same-day: nested markers in deliverable() stacked orphan script
tails (4x/post) across sweeps — repaired fleet-wide (603/603 clean, verified live), and
the relocation script now guards on an empty slot. Idempotency restored (absolute hrefs
match Ghost's stored form). Routines created: daily 11:00 UTC (new/changed) and weekly
Sun 12:00 UTC (full refresh + interlink wave prep). Option 2 fully deployed earlier today
(966 in-text links); Option 3 v2 strict manifest (779 mappings/309 articles, GLM-5.2)
awaits Floyd's review. Future: port Routines to Hermes webmaster agents.

## 2026-07-15 (evening) — Entity-link delta wave (Floyd's 18.6-year spot-check)

Root cause of missed names: the 2026-07-14 Haiku prune capped keeps at 6/article
(197 genuine links discarded fleet-wide). Delta wave: rescan against live link state
(794 remaining candidates), GLM-5.2 uncapped prune (drop only noise categories),
Floyd-approved delta manifest (452 links / 163 articles), applied in three passes with
two matcher upgrades (self-contained formatted runs; list items in both lexical and
mobiledoc — reference-list author names). Result: +344 links across ~110 posts, 0 drift,
0 errors. Remaining 108 unplaced = text already inside external links (correct skips)
+ cross-node splits (diminishing returns, logged). Entity links live: ~1,310 total.
The 18.6-year article: 25 wiki links incl. Patel, Ryan-Collins, Gaffney, Gordon Brown,
Toby Lloyd, Laurie Macfarlane. Standing rule: NO numeric caps in future prune prompts.
---
---

## 2026-07-14 — Slack deep-scan triage + first ingest wave (session udw74p, issue #24)

Wave 29 in the commit numbering. Input: 516 research candidates harvested from all SES Slack
channels (2019–2026), pre-deduped against registry URLs but not against titles — title-level
dedupe caught 13 mirrors of already-ingested sources (incl. the VoxEU/CEPR copies of
goodhart-stimulus, the IMF landing page for schwerhoff-imf-equity-efficiency, and the ILO/UVM
copies of Goldsmith's Alaska papers), plus 2 registry rows that were outright mislabeled and are
now fixed (wpiea2022187 = Hebous et al. WP/22/187, not Baunsgaard-Vernon; CD Howe E-Brief 341 =
Dachis "Buyers Beware", not a dev-charges title).

Division of labor per Floyd's directive: Haiku for bibliographic lookups, 3 Sonnet T2 writers
for the 10 entry drafts (each fetched its sources — 8/10 read in full, 2 partially via verified
secondary), Fable T1 for triage judgment, review, claim-lane wiring, and the gate. Commits:
4c3898d (registry +191) · 89e93d8 (triage map) · 0dcce23 (10 research pages + wiring).

Loop-priority check (EDITORIAL §0): the wave enriched all three claim lanes — benefits
(lvt-dampens-land-speculation, resource-rent-capture-works ×2, rent-targeting-taxes-reduce-debt-bias),
problems (housing-unaffordability-is-a-land-problem), objections (quasi-rents steelman +2 sources,
land-speculation-is-productive response +Brown 1927), and added honest counter-evidence
(BC panel as challenged_by on rent-dividends-reduce-poverty). Gap surfaced and queued: no
objections/ page for universal-vs-targeted transfer efficiency.

811 pages; lint 0 errors, 11 warnings (7 new honest [VERIFY]/wording flags, routed);
0 orphans; preview built. TIER-1 remainder (~64 rows) and TIER-2 wave queued in BACKLOG.

---

## 2026-07-15 — Wave 30: Slack TIER-1 remainder, first cut (session udw74p, issue #24)

12 research entries (3 Sonnet lanes, Fable T1 review/wiring) + the objections/ page the wave-29
UBI entries flagged as missing (universal-transfers-are-inefficient, T1-drafted: BC-panel
steelman, World Bank 10-country corroboration, Woo/Forget/Widerquist-Howard responses, honest
net assessment that the arithmetic stands) + Haiku dead-link mirror hunt (all 12 registry
dead links repaired with verified-200 mirrors; the Reform Scotland "SWAY" row turned out to be
a realist review of LVT/wealth taxes — retitled, queued).

Source-integrity catches this wave: E-Brief 341 ≠ dev-charges paper (= Dachis Buyers Beware,
already fixed w29); the supplied De Schutter URL was a different report (correct A/HRC/56/61
fetched from UN ODS); CIB study's real authors are Siemiatycki-Fagan-Arku (U of T), CIB only
funded; lead author is Blanca (not Beatriz) Fernandez Milan; wpiea2022187 = Hebous et al.
(fixed w29, entry now written). Two entries carry deliberately counter-narrative findings and
are wired on the challenge side: CMHC (quick-flip speculation NOT Montreal's main driver) and
BoC SAN 2023-12 (markup growth <1/10 of 2021 inflation).

Claim-lane deltas: rent-dividends-reduce-poverty +1 challenger (World Bank) · corporate-profits
+1 support (Hebous) +1 challenger (BoC) · resource-rent-dividends-work + Mongolia failure mode ·
public-investment-capitalizes + CIB practitioner survey · quasi-rents objection +1 steelman
source · fire-sector/financialization-of-land/land-value-tax/land-value-capture/denmark/
citizens-dividend enriched. Commits: 4a2072b · b68d667 · cde4c89. 824 pages; lint 0 errors;
0 orphans; registry 1,098 rows, 0 dead links.

---

## 2026-07-15b — Wave 31: TIER-1 lane closed out; UBI scope ruling applied (session udw74p, issue #24)

Floyd's scope ruling landed mid-loop (UBI only with rent/commons tie — codified EDITORIAL §0):
2 pure-UBI pages deleted on his instruction (namibia-big-pilot, de-schutter-poverty-beyond-growth;
wiring unwound, Osterkamp companion rows dropped), 11 registry rows demoted, pure-UBI candidates
struck from queues. Deploy attempted per Floyd's "commit/deploy" — blocked on the Ghost Admin key
(op://Emma item not resolving; Floyd-side fix, everything push-complete for a credentialed sync).

Wave 31 entries (2 Sonnet agents, T1 review): sway-lvt-wealth-taxes-review (Sam Wolstenholme-Britt
for Reform Scotland — MSc-placement report, graded supplementary; NWT avoidance losses 44%+ vs the
immobile land base, wired into lvt-not-enough-revenue Response) · london-group-land-balance-sheet
(ABS statisticians on the land/structure valuation problem — wired into the larson/davis-larson
land-measurement cluster) · walks-toronto-income-polarization (spatial-inequality context; honest
flag: no land-rent claim in the source) · carney-future-of-work (venue corrected to the Whitaker
Lecture, Dublin — the Slack context's "Toronto PPF" was wrong; Engels'-pause base rate for the AI
lane). First TIER-2 citation batch under the scope rule: SWF proposal landscape (Sanders/Bores/
CTF/IPPR×2) and US LVT legislative activity (Sightline WA, NY S7871) — 7 rows Referenced.

TIER-1 lane from issue #24 is COMPLETE: all 74 rows in registry; 24 research entries + 1 objection
page live; remainder registry-only by design or explicitly deferred (Fossum → books wave;
Hope-Limberg → general-tax, out of the rent lane). Issue closed; TIER-2 citation long-tail
continues in the normal loop. 826 pages; lint 0 errors.

---

## 2026-07-15c — Post-#24 loop: TIER-2 citations batch 2 + college-town LVT entry (session udw74p)

Scope-filtered TIER-2 continuation: places/south-korea gains a Contemporary Georgist Politics
section (Lee Jae-myung's land-dividend record + BIEN Korea's common-wealth-rent framing — Kang
PDF URL was truncated in the harvest and flagged [VERIFY], not guessed); NEF What Lies Beneath
cited on financialization-of-land; Equal Right's AI-commons framing added to the SWF proposal
landscape. New entry: miller-hoskins-college-town-lvt (South Bend 4:1 + Princeton ~3:1 parcel
simulations, advocacy-graded; both report PDFs read — Princeton found at its moved URL; the
advocates' own homestead numbers wired into the asset-rich-cash-poor objection's steelman).
Commits fe0c8d8 · 5edd217. 827 pages; lint 0 errors; registry 1,098 rows. Next iteration:
TIER-2 remainder by target page, then BACKLOG NOW lanes.

## 2026-07-16 — Wave (session 2z2oww): VERIFY burn-down + BACKLOG reconciliation

Floyd: "keep looping, find more useful things." Claimed the claim-lane enrichment wave;
discovered 4 of 5 claimed items were finished-but-unrecorded (sprawl at 6/5 w/ correct
challenged_by discipline; foldvary reply wired since wave 1; public-choice steelman +
raley both live) — BACKLOG NOW/NEXT sections reconciled against the page inventory so
future sessions stop re-planning shipped work. Real work of the wave: VERIFY burn-down,
10 markers closed across 10 pages (queue 27 -> ~16): Carver 1921 primary verbatim-confirms
Brown; CMHC HMA found DISCONTINUED (March 2022), page rescoped; GIS take-up quantified
(ESDC/Imbeau 2018: 89.8%, ~240k seniors) sizing the universal-transfers objection response;
Ontario CBC cap confirmed; BoC markups note confirmed by Faryaar et al 2023; C&C p.370
verbatim; fernandez-milan authorship settled; giovannoni negative finding dated; lapavitsas
honest downgrade (all channels walled); CIB provenance made exact. Registry +7 rows. lint
0 errors, warnings 30->20. T3: atcor Sources annotated; BC SVT rates verified current.
Coordination: udw74p's Slack lane + unmerged tail (forget/nyc/south-korea/split-rate)
deliberately untouched. Queue regenerated post-wave; next wave candidates: P&P + WoN
deepen-scans, WS-GEOISM financial-rents sweep, Life of Henry George read&mine.

## 2026-07-16 (later) — Gaffney corpus lane, wave 1 (Floyd's directive: hosting permission)

masongaffney.org inventoried (190 files: publications 87, workpapers 73, essays 30) into
sources/gaffney-corpus-triage.md; tier-1 (9 works) mirrored to sources/gaffney/ + OCR'd
(image-scanned PDFs; tesseract 200dpi, 72k words). READ&MINE, 8 new research pages:
- cycles: gaffney-causes-of-downturns (1982 — the 15-yr precursor to Foldvary 1997,
  ancestry wired) + gaffney-land-booms-destroy-capital (1993+2005 pair)
- tax-shift: europes-fatal-affair-with-vat, full-employment-tax-reform,
  excess-burden-shiftable-taxes (deadweight-loss gains an attributed-critique section,
  carefully 'alongside not instead of' Harberger)
- urban/resource: new-life-in-old-cities (9-city survey w/ Pittsburgh anomaly honestly
  in counter-evidence), california-severance-tax (+ actual Prop 87 defeat added),
  economics-of-abundance (D-claim polemic, labeled)
Claim lanes enriched: land-speculation-causes-cycles, cycles-are-credit-not-land,
lvt-can-replace-capital-taxes, taxing-land-raises-productivity, split-rate-increases-
construction, speculative-vacancy-wastes-cities, resource-rent-capture-works (novel
'capture lost, not never built' CA counter-example), tax-land-not-labor. All quotes
PDF-verified; working-paper/essay register throughout; 4 deliberate [VERIFY] markers on
second-hand claims. Coordination: nyc-1920s page untouched (udw74p's). Registry +9 rows
+ dated export. TIER 2 queued in the triage ledger. BLOCKED: Floyd's Notion priority
list (needs Notion-key approval or paste) — cross-check tier-1 when available.
Full-site preservation mirror: recommend R2 bucket (repo carries worked texts only).

## 2026-07-16 (evening) — Gaffney wave 1 addendum: G44 + Notion cross-check + R2 staging

Floyd's Notion priority list read (public-page API): 4/5 already covered; the gap —
G-44 "The Philosophy of Public Finance" (Losses of Nations ch.7, 1998) — mirrored, OCR'd,
research page shipped (organic-state theory, succession-premium base, formal ATCOR
derivation, Milwaukee isovalic study wired to split-rate-increases-construction as a
distinct data point). NOTABLE CORRECTION: the ATCOR acronym is first attested in this
1998 chapter, not WP096 (2005) — dated correction notes on concepts/atcor.md and
research/gaffney-atcor.md. tideman-plassmann backlog row annotated (book confirmed,
its own chapter still unobtained). Full-site mirror staged: 193 files/52.5MB local with
sha256 manifest (sources/gaffney-r2-manifest.csv); R2 upload BLOCKED on bucket access
(vault token is bucket-scoped) — Floyd to name/create buckets. archive_sources_r2.py
ready for the all-registry-PDFs preservation sweep (PRIVATE bucket; archive-not-serve
for copyrighted sources). 839 pages, lint 0 errors.

## 2026-07-16 (night) — archive.progress.org LIVE: full Gaffney mirror on R2

Floyd created buckets + token; executed the runbook: 193/193 objects uploaded and
size-verified to gaffney-archive; custom domain archive.progress.org attached via the
expanded progress.org zone token and serving (spot-checked 4 URLs incl. space-encoded,
byte-identical). All 12 Gaffney research pages now carry '[archived]' links beside the
masongaffney.org originals; the 10 mirrored PDFs removed from the repo (OCR texts kept;
sha256 manifest sources/gaffney-r2-manifest.csv is the record). Registry-wide PDF
preservation sweep into PRIVATE wiki-source-archive running (resumable;
sources/r2-archive-manifest.csv). Todoist task closed. Preservation posture: the corpus
now survives masongaffney.org's death; public serving limited to permissioned material.

## 2026-07-17 — License pass: 18 sources promoted to public archive, 16 wiki pages annotated

Classification (192 archived PDFs): rules pass found 26 candidates; T1 pre-review caught
substring/date false positives (treasury.govt.nz≠US, 'Canberra in Crisis' 1971, AJES 1971,
IP-paper 'public domain' as content); Sonnet doc-level verification settled 18
VERIFIED-PROMOTE / 7 HOLD / 1 already-public. Notable holds: Furman-Orszag (private
co-author on .gov host), Katz Commission (SA state copyright), Hudson AJES (© 2008).
Promoted set (server-side copy, size-verified): 6 US federal works, 7 CC-licensed
(variants recorded), 3 pre-1931 PD, 2 PD-stated — served at archive.progress.org/files/
with readable slugs; ledger sources/r2-public-files.csv. 16 wiki pages now carry
[archived] fallback links (14 auto via registry mapping + 2 hand-matched). Private
holdings stay private. Classifier .gov-final-label fix committed. Archive totals:
193 gaffney/ + 18 files/ public; 192 private. lint 0 errors.

## 2026-07-17 (cont.) — Wave: Gaffney tier-2 + link-health + archive retry

Gaffney tier-2 (3 units, quotes PDF-verified): gaffney-two-centuries-land-taxation
(K142, 1982 Lindholm&Lynn volume identified, registry row was mis-pointed/mis-dated —
fixed; Walras/Wicksell marginalist-founders evidence wired into progress-and-poverty-
outdated; Marshall 1909 into marshall-single-tax-objection; 13 people pages enriched);
gaffney-alaska-oil-leasing (1977 pre-PFD design study, AVC proposal, Prudhoe Bay
giveaway anchor -> resource-rent-capture 'design before the windfall' case);
gaffney-land-market-distortions (WP041+WP042, honest wiring declines documented).
Link-health: 16 registry 404s worked — 13 fixed (incl. wrong DOI, fabricated title
variant caught against the actual PDF, truncated URLs), 1 waybacked, 2 genuinely dead
(our monbiot article; the withdrawn Losses-of-Nations PDF — chapter citation precision
gained: 'Taxed Out of Work and Wealth' pp.146-174; $7tn row stays open). Archive retry
sweep: +62 preservation copies (254 archived total, 334+MB private). 842 pages, lint 0.
Process note: git add -A swept one agent's in-flight edits into a sibling commit
(verified correct, no damage) — explicit file lists are now the rule while agents run.

## 2026-07-18 — Wave: P&P DEEPEN-SCAN COMPLETE (all 10 books) + Cherokee primaries + Cincinnati

P&P full-text deepen-scan finished across three slices: 20 pages enriched with verbatim
Book/Chapter-cited primary material, 0 new pages needed (coverage validated). Highlights:
canons page now quotes George's actual per-canon application; cycles narrative quotes the
Book V mechanism; transition-shock carries George's harder no-compensation line contrasted
with modern phase-ins; wages-fund out of stub; T1 wired the Book IV 'rent would take
everything' limiting case into taxing-tech-rents as the 145-yr AI-rents antecedent.
Registry Scan Depth Medium->Heavy. Uncovered candidates logged (Spencer Social Statics,
Book VIII ch.I, spurious capital, Book X ch.IV decline mechanism).
Cherokee casino-dividend: primaries genuinely read (Akee 2010 full via PMC; 2018 via NBER
WP; Costello 2003 abstract-only, honestly graded) — and a prior-session fabrication caught
& corrected ('$6,000 by 2001' unconfirmable; 'fetched and read' overstated). 2018
personality-trait effects added. Top needs-new-source item closed.
Cincinnati queue scan: NDSPN report ingested (supplementary), queue item consumed;
sources/wiki-queue.json established as canonical committed intake.
843 pages, lint 0 errors.

## 2026-07-18 (cont.) — Wave: Gaffney timber/resource cluster + P&P follow-ups

Three research pages (quotes PDF-verified): gaffney-financial-maturity-timber (1957
NC State monograph — NOT Duke, NOT the dissertation, both corrected; tier Important on
external evidence: 81 citations, Newman 2002 historiography beside Samuelson 1976);
gaffney-forest-taxation (1977+1980 pair; site-value preference, 38%-equivalent yield-tax
calc; Forest Service as $42B undercapitalized asset -> resource-rent-capture gains the
renewable-resource institutional-failure case); gaffney-soil-depletion-land-rent (1965
Natural Resources Journal, peer-reviewed — land-is-just-capital objection gains the
fertility-depreciation response). P&P follow-ups earlier in wave: Spencer reversal with
George's 1897 footnote; land-monopoly Book VIII ch.I; rentier 1879 antecedent; Rogers/
Fawcett series; black-death<->Clark 2007 tie. Infra: B5 ampersand key broke the public
mirror URL — re-uploaded ampersand-free, manifest updated, live 200. Gaffney corpus now
15 research pages + person page; remaining tier-2 queued in triage ledger. lint 0 errors.

## 2026-07-18 (cont.) — Wave: WoN Book III + needs-new-source forage trio

WoN Book III: ch.IV mined (ch.II found already covered — correctly skipped); land-monopoly
+ book page (first Book III section, honest open question on commerce-vs-LVT) + adam-smith
+ highland-clearances (Smith's 1776 near-contemporary account). Jeffery-J.-Smith-vs-Adam
citation trap caught. Forage trio: all three items RESOLVED — Letchworth and symmetry/
decrement were already shipped (wave 4, ed8f40b) but BACKLOG never flipped; both
independently re-verified against primaries (O'Sullivan BPJ 2017 verbatim; Letchworth
2024 accounts figures exact; Hagman/Uthwatt anchors re-confirmed; the Hayek ch.22 lead
DEBUNKED — it's monetary policy, not betterment). COST enriched with real Taiwan
performance data (Lam & Tsui 1998 read in full: LVIT capture ~32% of assessed vs 40-100%
statutory, Taipei 1979-93); Niou & Tan 1994 genuinely paywalled, logged for Hermes.
needs-new-source channel now EMPTY. 846 pages, lint 0 errors.

## 2026-07-18 (cont.) — READ&MINE: Life of Henry George (Henry George Jr., 1900)

BACKLOG public-domain-texts NEXT TARGET. Pre-check confirmed the full text was already
ingested (2026-07-09 wave: books/life-of-henry-george.md + sources/publicdomain/
life-of-henry-george.md, Scan Depth Heavy) — this shift's job was the READ&MINE, not
the ingest. Read strategically by chapter (Second Period Ch. III "flash of insight,"
Ch. IX-X P&P composition; Third Period Ch. VIII 1886 campaign, Ch. IX Standard/
Anti-Poverty Society/McGlynn excommunication, Ch. IV Loughrea-Athenry Irish arrests,
Ch. XIV the 1897 death). Delta-mined into books/progress-and-poverty.md (new "How the
Book Was Written" section — the First Street workroom, Dr. Taylor's role, the
finishing-night quote, and the verbatim 1883 Dawson letter: "I flung myself on my
knees and wept like a child"), people/henry-george.md (the teamster "flash of insight"
quote + richer 1886/1897 political-career detail), events/1886-nyc-mayoral-election.md
(Ivins "raise hell" exchange, exact vote totals 90,552/68,110/60,135, Cooper Union
speech, Bunker Hill speech, Hewitt's letter — page was previously thin and lacked vote
totals entirely), people/michael-davitt.md (corrected/enriched the Athenry note — it
was actually two separate arrests, Loughrea then Athenry, with the Eton-master Joynes
detail and George's own account). Three new sourced stubs for figures/events the
biography showed were real gaps: people/edward-mcglynn.md (excommunicated ally,
including the 1892 Satolli reinstatement — richer than expected, found in Ch. XIII),
events/1897-nyc-mayoral-campaign.md (the fatal second run), organizations/
anti-poverty-society.md. All quotes PD-exempt from the 50-word cap (pd_quotes: true
added where flagged). registry.csv In-Wiki Citations for this source: 2→10; dated
export regenerated (sources/exports/registry-export-2026-07-18.csv). BACKLOG line
flipped to done. 849 pages, lint 0 errors, 30 warnings (unchanged by this wave — all
new-page warnings resolved). No commit (per task instruction) — working tree has the
changes.

## 2026-07-18 (cont.) — Wave: VERIFY unclassified burn-down (queue 33 -> 22)

9 resolved / 3 honest downgrades across 10 pages. Highlights: the 1960 CHPC report
identified precisely (title, May 1960, Schalkenbach-funded, Rybeck preface — via OCR of
the digitized primary); leduc-liu + Green-reanalysis publication upgrades (Green's
published version argues the OPPOSITE causal reading of Mincome — added as honest
nuance); August's REIT counts corroborated by StatCan CHSP land-registry data; Mintz-Chen
Australia figure verified against the paper's own table; two never-published leads
(Walks Part II; a land-specific efficiency-wage test) closed as SETTLED so nobody
re-chases them. Remaining unclassified markers are all deliberate gaffney-* flags.
MERGE NOTE: forget-mincome + nyc-1920s edits may conflict with udw74p's unmerged tail —
normal git conflicts, both sides' edits are compatible in substance. 853 pages, lint 0.

## 2026-07-18 (cont.) — Wave: Doucet ACX de-referencing + T3 cohesion

Doucet Parts 1+3 fully de-referenced against the live essays: 50 scholarly citations
enumerated, 33 already carried (the corpus has absorbed most of Doucet's evidence base
across prior waves), 12 added as Referenced/Light (ONS Blue Book, Gloudemans-Almy IAAO
textbook, ifo Grundsteuer study, both IAAO standards, Gaffney WP097, the six-country
mass-appraisal case-study tail — one Doucet mis-date flagged), 5 rejected with reasons.
Durable ledger: sources/doucet-acx-dereferencing.md — this task can never be re-done
blind again. Page candidates queued: Gloudemans-Almy, the IAAO standards pair, a
six-country mass-appraisal synthesis. T3 cohesion: 4 link-text fixes, terminology
otherwise conformant; BC/Vancouver overlap reviewed at T1 — already compliant, no churn.
853 pages, lint 0 errors. (Session-limit interruption mid-wave; recovered cleanly.)

## 2026-07-18 (cont.) — Wave: WoN Book II + Book IV deepen-scan

Smith's chapter-length engagement with the Physiocrats (Book IV Ch. IX) mined into
concepts/physiocrats.md (Colbert-overcorrection origin, three-class restatement,
five-point rebuttal of "barren and unproductive," the "with all its imperfections...
nearest approximation to the truth" verdict, physician/"exact regimen" analogy +
principle-of-preservation rebuttal, Mirabeau "three great inventions" tribute in
Smith's primary rendering) and people/francois-quesnay.md ("very ingenious and
profound author"). Book IV Ch. VII colonial land-engrossment natural experiment →
concepts/land-monopoly.md (improve-or-forfeit colony law, quit-rent-on-alienation,
"greatest obstruction to its improvement"). Book II Ch. V "work of Nature" second
rent theory → concepts/economic-rent.md, flagged honestly as in tension with the
Book I monopoly-price account. Zero-addition verdicts recorded: Turgot never named
in WoN (full grep); Book II Ch. II banking read but NOT forced onto
bank-money-creation (specie-displacement ≠ endogenous money); invisible-hand passage
read, no land/rent bearing. Scan-depth ledger on books/wealth-of-nations.md updated
(Book IV Ch. IX → Heavy; Book II Ch. V + Book IV Ch. VII → Medium; strict-delta
reasoning recorded inline). All quotes verified verbatim vs repo-hosted PG #3300
text (T1 re-verified 4 spot checks incl. capital-N "Nature" readings). 855 pages,
lint 0 errors.

## 2026-07-18 (cont.) — Wave: Gloudemans-Almy "Fundamentals of Mass Appraisal" book page

books/fundamentals-of-mass-appraisal.md created (856th page) — the assessment
profession's standard textbook, de-referenced WITHOUT pretending to read it: built
from IAAO Course 300 syllabus (structural proxy, flagged as a compression), the
Standard on Mass Appraisal's dozen+ page-specific citations to the book (land
valuation pp. 178-180, PRD/PRB pp. 385-392), and the authors' freely available
papers. Genuine Georgist gain: Gloudemans's separate Lincoln Institute LVT work
(2000 fellowship paper + 2002 WP02RG1, fetched and read in full) — CAMA models
"can predict land values with acceptable reliability, even when some neighborhoods
lack vacant land sales altogether." Page states plainly the textbook is NOT an LVT
advocacy source and should only be cited for the narrow standardization point.
Honest gaps recorded: no direct read, no reception literature found, 604-pp count
unconfirmed for 2011 print. 5 inbound links wired (bar ≥2): iaao-standards,
mass-appraisal-international-cases, almy-oecd, doucet-does-georgism-work (moved
from "second-hand only" list), mass-appraisal-methods. Registry: FMA row →
Scanned, 4 new source rows. 856 pages, lint 0 errors.

## 2026-07-18 (cont.) — Wave: Gloudemans LVT feasibility papers + BC SVT rate check

research/gloudemans-lvt-assessment-feasibility.md created (857th page): BOTH Lincoln
working papers (WP00RG1 2000, WP02RG1 2002) fetched via curl+pdftotext and read in
full. Mined: improved-only baseline CODs 5.87/5.75/8.82; combined vacant+improved
model barely moved improved accuracy (5.97/5.55) while fixing the land/building
split; vacant CODs 9.55-22.96 (consistent with IAAO's wider vacant tolerance, carried
honestly); the "no or few vacant sales" headline conclusion; PLUS the 2000 paper's
distributional caution (land-ratio shift correlates with age/size/quality, r=.63-.71,
"less advantageous to lower-value... properties") — a counter-evidence find carried
into land-cannot-be-assessed Limits. Provenance stated plainly: single-author,
Lincoln-funded, "not subject to detailed review," inconsistent fellowship names
between the papers' own citations (flagged, not reconciled), inconsistent Ada County
sample counts, no independent replication found. Wired: land-cannot-be-assessed
(Response 3d + Limits), fundamentals-of-mass-appraisal, mass-appraisal-methods.
BC SVT rate backlog item: NO EDIT NEEDED — british-columbia.md already carries the
2026 1%/3% rates with a sound gov.bc.ca cite, independently re-verified by fresh
fetch this session (backlog note about vancouver.md carrying the figures was wrong).
857 pages, lint 0 errors. Registry rows deferred to DST-wave commit (single-writer).

## 2026-07-18 (cont.) — Wave: DSTs-as-tried (WS-TECH-RENTS part a)

research/digital-services-taxes.md created (858th page) — country-by-country record
of DSTs as run, deliberately complementary to the existing incidence page (delta
rule: Muddasani-Langenmayr pass-through stays there; this page carries revenue +
political economy). Verified from primary fetches (NAO 2022, HMT Nov-2025 review,
OECD IF Jan-2025 co-chair statement, Assemblée nationale answer, Canada DoF —
garbled PDFs recovered via curl+pdftotext): UK £358m→£808m with 90% of yr-1 from 5
payers and a derived ~£2.80bn 5-yr cumulative flagged as OUR arithmetic vs HMRC/OBR
">£3bn" forecast; France €277m vs €400m forecast, CCIA-commissioned 55/40/5 incidence
split flagged as industry ex-ante modeling; India's two-piece levy dismantled
2024-25; Canada's DST rescinded 3 days after the June-2025 tariff ultimatum; Pillar
One treaty still unopened for signature per the IF's own statement — so the promised
multilateral DST retirement has actually proceeded only by unilateral coercion.
Georgist reading kept on the rent gradient: a DST is a REVENUE tax, not a rent tax.
Omissions recorded on-page: India multi-year collections (search-synthesis only),
Canada ~$2bn first payment (403s), India Pillar One-vs-Two attribution (sources
conflict), France rate flagged fast-moving. Wired: taxing-tech-rents §2 (primary
home), dst-incidence, data-rents, resource-rents. Registry +12 rows (DST) + deferred
Gloudemans merge (2000 row added; 2002 row Medium→Heavy, citations 1→4, wiki-page
repointed to the new deep-dive). Inventory regenerated. 858 pages, lint 0 errors.
WS-TECH-RENTS remaining: (b) attention/ad rents, (c) dissolution vs capture,
(d) is-it-rent diagnosis update, then the gated instrument-comparison synthesis.

## 2026-07-18 (cont.) — Wave: attention/ad rents (WS-TECH-RENTS part b)

Agent discovered the Romer proposal page ALREADY EXISTED (research/
romer-digital-advertising-tax.md, commit 75b4503) — stale backlog note honored via
delta rule: no duplication; built the genuinely missing piece instead.
research/maryland-digital-ad-tax.md created (T1 renamed from the agent's
digital-ad-taxes-romer slug — confusably close to the existing proposal page):
Maryland's Digital Advertising Gross Revenues Tax as Romer's real-world test.
Verified: cliff-not-marginal rate schedule 2.5/5/7.5/10% by global revenue tier —
a design DEPARTURE from Romer flagged on-page (no targeted-ads carve-out, no
subscription escape hatch); litigation as the main story (2022 trial-court
invalidation reversed 2023 on exhaustion grounds ONLY, merits still pending in
Tax Court; Fourth Circuit Aug-2025 struck the pass-through-disclosure ban on First
Amendment grounds, final injunction Oct-2025; core tax still in force); revenue
~$93M/$82.5M FY22/23 vs $250M projection, flagged press-reported. Honest gap
recorded: NO ex-post incidence estimate for Maryland exists (unlike UK DST's
Amazon evidence). Prat-Valletti carried at abstract level, disclosed. Wired:
taxing-tech-rents §3, romer proposal page (paired-page pattern), dst pages,
data-rents. Registry +12 rows. Lint 0 errors (inventory regen deferred to wave
close — Ch. 21 cluster agent still in flight).

## 2026-07-18 (cont.) — Wave: Doucet Ch. 21 capitalization cluster (5/5 de-referenced)

Scope correction found first: 4 of 5 papers (Borge-Rattsø, Capozza-Green-
Hendershott, Hilber, Buettner) already had research pages from an earlier wave —
another stale backlog note. Real gaps closed: (1) Choi & Sjoquist (2015) — full
Land Economics article fetched (gwern.net mirror) and read; new standalone page
research/choi-sjoquist-atlanta-lvt-cge.md (859th page): full capitalization onto
landowners under fixed boundaries, welfare gain 18-19% of revenue (~3x DiMasi
1987), and the previously-unmined PROGRESSIVE incidence result across income
groups; a source-INTERNAL inconsistency (82.9% vs 89.2% fixed-boundary revenue-
neutral rate, both verbatim in the primary at pp. 544/546) carried as a deliberate
[VERIFY] flag rather than silently resolved. 6 inbound links. (2) Buettner (2003)
upgraded abstract-only → Heavy: full text obtained, Table 2/3 coefficients mined
(land-value elasticity -0.314 GMM, rent coefficient ≈0 insignificant,
"substantial overcapitalization" vs theoretical 3.6%), Nebenkosten/rent-control
institutional detail added. Benefit pages wired with the model-evidence-not-
measurement caveat kept explicit. Doucet de-referencing ledger addendum written;
BACKLOG item checked off. Registry: no new rows (all 5 pre-existed); rows 564/637
Referenced→Scanned, Light→Heavy, citations updated. Inventory regenerated.
860 pages, lint 0 errors. All five Doucet Ch. 21 citations now rest on primary
text — none abstract-only, none second-hand.

## 2026-07-18 (cont.) — Wave: P&P Book X Ch. IV decline mechanism (strict delta)

The last uncovered candidate from the all-10-books P&P deepen-scan closed. Pre-check
confirmed Ch. IV was genuinely unmined and that the natural home already existed
(concepts/georgism.md "The Civilizational Argument (Book X)" section — so NO new
law-of-human-progress page, per delta rule). Ch. IV read in full plus Chs. I/III/V:
the political mechanism mined (universal suffrage as route TO despotism once wealth
concentrates; "government of the worst"; corrupted-franchise/tramp-pauper argument;
Prætorian Guard analogy for city machines; "leap upward or plunge downward"), plus
the "tomb of the dead empires" and Rome-from-within passages backing the thesis
paragraph. Method caveat extended honestly: 1870s pre-archaeological armchair
comparative history, carried as P&P's philosophical capstone, NOT an evidenced
collapse theory the wiki endorses. Ch. II correctly skipped (Spencer-critique
preamble, no distinct claim); Ch. V rhetoric not over-mined. All quotes T1
re-verified verbatim (5/5) against texts/progress-and-poverty-full-text.md.
books/progress-and-poverty.md gains the fourth-argument note + cross-link. New lint
warning is George's own quoted "always" — correct as a quote. No registry change
(source already Core/Heavy). 860 pages, lint 0 errors.

## 2026-07-18 (cont.) — Wave: rent dissolution vs capture (WS-TECH-RENTS part c)

research/tech-rent-dissolution-vs-capture.md created (861st page) — the enforcement
record complementing the existing DMA design page (paired-page pattern, delta rule
held). The Georgist asymmetry stated as the frame: land rent has no dissolution
option (fixed supply), some platform rents do — and where dissolution works it
beats capture. Verified from primaries/near-primaries: first DMA fines 23-Apr-2025
(Apple €500m Art. 5(4), Meta €200m Art. 5(2), both on appeal); gatekeeper roster
incl. Booking.com add + Facebook-Marketplace un-designation; WhatsApp Art. 7
interop launched Nov-2025 to two minor rivals; Mozilla choice-screen gains flagged
as vendor-self-reported; Epic iOS store ~29M vs 100M target. US record: Mehta
rejected Chrome/Android divestiture for data-access remedies (dissolution by data
sharing); Brinkema ad-tech remedies STILL PENDING (flagged, not predicted);
Boasberg's FTC-v-Meta loss carried as the no-moat-found case. Counter-case argued
(Schumpeter/scale-efficiency, Cambridge security paper on interop messaging,
Signal's objection). 3 new banned-word lint warnings T1-reviewed and accepted:
two state the land-side asymmetry (core doctrine), one conditional, one hedge.
Wired: taxing-tech-rents §5, quasi-rents objection Limits, DMA page, Furman page,
data-rents. Registry +16 rows. Inventory regenerated. 861 pages, lint 0 errors.
WS-TECH-RENTS: only (d) is-it-rent diagnosis update remains before the gated
instrument-comparison synthesis.

## 2026-07-18 (cont.) — Wave: is-it-rent diagnosis update (WS-TECH-RENTS part d — lane discovery COMPLETE)

Assigned targets (Furman diagnosis, Korinek-Stiglitz 2017, De Loecker markups) all
verified as ALREADY Heavy-scanned from earlier waves — three verified no-ops, no
churn. Agent instead found and mined two genuinely new on-point papers:
(1) research/korinek-vipra-ai-concentration.md (862nd page) — INET WP 228 / Economic
Policy 2025, read in full: the rent MECHANISM specified (fixed compute costs, Nvidia
92-98% GPU share — internal 92 vs cited-Wells-Fargo 98 discrepancy flagged not
resolved; intelligence feedback loop), authors' own phrase "monopoly rents" — BUT
their own Sept-2024 market snapshot shows near-Bertrand pricing among frontier labs:
diagnosis carried as mechanism-present/rent-not-yet-realized. (2) research/
korinek-lockwood-ai-public-finance.md (863rd) — NBER WP 34873 Feb-2026, read in
substantial part (formal proofs §§3-4 honestly NOT relied on beyond authors' prose):
independently derives the wiki's own rent-gradient principle ("tax rents of fixed
factors... unimproved land, spectrum rights, unique datasets... no distortion") and
maps every live AI-tax proposal onto capital-vs-consumption logic. Wired into
taxing-tech-rents (AI coda + Sources 21-22), data-rents, both existing Korinek/
Furman pages, quasi-rents objection. Registry +2 rows. 863 pages, lint 0 errors.
GATE OPEN: WS-TECH-RENTS a-d all done → instrument-comparison synthesis unlocked.
Synthesis must reconcile against Korinek-Lockwood Table 3 (DST/robot-services =
consumption-tax-like vs compute/robot-ownership = capital taxes) and decide
include-or-exclude-with-reason for their SWF/windfall-clause/UBC family.

## 2026-07-18 (cont.) — Wave: Gaffney Alaska 1977 Part II Appendices A-L (VERIFY resolved)

The deliberate Part-I-wave flag closed: Part II (155pp image scan) found on the
local gaffney mirror, OCR'd via pdftoppm+tesseract (mid-run agent stall recovered
by coordinator nudge after OCR completed 155/155), text committed to
sources/gaffney/text/. Standout find: Appendix E — Norgaard's Cook Inlet
regression (Lease Sales 7 and 9) showing bonus bidding captured only ~9-16% of
realized rent — independent ECONOMETRIC corroboration of Part I's anecdote-based
case, now wired into benefits/resource-rent-capture-works (explicitly labeled
corroborating-not-load-bearing) and concepts/resource-rents. Appendix C resolves
Part I's unspecified leaseholder-concentration claim with real numbers (top-5
noncompetitive = 53.8% of acreage); H/I give the AVC's worked 2.5:1 split on real
Sadlerochit data; J the royalty-timing-bias algebra (banned-word fix: "derives"
not "proves"); D/F/G/L the Crommelin/Rooney alternatives. Contributor dissent:
NONE FOUND — reported as absence, not tacit agreement, with a scoped VERIFY. 4 new
deliberate VERIFY flags all narrowly scoped (Vickrey/Consigny original not located;
OCR-poor pages not quoted; correspondence unchecked; Part I circulation history
untouched/out of scope). Triage ledger row checked off. Registry +1 row (Part II).
863 pages, lint 0 errors. Task #28 wave complete — WS-TECH-RENTS synthesis next.

## 2026-07-18 (cont.) — Wave: WS-TECH-RENTS GATED SYNTHESIS (T1) — lane COMPLETE

The instrument-comparison revision, graded at T1 per the model directive. Decisions:
(1) DST's D STANDS, now with independent corroboration — Korinek-Lockwood's
classification of the DST as consumption-tax-like is convergent, not contrary
(both frameworks agree the platform doesn't bear it; "efficient consumption tax"
and "failed rent tax" are the same fact viewed from different questions) —
reconciliation note added to §2. (2) NEW FAMILY §6: AI-specific taxes
(compute/token/robot) graded D-provisional — input taxes in rent-tax clothing,
deferred even by their friendliest analysts (K-L: services-variants pattern as
consumption taxes, ownership/compute variants are capital taxes to defer);
taxing inputs before the rent arrives is the REVERSE of the Georgist sequence.
(3) NEW FAMILY §7: public equity stakes (SWF/windfall clause/UBC) INCLUDED and
graded B-minus — the only incidence-proof instrument in the table (an equity
claim reprices nothing), Alaska Permanent Fund as the real precedent, but the
fair-value-acquisition trap stated plainly (buying equity at market price
captures no rent — same trap as buying land to "capture" its rent; Alaska worked
because the state already owned the oil). Grades table now 7 rows + K-L
cross-check note; patents-exclusion heading retitled (numbering went stale);
AI coda hand-off line closed out; honest-limits bullet extended. 863 pages,
lint 0 errors. WS-TECH-RENTS lane (a,b,c,d + synthesis) is DONE.

## 2026-07-18 (cont.) — Wave: T3 mechanical debt batch

Source annotations: 23 entries across 15 most-neglected pages (no last_reviewed at
all) annotated with usage DERIVED from each page's body — 1 honestly left
unannotated with an inline note (economic-rent's Mill entry: role not determinable
from page text; flagged, not invented). Thin-article burn-down, 4 high-inbound
pages, all expanded from material ALREADY in the repo (no new external claims):
henry-george-theorem 358→749 words (Behrens second-best extension + Feldstein
capitalization challenge with CKR/Fane replies — the wiki's own research pages
finally surfaced on the concept page; one garbled Feldstein sentence fixed at T1);
rent-seeking 346→802 (growth-cost + tax-design sections); split-rate-taxation
322→632 (Harrisburg + practical obstacles from Cohen-Coughlin); 1909-peoples-budget
355→673 (the four land-value duties with statutory rates from the book page).
Warning count verified unchanged vs baseline (git-stash comparison). ~400 pages
from later cohorts left for future recurring batches. 863 pages, lint 0 errors.

## 2026-07-18 (cont.) — Wave: stub-queue leftovers (3 backfills created, 4 honest skips)

All three NAMED candidates (sector-model, margin-of-production, progress-and-
poverty-institute) turned out to ALREADY EXIST fully written — stale backlog notes;
P&P-institute was below the accept bar at 1 inbound and got wired to 4. Real
output = the lloyd-george/BC backfill candidates, accept-bar-tested one by one:
CREATED people/henry-george-jr.md (8+ citing pages, Congress Bioguide/House
Historian verified; 1897-candidacy detail honestly left thin rather than padded),
organizations/bc-assessment-authority.md (BC Assessment's own corporate history,
3 inbound), events/parliament-act-1911.md (5 near-duplicate passages across UK
pages consolidated into one linkable home, primary statute cited, 5 inbound).
SKIPPED with reasons: 1913-bc-crash (already fully treated on vancouver/l-d-taylor,
a page would duplicate), land-enquiry-committee (1 substantive mention — fails
bar), 1925-green-book (only the discovering page mentions it), balfour (all 5
mentions tangential, confirming the backlog's own caveat). Registry rows deferred
to scratchpad (Gaffney agent holds the registry lock this round); inventory regen
deferred to wave close. Lint 0 errors at agent close (867 pages incl. Gaffney
agent's in-flight work).

## 2026-07-18 (cont.) — Wave: Gaffney tier-2 land-theory batch (C9 + D1; C2 declined with reasons)

C9 "Land as a Distinctive Factor of Production" (1994, 64pp native text): the
one-paragraph stub page substantially rewritten against the actual chapter — ten
land/capital distinctions plus the original B-8/B-9 credit-concentration mechanism
("the basis of credit is not marginal productivity, but collateral security";
land purchase "not self-liquidating") — advocacy tone flagged in Gaffney's own
words, and his Clark/Seligman motive-claims flagged AGAINST the wiki's existing
Missemer-Pottier/Milgate counter-findings rather than swallowed. D1 "Rising
Inequality and Falling Property Tax Rates" (1992, 19pp): new research page — farm
Gini 0.63 (1930) → 0.92 (1988, vanished-farms-adjusted) as farm property tax rates
fell 40%; carried as observational/cross-sectional, no regressions, causation left
open per Gaffney himself; wired into land-monopoly (new credit-mechanism
subsection), split-rate-increases-construction (17th supporter), land-is-just-
capital. C2 welfare-economics essay READ IN FULL but DECLINED a page — diffuse
programmatic overlap with existing coverage; bibliographic details logged in
triage for a future call. D1's ampersand-filename mirror rot found and worked
around (%26 refetch; archive mirror 404s — known B5-class issue). Registry: C9
row Light→Heavy, D1 new row, + 7 deferred stub-wave rows merged (Parliament
Act/House-Historian/BC-Assessment sources). Inventory regenerated (5 new pages
absorbed). 867 pages, lint 0 errors, warnings back to 32.

## 2026-07-18 (cont.) — Wave: Gaffney E11/E12 urban-land-rent pair (+ BACKLOG reconciliation committed separately)

research/gaffney-urban-land-rent.md created (868th page, Core tier) — the 1972-73
AJES two-parter read in full (ampersand mirror-rot hit as predicted; %26 refetch;
BOTH stale 404-stub mirror files REPAIRED in cache so future sessions don't
re-hit it). Part I: tripartite urban-rent sources (natural features, public
spending, synergism); rent rations land, never elicits supply. Part II: five
taxation mechanisms, fullest being the strong-hands/weak-hands credit
discrimination argument WITH worked leverage arithmetic (poor buyer's holding-cost
ratio 1.8→3.0 as land appreciates) — the earlier original of C9's B-8/B-9
mechanism, cross-wired. Also mined: a pre-Stiglitz informal HGT capitalization
statement ("conservation of economic energy," crediting Jensen 1931) — added to
henry-george-theorem's Origin as an intermediate data point, strict-delta with the
just-shipped Behrens/Feldstein material; and a logrolling political-economy
argument absent from later Gaffney. Honest limits: advocacy-toned theory, one
descriptive Milwaukee cross-section, several claims on Gaffney's own authority.
Congestion section deliberately NOT wired (no matching objection page — recorded,
not forced). sprawl page addition explicitly kept OUT of supported_by (theoretical
context, not evidence). Registry +2 rows; triage rows checked; inventory
regenerated. 868 pages, lint 0 errors.

## 2026-07-18 (cont.) — Wave: VERIFY-channel regeneration + 5 resolutions

Ground-truth census regenerated: 30 live markers → classified 13 DELIBERATE-SCOPED
(honest records, stay), 6 RETRYABLE (queued with approach), 3 BLOCKED (attempted
this wave: Samuelson 1976 paywalled everywhere free; 1971 Milwaukee Journal not
digitized; unpublished Andelson address untraceable), 5 RESOLVED with real fetches:
Vickrey/Consigny proof pinned to its exact primary (Appendix II, Gaffney
"Tax-Induced Slow Turnover of Capital" Part V, AJES 30(1) 1971 pp. 105-111,
fetched from masongaffney.org and cross-checked word-for-word vs the Alaska-report
reprint); South Korea BIEN presentation URL reconstructed + author-name corrected
(Nam Hoon Kang); Pittsburgh 10%-of-base figure corroborated via Hughes 2006
Lincoln WP tracing to Snowbeck, Post-Gazette 15-Jan-2001; forest-taxation venue
identified (Knedlick ed., Lincoln 1980); Now-the-Synthesis publication confirmed
and linked to the existing book page rather than re-read. verification-queue.md
rewritten in 3-way classified format; backlog narrative dated; hermes-workorder
auto-regenerated. VERIFY warnings 30→25 (exactly the 5 resolutions). 868 pages,
lint 0 errors.

## 2026-07-18 (cont.) — Wave: terminology normalization (the 2026-07-04 audit's last open half)

EDITORIAL §Terminology's 2026-07-11 rulings applied (they win over de facto counts).
Corpus found ~98% compliant already: citizen's-dividend family — 5 stray
mid-sentence capitals fixed (24 grep outliers all turned out to be out-of-scope
scratchpad files); 18-year-cycle family — ZERO fixes needed, all ~26 "18.6-year"
instances already correctly gated to Anderson's specific claim with caveats,
"property cycle" correctly recognized as a different term and left alone;
single-tax family — 6 genuine violations fixed out of ~1,900 raw instances
(the rest legitimate proper names/titles/quotes). Judgment calls recorded IN
EDITORIAL (not silently): "Single Tax movement" kept as historiographic
capitalization; Anderson's branded "Citizen's Dividend concept" kept. EDITORIAL
§Terminology extended with the cycle-naming distinction + closeout note so this
never re-litigates. BACKLOG cohesion item fully closed. No anchor breaks (no
heading edits). 868 pages, lint 0 errors, warnings unchanged — audit-grade no-op
where the corpus was already right, which is the correct outcome for a
normalization pass on a well-maintained corpus.

## 2026-07-18 (cont.) — Wave: Gaffney extractive-resources cluster (B1 volume + B4/B13 pair)

research/gaffney-extractive-resources-taxation.md (869th) — the 1967 TRED volume
bookends (26pp intro + 117pp conclusion, native text): STRICT-DELTA catch of the
wave — the ripeness/Figure C.4 timing theory turns out to be THIS essay, reused by
Gaffney as the Alaska report's appendix a decade later; recognized and
cross-referenced, NOT re-derived. Page carries what's genuinely new: the 1967
property-tax-vs-income-tax instrument comparison for exhaustibles + nine-reason
exploration-overmotivation taxonomy; strong-hands mechanism flagged as third
occurrence (corroboration only). Gray's reprinted 1914 QJE piece not summarized
(not Gaffney's work). research/gaffney-mineral-leasing-tax-reform.md (870th) —
B4+B13 combined as companion rent-leakage essays: B4's eight Crown-leasing errors,
Rent=Profit−Interest identity, BNA s.125 discussion (publication year unconfirmed,
[VERIFY], dated ~mid-70s from internal Turner-budget evidence); B13's 1982 US
loophole catalogue, strongest delta the ~80%-of-lease-cost-expensed-via-
abandonment mechanism absent from the capital-gains page. B13 mirror was another
ampersand 404-stub (%26 fix now confirmed generalizing across 5 files). B13's
factual figures honestly attributed to Gaffney's own trade-press citations, not
independently verified; neither paper claims econometric revenue estimates.
Wired: resource-rents (2 subsections), resource-rent-capture-works (modes 6-7 +
supported_by), capital-gains page, mason-gaffney. Registry +4 rows; triage rows
checked. 870 pages, lint 0 errors. (T3 batch-two agent still in flight; inventory
regen deferred to wave close.)

## 2026-07-18 (cont.) — Wave: T3 batch two (annotations + quote-cap compliance)

Annotations: the 2026-07-03..06 cohort (~90 pages) surveyed and found ALREADY
substantially annotated from earlier passes — first-pass grep false-positives
(line-wrapped phrasing, equivalent wording) manually adjudicated; 18 genuinely
thin entries fixed across 14 files, each derived from page text. Coming in under
the ~25 estimate is the honest outcome, not a shortfall. Quote caps (EDITORIAL
§1.5 ≤50 words per copyrighted work): precise per-quote counter built (fixing
naive blockquote-merge inflation); 4 pages/5 instances confirmed over-cap and
trimmed-or-paraphrased (worst: a 96-word Lie quote → 12-word verbatim close);
PD-exempt pages (Pigou/Smith-lectures/Walras/George quotes) correctly left; 4
apparent offenders cleared as parser false-positives. Baseline warnings verified
unchanged via git-stash comparison. Inventory regenerated (2 extractive pages
absorbed, warnings 36→34). 870 pages, lint 0 errors. Task #35 wave complete.

## 2026-07-18 (cont.) — Wave: Gaffney C4/D3/E10 + index sync (verified clean)

Three works, three pages (871st-873rd), two PRIORITY CORRECTIONS: (1) C4 "The
Unwieldy Time-Dimension of Space" (AJES 1961) is the earliest dated Gaffney in
the corpus — the algebraic root of the strong-hands credit mechanism, so
land-monopoly's earliest-statement attribution corrected 1972-73 → 1961; the
recurring conclusion held as corroboration-only (4th occurrence), page carries
the genuinely new time-indivisibility/leasing-critique/dynamic-equilibrium
content. (2) E10 "Land Planning and the Property Tax" (AIP Journal 1969) is the
PRIMARY of the Milwaukee isovalic 20%/50% study the wiki carried via the 1998
philosophy-of-public-finance restatement ("galloping merger movement" phrasing
near-verbatim) — citation priority corrected on that page + split-rate page,
Milwaukee material NOT re-derived; new page carries only the uncovered
building-tax credit-leverage mechanics + the seven-point LVT-increases-planning-
power argument. (3) D3 "Benefits of Farm Programs" (AJES 1966): Ricardian
subsidy-incidence catalogue + the original intensity-quotient rent-seeking
mechanism, wired into public-investment-capitalizes and rent-seeking-drags-growth.
D3 volume/issue unrecoverable from text ([VERIFY], B4 precedent). Index-sync:
problems (13) and benefits (15) indexes verified complete, zero dead rows, all
four expanded-page blurbs still accurate, evidence_strength buckets spot-checked
across all 28 — NO edits needed, verified-clean is the recorded outcome.
Registry +3 rows; triage 3 rows checked; inventory regenerated. 873 pages,
lint 0 errors.

## 2026-07-18 (cont.) — Wave: Gaffney urban-housing cluster (E14 reconciled; E3+E22 mined; E1/E37 declined)

E14 reconciliation: the unchecked row IS the synergistic-city page's sole source
(Lincoln Colloquium 1977 / Real Estate Issues 1978 match) — but the page had been
built from an ABSTRACT-ONLY read; PDF fetched and read in full this wave, registry
Light→Heavy, page enriched with the two missed findings (pollution/open-space
myth-busting; postage-stamp cross-subsidy mechanism, cross-linked to its earlier
1964 statement). Two new pages: research/gaffney-containment-policies-urban-sprawl
(874th) — the 1964 Kansas chapter, EARLIEST corpus statement of the LVT anti-sprawl
argument (negative/neutral/positive containment trichotomy; "cheap to buy, but
dear to hold"), wired into lvt-reduces-sprawl as historical priority, kept OUT of
supported_by per convention; research/gaffney-land-as-element-of-housing-costs
(875th) — the 1968 IDA/HUD study: pre-Oates capitalization argument for credit-
constrained buyers + the federal holdout-reward tax catalogue (1031, stepped-up
basis), wired into housing-affordability likewise as context-not-evidence, dated
1968 tax specifics flagged. DECLINED with reasons: E1 (1958 USDA — now the
earliest dated work known, but content overlaps existing coverage; flagged as
future priority-correction candidate), E37 (zero-addition vs new-life-in-old-
cities + urban-land-rent; [VERIFY] on its undated provenance). All five fetched
native-text from masongaffney.org (%26 fix again clean). Registry E14 upgraded
+2 new rows (none for declines, C2 precedent); triage 5 rows checked, batch-5
narrative. Inventory regenerated. 875 pages, lint 0 errors.

## 2026-07-18 (cont.) — Wave: VERIFY retryables (3/3/0) + E1 1958 priority corrections

Retryables: 3 RESOLVED (August REIT figures spot-checked line-for-line against a
second independent T&F-typeset mirror; Clawson $42bn corroborated via the Science
1976 PubMed abstract, granular split honestly left as Gaffney's citation;
soil-depletion citation count = 21 via Semantic Scholar) and 3 BLOCKED with
documented attempts (WorldCat 403/429 on Alaska circulation; Jarvis book
borrow-restricted; WP041/042 date still undatable — circa-1993 stands). Queue +
backlog ledgers updated. E1 (1958 USDA): mason-gaffney chronology gains the
earliest-land-policy-item line (explicitly distinguished from the earlier 1957
Faustmann monograph — different question); land-monopoly 1961 attribution
CORRECTLY LEFT UNTOUCHED (mechanism-presence verdict: E1 has land-boom/financial-
power material but NOT the self-reinforcing credit loop); land-booms page gains a
one-line historical-precursor note with the general-vs-CCA-mechanism distinction
explicit. No E1 page (morning decline respected). Registry +2 rows (Clawson, E1).
VERIFY warnings 31→28, exactly the 3 resolutions. 875 pages, lint 0 errors.

## 2026-07-18 (cont.) — Wave: Gaffney burn-down (water-rents gap filled; E13/E15 skimmed; K1 stale checkbox)

research/gaffney-water-rent-taxation.md created (876th page) — H3 "Diseconomies
Inherent in Western Water Laws" (1961, Kaweah case study: 10x+ marginal-value
dispersion between adjacent users under doctrine-not-price allocation;
price-umbrella/racing/logrolling overexpansion cycle; poor legacy scan re-OCR'd
at 250dpi recovering +28% words, residual [VERIFY] kept) + H21 "The Taxable
Surplus in Water Resources" (1992, six-fallacy case for withdrawal taxation;
$20/$240/$2000 per-acre-foot dispersion; Gaffney's own "books are cooked"
concession preserved). WATER was a total wiki gap despite being named in
resource-rents' own definition — now a section there + Eighth Mode on
resource-rent-capture-works. Priority note: H3 (Jan 1961) predates C4 (Oct 1961)
as earliest academic conference paper but does NOT contain the credit mechanism —
C4's land-monopoly attribution unaffected, documented on-page. E13 (1976 WAEA):
declined a page (overlaps 5 mined works) but its exclusionary-zoning fiscal
diagnosis ("federal grants to governments are grants to landowners") filled a
real gap on concepts/nimbyism.md. E15 (Heilbrun review, ~2pp): zero-addition,
no registry row. K1 stale triage checkbox fixed (already covered by
neoclassical-stratagem page). Registry +3 rows; triage updated; inventory
regenerated. 876 pages, lint 0 errors.

## 2026-07-18 (cont.) — Wave: Gaffney H-series completion (6 folds, 1 decline — water lane CLOSED)

All 9 H-series triage rows now checked. Best catch: H4 (JFE 1962) — recovered via
%26 fetch from a 404-stub mirror — is Gaffney's published reply to Dean Trelease's
critique of the Kaweah study: genuine third-party scholarly pushback the water
page previously said DIDN'T EXIST; Standing-and-Limits corrected accordingly (the
right direction: the page got MORE contested, not less). H8 (AJES 1969): nine-
criterion doctrine comparison + primary-source Wright Act economics, upgrading
california-irrigation-districts from secondary-only sourcing. H22 (AJES 1997):
heavy fold — WTP/WTA entitlement economics incl. treaty-rights example, named
1990s permit speculators, avoided-cost traced to George's Science of Political
Economy. H19's 4pp market design folded despite length (the "how" H21/H22 lack).
H18 light fold (pre-1986 expensing driver + Compact/revolving-fund details).
H20 partial (Chinatown Syndrome/Owens 1913; Irvine vs Wright district voting).
H5 DECLINED on garbled-OCR skim with the limit stated (a clean re-OCR could
theoretically surface something). No second water page — none cleared the
distinct-topic bar. Registry +6 rows (none for H5); 6 text mirrors. 876 pages,
lint 0 errors.

## 2026-07-18 (cont.) — Wave: Gaffney K-series (3 mined, 2 declined, 1 reconciliation)

K9 (Stabile AJES 1995 + Gaffney comment): Clark's 1886 "as conclusive as anything
in mathematics" praise of George's wage theory — a quote the wiki lacked,
predating its 1899 material; Wicksteed-not-Clark priority argument for marginal
productivity (Wicksteed's 1894 title paraphrasing George's chapter title); folded
into marginal-productivity, john-bates-clark, philip-wicksteed with Gaffney's
U-Boat motive-claim carried as attributed D-claim against Missemer-Pottier per
the C9 convention. K2008 (Keeping Land in Capital Theory): mid-wave discovery
that it was ALREADY quoted unregistered (and issue-miscited) on the timber page —
reconciled; Clark/Knight-vs-Austrians feud + three Wicksell contributions folded.
K17 (Wallace's land-nationalization campaign): compensation-annuity mechanics,
Mill's LTRA recruiting Wallace, Asquith's "Tax or Buy" — folded into the existing
wallace page + mill cross-link. K18/K2012 DECLINED (religious/political history
better-sourced on edward-mcglynn from primary correspondence). All three mined
works re-OCR'd (garbled/empty embedded layers). CSV-quoting bug in a comma-
bearing registry title caught pre-lint. K-series now fully checked. Registry +3
rows. 876 pages, lint 0 errors.

## 2026-07-18 (cont.) — Wave: Gaffney F/G series (21 rows verdicted; F7+G17 mined)

F-series CLOSED (3 rows): F7 "Nonpoint Pollution" (JBA 1988/89, re-OCR'd) → new
page (877th): seven failure modes of effluent-charge/surrogate toolkits for
diffuse pollution traced to land-market failure; FIRST Gaffney-specific source on
pigouvian-taxation; wired to ecological-georgism + 3 sibling gaffney pages.
Venue known only as "JBA" from the printed header — [VERIFY] on page AND registry.
F2Q declined (discussant wit, duplicative); F8 = same article, worse scan.
G-series: G17 "The Property Tax Is A Progressive Tax" (NTA 1971, re-OCR'd) → new
page (878th): four-part regressivity rebuttal reached independently of
Mieszkowski 1972 via disjoint premises — new section on the mieszkowski page
distinguishing the two; Table 1 concentration figures carried as Gaffney's
reported (some marked "preliminary" in his own original); landlords-benefit page
gets See Also ONLY (kept out of supported_by). 16 G rows declined on skims with
per-row reasons; G21 exposed as a DEAD FILE (scan mismatch — endnotes of an
unrelated book); G2009 (84pp, unOCR'd) and G45 (Gaffney-Noyes, richest remaining
G candidate) flagged as FUTURE candidates rather than confidently declined —
honest incompleteness recorded. No ampersand stubs this wave. Registry +2 rows;
all 21 triage boxes flipped; inventory regenerated. 878 pages, lint 0 errors.

## 2026-07-18 (cont.) — Wave: G45 + G2009 follow-ups (both resolved)

G45 (Gaffney & Noyes) → research/gaffney-noyes-income-stimulating-property-tax.md
(879th page) — identified as Losses of Nations ch. 8 (1998, pagination-continuous
with the covered ch. 7). CA/NH claim verdict: REAL argued comparison (50-state
1992 ACIR data) but unweighted top/bottom-ten means, no controls, disconfirming
states (HI/AK/MD/NV) explained away ad hoc, and Noyes's NH home-state proximity
disclosed as a limit — wired to taxing-land-raises-productivity as attributed
context, EXPLICITLY out of supported_by; didn't fit the flagged split-rate lane
(measures overall reliance, not land/buildings split) — recorded. Appendix
deltas: 1990s spectrum-concentration data → spectrum-auctions ([VERIFY] on the
business-press figures); 23-point falsified-land-values taxonomy → resource-rents.
G2009: 84pp OCR'd (~47k words) — turns out to be the PEER-REVIEWED PUBLISHED
version (IJSE 36(4) 2009) of the already-covered hidden-taxable-capacity paper,
NOT an expansion: page upgraded (full 16-element enumeration, journal citation,
Krugman-rebuttal + Sinai-Gyourko data points), registry Medium→Heavy. Table-cell
OCR misalignment in G45's source flagged; prose summaries relied on instead.
Registry +1 new row +1 upgrade; triage narrative added; inventory regenerated.
879 pages, lint 0 errors.

## 2026-07-18 (cont.) — Wave: Gaffney I/L/N/O/Z singles (3 pages; publications series ~complete)

16 rows verdicted. MINED: (1) I2015 "Real-Assets Model / Will China Crash in
2015?" (AJES 74(2), peer-reviewed) → research/gaffney-real-assets-model-china.md
(880th): K·T=F turnover mechanism, four land-price→capital-structure channels,
2008 case, the China prediction — upgrades what was a bare citation bullet on
18-year-land-cycle. (2) L2018 Gaffney-Cobb "Corporate Power and Expansive U.S.
Military Policy" (62pp unpublished draft, ~150 sources, largest single work in
corpus) → research/gaffney-corporate-power-military.md (881st): military spending
as rent-seeking — genuinely NEW wiki territory (cacique typology,
Mossadegh/Arbenz/Allende/F-35 cases); unpublished-draft status + motive-framing
conventions applied; rent-seeking-drags-growth gains a historical-illustration
subsection NOT added to supported_by. (3) L2 (1988) precursor given a short
priority page (882nd). DECLINED with reasons: 11 rows incl. I1 (68pp full-
employment work — declined on two-pick budget NOT merit, flagged strong future
candidate), I2012 (future 18-year-cycle addition), I6/I6A verbatim dupes, O12
incomplete draft, Z1 OCR-garbled tables. K9 checkbox reconciled (mined earlier,
never flipped). 3 more ampersand 404 stubs recovered + CACHE REPAIRED for future
sessions. Registry: I2015 Light→Heavy + 2 new rows. Remaining unchecked tail: 95
rows — 73 workpapers + essays dir + 5 stray publications (C2, E4, E5, E7, E9).
Inventory regenerated. 882 pages, lint 0 errors.

## 2026-07-18 (cont.) — Wave: I1 full-employment READ&MINE + I2012 fold + I16 decline

I1 "Toward Full Employment with Limited Land and Capital" (Lynn ed., Property
Taxes, Land Use and Public Policy, U. Wisconsin Press 1976, pp. 99-166 —
provenance confirmed from the running head, NOT the Lindholm volume) → research/
gaffney-full-employment-limited-land.md (883rd page): the Great Revolving Fund
K·T=F model with full worked derivations — the mathematical machinery the 2015
China paper USES WITHOUT DERIVING (priority note added there); dR/dn = i(R+S)
(higher land rent shortens optimal capital-recovery cycles — the paper's most
policy-relevant original result); monuments/frontiers/war capital-sink taxonomy
(distinct from WP041/042's five-fold micro version); the neo-Georgist/Keynesian
"benefits to capital are benefits to labor" critique. Appendices are derivations
from assumed parameters, not data fits — flagged. I2012 folded into
18-year-land-cycle: peace-dividend overlay, the 1990-2008 "perfect cycle" claim,
and Gaffney's own 2012 forecast of a crash "in about 2026" — carried as an OPEN
dated forecast, deliberately unadjudicated (today sits inside the window; no
evidence sought either way). I16 skim-confirmed as I1-minus (identical tables/
epigraph), declined without registry row. Registry +2 rows (I1 Heavy, I2012
Heavy). I11 surfaced as a related precursor — left flagged for a future
capital-theory cluster, not chased mid-wave. Inventory regenerated. 883 pages,
lint 0 errors.

## 2026-07-18 (cont.) — Wave: workpapers/essays skim-triage — GAFFNEY CORPUS TRIAGE COMPLETE

95 remaining rows verdicted (65 workpapers + 25 essays + 5 stray publications) →
FINAL UNCHECKED COUNT: 0. The 190-file triage that began 2026-07-16 is closed.
Breakdown: ~26 duplicates (byte-identical files, WP mirrors of covered AJES
essays, an E9 double-listing), ~45 declines (incl. a Bill Gates Sr. op-ed
mis-hosted under Gaffney's name, book reviews, bare tables, Groundswell columns),
~23 ranked future candidates recorded in the triage narrative (top: WP048/049
Peace Dividends pair; Cleveland/Chicago/Michigan city-growth cluster; WP077
Johannesburg/Cape Town; Great_Expectations bidding-power model; 1972 military-
spending piece as a priority correction for the corporate-power pages). Bonus
mine: E4 "Tax Reform to Release Land" (RFF 1972/73, 39pp) → research/
gaffney-tax-reform-release-land.md (884th page): local governments as collective
landowners practicing fiscal Mercantilism + three formal models (bidding-power,
ripening-date, differential-capitalization) not in closed form anywhere else in
the corpus — priority correction into nimbyism, third independent derivation into
land-monopoly, context into lvt-dampens-land-speculation. Registry +1; inventory
regenerated. 884 pages, lint 0 errors. Gaffney lane state: 38+ works read in
full, ~23 ranked candidates queued, triage ledger authoritative.

## 2026-07-18 (cont.) — Wave: Peace Dividends pair + 1972 military-spending priority

research/gaffney-peace-dividends-land-booms.md created (885th page) from WP048
(1991, King's College IU meetings — 4pp) + WP049 (2005 teaching module — 7pp,
course-outline provenance flagged): the peace-dividend overlay cycle in full —
PRIORITY CORRECTION on 18-year-land-cycle, which had credited the thesis solely
to the 2012 AFEE lecture (WP048 predates by 21 years, incl. the missing-1912-slump
and WWII-interruption analyses; WP049's seven-century sweep uses Levasseur
1892-93, cited nowhere else on the wiki). Bonus wiring: objections/cycles-are-
credit-not-land gains the boundary-condition point that pre-modern-banking-era
land booms sit outside the credit school's 1870-onward evidence base. Gaffney's
own "evidence needed" hedges preserved; no statistical test claimed. The 1972
"Benefits of Military Spending" (TRED, 53pp) proved MORE significant than its
#5 ranking: the true earliest caciques/military-rent-seeking source (16 years
before the 1988 summary, 46 before Gaffney-Cobb), already containing the
Guatemala/Iran cases — priority notes added to both military pages per the
no-re-derivation pattern; read ~20% + structure (Sections D-G surveyed only,
redundant with existing coverage — recorded, not hidden). Registry +3 rows;
triage annotations resolved; inventory regenerated. 885 pages, lint 0 errors.
