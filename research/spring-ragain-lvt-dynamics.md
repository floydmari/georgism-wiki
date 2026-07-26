---
title: "The Dynamic of a Tax on Land Value: Concepts, Models and Impact Scenario (Spring-Ragain, 2025)"
category: research
authors:
- Hugo Spring-Ragain
year: 2025
tier: Supplementary
source_url: https://arxiv.org/abs/2511.21766
supports_outcomes: []
subcategory: wiki-research-lvt
tags:
- research
- land-value-tax
- theory
- spatial-economics
- bifurcation
- simulation
- arxiv
- preprint
stub: false
excerpt: "An unreviewed 2025 arXiv preprint models land value and built capital as a spatial PDE system, finding a 'transcritical bifurcation' tax rate above which LVT shifts a city from a rent-dominated to a production-dominated equilibrium — rigorous but entirely uncalibrated theory."
last_reviewed: 2026-07-26
---

## Summary

**"The dynamic of a tax on land value: concepts, models and impact scenario"** is a November 2025 arXiv preprint by **Hugo Spring-Ragain**, a doctoral student at the Centre d'études diplomatiques et stratégiques (CEDS) in Paris.[1] It has not (as of this wiki's review, 2026-07-26) appeared in any peer-reviewed venue — it is a single-author, self-declared unfunded working paper posted to arXiv's general-economics category. [VERIFY: peer-review status — this is a preprint only; no journal publication, referee reports, or citations from established urban-economics scholars were found at time of writing.] The paper builds a **spatial-dynamic mathematical model** of how a [land value tax](/wiki/land-value-tax/) reshapes land value and construction activity across an urban area over time, extending the static comparative-statics tradition that dominates most LVT modeling (including the wiki's own [Neidle/TPA model](/wiki/tpa-what-would-lvt-do/)) into an explicitly time- and space-varying framework.

[VERIFY: author background] Spring-Ragain's institutional affiliation (CEDS, a diplomatic-studies school, not an economics department) and his other 2025 arXiv preprint — on an "action constant for quantum economics," an unconventional econophysics framework — suggest a non-specialist author working outside mainstream urban/public economics. The paper should be read as a rigorous but unvalidated theoretical exercise, not as evidence with the standing of peer-reviewed urban economics.

## Model and Method

The paper models two coupled fields over a two-dimensional city, evolving through time: land value *V(x,y,t)* and built capital *K(x,y,t)*. Land value decays at a rate driven by discounting, the land value tax rate τ, and a location-specific "centrality" growth term, diffuses spatially (modeling neighborhood spillovers via a Laplacian operator), and is replenished by the productive output of built capital. Built capital accumulates through investment that activates only once local profitability crosses a threshold, net of depreciation. The system is solved analytically for its steady states and numerically via finite-difference and stochastic (Euler–Maruyama) simulation. An appendix separately re-derives the standard partial-equilibrium result that a land value tax, unlike a per-unit or ad valorem commodity tax, creates no wedge between the price paid and price received because land supply is fixed — the tax is instead fully capitalized into a lower land price, consistent with the Georgist [tax-neutrality](/wiki/land-value-tax/) case already carried by this wiki via [ATCOR](/wiki/atcor/) and [deadweight loss](/wiki/deadweight-loss/) theory.

The model's parameters (productivity, discount rate, tax sensitivity, diffusion coefficient, and so on) are **illustrative constants chosen for tractability, not calibrated to any real city's data**. No empirical land-price, construction, or tax-revenue dataset is used anywhere in the paper.

## Key Findings

- **A transcritical bifurcation in the tax rate.** The model's central analytical result is that an interior equilibrium of positive land value and capital investment exists only when the combined discounting-plus-tax "decay rate" exceeds a profitability threshold (α > θ). At the critical tax rate τ_c(x,y), the system switches between an "inactive" regime (no net investment, land value and capital decay to zero) and an "active" regime where LVT revenue and construction coexist in equilibrium. Central, high-productivity locations tolerate a higher τ_c before losing the active regime than peripheral ones — a formal statement of the intuitive claim that a uniform LVT bites hardest at the urban edge first.
- **Diffusion smooths, not destabilizes.** Spatial diffusion in land value dampens (rather than amplifies) high-frequency spatial variation — the model finds no Turing-style pattern instability, because only the land-value field diffuses.
- **Ambiguous distributional/spatial effect.** Numerical Lorenz-curve and Gini-index simulations of "attractiveness" (Ψ = productivity ÷ effective decay rate) find inequality falls modestly as τ rises within a moderate range (illustrative Gini values move from 0.394 to 0.377 in the paper's baseline simulation), which the author interprets as a temporary equalizing effect before "re-stratification" toward the center at higher tax rates. This is a simulated property of the author's own parameterization, not an empirical finding about any real housing market.
- **Robustness checks.** The qualitative bifurcation structure is shown to survive under three alternative productivity-decay profiles (exponential, polycentric, suburban-flat), under spatial discretization into concentric rings, and under a spatially-graded tax rate — evidence the *mathematical* result is not an artifact of one specific functional-form choice, though this says nothing about whether the model's assumptions describe real cities.
- **Stochastic extension.** A version with mean-reverting random shocks to productivity and centrality shows the deterministic steady state becomes a "stochastic attractor" that land value and capital orbit rather than settle on — offered as a closer analogy to observed boom-bust cycles in real urban land markets, though again without empirical calibration.

## Limits and Honest Assessment

This is a **theoretical contribution only**: an internally consistent mathematical restatement and extension of the Georgist claim that LVT does not distort land use, cast in the language of reaction-diffusion dynamical systems. Its value to the wiki is illustrative — it shows that the standard static-neutrality result (Appendix A) survives the addition of space, time, diffusion, and stochastic shocks in at least one stylized model — but it carries **none of the empirical weight** of, for instance, the Pennsylvania split-rate literature or Denmark/Estonia implementation data already on this wiki. No claim in this paper should be cited as evidence about a real jurisdiction's likely LVT outcomes. [VERIFY: the paper is not yet peer-reviewed; its conclusions have not been independently checked by other economists at time of writing.]

## Bears On

- **Concept:** [Land Value Tax](/wiki/land-value-tax/) — a formal dynamical-systems restatement of the tax-neutrality argument
- **Concept:** [ATCOR](/wiki/atcor/) and [Deadweight Loss](/wiki/deadweight-loss/) — Appendix A's incidence derivation matches these directly
- **Research:** [What Would a Land Value Tax Actually Do? (Neidle/TPA)](/wiki/tpa-what-would-lvt-do/) — a contrasting empirical/static microsimulation of a real jurisdiction's LVT, versus this paper's theoretical/dynamic approach

## See Also

- [Land Value Tax](/wiki/land-value-tax/)
- [What Would a Land Value Tax Actually Do? (Neidle / Tax Policy Associates, 2026)](/wiki/tpa-what-would-lvt-do/)
- [ATCOR](/wiki/atcor/)
- [Deadweight Loss](/wiki/deadweight-loss/)
- [Henry George Theorem](/wiki/henry-george-theorem/)

## Sources

1. Hugo Spring-Ragain (2025), "The dynamic of a tax on land value: concepts, models and impact
   scenario," arXiv:2511.21766 [econ.GN], submitted 25 November 2025 — used for the full model,
   all findings, and the author-affiliation statement (CEDS, Paris) on the paper's title page.
   [arxiv.org/abs/2511.21766](https://arxiv.org/abs/2511.21766) ·
   [full-text PDF](https://arxiv.org/pdf/2511.21766).
