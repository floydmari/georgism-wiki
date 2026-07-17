---
title: "Equal Land Share"
category: concepts
tags: [concepts, citizens-dividend, land-value-tax, predistribution, equal-land-share]
stub: false
excerpt: "A predistributive formulation of Georgist rent-sharing: set each citizen's equal per-capita share of national land value as a threshold — those holding less receive payments in proportion, those holding more pay in. One straight-line schedule, no separate tax and dividend."
last_reviewed: 2026-07-17
---

> **Status: proposal under development.** This page formulates and analyzes a scheme
> proposed by [Floyd Marinescu](/wiki/floyd-marinescu/) (2026). Its components are each
> well-attested in the literature cited below; the combined single-instrument
> formulation does not appear as a named proposal in the corpus this wiki has surveyed.

## Definition

The **equal land share** scheme starts from the Georgist premise that the value of
land — as distinct from the buildings and improvements on it — is created by nature
and by the community, not by the owner, and is therefore the equal common property of
all citizens (George 1879, Bk. VII; Paine 1797). It then implements that premise
directly, as a property settlement rather than as a tax-and-spend program:

1. **Compute the threshold.** Divide the nation's total assessed land value by its
   citizen population. Call this per-capita share **V̄** — the land value each citizen
   is morally entitled to.
