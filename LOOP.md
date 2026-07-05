# LOOP.md — The Wiki Improvement Loop (model-agnostic)

This file is the executable prompt for one improvement iteration. Any capable model can run it
with only repo access + web search. Read `EDITORIAL.md` (the rules) before your first iteration.

**Visual map:** `docs/loop-diagram.md` (Mermaid; renders on GitHub) shows the iteration
pipeline, the growth flywheel, the agent lanes, and the honesty machinery. **Sync rule:** any
change to this file's structure (steps, gates, lanes, roles) updates the diagram in the same
commit.

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

**GLM AS T2/T3 EXECUTOR (2026-07-04; ENVIRONMENT-CONDITIONAL).** Applies only where a local
ollama/GLM endpoint exists (Floyd's machine, Hermes). The cloud campaign container has none —
there, T2/T3 volume runs on Claude subagents within the concurrency cap, and this section is
inert. Original text: volume drafting runs on glm-5.2:cloud via
`scripts/glm_draft_worker.py` (tasks.json in, drafts + report JSONL out, 6+ parallel workers,
zero Claude session quota): it fetches sources locally (HTML/pdftotext — local egress works),
loads the FULL corpus digest + template + exemplar into GLM's 1M window, and drafts with the
never-fabricate rules baked in. The stub/backfill/cohesion equivalents are
`scripts/comprehensiveness_sweep_glm.py` and `scripts/cohesion_audit_glm.py`. Parallelize at the
GLM layer, not the Claude layer. Claude subagents (<=3-4 concurrent, per Guardrails) are reserved
for what GLM cannot do: open-web verification/forage tasks ("agent verifies best cite"), and
judgment-heavy T1 work. EVERY GLM draft gets the stricter T1 review before commit: grounding
check (numbers/quotes vs supplied material), link/format check, honesty-of-wiring check.

**External models as T2/T3 (original rationale):** tiers are roles, not models. A non-Claude
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
   **Inbox sweep (added 2026-07-05):** if `sources/inbox/` holds unconsumed deliveries from
   Floyd's Hermes agent, process them FIRST per `sources/inbox/README.md` — verify manifests,
   apply verdicts to the flagged markers, upgrade scan depths, queue [DEEPEN-SCAN]s for
   delivered books, archive to `sources/inbox/consumed/`, regenerate the verification queue.
   Delivered evidence outranks new drafting: it un-blocks pages already shipped.
2. **Pick one task.** Take the top task whose `tier:` matches yours and whose `status:` is:
   - `todo` if you are a DRAFT-loop runner (T2/T3), or
   - `needs-review` if you are the REVIEW-loop runner (T1).
   Set it to `status:in-progress` in `BACKLOG.md`.
3. **Do the work — per `EDITORIAL.md`.** Web-research first; cite every substantive claim at
   **People pages (standing rule, Floyd 2026-07-06):** every `people/` page CREATION or BACKFILL
   starts with an Exa enrichment pass — `python3 scripts/exa_enrich.py "<Name>"` (key:
   `EXA_API_KEY` env var; report-only, T1 verifies and cites what it finds). An enrichment
   sweep over ALL existing people pages is queued in BACKLOG. If api.exa.ai is unreachable
   (current egress proxy blocks it), fall back to WebSearch corroboration and leave the
   page's enrichment flag in the queue.
   claim level; classify claims A–F; match language to evidence; never fabricate (use
   `[CITATION NEEDED]` / `[VERIFY]`). New empirical claim ⇒ ensure a `research/` entry exists.
   Create no new orphans (wire ≥2 inbound links). Add every source you use to
   `sources/registry.csv` (Title, Category, Author(s), Status, Wiki Page, Scan Depth,
   In-Wiki Citations, Year, Tier, Format, URL). **When a source's wiki page ships, flip its
   registry row to Status=Scanned and fill Wiki Page in the same iteration** — a page without
   its registry row updated is an incomplete task.
   **Registry mirror (MANDATORY — repo-only, Floyd 2026-07-06):** any iteration that changes
   `sources/registry.csv` must, before finishing, run
   `python3 scripts/export_registry_for_sheet.py` and **commit the dated export to
   `sources/exports/registry-export-YYYY-MM-DD.csv`** — the definitive, GitHub-viewable
   snapshot of all ingested sources (GitHub renders CSVs as sortable tables). Google
   Drive/Sheet snapshots are DE-SCOPED — do not push Drive exports or file [SHEET-SYNC]
   tasks; the repo export is the registry of record.
4. **`[CITE]` tasks** additionally produce the A–E report (revised text · Sources · still-needs-
   citation · softened claims · stronger sources to find) in `reports/<slug>.cite.md`.
5. **Self-review** against `QUALITY_RUBRIC.md`. T1 adds the adversarial pass: *"what would a
   skeptical economist dispute, and does each claim's wording match its source's strength?"*
   T1 review additionally gates on two structural rules (Floyd, 2026-07-05):
   - **Body-parity:** every slug wired in an outcome's `supported_by`/`challenged_by` must be
     discussed or linked in the page body — the frontmatter feeds the COVERAGE gauge, so a
     body that doesn't walk through its own evidence silently overstates the page.
     `lint_wiki.py` now emits `BODY-PARITY` warnings; a reviewed page ships with zero.
   - **Synthesis de-referencing:** if a page's evidence leans on a synthesis (Doucet's ACX
     series, review articles, compendia), queue ingestion of the primary papers it cites and
     demote the synthesis to navigation. A synthesis may introduce evidence; it may not BE the
     evidence.
