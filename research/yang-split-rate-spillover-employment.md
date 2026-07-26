---
authors:
- Zhou Yang
category: research
excerpt: Spatial panel study of Pennsylvania's split-rate municipalities finds the
  tax slows employment growth in close neighboring jurisdictions (within 5-10 miles)
  but speeds it up in more distant ones (15-20 miles) — a "zero-sum near, win-win far"
  spillover pattern, with no significant effect on employment in the taxing
  jurisdiction itself.
last_reviewed: 2026-07-26
source_url: https://doi.org/10.1007/s11146-024-09995-y
stub: false
subcategory: wiki-research-lvt
tags:
- research
- pennsylvania
- split-rate
- spillover
- employment
- spatial-econometrics
- empirical
tier: Important
title: "The Spillover Effects of Land Value Taxation: How Can It Affect Your Neighbors' Job Growth?"
year: 2024
---

## Summary

Zhou Yang (Robert Morris University) — the same author, with Zackary Hawley, of
[Yang & Hawley (2022) on split-rate tax-base effects](/wiki/yang-split-rate-tax-base/)
— published "The Spillover Effects of Land Value Taxation: How Can It Affect Your
Neighbors' Job Growth?" in *The Journal of Real Estate Finance and Economics*
(online 5 September 2024), DOI
[10.1007/s11146-024-09995-y](https://doi.org/10.1007/s11146-024-09995-y). The
published version is paywalled, but the paper began as Lincoln Institute of Land
Policy Working Paper WP15ZY1 (2015), "The Spillover Effects of the Two-Rate
Property Taxes in Pennsylvania: A Zero-Sum Game or a Win-Win Game?" — freely
available from the [Lincoln Institute](https://www.lincolninst.edu/app/uploads/legacy-files/pubfiles/2502_1846_Yang%20WP15ZY1.pdf)
and read in full for this page. The working paper's abstract, methodology, and
headline result match the 2024 published abstract essentially verbatim, so the
findings below are drawn directly from that open-access precursor.

The paper fills a specific gap the wiki's other split-rate research does not
address: every prior Pennsylvania study — [Oates & Schwab](/wiki/oates-schwab-pittsburgh/),
[Plassmann & Tideman](/wiki/plassmann-tideman-construction/),
[Banzhaf & Lavery](/wiki/banzhaf-lavery-pa-sprawl/), and Yang's own tax-base
paper — measures effects **inside** the jurisdiction that adopts split-rate
taxation. None asks whether a two-rate tax's local gains come **at the expense
of, or alongside a benefit to,** neighboring municipalities that did not adopt it.

## The Core Argument and Findings

Using a spatial panel Durbin model on Pennsylvania county subdivisions,
1980–2010, Yang regresses each jurisdiction's decade-over-decade percentage
change in employment (four measures: total, construction, male, female) on its
own property tax structure **and** a spatially-weighted average of the tax
structure in neighboring jurisdictions, separately identifying two-rate
neighbors from single-rate neighbors. Multiple neighborhood "distance rings"
(5, 10, 15, and 20 miles, using both straight-line and driving-distance
measures) let the model trace how the spillover effect changes with distance.

- **Close neighbors lose (Type B — empirical).** Within a 5-mile driving
  distance, a one-unit increase in the log average land-to-structure tax rate
  differential among two-rate neighbors is associated with roughly a **4.5
  percentage-point reduction** in a jurisdiction's total employment growth rate,
  with the negative effect also significant for female employment. The paper
  reads this as consistent with two-rate jurisdictions attracting firms and
  workers away from adjacent single-rate municipalities.
- **The effect reverses at greater distance.** The negative spillover
  disappears within the 10-mile ring (no significant effect) and then **turns
  positive and significant at 15 miles** — a roughly **7.5 percentage-point
  increase** in construction employment growth for a one-unit increase in the
  neighboring tax-rate differential — persisting, at a smaller magnitude, at 20
  miles. Yang's own summary: "two-rate property taxation slows down employment
  growth in close neighbors but speeds up employment growth in neighbors within
  a longer distance."
- **No significant own-jurisdiction employment effect.** The jurisdiction's own
  tax-rate differential has a positive but statistically insignificant
  coefficient on its own employment growth across specifications — split-rate
  taxation's previously-documented effects on construction and tax base (Oates
  & Schwab; Plassmann & Tideman; Yang & Hawley) do not translate into a
  detectable *employment* boost in the adopting jurisdiction itself over this
  sample.
- **Robustness.** The pattern (negative-then-positive as the ring widens) holds
  using an alternative distance measure that ignores road networks, and using
  two alternative tax-rate specifications (the land-to-structure ratio, and a
  simple adoption dummy). A Hausman-Wu test using lagged vacancy rates and local
  government debt as instruments cannot reject exogeneity of the tax-rate
  differential.

## Relation to the Georgist Case

Yang frames the result as testing whether two-rate taxation is a **"zero-sum
game"** (diverting jobs and investment from neighbors) or a **"win-win
game"** (generating agglomeration spillovers that help neighbors too) — and
finds **both, at different spatial scales.** The proposed mechanism: a two-rate
municipality may draw firms and construction activity away from its immediate
single-rate neighbors (a competitive/diversion effect, strongest close by,
where relocation is cheapest), while more distant municipalities may benefit
from broader agglomeration economies as the taxing jurisdiction's market and
degree of specialization grow. Yang is explicit that this explanation is
speculative — "[w]hether these are the actual explanations for the dynamics of
the spillover effect across space is debatable and beyond the purpose of this
paper."

This is a genuinely double-edged finding for the split-rate case. It does not
contradict the construction- and tax-base-level evidence that split-rate
taxation stimulates *local* building activity (see
[Split-rate taxation increases urban construction](/wiki/split-rate-increases-construction/)):
Yang's own within-jurisdiction employment coefficient is positive, just
statistically insignificant. But it complicates the simplest reading of that
evidence — that a two-rate jurisdiction's gains are a net addition to regional
economic activity rather than partly a **redistribution** from its closest
neighbors. The reader-facing honest summary is Yang's own framing: the policy
is not simply zero-sum or simply win-win, but **both, depending on distance** —
a nuance the wiki's other split-rate pages, which measure only the adopting
jurisdiction, cannot see.

## Nuances and Limits

- **Employment, not construction or tax base.** This paper's dependent
  variable is employment growth (total, construction, male, female), not
  building permits or assessed value — the outcome measured by the wiki's other
  Pennsylvania split-rate studies. The results are not directly comparable
  magnitude-for-magnitude with, say, Oates & Schwab's permit-value figures.
- **Speculative mechanism.** The paper documents the spatial pattern (negative
  close, positive far) carefully but explicitly declines to identify which
  economic mechanism (firm relocation vs. agglomeration spillovers) actually
  drives it, calling for further microeconomic research.
- **Working-paper text used; published version paywalled.** The findings above
  are verified against the freely available 2015 Lincoln Institute working
  paper, whose abstract and headline results match the 2024 *Journal of Real
  Estate Finance and Economics* publication's abstract; the published version
  may have refined specifications or an extended sample not reflected here.
  [VERIFY: confirm whether the published 2024 version updates the 1980–2010
  sample period or coefficient magnitudes reported in the 2015 working paper.]
- **Pennsylvania-only external validity**, as with the rest of the wiki's
  split-rate evidence base — few other US states have enough adopting
  municipalities for this kind of spatial analysis.
- **No effect within the taxing jurisdiction.** Readers should not treat this
  paper as evidence that split-rate taxation raises employment where it is
  adopted; the own-jurisdiction coefficient is statistically null. Its
  contribution is entirely about the **spillover pattern**, not a new
  within-jurisdiction employment finding.

## Bears On

- **Concept:** [Split-Rate Taxation](/wiki/split-rate-taxation/) — direct evidence on a
  dimension (inter-jurisdictional spillovers) not addressed by the concept
  page's existing construction and tax-base evidence.
- **Benefit:** [Split-rate taxation increases urban construction](/wiki/split-rate-increases-construction/) —
  a caveat rather than a challenge: does not contradict the local construction
  effect, but shows part of a two-rate jurisdiction's advantage over its
  closest neighbors may be competitive/diversionary rather than purely additive
  at the regional level, while more distant jurisdictions appear to benefit
  too.

## See Also

- [Effects of Split-Rate Taxation on Tax Base (Yang & Hawley, 2022)](/wiki/yang-split-rate-tax-base/) — the same author's companion study of tax-base effects within the adopting jurisdiction
- [Can the Land Tax Help Curb Urban Sprawl? (Banzhaf & Lavery, 2010)](/wiki/banzhaf-lavery-pa-sprawl/)
- [A Markov Chain Monte Carlo Analysis of the Effect of Two-Rate Property Taxes on Construction (Plassmann & Tideman, 2000)](/wiki/plassmann-tideman-construction/)
- [Split-rate taxation increases urban construction](/wiki/split-rate-increases-construction/)
- [Split-Rate Taxation](/wiki/split-rate-taxation/)

## Sources

1. Zhou Yang (2024), "The Spillover Effects of Land Value Taxation: How Can It
   Affect Your Neighbors' Job Growth?" *The Journal of Real Estate Finance and
   Economics*, online 5 September 2024. [Publisher/DOI](https://doi.org/10.1007/s11146-024-09995-y)
   (paywalled) — used for the published citation and confirmation this is the
   peer-reviewed version of the working paper below.
2. Zhou Yang (2015), "The Spillover Effects of the Two-Rate Property Taxes in
   Pennsylvania: A Zero-Sum Game or a Win-Win Game?" Lincoln Institute of Land
   Policy Working Paper WP15ZY1. [Free PDF](https://www.lincolninst.edu/app/uploads/legacy-files/pubfiles/2502_1846_Yang%20WP15ZY1.pdf)
   — used directly (full text read) for all reported coefficients, the
   spatial-distance-ring methodology, robustness checks, and the "zero-sum
   game or a win-win game" framing quoted above; this is the working-paper
   precursor of source 1.
3. H. Spencer Banzhaf & Nathan Lavery (2010), "Can the Land Tax Help Curb Urban
   Sprawl? Evidence from Growth Patterns in Pennsylvania," *Journal of Urban
   Economics* 67(2) — [wiki summary](/wiki/banzhaf-lavery-pa-sprawl/) — cited by
   Yang (2015) for the differenced-dependent-variable-with-fixed-effects
   ("difference-in-difference-in-differences") identification logic this paper
   also relies on.
4. Zhou Yang & Zackary B. Hawley (2022), "Effects of Split-Rate Taxation on Tax
   Base," *Public Finance Review* 50(6) — [wiki summary](/wiki/yang-split-rate-tax-base/)
   — the same author's companion study of within-jurisdiction tax-base effects,
   used for comparison/contrast.
