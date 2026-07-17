# ROADMAP.md — The Master Plan (strategic context for any session)

This is the durable copy of the approved master plan. `BACKLOG.md` holds the executable task
queues; this file holds the *why* and the big picture. Read together with `LOOP.md` (how to run
an iteration) and `EDITORIAL.md` (content rules).

## Vision

(Canonical short form: EDITORIAL.md §0 — quoted by every executor prompt so all models,
Claude or otherwise, work from the same mission.)

Make progress.org/wiki the definitive, Wikipedia-quality reference for the Geoist ecosystem —
all economic rents and their capture for public good, with the Georgist land core as its
foundation (scope expanded by Floyd, 2026-07-06; see EDITORIAL §0).
A reader can: (1) click any **benefit** and see every study that supports *or challenges* it,
inline-cited; (2) browse the persuasive **narratives** for LVT and see which have research
backing, who promotes them, and how to deploy them; (3) find any concept, person, place, or body
of research in one comprehensive, cross-linked place. Persuasive *because* accurate, well-sourced,
and intellectually fair — a skeptical reader sees their strongest objection understood, sourced,
and answered.

## The model division of labor (generator–critic)

Tiers are roles, not hard-wired models: **T1 frontier** (Fable 5 preferred; any frontier model as
stand-in) architects, judges evidence strength, steelmans objections, reviews every page, and is
the publish gate. **T2 mid** (Sonnet-class) drafts pages from vetted sources. **T3 bulk**
(Haiku/Flash-class, or a near-free external model via `scripts/llm_worker.py`) does mechanical
volume: cross-links, registry upkeep, scans. Cheap tiers generate and never publish unreviewed;
T1 review is what makes a page publishable. GitHub is the master record; Ghost publishing happens
only afterward via `scripts/sync_to_ghost.py`.

## Work streams and status (2026-07-04)

| # | Stream | Status |
|---|--------|--------|
| WS-infra | Editorial system, lint gate, preview, registry, hooks | ✅ done |
| WS2 | Narratives layer (12 planned) | ✅ **12/12 shipped 2026-07-05** (`narratives/_framework.md`) |
| WS3 | Research comprehensiveness (47→100+) | ~76 pages; 50-paper evidence campaign in progress |
| WS1 | Benefit→research linkage, ≥5 papers per outcome | **43/65 slots; 1/13 outcomes at goal** — active campaign, gauge in `lint_wiki.py` |
| WS6 | Concepts expansion (22→40+) | queued |
| WS5 | Deepen thin articles | partly done (deepen-scan wave); remainder queued |
| WS8 | Claim-level citation retrofit of legacy pages | queued (`[CITE]` tasks) |
| WS4/7 | Full cross-link graph, UX polish, `last_reviewed` everywhere | orphans 0 as of wave 3; rest queued |
| WS9 | Figure sourcing — load-bearing charts into entries (`LOOP-FIGURES.md`, EDITORIAL §3c) | **active 2026-07-16**: pipeline + queue live; 4 figures shipped (Bonnet, Rognlie, JST, KSS); 341-candidate queue seeded |

Success metrics: articles 139→300+ (now 240), research 47→100+ (now ~85), narratives 0→12 (✅ 12),
outcomes each ≥5 supporting papers, zero fabricated citations ever (enforced by
`[CITATION NEEDED]`/`[VERIFY]` discipline + lint).

## The growth flywheel (added 2026-07-04)

