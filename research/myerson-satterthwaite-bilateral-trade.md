---
title: "Myerson & Satterthwaite (1983): Efficient Mechanisms for Bilateral Trading"
category: research
tags: [research, mechanism-design, bargaining, coase-theorem, holdout-problem, stub]
authors: [Roger B. Myerson, Mark A. Satterthwaite]
year: 1983
tier: Important
source_url: https://www.cs.princeton.edu/courses/archive/spr10/cos444/papers/myerson_satterthwaite83.pdf
stub: true
excerpt: "A mechanism-design paper showing no bargaining mechanism between a buyer and seller with private valuations can generally be simultaneously efficient, incentive-compatible, individually rational, and subsidy-free — cited against Coasean solutions to land assembly and holdout problems."
last_reviewed: 2026-07-11
---

## Summary

"Efficient Mechanisms for Bilateral Trading" is a 1983 article by **Roger B. Myerson** and **Mark A. Satterthwaite**, published in the *Journal of Economic Theory*, vol. 29, no. 2, pp. 265–281.[1] The paper studies bargaining between one buyer and one seller for a single object, where each side's valuation is a private, independently drawn random variable unknown to the other. Its abstract states the central result directly: the authors "characterize the set of allocation mechanisms that are Bayesian incentive compatible and individually rational, and show the general impossibility of ex post efficient mechanisms without outside subsidies."[1] This impossibility result is now known as the **Myerson–Satterthwaite theorem**.

## The Core Result

Under incomplete information about each party's true valuation, no trading mechanism can simultaneously guarantee: (1) an efficient outcome (trade happens whenever the buyer values the object more than the seller), (2) that honest revelation of valuations is each party's optimal strategy (Bayesian incentive compatibility), (3) that neither party is ever made worse off by participating (individual rationality), and (4) that the mechanism is self-financing, requiring no subsidy from an outside party — whenever there is a positive probability that trade is efficient for some valuations but not others (i.e., the buyer's and seller's valuation ranges overlap).[1] The paper also shows, for a wide class of problems, how to compute mechanisms that maximize expected total gains from trade or a broker's expected profit, and demonstrates that under symmetric uniform priors, a bargaining game studied earlier by Chatterjee and Samuelson achieves the maximal expected gains from trade obtainable under these constraints.[1]

## Relevance to the Georgist Case

The theorem is cited in Eric Posner and Glen Weyl's *[Radical Markets](/wiki/radical-markets/)* (Ch. 1, footnote) as a formal argument that private, unassisted bargaining cannot be relied upon to achieve efficient trades whenever the parties have private information about their own valuations — a direct qualification of the informal "Coase theorem" intuition that parties will generally bargain their way to an efficient outcome absent transaction costs.[2] This matters for the Georgist [holdout problem](/wiki/holdout-problem/) in land assembly: when an assembler needs many parcels from separate owners who each have private reservation prices, ordinary sequential bargaining is exactly the kind of bilateral-trade setting the theorem covers, and owners face a structural incentive to misrepresent their true valuations rather than reveal them honestly. This is part of the motivation for mechanism-design alternatives such as the Clarke-mechanism and self-assessment proposals analyzed in [Tideman & Plassmann's land-assembly paper](/wiki/tideman-plassmann-land-assembly/), and for self-assessed-value taxation schemes like the [Harberger tax](/wiki/harberger-tax/).

## Limits and Caveats

The theorem is a general impossibility result about **bilateral** trade (one buyer, one seller) under private information; it does not by itself say anything about multilateral land-assembly bargaining with many owners, nor does it establish that any *particular* real-world land negotiation fails to reach efficiency — it establishes only that no mechanism can be guaranteed to succeed across the full range of possible private valuations. It is a piece of formal bargaining theory adopted into the Georgist argument by analogy to the land-assembly setting, not a result derived from or tested against land markets specifically. [CITATION NEEDED: a source applying the Myerson-Satterthwaite framework directly and formally to multi-owner land assembly, rather than citing it as a general motivation.]

## See Also

- [Holdout Problem (Land Assembly)](/wiki/holdout-problem/) — the land-specific bargaining failure this theorem's logic is cited to motivate
- [Radical Markets](/wiki/radical-markets/) — the discovery-source book citing this paper against Coasean private-bargaining solutions
- [Ronald Coase](/wiki/ronald-coase/) — originator of the private-bargaining intuition this theorem formally qualifies
- [Providing Incentives for Efficient Land Assembly](/wiki/tideman-plassmann-land-assembly/) — a mechanism-design response to the holdout problem in the same tradition

## Sources

1. Roger B. Myerson & Mark A. Satterthwaite (1983), "Efficient Mechanisms for Bilateral Trading," *Journal of Economic Theory* 29(2), 265–281. Open-access PDF: [cs.princeton.edu/courses/archive/spr10/cos444/papers/myerson_satterthwaite83.pdf](https://www.cs.princeton.edu/courses/archive/spr10/cos444/papers/myerson_satterthwaite83.pdf) — verified verbatim this session (abstract and Theorem 1 statement) — used for the abstract's statement of the impossibility result, the model setup (single buyer/seller, private independent valuations), and the paper's additional results on gains-from-trade-maximizing mechanisms.
2. Eric Posner & Glen Weyl (2018), *Radical Markets: Uprooting Capitalism and Democracy for a Just Society*, Princeton University Press, Ch. 1. [Publisher](https://press.princeton.edu/books/hardcover/9780691177502/radical-markets) — discovery source book; cited (per this wiki's discovery notes) as invoking Myerson-Satterthwaite against Coasean assumptions about costless private bargaining.

`[VERIFY: item 2's exact footnote wording and page in Radical Markets was not directly re-read this session; the citation is carried from this wiki's existing discovery-report notes on the book. A future revision should confirm the precise footnote text against the source directly.]`
