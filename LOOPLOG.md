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
  `Scanned` when its page shipped — LOOP.md now states the registry-row flip is part of the same
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

Numbers: 136 sources swept (64 full texts) + 46 deep full-text re-scans at the verified 1M-token
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
  taranu-verbeeck-property-tax-sprawl (systematic review, design-conditional),
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
rule closed pending full-text confirmations.
