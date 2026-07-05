# sources/inbox/ — Hermes delivery protocol (evidence courier lane)

This directory is the **hand-off point between Floyd's Hermes agent (unblocked web
access, book procurement) and the wiki's editorial loop (T1 review gate)**. Hermes
works the queues; the loop consumes deliveries, verifies them, resolves markers, and
edits pages. Division of labor, agreed 2026-07-05:

- **Hermes DOES:** fetch blocked URLs, procure free/legal book copies, extract exact
  quotes/figures with locators, drop deliveries here (new files only).
- **Hermes DOES NOT:** edit wiki pages, registry.csv, BACKLOG.md, or resolve
  `[VERIFY]`/`[CITATION NEEDED]` markers itself. One editorial pipeline; the loop is
  the publish gate. (If Hermes spots an error in a wiki page, it files a note here —
  `NOTE-<slug>.md` — rather than editing the page.)

## What to work from

1. `sources/verification-queue.md` — sections **"needs-unblocked-web"** (115 items)
   and **"needs-book-copy"** (43 items). Each entry names the page and what needs
   verifying.
2. `sources/wanted-books.md` — the book list with wiki targets. **Free/legal copies
   only** (open-access PDFs, publisher-released files, Internet Archive lending,
   author-hosted copies). No pirated files — deliveries that can't name a legal
   provenance will be discarded.

## Delivery format

One delivery = one manifest file, plus payload(s). Name by the wiki page it serves:

```
sources/inbox/<slug>.manifest.md      ← required
sources/inbox/<slug>.<ext>            ← payload: .pdf/.txt/.html (≤25 MB; bigger → Drive link in manifest)
```

Manifest template:

```markdown
# Delivery: <slug>
- queue-item: <the exact line(s) from verification-queue.md this answers>
- fetched-from: <URL(s)> on <date>
- provenance/legality: <why this copy is legal — publisher OA, IA lending, author page…>
- payload: <filename or Drive link> (sha256: <hash>)

## Findings (one block per marker addressed)
- marker: <the [VERIFY: …] text verbatim>
- verdict: CONFIRMED | CORRECTED | NOT-FOUND
- evidence: "<exact quote ≤50 words>" (p. X / §Y / table Z)
- notes: <anything the editor should know — e.g., figure differs between versions>
```

Hard rules for manifests: quotes must be **verbatim with a locator** (page/section/
table) — that is the entire value-add over the snippet-corroboration the loop already
did. A verdict of CORRECTED must show the correct value with its locator. Never
paraphrase inside quote marks.

## How the loop consumes this

Each iteration begins with an **inbox sweep** (LOOP.md step 1): verify manifest
against payload → apply verdicts (resolve markers, correct figures, upgrade Scan
Depth Light→Medium/Heavy, queue [DEEPEN-SCAN] for delivered books) → move consumed
deliveries to `sources/inbox/consumed/` with a line in LOOPLOG → regenerate
`sources/verification-queue.md`.

## Growth path

If this lane runs well, Hermes can graduate to running LOOP.md DRAFT-loop iterations
itself (the loop is model-agnostic by design: T2/T3 work ending at
`status:needs-review` + PR, never publishing). Conditions: it works on a single
dedicated branch (`hermes/draft-loop`), claims tasks in BACKLOG by setting
`status:in-progress` before starting (prevents the duplicate-drafting collision of
2026-07-05), and everything it drafts still lands behind the T1 review gate.
