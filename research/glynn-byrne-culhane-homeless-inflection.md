---
title: "Inflection Points in Community-Level Homeless Rates (Glynn, Byrne & Culhane 2021)"
category: research
tags: [research, homelessness, housing-costs, rents, cost-burden, bayesian, united-states]
authors: [Chris Glynn, Thomas H. Byrne, Dennis P. Culhane]
year: 2021
tier: Important
source_url: https://doi.org/10.1214/20-AOAS1414
stub: false
excerpt: "Glynn, Byrne & Culhane's Annals of Applied Statistics paper drops the usual linear assumption and lets the data find thresholds. Its central result: a community's expected homeless rate begins to climb sharply once median rent exceeds ~32% of median income — an empirical inflection point that lands almost exactly on the government's 30% housing-cost-burden line."
last_reviewed: 2026-07-11
supports_outcomes: [homelessness-is-housing-cost-problem]
---

## Summary

"Inflection Points in Community-Level Homeless Rates," by **Chris Glynn** (University
of New Hampshire), **Thomas H. Byrne** (Boston University) and **Dennis P. Culhane**
(University of Pennsylvania), appeared in **The Annals of Applied Statistics**, vol.
15, no. 2 (June 2021), pp. 1037–1053 (DOI
[10.1214/20-AOAS1414](https://doi.org/10.1214/20-AOAS1414)). It is a statistics
paper, not a policy one, and that is precisely its interest to this wiki: most
community-level homelessness models assume the homeless rate responds *linearly* to
predictors like rent, and the authors show that assumption hides the most
policy-relevant feature of the data — a **threshold**. It is the machine-learning /
Bayesian-nonparametric counterpart to the linear panel result in
[GAO-20-433](/wiki/gao-2020-homelessness-hud-oversight/), and it sharpens the
[Homelessness is a housing-cost problem](/wiki/homelessness-is-housing-cost-problem/)
claim by locating *where* on the rent scale homelessness accelerates.

## Key Findings

- **The threshold result.** From the abstract: "the expected homeless rate in a
  community increases sharply once median rental costs exceed 32% of median income,
  providing statistical evidence for the widely used definition of a housing cost
  burden at 30% of income."[1] In the authors' own three-finding summary: "there is an
  inflection point when ZRI [the Zillow Rent Index] reaches 32% of median income –
  after which the expected homeless rate in a community sharply increases."[1] The
  published-version abstract rounds this to "exceed 30% of median income."[2] Either
  way, the empirical inflection point lands almost exactly on the government's
  cost-burden line.
- **Why linearity was the wrong model.** The paper's premise: "This linear model
  assumption precludes the possibility of inflection points in homeless rates —
  thresholds in quantifiable metrics of a community that, once breached, are
  associated with large increases in homelessness."[1] The rent–homelessness
  relationship is not a gentle slope; it is a hinge.
- **The method.** The authors "utilize the Ewens-Pitman attraction distribution to
  develop a Bayesian nonparametric mixture model in which clusters of communities with
  similar covariates share common patterns of variation in homeless rates."[1] The
  model examines "structural changes in the relationship between homeless rates and
  community-level measures of housing affordability and extreme poverty."[1]
- **Geographic clustering.** Beyond the threshold, the model "identifies clusters of
  communities that exhibit distinct geographic patterns" — six clusters — "and yield[s]
  insight into the homelessness and housing affordability crisis unfolding on both
  coasts of the United States."[1] A worked example: a community where rent consumes
  ~40% of median income and extreme poverty is near the national average has an
  expected homeless rate of ≈0.32% — the range San Diego actually sat in (rent 40.16%
  of income, homeless rate 0.37%) in 2017.[1]

## Relation to the Georgist Case

Like the other homelessness sources here, the paper is not Georgist and says nothing
about land. Its contribution to the wiki's argument is a specific, quantitative one:
it converts the qualitative "homelessness is a housing-cost problem" claim into a
threshold — homelessness stays low while rent is a manageable share of income and then
*accelerates* once rent crosses the ~30–32% cost-burden line. That non-linearity is
why marginal changes in housing costs matter so much in already-expensive markets, and
it strengthens the reading (developed on the outcome page) that the price of *access
to location* — the Georgist variable — governs how many people a market pushes into
homelessness.

## Nuances and Limits

- **30% vs 32%.** The main-text and preprint finding is a **32%** inflection point;
  the published abstract phrases it as "exceed 30%." The two are consistent — the point
  is that the empirical hinge coincides with the standard cost-burden definition — but
  the exact figure depends on which sentence you quote.
- **Observational, model-dependent.** The inflection point is estimated from a
  Bayesian mixture model on observational CoC data, not from an experiment; the
  location of the threshold is a posterior estimate, and a third finding is explicitly
  that "unobserved factors in a CoC beyond poverty and housing affordability contribute
  meaningfully to increases (decreases) in homeless rates over time."[1]
- **Rent measured by ZRI.** Housing affordability is proxied by the Zillow Rent Index
  relative to median income, so the result inherits ZRI's coverage and construction.

## Bears On

- [Outcome: Homelessness is a housing-cost problem](/wiki/homelessness-is-housing-cost-problem/) — supplies the threshold / non-linear form of the rent–homelessness relationship.
- [Research: GAO-20-433 (2020)](/wiki/gao-2020-homelessness-hud-oversight/) — the linear panel estimate this paper generalises.
- [Research: Homelessness Is a Housing Problem (Colburn & Aldern)](/wiki/colburn-aldern-homelessness/) — the book-length cross-market statement of the same thesis.

## See Also

- [Outcome: Homelessness is a housing-cost problem](/wiki/homelessness-is-housing-cost-problem/)
- [Research: GAO-20-433 (2020)](/wiki/gao-2020-homelessness-hud-oversight/)
- [Research: Homelessness Is a Housing Problem (Colburn & Aldern)](/wiki/colburn-aldern-homelessness/)
- [Research: Do Local Economic Conditions Affect Homelessness? (Hanratty)](/wiki/hanratty-local-economic-homelessness/)
- [Narrative: The Housing Crisis Is a Land Crisis](/wiki/the-housing-crisis-is-a-land-crisis/)

## Sources

1. Chris Glynn, Thomas H. Byrne & Dennis P. Culhane, "Inflection points in
   community-level homeless rates," *The Annals of Applied Statistics* 15(2) (2021),
   1037–1053. DOI [10.1214/20-AOAS1414](https://doi.org/10.1214/20-AOAS1414). The
   abstract, the three-finding summary (32% ZRI inflection point; six clusters;
   unobserved-factor contribution), and the San Diego worked example were verified
   verbatim against the full-text author copy this session.
   [Author full-text PDF (g-lynn.github.io)](https://g-lynn.github.io/files/GlynnByrneCulhane_2019+.pdf) ·
   [Project Euclid record](https://projecteuclid.org/journals/annals-of-applied-statistics/volume-15/issue-2/Inflection-points-in-community-level-homeless-rates/10.1214/20-AOAS1414.full)
2. Published-version abstract phrasing ("the expected homeless rate in a community
   begins to quickly increase once median rental costs exceed 30% of median income")
   verified against the Project Euclid article record this session.
   [Project Euclid](https://projecteuclid.org/journals/annals-of-applied-statistics/volume-15/issue-2/Inflection-points-in-community-level-homeless-rates/10.1214/20-AOAS1414.full)