Ingest → extract → **discover across all categories** → stub immediately (sourced, visible,
tracked by lint's STUBS gauge) → T1 prioritizes the stub queue each wave → backfill re-mines the
already-ingested corpus before new web research → repeat. Breadth and depth grow together; each
ingest raises the value of every earlier one. Mechanics: LOOP.md (flywheel + step 8),
tasks/backfill-page-task.md, EDITORIAL.md stub standard.

## The comprehensiveness loop (added 2026-07-04, separate from the main loop)

A periodically-invoked audit (`LOOP-COMPREHENSIVENESS.md`): re-scan every SOURCE in the registry —
not the wiki pages — to catch anything the original single-purpose extraction missed across all 8
categories, with a dedicated authors channel (repeat contributors and Core-paper authors get
people/ pages). Phases: deterministic pre-pass (`scripts/comprehensiveness_prepass.py`) → source
sweep (report-only agents) → T1 triage → stubs → content development from the existing corpus →
watermark. Invoke after every ~50 new registry rows. Not part of LOOP.md's forward cycle.

## Standing constraints & pending items (outside the content loop)

- **Ghost publishing** is gated on `OP_SERVICE_ACCOUNT_TOKEN` (1Password service account → Emma
  vault) in the environment settings; `.claude/hooks/session-start.sh` then auto-loads
  `GHOST_ADMIN_KEY` each session. Until set: commit-only; publish is a later credentialed run.
- **Google Sheet mirror** of `sources/registry.csv`: snapshot-per-wave via Drive connector
  (mandatory-loud rule in `LOOP.md` step 3); durable in-place write-back awaits a Google
  service-account JSON in the Emma vault.
- **Egress proxy 403s most academic hosts** — agents corroborate via multi-source search and mark
  `[VERIFY]`; widening the network policy would upgrade many pages from Medium to Heavy scans.
- **External cheap models** (e.g. ollama-cloud GLM) can serve as T2/T3 via `scripts/llm_worker.py`
  once `LLM_API_KEY` + egress access exist; no-web models cite only supplied context.
- The live-site preview is republished each wave to the same Claude artifact URL; local preview:
  `python3 scripts/build_preview.py && python3 -m http.server -d preview 8000`.

## Exit criteria — when does the looping stop? (added 2026-07-05, Floyd + T1)

A wiki never "finishes"; campaigns finish and then the wiki enters maintenance. Floyd's
instinct — "all significant new research and findings in the last 50 years related to
economic rents processed" — is the right north star, made operational as three testable
gates rather than a judgment call:

**Gate 1 — Structurally complete** (measurable in lint, nearly reached):
all 12 narratives live · STUBS gauge 0 (or only owner-blocked items) · every objection
steelmanned with its primary source read · every outcome ≥5 supporters AND challenged_by
wherever counter-evidence exists · registry 100% Scanned at tier-appropriate depth
(Heavy for Core books) · zero [CITE]-queue pages without claim-level citations (WS8).

**Gate 2 — Canon convergence** (the operational version of "all significant research"):
"significant" = (a) cited ≥2 times by works already in the registry (snowball citation
mining), or (b) meets a venue+citations bar in a systematic sweep of the rent literature
(JUE/RSUE/NTJ/QJE/AEJ + Lincoln, IMF/OECD/World Bank, AJES) for 1975–present.
DONE is defined by **convergence, not coverage judgment**: run discovery invocations
(comprehensiveness loop + a citation-snowball round) and log the accept rate; when TWO
consecutive full invocations each yield fewer than ~5 accepted new pages, the corpus has
converged — the frontier is empty at the significance bar. Each invocation already
records its watermark + accept/reject counts in BACKLOG, so the trend is auditable.

**Gate 3 — Maintenance mode** (the actual exit): when Gates 1–2 hold, retire the
campaign loops and switch to a low-frequency maintenance loop — monthly: new-publication
sweep (post-watermark registry rows through the comprehensiveness loop), staleness sweep
("as of" claims, dead links, last_reviewed >12mo), cohesion audit, Ghost sync. Looping
"stops" in the sense that it becomes an hour a month instead of a campaign.

Current position: Gate 1 is ~80% (3 narratives, 8 stubs, WS8 retrofit outstanding);
Gate 2 has run one invocation (136 sources, 29 accepts — nowhere near convergence, as
expected this early); Gate 3 is blocked on GHOST_ADMIN_KEY for the sync half.

## Resuming after any reset

Everything needed is in-repo: start from the **⟳ RESUME HERE** block at the top of `BACKLOG.md`.
The loop has survived context summarization and a hard session kill; recovery is always
`git status` + `lint_wiki.py` + the backlog.
