---
title: "Buettner (2003): Tiebout Visits Germany — Land Tax Capitalization in a Sample of German Municipalities"
category: research
subcategory: wiki-research-finance
tags: [research, tax-capitalization, land-value-tax, germany, incidence, gmm, spatial-econometrics]
authors: [Thiess Buettner]
year: 2003
tier: Important
source_url: https://gwern.net/doc/economics/georgism/2003-buettner.pdf
stub: false
supports_outcomes: [landlords-cannot-pass-lvt-to-tenants]
excerpt: "Buettner's 2003 study of 675 Baden-Württemberg municipalities finds land taxes capitalize into land values (elasticity ≈ −0.31, GMM) at a rate well beyond what simple full capitalization predicts, while monthly rents — measured gross, including the cost items landlords normally pass through — show no significant relationship to the local land tax rate."
last_reviewed: 2026-07-18
bears_on_objections: [lvt-destroys-its-own-tax-base]
---

## Overview

"Tiebout Visits Germany: Land Tax Capitalization in a Sample of German Municipalities"
is a paper by economist **Thiess Büttner** (Centre for European Economic Research,
ZEW, and Mannheim University; rendered "Buettner" in some citations), presented at
the Third Norwegian-German Seminar on Public Economics, CESifo Conference Centre,
Munich, 20–21 June 2003 (JEL H73, R21, C21).[1] The paper applies a Tiebout-style
test to Germany's local land tax (*Grundsteuer B*), which municipalities set via a
local multiplier (*Hebesatz*) on a national base rate, asking whether cross-municipal
differences in the effective tax rate capitalize into land prices — as standard
tax-capitalization theory predicts — and whether any of that burden instead shows up
in rents paid by tenants.[1] The full conference-paper text was fetched and read in
full this session (2026-07-18), superseding the earlier abstract-only version of this
page.

## Data and Method

The sample is the **675 municipalities of Baden-Württemberg** (a major German state)
with population above 1,000 and available 1987 land-transaction data, drawn from a
base dataset of 1,111 municipalities in the state.[1] The land tax rate is defined by
the *Hebesatz* multiplier on a basic land-tax rate of 0.35% (0.50% in 1964); across
the sample the **statutory rate averages 0.863%**, ranging from **0.648% to 1.295%**,
while the **effective rate averages 0.113%**, ranging from 0.027% to 0.583%.[1] Land
value averages 164.7 DM/m² (range 16.45–936.9) and monthly gross rent (including
water, sewerage, and tax side-costs, but excluding heating) averages 6.29 DM/m²
(range 4.12–9.42).[1] Because the *current* statutory tax rate is endogenous to
unobserved local conditions, Büttner instruments for the effective tax rate using the
current and 1961 statutory rates in a GMM specification, and adds a spatial-lag
(spillover) structure for amenities across neighboring municipalities.[1]

## Core Findings

- **Land values fall with the local land-tax rate — more than full capitalization
  alone would predict.** The GMM specification finds the land-value elasticity with
  respect to the effective land-tax rate is **−0.314** (significant at 5%, N=675,
  R²=0.803); the simpler OLS specification on the statutory rate gives a similar but
  statistically insignificant −0.329.[1] Büttner works out what "full capitalization"
  alone would imply: at the mean effective tax rate of 0.113% and a 3% discount rate,
  the tax should be about **3.6% of the cost of holding land** — a far smaller number
  than the estimated 31% elasticity, which Büttner reads as evidence of
  **"substantial overcapitalization."**[1] He offers two candidate explanations: (1)
  measurement error in the effective tax rate from Germany's "disappearing tax base"
  problem (uncertain assessment ratios, since land was last officially assessed in
  1964); and (2) sample land prices rose roughly **9.6% annually between 1964 and
  1987**, so if landowners anticipate continued appreciation, the true cost of
  holding land net of expected appreciation is lower than the tax-only calculation
  assumes, mechanically amplifying the apparent capitalization response.[1]
- **No rent effect — and the rent variable is defined in a way that makes this a
  stronger result than it first looks.** Re-running the same specification with
  monthly rent as the dependent variable, the coefficient on the land tax rate is
  small and statistically insignificant under both OLS (0.005) and GMM (−0.002),
  against R²=0.791.[1] Büttner flags why this is notable in the German institutional
  context specifically: the land tax is legally listed as part of the *Nebenkosten*
  (side costs) that landlords routinely pass through to tenants and that are **not**
  subject to German rent-control limits — and the rent variable used is the gross
  rent, which explicitly *includes* those side costs.[1] Finding no relationship
  under a measure that would have captured a pass-through if one existed is a more
  demanding test than it would be under a narrower rent definition.
