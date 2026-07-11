# T1 TODO — Doucet ACX "Does Georgism Work?" Parts 1 & 3 de-referencing

**Auditor:** T2 pass, 2026-07-11. **Read-only** except this file.
**Essays fetched OK** (live, no Wayback needed, no BLOCKED items):
- Part 1 "Is Land Really A Big Deal?" — https://www.astralcodexten.com/p/does-georgism-work-is-land-really
- Part 3 "Can Unimproved Land Value Be Accurately Assessed?" — https://www.astralcodexten.com/p/does-georgism-work-part-3-can-unimproved

**Scope:** every empirical citation Parts 1 & 3 actually lean on, diffed against `sources/registry.csv` and `research/`. Generic definitional links (Investopedia, Wikipedia, YIMBY, Kelley Blue Book), live pricing tools (Zillow/Redfin/CBRE cap-rate map), and one-off news/blog color links are excluded unless a number rests on them. Known Almy/Hefferan figure-conflations are already documented in `research/doucet-does-georgism-work.md` and are **not** re-litigated here.

**Headline finding:** the diff is *much* better than `research/doucet-does-georgism-work.md` claims. That page's "not yet on the wiki" lists (both the Part-1 and Part-3 ledgers) are **stale** — Kuminoff-Pope, Hudson (*Where Did All the Land Go?*), Kolbe, Hefferan-Boyd, and Almy all now have full research pages + registry rows. See the CONFLICTS section; the real remaining gap is ~7 load-bearing sources plus a tail of minor case studies.

---

## Counts
- **Empirical citations enumerated:** 34 (Part 1: 18; Part 3: 16)
- **HAVE-page:** 17
- **HAVE-registry-row-only:** 2 (McKinsey Global Balance Sheet; Lincoln Institute land-values dataset)
- **MISSING (no row):** 15

---

## Part 1 — "Is Land Really A Big Deal?" citation ledger

