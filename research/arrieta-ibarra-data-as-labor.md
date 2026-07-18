---
authors:
- Imanol Arrieta-Ibarra
- Leonard Goff
- Diego Jiménez-Hernández
- Jaron Lanier
- E. Glen Weyl
category: research
excerpt: 'The 2018 AEA Papers and Proceedings paper formalizing the ''data as labor''
  proposal: because a handful of platforms are the dominant buyers of user data, they
  hold monopsony power and capture users'' unpriced data contribution as an uncompensated
  input.'
last_reviewed: 2026-07-17
source_url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3093683
stub: false
subcategory: wiki-research-resources
tags:
- research
- data-rents
- platform-economy
- radical-markets
- monopsony
tier: Important
title: Should We Treat Data as Labor? Moving Beyond 'Free'
year: 2018
---

## Overview

This 2018 *AEA Papers and Proceedings* article by Imanol Arrieta-Ibarra, Leonard Goff, Diego Jiménez-Hernández, Jaron Lanier, and E. Glen Weyl formalizes the "data as labor" proposal that Lanier had earlier popularized informally in *Who Owns the Future?* (2013).[1] The authors argue that because a small number of dominant digital platforms are the near-exclusive buyers of the data individual users generate, those platforms hold **monopsony power**: they can set the terms on which data is supplied and compensate users with nothing beyond access to the service, capturing as profit the surplus value users' data creates.[1] Their proposed remedy is to build a genuine, priced labor market for data — ideally through collective bargaining structures the authors call "data labor unions" — rather than relying on take-it-or-leave-it terms of service.[1]

The paper is the academic anchor for Chapter 5 of Eric Posner and E. Glen Weyl's *[Radical Markets](/wiki/radical-markets/)* (2018), which popularized the argument for a general audience, and for this wiki's existing [Data as Labor](/wiki/data-as-labor/) concept page, which draws its central claims from this paper.[2]

## Significance

On the wiki's rent gradient, this paper sits at the **contested platform/data-rent frontier**: it treats a share of dominant-platform profit as an extractable rent on an unpriced input (user data) captured through monopsony power — an explicit analogy to land rent that is itself disputed. Whether platform profits are rent at all, as opposed to returns to genuine network effects and engineering investment, is not settled in the economics literature, and neither is how to value an individual user's data contribution or operate "data unions" at scale; no large working precedent exists.

## Nuances and Limits

- **The aggregation problem: an individual's data may be worth close to nothing on its own.** A
  recurring objection is that pricing data laborer-by-laborer misconceives where the value actually
  sits. In a philosophical treatment of the thesis, Julian David Jonker writes that "the marginal
  value of any individual's data to one of the platforms is very close to zero, since it is likely
  to account for a tiny amount of the accuracy of the algorithm and the popularity of the
  platform," which leaves an individual user "no credible threat of exit" and so "very little
  bargaining power over terms of service."[3] Formal economic theory reaches a parallel result from
  a different direction: modeling a data market with externalities across correlated users' data,
  Acemoglu, Makhdoumi, Malekian & Ozdaglar show that once one user has shared correlated
  information, "the platform will be able to acquire both users' data at approximately zero price"
  in equilibrium — the price does not reflect users' true valuation of privacy, because the value
  genuinely resides in the pooled, correlated dataset rather than in any single contribution.[4]
  Neither paper treats this as fatal to compensating data contribution in principle, but both treat
  individual-level pricing as the wrong unit of account — a problem this paper's proposed data
  labor unions are meant to solve by bargaining collectively rather than person-by-person, though
  neither Jonker nor Acemoglu et al. evaluates whether collective bargaining actually overcomes it
  (see the next two points).
- **Feasibility of "data labor unions" is the least-developed part of the proposal.** Economist
  David K. Levine's *Journal of Economic Literature* review essay of *Radical Markets* — the book
  that popularized this paper's argument — singles out the data-labor-union mechanism as
  underdeveloped. Quoting the book's own hedge that a union "could approach Facebook or Google and
  threaten a 'strike'... The technical details would be complex, but we can imagine a range of
  possible approaches," Levine's response is two words: "If only."[5] He is similarly unpersuaded by
  the paper's supporting claim that data may exhibit increasing rather than diminishing marginal
  returns, noting the authors themselves concede this only "may actually" be true, which he judges
  too thin a foundation for "an entire radical utopian proposal."[5] (Page numbers for this source
  are cited to the author's freely posted manuscript, not the AEA's typeset pagination.)
- **Substitutability can erode bargaining leverage precisely as it is most needed.** Even where a
  data-labor union could organize a "data strike," empirical simulations on a real recommender-system
  dataset by Vincent, Hecht & Sen find that "as datasets grow larger, data strikes become less
  effective" — because a large accumulated dataset makes any one contributor's, or subset's, data
  more substitutable by other users' data, which is exactly the dynamic a durable data-labor-union
  bargaining position would need to overcome as platforms and their datasets scale up.[6] The same
  study finds real near-term leverage is possible at smaller scale — a strike by a realistic ~30% of
  users can erase roughly half the gains from personalization on a moderate-sized dataset — so the
  substitutability problem is a matter of degree and dataset size rather than an absolute bar, but
  it points the wrong way for a scheme meant to check the largest, most data-rich platforms.[6]

