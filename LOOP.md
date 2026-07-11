# LOOP.md — How the Georgism Wiki Grows

## The mission

We are building **the definitive, honest reference on Geoism — the capture of economic
rents of every kind for public good** (Floyd's scope expansion, 2026-07-06). Georgism and
the land value tax are the core and the historical root; the full scope runs from land and
resources through carbon, spectrum, road space, monopoly privilege, finance, platforms, and
IP — each rent domain with its own capture instrument and its own evidence base, honestly
graded (see EDITORIAL §0's rent gradient: land is the clean case; the frontier is contested).
"Definitive" means a reader can start from any
question — *does LVT actually get passed on to renters? are platform profits rents? what did
Norway do right?* — and find the strongest available evidence, the strongest
counterargument, and the primary sources, all cited. "Honest" means we never claim more than
the sources support: advocacy is labeled advocacy, contested findings are shown contested,
and anything we couldn't verify says so on the page.

The wiki grows the way a good research desk grows a beat:

- **FIND** the literature — the papers, books, sites, and people that bear on the land
  question, from Ricardo to the FHFA's tract-level land data. The reading list is
  `sources/registry.csv` (what we've found) and `sources/wanted-books.md` (what we're hunting).
- **READ & MINE** each source — write its `research/` or `books/` page, pull out every
  finding, figure, person, event, place, and counterargument it contains. A source isn't
  "done" when summarized; it's done when everything it teaches has somewhere to live.
  **The delta rule (Floyd, 2026-07-06):** when weaving a new source's findings into
  EXISTING pages, read the target page (and the evidence pages it links) first and add
  only what's genuinely new — a sharper number, a missing caveat, a counterargument, a
  primary behind a synthesis. If the wiki already carries the finding somewhere, LINK to
  that home rather than restating it; one finding, one home, many links. (Lesson: the
  Danish natural experiment got restated on three pages in w1 before cross-linking.)
  Public-domain primary texts can be held in full — see EDITORIAL §3b.
- **SYNTHESIZE** what the sources collectively show into the wiki's argument pages:
  `problems/` and `benefits/` (what the evidence supports — e.g. *split-rate taxation increases
  construction*), `objections/` (what critics say, steelmanned — e.g. the homevoter
  problem), `narratives/` (how to tell the story), `concepts/` (how the mechanisms work).
- **VERIFY** relentlessly — every claim we couldn't confirm carries a visible
  `[CITATION NEEDED]` / `[VERIFY]` flag, and the **Fact-Check Desk** (below) works those
  flags down or routes them to whoever can.
- **EXPAND** the map — reading always surfaces topics the wiki should cover (a critic
  worth a bio, an episode like the 1990 Gorbachev letter, a mechanism like ATCOR).
  Warranted ones become stubs immediately; the best-connected stubs get built out.

Everything below is the shift-by-shift procedure for doing that. Read `EDITORIAL.md`
(the editorial constitution) before your first shift. **Visual map:** `docs/loop-diagram.md`
(Mermaid; renders on GitHub). **Sync rule:** any change to this file's structure updates the
diagram in the same commit.

## Who works the desk

Each `BACKLOG.md` task is tagged `tier:T1|T2|T3` — editorial roles, not just model sizes:

- **T1 — the editor** (Fable 5 preferred; any frontier model as stand-in): judgment calls —
  what the evidence collectively justifies, whether a claim's wording matches its source's
  strength, review of everyone else's drafts. `[DESIGN] [JUDGE] [REVIEW] [AUDIT]` tasks and
  flagship pages. **T1 is the only gate to main.**
- **T2 — staff writers** (Sonnet-class): research and draft pages against vetted sources and
  templates. `[DRAFT] [DEEPEN] [CITE tier:T2]`.
- **T3 — the copy desk / librarians** (Haiku-class): scan sources, wire cross-links, maintain
  the registry and reading list, keep lint green. `[BULK] [RECONCILE]`.

If unsure whether a task needs editorial judgment, leave it for T1.

## One shift (an iteration)

1. **Catch up on the desk.** `git pull`; run `python3 scripts/lint_wiki.py`. Lint errors are
   the wiki telling you a page misrepresents itself — fixing them outranks the backlog.
   **Hermes inbox first:** if `sources/inbox/` holds unconsumed deliveries (verified quotes,
   book findings, fact-check verdicts), process them per `sources/inbox/README.md` before
   drafting anything new — delivered evidence un-blocks pages already shipped.
2. **Choose one piece of work** from `BACKLOG.md` matching your tier (`todo` for writers,
   `needs-review` for the editor); set it `in-progress`. One piece per shift keeps the record
   reviewable.
3. **Research and write it — per `EDITORIAL.md`.** Read the sources first; cite every
   substantive claim; match your language to the evidence's strength; never fabricate — an
   unverified fact gets a flag, not a guess. A new empirical claim means its study gets a
   `research/` page. New pages get wired into the wiki (≥2 inbound links — an unlinked page
   teaches no one). Every source you used goes on the reading list (`sources/registry.csv`),
   and when its wiki page ships, its row flips to Scanned in the same shift.
   - **People pages:** every creation or backfill starts with an Exa enrichment pass —
     `python3 scripts/exa_enrich.py "<Name>"` (report-only; the editor verifies and cites
     what it finds). If api.exa.ai is unreachable (current proxy blocks it), fall back to
     WebSearch and leave the page in the BACKLOG enrichment sweep.
   - **Reading-list mirror:** any shift that changes the registry commits the dated export
     (`python3 scripts/export_registry_for_sheet.py` →
     `sources/exports/registry-export-YYYY-MM-DD.csv`). The repo export is the registry of
     record; Drive/Sheet sync is retired.
4. **`[CITE]` fact-checking assignments** additionally file the A–E report (revised text ·
   sources · still-needs-citation · softened claims · stronger sources to find) in
   `reports/<slug>.cite.md`.
5. **Self-review as a skeptical reader** (`QUALITY_RUBRIC.md`). The editor's adversarial
   question: *"what would a skeptical economist dispute, and does each claim's wording match
   its source's strength?"* Two structural checks are part of the editor's review:
   - **Body-parity:** an outcome page must actually walk through the evidence its frontmatter
     claims — a page that lists seven studies and discusses two is overstating itself.
   - **Delta check on enrichments:** additions to an existing page must be genuinely new to
     the wiki's coverage (EDITORIAL §3 delta rule) — restating a finding that already has a
     home elsewhere is drift, not depth; convert restatements to links.
   - **Evidence ordering:** supporting-research lists read strongest-first (EDITORIAL §3
     ordering rule); a reviewed page's `supported_by` and Evidence sections are in
     descending evidential weight.
   - **Synthesis de-referencing:** if a page leans on someone else's literature review
     (Doucet's ACX series, a survey article), queue the primary studies it cites and demote
     the synthesis to navigation. *This wiki works through the literature itself* — a
     synthesis may introduce evidence; it may not BE the evidence.
6. **Run the Fact-Check Desk** (gap-1 machinery, upgraded 2026-07-06). Re-run lint; then
   `python3 scripts/verification_queue.py` — it rebuilds `sources/verification-queue.md`
   (every open fact-check, grouped by who can resolve it) AND `sources/hermes-workorder.md`
   (the ready-to-work order for Hermes's next run). The desk's rules:
   - **Every open flag has an owner.** Proxy-blocked fetches → Hermes's work order.
     Books we don't hold → `wanted-books.md` + Floyd. Owner-only facts (bios, attestations)
     → Floyd's short list. Only genuinely workable-from-here items stay ours.
   - **The campsite rule:** every shift resolves or routes **at least 5 items** of standing
     debt — open fact-checks, unannotated Sources sections, thin pages, banned-certainty
     wording — regardless of what the shift's main work was. New pages may add honest flags;
     the *net* count must not drift upward un-routed (the ratchet).
7. **Preview the wiki as a reader.** `python3 scripts/build_preview.py`; confirm the changed
   pages render and their links resolve.
8. **Grow the map — triage discoveries into stubs.** Reading always surfaces candidate
   topics in every category (people, events, places, concepts, organizations, objections,
   research, books). Accept a candidate only if **≥2 existing pages would naturally link to
   it** or it directly strengthens an outcome/objection; create accepted ones as sourced
   stubs immediately (EDITORIAL stub standard), reject the rest with a one-line reason.
   Before creating ANY stub (people, research, events, all categories), **check for existing
   coverage BOTH ways**: `ls <category>/` for slug variants AND a repo-wide grep for the
   surname / paper-title keywords / author combination — and read the full result list, not
   the first screen. Three same-day lessons (2026-07-06): richard-ely vs richard-t-ely;
   robert-schalkenbach-foundation vs schalkenbach-foundation; tideman-kumhof-… vs
   goodhart-stimulus (same paper, different slug conventions). Slugs lie; grep the words.
   - **Digest before you scan (gap-2 machinery, 2026-07-06):** cap new stubs at **~8 per
     shift**, and **launch no new site/book scans while ≥2 discovery reports sit untriaged**
     in `sources/inbox/`. The wiki grows by *digesting* what it has read — an unread pile of
     candidates is inventory, not coverage. Discovery reports are the parking lot; the
     BACKLOG stub queue is the commitment.
9. **Log the shift in `BACKLOG.md`** — task to `done` (editor) or `needs-review` (writers);
   append follow-ups you discovered, tier-tagged.
10. **File the work.** One task per commit: `content: <what> (<TYPE> tier:T<n>)`; push;
    writers open/refresh a PR (drafts never self-publish).
11. **Publishing is not the loop's job.** Deployment to progress.org is Floyd's separate
    process; the loop ends at commit + push + preview.

## The flywheel (why coverage compounds)

Reading Harrison's 1983 book gave the wiki Australian construction evidence for two outcome
pages, bios-in-waiting for the critics he cites, four books for the wanted list, and the
Japanese land bubble as a historical episode. Each of those, built out, cites new sources —
which get read, which surface more. Formally:

**FIND** sources → **READ & MINE** them (`research/`, `books/` pages) → **SYNTHESIZE** into
the argument pages (`problems/`, `benefits/`, `objections/`, `narratives/`, `concepts/`) → **DISCOVER**
warranted new topics → **STUB** them (visible, sourced) → **PRIORITIZE** by inbound-link
demand (`[PRIORITIZE] tier:T1`) → **BUILD OUT** the top stubs, *re-mining the existing corpus
first* (earlier pages were written before the stub existed) → built-out pages cite new
sources → next **FIND**. Every ~10 sources read, the editor runs a **`[SYNTHESIS]`** pass:
what does the recent reading *collectively* justify — a new outcome? a recurring
counterargument that deserves steelmanning? a narrative pattern? That is the bottom-up
growth channel; curated lists are top-down only.

Every ~10th editor shift, run an **`[AUDIT]`**: rubric-score 8 random pages, refresh
`BACKLOG.md` priorities, staleness sweep, registry↔repo consistency.

## Lanes (who edits what, so agents never collide)

- **Campaign branch** (this repo's `claude/...` branch): new coverage — the editor + writers.
- **Hermes lane** (`hermes/*` branches, Floyd's machine): the Fact-Check Desk's field agent —
  unblocked web + Floyd's private book library. Works `sources/hermes-workorder.md` and book
  scans; files discovery reports; opens PRs; **never merges its own work**. Book files and
  long excerpts never enter the repo; provenance must be legal (no shadow libraries) —
  `sources/inbox/README.md` is its contract.
- Both lanes end at the same place: **T1 editor review, then main.**

## Related loops

`LOOP-COMPREHENSIVENESS.md` — the periodic re-mining audit: go back over every source on the
reading list and ask what the wiki failed to extract the first time (missed stubs, missed
authors). Run after major reading campaigns; never concurrently with a drafting wave.

## Guardrails

- **Concurrency cap:** ≤3–4 concurrent Claude subagents (session limits are the binding
  constraint; 13 concurrent scanners burned a full quota on 2026-07-04).
- Never delete an article; never fabricate a citation; quotes ≤50 words with locators;
  free/legal sources only.
- One task per shift keeps commits reviewable and the preview diff legible.

---

## Execution notes (technical appendix — environment-dependent)

**GLM as T2/T3 executor (2026-07-04; only where a local ollama/GLM endpoint exists — Floyd's
machine, Hermes; the cloud container has none).** Volume drafting via
`scripts/glm_draft_worker.py` (tasks.json in, drafts + report JSONL out, 6+ parallel workers,
zero Claude quota): fetches sources locally, loads the corpus digest + template + exemplar
into GLM's 1M window, drafts with never-fabricate rules baked in. Companions:
`scripts/comprehensiveness_sweep_glm.py`, `scripts/cohesion_audit_glm.py`. Parallelize at the
GLM layer, not the Claude layer.

**External models generally:** tiers are roles, not models. A non-Claude model runs drafting
via `scripts/llm_worker.py` (env: `LLM_API_KEY`, `LLM_BASE_URL`, `LLM_MODEL`). Such models
have no web access or lint tools, so the driver forbids citing anything not supplied in the
task context (`[CITATION NEEDED]` instead), and their drafts get the stricter T1 review:
every citation verified against registry/web, lint run, links wired before commit. Near-free
external models are the default for `[BULK]` extraction and first drafts from supplied
material; live web research stays on tool-using agents.
