---
title: "Market Power in Artificial Intelligence (Gans, 2024/2026)"
category: research
subcategory: wiki-research-resources
tags: [research, artificial-intelligence, market-power, data, competition-policy, rent-seeking]
authors: [Joshua S. Gans]
year: 2024
last_reviewed: 2026-08-16
source_url: https://www.nber.org/papers/w32270
tier: important
stub: false
excerpt: "A survey by IO economist Joshua Gans of how market power emerges and persists across three distinct AI markets — training data, input data, and predictions themselves — arguing that whether data can be traded across firm boundaries is the single biggest determinant of whether AI markets stay competitive."
---

## Summary

"Market Power in Artificial Intelligence," by **Joshua S. Gans** (Rotman School of
Management, University of Toronto; NBER), circulated as [NBER Working Paper
32270](https://www.nber.org/papers/w32270) in March 2024 and later published in the
*Annual Review of Economics* (Vol. 18, 2026, first posted online 6 May 2026; DOI
10.1146/annurev-economics-051624-061832). Gans is a leading industrial-organization
economist of AI — co-author, with Ajay Agrawal and Avi Goldfarb, of *Prediction Machines*
and *Power and Prediction*, the standard "AI as cheap prediction" economic framing this
survey builds on. This paper is a genuinely new anchor for the wiki's AI-rents research
cluster: the existing pages (Korinek, Stiglitz, and collaborators) focus on redistribution
and tax design given AI-driven rents; this is the competition-policy question underneath
that literature — *do AI markets naturally concentrate, and why?*

## The Framework: Three Distinct Markets

Gans's central methodological move is to separate "the provision of AI" into three
markets that behave differently and call for different competition analysis:

- **Training data** — the data used to *build* a prediction algorithm in the first place.
  Gans treats this as the component that drives **entry**: an incumbent with a large
  training-data repository has a durable advantage in building superior models, a barrier
  new entrants must somehow clear. Crucially, Gans notes that data is **non-rival** — it
  can in principle be shared with entrants at zero marginal cost — so market power here
  is not a resource-scarcity story but an **incentive** story: incumbents choose not to
  share or sell their training data, even at a price, because doing so would erode their
  own competitive position.
- **Input data** — the ongoing, real-time data an algorithm needs to generate each
  individual prediction (e.g., current demand conditions). Gans treats this as the
  component that drives **within-market competitiveness** rather than entry: because
  input data is generated continuously, whether it can be shared or traded in an
  arms-length market determines whether rival firms' prediction quality converges or
  diverges over time.
- **AI predictions themselves** — markets where the product *is* the prediction, the
  closest current real-world example being platforms selling predicted match quality
  between advertisers and consumers (an application of Bergemann & Bonatti's 2015
  economics-of-data framework). Prediction-quality differences here translate directly
  into advertising-revenue differences between platforms with different underlying data.

## The Headline Finding

Across all three markets, Gans's conclusion converges on a single structural variable:
**whether functioning markets exist for trading data across firm boundaries**. Where data
can be bought and sold between firms, market power in AI provision is transient — rivals
can buy their way to competitive parity. Where no such market exists — because incumbents
refuse to sell, or because no institutional mechanism for data trading has developed — the
training-data and input-data advantages compound, and market power persists. The paper's
own conclusion is explicit that this is unresolved territory: "Precisely how market power
might impact the various markets that constitute the provision of AI is an open question,"
and Gans flags an unaddressed complication — firms integrated across two or more of the
three markets (training data, input data, predictions) may compound their advantage
through feedback loops even as that same integration requirement makes entry harder for
any rival who would need to compete in all three markets simultaneously to challenge them.

## Relation to the Georgist Case

This paper supplies the competition-economics half of a question the wiki's [rentier
economy](/wiki/the-rentier-economy/) narrative and [markup-rent
literature](/wiki/de-loecker-eeckhout-unger-markups/) leave open: when AI-sector profits
look like rents rather than returns to genuine innovation, *what specifically makes them
persist rather than compete away?* Gans's answer — non-rival data that incumbents
strategically withhold from trade — is structurally close to the Georgist land case in one
respect and sharply different in another. The similarity: in both cases, a fixed or
slow-to-replicate input (land; a training-data repository) grants a durable advantage
independent of ongoing effort. The difference, which Gans's own framework makes precise
and which this wiki should not blur: **land is truly non-producible and rival in use**,
while training data is **non-rival and, in principle, producible or licensable** — Gans's
whole policy-relevant finding is that the market-power outcome depends on an *institutional
choice* (does a data-trading market exist?) rather than on a physical scarcity constant.
That makes the AI case more tractable by policy than the land case in one sense (data
markets could in principle be built where land supply cannot be expanded) and less settled
in another (no consensus data-trading-market design yet exists, whereas the land case has
centuries of assessment and taxation practice to draw on).

