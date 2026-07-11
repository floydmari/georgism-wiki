---
title: "Mass Appraisal Methods"
category: concepts
tags: [concepts, assessment, cama, hedonic-regression, valuation, lvt]
stub: false
excerpt: "The statistical toolkit — computer-assisted mass appraisal, hedonic regression, and cooperative-game separation methods — used by assessors to estimate land value separately from building value at scale."
last_reviewed: 2026-07-05
---

## Definition

**Mass appraisal** is the practice of valuing many properties simultaneously, on a common valuation date, using standardized statistical methods rather than individual expert appraisals. **Computer-assisted mass appraisal (CAMA)** systems apply **hedonic regression** — modeling a property's sale price as a function of its location, lot size, structure characteristics, and other measurable attributes — to estimate land and building components separately across an entire jurisdiction. Because location dominates the pricing of otherwise-similar parcels, these systems can isolate the land component even where few or no unimproved lots actually sell.[1]

More recent refinements include cooperative-game approaches. A **Shapley-value method** for allocating a combined sale price between land and structure offers a principled, replicable way to perform land/building separation, formalizing what has historically been an assessor's judgment call.[2]

## Core Methods

### Hedonic Regression

Hedonic regression treats a property's sale price as the sum of implicit prices for its individual characteristics. Land-related attributes — location, lot size, frontage, topography, zoning — are modeled alongside structure-related attributes — square footage, age, condition, number of rooms. The regression coefficients on land-related variables yield an estimated land value surface across the jurisdiction, even when most transactions involve improved parcels.[1]

This approach is standard in modern assessment practice and underlies most CAMA systems in use by large assessment jurisdictions. [CITATION NEEDED: specific jurisdiction or vendor examples of CAMA systems in production use]

### Residual and Comparable-Sales Methods

Three traditional methods for isolating land value remain foundational and are formalized within the CAMA framework:

- **Comparable vacant-lot sales:** where unimproved lots do sell, their prices directly indicate land value for nearby parcels.
- **Teardown sales:** when a buyer purchases a property and demolishes the structure, the purchase price approximates land value (minus demolition cost), providing a land-value signal even in built-up areas.
- **Residual estimation:** land value equals sale price minus the depreciated cost of the structure, estimated from construction-cost data and depreciation schedules.[1]

[Lars Doucet](/wiki/doucet-does-georgism-work/) argues that these methods work because land value is **spatially smooth** — neighbouring parcels have similar land values — whereas building value varies house-by-house. That smoothness means location-based methods can estimate land value with accuracy comparable to or better than whole-property assessment, which must also value the more heterogeneous building component.[1]

### Cooperative-Game (Shapley-Value) Separation

Kumar et al. (2020) propose a cooperative-game approach in which a property's combined sale price is allocated between land and structure using **Shapley values** — a concept from cooperative game theory that distributes a coalition's total value among its members according to their marginal contributions. Applied to land/building separation, this method treats land and structure as complementary "players" whose combined value exceeds either alone, and assigns each a share based on its incremental contribution to total property value.[2]

This method offers a replicable, axiomatically grounded alternative to ad hoc residual estimation, though its adoption in operational assessment practice appears limited as of the time of writing. [VERIFY: whether any assessment jurisdiction has implemented Shapley-value separation in production]

## Why It Matters for LVT

Mass appraisal is the practical answer to the [objection that land value can't be assessed](/wiki/land-cannot-be-assessed/): assessors do not need a pure land sale next to every parcel, because the spatial smoothness of land values lets statistical methods interpolate from available data points across a jurisdiction.[1]

The [Lincoln Institute of Land Policy](/wiki/lincoln-institute/)'s standard policy reference on land value taxation, by Dye & England (2010), treats assessment methodology — including these techniques — as an implementation question to be addressed with better tools and investment, rather than a fundamental barrier to a [land value tax](/wiki/land-value-tax/).[3] The report surveys experience across more than 30 countries and US municipalities, including the [Pennsylvania](/wiki/pennsylvania/) split-rate cities, and covers assessment methods, transition issues, and the political economy of adoption.[3]

## Existing Practice at Scale

Separate land-value assessment is not merely theoretical. Several jurisdictions already assess land values separately as routine practice:

- **[Estonia](/wiki/estonia/)** has levied a pure land value tax since 1993, requiring land-only assessments nationwide.[4]
- **[Denmark](/wiki/denmark/)** operates a *grundskyld* (land tax) assessed on land value separately from buildings.[4]
- Several **[Australian](/wiki/new-south-wales/) states**, including [New South Wales](/wiki/new-south-wales/) (land tax since 1895 on unimproved capital value), assess land value separately as a matter of long-standing practice.[5]
- Most US assessments already publish a land/improvement split, though the quality and methodology of that split varies widely across jurisdictions.[4]

[New Zealand](/wiki/new-south-wales/)'s historical use of land-value rating as a primary local government funding mechanism provides another significant case, and the country's gradual shift from land-value to capital-value rating bases has given researchers a quasi-natural experimental setting for studying the effects of the assessment base choice.[6]

## Assessment Quality and Error

Because land is immobile and visible, gross mis-assessment is relatively easy to challenge through appeal processes. Assessment quality improves with investment in data, methodology, and professional capacity — a focus of the [Center for Land Economics](/wiki/center-for-land-economics/), co-founded by [Lars Doucet](/wiki/doucet-does-georgism-work/).[4]

The key insight from the assessment literature is that land-value assessment errors are **bounded and contestable** in ways that many other tax-base errors are not: land cannot be hidden, moved offshore, or recharacterized as another asset class. Under-assessment, not evasion, is the primary practical risk — a concern addressed in the wiki's [tax-you-can't-dodge](/wiki/the-tax-you-cant-dodge/) narrative.[4]

