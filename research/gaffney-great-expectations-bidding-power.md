---
title: "Gaffney (2013): Great Expectations — How Credit Markets Twist Land"
category: research
subcategory: wiki-research-georgism
authors:
- Mason Gaffney
year: 2013
tier: important
source_url: https://masongaffney.org/essays/Great_Expectations.pdf
stub: false
tags:
- research
- mason-gaffney
- land-speculation
- land-monopoly
- credit-rationing
- bidding-power
- capitalization
- great-depression
- henry-george
excerpt: "A short 2013 essay giving Gaffney's clearest, most quotable statement of why cheap long-term credit lets 'Scrooge' out-bid 'Cratchit' 23.9-to-1 for the speculative component of land value — plus a distinct historical illustration of Henry George's land-as-cartel analogy drawn from Depression-era withholding schemes (NRA, AAA, Texas oil prorating, ALCOA)."
last_reviewed: 2026-07-18
---

## Overview

"Great Expectations: How Credit Markets Twist the Allocation and Distribution
of Land" is a short (2-page, ~1,600-word) essay Mason Gaffney dated 5-14-2013
and posted directly to his own website; no journal or conference venue is
indicated in the text, and this page treats it as an unpublished essay
accordingly.[1] It does two things: it supplies a concrete historical
illustration — largely new to this wiki's Gaffney corpus — of Henry George's
claim that land speculation produces cartel-like effects without a formal
cartel, and it derives a distinct, more accessible algebraic model of why
cheap long-term credit concentrates bidding power for speculative land in a
small class of buyers, worked through a vivid numerical example ("Scrooge"
vs. "Cratchit").

This is the wiki's fourth independently-sourced Gaffney statement of the
credit-access "strong hands" concentration mechanism, alongside the 1961,
1972–73, and 1973 derivations already covered on
[concepts/land-monopoly](/wiki/land-monopoly/) and
[research/gaffney-tax-reform-release-land](/wiki/gaffney-tax-reform-release-land/)
— see Standing and Limits below for why it is not a priority correction (it
is chronologically the *latest* of the four, not the earliest) but is kept
as its own page rather than folded into an existing one.

## Land Speculation as an Unwitting Cartel: A Depression-Era Illustration

