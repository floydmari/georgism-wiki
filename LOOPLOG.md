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