## Limits and Open Questions

- **Data quality varies by jurisdiction.** CAMA systems require transaction data, structure characteristics, and geographic information; jurisdictions with poor records or few arm's-length sales face greater estimation uncertainty. [CITATION NEEDED: systematic evidence on assessment accuracy variation across US jurisdictions]
- **The land/building split is hardest where land value is most concentrated.** In dense urban cores where land value dwarfs structure value, small percentage errors in the split can produce large absolute errors in either component. [VERIFY: whether this specific concern is addressed in Dye & England or Doucet's work]
- **Shapley-value and other advanced methods remain largely academic.** Operational adoption of cooperative-game separation methods in assessment practice has not been documented in the sources reviewed here.[2]
- **Agricultural and peri-urban land** presents special challenges where planning-permission value creates a large gap between use-value and market value — a concern noted in the [Mirrlees Review](/wiki/mirrlees-review/) and relevant to the [farmer impact objection](/wiki/lvt-hurts-farmers/).[7]

## See Also

- [International Association of Assessing Officers (IAAO)](/wiki/iaao/) — the professional standards body behind mass appraisal and ratio-study methodology
- [Objection: Land value can't be assessed accurately](/wiki/land-cannot-be-assessed/)
- [Land Value Tax](/wiki/land-value-tax/)
- [Site Value](/wiki/site-value/)
- [Split-Rate Taxation](/wiki/split-rate-taxation/)
- [Research: Dye & England, Assessing the Theory and Practice of Land Value Taxation](/wiki/dye-england-assessing-lvt/)
- [Research: Doucet, Does Georgism Work?](/wiki/doucet-does-georgism-work/)
- [Center for Land Economics](/wiki/center-for-land-economics/)

## Sources

1. Lars Doucet (2022), "Does Georgism Work? Part 3: Can Unimproved Land Value Be Accurately Assessed?", *Astral Codex Ten* — [wiki summary](/wiki/doucet-does-georgism-work/) · [original](https://www.astralcodexten.com/p/does-georgism-work-part-3-can-unimproved) — used for the claim that land's spatial smoothness lets comparable-sales, teardown-sale, and residual methods estimate land value at accuracy comparable to or better than whole-property assessment; and for the hedonic regression framework description.
2. Kumar et al. (2020), "Land and building separation based on Shapley values," *Humanities and Social Sciences Communications* (Nature). [Article](https://www.nature.com/articles/s41599-020-0444-1) — used for the cooperative-game (Shapley-value) formalisation of land/building value separation.
3. Richard F. Dye & Richard W. England (2010), *Assessing the Theory and Practice of Land Value Taxation*, Lincoln Institute of Land Policy — [wiki summary](/wiki/dye-england-assessing-lvt/) · [Report](https://www.lincolninst.edu/publications/policy-focus-reports/assessing-theory-practice-land-value-taxation/) — used for framing assessment methodology as a practical implementation issue and for the survey of international and US experience.
4. Lars Doucet (2022), "Does Georgism Work? Part 3" — as summarised on the wiki's [assessment objection page](/wiki/land-cannot-be-assessed/) — used for the list of jurisdictions already assessing land separately (Estonia, Denmark, Australian states), the claim that most US assessments publish a land/improvement split, and the Center for Land Economics reference.
5. Robert Andelson, ed. (2001), *Land-Value Taxation Around the World* — [wiki summary](/wiki/andelson-lvt-around-the-world/) — used for the comparative survey of site value rating in Australia and New Zealand, including NSW's land tax on unimproved capital value since 1895.
6. Gemmell, Grimes & Skidmore (2019), "Do Local Property Taxes Affect New Building Development?", *Journal of Housing Economics* — [wiki summary](/wiki/gemmell-grimes-skidmore-nz/) — used for New Zealand's land-value vs capital-value rating distinction and the Auckland quasi-natural experiment.
7. James Mirrlees et al. (2011), *Tax by Design: The Mirrlees Review*, Institute for Fiscal Studies — [wiki summary](/wiki/mirrlees-review/) — used for the agricultural/development value gap concern relevant to assessment difficulty.