Gaffney opens by restating Henry George's observation that aggregate land
speculation produces the same effects as a landowners' cartel — restricting
a resource from its full and best use — even without the formal collusion of
an actual cartel. He then illustrates the point with a cluster of Depression-
era examples not found elsewhere in the wiki's Gaffney corpus: Herbert
Hoover's "Associationism" and trade associations; FDR's National Recovery
Administration (NRA), whose Blue Eagle emblem marked participants "doing our
part" to hold up prices while "goods stuck glued to the shelves"; the
Agricultural Adjustment Administration (AAA), which paid farm landowners
(not tenants or workers) to retire land from production; cities and counties
that foreclosed on tax-delinquent land and then held it "in cold storage for
years" rather than releasing it to the market; Texas's oil-well "prorate"
limiting wells to 15 pumping days a month; and ALCOA's monopolization of
bauxite, holding it underground until wartime aircraft demand forced the
government to build up a rival producer (Reynolds).[1] Gaffney's point is
that all of these — quite different industries and mechanisms — share the
same underlying logic as land speculation: a resource is withheld from full
use because withholding, not intensive use, is what maximizes the holder's
return. (A-claim, historical illustration; D-claim, the unifying "cartel
logic" interpretation is Gaffney's own argument.)

## The Two-Part Capitalization Model

Gaffney's formal contribution is a reworking of the simple perpetuity
formula `V = a/i` (land value = annual rent ÷ interest rate) that most
Georgist writing uses as shorthand. He argues this hides several
assumptions — a single interest rate available to everyone, a single
forecast of future rent, and an unrealistic ability to think in infinite,
levelized time — and instead splits land's infinite future income stream
into two explicit parts:[1]

- **Part (a): the current use**, a levelized annual rent `a` running for a
  finite horizon of `n` years (Gaffney's illustrative example sets `n = 30`).
  Its present value is the ordinary Discounted Cash Flow Factor (DCFF),
  `[1 − (1+i)⁻ⁿ] / i`.
- **Part (b): everything after year `n`**, a levelized annual rent `b` (with
  `b ≥ a`, "and may well be >> a") running to infinity. Its present value at
  time zero is `1 / [i·(1+i)ⁿ]` — the ordinary perpetuity value `b/i` at
  year `n`, discounted back `n` years.

The key move is algebraic: the denominator of Part (b)'s present-value
factor contains `i` **twice** — once discounting the perpetuity itself, once
discounting it back to the present — so Part (b)'s value is a *sharply*
decreasing function of the interest rate `i`, far more sensitive than Part
(a)'s. Gaffney names the resulting asymmetry **"Financial Power"** or
**"Waiting Power"**: access to long-term funds at a low interest rate is
disproportionately more valuable for bidding on the *distant-future,
speculative* component of a land price than for bidding on its current-use
component. This is the essay's central claim: land speculation is not
simply "the rich can outbid the poor" in the abstract — it is specifically
the far end of a property's cash-flow tail where cheap long-term credit
delivers the largest edge.

Note what this model does *not* include: unlike the differential-
capitalization model on
[research/gaffney-tax-reform-release-land](/wiki/gaffney-tax-reform-release-land/)
(the "E4" 1973 paper), there is no property-tax variable `t` here, and no
explicit land-appreciation growth rate `g` — the futurity effect is captured
instead by splitting the *time horizon* into two additive terms. The two
models are complementary formalizations of the same "strong hands" intuition
from different angles (one shows how a *tax* equalizes Rich/Poor carrying
costs; this one shows how a *credit-access gap alone, with no tax at all*
produces enormous bidding-power disparity specifically for land's
speculative value), not one restating the other.

## Worked Example: Scrooge vs. Cratchit

Gaffney illustrates the model with a numerical table comparing two
individuals bidding for the same land: **"Scrooge,"** a retired banker with
access to long-term funds at 3% interest, and **"Cratchit,"** who must pay
10% for the same kind of funds.[1] Reproducing his Table 1's key results:

| | `i` | DCFF (Part a) | `1/[i·(1+i)³⁰]` (Part b factor) |
|---|---|---|---|
| Scrooge | 3% | 19.6 | 13.7 |
| Cratchit | 10% | 9.4 | 0.57 |
| Scrooge ÷ Cratchit | — | 2.1× | **23.9×** |

For the current-use component (Part a), Scrooge's cheaper credit gives him
only a 2.1-to-1 bidding advantage. But for the speculative, distant-future
component (Part b) — the part that dominates a speculatively-held parcel's
value — **Scrooge can bid 23.9 times what Cratchit can bid**.[1] Gaffney's
gloss: "This wide disparity is why the land market is so flawed, and
speculators, Scrooge-like, choose to withhold so much land from the
Cratchits of this world." He closes by rejecting the standard lender-side
justification (that poorer borrowers simply must pay a "risk premium" for
bad credit records) as a view "from the side of the lender class, who
butter their bread," arguing that from Cratchit's side the same disparity
is simply a penalty for being poor, most acute precisely when trying to buy
land from speculators who "preempt more than they need, or will ever
need."[1] (C-claim, theoretical model — the algebra is Gaffney's own,
internally consistent, and independently checked against the source PDF for
this page; D-claim, the closing distributional framing is Gaffney's own
argument, attributed.)

## Standing and Limits

- **Unpublished status.** This is a short essay posted to Gaffney's personal
  website with no indicated journal, conference, or book venue — not a
  peer-reviewed or independently edited work. It is treated here as an
  attributed primary source, not as settled academic consensus.
- **Not a priority correction.** The wiki already documents earlier, more
  fully worked formal derivations of the same credit-access "strong hands"
  mechanism: an algebraic original in Gaffney's 1961 "The Unwieldy
  Time-Dimension of Space" (see
  [concepts/land-monopoly](/wiki/land-monopoly/)), a fuller worked example in
  his 1972–73 "Sources and Taxation of Urban Land Rent" (see
  [research/gaffney-urban-land-rent](/wiki/gaffney-urban-land-rent/)), and
  the tax-and-appreciation-inclusive model in his 1973 "Tax Reform to
  Release Land" (see
  [research/gaffney-tax-reform-release-land](/wiki/gaffney-tax-reform-release-land/)).
  This 2013 essay is 40-52 years *later* than those — it is the most
  accessible and most quotable of the four statements, not the earliest, and
  is presented on this wiki as a companion illustration rather than as
  supplying new priority.
