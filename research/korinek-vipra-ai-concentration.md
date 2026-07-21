---
authors:
- Anton Korinek
- Jai Vipra
bears_on_objections:
- taxing-quasi-rents-kills-innovation
category: research
excerpt: 'The freshest official diagnosis of whether AI-firm profit is rent: foundation
  models combine massive fixed compute costs with near-zero marginal cost, a near-monopoly
  compute supplier (Nvidia), and talent bottlenecks — a textbook setup for ''monopoly
  rents,'' the authors'' own phrase.'
last_reviewed: 2026-07-18
source_url: https://www.ineteconomics.org/uploads/papers/WP_228-Korinek-and-Vipra.pdf
stub: false
subcategory: wiki-research-resources
tags:
- research
- artificial-intelligence
- market-concentration
- economic-rent
- antitrust
- compute
- data-rents
- geoism
- quasi-rent
tier: Important
title: 'Korinek & Vipra — Concentrating Intelligence: Scaling and Market Structure
  in AI'
year: 2025
---

## Summary

"Concentrating Intelligence: Scaling and Market Structure in Artificial Intelligence" is
**Anton Korinek** (University of Virginia, Brookings, NBER) and **Jai Vipra**'s (Centre for
the Governance of AI) analysis of competition dynamics in the foundation-model market — the
market for large language models such as GPT-4, Gemini, and Claude.[1] It circulated first as
an INET working paper (No. 228, October 2024, under the title "Market Concentration
Implications of Foundation Models: The Invisible Hand of ChatGPT" in its earliest draft) and
an NBER working paper (w33139), and has since been peer-reviewed and published in **Economic
Policy** 40(121), 225–256 (2025).[1] It is the direct successor, on the *diagnosis* side, to
[Korinek & Ng's earlier digital-superstars model](/wiki/korinek-ng-digital-superstars/) and to
the [Furman Review's](/wiki/furman-review-digital-competition/) 2019 warning that if the next
technology wave centers on AI, "the firms best placed to exploit it may well be the existing
large companies because of the importance of data" — a prediction this paper checks against
2023–24 evidence.

The paper's contribution to the wiki's [rent gradient](/wiki/geoism/) is a fresh, granular
answer to *what specifically* would make AI profit a rent rather than a competitive return:
extreme economies of scale in compute, a near-monopoly supplier of the physical input those
economies run on, and data/talent bottlenecks that compound first-mover advantage. But the
paper is explicit that, as of late 2024, none of this had yet produced a durable winner — the
market it describes is fiercely, even destructively, competitive.

## What It Establishes — the Diagnosis

**The cost structure is a classical natural-monopoly setup.** Foundation models combine a
**large fixed cost** for pre-training (Epoch (2024) estimates Gemini Ultra's 2023 training run
at $130 million) with **near-zero marginal cost** per query — "since fixed costs are high and
variable costs relatively low, foundation models offer a classical example of economies of
scale," compounded by economies of *scope* because one model serves many industries at
once.[1] Training compute for frontier systems has grown **4.1x per year for fifteen years**
(Epoch AI data reproduced in the paper), a trend the authors say could produce "trillion-dollar
foundation models" by the end of the decade if it continues.[1]

**The compute layer is genuinely, not just metaphorically, concentrated.** The chips that
train and run foundation models are supplied almost entirely by one company: the paper's own
Figure 3 puts **Nvidia at 92% of the GPU market**, and it cites a February 2024 Wells Fargo
estimate of **98% of the data-center GPU market** specifically.[1] This is the paper's
clearest, least-contestable rent-adjacent fact — a bottleneck input controlled by a single
firm sits upstream of every foundation-model producer's cost base.

**Talent is price-inelastic in the short run, compounding entry costs.** Because expertise in
frontier models takes years to acquire and because engineers cluster where the compute is,
"new entrants to the market often have to hire people who already work with market leaders and
pay a premium to induce them to switch" — a labor-market echo of the same increasing-returns
story.[1]

**"Monopoly rents" is the authors' own term for the tipping scenario.** Describing the
historical playbook of digital platforms (heavy early losses, a shakeout, a durable
winner), the paper writes: "the losses became unsustainable and led to a shake-out whereby a
single platform or a small number of platforms survived, became the dominant players, and
**started to earn significant monopoly rents**. The expectation of these profits was what led
to the large number of entrants."[1] The paper argues foundation models share the mechanisms
that produced that outcome for platforms — economies of scale and scope, data feedback loops,
user inertia — plus one AI-specific channel with no platform analogue: an **"intelligence
feedback loop,"** in which a lab with better internal models becomes faster at building the
*next* model, potentially "leave[ing] the competition ever further behind" and, in the limit,
producing what I.J. Good (1965) called an "intelligence explosion."[1]

**Vertical integration is already underway and compounds the concentration risk.** The paper
documents Google DeepMind's in-house TPU chips, Microsoft's and Amazon's in-house AI chip
programs, Microsoft's cloud exclusivity over OpenAI, and Google Cloud's preferred-provider
status for Anthropic, plus 2024 "acquisitions-by-proxy" — Microsoft hiring Inflection AI's
founders and staff via a $650 million licensing deal rather than a formal acquisition, which
the authors flag as "expected to lower [Inflection's] valuation and has drawn attention from
antitrust authorities since it may represent a take-over in disguise."[1] Four antitrust
authorities — the US FTC and DOJ, the UK CMA, and the EU Competition Commissioner — issued a
rare **joint statement** in July 2024 naming concentrated control of compute/data/talent
inputs, market-power extension, and anticompetitive partnerships as shared concerns, explicitly
motivated by "a sense that competition authorities were not sufficiently proactive" the last
time this happened with digital platforms.[1]

## But the Paper Is Equally Clear the Market Was Not Yet Tipped

The honest complication for the rent reading is that the paper's own snapshot of the market —
September 2024 — describes **fierce, ongoing competition, not a settled winner**. Fourteen
companies had matched or exceeded the original GPT-4's capability within a year of its release;
leading models were "clustered quite closely together" on the LMSYS benchmark (a 52% win
probability for the top model against the second-ranked one); and "prices charged by the
leading AI labs barely seem to allow them to cover their variable costs... the competition
dynamics seem close to **Bertrand competition**" — the textbook zero-economic-profit
outcome, the opposite of a rent.[1] The paper's own framing is conditional and forward-looking:
it identifies the *economic forces that could* produce concentration and monopoly rents, and
recommends *proactive* policy precisely because the authors think regulators moved too late
last time — not because they conclude the rent has already arrived.

**Policy remedies target the mechanism, not the profit.** The paper's own menu is
dissolve-the-moat, in the same register as the [Furman Review](/wiki/furman-review-digital-competition/)
and the [DMA](/wiki/dma-interoperability-dissolution/): mandated **data sharing** to blunt data
feedback loops (with an explicit warning that this can cut against privacy regulation such as
GDPR and can itself increase incumbents' data power if not designed carefully); policies that
reduce **switching costs** (aggregator subscriptions, common API standards); **disclosure of
model architectures** and public research investment to slow the intelligence feedback loop;
**stronger ex-ante merger review** given how fast intellectual property can move before an
acquisition can be unwound; and, as foundation models become more utility-like,
**non-discrimination requirements** modeled on public-utility law.[1] No rent tax, data
dividend, or ACE/DBCFT-style capture instrument appears in the paper's own remedy list — this
is a pure-dissolve diagnosis paper, structurally the AI-market analogue of the Furman Review.

## Relation to the Georgist Case — Both Ways

- **The rent reading gets a genuinely new mechanism, not a restatement of the platform case.**
  Unlike ordinary platform network effects, the paper's "intelligence feedback loop" describes
  a channel where the *first-mover advantage compounds through the technology itself* —
  better models make better models faster — which is a stronger tipping mechanism than
  anything in the older superstar-firms literature. And the near-monopoly compute layer
  (Nvidia at 92–98%) is a rent sitting *upstream* of every foundation-model firm, whether or
  not any individual AI lab ever earns one downstream — a distinct, verifiable rent claim that
  does not depend on resolving whether OpenAI's or Anthropic's own margins are rent or
  quasi-rent.
- **The efficiency/competition counter is carried by the same paper, not a rival source.**
  The Bertrand-competition observation — labs pricing near variable cost, a proliferation of
  near-substitute models, six-monthly leadership churn — is the paper's own evidence that as
  of the data available, the tipping the authors worry about had **not yet happened**. That is
  an unusually clean instance of the wiki's rent-gradient discipline: the same authors who
  supply the strongest mechanism for AI rent also supply the strongest evidence it has not yet
  materialized as realized profit.
- **The gradient-honest synthesis.** Read together with
  [Korinek & Stiglitz (2017)](/wiki/korinek-stiglitz-ai-rents/) — which theorizes that AI's
  *long-run* distributional gravity pulls toward whatever factor stays irreproducible — this
  paper supplies the *short-run, empirical* companion: a specific, checkable account of which
  inputs (compute above all) are concentrated today, and a call for **proactive** policy
  precisely because market tipping, once it happens, is expected to be hard to reverse. Neither
  paper claims current AI-lab profit already **is** rent at scale; both supply reasons a
  reader should expect the question to get more decidable, not less, over the coming years.

## Limits

- **A working paper turned journal article, not a competition-authority finding.** Although now
  peer-reviewed (*Economic Policy* 2025), the paper is an academic analysis, not a market
  investigation with subpoena power or access to firms' internal cost data; its cost and
  market-share figures are drawn from public estimates (Epoch AI, Wells Fargo, Fernandez et al.)
  that the authors themselves flag as approximate.
- **The 92%/98% Nvidia figures come from two different sources measuring slightly different
  things** (the paper's own Figure 3, sourced to Fernandez et al. 2023, versus a Wells Fargo
  estimate specifically for data-center GPUs) — both point the same direction but should not be
  quoted interchangeably as a single precise number.
- **The paper is explicitly a snapshot of September 2024** in a fast-moving market; the authors
  flag that "the technological landscape may change quickly," and the market structure should
  be re-checked against later evidence (e.g., subsequent DeepSeek, Grok, and open-source model
  releases) before this page's "not yet tipped" reading is treated as current.
- **Does not itself evaluate tax instruments.** This page covers the diagnosis only; for the
  authors' own view on how to *tax* AI rents if and when they materialize, see the companion
  paper [Korinek & Lockwood, "Public Finance in the Age of AI"](/wiki/korinek-lockwood-ai-public-finance/),
  read separately for this wiki.
- **Provenance.** Findings and quotations verified against the INET working-paper PDF (No. 228,
  October 2, 2024 revision), fetched and read in full this session; the published citation
  (*Economic Policy* 40(121), 225–256, 2025) is taken from the paper's own reference list in the
  companion Korinek & Lockwood (2026) manuscript, which cites it as published.

## See Also

- [Taxing Tech Rents — Instrument Comparison](/wiki/taxing-tech-rents/) — the graded synthesis this diagnosis feeds
- [Korinek & Lockwood — Public Finance in the Age of AI](/wiki/korinek-lockwood-ai-public-finance/) — the same research program's instrument-design companion (compute/token/robot taxes, sovereign wealth funds, windfall clauses)
- [Korinek & Stiglitz — AI and income distribution](/wiki/korinek-stiglitz-ai-rents/) — the long-run theory this paper's short-run market evidence complements
- [Korinek & Ng — digital superstars](/wiki/korinek-ng-digital-superstars/) — the predecessor model of digitization-driven superstar rents
- [Furman Review — Unlocking Digital Competition](/wiki/furman-review-digital-competition/) — the platform-era diagnosis this paper explicitly checks against the AI market
- [Rent Dissolution vs. Rent Capture: the Enforcement Record](/wiki/tech-rent-dissolution-vs-capture/) — the dissolve-pole remedies this paper's own policy menu belongs to
- [Platform and Data Rents](/wiki/data-rents/) · [Economic Rent](/wiki/economic-rent/) · [Quasi-Rent](/wiki/quasi-rent/)
- [Objection: Taxing quasi-rents kills innovation](/wiki/taxing-quasi-rents-kills-innovation/) — the incentive question this paper's Bertrand-competition evidence bears on directly
- [Geoism](/wiki/geoism/) — the rent-domain program and its gradient

## Sources

1. Anton Korinek & Jai Vipra (2024, rev. October 2, 2024), "Concentrating Intelligence: Scaling
   and Market Structure in Artificial Intelligence," Institute for New Economic Thinking
   Working Paper No. 228; published as Korinek & Vipra (2025), *Economic Policy* 40(121),
   225–256; also circulated as NBER Working Paper 33139.
   [INET PDF](https://www.ineteconomics.org/uploads/papers/WP_228-Korinek-and-Vipra.pdf) ·
   [DOI](https://doi.org/10.36687/inetwp228) · [NBER](https://www.nber.org/papers/w33139)
   — used for the cost-structure and economies-of-scale analysis; the Nvidia 92%/98% GPU-market
   figures; the talent-bottleneck mechanism; the "monopoly rents" quotation and the
   platform-shakeout analogy; the "intelligence feedback loop" mechanism; the vertical-integration
   examples (Microsoft/OpenAI, Google DeepMind TPUs, the Inflection AI "acquisition-by-proxy");
   the July 2024 four-authority joint antitrust statement; the Bertrand-competition observation
   and LMSYS clustering evidence; and the full policy-remedy menu (B/C-claims — a peer-reviewed
   working paper offering diagnosis and policy analysis, not a randomized or quasi-experimental
   empirical estimate; fetched and read in full this session).