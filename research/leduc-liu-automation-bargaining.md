---
authors:
- Sylvain Leduc
- Zheng Liu
category: research
excerpt: A Federal Reserve Bank of San Francisco DSGE model finds the mere threat
  of automation weakens workers' wage-bargaining power, dampening wages and amplifying
  unemployment swings even when automation is never deployed — a mechanism, not
  a rent measurement, for labor-to-capital income shifts.
last_reviewed: 2026-07-15
source_url: https://www.frbsf.org/economic-research/files/wp2019-17.pdf
stub: false
subcategory: wiki-research-inequality
tags:
- research
- automation
- artificial-intelligence
- bargaining-power
- labor-share
- wages
- dsge
- federal-reserve
tier: important
title: 'Automation, Bargaining Power, and Labor Market Fluctuations (Leduc & Liu,
  FRBSF Working Paper 2019-17)'
year: 2023
---

## Summary

"Automation, Bargaining Power, and Labor Market Fluctuations" is a Federal Reserve Bank of San Francisco working paper by **Sylvain Leduc** and **Zheng Liu**, both FRBSF economists. The paper was first circulated under the title "Robots or Workers? A Macro Analysis of Automation and Labor Markets," carries the working-paper number **2019-17**, and this entry reads the version dated **February 2023** (DOI 10.24148/wp2019-17) — the most recent revision available on the FRBSF site at the time of writing. Its central claim: **the threat of automation weakens workers' bargaining power in wage negotiations, dampening wage growth and amplifying unemployment fluctuations — even in periods when firms do not actually automate.** This entry reads the full 43-page paper, including the model setup, calibration, empirical sections, and appendices.

The paper builds a dynamic stochastic general equilibrium (DSGE) model — a generalization of the standard Diamond-Mortensen-Pissarides (DMP) labor-search model — in which firms choose, period by period, whether to fill a job vacancy with a worker or with automation equipment. The paper is explicitly a mechanism/business-cycle study, not an empirical measurement of how much income automation has actually shifted from labor to capital; its authors frame it as answering a different, complementary question from the long-run automation literature (Acemoglu & Restrepo and others), namely how automation *threats* — not just realized automation — shape short-run wage and employment dynamics.

## The Core Argument / Findings

**The mechanism.** In the model, each firm draws a random cost of automating an open vacancy every period. If that cost falls below a threshold, the firm automates instead of hiring; the possibility of automating raises the firm's "reservation value" in wage bargaining with workers, since the firm's outside option (automate instead of paying a higher wage) has improved. This lowers the wage workers can bargain for, even though most vacancies are never actually automated in any given period — the effect operates through the *threat*, structurally analogous to how a strong outside option depresses a worker's bargained wage in standard search theory. Because automation incentives are procyclical (automating is more attractive when labor markets are tight and wages would otherwise rise), the model generates **countercyclical fluctuations in the labor share of income**, matching observed U.S. data.

**Calibration and quantitative findings.** Fitting the model to U.S. quarterly data (1985–2018/2019) on unemployment, job vacancies, real wage growth, and labor productivity growth using Bayesian estimation, the authors find the automation channel is "quantitatively important": absent the automation threat, the volatility of labor-market tightness (the vacancy-to-unemployment ratio) relative to real-wage volatility would be **36% smaller** than the estimated model predicts. The model also reproduces two puzzling patterns in the aggregate data: rising volatility of labor-market tightness since the 2000s, and a declining correlation between real wages and labor productivity since the early 2000s — both consistent with a rising automation threat over that period.

**Cross-sectional empirical evidence.** Beyond the calibrated model, the paper reports a reduced-form panel regression using industry-level U.S. data (15 two-digit NAICS industries, JOLTS/BLS data, 2001–2019), interacting the aggregate relative price of computer equipment (a proxy for automation cost) with a fixed industry-level "automation potential" score (McKinsey Global Institute estimates). It finds industries more exposed to automation see significantly larger increases in vacancies and the vacancy-to-unemployment ratio, and larger declines in unemployment, when computer prices fall — consistent with the model's prediction, with coefficients significant at the 5–10% level across specifications, holding controlling for industry unionization and offshoring exposure.

**Skill heterogeneity extension.** In an extended version of the model where automation substitutes for low-skill labor but complements high-skill labor, the core mechanism survives: the automation threat still depresses low-skill wages and raises labor productivity, and the model additionally predicts automation increases the skill wage premium — consistent with firm-level evidence on automation's skill-upgrading effects (cited to Acemoglu et al. 2022).

## Relation to the Georgist Case