- **Illustrative, not measured.** Neither the Depression-cartel history nor
  the Scrooge/Cratchit table is an empirical test: the historical examples
  are asserted, not sourced to independent primary documentation within this
  essay itself (Gaffney does not cite, e.g., specific NRA or AAA
  administrative records), and the 3%/10% interest-rate gap in Table 1 is an
  illustrative assumption, not a measured credit-market spread. This page
  presents both as Gaffney's own attributed argument and worked example.
- **Native text, clean extraction** — no OCR artifacts; the essay's algebra
  was independently re-derived and checked against Table 1's reported values
  for this page (all seven columns reconcile).

## Bears On

- **Concept:** [Land Monopoly](/wiki/land-monopoly/) — a fourth,
  chronologically-latest but most quotable formal statement of the
  credit-access concentration mechanism, distinguished by its temporal
  (current-use vs. speculative-tail) decomposition rather than a
  tax-and-appreciation model.
- **Research:** [Gaffney (1973): Tax Reform to Release
  Land](/wiki/gaffney-tax-reform-release-land/) — a companion, not a
  duplicate: that page's differential-capitalization model isolates how a
  *property tax* equalizes Rich/Poor bidding power; this essay isolates how
  *credit access alone* (no tax) concentrates bidding power specifically in
  land's speculative-tail value.
- **Research:** [Gaffney (1993/2005): How Land Booms Destroy
  Capital](/wiki/gaffney-land-booms-destroy-capital/) — a companion
  Depression/land-boom-era illustration; that page's mechanism is about
  capital consumption once a boom is underway, this essay's Depression
  examples (NRA, AAA, Texas oil prorating, ALCOA) are about deliberate
  withholding of resources from use, the behavior the boom mechanism
  presupposes.
- **Benefit:** [LVT dampens land speculation](/wiki/lvt-dampens-land-speculation/) —
  the Scrooge/Cratchit model is theoretical elaboration of why speculative
  land-holding concentrates among well-financed buyers; carried as
  theoretical context, not added to that page's `supported_by` evidence
  list, per the wiki's standing convention for Gaffney-authored theoretical
  argument on benefit pages.

## See Also

- [Land Monopoly](/wiki/land-monopoly/)
- [Gaffney (1973): Tax Reform to Release Land](/wiki/gaffney-tax-reform-release-land/)
- [Gaffney (1972–73): Sources and Taxation of Urban Land Rent](/wiki/gaffney-urban-land-rent/)
- [Gaffney (1993/2005): How Land Booms Destroy Capital](/wiki/gaffney-land-booms-destroy-capital/)
- [LVT dampens land speculation](/wiki/lvt-dampens-land-speculation/)
- [Mason Gaffney](/wiki/mason-gaffney/)

## Sources

1. Mason Gaffney (2013), "Great Expectations: How Credit Markets Twist the
   Allocation and Distribution of Land," essay dated 5-14-2013, posted at
   masongaffney.org — used for all claims, the historical illustration, and
   the algebraic model and Table 1 figures on this page; read in full from
   the source PDF (native text, no OCR needed; Table 1's seven columns
   independently reconciled). [Free PDF
   (masongaffney.org)](https://masongaffney.org/essays/Great_Expectations.pdf);
   local mirror at `sources/gaffney/text/Great_Expectations.txt`.
