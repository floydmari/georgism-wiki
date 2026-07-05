# sources/inbox/ — Hermes delivery protocol (the Fact-Check Desk's field agent)

> **The mission you are working for:** the definitive, honest reference on Georgism and land
> value taxation (progress.org/wiki) — every claim cited, every counterargument steelmanned,
> every important source read and mined. Your environment (unblocked web + Floyd's book
> library) can resolve the fact-checks this repo's environment cannot: your standing
> assignment is **`sources/hermes-workorder.md`** (auto-generated each shift from the
> verification queue), plus book scans from `sources/wanted-books.md`. Accuracy beats
> coverage: a CORRECTED or NOT-FOUND verdict is as valuable as a CONFIRMED one.

> **UPDATE 2026-07-05 (Floyd's authorization):** Hermes is promoted to running FULL
> DRAFT-loop iterations — it edits wiki pages directly on its own `hermes/*` branch
> under EDITORIAL.md + LOOP.md rules, ending at an open PR that the T1 loop reviews.
> The courier-only restriction below is superseded; this inbox remains available for
> raw-evidence hand-offs where a full edit isn't warranted. Two rules survive
> unchanged: Hermes never merges its own PRs, and copyrighted book files/long
> excerpts are NEVER committed — books stay in Floyd's private storage; the wiki
> carries a summary page per book (≤50-word quotes, page-cited) in the **`books/`
> category** (ratified 2026-07-06 — Hermes's `books/*.md` pages made this a
> first-class category; frontmatter standard in EDITORIAL.md §5).

## Discovery is universal (generalized 2026-07-06, Floyd)

**Every source Hermes processes — book scan, paper, article, or verification-queue
item — must ALSO produce a discovery report**, not only the summary/marker work. The
original rule covered book scans; it now covers everything. For each source
processed, file `DISCOVERY-<slug>.report.md` (in the PR next to the work, or in this
inbox; the earlier `BOOKSCAN-<slug>.report.md` name is accepted for books) listing
candidates in **ALL wiki categories**:

- **research** — papers/studies the source cites that bear on wiki outcomes
- **people** — scholars, reformers, politicians, critics warranting a bio
- **events** — historical episodes (campaigns, crashes, enactments, repeals)
- **places** — jurisdictions with land-policy experience
- **concepts** — mechanisms/terms the wiki lacks
- **organizations** — institutes, movements, publishers
- **objections** — recurring counterarguments not yet steelmanned on the wiki
- **books** — further books referenced (→ `sources/wanted-books.md` if no free/legal
  e-copy; a `books/` page once scanned)

Per candidate, one line: name · category · why warranted (which wiki page needs it) ·
where found (page/section locator). The T1 loop triages every report — accepted
candidates become stubs per EDITORIAL.md's stub standard, rejected ones get a
one-line reason. A scan that produces zero candidates is a smell, not a clean bill.

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
   author-hosted copies, or a copy Floyd verifiably owns). No pirated files —
   deliveries that can't name a legal provenance will be discarded.
   **HARD RULE (added 2026-07-06 after two w1 pages named libgen.vg as source):**
   Library Genesis, Z-Library, Anna's Archive, Sci-Hub and similar shadow-library
   sources are PROHIBITED as procurement channels, even when the file never touches
   the repo. Every book page's Origin line must name a legal provenance (owned copy,
   OA, lending, publisher). Pages sourced from a prohibited channel get a
   provenance-pending [VERIFY] flag at T1 review and their scan-depth upgrades are
   frozen until the owner attests a legitimate copy.

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
