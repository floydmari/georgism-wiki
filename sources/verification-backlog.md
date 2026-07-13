# Verification Backlog — deferred primary-source checks (retry ledger)

*Created 2026-07-13 (wave 28). INTERNAL — this file lives in `sources/` and is **not**
published to Ghost (the sync only touches wiki content folders). Its job is to keep the
"we couldn't get the primary this session" items **retryable** instead of losing them.*

## Why this file exists
Wave 27 (2026-07-13) cleared the in-page `[CITATION NEEDED]/[VERIFY]` markers on ~19 pages.
Those markers render as **visible text on the public wiki**, so leaving them in reader-facing
prose is not acceptable long-term — wave 27 correctly rewrote each as an honest one-line
provenance caveat ("relies on X's secondary citation; primary not independently consulted").
The tradeoff (flagged by Floyd): once the marker token is gone, `scripts/verification_queue.py`
and a `grep [VERIFY` sweep no longer surface the item, so it drops off the retry queue.
**This ledger is that retry queue, kept out of the published body.**

## Access policy
**Paid / library access APPROVED by Floyd (2026-07-13).** Free/legal copies still preferred,
but JSTOR / publisher / a purchased e-book / a working archive.org lending link are all fair
game now. Book-copy items are also tracked in `sources/wanted-books.md` (deliver a PDF/EPUB or
a working link there and each has a ready wiki target).

## RETRYABLE — primary exists, we couldn't reach it this session
| Page | What's still unverified | Unblock channel |
|------|-------------------------|-----------------|
| `research/phelps-brown-weber-accumulation` | the 1953 *Economic Journal* paper's own capital-return figures (page currently leans on Harrison's citation of it) | **paywall** — JSTOR / OUP |
| `research/tideman-plassmann-losses-of-nations` | the primary chapter in *The Losses of Nations* (Harrison ed., 1998); the "$7tn" magnitude is framed against a US counterfactual, not a verified G7 aggregate | **book copy** (add to wanted-books) |
| `research/world-bank-changing-wealth` | main-volume (chapter-level) detail; Executive Summary + FAQ were read directly, main PDF returns 403/404 | **forage** — working WB/openknowledge mirror |
| `research/widerquist-howard-pfd` | page-level quotations vs the book text (chapters confirmed via publisher/RePEc listings only) | **book copy** — *Alaska's Permanent Fund Dividend*, Widerquist & Howard eds. (already in wanted-books) |
| `research/modelewska-value-capture-finance` | the ~55-rail-studies count is Patel's characterization; the thesis full text isn't online | **forage** — UCL repository / ILL |
| `research/pistor-code-of-capital` | direct page citations (book cited but not fully read) | **book copy** — *The Code of Capital*, Pistor 2019 |
| `research/vickrey-counterspeculation-auctions` | direct page cite from *Radical Markets* (Posner & Weyl) | **book copy** — *Radical Markets* (already in wanted-books) |
| `research/myerson-satterthwaite-bilateral-trade` | exact footnote wording/page in *Radical Markets* | **book copy** — *Radical Markets* (**same copy clears vickrey too**) |
| `research/lewis-building-cycles` | Lewis's primary text (page drafted from secondary/reception sources; 17.4-yr figure is Harrison's reading) | **book copy** — *Building Cycles* (already in wanted-books) |
| `research/miller-dying-for-justice` | the 50,000 figure + submission detail (book not digitized; via Harrison's secondary account) | **book copy** — *Dying for Justice*, Centre for Land Policy Studies 1999 |

**Quick win:** one copy of *Radical Markets* closes **two** rows (vickrey + myerson), and there
are further Radical-Markets-dependent pages tracked in `sources/wanted-books.md`.

## SETTLED — nothing to retry (recorded so no one re-opens them)
- `research/piketty-capital-21st-century` — the primary (Piketty & Zucman 2014 QJE) **was** fully read; the caveat just documents scope. No action.
- `research/simpson-real-estate-speculation-depression` — attribution clarified ("largest single factor" is Anderson's synthesis, not Simpson's words). No action.
- `research/natural-common-wealth-economic-rent-canada` — a genuine search found **no** independent third-party assessment of this specific report; only re-open if one gets published.
- `research/social-problems` — no dedicated reception/circulation scholarship exists; the reach claims are inferential by necessity.
- `narratives/land-speculation-causes-cycles` — 2× `[VERIFY — PENDING]` are **time-locked** (Foldvary's 2026 forecast; revisit after year-end 2026). Left in place deliberately.

## How to work this ledger
1. Obtain a source (paid/library now approved) → verify the specific claim on the page → replace the provenance caveat with a proper citation → delete the row here.
2. Book arrivals also update `sources/wanted-books.md`.
3. Live in-page markers (if any are re-introduced) are still tracked by `scripts/verification_queue.py` → `sources/verification-queue.md`; this ledger covers the items that were resolved-to-caveat and thus no longer carry a marker.
