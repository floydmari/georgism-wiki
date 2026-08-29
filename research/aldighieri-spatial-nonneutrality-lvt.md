---
authors:
- Pedro Aldighieri
bears_on_objections: []
category: research
excerpt: "Arnott & Stiglitz (1979) showed a 100% land value tax finances public goods without distortion — but that result depends on spillovers being fully local to a parcel. When assessed land value capitalizes neighbors' spillovers, LVT becomes an 'inverse Pigouvian subsidy': it rewards merging parcels under positive spillovers and splitting them under negative ones. Cook County parcel-split/merger data (2001–2023) confirms the predicted pattern."
last_reviewed: 2026-08-29
source_url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7107758
stub: false
subcategory: wiki-research-lvt
tags:
- research
- land-value-tax
- spatial-economics
- externalities
- henry-george-theorem
- assessment
tier: important
title: "Drawing the Line: The Spatial Non-Neutrality of Land Value Taxation (Aldighieri, 2026)"
year: 2026
---

## Summary

"Drawing the Line: The Spatial Non-Neutrality of Land Value Taxation," by **Pedro Aldighieri**
(Northwestern University), is an SSRN working paper (posted July 2026) that identifies a
specific, technically serious limit on land value taxation's canonical efficiency result — the
[Henry George Theorem](/wiki/henry-george-theorem/)'s ancestor result, [Arnott &
Stiglitz (1979)](/wiki/arnott-stiglitz-henry-george-theorem/), which showed a 100% LVT can
finance local public goods without distortion.

## The Mechanism: An "Inverse Pigouvian Subsidy"

Per the paper's own abstract: "This result fails once assessed land values capitalize
neighboring spillovers, which enter the base only when they cross property lines." Because
[mass appraisal](/wiki/mass-appraisal-methods/) methods estimate a parcel's land value partly
from the value of *neighboring* land — spillovers a parcel's own boundary does not fully
contain — the tax base itself becomes sensitive to what happens next door. The paper shows
this creates two distortions: an LVT "favors merging parcels under positive spillovers and
splitting under negative ones, and subsidizes externalities that depress neighbors' assessed
land, functioning as an inverse Pigouvian subsidy." In other words, an owner whose land use
imposes a negative externality on neighbors (noise, blight, pollution) sees *their own*
assessed value fall less than the harm they cause, since the harm is partly capitalized into
the *neighbors'* assessments instead — a subsidy to negative-spillover generators, and by the
same logic a penalty on positive-spillover generators, running exactly backward from what a
Pigouvian tax/subsidy scheme would want.

## Empirical Test

The paper tests this with a difference-in-differences design using **Cook County (Chicago)
parcel splits and mergers, 2001–2023**: if the mechanism is real, merging two parcels should
change how spillovers capitalize into the resulting single assessment differently than
splitting one parcel into two. Per the abstract, the empirical results "confirm the required
mechanism: assessed land values move in opposite directions, reversing between nuisance and
positive-spillover exposures" — direct evidence that assessed land values respond to the
predicted parcel-boundary effect rather than tracking a spillover-free, purely site-specific
value.

## Relation to the Georgist Case

This is a genuine, technical qualification to LVT's textbook neutrality claim, in the same
family as [Bentick & Mills' timing-neutrality critique](/wiki/bentick-mills-timing-neutrality/)
(a research page) already cited on the wiki's [tax capitalization](/wiki/tax-capitalization/) page: both show that a
tax on *assessed value* rather than pure, spillover-free site rent can introduce real
distortions the "LVT is neutral" slogan glosses over. The mechanism here is specifically
about assessment methodology — how spillovers get captured across a parcel boundary — rather
than about the land tax concept itself, which is a useful distinction for the wiki's
[assessment feasibility](/wiki/land-cannot-be-assessed/) coverage: it is not that land value
can't be measured, but that measuring it accurately at the parcel level, with spillovers
correctly attributed, is harder than the textbook 100%-LVT result assumes.

## Nuances and Limits

- **A boundary/attribution problem, not a case against LVT generally.** The paper's own
  framing is about a *specific* failure condition (spillovers crossing property lines) rather
  than a wholesale rejection of land value taxation's efficiency case.
- **Abstract-level source (B-claim).** SSRN blocked direct access to the paper itself; this
  page is built from the paper's verbatim abstract (obtained via the Crossref API) and
  independent corroboration of the author's institutional context (a Northwestern economics
  PhD student who has presented related work at Yale's Economic History Lunch series), not a
  read of the full empirical design, regression specifications, or magnitude of the effect.
- **A working paper, not yet peer-reviewed.**

## Bears On

- **Concept:** [Henry George Theorem](/wiki/henry-george-theorem/) — a technical limit case on the theorem's canonical no-distortion result, driven by spillover capitalization across parcel boundaries.
- **Concept:** [Tax Capitalization](/wiki/tax-capitalization/) — extends the page's existing "timing neutrality is contested at the margin" caveat with a second, spatial-neutrality qualification.
- **Concept:** [Mass Appraisal Methods](/wiki/mass-appraisal-methods/) — the mechanism depends specifically on how assessment methodology attributes spillover value across parcel lines.

## See Also

- [Henry George Theorem](/wiki/henry-george-theorem/)
- [Tax Capitalization](/wiki/tax-capitalization/)
- [Mass Appraisal Methods](/wiki/mass-appraisal-methods/)
- [Objection: Land Value Can't Be Assessed Accurately](/wiki/land-cannot-be-assessed/)

## Sources

1. Pedro Aldighieri (2026), "Drawing the Line: The Spatial Non-Neutrality of Land Value
   Taxation," SSRN Working Paper, DOI 10.2139/ssrn.7107758, posted July 2026.
   [papers.ssrn.com](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7107758) — fetch
   blocked (403) to this session 2026-08-29; verbatim abstract obtained via the Crossref API
   ([api.crossref.org/works/10.2139/ssrn.7107758](https://api.crossref.org/works/10.2139/ssrn.7107758))
   — used for the inverse-Pigouvian-subsidy mechanism, the Arnott-Stiglitz framing, and the
   Cook County 2001–2023 difference-in-differences design and result, all quoted directly
   from the abstract above (B-claim; abstract-level, full paper and empirical detail not
   read).