2. **Net each person against the threshold.** A citizen whose attributed land value
   **V** is below V̄ *receives* an annual payment in proportion to the shortfall; a
   holder whose V exceeds V̄ *pays* in proportion to the excess. With an annual rate
   **r** (a fraction of land's rental yield), the net transfer is:

   **T = r × (V̄ − V)** — positive means receive, negative means pay.

A citizen who owns no land receives the full payment r·V̄ (the maximum — the position
of most renters); a citizen holding exactly the per-capita share neither pays nor
receives; payments from above-threshold holders fund the payouts, so the scheme
raises **zero net revenue** by construction — it is a pure transfer among citizens,
not a source of government funding.

## Formal Properties

**Equivalence to LVT plus citizen's dividend.** Algebraically, T = r·V̄ − r·V: the
scheme is *identical* to a flat-rate [land value tax](/wiki/land-value-tax/) at rate
r on every holding, combined with an equal [citizen's dividend](/wiki/citizens-dividend/)
of r·V̄ paid to every citizen — with the two flows netted into a single settlement.
Every incidence, efficiency, and capitalization result in the LVT literature
therefore carries over unchanged. (C-claim; follows directly from the definition.)

**One straight line — no kink.** The schedule superficially resembles Milton
Friedman's **negative income tax** (Friedman 1962, Ch. 12), which pays out below a
break-even income and collects above it. But the NIT schedule has a *kink* — the
marginal rate changes at the break-even point, which is where its work-incentive
problems live. The equal-land-share schedule is a single straight line through the
threshold: the marginal cost of holding one more dollar of land value is r
*everywhere*, above or below V̄. The threshold determines only who nets in or out,
never the marginal incentive — so the scheme inherits the LVT's neutrality (holding
land yields no return beyond its use value at full r; there is no gain to gaming
one's position around the threshold). (C-claim; theoretical.)

**A built-in majority of net recipients.** Land wealth is right-skewed — a minority
holds far more than the mean, so the mean exceeds the median and most citizens hold
less than V̄. The majority of citizens are therefore net *recipients* on day one.
This is the distributional finding of the wiki's LVT-progressivity evidence:
land ownership is concentrated at the top of the wealth distribution
([Saez & Zucman 2016](/wiki/saez-zucman-wealth-inequality/); see
[A land value tax can be progressive](/wiki/land-value-tax-can-be-progressive/)),
and [Common Wealth Canada's 2024 distributional modelling](/wiki/cwc-distributional-impacts-lvt/)
of a national LVT with a flat refundable credit — the same mathematics as this
scheme — found the credit turns the package progressive for most households.
(B-claim; empirical, via the cited distributional studies.)

**Netting minimizes gross fiscal flows.** Because only the *net* position moves
money, gross flows are far smaller than under separate tax-and-dividend
administration: a median homeowner slightly below V̄ receives a small cheque rather
than paying a large tax bill and receiving a large dividend. Detroit's proposed
land-value-tax credit design uses the same netting logic at municipal scale — a
credit guarantees no overall increase for below-break-even homeowners rather than
routing both flows separately (City of Detroit 2023). (D-claim; design analysis.)

![The equal-land-share payment schedule — one straight line through the per-capita threshold](/docs/figures/equal-land-share-schedule.svg)

![Net annual transfer by land-wealth decile — most deciles receive; the top decile pays most](/docs/figures/equal-land-share-deciles.svg)

*Both figures use illustrative round numbers (V̄ = $100,000 per citizen, r = 5%) and
an illustrative right-skewed decile distribution; they are not estimates for any
jurisdiction.*

## The Predistribution Framing

The scheme's proponents present it as **predistribution, not redistribution**: it
does not tax away the fruits of anyone's labor and hand them to others — the moral
vulnerability of income-based transfers — but settles who was owed what in the first
place. The framing has deep roots:

- **Thomas Paine** (1797) grounded his ground-rent-funded National Fund in exactly
  this distinction: every proprietor of cultivated land "owes to the community a
  ground-rent," and the payments funded from it are "not charity but a right"
  ([*Agrarian Justice*](/wiki/agrarian-justice/), held in full on this wiki).
- **Peter Barnes** (2014) applies it to modern commons dividends: "Dividends of this
  sort aren't redistribution; they're a way to allocate income fairly in the first
  place... they're legitimate property income" ([*With Liberty and Dividends for
  All*](/wiki/with-liberty-and-dividends-for-all/), Preface).
- **Hillel Steiner's "Global Fund"** is the closest structural precedent: in
  Steiner's left-libertarian theory of justice, every person is entitled to an equal
  share of all natural-resource values, and holders of more than their share owe
  payments into a fund disbursed equally — applied by Steiner at the level of
  nations rather than individual landholders (Steiner 1994; 2011). The equal land
  share is, in effect, Steiner's principle implemented domestically at the level of
  the individual citizen, with land value as the base.

The advocacy case for the framing: it asks nothing technical of the audience — no
tax rates, no revenue projections — only a moral judgment that each citizen is
entitled to an equal share of what none of them made. The schedule then follows
from the judgment by arithmetic.

## Design Questions

**Person-based, not parcel-based.** A conventional LVT is *in rem* — assessed on the
parcel regardless of who owns it. The equal land share must attribute land value to
*persons* to compute each citizen's V, which raises the question of land held
through corporations, trusts, and foreign owners. One design answer: give every
citizen a **land allowance** of V̄ (the analogue of a personal income-tax
allowance); land held by entities carries no allowance and pays the full rate r,
while citizens offset personally-attributed holdings against their allowance and
receive the unused balance in cash. Entity-held land is then taxed exactly as under
an in-rem LVT, and only owner-occupied and personally-held land needs attribution.
The difficulty of tracing beneficial ownership is real and documented — see
[the land-ownership-secrecy problem](/wiki/land-ownership-secrecy/). (D-claim;
design analysis.)

**The rate still exists.** Land *value* is a stock; the scheme transfers an annual
*flow*. The choice of r is the choice of how much of the rent is equalized: at r
equal to land's full rental yield, the entire annual value of holding more than
one's share is transferred, and the private return to holding land above one's
share — the speculative motive — is eliminated. Presenting the scheme as
"threshold plus proportion" moves the rate out of the moral foreground, but the
parameter remains, and assessments must be maintained exactly as under an LVT.

## Honest Limits

- **It raises no revenue.** The classic Georgist program uses captured rent to
  *replace* taxes on labor and capital (the [single tax](/wiki/single-tax/); the
  [Henry George Theorem](/wiki/henry-george-theorem/)). A pure equal-land-share
  settlement forgoes that gain entirely: existing taxes remain. Hybrids are possible
  (retain a fraction of collections for public revenue), but they reintroduce the
  tax framing the scheme is designed to avoid.
- **Transition effects are those of an LVT at rate r.** Above-threshold holders
  bear a one-time capitalized loss when the scheme is announced, exactly as under
  the equivalent LVT — the equivalence cuts both ways, and the standard transition
  objections (see [the transition-fairness objection](/wiki/lvt-hurts-asset-rich-cash-poor/))
  apply unchanged.
- **Attribution is harder than parcel taxation.** The person-based accounting that
  gives the scheme its moral legibility is also its main administrative cost
  relative to in-rem LVT.
- **Novelty caveat.** The wiki has not found this exact formulation in the
  literature, but its mathematical content — flat LVT plus equal dividend — is a
  standard proposal; claims made for the scheme should therefore be evaluated
  against, and inherit the evidence base of, that established package.

## See Also

- [Citizen's Dividend](/wiki/citizens-dividend/) — the tax-and-dividend form of the same mathematics
- [Land Value Tax](/wiki/land-value-tax/) — the levy side of the equivalence
- [A land value tax can be progressive](/wiki/land-value-tax-can-be-progressive/) — the evidence on who pays and who gains
- [Agrarian Justice](/wiki/agrarian-justice/) — Paine's "a right, not charity" predecessor, held in full
- [Milton Friedman](/wiki/milton-friedman/) — the negative-income-tax schedule the scheme visually resembles (and structurally improves on: no kink)
- [Land as Commons](/wiki/land-as-commons/) · [Geolibertarianism](/wiki/geolibertarianism/)

## Sources

1. Henry George, *Progress and Poverty* (1879), Bk. VII — used for the
   rent-as-common-property premise (A/C-claim). [Full text](/wiki/progress-and-poverty-full-text/)
2. Thomas Paine, *Agrarian Justice* (1797) — used for the ground-rent obligation and
   the "a right, not charity" predistributive framing (A-claim; public domain,
   held in full). [Text page](/wiki/agrarian-justice/)
3. Milton Friedman, *Capitalism and Freedom* (1962), Ch. 12 — used for the
   negative-income-tax schedule the scheme is contrasted with (A/C-claim).
   https://miltonfriedman.hoover.org/internal/media/dispatcher/271085/full
4. Hillel Steiner, *An Essay on Rights* (Blackwell, 1994) and "The Global Fund: A
   Reply to Casal," *Journal of Moral Philosophy* 8:3 (2011) — used for the
   equal-share-of-natural-resource-values principle with above-share holders paying
   in (C-claim). https://philpapers.org/rec/STET_F-5
5. Peter Barnes, *With Liberty and Dividends for All* (Berrett-Koehler, 2014),
   Preface — used for the dividends-as-predistribution framing (D-claim).
   [Book page](/wiki/with-liberty-and-dividends-for-all/)
6. Common Wealth Canada, *Distributional Impacts of a National Land Value Tax*
   (2024) — used for the finding that a flat refundable credit makes a national LVT
   progressive for most households (B-claim). [Research page](/wiki/cwc-distributional-impacts-lvt/)
7. City of Detroit, *Land Value Tax Plan* (2023) — used for the municipal netting/credit
   design precedent (A-claim). https://detroitmi.gov/departments/office-chief-financial-officer/land-value-tax-plan
