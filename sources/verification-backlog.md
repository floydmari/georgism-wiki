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
| `research/tideman-plassmann-losses-of-nations` | **narrowed 2026-07-17:** chapter now pinned ("Taxed Out of Work and Wealth", Ch. 6) and the per-country figures double-corroborated by two independent secondaries (Labour Land Campaign *Cut Out the Deadweight* fn. xiv + Leichter 2013) — US $5.495tn actual vs $7.097tn counterfactual, UK at 55% of counterfactual. Still unverified against the primary: whether the volume states any combined G7 figure, and which country (if any) shows the "over 90%" gain. Book confirmed undigitized (not on archive.org; Google Books metadata-only). wealthandwant.com was DNS-unreachable from the sandbox — worth one retry from an unrestricted network. | **book copy** (in wanted-books) |
| `research/modelewska-value-capture-finance` | the ~55-rail-studies count is Patel's characterization; **confirmed 2026-07-17 the full text is nowhere online** — UCL Discovery says "Full text not available", EThOS (restored) is a metadata mirror pointing back to the same record, nothing on ResearchGate/Academia/Bartlett | **ILL to UCL Library, or contact the author** — foraging is exhausted |
| `research/lewis-building-cycles` | **narrowed 2026-07-17:** two independent HathiTrust search-only scans (`mdp.39015007186649`, `mdp.39015030457421`) both place the book's single "17.4" occurrence at **printed p. 314** — three independent indexes now corroborate the figure and its location, but no snippet tier exists, so the context is still unread. Barras (2009, searchable preview) contains no "17.4" and quotes Lewis only on methodology. A second archive.org copy exists (`buildingcyclesbr0000unse_b5o0`), same CDL restriction. **Cheapest unblock: free archive.org account + 1-hour CDL loan of either copy, read p. 314 directly** (a human step — needs account signup). Fleming's 1966 EcHR review (DOI 10.2307/2592282) added to the page's sources. | **1-hr archive.org loan** (or book copy — in wanted-books) |
| `research/miller-dying-for-justice` | the 50,000 figure + submission detail (book not digitized — archive.org/Google Books confirmed empty 2026-07-17; via Harrison's secondary account, which itself concedes the analysis was never peer-evaluated). Same pass: publication year corrected to **2003** (BMJ obituary + *Ricardo's Law* bibliography/footnote; the AbeBooks 1999 date is a catalogue error) and the RCP/BMJ obituary added as an independent source on Miller's credentials. | **book copy** — *Dying for Justice*, Centre for Land Policy Studies 2003 |

## SETTLED — nothing to retry (recorded so no one re-opens them)
- `research/widerquist-howard-pfd` (2026-07-17) — **closed**: Goldsmith's Ch. 4 was read in full via co-editor Widerquist's self-hosted pre-publication manuscript of the entire volume ([widerquist.com PDF](https://widerquist.com/wp-content/uploads/2024/03/Alaskas-Permanent-Fund-Dividend-Examining-its-Suitability-as-a-Model-107.pdf), 342 pp.; front matter self-identifies as an early version of the published book). The income-inequality-reversal passage was read verbatim (fn. cites Bernstein et al., *Pulling Apart*, CBPP 2005). One reattribution: the Alaska Native 25%→19% poverty figure is **absent** from Ch. 4's text — it lives in Goldsmith's 2010 BIEN XIII paper (fn. 22), and the page now cites it there. Residual (accepted): draft wording may differ trivially from the paywalled typeset text; nothing on the page depends on it.
- `research/piketty-capital-21st-century` — the primary (Piketty & Zucman 2014 QJE) **was** fully read; the caveat just documents scope. No action.
- `research/simpson-real-estate-speculation-depression` — attribution clarified ("largest single factor" is Anderson's synthesis, not Simpson's words). No action.
- `research/natural-common-wealth-economic-rent-canada` — a genuine search found **no** independent third-party assessment of this specific report; only re-open if one gets published.
- `research/social-problems` — no dedicated reception/circulation scholarship exists; the reach claims are inferential by necessity.
- `narratives/land-speculation-causes-cycles` — 2× `[VERIFY — PENDING]` are **time-locked** (Foldvary's 2026 forecast; revisit after year-end 2026). Left in place deliberately.
- `research/vickrey-counterspeculation-auctions` (2026-07-14) — **closed**: verified against Princeton University Press's free sample chapter of *Radical Markets* Ch. 1 ([assets.press.princeton.edu/chapters/s11222.pdf](https://assets.press.princeton.edu/chapters/s11222.pdf)); page cite is now pp. 49–50, endnote 29. No further action.
- `research/myerson-satterthwaite-bilateral-trade` (2026-07-14) — **closed**: same PDF confirmed the Ch. 1 passage and page/endnote (pp. 50–51, endnote 32; p. 66, endnote 56) invoking Myerson–Satterthwaite against Coase. One residual gap noted on the page itself: the literal back-matter endnote text (vs. the body text it footnotes) wasn't in the sample chapter, so wasn't independently seen.
- `research/phelps-brown-weber-accumulation` (2026-07-14) — **closed**: the 1953 *Economic Journal* issue (vol. 63, no. 250) is digitized and freely readable on the Internet Archive (`sim_economic-journal_1953-06_63_250`, not access-restricted, no login/paywall). The paper's own capital-return figures were read directly and are now cited on the page with printed page numbers (pp. 266, 266–267, 271), confirming Harrison's 10–11%-to-~7% figure and clarifying that the paper itself does not discuss land returns or use a "scissors" framing — that synthesis is Harrison's own, not the paper's. No further action.
- `research/pistor-code-of-capital` (2026-07-14) — **closed via alternate channels, not the book itself**: no archive.org copy or Google Books preview of *The Code of Capital* exists (checked this session). Direct page citations (pp. 4, 86, 93, 229, 317–318) were obtained instead via two reliable channels quoting/restating the book's own text with confirmable pages: Pistor's own 2021 *Social & Legal Studies* rejoinder essay (her own words, read in full) and a Jotwell law-review quoting the book verbatim with page numbers. The 297-page book itself is still not read cover-to-cover — re-open only if a claim beyond what's now cited (e.g. the sovereign-debt or IP chapters' internal argument) needs checking.

## How to work this ledger
1. Obtain a source (paid/library now approved) → verify the specific claim on the page → replace the provenance caveat with a proper citation → delete the row here.
2. Book arrivals also update `sources/wanted-books.md`.
3. Live in-page markers (if any are re-introduced) are still tracked by `scripts/verification_queue.py` → `sources/verification-queue.md`; this ledger covers the items that were resolved-to-caveat and thus no longer carry a marker.