## Nuances and Limits

- **Working paper, not a magnitude study.** This is a theoretical/survey paper organizing
  the relevant economic models (Hagiu & Wright 2023; Bergemann & Bonatti 2015, among
  others), not an empirical measurement of how much AI-sector profit is actually rent
  versus genuine returns to R&D and scale. It should be read alongside, not as a
  substitute for, empirical markup studies like [De Loecker, Eeckhout &
  Unger](/wiki/de-loecker-eeckhout-unger-markups/).
- **No land- or resource-rent framing in the original.** Gans's paper is entirely silent
  on land, location, or the Georgist rent tradition — the connection drawn in this page's
  "Relation to the Georgist Case" section is this wiki's own synthesis, not Gans's
  argument, and should be read as such (D-claim, interpretive).
- **Author disclosures.** Gans discloses paid speaking, consulting (including antitrust
  and IP consulting via Charles River Associates), book royalties on the AI-economics
  trilogy this paper builds on, and equity/advisory relationships with AI startups — noted
  in the paper's own front matter. This does not by itself undermine the survey's
  economics, but is worth recording given the paper bears on live antitrust policy
  questions.

## Bears On

- **Research:** [Korinek & Vipra: Concentrating Intelligence](/wiki/korinek-vipra-concentrating-intelligence/) — the redistribution/tax-design half of the AI-rents question; this paper supplies the competition-policy half of the same underlying concern.
- **Research:** [De Loecker, Eeckhout & Unger: The Rise of Market Power](/wiki/de-loecker-eeckhout-unger-markups/) — the empirical markup-rent evidence this paper's theoretical framework could, in principle, be tested against for the AI sector specifically.
- **Guide:** [Portal: The Rent Frontier](/wiki/portal-rent-frontier/) — the wiki's index of contested, non-land rent domains this paper's three-market AI-competition framework extends.

## See Also

- [Portal: The Rent Frontier](/wiki/portal-rent-frontier/)
- [Korinek & Vipra: Concentrating Intelligence](/wiki/korinek-vipra-concentrating-intelligence/)
- [De Loecker, Eeckhout & Unger: The Rise of Market Power](/wiki/de-loecker-eeckhout-unger-markups/)
- [Jan Eeckhout](/wiki/jan-eeckhout/)
- [Narrative: The Rentier Economy](/wiki/the-rentier-economy/)

## Sources

1. Joshua S. Gans (2024), "Market Power in Artificial Intelligence," NBER Working Paper
   32270 (March 2024); published as Joshua S. Gans (2026), "Market Power in Artificial
   Intelligence," *Annual Review of Economics* 18. [NBER PDF](https://www.nber.org/system/files/working_papers/w32270/w32270.pdf) ·
   [Annual Reviews (paywalled)](https://www.annualreviews.org/content/journals/10.1146/annurev-economics-051624-061832) —
   the NBER working-paper PDF (the free, open-access version; the Annual Reviews version
   of record is paywalled and returned a 403 to direct fetch) was downloaded and read in
   full 2026-08-16; used for the abstract, the three-market framework (training data,
   input data, predictions) and its entry-vs-competitiveness distinction, the
   non-rival-but-withheld characterization of training data, the data-trading-markets
   headline finding, the multi-market-integration complication, and the verbatim
   conclusion quotation. Author disclosures (consulting, royalties, equity/advisory
   relationships) are as stated in the paper's own front matter.
