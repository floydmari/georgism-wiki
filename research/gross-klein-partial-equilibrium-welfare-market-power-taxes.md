---
title: "A New Partial-Equilibrium Approach to Approximating the Welfare Effects of Market Power and Taxes"
category: research
tags:
- research
- deadweight-loss
- market-power
- taxation
- general-equilibrium
- excess-burden
- second-best
stub: false
excerpt: "Gross and Klein show the textbook deadweight-loss formula quietly assumes every other market is undistorted. When most other markets are already taxed or monopolized, taxing one more market can raise welfare even as the standard formula predicts a loss."
authors:
- Till Gross
- Paul Klein
year: 2026
tier: Important
source_url: https://doi.org/10.1016/j.jebo.2026.107747
last_reviewed: 2026-09-27
---

## Summary

The standard [deadweight-loss](/wiki/deadweight-loss/) (DWL) triangle — the Harberger measure used to estimate the efficiency cost of a tax or a monopoly — rests on an assumption that is rarely stated and almost never checked: that every other market in the economy is perfectly competitive and untaxed. Till Gross (Carleton University) and Paul Klein (Stockholm University) derive an extended partial-equilibrium formula that adds a term for the average distortion elsewhere in the economy, and show in worked numerical examples that this term is large enough to flip the sign of the estimated welfare change. In their headline example, when 90% of markets already carry a commodity tax, taxing one more market *raises* general-equilibrium welfare by roughly 0.11 to 0.46 (in the paper's normalized units, depending on the labour-tax rate), while both the standard DWL formula and an alternative formula from Goulder and Williams (2003) predict a loss (Table 6, p. 33). The paper is a pure produced-goods and labour-market analysis; it does not discuss land, land value taxation, or Georgism.

## The Core Argument and Findings

### What the standard formula assumes

The DWL formula treats the marginal cost a firm pays for its inputs as equal to the true social cost of those inputs. Gross and Klein point out that this identification is only correct if the "marginal surplus" — the gap between marginal willingness to pay and marginal cost — is zero in every other market the reallocated inputs could flow to or from (p. 2). As the abstract states:

> "The traditional deadweight-loss (DWL) formula rests on a usually unstated, strong assumption: that all other markets are undistorted." (Abstract, p. 1)

The authors note that this limitation has been flagged before — as far back as Hicks (1941) — and that Harberger (1971) himself acknowledged it while observing that applied work routinely ignores it:

> "it is in fact rarely done in studies involving applied welfare economics. I do not want to appear to defend this neglect – indeed, the sooner it is rectified, the better." (Harberger 1971, p. 791, quoted p. 3)

The intuition for why the omission matters, even when the market being studied is a vanishing sliver of the economy, is an aggregation argument: making one market more competitive (or lowering a tax there) requires more inputs, which must be drawn away from every other market. The effect on any single other market is tiny, but summed across all of them it is "of the same order of magnitude as the effect on market m" (p. 3) — so it cannot be dropped as negligible just because the target market is small.

### The extended formula

Gross and Klein model an economy with N intermediate-good markets, each either competitive or monopolistic, feeding a final-goods aggregator, with labour as the sole input (Section 3). Taking the total differential of the equilibrium conditions, they derive a formula for the change in surplus from changing one market's structure (Equation 9, p. 14) and a simplified closed form under additional assumptions — equal output elasticities across markets, constant returns, and price equal to marginal product (Equation 15, p. 17):

> "The first term on the right-hand side of Equation (15) is the traditional DWL. The second term is new to our analysis and reflects the opportunity cost (beyond the firm's private costs) of expanding output in market 1." (p. 17)

That second term is proportional to the *quantity-weighted average markup (or tax wedge) in the rest of the economy*. It is zero only when every other market is competitive and untaxed — precisely the case in which the DWL formula is exact. When the rest of the economy carries positive average markups or taxes, the term is negative, and it does not shrink as the studied market's share of the economy shrinks.

### The sign-flip examples

Using a Dixit-Stiglitz aggregator (elasticity of substitution 7) with up to 1,000,001 markets, the paper's Table 1 (p. 23) compares the standard DWL, the authors' formula (∆S), and the true general-equilibrium change (GE) from making one monopolized market competitive, as the share of *other* markets that are monopolistic rises. With N = 1,000,001 markets (panel b): at 0% monopolization elsewhere, DWL = ∆S = GE = 1.0000; at 100% monopolization elsewhere, DWL = 2.5216 (predicting a large efficiency *gain*), while ∆S = GE = -3.7949 (an efficiency *loss* of similar magnitude) — the standard formula gets both the size and the sign wrong.

A companion exercise (Table 5, p. 29) removes a commodity-tax exemption — modeled on Ontario's tax treatment of groceries and prescription drugs — when 90% of the remaining markets already carry a 13% tax. Here the standard DWL formula predicts an efficiency *loss* from taxing the exempted market (∆Y = -0.5850 whether or not other markets are also monopolized), while the authors' formula and the true general-equilibrium calculation both show an efficiency *gain* of 0.5204: taxing the last untaxed market moves the economy toward *uniform* taxation, which is what raises welfare, not the level of taxation itself.

The paper's Table 6 (p. 33) extends this to endogenous labour supply and compares against the formula of Goulder and Williams (2003), who separately argued that the standard DWL formula also ignores commodity taxes' effect on the labour market. When no goods markets are taxed (panel a), all three partial-equilibrium formulas — DWL, Goulder-Williams (GW), and the authors' — are in the right ballpark, though GW overstates and the authors' formula understates the true loss somewhat. But when 90% of other markets already carry the 13% goods tax (panel b), both DWL (flat at -0.5850) and GW (ranging from -0.6866 to -1.2077 as the labour-tax rate rises from 0 to 0.6) predict a welfare *loss* from taxing one more market, while the true general-equilibrium change (GE) is positive throughout, ranging from about +0.46 (no labour tax) down to about +0.11 (a 60% labour tax) — matching the authors' own formula (∆S) closely. Gross and Klein trace the Goulder-Williams error to that formula's implicit assumption that the economy starts from *uniform* commodity taxation; when taxation is broad but not uniform, renormalizing the labour tax to account for the average goods tax does not capture the effect of taxing one more, previously-exempt, market.

### What the paper explicitly does not claim

The authors are careful to note that neither the standard DWL formula nor their own extension is suited to estimating the *aggregate*, economy-wide efficiency effect of changing market structure or tax policy across many markets at once — only a full general-equilibrium model can do that (Table 2, p. 24, shows that simply summing the partial-equilibrium formula's predictions across all markets diverges sharply from the true general-equilibrium result once a large share of the economy is monopolized). Their formula is offered as a better *single-market* approximation, not a substitute for general-equilibrium modeling of system-wide reform.

## Relation to the Georgist Case

Gross and Klein do not discuss land, land value taxation, or Georgism anywhere in the paper. Any connection to the geoist case for a land value tax is therefore an interpretive reading, not a claim the authors make.

The [zero-deadweight-loss argument for land value tax](/wiki/deadweight-loss/#why-land-value-tax-has-zero-deadweight-loss) rests on a property of the taxed market's *own* elasticity: land's supply is fixed, so there is no quantity of land withdrawn from use when it is taxed, and hence no Harberger triangle in the land market itself. Gross and Klein's extension does not touch that argument. Their added term captures the opportunity cost of inputs (labour, in their model) reallocated *into or out of other, already-distorted markets* when the market under study changes; it says nothing about whether the studied market's own supply curve is elastic or inelastic, and it applies with equal force whether the market being made competitive or taxed produces widgets or anything else with a normal supply response. A tax whose own base is perfectly inelastic sits outside the mechanism the paper describes, because there is no reallocation of the taxed input to correct for.

What the paper's findings do bear on, read this way, is the evaluation of taxes on ordinary produced goods in an economy where most other markets are *already* distorted by taxes or market power — which describes most real economies more accurately than the textbook "one distorted market, all others clean" setup. The paper's central numerical result — that adding a tax (or removing an exemption) in a heavily taxed economy can *raise* rather than lower welfare, because it moves the tax system toward uniformity — is a second-best result in the tradition of Lipsey and Lancaster (1956), which the authors cite explicitly (p. 3, fn. 3). Read as an interpretive extension, it cuts against naive comparisons in both directions: it undercuts the reflex assumption that any additional tax on produced goods must be efficiency-reducing in a world already full of taxes and market power, but by the same logic it undercuts an equally naive assumption that removing any one distortion from a heavily distorted economy is automatically an improvement. Neither direction can be read off the standard DWL triangle once other markets are known to be distorted; the paper's own conclusion is that only a general-equilibrium calculation, or their formula applied market-by-market, can settle which way the sign runs in a given case.

## Nuances and Limits

- **Working-paper source.** This page is drawn from the authors' own accepted-manuscript PDF (dated June 16, 2025), not the copy-edited journal proof; the published pagination was not consulted, so page references above are to the manuscript.
- **Does not aggregate.** The authors state plainly that their formula, like the standard DWL, is not designed to measure the total efficiency cost of market power or taxation across the whole economy — only the effect of a change in a single market (or a small connected set of markets) that is small relative to the rest of the economy (p. 4, p. 24).
- **A special case where the standard formula is exact.** Under quasi-linear preferences or production — an extreme case involving some infinite elasticities — the authors show the DWL formula recovers the exact answer regardless of distortions elsewhere (Section 4.3, p. 21). They are explicit that they do not regard this case as empirically relevant, calling the elasticities it requires "unrealistic."
- **Endogenous labour supply changes little.** Allowing labour supply to respond to wages (using a Frisch elasticity of 0.4, the U.S. Congressional Budget Office's central estimate) leaves the qualitative sign-flip results intact and changes the quantitative results only modestly (Table 4, p. 27).
- **A closely related paper reaches similar conclusions by a different route.** Kaplow (2023) derives a general-equilibrium formula for the welfare effect of market-power changes that the authors describe as "very similar to ours" in spirit, though Kaplow's own partial-equilibrium special case (built on quasi-linearity) supports the standard DWL formula as correct — a result Gross and Klein attribute to the restrictive functional form rather than to a disagreement about the underlying economics (p. 4–6).
- **Informational demands.** Even the simplified formula requires an estimate of the average markup or tax wedge, weighted by quantity, across the rest of the economy — information the standard DWL calculation does not need. The authors argue this is unavoidable, not a defect specific to their approach: the information is genuinely required to sign the welfare effect once other markets are distorted.

## Bears On

- **[Deadweight Loss](/wiki/deadweight-loss/)** — this paper is the source for the qualification, now added to that page, that the textbook Harberger-triangle exposition implicitly assumes every other market is undistorted, and that this assumption fails once market power or taxation is widespread.
- **[Objection: LVT is just a property tax with extra steps](/wiki/lvt-is-just-a-property-tax/)** — that page's efficiency argument for a land-only base rests on land's fixed supply, a property this paper's mechanism (reallocation of a variable input across distorted markets) does not disturb; see Relation to the Georgist Case above.

## See Also

- [Deadweight Loss](/wiki/deadweight-loss/) — the textbook Harberger-triangle formula this paper extends
- [Tideman & Plassmann, Losses of Nations (1998)](/wiki/tideman-plassmann-losses-of-nations/) — the movement's own general-equilibrium-style deadweight-loss calculation, for taxes on labour and capital rather than commodities
- [Objection: LVT is just a property tax with extra steps](/wiki/lvt-is-just-a-property-tax/)
- [Pigouvian Taxation](/wiki/pigouvian-taxation/)

## Sources

1. Till Gross and Paul Klein, "A New Partial-Equilibrium Approach to Approximating the Welfare Effects of Market Power and Taxes," *Journal of Economic Behavior & Organization* (2026), DOI [10.1016/j.jebo.2026.107747](https://doi.org/10.1016/j.jebo.2026.107747) — used for the core formula, all numerical examples (Tables 1, 2, 4, 5, and 6), and the Dixit-Stiglitz derivations (B-claim: peer-reviewed article, text read from the June 16, 2025 working-paper version; the published pagination was not consulted).
2. Arnold C. Harberger, "Three Basic Postulates for Applied Welfare Economics: An Interpretive Essay," *Journal of Economic Literature* 9(3) (1971), pp. 785–797 — used, via the quotation carried in Gross and Klein (p. 3), for Harberger's own acknowledgment that applied welfare studies rarely account for distortions in other markets (B-claim; quoted secondhand from the working paper, not read directly).
3. Lawrence H. Goulder and Roberton C. Williams III, "The Substantial Bias from Ignoring General Equilibrium Effects in Estimating Excess Burden, and a Practical Solution," *Journal of Political Economy* 111(4) (2003), pp. 898–927 — used, via Gross and Klein's discussion and their Table 6 comparison, for the alternative formula that accounts for a commodity tax's effect on the labour market (B-claim; the comparison numbers are Gross and Klein's, not independently recomputed from Goulder and Williams directly).