This paper's relevance to the wiki runs through the rent-gradient discipline that governs the frontier chapters on AI and automation, and readers should apply it carefully: **this is a paper about automation rents (returns to capital owners and firms from labor-substituting technology), not about land rent**, and the two should not be conflated. The mechanism Leduc and Liu identify — bargaining-power erosion that shifts income from labor toward whoever owns the substitute technology — is structurally similar to arguments the wiki already carries about AI-driven rent capture (see [Korinek & Stiglitz](/wiki/korinek-stiglitz-ai-rents/)), but it operates through a different channel: not "AI generates innovator rents that exceed innovation cost," but "the mere *option* to automate improves the firm's bargaining position, regardless of whether any rent is actually captured by the automation itself." The income that does not go to workers under this mechanism goes to whichever factor owns the automation equipment or the firm's residual claim — which may or may not be scarce, irreproducible, or rent-bearing in the Georgist sense. Automation capital (robots, software, compute) is, in general, *reproducible* — more can be built — which places this paper's mechanism closer to the wiki's more contested, capital/monopoly end of the rent gradient than to the clean land case. Where this paper *does* connect to land, it is only via the general logic (also present in Korinek & Stiglitz) that as automation makes labor itself more substitutable, whatever factor remains scarce — potentially including land and location — captures a growing share of the gains; Leduc and Liu do not develop that connection themselves.

## Nuances and Limits

- **Model-based, not quasi-experimental.** This is a structural DSGE paper: its headline "36% of tightness volatility" figure is a property of an estimated theoretical model fit to aggregate time series, not a causal estimate from a natural experiment or instrumented regression. The Bayesian estimation procedure imposes the model's functional-form assumptions on the data by construction.
- **The cross-sectional regressions are the paper's strongest empirical anchor** but are still reduced-form correlations between an aggregate price proxy and industry outcomes, not a randomized or quasi-experimental design; the authors' own robustness checks (controlling for unionization and offshoring) mitigate but do not eliminate confounding concerns.
- **Working paper status, now resolved.** As of the version read (February 2023), the paper was a Federal Reserve Bank working paper; the views were stated to be "solely the responsibility of the authors" and not those of the Federal Reserve System. **Update (2026-07-18, T2 verification):** the paper has since been peer-reviewed and published as Sylvain Leduc and Zheng Liu, "Automation, Bargaining Power, and Labor Market Fluctuations," *American Economic Journal: Macroeconomics* 16(4): 311–349 (October 2024), DOI [10.1257/mac.20220181](https://doi.org/10.1257/mac.20220181) — confirmed via the AEA/IDEAS-RePEc listing. The working-paper text used for this page's quotations and findings is unchanged in substance from the published version per the journal listing's abstract; page/section citations above refer to the FRBSF working-paper pagination, not the final journal pagination, which was not independently re-checked.
- **Does not measure rent capture or land specifically.** The paper is silent on land, location, or economic rent as such; its contribution to the wiki is a *mechanism* for labor-to-capital income shifts under automation, useful context for the AI-and-inequality lane, but it should not be cited as evidence about land rent or LVT incidence.
- **Ambiguous net employment effect.** The model's own logic implies employment effects of automation are ambiguous, not uniformly negative: automating a vacancy displaces the worker who would have filled it, but the option to automate also raises the expected value of *creating* a vacancy in the first place, which can raise job creation and the job-finding rate.

## Bears On

This paper strengthens the mechanism side of the wiki's automation/AI-and-labor-share literature without making an empirical rent-magnitude claim. It is a useful mechanism companion to [Gen-AI: Artificial Intelligence and the Future of Work (IMF, 2024)](/wiki/imf-gen-ai-future-of-work/), which documents AI's labor-market exposure at scale without offering this bargaining-power channel, and to [Korinek & Stiglitz](/wiki/korinek-stiglitz-ai-rents/), whose "innovator rents" framing this paper's threat-based mechanism complements rather than duplicates. Its connection to [Most of the modern rise in the capital share is land, not capital](/wiki/capital-share-rise-is-land/) is real but should be flagged as **indirect and not land-specific**: this paper documents one mechanism (automation-threat bargaining erosion) for a labor-to-capital income shift, but does not identify land as the destination of that shift the way the capital-share-is-land literature does for housing wealth — citing it on that page would need an explicit caveat that automation capital, unlike land, is in general reproducible.

## See Also

- [Gen-AI: Artificial Intelligence and the Future of Work (IMF SDN 2024)](/wiki/imf-gen-ai-future-of-work/)
- [Korinek & Stiglitz — AI, Innovator Rents and Non-Distortionary Redistribution](/wiki/korinek-stiglitz-ai-rents/)
- [Carney — The Future of Work (Whitaker Lecture, 2018)](/wiki/carney-future-of-work/) — a central banker's synthesis of the same automation-inequality diagnosis, with the Engels' pause precedent
- [Most of the modern rise in the capital share is land, not capital](/wiki/capital-share-rise-is-land/)
- [Economic Rent](/wiki/economic-rent/)
- [Korinek & Ng — digital superstars](/wiki/korinek-ng-digital-superstars/)

## Sources

1. Sylvain Leduc & Zheng Liu, "Automation, Bargaining Power, and Labor Market Fluctuations," Federal Reserve Bank of San Francisco Working Paper 2019-17 (version dated February 2023), DOI: 10.24148/wp2019-17. [PDF](https://www.frbsf.org/economic-research/files/wp2019-17.pdf) — fetched and read in full — used for the model mechanism, the Bayesian calibration results (the 36% volatility figure), the cross-sectional industry-level regression evidence, the skill-heterogeneity extension, and all direct quotations.
