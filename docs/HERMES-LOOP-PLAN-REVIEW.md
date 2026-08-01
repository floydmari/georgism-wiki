# Review: "Georgism Wiki Evolution Loop — System Design Plan" (Hugh/Hermes, 2026-07-31)

Reviewed by the T1 editor (Claude Code, Fable), 2026-08-01, at Floyd's request.
Plan source: ubiworks.notion.site page `3afa9ac7ed7381d99c2ef1aea36ee0f8`.

## Verdict

The architecture is sound and most guardrails are correctly inherited. The T0
context-engine idea (GLM 5.2 pre-processing the full corpus into per-item briefs) is a
genuine improvement over the current loop and worth adopting even if nothing else changes.
**But run as written, the plan causes three regressions** — a publishing gap that would
let the live wiki go stale, a silent model-downgrade path for the only quality gate, and a
new-page-shaped pipeline for what is mostly enrichment work. All three are fixable without
changing the plan's architecture. Recommendation: fix the blocking items, then run in
**shadow mode** for 1–2 weeks before cutting over (see Rollout below).

---

## A. Blocking issues (quality or policy loss if run as-is)

### A1. The loop has no publish step — and it reverts the merge protocol

The plan ends at "PRs opened by Hugh against main. Floyd reviews and merges." Two
problems:

1. **This reverts Floyd's 2026-07-31 standing authorization** (LOOPLOG, 2026-07-31):
   the current protocol merges to main at the end of every loop, Ghost-syncs the changed
   pages to progress.org, and spot-checks a live URL. The plan silently reinstates the
   old Floyd-gated flow. That is a policy decision only Floyd can make, and the plan
   doesn't surface it as one.