6. **Lint until clean.** Re-run `lint_wiki.py`; resolve errors. Warnings should trend down.
   If your work added or resolved any `[CITATION NEEDED]`/`[VERIFY]` marker, regenerate the
   worked queue: `python3 scripts/verification_queue.py` (→ `sources/verification-queue.md`,
   grouped by unblock channel). Markers are debt, the queue is the ledger; the count is a
   per-wave trend-down metric alongside warnings.
   **Debt ratchet (added 2026-07-06 after the first-principles review):** a wave may not end
   with more warnings+markers than it started unless the excess is (a) new pages' honest
   conservative flags AND (b) matched by an explicit routing — a queued Hermes-lane task for
   channel-blocked debt, or a BACKLOG debt-paydown task for mechanical debt (unannotated
   Sources, missing excerpts, banned-certainty words, thin articles). Debt that is structurally
   unpayable from this container (proxy-blocked fetches) is Hermes's queue, not a standing
   guilt pile here — route it, don't carry it.
7. **Preview.** Run `python3 scripts/build_preview.py`. Confirm the changed pages render and
   cross-links resolve. (Serve locally with `python3 -m http.server -d preview 8000`.)
8. **Harvest discoveries → create stubs.** Triage the generator's DISCOVERED candidates (all
   categories). For each ACCEPTED candidate, immediately create a **stub** per EDITORIAL.md's
   stub standard (`stub: true`, sourced 2-4 sentence definition, >=2 links out, >=1 inbound link,
   cited Sources) and add it to BACKLOG's Stub queue; reject the rest with a one-line reason.
   Ingestion must grow breadth, not only depth — a wave that adds 8 research pages and 0
   candidates is a smell. Stubs make discovery *visible on the wiki itself* (tagged `stub` on
   Ghost, counted in lint's STUBS gauge).
   **Accept bar + quota (added 2026-07-06):** discovery now outruns triage (one book scan can
   surface 40+ candidates), so acceptance is demand-driven: a candidate needs **≥2 existing
   pages that would naturally link to it** or direct evidence value for an outcome/objection.
   Cap stub creation at **~8 per wave** so backfill keeps pace with intake; park the remainder
   in the report (reports are the parking lot — only accepted candidates enter the wiki).
9. **Update `BACKLOG.md`.** Mark the task `done` (T1 REVIEW loop) or `needs-review` (T2/T3 DRAFT
   loop). Append any follow-up tasks you discovered, tier-tagged.
10. **Commit & push (GitHub is the master record).** One task per commit:
   `content: <what> (<TYPE> tier:T<n>)`. Push to the working branch. **Open/refresh a PR** for
   DRAFT-loop work (cheap output must not auto-publish).
11. **Publish — NOT the loop's job (Floyd, 2026-07-05).** Deployment to progress.org is Floyd's
    separate process. The loop's output ends at commit + push + preview artifact. Do not chase
    GHOST_ADMIN_KEY / 1Password; `scripts/sync_to_ghost.py` stays in the repo for Floyd's use.

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
