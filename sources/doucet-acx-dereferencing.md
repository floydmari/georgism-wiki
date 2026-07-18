# Doucet ACX "Does Georgism Work?" — Parts 1 & 3 de-referencing

**Wave:** T2 READ&MINE, 2026-07-18. **Method:** live fetch of both essays (no Wayback
needed — both load directly), full-text link enumeration, diffed against
`sources/registry.csv` by author/title. Supersedes and formalizes the earlier informal
audit at `sources/inbox/T1-TODO-doucet-parts-1-3-dereferencing.md` (2026-07-11), whose
findings this file confirms and refreshes against the current registry state — most of
its "MISSING" items had already been ingested by the time this wave ran.

- Part 1, "Is Land Really A Big Deal?" — <https://www.astralcodexten.com/p/does-georgism-work-is-land-really>
- Part 3, "Can Unimproved Land Value Be Accurately Assessed Separately From Buildings?" — <https://www.astralcodexten.com/p/does-georgism-work-part-3-can-unimproved>

Scope: every link to a scholarly/empirical source (papers, books, datasets, official
statistical reports, institutional standards). Excluded as non-scholarly and not
re-litigated here: generic definitional links (Wikipedia, Investopedia), live pricing
tools (Zillow/Redfin/CBRE), and Doucet's own back-of-envelope arithmetic inputs (raw
government data series he plugs into his own calculations rather than third-party
findings he is citing) — these are listed at the bottom of each section for completeness
but carry no ingest verdict.

**Totals:** 50 distinct scholarly works enumerated (Part 1: 25; Part 3: 26 rows, of which
one — the Arnott & Stiglitz Henry George Theorem origin paper — is a cross-part duplicate
already counted under Part 1, so 25 net-new). **Already in registry before this wave: 33.
Added this wave: 12. Rejected (fails registry bar): 5.** (Doucet's own back-of-envelope
data inputs and industry trackers are listed at the end of each section for completeness
but are not counted as "citations" in these totals.)

---

## Part 1 — "Is Land Really A Big Deal?"