2. **Ghost sync is absent entirely.** Nothing in the plan pushes approved pages to the
   live site. Merged-but-unsynced pages are invisible to readers; unmerged PRs are worse —
   the scanner's dedup reads main, so a backlog of unmerged cycles degrades Hermes's own
   queue dedup (items re-queued because main doesn't show them consumed).

**Fix (recommended):** split authoring from publishing. Hermes cron authors and opens
PRs; a Claude Code routine remains the T1 gate — reviews with tools (lint, link checks,
live fetches Hugh's API-called judge cannot do), merges under the standing authorization,
runs Ghost sync (`sync_changed.py` pattern, retry-hardened), regenerates the inventory
census, and spot-checks a live URL. This preserves "T1 is the only gate to main"
(LOOP.md) with a tool-equipped judge, and keeps the live site continuously current.
Granting Hermes direct merge + Ghost credentials is a larger trust delta that should wait
for a track record.

### A2. Judge model integrity — no silent fallback on the T1 gate

The cron prompt reads "spawn Fable as judge (via delegate_task with model
`anthropic/claude-opus-4` or the Fable model)". Two defects:

- **The model IDs are stale.** `claude-sonnet-4` and `claude-opus-4` are outdated;
  current IDs are `claude-sonnet-5` (writers) and `claude-fable-5` (judge).
- **"Opus-4 or Fable" is a silent-downgrade path for the only gate to main.** LOOP.md
  defines T1 as "Fable 5 preferred; any frontier model as stand-in" — a stand-in is
  acceptable, but the substitution must be *loud*, not a fallback buried in a cron
  prompt. If the pinned judge model is unavailable, the cycle should park its drafts in
  `preview/glm_drafts/`, report the degradation to Slack, and stop — never approve pages
  through a weaker judge without saying so.

### A3. The pipeline is new-page-shaped; most real queue work is not new pages

Evidence from the consumed ledger (`sources/wiki-queue.json`, 151 dispositioned items):
recent waves are dominated by **folds into existing pages, duplicates, and rejects**.
The 2026-07-31 cycle was 1 fold, 1 duplicate, 1 reject — zero new pages. The plan's
writer → copywriter → judge flow assumes "draft a page." The GLM brief schema *does*
detect deltas (good), but the plan never says what happens next for the majority case:

- **Enrich lane:** when the brief says `fold_into_existing`, the writer must receive the
  full existing page + the source + the delta assessment, and produce a **minimal edit**
  (the current loop does surgical folds — often 2 sentences and a source line). The judge
  must then review the **diff**, not re-review the whole page as if fresh.
- **Consumed-ledger discipline:** every item gets `disposition` +
  `disposition_reason` + `consumed_at` in `wiki-queue.json` (see existing entries for
  format); dispositioned URLs are **never resurrected**; when the scanner pushes to main
  mid-cycle, `wiki-queue.json` is **union-merged** (scanner's new items in, consumed
  ledger preserved). This has already caused a real merge conflict once; the cron prompt
  needs the rule verbatim.

---

## B. Non-blocking fixes (should change before or shortly after launch)

- **B1. Copywriter drift risk.** A polish pass that restructures paragraphs is exactly
  where claims drift from their citations even when no "fact is changed." Mitigations:
  (a) the judge receives the writer-draft→copyedit **diff** alongside the final text;
  (b) skip the copywriter for enrichment edits and stubs (polish only full new pages);
  (c) `lint_wiki.py` banned-certainty checks run **after** the copyedit. Alternative:
  make the pass conditional — only when the judge scores narrative_clarity < 4.
- **B2. Deterministic dedup before GLM.** URL/registry dedup is a grep, not a model call.
  Keep the scripted registry check ahead of the GLM brief (the plan's §10.2 has this —
  make sure it stays a script, with GLM's semantic delta check as the second layer, not
  the only one). Yesterday's Sightline duplicate was caught by an exact-URL grep.
- **B3. The campsite rule is misquoted, and absent from the cron.** LOOP.md's campsite
  rule is "every shift resolves or routes **≥5 items of standing debt**" — not "pick ≤8
  items" (that is the separate gap-2 stub cap, which §10.1 states correctly). The cron
  prompt has **no standing-debt step at all**: regenerating `verification_queue.py`
  files (step 15) routes debt but resolves none. Without a burn-down step the flag count
  ratchets upward — the exact failure LOOP.md's ratchet clause guards against. Add: each
  cycle resolves ≥5 debt items (open VERIFY/CITATION flags, unannotated sources, thin
  pages), especially in the ~3 of 4 daily cycles where the queue is empty (see B5).
- **B4. LOOPLOG.md continuity.** The plan never mentions it. Every cycle must append a
  LOOPLOG entry (dispositions, counts, anomalies, protocol notes) — it is the
  institutional memory that every later session, and Floyd, reads.
- **B5. Cadence vs. scanner.** The scanner feeds the queue once daily (~10:00 UTC); a 6h
  cron means most cycles find an empty queue. Don't waste them: run the post-scan cycle
  (~11:00 UTC) on the queue, and make off-scan cycles do campsite/backlog work instead of
  "report empty and stop."
- **B6. Slack noise.** "Report queue empty every 6h" contradicts the quiet-pass rule the
  current loop runs under (silent when nothing happened). Report when work happened or on
  failure; at most a daily digest otherwise.
- **B7. Missing repo-state steps** for whoever publishes: `build_inventory.py` census
  regen; frontmatter `last_reviewed` updates on enriched pages; related-boxes/interlink
  maintenance for new pages (the precompiled-boxes pipeline); BACKLOG claim stamps
  (LOOP.md "Claiming work") if the Claude Code lane ever runs concurrently with Hermes
  cycles.
- **B8. Stale numbers.** The wiki is 918 pages / 1,378 registry sources as of 2026-08-01
  (plan says 838/1,379 — written before the July queue waves). Context budgets still
  hold; the 1M window fits the digest to roughly 2,500+ pages.

---

## C. Answers to the plan's §12 evaluation questions

1. **Tiering matches?** Yes, with A2's caveat. Adding T0 as a context tier is sound and
   consistent with LOOP.md's precedent of GLM as a non-gating executor whose output gets
   stricter T1 review.
2. **GLM well-scoped?** Yes — context-only is the right call, and §3.5's reasoning is
   correct. Keep deterministic dedup ahead of it (B2).
3. **Writer/copywriter split justified?** Marginal. The accuracy/readability separation
   is principled, but the drift risk (B1) is real and most items don't need polish
   (enrichments, stubs). Make it conditional or diff-audited.
4. **Context budget realistic?** Yes (B8 updates the numbers). And yes — the judge should
   eventually get the full digest directly (the plan's own §13 "full-corpus judge"); Fable
   has the window for it.
5. **Failure handling?** The table is good. Missing: Ghost-sync failures (if adopted per
   A1), `wiki-queue.json` merge conflicts (A3 — a real, recurring event), and mid-cycle
   restart idempotency (drafts in `preview/` help; make steps re-runnable).
6. **Guardrails respected?** Mostly. Campsite rule is misapplied (B3); never-self-merge
   is kept but the *current* merge protocol is newer than the rule the plan inherited
   (A1); quiet-pass rule violated (B6).
7. **Git workflow sound?** Branch-per-cycle + PR is fine *if* A1's publisher exists.
   Branch from latest main each cycle; union-merge the queue file on conflict.
8. **What's missing?** Publishing (A1), enrichment lane (A3), LOOPLOG (B4), standing-debt
   burn-down (B3), inventory/interlink upkeep (B7).

---

## D. Ideas from this plan worth adopting into the current loop regardless

- **T0 context briefs** — a cheap corpus-wide delta/cross-link pre-pass would improve the
  Claude Code loop's triage too. Extend `glm_draft_worker.py` with a brief mode; the loop
  consumes briefs during triage.
- **Structured judge verdicts** (JSON verdict + rubric scores + `reports/<slug>.judge.md`
  audit trail) — the current T1 review is implicit; recording it is strictly better.
- **Explicit max-2-revision-rounds** and the failure-mode table — current loop has these
  only as habits; write them down.
- **`preview/context-briefs/` audit trail** for triage decisions.

## E. Recommended rollout

**Shadow mode, 1–2 weeks.** Hermes cron runs the full pipeline and opens PRs, but the
Claude Code loop keeps running as today and acts as tool-equipped T1 on Hermes's PRs:
review, merge (standing authorization), Ghost-sync, spot-check. Compare Hermes's
dispositions against the Claude Code loop's own triage of the same queue items. Cut the
Claude Code loop's *writing* role over to Hermes when (a) disposition agreement is
consistently high, (b) judge verdicts hold up under T1 spot-audit, and (c) zero
fabrication-check failures ship. The merge + publish gate stays with Claude Code (or
Floyd) until Hermes has a clean track record — then granting it publish rights is a
one-line change, made deliberately rather than by default.
