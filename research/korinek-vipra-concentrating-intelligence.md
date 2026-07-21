---
authors:
- Anton Korinek
- Jai Vipra
bears_on_objections:
- taxing-quasi-rents-kills-innovation
category: research
excerpt: The wiki's first AI-rents anchor written after the foundation-model boom
  began. Korinek and Vipra trace how compute, data and talent economies of scale push
  the foundation-model market toward concentration — but their own evidence (Bertrand-like
  pricing, a 17-month new entrant reaching the top.
last_reviewed: 2026-07-17
source_url: https://www.nber.org/system/files/working_papers/w33139/w33139.pdf
stub: false
subcategory: wiki-research-resources
supports_outcomes:
- corporate-profits-increasingly-rents
tags:
- research
- artificial-intelligence
- foundation-models
- market-concentration
- natural-monopoly
- antitrust
- compute
- economic-rent
- geoism
tier: Important
title: 'Korinek & Vipra — Concentrating Intelligence: Scaling and Market Structure
  in Artificial Intelligence'
year: 2024
---

## Summary

"Concentrating Intelligence: Scaling and Market Structure in Artificial Intelligence"
(NBER Working Paper No. 33139, November 2024; an earlier draft circulated in September
2023 as "Market Concentration Implications of Foundation Models: The Invisible Hand of
ChatGPT"; subsequently published in *Economic Policy*, vol. 40, issue 121, January 2025,
pp. 225–256) is **Anton Korinek** (University of Virginia and NBER) and **Jai Vipra**'s
(Cornell) account of why the market for AI **foundation models** — the large,
general-purpose, pre-trained models such as GPT-4o, Gemini, Claude and Grok that
underlie the generative-AI boom — tends toward concentration.[1] It closes a real gap in
this wiki: the existing AI-rents anchor, [Korinek & Stiglitz (2017)](/wiki/korinek-stiglitz-ai-rents/),
theorizes AI's *long-run* distributional endpoint from before ChatGPT existed. This paper
was written in the thick of the foundation-model era it describes, dated to specific market
snapshots (September 2023, then November 2024), and it names the concrete mechanisms
— compute, data, and talent economies of scale, market tipping, vertical integration — that
could turn today's competition into tomorrow's rent.

The paper's own framing is conditional and forward-looking, not a claim about rents
already captured. Its abstract states that the cost structure of foundation models
"identifies significant economies of scale and scope that **may create a tendency towards
greater market concentration in the future**, exploring two concerns for competition, the
risk of market tipping and the implications of vertical integration, and evaluat[ing]
policy remedies that aim to maintain a competitive landscape. Looking ahead to
increasingly transformative AI systems, [the authors] discuss how market concentration
**could translate into unprecedented accumulation of power**, highlighting the broader
societal stakes of competition policy."[1] That hedged language — *may*, *could*,
*tendency* — is itself the central fact for this wiki's [rent gradient](/wiki/geoism/):
Korinek and Vipra document the structural preconditions for AI rent, and evidence that the
market has not (yet) settled into one.

## Core Argument and Findings

**A fiercely competitive market, priced close to zero economic profit, as of the paper's
writing.** The authors' own market snapshot (dated November 4, 2024) is instructive
against a premature rent reading. The leading models were "clustered quite closely
together" on the LMSYS benchmark — ChatGPT-4o's win probability against fourth-ranked
Claude 3.5 Sonnet was only 57.7% — and "every single one" of the top labs had released
or updated its model within the prior three months.[1] On pricing: "Many observers note
that the prices charged by the leading AI labs barely allow them to cover their variable
costs... the competition dynamics seem to be close to **Bertrand competition**" — the
textbook zero-economic-profit benchmark, the opposite of rent extraction.[1] And on entry:
"The rapid ascent of xAI's Grok-2 into the top-3 within 17 months of the lab's founding
illustrates how **contestable** the market for frontier AI systems is for someone willing to
spend the requisite amounts."[1] A market with 16 labs surpassing the original GPT-4
within about a year of its release, in the authors' telling, does not currently look like a
rent position.

**Three inputs — compute, data, talent — generate real economies of scale and scope.**
Producing a foundation model has a large fixed cost of pre-training, a smaller fixed cost of
fine-tuning per application, and low variable ("inference") costs — "a classical example of
economies of scale," compounded by economies of scope because one general-purpose
model serves many industries.[1] Compute costs for frontier training runs have grown "by
a factor of 4.1x per year over the past 15 years," a trend the authors expect to continue for
several more years given semiconductor concentration and rising demand, even as
government programs (the US CHIPS Act, the EU Chips Act, large Chinese state funds)
race to expand supply.[1] High-quality public training text is running out, pushing labs
toward proprietary data and synthetic data generation, and the market for AI talent is
"price-inelastic" in the short run because expertise takes years to acquire — pushing
salaries and hiring costs up and drawing researchers out of universities (73% of AI PhDs
went into industry by 2022, versus 21% in 2004).[1] The authors conclude the section:
these "technological and economic factors contribute to substantial first-mover advantages
for current industry leaders," which have "preempted scarce assets crucial for AI
development."[1]

**Two mechanisms could turn scale economies into concentration.** (1) *Market tipping*:
digital platforms in the 2000s saw fierce early competition give way to a shakeout in which
"a single platform or a small number of platforms survived, became the dominant players,
and started to earn significant monopoly rents" — driven by economies of scale/scope,
network effects, data feedback loops, and user inertia.[1] Foundation models share the
scale/scope force but weaker network effects; the authors add a mechanism specific to AI,
an "intelligence feedback loop": a lab with better internal models makes faster progress on
its next model, which "would cause first-mover advantages to snowball, leave the
competition ever further behind, and create a large monopoly" in the limit.[1] They state
plainly that "the number of players that a market of a given size can support is shrinking
fast, creating a growing force towards **natural monopoly**," while noting this is offset by
the market itself growing.[1] (2) *Vertical integration*: AI labs are integrating upstream
with chip production (Google's TPUs) and cloud providers (Microsoft's exclusivity over
OpenAI's compute, Google Cloud for Anthropic), and downstream into office software and
app-store-like platforms (OpenAI's GPT Store); the authors flag exclusive contracts,
preferential early access (OpenAI gave GPT-4 early access to Stripe, Duolingo and Morgan
Stanley), and "nascent competitor" acquisitions as levers of power that large technology
companies already hold over AI labs today.[1]

**Policy remedies are dissolve-the-rent, not capture-the-rent.** The authors' menu is
almost entirely structural/regulatory: mandated data sharing and access to counter data
feedback loops, interoperability and common API standards to cut switching costs,
mandatory disclosure of research results and model architectures to counter the
intelligence feedback loop, merger review and scrutiny of exclusive contracts to blunt
vertical integration, and — their closest approach to treating AI as a rent-bearing
essential facility — **public-utility regulation**: "as foundation models become
increasingly integrated into the economy, they may come to resemble public utilities.
Non-discrimination requirements for access to these models, similar to those applied in
other essential industries, could avoid shutting out potential users."[1] They cite Lina
Khan's (2017) essential-facilities-doctrine argument — "compelling a monopolist to
provide easy access to competitors in an adjacent market" — as a candidate legal tool if
foundation models morph into gatekeeping platforms.[1] Every remedy is explicitly
qualified against AI-safety trade-offs: open-sourcing and mandatory disclosure, the
authors note, are "subject to safety caveats."[1]

**The conclusion states the open question, not a verdict.** "The market structure for
developing and deploying these models exhibits a strong tendency toward concentration,
driven by significant economies of scale and scope... Will we see a winner-take-all
scenario where a single dominant firm provides the AI substrate for major parts of the
global economy? Or will we experience a diverse ecosystem of AI providers?"[1] The
authors close by flagging that market concentration could eventually mean AI's gains
"concentrat[e]... among a small subset of stakeholders," a distributional worry that extends
beyond profit shares to "equitable access to AI-enabled tools, opportunities, and
resources."[1]

## Relation to the Georgist Case — the Frontier, Named Without Being Named

This is a pure industrial-organization and antitrust paper: it never engages the rent
literature, never mentions Georgism or land, and its authors do not intend a Georgist
argument. What it supplies the wiki is something [Korinek & Stiglitz (2017)](/wiki/korinek-stiglitz-ai-rents/)
could not: a market-structure diagnosis, written after the foundation-model era began,
of *why* AI infrastructure might behave like a rent-bearing asset — compute, data, and
elite talent function here as the scarce, hard-to-reproduce inputs whose control
concentrates over time, the general shape of every rent story, applied to a genuinely new
substrate. The paper's own "natural monopoly" finding — a shrinking number of viable
entrants as investment requirements rise faster than the market — is the closest analogue
in this literature to the fixed-supply logic that makes land the clean case; its account of
Microsoft's leverage over OpenAI and Google's over Anthropic describes asymmetric power
that already exists, prior to any full monopoly.

But the honest reading has to hold the line the wiki's rent gradient exists to hold. The same
paper that documents concentration *risk* documents, in the same breath, evidence
*against* current rent extraction: Bertrand-like pricing at or below variable cost, a cluster
of near-substitute frontier models, and a new entrant (xAI) reaching the top three within
17 months. Korinek and Vipra are describing a market whose current behavior looks like
textbook competition, and whose *structure* looks like it is heading toward concentration
— a claim about tendency and trajectory, not a claim that AI firms are today earning
location-rent-like unearned income. Where this paper's own remedies land — data
sharing, interoperability, disclosure mandates, merger review, non-discrimination rules —
is overwhelmingly the *dissolve* pole of the wiki's capture-or-dissolve menu (compare
[the Digital Markets Act](/wiki/dma-interoperability-dissolution/) and the
[Furman Review](/wiki/furman-review-digital-competition/)), not a fiscal rent-capture
instrument; only the public-utility/non-discrimination suggestion gestures toward treating
AI infrastructure as an essential facility, and even that is regulatory access, not a tax on
economic rent.

## Nuances and Limits

- **A working paper's market-structure taxonomy, not a rent estimate.** NBER w33139
  is explicitly "circulated for discussion and comment" and had not been peer-reviewed
  when this version was written; it offers no quantitative measurement of AI firms'
  markups, economic profit, or rent share — no equivalent of the markup/profit-share
  estimates the wiki cites for [corporate profits generally](/wiki/corporate-profits-increasingly-rents/).
  It establishes mechanisms and a directional prediction, not a measured magnitude.
- **The strongest counterargument is contestability and churn — and it comes from the
  authors' own evidence.** The market snapshot in this very paper (thin, Bertrand-like
  margins; 16 labs surpassing the original GPT-4 within about a year; xAI's rapid ascent)
  is itself the best case against reading current AI profits as rent. The authors also cite
  Joshua Gans (2024, NBER w32270) for the point that data feedback loops "do[] not
  necessarily guarantee market dominance" and can even favor lagging firms if returns to
  additional data diminish quickly enough[1] — a serious economist's dissent from the
  natural-monopoly reading, reported here as Korinek and Vipra's own characterization of
  Gans's argument rather than independently verified against Gans's paper, which this
  page has not read.
- **Quality-adjusted price declines cut the other way from a pure rent story.** The paper
  reports that OpenAI's model updates over roughly 20 months increased benchmark
  quality, tripled speed, expanded context length 16-fold, and cut the cost of a given
  amount of output by 92%.[1] Falling quality-adjusted prices during a period of rising
  investment is more consistent with the authors' innovation-and-competition reading than
  with rent extraction, though it does not settle what happens if and when the shakeout the
  paper warns about actually occurs.
- **The land-like "fixed factor" here is being deliberately unfixed.** Compute is
  physically scarce today (semiconductor manufacturing concentration, chip prices,
  government subsidies), which is the closest thing in this paper to land's fixed-supply
  logic — but unlike land, its scarcity is the target of tens of billions of dollars in
  public and private investment (the paper cites the US CHIPS Act's $50bn+ and the EU
  Chips Act's €43bn) explicitly aimed at expanding capacity.[1] A factor whose scarcity is
  being actively engineered away is not the textbook non-reproducible factor the land case
  rests on; this is the same quasi-rent-versus-true-rent line the wiki draws elsewhere on
  the AI frontier (see [Korinek & Stiglitz](/wiki/korinek-stiglitz-ai-rents/) and
  [taxing quasi-rents kills innovation](/wiki/taxing-quasi-rents-kills-innovation/)).
- **A dated snapshot in a fast-moving market.** The authors are explicit that their picture
  of "fierce competition" as of November 2024 was a sharp reversal from the
  single-firm-dominant market they described in their own September 2023 draft.[1] Any
  claim on this page about the "current" state of foundation-model concentration is dated
  to when the cited paper was written (November 2024), not evergreen; the market may
  have consolidated, fragmented further, or done both in different segments by the time a
  reader encounters this page.
- **Safety and competition can trade off against each other.** The authors flag, without
  resolving, that some of their own pro-competition remedies (open-sourcing frontier
  models, mandatory disclosure of architectures) carry AI-safety risks that could require
  sacrificing "maximizing consumer welfare by keeping the market competitive... in order
  to keep humanity safe."[1] This is a genuine tension in the authors' own policy menu, not
  a gap this page can resolve.
- **Provenance.** All quotations, figures, and section summaries above were taken from
  the NBER working-paper PDF of w33139 (November 2024 revision), fetched directly
  from nber.org and read in full this session. The subsequently published *Economic
  Policy* version (vol. 40, issue 121, January 2025, pp. 225–256) was not independently
  obtained or checked against this working-paper text for wording or content differences;
  claims here should be understood as sourced to the NBER working paper specifically.

## See Also

- [Korinek & Stiglitz — AI, Innovator Rents and Non-Distortionary Redistribution](/wiki/korinek-stiglitz-ai-rents/) — the companion long-run theory piece; this paper is its market-structure prequel, written after the foundation-model era began
- [Korinek & Ng — digital superstars](/wiki/korinek-ng-digital-superstars/) — Korinek's companion model of how digitization creates superstar-firm rents through near-zero marginal cost scaling
- [The Digital Markets Act — Dissolving the Platform Rent](/wiki/dma-interoperability-dissolution/) — the legislated version of the interoperability/data-access remedies this paper recommends for AI
- [Furman Review — Unlocking Digital Competition](/wiki/furman-review-digital-competition/) — the earlier digital-platform precedent (network effects, data returns to scale "tipping" markets) this paper explicitly models AI market tipping on
- [Gen-AI: Artificial Intelligence and the Future of Work (IMF SDN 2024)](/wiki/imf-gen-ai-future-of-work/) — the labor-exposure counterpart; this paper covers market structure, not exposure
- [OpenAI — Industrial Policy for the Intelligence Age](/wiki/openai-industrial-policy-intelligence-age/) — a leading AI lab's own policy proposal, worth reading against this paper's antitrust-focused remedies
- [Platform and Data Rents](/wiki/data-rents/) — the wider concept page this paper's compute/data/talent analysis extends into foundation models specifically
- [Corporate profits increasingly reflect economic rents](/wiki/corporate-profits-increasingly-rents/) — the broader claim this paper supplies a forward-looking, AI-specific mechanism for, without yet measuring AI rents themselves
- [Objection: Taxing quasi-rents kills innovation](/wiki/taxing-quasi-rents-kills-innovation/) — this paper's own evidence of thin-margin, contestable competition is double-edged: it questions whether AI profits are rents worth taxing today, while its concentration-risk analysis supports proactive competition policy against future rents
- [Economic Rent](/wiki/economic-rent/) · [Geoism](/wiki/geoism/) — the rent-domain program and its gradient

## Sources

1. Anton Korinek & Jai Vipra (2024), "Concentrating Intelligence: Scaling and Market
   Structure in Artificial Intelligence," NBER Working Paper No. 33139, November 2024
   (JEL D43, K21, L4, L86, O33); an earlier version circulated as "Market Concentration
   Implications of Foundation Models: The Invisible Hand of ChatGPT" (2023); published in
   *Economic Policy*, vol. 40, issue 121, January 2025, pp. 225–256.
   [NBER page](https://www.nber.org/papers/w33139) ·
   [PDF](https://www.nber.org/system/files/working_papers/w33139/w33139.pdf)
   — used for the cost-structure/economies-of-scale-and-scope analysis of compute, data
   and talent; the market snapshot (LMSYS bunching, Bertrand-competition pricing, xAI
   contestability); the market-tipping and vertical-integration concentration mechanisms
   and the "monopoly rents"/"natural monopoly"/intelligence-feedback-loop passages; the
   policy-remedies analysis (data sharing, interoperability, research disclosure, merger
   review, public-utility non-discrimination, the essential facilities doctrine, and the
   safety/competition trade-off); the compute cost-growth and CHIPS Act/EU Chips Act
   figures; and all verbatim quotes (C/D-claims — an unrefereed working paper's
   market-structure taxonomy and forward-looking policy analysis; fetched and read in
   full this session).