## See Also

- [Data as Labor](/wiki/data-as-labor/) — the wiki's concept page for which this paper is the primary academic source
- [Radical Markets](/wiki/radical-markets/) — the book (Ch. 5) that popularized this paper's proposal
- [Jaron Lanier](/wiki/jaron-lanier/) — coauthor; originator of the underlying "siren servers" and data-as-labor framing
- [E. Glen Weyl](/wiki/e-glen-weyl/) — coauthor
- [Eric A. Posner](/wiki/eric-posner/) — Weyl's *Radical Markets* coauthor who popularized this paper's proposal

## Sources

1. Imanol Arrieta-Ibarra, Leonard Goff, Diego Jiménez-Hernández, Jaron Lanier & E. Glen Weyl (2018), "Should We Treat Data as Labor? Moving Beyond 'Free'," *AEA Papers and Proceedings* 108: 38–42, DOI: 10.1257/pandp.20181003 — used for the paper's monopsony diagnosis and data-labor-union remedy. [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3093683) · [AEA](https://www.aeaweb.org/articles?id=10.1257/pandp.20181003)
2. Eric Posner & E. Glen Weyl (2018), *Radical Markets: Uprooting Capitalism and Democracy for a Just Society*, Princeton University Press, Ch. 5 — used for the popularized book-length statement this paper anchors. [wiki summary](/wiki/posner-weyl-radical-markets/)
3. Julian David Jonker (2025), "Is Data Labor? Two Conceptions of Work and the User-Platform
   Relationship," *Business Ethics Quarterly* 35(2): 153–186, DOI: 10.1017/beq.2024.25 — used for
   the "marginal value... very close to zero" and "no credible threat of exit" quotations in
   Nuances and Limits (author's manuscript p. 13; final-journal pagination may differ). Fetched and
   read this session. [Author's free PDF, Wharton Legal Studies & Business Ethics faculty page](https://faculty.wharton.upenn.edu/wp-content/uploads/2017/09/iDL-BEQ-published-version.pdf) ·
   [Cambridge Core](https://www.cambridge.org/core/journals/business-ethics-quarterly/article/is-data-labor-two-conceptions-of-work-and-the-userplatform-relationship/15E922A1132C86474545D35F7F58426D)
4. Daron Acemoglu, Ali Makhdoumi, Azarakhsh Malekian & Asu Ozdaglar (2022), "Too Much Data: Prices
   and Inefficiencies in Data Markets," *American Economic Journal: Microeconomics* 14(4): 218–256,
   DOI: 10.1257/mic.20200200 (earlier circulated as NBER Working Paper No. 26296, September 2019) —
   used for the aggregation/marginal-value objection in Nuances and Limits: data externalities
   across correlated users drive an individual's own data price toward zero in equilibrium (quoted
   passage, p. 2 of the NBER working-paper text), because the value resides in the correlated,
   pooled dataset rather than any one contribution. Fetched and read this session.
   [NBER working paper (free PDF)](https://www.nber.org/system/files/working_papers/w26296/w26296.pdf) ·
   [AEA](https://www.aeaweb.org/articles?id=10.1257/mic.20200200)
5. David K. Levine (2020), "Radical Markets by Eric Posner and E. Glen Weyl: A Review Essay,"
   *Journal of Economic Literature* 58(2): 471–487, DOI: 10.1257/jel.20191533 — used for the
   feasibility critique of data labor unions in Nuances and Limits, including the "If only"
   dismissal of the book's own union-formation sketch and the skepticism toward the
   increasing-returns-to-data claim (quoted passages, pp. 13–14 of the author's freely posted
   manuscript version, whose pagination differs from the AEA's typeset pp. 471–487). Fetched and
   read this session. [Author's free PDF](http://board.dklevine.com/papers/radical.79.pdf) ·
   [AEA](https://www.aeaweb.org/articles?id=10.1257/jel.20191533)
6. Nicholas Vincent, Brent Hecht & Shilad Sen (2019), "'Data Strikes': Evaluating the Effectiveness
   of a New Form of Collective Action Against Technology Companies," *Companion Proceedings of The
   Web Conference 2019 (WWW '19)*, pp. 1931–1943 — used for the substitutability point in Nuances
   and Limits: simulated data strikes on a real recommender-system dataset lose effectiveness as
   the underlying dataset grows larger (quoted passage, p. 1942), while a realistic ~30%-of-users
   strike still erases roughly half the gains from personalization on a moderate-sized dataset.
   Fetched and read this session. [Author's free PDF](https://brenthecht.com/publications/thewebconference2019_datastrikes.pdf) ·
   [ACM DL](https://dl.acm.org/doi/10.1145/3308558.3313742)