| # | Citation | Registry status (pre-wave) | Verdict |
|---|----------|----------------------------|---------|
| 1 | Barr, Smith & Kulkarni (2018), *What's Manhattan Worth? A Land Values Index from 1950 to 2014*, Regional Science and Urban Economics 70 | **HAVE** — page `barr-smith-kulkarni-manhattan-land` | Already ingested (2026-07-11 wave) |
| 2 | Albouy, Ehrlich & Shin (2018), *Metropolitan Land Values* | **HAVE** — page `albouy-ehrlich-shin-metro-land` | — |
| 3 | Larson (2015), *New Estimates of the Value of Land of the United States* (BEA WP2015-3) | **HAVE** — page `larson-us-land-value` | — |
| 4 | Davis, Larson, Oliner & Shui (2019/2021), FHFA cost-approach land estimates | **HAVE** — page `davis-larson-oliner-shui-fhfa-land` | — |
| 5 | Federal Reserve Z1 / Yglesias's ~$24T method (Slate, 2013) | **HAVE** — folded into `davis-larson-oliner-shui-fhfa-land` | No standalone row needed |
| 6 | Dwyer (2003), *The Taxable Capacity of Australian Land and Resources* | **HAVE** — page `dwyer-taxable-capacity-australia` | — |
| 7 | Kuminoff & Pope (2013), *Value of Residential Land and Structures* | **HAVE** — page `kuminoff-pope-land-values` | Research page's own citation ledger was stale on this; corrected by the 2026-07-11 wave |
| 8 | Jordà, Schularick & Taylor, *The Great Mortgaging* (NBER WP 20501) | **HAVE** — registry row (Academic Paper) | — |
| 9 | Hudson (2001), *Where Did All the Land Go?* | **HAVE** — page `hudson-where-did-all-the-land-go` | — |
| 10 | Arnott & Stiglitz (1979), *Aggregate Land Rents, Expenditure on Public Goods, and Optimal City Size* (HGT origin) | **HAVE** — page `arnott-stiglitz-henry-george-theorem` | Cited again in Part 3 as the HGT origin paper; not double-counted |
| 11 | Tideman, Kumhof, Hudson & Goodhart (2021), *Post-Corona Balanced-Budget Super-Stimulus* | **HAVE** — page `goodhart-stimulus` | — |
| 12 | Rognlie (2015), *Deciphering the Fall and Rise in the Net Capital Share* | **HAVE** — page `rognlie-capital-share` | — |
| 13 | Artola Blanco, Bauluz & Martínez-Toledano, *Wealth in Spain, 1900–2014* (WID working paper) | **HAVE** — registry row, Light | — |
| 14 | Saez & Zucman (2016), *Wealth Inequality in the United States since 1913* | **HAVE** — registry row (important) | — |
| 15 | Ebeling (2015), *There Is No Social Security Santa Claus* (fff.org) | **HAVE** — registry row, supplementary | — |
| 16 | Cord (1985), *How Much Revenue Would a Full Land Value Tax Yield?* (AJES 44(3)) | **HAVE** — registry row, supplementary | Headline is 28% of 1981 national income; Doucet/Smith render it ~24% — conflation already documented on `land-rent-could-fund-government` |
| 17 | *Counting Bounty* (Jeffrey J. Smith, 2020) | **HAVE** — page `land-rent-could-fund-government` | Source of the Foldvary/Tideman/Gaffney/Cord/Ebeling data points |
| 18 | Lincoln Institute land-values data toolkit | **HAVE** — registry rows (dataset + org) | — |
| 19 | PLACES Lab machine-learning land-value maps → Nolte (2020), *High-Resolution Land Value Maps Reveal Underestimation of Conservation Costs*, PNAS 117(47) | **HAVE** — registry rows | — |
| 20 | AEI Land Price and Land Share Indicators (dataset + methodology) | **HAVE** — page `aei-land-price-indicators` | — |
| 21 | McKinsey Global Institute (2021), *The Rise and Rise of the Global Balance Sheet* | **HAVE** — registry row + page `mckinsey-global-balance-sheet` | — |
| 22 | Piketty, *Capital in the Twenty-First Century* | **HAVE** — registry row (core) | — |
| 23 | Positive Money, UK bank-lending-by-sector breakdown | **HAVE** — registry row, supplementary | Used here for a different figure than its usual wiki context; no action needed |
| 24 | Gaffney (2005), *The Physiocratic Concept of ATCOR* (WP096) | **HAVE** — page `atcor` | Attributed theory, not an empirical result |
| 25 | **UK Office for National Statistics, *UK National Accounts, The Blue Book: 2017*** — land ≈ half of UK real assets | **MISSING** | **ADDED** this wave (Report, supplementary). Registry row only — the claim it supports (UK land ≈ half/three-fifths of net worth) is already better evidenced on `places/united-kingdom.md` via a more recent (March 2022) ONS blog release with the same finding updated to £6.3T/"nearly three-fifths"; no page needed, the 2017 edition is a superseded vintage of the same series. |

**Not scholarly citations — Doucet's own arithmetic inputs / industry data trackers, no ingest:** USDA farmland value report (NASS); Federal Reserve flow-of-funds portal (Z1); CBO 2019 federal budget; NASBO state expenditure report; Tax Policy Center state-local finance data; federal budget receipts/outlays (presidency.ucsb.edu, govinfo.gov); Arbor Q1 2021 rental-investment cap-rate report; CBRE cap-rate survey; Reserve Bank of New Zealand bank-asset dashboard; APTA transit real-estate value study (a trade-association report; the transit-uplift claim it illustrates is already far better evidenced on the wiki via Gibbons & Machin — no ingest value added).

---

## Part 3 — "Can Unimproved Land Value Be Accurately Assessed Separately From Buildings?"