| # | Source | What Doucet uses it for | Registry status | Notes / ingest verdict |
|---|--------|-------------------------|-----------------|------------------------|
| 1 | Krugman, PSMag interview (2013) | The framing foil: theory OK but "not a big enough thing" | n/a (quote) | Rhetorical anchor, not empirical. No ingest. |
| 2 | **AEI Land Price Indicators** (aei.org/housing) + methodology PDF | SF county **70.9%** land-share; the empirical backbone of "most urban value is land" | **MISSING** | **INGEST — high.** Live, methodologically-documented dataset; the county land-share figure is load-bearing for his headline claim. Registry row (Dataset, important). |
| 3 | **Barr, Smith & Kulkarni (2018)**, *What's Manhattan Worth?* (Regional Science and Urban Economics 70) | An aggregate-land-value data point in the $19–65T span | **INGESTED 2026-07-11** → /wiki/barr-smith-kulkarni-manhattan-land/ | **INGEST — high.** Peer-reviewed; one of the twelve estimation methods. Registry row + short page, important. |
| 4 | Albouy, Ehrlich & Shin (2018), *Metropolitan Land Values* (+ online appendix) | Preferred vacant-land-sales estimate; dense pure-land sales | **HAVE-page** `albouy-ehrlich-shin-metro-land` | — |
| 5 | Larson (2015), *New Estimates of the Value of Land of the US* (BEA) | Hedonic aggregate land estimate | **HAVE-page** `larson-us-land-value` | — |
| 6 | Davis, Larson, Oliner & Shui (2019), FHFA | Cost-approach estimate (vacant-land sales excluded) | **HAVE-page** `davis-larson-oliner-shui-fhfa-land` | — |
| 7 | Federal Reserve Z1 flow-of-funds / Yglesias method (Slate 2013) | The ~$24T "conservative lower bound" | **HAVE-page** (folded into `davis-larson-oliner-shui-fhfa-land`) | Yglesias's Slate write-up has no standalone row; adequately covered. |
| 8 | Lincoln Institute land-values data toolkit | One of the twelve estimation methods (cost approach) | **HAVE-registry-row-only** (Lincoln Institute dataset + org) | Dataset row exists; no dedicated de-ref page needed. |
| 9 | **PLACES Lab** ML fair-market-value estimate (placeslab.org) | A machine-learning aggregate land estimate | **INGESTED 2026-07-11** (registry row → /wiki/land-rent-could-fund-government/) | **VERIFIED.** PLACES lab = research group in Dept. of Earth & Environment, Boston University, led by assoc. prof. **Christoph Nolte**. Doucet links `placeslab.org/fmv_usa/`; there IS a peer-reviewed paper behind it: Nolte (2020), *High-resolution land value maps reveal underestimation of conservation costs in the US*, **PNAS 117(47):29577–29583**, doi 10.1073/pnas.2012865117. Registry row (Dataset, supplementary). |
| 10 | *Counting Bounty* (Jeffery J. Smith, 2020) | ~$44T upper bound; source of Foldvary/Tideman/Gaffney/Cord/Ebeling data points | **HAVE-page** `land-rent-could-fund-government` | — |
| 11 | Dwyer (2003), *Taxable Capacity of Australian Land* | Recomputed to ~21%; "Foldvary contradicted by own source" | **HAVE-page** `dwyer-taxable-capacity-australia` | — |
| 12 | **Steven Cord** ~24%-of-national-income estimate (cooperative-individualism.org) | A US rent-share-of-income data point | **INGESTED 2026-07-11** (registry row → /wiki/land-rent-could-fund-government/) | **VERIFIED — with a figure caveat.** Actual paper: Steven Cord, *How Much Revenue Would a Full Land Value Tax Yield? …It Would Nearly Equal All Taxes*, **AJES 44(3) (Jul. 1985), 279–293** (full PDF on cooperative-individualism.org). Method: capitalises 1981 Census-Bureau + Federal-Reserve assessed land values (adjusted for under-assessment, tax-exempt land, federal holdings) at ~14%. Headline result: full land-rent tax ≈ **$658B ≈ 28% of 1981 national income** — *not* 24%; the ~24% is Smith's/Doucet's rendering via *Counting Bounty*. Registry row (Paper, supplementary). |
| 13 | **Richard Ebeling** (2015) federal land+mineral holdings ~$5.5T | A land-value data point (via Smith) | **INGESTED 2026-07-11** (registry row → /wiki/land-rent-could-fund-government/) | **VERIFIED.** Doucet's essay hyperlinks the "$5.5 trillion" to the actual source: Richard M. Ebeling, *There Is No Social Security Santa Claus*, **Future of Freedom Foundation (fff.org), 21 Dec 2015** — "federal land and the mineral reserves may have, in 2015, an estimated total value of about $5.5 trillion." Reaches Doucet second-hand via *Counting Bounty* (Smith extrapolates to $6.6T for 2020). Doucet himself discounts it as method-free, but it is a real, citable artifact → registry row (Article, supplementary). |
| 14 | Kuminoff & Pope (2013), *Value of Residential Land and Structures* | Hedonic-regression method | **HAVE-page** `kuminoff-pope-land-values` | ⚠ research page still lists this as "not yet on the wiki" — STALE. |
| 15 | Hudson (2001), *Where Did All the Land Go?* | The Fed-critique Doucet leans on | **HAVE-page** `hudson-where-did-all-the-land-go` | ⚠ research page still lists as "not yet on the wiki" — STALE. |
| 16 | Gaffney (2005), *Physiocratic Concept of ATCOR* | Attributed theory (ATCOR) | **HAVE-page** `atcor` | Attributed hypothesis, not result. |
| 17 | Arnott & Stiglitz (1979), HGT / Tideman correspondence | Attributed theory (Henry George Theorem) | **HAVE-page** `arnott-stiglitz-henry-george-theorem` (+ `arnott-hgt-practical-guide`) | — |
| 18 | Tideman, Kumhof, Hudson & Goodhart (2021), *Post-Corona Super-Stimulus* | The worked-out policy paper | **HAVE-page** `goodhart-stimulus` | — |

**Part-1 supporting empirics also cited (bank-loans / capital-share / concentration sections):**

| # | Source | Use | Status | Verdict |
|---|--------|-----|--------|---------|
| 19 | Jordà, Schularick & Taylor (2014), *The Great Mortgaging* | Land as large share of bank loans | **HAVE-page** `great-mortgaging` | — |
| 20 | Rognlie (2015), *Deciphering the Fall and Rise in the Net Capital Share* | Housing/land drives capital-share rise | **HAVE-page** `rognlie-capital-share` | — |
| 21 | Piketty, *Capital in the 21st Century* | Wealth-in-land framing | **HAVE-page** `piketty-capital-21st-century` | — |
| 22 | **Artola Blanco et al., *Wealth in Spain 1900–2014*** (WID working paper) | Land = large share of national wealth (Spain 55%/61%) | **MISSING** | INGEST — low/medium. Registry row (Paper, supplementary). |
| 23 | **Tideman et al. "big paper"** (SSRN 3960235) | OECD non-produced-asset share of US household wealth chart | **MISSING** (distinct from goodhart-stimulus 3954888 & losses-of-nations) | INGEST — medium. Verify identity; likely folds into existing Tideman coverage but wants its own row. |
| 24 | **McKinsey Global Institute (2021), *Rise and Rise of the Global Balance Sheet*** | Global net worth / real-estate share | **HAVE-registry-row-only** (no page) | Page optional; row suffices unless it becomes a cited anchor elsewhere. |
| 25 | **Saez & Zucman (2015)** wealth-distribution data (eml.berkeley.edu) | Land-ownership concentration among the wealthy | **MISSING** | INGEST — medium. Heavily-cited primary; registry row (Paper, important). |

