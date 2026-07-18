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

## 2026-07-18 — T1 VERIFY-channel pass (in-page marker burn-down, wave continuing ab63114)
Regenerated ground truth from scratch: a full `grep [VERIFY|CITATION NEEDED` sweep across
every content category (not just `scripts/verification_queue.py`'s CATS list) found **30**
live markers (23 caught by the script's strict regex + 2 `[VERIFY — PENDING]` time-locked
markers the regex deliberately doesn't match + 5 more the script *does* match once its
regex quirks are accounted for — see `sources/verification-queue.md`'s header for the
reconciliation). Classified every marker DELIBERATE-SCOPED (13, honest scope notes — OCR
caveats, session-boundary notes, a source-internal inconsistency, time-locked forecasts —
left in place) / RETRYABLE (started at 9, worked down) / BLOCKED (book copy, paywall, or
no-longer-extant primary). Worked the RETRYABLE queue, highest-value first, **5 resolved**:
- `research/gaffney-alaska-oil-leasing.md` — the Vickrey/Consigny neutral-depreciation proof
  (Appendix J of the report's Part II) was pinned to its exact primary source: it is
  Appendix II of Gaffney's own 5-part AJES series "Tax-Induced Slow Turnover of Capital"
  (Part V, *AJES* 30(1), 1971, pp. 105–111), fetched directly from masongaffney.org's own
  posted unabridged text (`pdftotext -layout` recovered an embedded OCR text layer; no
  image OCR needed) and cross-checked word-for-word against the Alaska-report reprint
  already OCR'd locally. Confirms the joint Vickrey/Consigny credit is accurate (per the
  document's own authorship footnote) and that the proof sits inside Gaffney's article
  rather than a separate Vickrey–Consigny paper. New registry row added.
- `places/south-korea.md` — the truncated basicincomekorea.org PDF URL was reconstructed
  via web search and fetched in full (`pdftotext`); corrected the presentation's exact
  title ("Common Wealth Rent and **Common Wealth** Basic Income," not "...and Basic
  Income") and the author's name ("Nam Hoon Kang," two words, not "Namhoon"). Registry
  row updated in place (Status: Referenced → Scanned).
- `research/gaffney-new-life-in-old-cities.md` — the Pittsburgh "10% of property tax base"
  land-value figure (attributed to councilman Dan Cohen) was independently corroborated —
  not via Gaffney's own citation, but via Mark Alan Hughes's 2006 Lincoln Institute working
  paper (already in the registry for the Pennsylvania page), whose own footnote 42 traces
  the identical claim to a named, dated article: Christopher Snowbeck, "Murphy: Land Tax
  Values Illogical," *Pittsburgh Post-Gazette*, January 15, 2001. New Sources entry added
  to the page; registry row's citation count bumped.
- `research/gaffney-forest-taxation.md` — "Number 43, March 1980"'s publication venue was
  identified via masongaffney.org's own publication catalog (not stated in the document
  itself): Will Knedlick (ed.), *State Taxation of Forest and Land Resources*, Lincoln
  Institute of Land Policy, 1980, pp. 5–16; "Number 43" is Gaffney's UC Riverside working-
  paper number, not a separate lecture series as the prior text speculated.
- `research/gaffney-capital-gains-free-enterprise.md` — confirmed the host volume (Richard
  Noyes ed., *Now the Synthesis*) did complete publication as the source document's own
  "being expanded for Shepheard-Walwyn" note anticipated (Shepheard-Walwyn/Holmes & Meier,
  1991) — the wiki already has this book fully primary-verified at Heavy scan depth
  (`books/now-the-synthesis.md`), so this resolution links there rather than duplicating
  the read.

3 more RETRYABLE items were attempted and moved to BLOCKED after failing (Samuelson 1976,
paywalled/403'd on every free channel tried; a 1971 Milwaukee Journal article, no free
digitized copy; an unpublished Andelson conference address, no trace found online) — see
`sources/verification-queue.md` BLOCKED section for detail. 6 RETRYABLE rows remain open
for the next wave (WP041/WP042 date, Alaska report circulation history, the Clawson $42bn
figure, the Jarvis Prop-13 slogan, a citation-count check, and the T&F PDF cross-check for
`august-rental-financialization`). Lint 0 errors before and after; queue script's marker
count 28→23 (the 5 resolutions; the 2 PENDING markers were never in its count).

## 2026-07-18 (cont.) — T1 retryable-queue wave 2 (6 RETRYABLE worked: 3 resolved, 3 BLOCKED)
Worked all 6 RETRYABLE rows queued above, same day. **3 resolved:**
- `research/august-rental-financialization.md` — a second independent mirror of the
  actual Taylor & Francis-typeset PDF (tandfonline.com branding, DOI cover page, "To
  cite this article" header intact) was found via web search at a University of
  Waterloo-region community site (not the paywalled tandfonline.com page itself, which
  Unpaywall confirms has no OA copy — `is_oa: false`, `oa_status: closed`). Downloaded
  both this PDF and the already-cited Herongate Tenants mirror with `curl`, extracted
  both with `pdftotext -layout`, and spot-checked every figure the wiki page cites
  (164,498-suite REIT growth including its footnote marker, the 290,712 top-25 total,
  the 15.8%→20.2% concentration rise, "27.8"/"one fifth" phrasing, "nine of the top 10,
  and 18 of the top 25") — all matched verbatim between the two independent copies.
  Marker removed.
- `research/gaffney-forest-taxation.md` — identified Gaffney's likely source for the
  $42-billion National Forest valuation: Marion Clawson, "The National Forests,"
  *Science* 191(4228): 762–767 (Feb. 20, 1976), found via a targeted web search after
  general Clawson/RFF searches turned up nothing. The article's own PubMed abstract
  (the article itself is paywalled, not read in full) independently states
  "approximately $42 billion in assets" and "$400-500 million annually" — corroborating
  Gaffney's headline figure and revenue range. Gaffney's more granular $486-million 1974
  receipts/outlays split is still his own citation of Clawson, not independently
  re-derived — noted as a narrower residual caveat rather than a blanket marker. New
  registry row added (Light scan / abstract-only).
- `research/gaffney-soil-depletion-land-rent.md` — Semantic Scholar's paper-search API
  (`api.semanticscholar.org/graph/v1/paper/search`) records **21 citations** for
  Gaffney's 1965 paper (rate-limited on repeated calls; one successful call sufficed).
  Marker removed.

**3 moved to BLOCKED:**
- `research/gaffney-alaska-oil-leasing.md` — WorldCat (`worldcat.org`,
  `search.worldcat.org`) returned HTTP 403/429 on every access pattern tried in this
  environment; no citing paper or Alaska State Library catalog record surfaced via
  general web search. Direct catalog access (outside this environment) or an Alaska
  State Library/legislative-archives lookup is the next channel.
- `research/gaffney-land-distinctive-factor.md` — Jarvis's *I'm Mad As Hell* (1979) is
  on Internet Archive only as a borrow-restricted scan (no full-text search without a
  loan); a previously indexed third-party full-text mirror (members.tripod.com) no
  longer resolves (DNS failure). Book/archival access needed.
- `research/gaffney-land-market-distortions.md` — re-checked masongaffney.org's
  workpapers listing and vita/CV page (still no date shown for WP041/WP042); searched
  for citing sources by title (found only one indirect, itself-undated mention); tried
  fetching two of Gaffney's own later papers that might cite these by date (2007 UCR
  working paper, 2009 AJES paper) but PDF text extraction failed on both (image/font-
  encoded streams) in this environment. Circa-1993 remains the best-supported estimate.

Lint 0 errors before and after; live-marker count 25→22 (3 resolutions this pass).

## RETRYABLE — primary exists, we couldn't reach it this session
| Page | What's still unverified | Unblock channel |
|------|-------------------------|-----------------|
| `research/tideman-plassmann-losses-of-nations` | the primary chapter in *The Losses of Nations* (Harrison ed., 1998); the "$7tn" magnitude is framed against a US counterfactual, not a verified G7 aggregate. **Update 2026-07-16:** a *different* chapter of the same book — Mason Gaffney's Ch. 7, "The Philosophy of Public Finance" (pp. 175–205) — is now held locally in full (`sources/gaffney/text/G44_Philosophy_of_Public_Finance.txt`, spot-checked against `sources/gaffney/G44_Philosophy_of_Public_Finance.pdf`; see [research/gaffney-philosophy-of-public-finance](/wiki/gaffney-philosophy-of-public-finance/)). This confirms the book's title ("The Losses of Nations," from the running header), the Othila Press/1998 publication basis, and the chapter-book structure directly from a primary copy — but it is Gaffney's chapter, not Tideman & Plassmann's, and contains no G7 deadweight-loss figures. **This row stays open**: Tideman & Plassmann's own chapter (with the $7tn claim) has still not been independently obtained. **Update 2026-07-17 (T2 link-health pass):** the sharetherents.org mirror is confirmed permanently dead (registry `Status` set to `Dead link`) — sharetherents.org's current `/publications/` page links the 1998 book only to an Amazon purchase page, no Wayback capture of the PDF exists at any timestamp, and no copy was found at landresearchtrust.org, cooperative-individualism.org, SSRN, archive.org, or the authors' pages. Independently pinned the chapter's exact title and pages via Wikipedia's own citation + corroborating search: "Taxed Out of Work and Wealth: The Costs of Taxing Labor and Capital," pp. 146–174 — added to `research/tideman-plassmann-losses-of-nations.md`, but this is a citation-precision gain only, not a primary read. | **book copy** (add to wanted-books) — specifically still need Tideman & Plassmann's own chapter, not Ch. 7 |
| `research/widerquist-howard-pfd` | **narrowed 2026-07-14:** front matter, the full 15-chapter TOC (with primary-confirmed page numbers), and the complete Ch. 12 (Casassas & De Wispelaere, pp. 169–188) are now read directly, via a contributor-hosted PDF (davidcasassas.com). What remains unverified is specifically **Goldsmith's Ch. 4 (pp. 49–64)** — the volume's central empirical chapter (the income-inequality reversal and Alaska Native poverty-rate figures) — still sourced to the RePEc listing/secondary description only. | **book copy** — *Alaska's Permanent Fund Dividend* (already in wanted-books); specifically need Ch. 4 |
| `research/modelewska-value-capture-finance` | the ~55-rail-studies count is Patel's characterization; the thesis full text isn't online | **forage** — UCL repository / ILL |
| `research/lewis-building-cycles` | **checked 2026-07-14:** the one archive.org copy (`buildingcyclesbr0000unse`) is lending-restricted — search-inside/fulltext API returns 403 without a loan. Google Books confirms "17.4" occurs exactly once in the indexed text (search-within-book hit count) but is a no-preview record — no snippet or page number visible. Lewis's primary text (Table 5.1, the 17.4-yr figure's context) remains unverified. | **book copy / library loan** — *Building Cycles* (already in wanted-books) |
| `research/miller-dying-for-justice` | the 50,000 figure + submission detail (book not digitized; via Harrison's secondary account) | **book copy** — *Dying for Justice*, Centre for Land Policy Studies 1999 |
| `research/cohen-coughlin-two-rate-taxation` (2026-07-16) | Edwin S. Mills's original chapter, "The Economic Consequences of a Land Tax" (in Netzer, ed., *Land Value Taxation: Can It and Will It Work Today?*, Lincoln Institute of Land Policy, 1998, pp. 31–48) — the primary behind the "site rents at most 1 percent of property values" figure. Checked this session: not on archive.org, not previewable on Google Books, no free PDF found. Cohen & Coughlin's own exact wording (p. 370) was confirmed directly against a full-text PDF, and an independent Netzer conference summary (*Land Lines*, March 1998) corroborates the substance (Mills skeptical of LVT revenue adequacy), so the page's claim is well-attributed even without Mills's own text. | **book copy / library** — *Land Value Taxation* (Netzer ed., 1998); add to wanted-books |
| `research/lapavitsas-financialization` (2026-07-16) | the 2013 *City* article's full text ("The financialization of capitalism: 'Profiting without producing'," 17(6): 792-805) — still unreachable. Retried this session via the Taylor & Francis PDF (HTTP 403, Cloudflare challenge, including the `?needAccess=true` variant Unpaywall's metadata points to), ResearchGate (HTTP 403), and the SOAS institutional repository (eprints.soas.ac.uk, unreachable/502). A Marx & Philosophy Review of Books review of the related 2013 book (Despain) was newly readable this session (earlier 503 cleared) and corroborates the mortgage/"financial expropriation" illustration at the book level (pp. 146–7, 170), but the article itself remains unread. | **paid/library** — JSTOR or a Taylor & Francis institutional/library login |
| `research/miller-hoskins-college-town-lvt` (2026-07-18) | whether core campus buildings (Notre Dame in South Bend, Princeton University in Princeton) are included as taxable parcels in either report's underlying dataset — neither report's summary text says, and confirming it would require re-opening both source PDFs' parcel-level tables/GIS maps and cross-checking university-owned parcel IDs against each city's exemption rolls, not just re-reading the summary prose already used for the page. | **re-read primary** — both PDFs are already freely available (see page's Sources 2–3); needs a parcel-data-level pass, not a new source |
| `research/fernandez-milan-location-value-taxes` | **checked 2026-07-16:** author name confirmed ("Blanca Fernandez Milan," via CrossRef metadata — the task-brief spelling "Beatriz Fernández Milan" was wrong and has been corrected on the page). What remains open: the ScienceDirect version-of-record (DOI 10.1016/j.landusepol.2015.11.022) is still paywalled; a search this session (Scholar, ResearchGate, SSRN, MCC/TU Berlin author pages) found no further free copy beyond the DepositOnce postprint already used, so possible pagination differences between postprint and version-of-record are unverified. | **paid/library access** — ScienceDirect or a university proxy |
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
- `benefits/taxing-land-raises-productivity` (2026-07-18) — a genuine search found **no** modern study directly testing George's wage-competition or efficiency-wage mechanism against a land-tax shift specifically; adjacent literature (general efficiency-wage studies, density/agglomeration-wage work) tests a different claim. Only re-open if such a study is published.
- `research/walks-toronto-income-polarization` (2026-07-18) — the NCRP's own complete publications list (2005–2021, the authoritative source for the partnership's own output) shows no "Part II" follow-up to the 2016 Research Paper 238; only re-open if one is published.
- `research/pistor-code-of-capital` (2026-07-14) — **closed via alternate channels, not the book itself**: no archive.org copy or Google Books preview of *The Code of Capital* exists (checked this session). Direct page citations (pp. 4, 86, 93, 229, 317–318) were obtained instead via two reliable channels quoting/restating the book's own text with confirmable pages: Pistor's own 2021 *Social & Legal Studies* rejoinder essay (her own words, read in full) and a Jotwell law-review quoting the book verbatim with page numbers. The 297-page book itself is still not read cover-to-cover — re-open only if a claim beyond what's now cited (e.g. the sovereign-debt or IP chapters' internal argument) needs checking.

## How to work this ledger
1. Obtain a source (paid/library now approved) → verify the specific claim on the page → replace the provenance caveat with a proper citation → delete the row here.
2. Book arrivals also update `sources/wanted-books.md`.
3. Live in-page markers (if any are re-introduced) are still tracked by `scripts/verification_queue.py` → `sources/verification-queue.md`; this ledger covers the items that were resolved-to-caveat and thus no longer carry a marker.
