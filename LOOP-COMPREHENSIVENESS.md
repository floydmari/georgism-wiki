# LOOP-COMPREHENSIVENESS.md — The Source-Comprehensiveness Loop (invokable, not part of the main loop)

This is a **separate, periodically-invoked audit loop**, distinct from the main expansion loop in
`LOOP.md`. The main loop grows the wiki forward (ingest → extract → discover → stub → backfill).
This loop looks **backward at the sources themselves**: every source in `sources/registry.csv` was
originally mined for a specific purpose (usually one research page wired to one outcome), and
nothing guarantees it was mined for everything else the wiki synthesizes — the people it discusses,
the places and events it documents, the concepts it formalizes, the objections it steelmans, the
narrative patterns it deploys. This loop closes that gap so the wiki is **cohesive with respect to
its own source corpus**: a reader following any source should find every wiki-worthy thing that
source substantively treats.

**When to invoke:** after any major ingest campaign (roughly every ~50 new registry rows), or on
demand. It is idempotent — each invocation records a watermark in `BACKLOG.md` (registry row count
+ date) and the next invocation sweeps only sources added since, unless a `--full` re-sweep is
requested.

**Unit of scanning:** the SOURCE (registry row), not the wiki page. Wiki pages are consulted only
to determine what has *already* been extracted (a candidate must not already exist as a page or a
queued task).

---

## Phase 0 — Deterministic pre-pass (script, no agents)

Run `python3 scripts/comprehensiveness_prepass.py`. It emits, from `sources/registry.csv` alone:

1. **The sweep list** — all external-source rows (Category not in the wiki-page categories),
   chunked into agent batches (~10–12 sources each), minus rows covered by the last watermark.
2. **The authors channel** — every author aggregated across rows, matched against `people/`;
   flags authors with **≥2 registry sources** or **any Core-tier source** who lack a people page.
   These are *candidates*, not automatic accepts — the people bar (below) is applied at triage.
3. **Under-mined flags** — rows with `Status=Referenced` (cited but never scanned) and rows whose
   `Scan Depth` is below their Tier's target (per EDITORIAL.md §3) — these sources are the likeliest
   to be hiding material.

## Phase 1 — SOURCE-SWEEP (default execution: near-free external model, NOT Claude agents)

**Run `python3 scripts/comprehensiveness_sweep_glm.py`** (background; resumable JSONL output in
`preview/comprehensiveness_sweep_results.jsonl`). It fetches each source document locally (HTML,
or PDF via pdftotext), supplies the source's research page as already-extracted orientation, and
has GLM on Ollama Cloud enumerate candidates — **zero Claude session quota**. Per LOOP.md's
external-model rule its output gets a stricter T1 review: every candidate is verified at triage
before any stub is written, and fetch-failed sources are marked confidence=low by construction.
Claude subagents are the FALLBACK only (when ollama is unavailable), and then capped at 3–4
concurrent — session limits are the binding constraint, learned 2026-07-04 when 13 concurrent
Sonnet scanners exhausted the quota before reporting.

### Fallback agent spec (only if the script path is unavailable): report-only T2/T3 agents, ~10–12 sources per agent

Each scan agent receives its batch of registry rows (Title, Authors, Year, Tier, URL, Wiki Page)
and, for each source:

1. **Orient:** if the source has a dedicated `research/` page, skim it to learn what was already
   extracted (orientation only — the page is not the scan target).
2. **Access the source:** fetch the URL / an archive copy where the egress proxy allows; otherwise
   corroborate via multiple agreeing web references *about* the source. Never fabricate content.
3. **Enumerate** everything the source substantively treats, across all 8 categories (concepts,
   people, places, organizations, objections, events, outcomes, narratives). "Substantively" =
   a section, a recurring argument, a documented case — not a passing name-drop.
