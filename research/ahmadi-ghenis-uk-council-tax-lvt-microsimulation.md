---
authors:
- Vahid Ahmadi
- Max Ghenis
bears_on_objections: []
category: research
excerpt: "A PolicyEngine microsimulation replacing UK council tax — still assessed on 1991 valuations — with a flat land value tax finds roughly two-thirds of households gain, with losses concentrated in the top wealth deciles; the burden tracks wealth (Gini 0.70) far more than income (Gini 0.37), and absolute poverty falls."
last_reviewed: 2026-08-29
source_url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7242479
stub: false
subcategory: wiki-research-lvt
tags:
- research
- united-kingdom
- council-tax
- land-value-tax
- microsimulation
- policyengine
tier: important
title: "Replacing Council Tax With a Land Value Tax: A Household-Level Microsimulation for the UK (Ahmadi & Ghenis, 2026)"
year: 2026
---

## Summary

"Replacing Council Tax With a Land Value Tax: A Household-Level Microsimulation for the UK,"
by **Vahid Ahmadi** (Research Associate, PolicyEngine; LSE) and **Max Ghenis** (Founder/CEO,
PolicyEngine), is an SSRN working paper built on **PolicyEngine UK**, an open-source tax-benefit
microsimulation model, run against the **Enhanced Family Resources Survey (FRS) 2023–24**.
It targets a specific, long-standing UK reform question: council
tax remains assessed on **1991 property valuations**,
producing a tax that is, per the paper's own abstract, "sharply regressive in property value."

## The Simulation

Per the SSRN abstract, the paper "simulates various reform scenarios with tax rates ranging
from 0.5 to 5 percent, incorporating a citizen's dividend and exempt bands." Under the
budget-neutral central scenario, replacing approximately **£58.5 billion** in council tax
revenue requires a **0.79%** land value tax rate. The paper reports that "two thirds of
households gain under the central incidence treatment (63 to 76 per cent across defensible
alternatives), and incidence is organised by wealth rather than income."

A companion blog analysis by the same PolicyEngine team, published on the *Progress and
Poverty* Substack, works through a related single-scenario dashboard using the same
underlying model and data: at a revenue-neutral rate of **0.77%** on £7.46 trillion of UK
land value (replacing £57.6bn of council tax), 68% of households gain overall. By income
decile, the bottom decile gains roughly £481/year (+2.3% of net income), deciles 2–8 are all
positive, while decile 9 loses roughly £991/year and the top decile loses roughly £966/year.
By wealth decile, deciles 2–8 all gain (£484–£1,464/year), and only the top two wealth
deciles lose. Households with no land wealth (~17% of households) gain an average £832/year,
with 82% better off. Absolute poverty (before housing costs) falls by 0.65 percentage points.
Income inequality is barely affected (Gini rises 0.11%), because — as the analysis frames
it — the tax tracks **wealth** (Gini 0.70) far more than **income** (Gini 0.37).

## Two Related but Distinct Figures

The SSRN paper's own headline numbers (0.79% rate, £58.5bn, 63–76% of households gaining
across scenarios) differ modestly from the blog's single-scenario figures (0.77%, £57.6bn,
68% gaining) — consistent with the SSRN paper being a more elaborate academic write-up (a
rate sweep from 0.5% to 5%, multiple incidence-assumption scenarios, and design features —
a citizen's dividend and exempt bands — not present in the blog's simpler dashboard) built on
the same underlying PolicyEngine UK model and FRS data, rather than being identical to it.
This page cites both sets of figures, attributed to their respective source, rather than
treating them as interchangeable.

## Relation to the Georgist Case

This is a rigorous, reproducible, open-source quantification of a specific and immediately
actionable UK reform — replacing a genuinely outdated (34-year-stale) valuation-based tax with
land value taxation — with distributional results that directly support the wiki's core claim
that LVT burdens fall on wealth rather than income or ordinary consumption. The finding that
roughly two-thirds of households gain, with losses concentrated at the top of the wealth
distribution, is a concrete answer to the standard "who wins and loses" question any UK LVT
reform proposal faces.

## Nuances and Limits

- **Two distinct source documents, cited separately.** The SSRN paper's own headline figures
  (0.79%, £58.5bn, 63–76% range) should not be conflated with the companion blog's simpler
  single-scenario figures (0.77%, £57.6bn, 68%) — see above.
- **A microsimulation of a static reform, not a dynamic or transition analysis.** Like most
  microsimulation studies, this models the distributional effect of the tax change on the
  existing population and asset distribution; it does not model behavioral responses,
  transition costs, or the political economy of implementation.
- **Abstract-level source for the SSRN paper itself (B-claim); the companion blog analysis
  was read in full (A-claim) for its specific figures.** SSRN blocked direct access to the
  paper's full text.

## Bears On

- **Concept:** [Land Value Tax](/wiki/land-value-tax/) — a concrete, current UK reform proposal with worked distributional numbers.
- **Place:** [Wales](/wiki/wales/) — the wiki's existing coverage of a separate Welsh council-tax-replacement inquiry; this paper covers UK-wide/English data specifically.
- **Person:** [Andy Burnham](/wiki/andy-burnham/) — the wiki's existing coverage of UK political debate over council tax reform, which this paper supplies quantitative grounding for.

## See Also

- [Land Value Tax](/wiki/land-value-tax/)
- [Wales](/wiki/wales/)
- [Andy Burnham](/wiki/andy-burnham/)
- [Henry George Foundation's Hybrid LVT Proposal](/wiki/henry-george-foundation-hybrid-lvt-proposal/) — a different UK LVT design proposal, useful comparison

## Sources

1. Vahid Ahmadi & Max Ghenis (2026), "Replacing Council Tax With a Land Value Tax: A
   Household-Level Microsimulation for the UK," SSRN Working Paper, DOI
   10.2139/ssrn.7242479. [papers.ssrn.com](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7242479) —
   fetch blocked (403) to this session 2026-08-29; verbatim abstract obtained via the
   Crossref API — used for the 0.79% central-scenario rate, the £58.5bn revenue figure, the
   0.5–5% rate-sweep design, the citizen's-dividend/exempt-band features, and the 63–76%
   gaining-households range (B-claim; abstract-level).
2. PolicyEngine, "How replacing council tax with a flat land value tax would affect
   households in the UK," *Progress and Poverty* (Substack), 2026.
   [blog.landeconomics.org](https://blog.landeconomics.org/p/how-replacing-council-tax-with-a) —
   read in full 2026-08-29; used for the 0.77% single-scenario rate, the £57.6bn/£7.46
   trillion figures, the income- and wealth-decile winner/loser breakdown, the landless-household
   figures, the poverty-reduction figure, and the income/wealth Gini figures (A-claim; full
   text read, built on PolicyEngine UK's Enhanced FRS 2023-24 microdata).