| # | Citation | Registry status (pre-wave) | Verdict |
|---|----------|----------------------------|---------|
| 1 | Gwartney, *Assessing Land Values — Principles and Methods* (Henry George School seminar/essay) | **HAVE** — page `gwartney-estimating-land-values` | — |
| 2 | IAAO, *Standard on Mass Appraisal of Real Property* (2017) | **HAVE** — registry row, folded into `mass-appraisal-methods` | — |
| 3 | Hefferan & Boyd (2010), *Property taxation and mass appraisal valuations in Australia* | **HAVE** — page `hefferan-boyd-mass-appraisal-australia` | — |
| 4 | **Kolbe, Schulz, Wersing & Werwatz (2019)**, *Land Value Appraisal Using Statistical Methods* (Berlin, FORLand WP-07) | **HAVE** — page `kolbe-berlin-land-value-appraisal`, Scan Depth Heavy | The load-bearing Part-3 source (0.845 semiparametric / 0.704 kernel); Doucet's gloss confirmed faithful, with the standing nuance (already on the page) that 0.845 is a house-transactions-only subset from Kolbe et al. 2012 |
| 5 | Kolbe, Schulz, Wersing & Werwatz, *Identifying Berlin's land value map using adaptive weights smoothing* (Computational Statistics, 2015) | **HAVE** — registry row (important), folded into the Kolbe Berlin page as a marked companion section | — |
| 6 | Almy (2014), *Valuation and Assessment of Immovable Property* (OECD WP 19) | **HAVE** — page `almy-oecd-valuation-assessment` | ≈1%-of-receipts conflation already documented on the page |
| 7 | Bencure, Tripathi, Miyazaki, Ninsawat & Kim (2019), *iLVM* (BayBay City, Philippines) | **HAVE** — page `bencure-ilvm-baybay-philippines` | Sole developing-country case in the essay |
| 8 | Arnott & Stiglitz (1979) — cited again as the HGT origin paper | **HAVE** (see Part 1 #10) | Not double-counted |
| 9 | Gaffney, *The Hidden Taxable Capacity of Land: Enough and to Spare* | **HAVE** — registry row (core) | Further-reading link |
| — | Tideman, Kumhof, Hudson & Goodhart, *Post-Corona Balanced-Budget Super-Stimulus* — also listed in Part 3's "further reading" | **HAVE** (see Part 1 #11) | Cross-part duplicate, not re-numbered or re-counted |
| 10 | Christopher England, *Land and Liberty: Henry George and the Crafting of Modern Liberalism* (JHU Press, 2023) — cited by Doucet via its predecessor Georgetown PhD dissertation, *Land and Liberty: Henry George, the Single Tax Movement, and the Origins of 20th Century Liberalism* | **HAVE** — registry row (important), same author's published-book form | The dissertation is a distinct document from the book but by the same author on the same subject; no separate row — an editor should confirm the book supersedes the thesis rather than adding a name-collision duplicate |
| 11 | **Gloudemans & Almy (2011), *Fundamentals of Mass Appraisal*** (IAAO textbook) | **MISSING** | **ADDED** this wave (Modern Book, important). **Top page candidate** — the methods backbone (market/cost/income approaches; MRA) that both Gwartney and Kolbe presuppose; no free full text (IAAO store item), so any page would summarize from reviews/excerpts and flag the paywall |
| 12 | **Fuest, Immel, Meier & Neumeier (2018)**, *Die Grundsteuer in Deutschland: Finanzwissenschaftliche Analyse und Reformoptionen* (ifo Institute monograph) | **MISSING** | **ADDED** this wave (Report, supplementary). Distinct from the `fuest-peichl-siegloch-incidence` wage-incidence paper already on the wiki — same lead author, different work; do not conflate |
| 13 | **Kilić, Rogulj & Jajac (2019)**, *Fuzzy expert system for land valuation in land consolidation processes* (Croatian Operational Research Review 10(1)) | **MISSING** | **ADDED** this wave (Academic Paper, supplementary). Tail case study; registry row only |
| 14 | **Yalpır & Ünel (2017)**, *Use of Spatial Analysis Methods in Land Appraisal; Konya Example* (ISITES2017 conference) | **MISSING** | **ADDED** this wave (Academic Paper, supplementary). Tail case study; registry row only |
| 15 | **Raslanas, Zavadskas, Kaklauskas & Zabulėnas (2010)**, *Land value tax… Part II: … the case of Vilnius* (Intl. J. Strategic Property Management 14(2)) | **MISSING** | **ADDED** this wave (Academic Paper, supplementary). Note: Doucet's essay dates this "2014"; the paper is actually **2010** — flagging the discrepancy rather than propagating it |
| 16 | **Aragonés-Beltrán, Aznar, Ferrís-Oñate & García-Melón (2008)**, *Valuation of urban industrial land: An analytic network process approach* (European Journal of Operational Research 185(1)) | **MISSING** | **ADDED** this wave (Academic Paper, supplementary). The AHP/ANP expert-weighted method case; registry row only |
| 17 | **Xue et al. (2008)**, *Land evaluation based on Boosting decision tree ensembles* | **MISSING** | **ADDED** this wave (Academic Paper, supplementary), author list incomplete — [VERIFY: full byline unconfirmed beyond "Xue et al." as Doucet cites it and the ResearchGate record title]. Tail ML case study |
| 18 | **Kettani & Khelifi (2001)**, *PariTOP: A goal programming-based software for real estate assessment* (European Journal of Operational Research 133(2)) | **MISSING** | **ADDED** this wave (Academic Paper, supplementary). Tail case study; registry row only |
| 19 | **IAAO, *Standard on Ratio Studies*** | **MISSING** (distinct from the Mass Appraisal standard already on the wiki) | **ADDED** this wave (Report/Standard, supplementary). Canonical definitional source for "ratio study," used across `mass-appraisal-methods` and `land-cannot-be-assessed` |
| 20 | **IAAO, *Standard on Property Tax Policy*** | **MISSING** | **ADDED** this wave (Report/Standard, supplementary). Source for the "core principles" list Doucet quotes |
| 21 | **Gaffney, *The Unknown Revenue Potential of Land: Fifteen Hidden Elements*** (WP097, 2004) | **MISSING** | **ADDED** this wave (Academic Paper, supplementary). Further-reading pointer, not relied upon for a specific figure |
| 22 | Marshall & Swift, *Valuation Service* (CoreLogic cost manual) | **MISSING** | **REJECTED** — commercial cost-estimation manual for the *improvement* (building) side of valuation, not the land side; doesn't bear on the land-assessability claim lane this wiki tracks |
| 23 | Marshall & Swift, *Residential Cost Handbook* | **MISSING** | **REJECTED** — same reasoning as #22 |
| 24 | PriceWaterhouseCoopers (2006), state/local retail sales-tax compliance-cost report | **MISSING** | **REJECTED** — tangential IRS/sales-tax administrative-cost color, not a land-assessment finding |
| 25 | IRS budget & workforce statistics page | **MISSING** | **REJECTED** — Doucet's own input for an "army of assessors" cost comparison, not a third-party finding |
| 26 | University of California Academic Senate, standardized-testing task-force report | **MISSING** | **REJECTED** — off-topic aside (a testing-accuracy analogy), no connection to land, Georgism, or any wiki claim lane |

**Not scholarly citations — no ingest:** IAAO's general "core principles" framing repeats the two Standards above; no separate action.

---

## Top page candidates for a future wave (FIND only — not drafted this wave)

1. **Gloudemans & Almy, *Fundamentals of Mass Appraisal* (IAAO, 2011).** The textbook backbone underneath both Gwartney's and Kolbe's methodology — market/cost/income approaches, MRA — that the wiki currently only has at second hand. Highest-value single addition from this pass; note it is a paywalled IAAO store item, so a page would need to work from reviews/summaries and disclose that constraint per EDITORIAL §1 rule 6.
2. **IAAO *Standard on Ratio Studies* + *Standard on Property Tax Policy*.** Two short, canonical, freely-downloadable institutional standards that are the actual definitional source for "ratio study" and the objection-rate benchmarks already cited (via Hefferan & Boyd) on `mass-appraisal-methods` and `land-cannot-be-assessed` — currently only cited at second hand through Doucet and Hefferan & Boyd. A short joint page (or an expansion of the existing `mass-appraisal-methods` concept page with direct citations) would tighten sourcing on a Type F (definitional) claim.
3. **The Part-3 mass-appraisal case-study tail (Kilić 2019 / Yalpır & Ünel 2017 / Raslanas et al. 2010 / Aragonés-Beltrán et al. 2008 / Xue et al. 2008 / Kettani & Khelifi 2001), as a single comparative page.** Individually each is thin (one national case study apiece — Croatia, Turkey, Lithuania, Spain, an unspecified ML case, Quebec), but together they are the empirical breadth behind Doucet's "methods work in multiple countries" claim. A single synthesis page tabulating method / country / accuracy-metric across all six would out-perform six separate stub pages and is a natural next-wave EXPAND, not a FIND item.

---

## Counts summary

Row mentions across both tables: 25 (Part 1) + 27 (Part 3, including the unnumbered
Post-Corona cross-reference) = 52. Two of those Part-3 mentions (Arnott–Stiglitz, row 8;
Post-Corona, unnumbered) are duplicates of works already given their own row in Part 1,
leaving **50 distinct scholarly works** — the figure used throughout this file.

| | Part 1 | Part 3 (net of the 2 duplicates) | Total distinct works |
|---|---|---|---|
| Already in registry pre-wave | 24 | 9 | **33** |
| Added this wave | 1 | 11 | **12** |
| Rejected (fails registry bar) | 0 | 5 | **5** |
| **Total** | **25** | **25** | **50** |
