---
title: "Mass Appraisal Methods"
category: concepts
tags: [concepts, assessment, cama, hedonic-regression, valuation, lvt]
stub: false
excerpt: "The statistical toolkit — computer-assisted mass appraisal, hedonic regression, and cooperative-game separation methods — used by assessors to estimate land value separately from building value at scale."
last_reviewed: 2026-07-10
---

## Definition

**Mass appraisal** is the practice of valuing many properties simultaneously, on a common valuation date, using standardized statistical methods rather than individual expert appraisals. **Computer-assisted mass appraisal (CAMA)** systems apply **hedonic regression** — modeling a property's sale price as a function of its location, lot size, structure characteristics, and other measurable attributes — to estimate land and building components separately across an entire jurisdiction. Because location dominates the pricing of otherwise-similar parcels, these systems can isolate the land component even where few or no unimproved lots actually sell.[1]

More recent refinements include cooperative-game approaches. A **Shapley-value method** for allocating a combined sale price between land and structure offers a principled, replicable way to perform land/building separation, formalizing what has historically been an assessor's judgment call.[2]

## Core Methods

### Hedonic Regression

Hedonic regression treats a property's sale price as the sum of implicit prices for its individual characteristics. Land-related attributes — location, lot size, frontage, topography, zoning — are modeled alongside structure-related attributes — square footage, age, condition, number of rooms. The regression coefficients on land-related variables yield an estimated land value surface across the jurisdiction, even when most transactions involve improved parcels.[1]

This approach is standard in modern assessment practice. The IAAO's *Standard on Mass Appraisal of Real Property* (2017) — the assessing profession's consensus standard — notes that "Multiple regression analysis (MRA) and related techniques have been successfully used" in valuation and directs that sale data be maintained for "the development of land values."[8] Production examples include Philadelphia, whose Office of Property Assessment reports that its "CAMA system, iasWorld, went live in February 2020" (iasWorld is a Tyler Technologies product) and calls implementing a CAMA system "an industry best practice";[9] and Cook County (Chicago), whose assessor publishes an open-source machine-learning CAMA model "used to generate initial assessed values for single- and multi-family residential properties in Cook County."[10]

### Residual and Comparable-Sales Methods

Three traditional methods for isolating land value remain foundational and are formalized within the CAMA framework:

- **Comparable vacant-lot sales:** where unimproved lots do sell, their prices directly indicate land value for nearby parcels.
- **Teardown sales:** when a buyer purchases a property and demolishes the structure, the purchase price approximates land value (minus demolition cost), providing a land-value signal even in built-up areas.
- **Residual estimation:** land value equals sale price minus the depreciated cost of the structure, estimated from construction-cost data and depreciation schedules.[1]

[Lars Doucet](/wiki/doucet-does-georgism-work/) argues that these methods work because land value is **spatially smooth** — neighbouring parcels have similar land values — whereas building value varies house-by-house. That smoothness means location-based methods can estimate land value with accuracy comparable to or better than whole-property assessment, which must also value the more heterogeneous building component.[1]

### Cooperative-Game (Shapley-Value) Separation

Özdilek (2020) proposes a cooperative-game approach in which a property's combined sale price is allocated between land and structure using **Shapley values** — a concept from cooperative game theory that distributes a coalition's total value among its members according to their marginal contributions. Applied to land/building separation, this method treats land and structure as complementary "players" whose combined value exceeds either alone, and assigns each a share based on its incremental contribution to total property value.[2]

This method offers a replicable, axiomatically grounded alternative to ad hoc residual estimation, but no assessment jurisdiction is known to have adopted it in production. The 2020 paper that proposed it validated the approach only as an empirical case study — on 14,715 residential sales across Montreal's 27 districts — rather than in an operational assessment roll,[2] and a 2025 follow-up applying game theory to cadastral valuation states plainly that for the land/building split "there are no established methods" and that its own game-theoretic approach "is new in the theory and practice of valuation."[13]

## Why It Matters for LVT

