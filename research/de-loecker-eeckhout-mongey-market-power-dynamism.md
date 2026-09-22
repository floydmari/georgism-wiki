---
title: "Quantifying Market Power and Business Dynamism in the Macroeconomy"
category: research
subcategory: wiki-research-inequality
tags:
- research
- market-power
- markups
- business-dynamism
- general-equilibrium
- entry
- overhead-costs
- productivity-dispersion
- welfare
- federal-reserve
authors:
- Jan De Loecker
- Jan Eeckhout
- Simon Mongey
year: 2026
tier: Important
source_url: https://www.minneapolisfed.org/research/staff-reports/quantifying-market-power-and-business-dynamism-in-the-macroeconomy
stub: false
excerpt: "A Minneapolis Fed structural model finds rising markups, overhead costs, and weakening entry jointly drove US business dynamism down 1980-2023, producing a net 5% welfare and 6% output loss despite +15.5% reallocation gains. A working paper, not yet peer-reviewed."
supports_outcomes:
- corporate-profits-increasingly-rents
last_reviewed: 2026-09-22
---

## Summary

"Quantifying Market Power and Business Dynamism in the Macroeconomy" is a September 2026 paper by
**Jan De Loecker** (KU Leuven), **Jan Eeckhout** (UPF Barcelona), and **Simon Mongey** (Federal Reserve
Bank of Minneapolis), published as [Federal Reserve Bank of Minneapolis Staff Report
688](https://www.minneapolisfed.org/research/staff-reports/quantifying-market-power-and-business-dynamism-in-the-macroeconomy)
(DOI: [10.21034/sr.688](https://doi.org/10.21034/sr.688)), dated September 4, 2026. De Loecker and
Eeckhout are two of the three authors of ["The Rise of Market Power and the Macroeconomic
Implications"](/wiki/de-loecker-eeckhout-unger-markups/) (De Loecker, Eeckhout & Unger, *QJE* 2020), the
paper most responsible for the reduced-form finding that firm-level markups rose sharply after 1980. This
new paper is a different kind of exercise, not a restatement of that one: it builds a **general-equilibrium
model** of oligopolistic competition with heterogeneous firms and endogenous entry, and structurally
estimates it year by year on U.S. data from 1980 to 2023, in order to ask **why** markups rose and what
that rise did to welfare. Because the paper is a Federal Reserve staff report — a working paper carrying
the authors' own methodological rigor but not yet through journal peer review — its results are sourced
and framed on this wiki as strong but provisional evidence, not a settled finding.

## The Core Argument and Findings

**The model and its three channels.** The paper models a large economy of small markets, each populated
by a limited number of firms competing in oligopoly (Cournot in the baseline, with a Bertrand robustness
check), subject to a fixed operating cost. Firms differ in productivity, and a pool of potential entrants
decides each period whether to pay the fixed cost and produce. Within this structure, three underlying
"primitives" can independently drive up equilibrium markups: (i) greater **dispersion in the firm
productivity distribution** (σ) — a few firms pull far ahead of the pack; (ii) a rising **share of fixed
(overhead) versus variable costs** (φ) — firms need to spend more before they produce a unit of output;
and (iii) a decline in the **number of potential competitors** (M) — markets simply have fewer firms able
to contest them. The authors show, through comparative statics, that these three channels have different
and sometimes opposite implications for measurable data: a fall in the number of competitors raises
markups but *lowers* business dynamism (the rate of job reallocation across firms), while a rise in
productivity dispersion or fixed costs raises markups while *raising* reallocation — so a joint time series
on markups, cost composition, and business dynamism can separately identify which forces were actually
at work, without the model needing to define what a "market" is or measure market shares directly.

**Headline result: all three channels are needed.** Estimating the model on U.S. data from 1980 to 2023,
the authors find that no single channel fits the data — "we then estimate that all three channels are
necessary to explain these data between 1980 and 2023" (Abstract). Fixed costs rose, productivity
dispersion widened, and the number of potential competitors fell, together. The paper reads the declining
number of potential entrants as consistent with "an increase in the number of mergers and acquisitions"
and "increasingly slack antitrust enforcement policy in the U.S. and around the world," citing the prior
literature on this point; the model does not itself measure antitrust enforcement or merger activity, and
this reading is offered as context for the estimated decline in M rather than as a direct empirical test.

**Welfare and output: the net numbers.** The paper's central quantitative result is that the identified
1980–2023 changes produced **a 5 percent decline in welfare and a 6 percent decline in output** (Abstract;
Introduction, p. 2). This net number conceals a much larger set of offsetting forces: "substantial output
gains of +15.5% occur due to reallocation toward more productive firms, but these are more than offset by
more labor being tied up in fixed costs and increasing deadweight loss from markups" (Introduction, p. 2).
In other words, the same forces that shifted output toward more efficient firms also let those firms extract
more surplus from the shift than they would have under tougher competition.

**The wedge decomposition.** The authors formally decompose the net output and welfare changes into five
"welfare-relevant aggregate wedges": productivity, selection, overhead, markups, and misallocation, with
overhead, selection, and the markup wedge doing most of the work (Introduction, p. 2; Section 6, p. 33).
Isolating the markup and fixed-cost wedges alone, the paper finds they "would have led to around a 20
percent decline in output: 12 percent from markups, and 8 percent from the rise in fixed costs" — a decline
"half offset by the combined increase in productivity due to innate changes in the productivity
distribution... and better selection... of firms that enter" (Section 6, p. 33). The net 6 percent output
decline is thus a small residual sitting on top of much larger offsetting effects — a pattern the paper
states directly: "there is a much larger decline that is partly offset by the increase in productivity... Firms
in the tail have become more productive while incurring higher fixed costs. This has lead to fewer firms
entering, and those that do, keep more of those productivity gains as profits, resulting in higher deadweight
loss. The net effect is negative as more productive firms extract even more rents" (Section 6, p. 33). Welfare
follows a parallel decomposition and declines by "about the same amount," 5 percent (Section 6, p. 33).

**Fit against the raw data.** The model's estimated markup series rises from a sales-weighted average of
**1.21 in 1980 to 1.59 in 2023**, a 38.2-percentage-point increase (Section 5, p. 26) — broadly consistent
with, though not identical to, the QJE paper's separately-estimated 1.21-to-1.61 (1980–2016) series, since
the two papers use different sample windows and (in this paper's case) time-varying output elasticities. The
paper reports the labor share fell by 6.1 percentage points between 1980 and 2023 on raw annual data
(4.7 points on a smoothed basis, versus 3.5 points implied by the model); wages relative to total factor
productivity fell by 20 log points in both the model and the data; and employment (the prime-age
employment-population ratio) shows a trend decline of 6.9 log points, of which the model accounts for
"about three-quarters" (Section 5, pp. 26–27). None of these aggregate series were used to fit the model —
they are targeted only by the three primitive parameters {M, σ, φ} and are matched as an independent
validation check.

**Robustness.** The authors report the three-channel result and the welfare conclusion are robust to
estimating under Bertrand rather than Cournot competition, and to targeting a cost-weighted rather than
sales-weighted markup series (Abstract; Section 8).

## Relation to the Georgist Case

Like the companion [De Loecker, Eeckhout & Unger (2020)](/wiki/de-loecker-eeckhout-unger-markups/)
paper, this staff report matters to the Georgist case **without being about land at all**. A full-text check of
the paper's 70 pages, including the online appendix, finds **zero occurrences of the word "land" and zero
occurrences of "rent-seeking"** — the paper is entirely silent on real estate, location, or land rent as a
source of the market power or entry barriers it models. Rather than land-specific evidence, its relevance
here is as a further instance of the **generalization of economic rent** beyond land that this wiki's
existing Eeckhout pages already make: a persistent gap between price and cost, captured by firms holding
a scarce, non-produced advantage — here, market position rather than a parcel of land. The paper's own
authors use exactly that language for their result: in the conclusion, they write that welfare gains from
reallocating output to more productive firms are "more than offset by these firms' use of their dominance
to **extract rents from customers**" (Section 9, p. 39). That the paper's own authors — mainstream
industrial-organization and macro economists writing for a Federal Reserve audience, with no Georgist
framing — independently reach for the word "rent" to describe the wedge their model isolates is exactly
the kind of non-Georgist corroboration this wiki looks for; it should not be overclaimed as evidence for
land rent specifically, which the paper never addresses.

Beyond that parallel, the paper adds something the reduced-form 2020 QJE paper could not supply: a
**causal decomposition**, not just a measured pattern. Where the QJE paper documents that markups rose
and correlates that with declining labor share and dynamism, this paper's structural model attributes the
rise to specific, separately identified mechanisms — rising overhead costs, wider productivity dispersion,
and fewer potential competitors — and shows that the same forces which raise measured output (through
reallocation to more productive firms) are, on net, welfare-*reducing* once the accompanying markup and
overhead effects are counted. That is a more demanding empirical claim than "markups rose": it says the
economy would be measurably better off, by the model's own welfare metric, under the pre-1980 mix of
competition and cost structure, even though *output from reallocation alone* rose. This gives the wiki's
broader rentier-economy argument (see [The Rentier Economy](/wiki/the-rentier-economy/)) a
structural-model counterpart to the reduced-form and national-accounts evidence it already carries — at
the cost of resting on a specific, calibrated model rather than a direct measurement (see Nuances and
Limits).

## Nuances and Limits

- **Not yet peer-reviewed.** This is a Federal Reserve Bank of Minneapolis staff report dated September
  2026; as of this page's last review it has not been published in a peer-reviewed journal, unlike the 2020
  QJE paper. The wiki's usual pattern of tracking post-publication critiques (as on the
  [markups page](/wiki/de-loecker-eeckhout-unger-markups/), which documents the Traina, Basu, and
  Benkard–Miller–Yurukoglu disputes) has not had time to develop here; none exists yet because the paper
  is too recent, not because the paper is uncontested.

- **The number of competitors is model-inferred, not directly measured.** A central design choice of the
  paper is that it deliberately avoids defining a "market" or counting actual competitors or market shares;
  instead the number of potential entrants, M, is "solved for indirectly by taking the model to the data and
  fitting the moments" (Introduction, p. 3) — markups, the cost-composition share, and the job-reallocation
  rate. This is a genuine methodological strength for avoiding contestable market definitions, but it also
  means the paper's central "fewer competitors" finding is an inference from the model's fit to three
  aggregate time series, not a direct count of firms or entrants. The paper's own gloss on why M might have
  fallen — rising M&A activity and weaker antitrust enforcement — is drawn from citations to other
  literature, not measured within this paper.

- **A static, single steady-state-per-year model.** The authors are explicit that they solve a static model
  for tractability rather than a fully dynamic one with forward-looking investment, and that a single year's
  estimation takes about 20 days of computing time; they note this choice cannot capture dynamic
  investment stories such as the rollout of a national distribution network (their own examples: Walmart,
  Amazon) that raise a firm's productivity over time (Section 4, p. 21). The three-channel decomposition
  should be read as the best fit of a deliberately parsimonious model, not as a complete causal account.

- **Sample and scope.** As with the underlying markup data, the exercise draws on Compustat, meaning
  publicly traded U.S. firms; it does not directly cover privately held firms. The paper's welfare, output,
  and wedge numbers are specific to this model's assumptions (nested-CES preferences, a common
  cross-market elasticity, a common within-market elasticity) and to the U.S. economy 1980–2023; the
  authors do not claim the specific magnitudes generalize to other countries or periods.

- **No decomposition of why entry barriers rose, and no land component.** The paper identifies *that*
  potential competition fell and attributes plausibility to M&A and antitrust trends, but does not model
  zoning, real-estate costs, or any other location-based barrier to entry — land is absent from the analysis
  entirely, as the zero-occurrence text check above confirms. Readers should not read this paper as
  evidence that entry barriers are land-related; the paper simply does not address the question.

## Bears On

- **[Rent-Seeking](/wiki/rent-seeking/)** — the paper's own language ("extract rents from customers") and
  its markup wedge are a modern, structurally-estimated instance of the rent concept this page defines,
  generalized beyond land; the model additionally shows *why* the wedge opened (overhead, dispersion,
  entry), not just that it did.

- **[Economic Rent](/wiki/economic-rent/)** — the markup wedge the model isolates is, by the standard
  definition, a form of economic rent; this paper supplies a causal decomposition of what drove its
  post-1980 rise.

- **[Corporate profits increasingly reflect economic rents](/wiki/corporate-profits-increasingly-rents/)**
  — this paper adds a structural-model layer to that claim page's existing markup and profit-share evidence,
  showing the estimated rise is not explained by productivity dispersion alone but requires overhead-cost
  and competition changes as well.

- **[De Loecker, Eeckhout & Unger (2020) — markups](/wiki/de-loecker-eeckhout-unger-markups/)** — the
  companion reduced-form paper this one builds on and extends into a structural, causally-decomposed
  general-equilibrium setting; the two should be read together, with the 2020 paper establishing the
  markup pattern and this paper attempting to explain its causes and welfare consequences.

- **[Narrative: The Rentier Economy](/wiki/the-rentier-economy/)** — a structural-model complement to
  that narrative's existing reduced-form and national-accounts evidence for rising rent capture outside
  land.

## See Also

- [Jan Eeckhout](/wiki/jan-eeckhout/)
- [De Loecker, Eeckhout & Unger — The Rise of Market Power and the Macroeconomic Implications](/wiki/de-loecker-eeckhout-unger-markups/)
- [The Profit Paradox: How Thriving Firms Threaten the Future of Work](/wiki/eeckhout-profit-paradox/)
- [Corporate Profits Increasingly Reflect Rents](/wiki/corporate-profits-increasingly-rents/)
- [Economic Rent](/wiki/economic-rent/)
- [Rent-Seeking](/wiki/rent-seeking/)
- [Narrative: The Rentier Economy](/wiki/the-rentier-economy/)
- [Superstar Firms](/wiki/superstar-firms/)

## Sources

1. Jan De Loecker, Jan Eeckhout & Simon Mongey (2026), "Quantifying Market Power and Business Dynamism
   in the Macroeconomy," Federal Reserve Bank of Minneapolis Staff Report 688, September 4, 2026.
   [DOI: 10.21034/sr.688](https://doi.org/10.21034/sr.688) ·
   [Minneapolis Fed](https://www.minneapolisfed.org/research/staff-reports/quantifying-market-power-and-business-dynamism-in-the-macroeconomy) —
   the full 70-page PDF (including the online appendix) was read in full — used for every quantitative claim
   and quotation on this page, including the model structure and three channels (pp. 2–3, 13–18), the
   headline welfare/output result and +15.5% reallocation figure (Abstract; p. 2), the five-wedge
   decomposition and the 12%/8%/20% markup-and-fixed-cost figures (Section 6, p. 33), the markup and
   labor-share/wage/employment fit statistics (Section 5, pp. 26–27), the "extract rents from customers"
   quotation (Section 9, p. 39), and the confirmation that "land" and "rent-seeking" do not appear anywhere
   in the text. B-claim; a Federal Reserve staff working paper, not yet peer-reviewed at the time of this
   page's writing.

2. [Wiki: De Loecker, Eeckhout & Unger — The Rise of Market Power and the Macroeconomic
   Implications](/wiki/de-loecker-eeckhout-unger-markups/) — internal navigation only; records the
   companion 2020 *QJE* paper's reduced-form markup measure that this staff report builds on and its own
   measurement critiques (Traina 2018; Basu 2019; Benkard, Miller & Yurukoglu 2025), which bear on the
   markup data series both papers share.

3. [Wiki: Jan Eeckhout](/wiki/jan-eeckhout/) — internal navigation only; records the author's wider
   research program and biography.
