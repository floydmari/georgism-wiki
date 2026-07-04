# LOOP.md — The Wiki Improvement Loop (model-agnostic)

This file is the executable prompt for one improvement iteration. Any capable model can run it
with only repo access + web search. Read `EDITORIAL.md` (the rules) before your first iteration.

## Your tier

Each `BACKLOG.md` task is tagged `tier:T1|T2|T3`. Only pick tasks matching your capability:

- **T1 FRONTIER** (Fable 5 preferred; Opus 4.8 or any frontier model as stand-in) —
  judgment work: `[DESIGN]`, `[JUDGE]`, `[REVIEW]`, `[AUDIT]`, flagship articles, and the
  `[CITE tier:T1]` strength-calibration pass. **T1 is the publish gate.**
- **T2 MID** (Sonnet) — `[DRAFT]`, `[DEEPEN]`, `[CITE tier:T2]`: author articles and draft
  citations against vetted sources and templates.
- **T3 BULK** (Gemini Flash / Haiku) — `[BULK]`, `[RECONCILE]`: scan sources, wire cross-links,
  backfill frontmatter, maintain the registry, run/fix lint.

If you are unsure whether a task needs T1 judgment, leave it for T1.

**External models as T2/T3 (e.g. ollama-cloud GLM):** tiers are roles, not models. A non-Claude
model runs a drafting task via `scripts/llm_worker.py` (env: `LLM_API_KEY`, `LLM_BASE_URL`,
`LLM_MODEL`). Because such models have **no web access or lint tools**, the driver forbids them
from citing anything not supplied in the task context (they must use `[CITATION NEEDED]` instead),
and their drafts get a **stricter T1 review**: T1 verifies every citation against the registry/web,
runs lint, and wires links before commit. Cost-tiering guidance: near-free external models are the
default for `[BULK]`, `[DEEPEN-SCAN]` extraction, and first drafts from *supplied* source material;
tasks needing live web research stay on tool-using agents.

## One iteration

1. **Sync & gate.** `git pull`. Run `python3 scripts/lint_wiki.py`. If it reports errors, fixing
   them is your task this iteration (they outrank the backlog).
2. **Pick one task.** Take the top task whose `tier:` matches yours and whose `status:` is:
   - `todo` if you are a DRAFT-loop runner (T2/T3), or
   - `needs-review` if you are the REVIEW-loop runner (T1).
   Set it to `status:in-progress` in `BACKLOG.md`.
3. **Do the work — per `EDITORIAL.md`.** Web-research first; cite every substantive claim at
   claim level; classify claims A–F; match language to evidence; never fabricate (use
   `[CITATION NEEDED]` / `[VERIFY]`). New empirical claim ⇒ ensure a `research/` entry exists.
   Create no new orphans (wire ≥2 inbound links). Add every source you use to
   `sources/registry.csv` (Title, Category, Author(s), Status, Wiki Page, Scan Depth,
   In-Wiki Citations, Year, Tier, Format, URL). **When a source's wiki page ships, flip its
   registry row to Status=Scanned and fill Wiki Page in the same iteration** — a page without
   its registry row updated is an incomplete task.
   **Sheet mirror (MANDATORY, never silent):** any iteration that changes `sources/registry.csv`
   must, before finishing: run `python3 scripts/export_registry_for_sheet.py` and EITHER
   (a) push the export to Floyd's Google Drive as a dated snapshot spreadsheet (via available
   Drive/Sheets tooling), OR (b) if no Drive access, append a loud
   `- [ ] [SHEET-SYNC] tier:T3 status:todo — push registry export to the master Google Sheet
   (last synced: <date>)` line to `BACKLOG.md`. A log line saying "sync pending" is NOT
   sufficient — the staleness must be visible in the backlog Floyd reads.
4. **`[CITE]` tasks** additionally produce the A–E report (revised text · Sources · still-needs-
   citation · softened claims · stronger sources to find) in `reports/<slug>.cite.md`.
5. **Self-review** against `QUALITY_RUBRIC.md`. T1 adds the adversarial pass: *"what would a
   skeptical economist dispute, and does each claim's wording match its source's strength?"*
6. **Lint until clean.** Re-run `lint_wiki.py`; resolve errors. Warnings should trend down.
7. **Preview.** Run `python3 scripts/build_preview.py`. Confirm the changed pages render and
   cross-links resolve. (Serve locally with `python3 -m http.server -d preview 8000`.)
