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
   ecological-rent ← barnes-who-owns-the-sky + song-zenou-property-tax-sprawl;
   the-corruption-of-economics ← blaug-henry-george-rebel (the anti-Gaffney counter-source);
   the-great-land-robbery ← fairlie-enclosure-history (with Clark & Clark 2001 revisionist
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
