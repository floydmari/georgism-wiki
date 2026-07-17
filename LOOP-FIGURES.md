# LOOP-FIGURES.md — the figure-sourcing loop

*Created 2026-07-16 (Floyd + Liam's ask: "pull images from the sources where it adds
value"). This is a periodic sweep over the EXISTING corpus, like
`LOOP-COMPREHENSIVENESS.md` — not part of LOOP.md's forward drafting cycle. Policy lives
in EDITORIAL §3c; this file is the runbook.*

**The mission:** every wiki entry whose source paper carries a load-bearing chart — the
figure that shows the finding the entry exists to document — should show that chart, with
honest provenance, a caption that does the reading for the visitor, and a credit line
marking the copyright boundary. A visitor who only looks at the pictures should still
meet the strongest evidence.

## The machinery (all in-repo)

| Piece | Role |
|-------|------|
| `scripts/build_figure_queue.py` | Deterministic pre-pass: scores every research/books entry (tier, inbound links, outcome wiring, PDF accessibility), skips entries that already carry a figure, writes `sources/figure-queue.md` |
| `sources/figure-queue.md` | The prioritized queue + status column (the loop's memory) + re-embed placement candidates |
| `scripts/source_figures.py` | The extraction pipeline: FIGURES manifest (provenance record) → PDF fetch → PyMuPDF crop → Ghost image upload → `<figure>` block |
| EDITORIAL §3c | The bar and the rules (load-bearing only, credit line, alt text, CC-BY carve-out) |

## One shift (≤4 figures — every crop gets human-grade eyes)

1. **Catch up & claim.** `git pull`; regenerate the queue
   (`python3 scripts/build_figure_queue.py`); claim the lane per LOOP.md "Claiming work"
   (stamp queue rows `in-progress:<branch>`; claims are only real on `origin/main`).
2. **Pick** the top unclaimed `todo` rows. Batch cap: **4 figures per shift** — each one
   needs visual verification, and small PRs keep the editor's review real.
3. **Get the PDF.** `source_url` first; if paywalled, find the open-access version
   (HAL, NBER/CEPR/CESifo/IZA working paper, author's site, institutional repository) and
   note WHICH version the figure numbers refer to. No legal open copy → stamp
   `blocked:paywalled` and route to the Hermes work order like any blocked fact-check.
   Shadow libraries are banned (sources/inbox/README.md) — for figures too.
4. **Find the load-bearing chart.** List the paper's figure captions (PyMuPDF text scan),
   read them against the entry's Summary/Key Findings, render the candidate page and
   LOOK at it. The §3c bar: the chart must carry the entry's **headline finding**, not
   decorate it. Papers with no such chart get stamped `no-chart` — that stamp is a
   finding; the loop never re-fetches them.
5. **Extract via the manifest — never hand-crop.** Add the FIGURES entry to
   `scripts/source_figures.py` (pdf_url, page, clip, dpi, alt, caption), render with
   `--no-upload`, **view the PNG** (crop the figure body; exclude the paper's own
   caption/notes; never alter the chart), iterate the clip until clean, then run the
   upload.
6. **Embed** the printed `<figure>` block after the entry's Summary — hosted URL in the
   `www.progress.org/content/images/...` form, descriptive alt text, caption that states
   what the chart shows AND the credit line ending "— reproduced for comment and review"
   (or "Public domain." for pre-1931 sources).
7. **Re-embed pass (optional, T1 judgment).** Work the queue's placement list: an
   outcome/problem/benefit page may re-embed an already-hosted figure that directly
   evidences its headline claim — same caption + credit, plus a link to the source's
   entry. One figure per page still.
8. **Gate & ship.** `lint_wiki.py` green → `build_preview.py` → screenshot the changed
   pages (figures render at column width, captions legible) → stamp queue rows `done` →
   LOOPLOG entry → commit (`figures: …`) → push → PR. **Editor review before merge**, as
   ever. After merge, sync the touched pages:
   `python3 scripts/sync_to_ghost.py <files…>` (foreground shell — background shells
   lack the 1Password token).

## Judgment split (generator–critic, same as LOOP.md)

- **T2/T3 can do** the mechanics: PDF fetch, caption listing, page renders, clip
  iteration, lint/preview runs.
- **T1 decides** what is load-bearing: which figure (if any) carries the entry's headline
  finding, the caption wording (it's a claim about evidence — claim-strength rules
  apply), and every re-embed placement. A wrong chart with a confident caption is worse
  than no chart.

## Guardrails

- **Never alter chart content** — crop only. No recoloring, relabeling, or redrawing.
  (If a redrawn/improved chart is ever wanted, that's a new dataviz work-stream with its
  own provenance rules — not this loop.)
- **One figure per page; the source entry is the canonical home** and embeds before any
  re-embed.
- **Copyright discipline:** figures are quotation-scale excerpts reproduced for comment
  and review; the credit line marks the CC-BY-4.0 carve-out. Public-domain test per
  EDITORIAL §3b if claiming PD.
- **Provenance is the manifest** — every hosted figure must have its FIGURES entry
  (source URL, page, crop box) committed in the same PR. PNGs are never committed.
- **Visual verification is mandatory** before upload — a queue stamp `done` asserts a
  human-grade look at both the crop and the rendered page.
- **Cadence:** run a shift when the queue's top score is ≥9, after big research-entry
  waves, or when Floyd/Liam point at a chart. Regenerate the queue after every merge.

## Exit criteria

The loop idles (not "finishes") when every `tier: core` and `tier: important` research
entry is stamped `done`, `no-chart`, or `blocked:paywalled` — new research entries re-arm
it, which is why the queue is regenerated rather than maintained by hand.