- **Amenity spillovers, not the land tax, drive most of the cross-municipal
  variation in both land values and rents.** The spatial-lag terms for public
  swimming pools, tennis courts, theaters, and highway access are significant in
  both the land-value and rent regressions, "pointing to significant spillovers from
  amenities and the provision of public goods across municipalities" — a secondary
  finding of the paper, orthogonal to the tax-capitalization result but part of its
  headline claim.[1]

## Limits and Caveats

- **Single-state, 1987 cross-section.** The sample is Baden-Württemberg only, not a
  national German dataset, and the data are a single year (1987), with a fixed-tax
  rate history back to 1961 used only as an instrument. Generalizing the exact
  elasticity to other German states or later periods is not warranted by this design
  alone.
- **The overcapitalization result is a puzzle the author himself flags, not a clean
  finding.** An elasticity roughly nine times what simple full capitalization
  predicts is a strength for the *qualitative* claim (the tax capitalizes, per the
  significant GMM coefficient)
  but a complication for using this paper's coefficient as a *quantitative*
  capitalization-rate estimate; Büttner's own candidate explanations (assessment-ratio
  measurement error; anticipated appreciation) are plausible but not separately
  tested in the paper.
- **A conference paper, not (as far as this session could confirm) a journal
  publication.** This should not be confused with Büttner's separate,
  journal-published 2003 paper "Tax base effects and fiscal externalities of local
  capital taxation" (*Journal of Urban Economics* 54(1): 110–128), which concerns
  local *capital* taxation, not this land-tax-capitalization study.
- **A partial-equilibrium, not general-equilibrium, exercise.** Like the wiki's other
  reduced-form capitalization studies, this is a hedonic-style cross-section, not a
  model of the whole local economy; see the [CGE cluster](/wiki/site-value-ge-simulations/)
  and specifically [Choi & Sjoquist (2015)](/wiki/choi-sjoquist-atlanta-lvt-cge/) for
  the general-equilibrium analogue of the same no-rent-pass-through result.

## See Also

- [Landlords Cannot Pass a Land Value Tax on to Tenants](/wiki/landlords-cannot-pass-lvt-to-tenants/)
- [Tax Capitalization](/wiki/tax-capitalization/)
- [Borge & Rattsø (2014), Norway capitalization](/wiki/borge-rattso-norway-capitalization/) · [Choi & Sjoquist (2015), Atlanta CGE](/wiki/choi-sjoquist-atlanta-lvt-cge/) — the other members of this cluster
- [Land Is a Big Deal](/wiki/land-is-a-big-deal/)
- [Mieszkowski: The Property Tax — An Excise Tax or a Profits Tax?](/wiki/mieszkowski-property-tax-incidence/)
- [Objection: Land value can't be assessed accurately](/wiki/land-cannot-be-assessed/)

## Sources

1. Thiess Büttner (2003), "Tiebout Visits Germany: Land Tax Capitalization in a
   Sample of German Municipalities," presented at the Third Norwegian-German Seminar
   on Public Economics, CESifo Conference Centre, Munich, 20–21 June 2003. Free
   full-text PDF (conference-paper scan, gwern archive):
   [gwern.net/doc/economics/georgism/2003-buettner.pdf](https://gwern.net/doc/economics/georgism/2003-buettner.pdf)
   — **fetched and read in full (2026-07-18)**, superseding the earlier abstract-only
   citation to [economicpossibility.org](https://www.economicpossibility.org/sources/tiebout-visits-germany-land-tax-capitalization-in-a-sample-of-german-municipaliti) —
   used for every finding on this page: the 675-municipality Baden-Württemberg
   sample and descriptive statistics (Table 1), the land-value and rent regressions
   (Tables 2–3), the overcapitalization calculation and its two candidate
   explanations, and the *Nebenkosten*/rent-control institutional detail (footnote 5
   of the original).
2. Economic Possibility, "In German municipalities, land value tax does not increase
   monthly rent levels" — a related insight summary corroborating the no-rent-effect
   finding. [economicpossibility.org](https://www.economicpossibility.org/insights/in-german-municipalities-land-value-tax-does-not-increase-monthly-rent-levels-and) —
   used to cross-check the rent-incidence finding.
3. Lars Doucet, *Land Is a Big Deal* (2022), Ch. 21 — used for the discovery context
   and for listing this paper among the sources supporting full capitalization of
   property/land taxes. See this wiki's book page:
   [Land Is a Big Deal](/wiki/land-is-a-big-deal/).