Mass appraisal is the practical answer to the [objection that land value can't be assessed](/wiki/land-cannot-be-assessed/): assessors do not need a pure land sale next to every parcel, because the spatial smoothness of land values lets statistical methods interpolate from available data points across a jurisdiction.[1]

The [Lincoln Institute of Land Policy](/wiki/lincoln-institute/)'s standard policy reference on land value taxation, by Dye & England (2010), treats assessment methodology — including these techniques — as an implementation question to be addressed with better tools and investment, rather than a fundamental barrier to a [land value tax](/wiki/land-value-tax/).[3] The report surveys experience across more than 30 countries and US municipalities, including the [Pennsylvania](/wiki/pennsylvania/) split-rate cities, and covers assessment methods, transition issues, and the political economy of adoption.[3]

## Existing Practice at Scale

Separate land-value assessment is not merely theoretical. Several jurisdictions already assess land values separately as routine practice:

- **[Estonia](/wiki/estonia/)** has levied a land value tax since 1993, requiring land-only assessments nationwide — national valuations were carried out in 1993, 1996, and 2001, moving to mass-valuation models with value zones.[12]
- **[Denmark](/wiki/denmark/)** operates a *grundskyld* (land tax) assessed on land value separately from buildings.[4]
- Several **[Australian](/wiki/new-south-wales/) states**, including [New South Wales](/wiki/new-south-wales/) (land tax since 1895 on unimproved capital value), assess land value separately as a matter of long-standing practice.[5]
- Most US assessments already publish a land/improvement split, though the quality and methodology of that split varies widely across jurisdictions.[4]

[New Zealand](/wiki/new-south-wales/)'s historical use of land-value rating as a primary local government funding mechanism provides another significant case, and the country's gradual shift from land-value to capital-value rating bases has given researchers a quasi-natural experimental setting for studying the effects of the assessment base choice.[6]

## Assessment Quality and Error

Because land is immobile and visible, gross mis-assessment is relatively easy to challenge through appeal processes. Assessment quality improves with investment in data, methodology, and professional capacity — a focus of the [Center for Land Economics](/wiki/center-for-land-economics/), co-founded by [Lars Doucet](/wiki/doucet-does-georgism-work/).[4]

The key insight from the assessment literature is that land-value assessment errors are **bounded and contestable** in ways that many other tax-base errors are not: land cannot be hidden, moved offshore, or recharacterized as another asset class. Under-assessment, not evasion, is the primary practical risk — a concern addressed in the wiki's [tax-you-can't-dodge](/wiki/the-tax-you-cant-dodge/) narrative.[4]

## Limits and Open Questions

- **Data quality varies by jurisdiction.** CAMA systems require transaction data, structure characteristics, and geographic information; jurisdictions with poor records or few arm's-length sales face greater estimation uncertainty. Berry (2021), regressing sale prices against assessed values in 2,628 US counties, found an average county-level r-squared of just .46 with an interquartile range of .25 to .67, concluding: "Clearly, there is variation in performance across assessors, but there is a great deal of unexplained variation in sale prices in the vast majority of jurisdictions."[11] The same study finds assessments "typically regressive," with bottom-decile homes assessed at roughly twice the ratio to sale price of top-decile homes within a jurisdiction — though this concerns whole-property assessment, the current baseline against which land assessment would be compared.[11]
- **The land/building split is hardest in dense, built-up areas.** Dye & England note that "traditional methods of assessing land values in developed urban areas have various drawbacks": the common abstraction (residual) method requires "subjective judgments" to extract land value, and the allocation method "makes the arbitrary assumption that land values are the same fixed percentage of total value" for every property.[3] Doucet reports the same difficulty for statistical methods: in the Berlin studies he reviews, nonparametric kernel interpolation from pure land sales was "not able to produce estimates for the city center, only the outlying areas," which is what motivates semiparametric methods that add building characteristics to the model.[1]
- **Shapley-value and other advanced methods remain largely academic.** Operational adoption of cooperative-game separation methods in assessment practice has not been documented in the sources reviewed here.[2]
- **Agricultural and peri-urban land** presents special challenges where planning-permission value creates a large gap between use-value and market value — a concern noted in the [Mirrlees Review](/wiki/mirrlees-review/) and relevant to the [farmer impact objection](/wiki/lvt-hurts-farmers/).[7]

## See Also