4. **Filter** against existing pages (`ls` the category dirs; treat synonym slugs as existing) and
   against `BACKLOG.md` (queued items don't count as discoveries).
5. **Report only** — no file edits, no git. Return:
   - `DISCOVERED:` list (max ~8, ranked): `slug | category | rationale | citation (source + chapter/page where known)`
   - `AUTHORS-CHANNEL:` authors in this batch meeting the people bar (see below) with their contributions
   - `UNDER-MINED:` sources in the batch whose extractable value clearly exceeds what the wiki holds
     (candidates for `[DEEPEN-SCAN]`)
   - `REJECTED-NEAR-MISSES:` with one-line reasons

**The people bar** (applied in Phase 2, advertised to scanners): a person gets a page when they
have (a) **multiple contributions** to the land-economics/Georgist literature over time (≥2 registry
sources, or one Core source plus sustained influence), or (b) substantive discussion *as a subject*
in the corpus. Prolific researchers whose papers anchor multiple outcomes belong in `people/` even
if no wiki page discusses them biographically yet — that is precisely the gap this loop exists to
catch.

## The 1M-context strategy (GLM's window is the asset — fill it where it adds value)

GLM 5.2 on Ollama Cloud has a ~1M-token context window (verified: ~275k-char needle test passes
in ~20s). Use it deliberately:

1. **Light pass (default sweep):** papers get ~45k chars of document text — most papers fit whole.
2. **Deep pass (`--deep`):** Core-tier and under-mined sources get up to ~900k chars (whole books,
   pdftotext up to 400 pages) PLUS the full wiki corpus digest (title+excerpt of every page), so
   dedupe happens against real content, not slug names. Output goes to
   `preview/comprehensiveness_sweep_deep.jsonl`. This doubles as the Heavy-scan upgrade the
   registry's Scan Depth policy wants for books.
3. **Whole-corpus cohesion audit (`scripts/cohesion_audit_glm.py`):** the ENTIRE wiki (~1.5M chars
   ≈ 350k tokens) in ONE call → contradictions, duplications, missing cross-links, terminology
   drift, stale/inconsistent facts, corpus-scale gaps. Run it as **Phase 3.5** each invocation,
   after stubs are created; its findings feed T1 fix-ups and the main loop's queues.
4. **Corpus-aware drafting (Phase 3):** when backfilling a stub, a single GLM call can hold the
   full text of the discovering sources + every related wiki page — draft with total context,
   then T1 review. Prefer this over web-searching Claude agents whenever the material is already
   in the corpus.

## Phase 2 — T1 triage → stubs

T1 dedupes across all chunk reports (and against the wiki + BACKLOG), accepts/rejects each
candidate **with a recorded reason**, then fans out stub-writer agents (disjoint file ownership)
to create every accepted candidate per EDITORIAL.md §6's stub standard: `stub: true`, 2–4 sourced
sentences, ≥2 links out, ≥1 inbound link wired **from the discovering source's research page**
(that is the natural inbound edge for this loop), annotated Sources citing the discovering
source(s). Registry rows for any new external sources are reported to the orchestrator and applied
centrally. Rejections are appended to the BACKLOG stub queue's rejected list so future sweeps skip
them.

## Phase 3 — Content development from the existing corpus

Once stubs exist, a second agent wave fills them **from the already-scanned corpus first** —
`tasks/backfill-page-task.md` applies, with one override: the re-mine step starts from the
**discovering sources identified in Phase 1** (read those documents/notes again *for this topic*),
then the wiki corpus, and only then new web research. Prioritize (T1 judgment): people with the
largest citation footprint in the corpus, then stubs demanded by multiple sources, then the rest.
Not every stub must be backfilled in the same invocation — unfilled stubs stay honest scaffolding
in the STUBS gauge and the queue.

## Phase 4 — Wrap-up (same obligations as the main loop)

Registry flips in-iteration → Google Sheet snapshot (mandatory-loud rule, LOOP.md step 3) →
`LOOPLOG.md` entry labelled **[COMPREHENSIVENESS]** → preview rebuild + artifact redeploy → commit
per reviewed batch, push, PR. Finally, **write the new watermark** into the BACKLOG section
"Comprehensiveness loop" (registry row count + date + commit), so the next invocation knows where
to start.

## Guardrails

- Everything in EDITORIAL.md applies unchanged (never fabricate; stub standard; claim-level cites).
- Scanners are strictly report-only; stub writers own disjoint file sets; only the orchestrator
  touches `sources/registry.csv` and `BACKLOG.md`.
- This loop creates breadth, not depth — resist upgrading it into a rewrite pass. Depth work it
  surfaces goes to the main loop's queues (`[DEEPEN-SCAN]`, `[BACKFILL]`, `[CITE]`).
- Do not run this loop concurrently with a main-loop drafting wave that is creating research pages
  (registry churn makes the sweep list unstable mid-flight).