(Minor Part-1 raw-data links used in his own arithmetic — USDA farmland $3,160/acre; Statista 896.6M farm acres; FRED GNI; CBO/OMB budget tables; NYT billionaires; *Economist* "Paradox of Soil" — are Doucet's own back-of-envelope inputs, not third-party findings; no ingest.)

---

## Part 3 — "Can Unimproved Land Value Be Assessed?" citation ledger

| # | Source | What Doucet uses it for | Registry status | Notes / ingest verdict |
|---|--------|-------------------------|-----------------|------------------------|
| 26 | Gwartney, *Assessing Land Values — Principles and Methods* (HGS seminar/essay) | Land easier to value than buildings; residual method; ~690-staff BC anecdote; "wiggle room" quote | **HAVE-page** `gwartney-estimating-land-values` | — |
| 27 | IAAO standards (Property Tax Policy; Ratio Studies) | Ratio-study method; annual reassessment norm | **HAVE-page** (folded into `mass-appraisal-methods`) | Standards docs; no separate row needed. |
| 28 | **Kolbe, Schulz, Wersing & Werwatz (2019)**, *Land Value Appraisal Using Statistical Methods* (Berlin) | THE load-bearing Part-3 source: **0.845** semiparametric vs **0.704** kernel | **HAVE-page** `kolbe-berlin-land-value-appraisal` | ⚠ research page still lists as "not yet on the wiki" — STALE. Wiki confirms Doucet's gloss is faithful (0.845 is a house-transactions-only subset carried from Kolbe et al. 2012; both are correlations vs the expert BRW map). |
| 29 | **Kolbe et al., *Identifying Berlin's land value map using adaptive weights smoothing*** (Computational Statistics, 2015/16) | The AWS method behind the semiparametric surface | **MISSING** (partially folded into #28's page) | **INGEST — medium-high.** The methodological companion; warrants its own registry row (and a short page feeding `mass-appraisal-methods`). |
| 30 | Hefferan & Boyd (2010), *Property taxation and mass appraisal valuations in Australia* | <2% / <1% objection-rate benchmark | **HAVE-page** `hefferan-boyd-mass-appraisal-australia` | ⚠ research page still lists as "not yet on the wiki" — STALE. Conflation already documented. |
| 31 | Almy (2014), *Valuation and Assessment of Immovable Property* (OECD WP 19) | ~€20/property cost (≈1% of receipts) | **HAVE-page** `almy-oecd-valuation-assessment` | ⚠ research page still lists as "not yet on the wiki" — STALE. ≈1% conflation already documented. |
| 32 | **Gloudemans & Almy (2011), *Fundamentals of Mass Appraisal*** (IAAO textbook) | The methods backbone (market/cost/income; MRA) | **MISSING** | INGEST — medium. Canonical IAAO reference; registry row (Book, supplementary/important). |
| 33 | **Bencure, Tripathi, Miyazaki, Ninsawat & Kim (2019), iLVM** (BayBay City, Philippines) | Developing-country evidence; ~67% of variance explained | **MISSING** | **INGEST — high.** The only developing-country mass-appraisal case in the essay; distinct evidentiary value for `mass-appraisal-methods` + `land-cannot-be-assessed`. Registry row + short page. |
| 34 | **Fuest et al. (2018), ifo *Grundsteuer* study** | Cost comparison of German property-tax reform options | **MISSING** (distinct from `fuest-peichl-siegloch-incidence`) | INGEST — low/medium. Registry row (Report, supplementary). ⚠ do not conflate with the Fuest-Peichl-Siegloch wage-incidence paper already on the wiki. |
| 35 | **Yalpir & Unel (2017)**, Konya MRA | A modern MRA case study | **MISSING** | INGEST — low. Registry row (Paper, supplementary). |
| 36 | **Kilić et al. (2019)** | Minor mass-appraisal case | **MISSING** | INGEST — low. Registry row only. |
| 37 | **Raslanas et al. (2014)** | Minor mass-appraisal case | **MISSING** | INGEST — low. Registry row only. |
| 38 | **Aragonés-Beltrán et al. (2008)**, AHP | Expert-weighted (AHP) method | **MISSING** | INGEST — low. Registry row only. |
| 39 | **Xue et al. (2008)**, boosting decision-tree ensembles | ML land-evaluation case | **MISSING** | INGEST — low. Registry row only. |
| 40 | **Kettani & Khelifi (2001)**, PariTOP | Goal-programming valuation software | **MISSING** | INGEST — low. Registry row only. |