8. **Harvest discoveries → create stubs.** Triage the generator's DISCOVERED candidates (all
   categories). For each ACCEPTED candidate, immediately create a **stub** per EDITORIAL.md's
   stub standard (`stub: true`, sourced 2-4 sentence definition, >=2 links out, >=1 inbound link,
   cited Sources) and add it to BACKLOG's Stub queue; reject the rest with a one-line reason.
   Ingestion must grow breadth, not only depth — a wave that adds 8 research pages and 0
   candidates is a smell. Stubs make discovery *visible on the wiki itself* (tagged `stub` on
   Ghost, counted in lint's STUBS gauge).
9. **Update `BACKLOG.md`.** Mark the task `done` (T1 REVIEW loop) or `needs-review` (T2/T3 DRAFT
   loop). Append any follow-up tasks you discovered, tier-tagged.
10. **Commit & push (GitHub is the master record).** One task per commit:
   `content: <what> (<TYPE> tier:T<n>)`. Push to the working branch. **Open/refresh a PR** for
   DRAFT-loop work (cheap output must not auto-publish).
11. **Publish — REVIEW loop only.** After T1 approval + merge, if `GHOST_ADMIN_KEY` is set:
    `python3 scripts/sync_to_ghost.py <changed files>`. Otherwise log `publish pending`.

## The growth flywheel

The loop is not a straight pipeline; it is a cycle that feeds itself:

**INGEST** sources (research pages) → **EXTRACT** claims into existing pages → **DISCOVER**
warranted new topics in every category → **STUB** them immediately (visible, sourced, tracked) →
**PRIORITIZE** (`[PRIORITIZE] tier:T1`: rank the stub queue by inbound-link demand, evidence
already present in the ingested corpus, and citing-source tier) → **BACKFILL** the top stubs via
`tasks/backfill-page-task.md`, whose first step **re-mines the existing corpus** (earlier pages
were written before the stub existed, so their sources were never extracted for it) → backfilled
pages cite new sources and surface new candidates → next INGEST. Each turn of the wheel makes
every earlier ingest more valuable. `[SYNTHESIS]` (below) is the same motion at the set level.

## Loop roles

- **DRAFT loop** (T2/T3): steps 1–10, ending at `needs-review` + PR. Never publishes.
- **REVIEW loop** (T1): pulls `needs-review` items, applies judgment, approves, merges, and is the
  only loop that runs step 11. Also runs T1-native `[DESIGN]/[JUDGE]/[AUDIT]` tasks.
- Every ~10 research pages ingested, run a **`[SYNTHESIS] tier:T1`** pass: reread the recent
  ingests as a set and ask what they collectively justify — a claim with enough evidence for a
  new OUTCOME page, a recurring mechanism deserving a CONCEPT page, a recurring counterargument
  deserving an OBJECTION page (steelmanned), a persuasive pattern deserving a NARRATIVE. Create
  or queue them. This is the bottom-up growth channel; the curated lists are top-down only.
- Every ~10th REVIEW iteration, run an **`[AUDIT]`**: rubric-score 8 random articles, refresh and
  reprioritize `BACKLOG.md`, staleness sweep (`last_reviewed`, dead links), and re-check
  registry↔repo↔sheet consistency (`lint_wiki.py` surfaces drift).

## Related loops

`LOOP-COMPREHENSIVENESS.md` — the source-comprehensiveness audit (re-mine all registry sources for
missed stubs in every category + the authors channel). Invoked separately, after major ingest
campaigns; never run concurrently with a drafting wave.

## Guardrails
- **Concurrency cap:** never run more than 3–4 concurrent Claude subagents — Claude session
  limits are the binding constraint (13 concurrent scanners burned a full quota on 2026-07-04).
  Volume scan/extract work goes to the near-free external-model path first (`scripts/llm_worker.py`,
  `scripts/comprehensiveness_sweep_glm.py` — GLM via local ollama, zero session quota).
- GitHub first, Ghost second, always via `scripts/sync_to_ghost.py`.
- Never delete an article; never fabricate a citation; ≤50 words quoted; free/legal sources.
- One task per iteration keeps commits reviewable and the preview diff legible.