- [Objection: Land value can't be assessed accurately](/wiki/land-cannot-be-assessed/)
- [Land Value Tax](/wiki/land-value-tax/)
- [Site Value](/wiki/site-value/)
- [Split-Rate Taxation](/wiki/split-rate-taxation/)
- [Research: Dye & England, Assessing the Theory and Practice of Land Value Taxation](/wiki/dye-england-assessing-lvt/)
- [Research: Doucet, Does Georgism Work?](/wiki/doucet-does-georgism-work/)
- [Center for Land Economics](/wiki/center-for-land-economics/)

## Sources

1. Lars Doucet (2022), "Does Georgism Work? Part 3: Can Unimproved Land Value Be Accurately Assessed?", *Astral Codex Ten* — [wiki summary](/wiki/doucet-does-georgism-work/) · [original](https://www.astralcodexten.com/p/does-georgism-work-part-3-can-unimproved) — used for the claim that land's spatial smoothness lets comparable-sales, teardown-sale, and residual methods estimate land value at accuracy comparable to or better than whole-property assessment; and for the hedonic regression framework description.
2. Ünsal Özdilek (2020), "Land and building separation based on Shapley values," *Humanities and Social Sciences Communications* (Nature), DOI 10.1057/s41599-020-0444-1. [Article](https://www.nature.com/articles/s41599-020-0444-1) — used for the cooperative-game (Shapley-value) formalisation of land/building value separation, verified as an empirical case study on 14,715 Montreal residential sales rather than an operational deployment (author confirmed as Ü. Özdilek, sole corresponding author, 2026-07-10).
3. Richard F. Dye & Richard W. England (2010), *Assessing the Theory and Practice of Land Value Taxation*, Lincoln Institute of Land Policy — [wiki summary](/wiki/dye-england-assessing-lvt/) · [Report](https://www.lincolninst.edu/publications/policy-focus-reports/assessing-theory-practice-land-value-taxation/) — used for framing assessment methodology as a practical implementation issue and for the survey of international and US experience.
4. Lars Doucet (2022), "Does Georgism Work? Part 3" — as summarised on the wiki's [assessment objection page](/wiki/land-cannot-be-assessed/) — used for the Denmark and Australia examples, the claim that most US assessments publish a land/improvement split, and the Center for Land Economics reference. (An earlier draft also attributed the Estonia example to this article; Estonia does not appear in it — the Estonia claim is now sourced to [12].)
5. Robert Andelson, ed. (2001), *Land-Value Taxation Around the World* — [wiki summary](/wiki/andelson-lvt-around-the-world/) — used for the comparative survey of site value rating in Australia and New Zealand, including NSW's land tax on unimproved capital value since 1895.
6. Gemmell, Grimes & Skidmore (2019), "Do Local Property Taxes Affect New Building Development?", *Journal of Housing Economics* — [wiki summary](/wiki/gemmell-grimes-skidmore-nz/) — used for New Zealand's land-value vs capital-value rating distinction and the Auckland quasi-natural experiment.
7. James Mirrlees et al. (2011), *Tax by Design: The Mirrlees Review*, Institute for Fiscal Studies — [wiki summary](/wiki/mirrlees-review/) — used for the agricultural/development value gap concern relevant to assessment difficulty.
8. International Association of Assessing Officers (2017), *Standard on Mass Appraisal of Real Property*, approved July 2017. [PDF](https://www.iaao.org/wp-content/uploads/StandardOnMassAppraisal.pdf) — used for the professional-consensus status of mass appraisal, the successful use of multiple regression analysis, and the requirement to maintain sale data for developing land values.
9. City of Philadelphia, Office of Property Assessment (2023), *Mass Appraisal Valuation Methodology Overview, Tax Year 2023*. [PDF](https://www.phila.gov/media/20220525080608/tax-year-2023-mass-appraisal-valuation-methodology.pdf) — used for the production example of the iasWorld CAMA system (live February 2020) and the characterisation of CAMA as industry best practice.
10. Cook County Assessor's Office, *Residential Automated Valuation Model* (model-res-avm), public code repository. [GitHub](https://github.com/ccao-data/model-res-avm) — used for the production example of an open-source machine-learning CAMA model generating initial assessed values for Cook County residential property.
11. Christopher Berry (2021), "Reassessing the Property Tax," University of Chicago, Harris School of Public Policy, working paper. [PDF](https://law.yale.edu/sites/default/files/area/center/corporate/spring2022_paper_berrychristopher_2-24-22.pdf) — used for systematic evidence on assessment accuracy variation across 2,628 US counties (county-level r-squared averaging .46) and on the regressivity of existing whole-property assessments.
12. Tambet Tiits, "Current Situation and Practice of Land Valuation and Taxation in Estonia" (Lincoln Institute of Land Policy). [PDF](https://www.lincolninst.edu/app/uploads/2024/04/tiits_current_situation_and_practice_in_estonia_0.pdf) — used for Estonia's Land Tax Act (levied on the value of land, national collection) and the 1993/1996/2001 national land valuations with value-zone mass-valuation models (verified against the PDF, 2026-07-10).
13. Michael Laskin (2025), "The method for the land plot value appraisal as part of the single real estate object, based on game theory approach," *Business Informatics*, DOI 10.17323/2587-814x.2025.1.93.107 — used to corroborate that game-theoretic (Shapley) land/building separation remains a research method: the paper states there "are no established methods" for the split and that its own approach "is new in the theory and practice of valuation" (verified via abstract/introduction, 2026-07-10).