**Minor / tangential Part-3 links (not ranked):** Marshall & Swift valuation manuals (cost-approach reference — MISSING, low, registry row only; note ≠ Alfred Marshall's *Principles*, which IS in registry); PriceWaterhouseCoopers 2006 sales-tax collection-cost report (MISSING, tangential IRS-cost color, no ingest). Part-3 "further reading" list re-cites already-HAVE sources (Post-Corona/`goodhart-stimulus`, Arnott-Stiglitz, Gaffney *Hidden Taxable Capacity*) plus a Georgetown *Land and Liberty* thesis (a DIFFERENT work from the Christopher England book already in registry — no ingest, further-reading only) and Gaffney's WP097 *Unknown Revenue Potential of Land* (MISSING, low — a further-reading pointer, not relied upon).

---

## MISSING shortlist — ranked by ingest value (feeds next wave)

1. **Barr, Smith & Kulkarni (2014), Manhattan land value** — peer-reviewed; a distinct point in Doucet's twelve-method aggregate-land-value span. → registry row + short page (important).
2. **AEI Land Price Indicators** (dataset + methodology PDF) — the 70.9% SF land-share figure is the empirical spine of his "most urban value is land" claim. → registry row (Dataset, important); a de-ref page if the number gets cited elsewhere.
3. **Bencure et al. (2019), iLVM (BayBay City)** — the sole developing-country mass-appraisal case in Part 3; unique evidentiary value for `mass-appraisal-methods` and `land-cannot-be-assessed`. → registry row + short page.
4. **Kolbe et al., adaptive-weights-smoothing companion (2015/16)** — the method behind the 0.845 semiparametric surface; currently only implicit in the Kolbe page. → its own registry row + short page feeding `mass-appraisal-methods`.
5. **Saez & Zucman (2015)** — the primary behind Part 1's land-ownership-concentration section; heavily citable across the wiki. → registry row (Paper, important).

*Second tier (registry rows, pages only if later load-bearing):* Gloudemans & Almy *Fundamentals of Mass Appraisal*; Fuest et al. ifo *Grundsteuer*; Tideman SSRN 3960235; Artola Blanco *Wealth in Spain*; McKinsey (already a row — consider a page); Steven Cord; PLACES Lab; Marshall & Swift. *Tail (rows only):* Yalpir & Unel, Kilić, Raslanas, Aragonés-Beltrán, Xue, Kettani. *No ingest:* Ebeling, PwC 2006, Georgetown *(Sustainability 11(13), MDPI) and Liberty* thesis, Doucet's own arithmetic-input links.

---

## Conflicts / drift flagged (flag, don't fix)

1. **`research/doucet-does-georgism-work.md` is materially STALE on both ledgers.** Its Part-1 note (line 48) lists Kuminoff-Pope and Hudson *Where Did All the Land Go?* as "not yet on the wiki"; its Part-3 ledger (lines 64–71) calls the Kolbe cluster, Hefferan-Boyd, and Almy "the substantive gap … none has its own registry row or page." All five now have full research pages **and** registry rows. The de-referencing those bullets ask for has already been done. The page's citation ledger should be refreshed (out of scope here; flagged for the editor).
2. **No new source-use conflicts found.** The two figure-conflations the task pre-flagged (Almy "≈1%" vs valuation-only-vs-total-admin; Hefferan "<1%-objection / <2%-complaint" collapsing one benchmark into two) are already documented on the respective pages and on the research page — not re-flagged. Doucet's Berlin 0.845/0.704 gloss is confirmed **faithful** to `kolbe-berlin-land-value-appraisal.md` (with the standing nuance, already on that page, that 0.845 is a house-transactions-only subset imported from Kolbe et al. 2012 and both are correlations vs the expert BRW map, not vs realised sale prices).
3. **Naming-collision hazard for the ingest wave:** two "Fuest" papers (Part-3 ifo *Grundsteuer* cost study ≠ the wage-incidence `fuest-peichl-siegloch-incidence` already on the wiki) and two "Marshall" entries (Marshall & Swift manual ≠ Alfred Marshall's *Principles* already on the wiki). Keep them distinct when creating rows.

---

## BLOCKED
None. Both essays fetched live on first attempt.
