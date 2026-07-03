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
   In-Wiki Citations, Year, Tier, Format, URL).
4. **`[CITE]` tasks** additionally produce the A–E report (revised text · Sources · still-needs-
   citation · softened claims · stronger sources to find) in `reports/<slug>.cite.md`.
5. **Self-review** against `QUALITY_RUBRIC.md`. T1 adds the adversarial pass: *"what would a
   skeptical economist dispute, and does each claim's wording match its source's strength?"*
6. **Lint until clean.** Re-run `lint_wiki.py`; resolve errors. Warnings should trend down.
7. **Preview.** Run `python3 scripts/build_preview.py`. Confirm the changed pages render and
   cross-links resolve. (Serve locally with `python3 -m http.server -d preview 8000`.)
8. **Update `BACKLOG.md`.** Mark the task `done` (T1 REVIEW loop) or `needs-review` (T2/T3 DRAFT
   loop). Append any follow-up tasks you discovered, tier-tagged.
9. **Commit & push (GitHub is the master record).** One task per commit:
   `content: <what> (<TYPE> tier:T<n>)`. Push to the working branch. **Open/refresh a PR** for
   DRAFT-loop work (cheap output must not auto-publish).
10. **Publish — REVIEW loop only.** After T1 approval + merge, if `GHOST_ADMIN_KEY` is set:
    `python3 scripts/sync_to_ghost.py <changed files>`. Otherwise log `publish pending`.

## Loop roles

- **DRAFT loop** (T2/T3): steps 1–9, ending at `needs-review` + PR. Never publishes.
- **REVIEW loop** (T1): pulls `needs-review` items, applies judgment, approves, merges, and is the
  only loop that runs step 10. Also runs T1-native `[DESIGN]/[JUDGE]/[AUDIT]` tasks.
- Every ~10th REVIEW iteration, run an **`[AUDIT]`**: rubric-score 8 random articles, refresh and
  reprioritize `BACKLOG.md`, staleness sweep (`last_reviewed`, dead links), and re-check
  registry↔repo↔sheet consistency (`lint_wiki.py` surfaces drift).

## Guardrails
- GitHub first, Ghost second, always via `scripts/sync_to_ghost.py`.
- Never delete an article; never fabricate a citation; ≤50 words quoted; free/legal sources.
- One task per iteration keeps commits reviewable and the preview diff legible.
