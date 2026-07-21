---
authors:
- European Commission
- U.S. Department of Justice
- Federal Trade Commission
- Stigler Center Committee for the Study of Digital Platforms
bears_on_objections:
- taxing-quasi-rents-kills-innovation
category: research
excerpt: Land rent cannot be dissolved by competition — the supply is fixed, so capture
  is the only remedy. A platform rent sustained by artificial switching costs sometimes
  can be dissolved instead.
last_reviewed: 2026-07-18
source_url: https://digital-markets-act.ec.europa.eu/commission-finds-apple-and-meta-breach-digital-markets-act-2025-04-23_en
stub: false
subcategory: wiki-research-resources
tags:
- research
- antitrust
- digital-markets-act
- interoperability
- platform-economy
- data-rents
- geoism
- rent-gradient
- quasi-rent
tier: Important
title: Rent Dissolution vs. Rent Capture — the Enforcement Record on Antitrust, the
  DMA, and Interoperability
year: 2025
---

## Summary

[Taxing Tech Rents](/wiki/taxing-tech-rents/) grades five instrument families for capturing
platform rent and names antitrust/DMA/interoperability the **dissolve pole** — attack the
moat instead of taxing what it throws off. [The DMA itself](/wiki/dma-interoperability-dissolution/)
and the [Furman Review](/wiki/furman-review-digital-competition/) cover the *design* of that
pole in depth: what the DMA obligates gatekeepers to do, and the diagnosis (tipping, network
effects, durable positions) that justifies dissolving rather than taxing. This page does not
repeat that design walkthrough. It exists because both of those pages were written in 2026
against 2019–2023 material, and the two years since have produced the first hard evidence of
what dissolution *actually does* when enforced: the EU's first DMA fines and gatekeeper
compliance record (2025), a US federal court's rejection of a Google breakup in favor of forced
data-sharing (September 2025), an unresolved Google ad-tech remedies fight over structural
divestiture (2025–26), and an FTC loss that found no durable moat to dissolve at all
(November 2025). It also carries, at full strength, the honest counter-case the wiki's rent
gradient demands: dissolution is not free either, and courts, economists, and even Signal's
own security researchers have identified real costs — lost integration efficiencies, weakened
security, and a genuine possibility that some "moats" are actually just switching costs nobody
has bothered to lower.

## The Georgist Asymmetry: A Second Remedy Land Never Has

The wiki's [rent gradient](/wiki/geoism/) treats land as the case with only one lever. A site's
supply is fixed by nature; no policy can manufacture more usable land at a given location, so
the *only* way to deal with land rent is to **capture** it — tax it and either keep it public
or redistribute it, because the rent will exist and accrue to *someone* regardless of what the
state does. That is the entire argument for the [LVT](/wiki/land-value-tax/): capture is not
merely the best option, it is the only one that does not require conjuring competition that
cannot exist.

A platform moat is different in kind, and the difference is the whole reason this page and its
siblings exist. Where a "location" a business must pass through is held together by **artificial**
switching costs — data that cannot be exported, a messaging protocol that will not interoperate,
a default contract that forecloses rivals — the scarcity is not natural, it is *engineered*, and
engineering can in principle be undone. [Kades & Scott Morton (2020)](/wiki/dma-interoperability-dissolution/)
make the formal case: mandatory interoperability "could overcome the network effects that protect
the incumbent from entry," and because digital networks (unlike phone wires or rail track) carry
no marginal cost to interconnect, the opening itself is cheap even if the standard-setting is
not.[1] The Stigler Center's Committee for the Study of Digital Platforms — chaired by Fiona
Scott Morton, released September 2019 — reached the same design conclusion independently,
recommending Congress "tighten many US antitrust rules and impose interoperability among digital
platforms, similar to the way the US forced interoperability among phone companies, as a way of
weakening network effects," backed by a new Digital Authority empowered to "allow for data
portability and interoperability" and "promote open standards."[2] Two independent, non-Georgist,
mainstream expert panels — Furman's competition-law panel and Scott Morton's economics
committee — converged on the same diagnosis-and-remedy pair years apart: durable position, dissolve
by opening the network.

**Where dissolution genuinely works, it should beat capture on the wiki's own terms.** A
successful rent tax redistributes the rent; a successful dissolution *eliminates* it — the
consumer keeps the surplus a tax would have routed through the state, and the platform faces
the same competitive discipline every non-rent-earning firm faces. That is a stronger outcome
than any capture instrument in the [instrument comparison](/wiki/taxing-tech-rents/) delivers,
and it is available *only* because the platform case, unlike land, has an artificial-scarcity
component to unwind. **But the "artificial" qualifier is load-bearing.** Where the moat is a
*natural* network effect — a platform users prefer because more of their friends are already on
it, not because leaving is technically blocked — dissolution has nothing to attack: opening an
API does not make users leave a network they independently prefer, and forcing the attempt risks
only cost and fragmentation for no competitive gain. That is exactly the fork this page's
enforcement record and counter-case sections explore.

## The DMA in Enforcement: Two Years of Fines, One Contested Compliance Record

The DMA has moved from statute to enforcement history since [the DMA design page](/wiki/dma-interoperability-dissolution/)
was last substantially reviewed. Six gatekeepers were designated 6 September 2023 — Alphabet,
Amazon, Apple, ByteDance, Meta, and Microsoft, covering 22 core platform services — with
Booking.com added 13 May 2024 and Apple's iPadOS added 29 April 2024; Meta's Facebook
Marketplace was subsequently **un**designated on 23 April 2025 after Meta successfully argued it
no longer met the gatekeeper thresholds, showing the designation test is not one-way.[3]

**The first fines, and what they were actually for.** On 23 April 2025 the European Commission
issued its first two DMA non-compliance decisions. **Apple was fined €500 million** for breaching
**Article 5(4)**, the anti-steering obligation: developers must be able to inform users of
cheaper offers outside the App Store and direct them there free of charge, and the Commission
found Apple's technical and business terms continued to obstruct this. **Meta was fined €200
million** for breaching **Article 5(2)**: its "consent-or-pay" model — pay a subscription or
consent to combining personal data across services for ads — did not give users the "genuine
choice" the DMA requires between a less-personalized-but-free service and a fully consented one;
Meta's revised November 2024 model was, as of this page's research, still under separate
Commission assessment.[4][5] Both companies appealed to the EU **General Court** in mid-2025 —
Apple's appeal was formally filed 7 July 2025 — putting the fines' legal validity, not merely
their size, still in dispute as of this writing.[6]

**Technical compliance is arriving, but on a multi-year clock.** WhatsApp's headline DMA
obligation — Article 7 messaging interoperability — began rolling out in November 2025, nearly
20 months after gatekeeper designation: Meta enabled interoperable chat with two small European
challengers, BirdyChat and Haiket, describing the delay as "a three-year collaboration... to
develop a third-party chat solution" that preserves end-to-end encryption.[7] This is real
compliance — the first time a major messaging network has opened to outside apps under legal
compulsion anywhere — but it has so far reached two minor competitors, not Signal, Telegram, or
any rival with an installed base large enough to test whether interoperability actually erodes
WhatsApp's network effect.

**The one domain with a measurable market shift is the one with the lowest switching cost to
begin with.** Apple's and Google's browser-choice screens (required since March 2024) coincide
with real, if company-self-reported, gains for smaller browsers: Mozilla reports Firefox has been
selected "every 10 seconds across Europe," more than 6 million selections since the DMA took
effect, with Firefox's iOS daily active users up 99% in Germany and 111% in France over the same
period; other vendors (DuckDuckGo, Brave, Opera, Vivaldi) report parallel gains.[8] This is the
best real-world evidence to date that a DMA remedy has shifted user behavior at meaningful scale —
and it is also, per the counter-case below, exactly the case the interoperability skeptics
predicted would move: switching a *default*, not building or leaving a *network*.

**The domain the DMA opened but did not make people use is alternative iOS app stores.** Epic
Games launched its Epic Games Store on iOS in the EU in August 2024 with a public goal of 100
million installs by end-2024; it reported roughly 29 million — under a third of target — and
attributed the shortfall to Apple's "scare screens" and "Eligibility Requirements" warnings shown
during installation, which Epic says blocked more than half of attempted installs on some
measures, including an additional 5 million EU installs blocked outright.[9] This is a genuinely
important honest data point against a simple dissolution story: the DMA *legally* opened the
market, and adoption still stalled — either because Apple's friction (contested, and itself
under a separate, ongoing Commission investigation into "user choice obligations") suppressed
demand that would otherwise have materialized, or because most iOS users, even once free to
leave, preferred the incumbent store. The record as it stands cannot fully distinguish the two
explanations, and neither can this page.

## US Antitrust: Courts Choosing Data Access Over Divestiture — and One Case Where No Moat Was Found

The United States ran three major monopolization cases against platforms to a decision or
near-decision in 2025, and the pattern that emerged is a third path between full capture and full
dissolution: **forced data access and behavioral constraints, not corporate breakup** — plus, in
one case, a court concluding the alleged moat no longer exists.

**United States v. Google (Search).** After finding in 2024 that Google illegally maintained its
search monopoly, Judge Amit Mehta issued a 230-page remedies ruling on 2 September 2025 (with
additional implementation detail issued 5 December 2025) that **rejected the DOJ's request to
force Google to divest Chrome or Android**, explaining that "after two complete trials, this court
cannot find that Google's market dominance is sufficiently attributable to its illegal conduct to
justify divestiture," and separately that a Chrome divestiture would be "incredibly messy and
highly risky" and would disrupt an integrated product without directly remedying the exclusionary
conduct found unlawful.[10] He also cited the emergence of generative-AI competitors as a reason
to expect the market to become more contestable without a structural remedy. In place of
divestiture, the court **banned exclusive default-placement contracts** (Google may still pay for
default status, but not exclusively, and any such deal must run one year or less) and ordered
Google to **share search index and user-interaction data, and syndicate search and search-text-ad
results, with "Qualified Competitors"** on ordinary commercial terms for five years, capped at 40%
of a competitor's query volume in year one.[11] This is dissolution-by-data-access rather than
dissolution-by-breakup: it tries to let rivals build competing products on Google's own signal
without touching Google's corporate structure. Both Google and the DOJ have signaled appeals over
different parts of the ruling, so none of this is final.[10]

**United States v. Google (Ad Tech).** In a separate case in the Eastern District of Virginia,
Judge Leonie Brinkema ruled on 17 April 2025 that Google illegally monopolized the **publisher
ad-server** and **ad-exchange** markets (dismissing a third claim about advertiser ad networks for
lack of a distinct relevant market).[12] Unlike the search case, the DOJ here is seeking genuine
structural relief: divestiture of Google's ad exchange (AdX), with publisher ad server (DFP)
divestiture as a fallback if AdX alone proves insufficient, plus open-sourcing the ad-auction
algorithm and mandated interoperability APIs so rival ad servers and exchanges can plug in.[13]
The remedies trial ran September–November 2025 with closing arguments on 21 November 2025; as of
this research pass **no ruling has issued**, with observers expecting a decision sometime in
2026.[13] This is the live case to watch for whether a US court will order actual structural
dissolution rather than the data-access remedy chosen in the search case — an open question this
page cannot resolve and should be re-checked before being cited as settled.

**FTC v. Meta.** After a six-week bench trial, Judge James Boasberg ruled on 18 November 2025 that
the FTC had **failed to prove Meta currently holds monopoly power** in personal social
networking — regardless of whether it held that power when it acquired Instagram (2012) and
WhatsApp (2014) — because the relevant market now credibly includes competitors like TikTok and
YouTube that the FTC had argued should be excluded.[14] This is, on the ITIF/DLA Piper framing
several commentators used, the most decisive government loss across the current wave of US
platform cases. It matters for this page specifically because it is the one instance where a
court did not merely decline a remedy on cost-benefit grounds (as Mehta did) but found, on the
merits, that the alleged durable position **no longer exists** — competition itself may already
have partially dissolved the moat the FTC's 2020 complaint described. The FTC filed notice of
appeal to the DC Circuit in January 2026, so this is not the last word either.[15]

**Reading the three cases together.** No US court in 2025 ordered a platform broken up. Two
courts (Mehta on search, and implicitly the ad-tech case's emphasis on interoperability APIs as a
fallback to full divestiture) reached for data-sharing and interoperability remedies as the
preferred tool even where liability for illegal monopolization was found — a real-world
convergence, independent of the EU and unprompted by any Georgist framing, on exactly the
dissolve-the-moat-not-the-firm logic this page's opening section describes. And one court found no
moat left to dissolve at all. None of this is a verdict that dissolution "works" in the sense of
measurably lower prices or durable new entrants; it is a verdict about which *tool* American
judges currently prefer when they do intervene, and about how contested the underlying "is there
still a durable position here" question remains even after a full trial.

## The Counter-Case, Argued Honestly: What Dissolution Can Destroy

The wiki's rent-gradient discipline requires treating this as a genuinely two-sided question, not
a foregone Georgist conclusion that dissolution is costless where it is available. Three distinct
strands of the counter-case deserve full weight.

**Scale itself may be doing real economic work, not just entrenching a rent.** The Schumpeterian
tradition holds that large, insulated firms have both greater capacity (deep R&D budgets — "R&D
spending of American big tech firms exceeds the total R&D spending of many foreign nations," in
one 2025 synthesis) and greater incentive (protecting an existing position from disruption) to
innovate than small competitive firms do, and a meta-analysis of 95 empirical studies and 655
statistical estimates on firm size and innovation found an overall **positive** average
relationship, with concentration and innovation following an inverted-U rather than a simple
monotonic trade-off.[16] If dominant platforms' scale is genuinely productive rather than merely
extractive, a remedy that fragments that scale — whether by antitrust breakup or by forcing
interoperability that erodes the returns to building the best integrated product — risks
destroying real value on the theory that it is destroying only rent. Judge Mehta's own rejection
of Chrome/Android divestiture is the clearest applied instance of a court making exactly this
judgment: not that Google's conduct was lawful, but that unwinding the integration would cost
more than it would recover.

**Interoperability mandates work best exactly where they are needed least.** The International
Center for Law & Economics' analysis of network effects and interoperability argues that
mandates "have tended to focus on markets that already have low switching costs, hence limiting
potential gains" (payments apps, browsers) while the deepest moats — where switching costs are
genuinely high — are also where forced interoperability is hardest to implement without degrading
the product, and where **competition "for the market"** (aggressive pre-adoption pricing and
positioning) may already substitute for post-adoption compatibility.[17] The DMA's own record to
date is consistent with this critique on its face: the browser choice screen (low switching cost)
shows the clearest measurable effect; alternative app stores and messaging interoperability
(genuinely high switching cost) show the weakest uptake so far. That pattern is only two years of
data and could still change, but it points the same direction the ICLE argument predicts.

**Forced interoperability has real, technical security costs, not merely a hypothetical
trade-off.** Jenny Blessing and Ross Anderson's peer-reviewed-adjacent Cambridge analysis of DMA
messaging interoperability documents specific, concrete implementation problems: reconciling
different providers' content-moderation policies once messages cross platform boundaries,
authenticating users across federated systems, managing encryption keys when multiple providers
must exchange them, and controlling metadata leakage between competing services — problems the
authors frame as "open questions" without a demonstrated general solution, not solved
edge-cases.[18] Signal's own leadership has taken a similar position in public commentary:
interoperability is acceptable in principle only if there are no compromises "on the backend,"
and Signal states it will not lower its own security and metadata-protection standards to
interoperate with a weaker system — a private-sector veto, in effect, on the version of
interoperability that would maximize competitive reach.[19] Meta's own DMA compliance choice —
building its third-party bridge on the Signal protocol specifically, and taking three years to do
it — is itself evidence that the security concern is not merely rhetorical opposition dressed up
as engineering caution.

**None of this is a case that dissolution never works — it is a case that "moat" and "genuine
scale" are not always cleanly separable, and a regulator or court can get the call wrong in either
direction.** Epic's stalled iOS store adoption could reflect either Apple's obstruction (the
dissolution-favorable reading) or a genuine, if unwelcome, consumer preference for Apple's
integrated store (the counter-case reading); the evidence assembled here cannot fully adjudicate
between them, and this page does not pretend otherwise.

## The Georgist Reading

The asymmetry this page opened with survives the enforcement record, but with real caveats the
land case never carries. **Land admits exactly one remedy because its scarcity is natural; a
platform moat sometimes admits a second remedy because part of its scarcity is engineered** — and
where that is demonstrably true (Google's exclusive default contracts, Apple's steering
restrictions, WhatsApp's historical non-interoperability), courts and regulators on both sides of
the Atlantic have now, independently and without Georgist framing, reached for dissolution
instruments — forced data-sharing, anti-exclusivity rules, mandated interoperability — ahead of
either full corporate breakup or a rent tax. That convergence is itself evidence the wiki should
weigh: two different legal systems, applying ordinary competition law with no rent-capture
framing, arrived at "make the moat contestable" as the default answer once liability was found.

But the record two years in is honestly thin on the outcome that would matter most — **whether
the rent is actually being competed away, or merely relocated.** The browser-choice evidence is
the strongest available and it is company-self-reported, not independently audited, and measures
selections and DAU, not price or profit effects. The app-store and messaging-interoperability
evidence shows real technical compliance arriving on a multi-year lag with adoption far below
even the platforms' own targets. And FTC v. Meta is a live reminder that the prior question —
*is there still a durable position to dissolve at all* — can be litigated to a "no" outcome after
a full trial, exactly the honesty the wiki's is-it-rent gradient demands. The instrument
comparison's B grade for dissolution — "legislated, sidesteps quasi-rent, unproven" — still holds
after this update; unproven has simply acquired two more years of specific, checkable content.

## Honest Limits

- **No completed structural breakup exists to observe.** Judge Mehta's rejection of Chrome/Android
  divestiture means the strongest available real-world test of "does breakup destroy genuine scale
  efficiencies" has not happened; the Schumpeterian and ICLE counter-cases here are theoretical and
  cross-market inference, not a measured before/after on an actual platform breakup. The Google
  ad-tech case (still undecided as of this page) is the nearest live test and should be revisited
  once Judge Brinkema rules.
- **Browser-choice figures are vendor-reported, not independently verified.** Mozilla's 6-million-
  selection and DAU-growth figures are Mozilla's own claims; this page did not locate an independent
  dataset (e.g., StatCounter) confirming Safari's EU share loss at a comparable level of precision,
  and none is cited here as a fact rather than an attributed vendor claim.
- **The Epic Games Store adoption shortfall has two live, unresolved explanations** (Apple friction
  vs. genuine consumer preference) and the Commission's own investigation into Apple's "user choice
  obligations" was ongoing as of this page's research — its outcome should be checked before this
  section is treated as final.
- **Both major DMA fines are under active appeal** to the EU General Court; this page reports the
  Commission's findings and the fact of appeal, not a final adjudicated outcome.
- **The Google ad-tech remedies ruling had not issued** as of this research pass; whether the US
  produces its first real platform-breakup order in that case is unresolved and should be checked
  before citing this page for a US "no breakups" pattern.
- **FTC v. Meta is on appeal**, and this page's "no durable moat found" reading is one district
  court's finding, not a settled question — the DC Circuit could reverse on the market-definition
  question (whether TikTok/YouTube belong in the relevant market) that decided the case below.
- **This page does not re-litigate whether platform profit is rent or quasi-rent** — see
  [Platform and Data Rents](/wiki/data-rents/) and the Grades at a Glance on
  [Taxing Tech Rents](/wiki/taxing-tech-rents/) for that question, which this page's enforcement
  record does not resolve either way.

## See Also

- [Taxing Tech Rents — Instrument Comparison](/wiki/taxing-tech-rents/) — where dissolution is graded against the four capture instruments; this page is the enforcement-record deep dive behind that grade
- [The Digital Markets Act — Dissolving the Platform Rent by Mandated Interoperability](/wiki/dma-interoperability-dissolution/) — the DMA's design and legal mechanics, not repeated here
- [Furman Review — Unlocking Digital Competition](/wiki/furman-review-digital-competition/) — the diagnosis (tipping, durable positions) that justifies dissolution over taxation
- [Platform and Data Rents](/wiki/data-rents/) — the underlying rent-or-quasi-rent question this page's enforcement record does not resolve
- [Objection: Taxing quasi-rents kills innovation](/wiki/taxing-quasi-rents-kills-innovation/) — the objection dissolution sidesteps rather than answers, and the Schumpeterian scale argument this page's counter-case extends to antitrust remedies specifically
- [Digital Services Taxes as Actually Implemented](/wiki/digital-services-taxes/) · [Digital Advertising Taxes After Romer: Maryland's Real-World Test](/wiki/maryland-digital-ad-tax/) — the capture-pole instruments this page's dissolution record is measured against
- [Korinek & Stiglitz — AI and income distribution](/wiki/korinek-stiglitz-ai-rents/) — the frontier where dissolution has no obvious analogue (an AI compute/model moat is not a messaging protocol)
- [Geoism](/wiki/geoism/) — the rent gradient and the land/platform asymmetry this page develops

## Sources

1. Michael Kades & Fiona Scott Morton (2020), "Interoperability as a competition remedy for
   digital networks," Washington Center for Equitable Growth Working Paper. [Equitable Growth](https://equitablegrowth.org/working-papers/interoperability-as-a-competition-remedy-for-digital-networks/)
   — used for the "overcome the network effects" formulation and the low-marginal-cost-of-opening
   argument; full citation and additional context at [dma-interoperability-dissolution](/wiki/dma-interoperability-dissolution/).
2. Committee for the Study of Digital Platforms (Fiona Scott Morton, chair, Market Structure
   Subcommittee), *Final Report*, George J. Stigler Center for the Study of the Economy and the
   State, University of Chicago Booth School of Business, 16 September 2019.
   [Chicago Booth](https://www.chicagobooth.edu/research/stigler/news-and-media/committee-on-digital-platforms-final-report) ·
   summarized via [ProMarket](https://www.promarket.org/2019/09/17/how-to-rein-in-big-tech-stigler-committee-digital-platforms/)
   — used for the interoperability/data-portability/Digital Authority recommendations and the
   "impose interoperability... as a way of weakening network effects" formulation (report PDF was
   not machine-extractable this session; content corroborated via the committee's own press
   materials and ProMarket's summary of the report, both institutionally affiliated with the
   Stigler Center; C/D-claims).
3. European Commission, DMA gatekeepers portal (designation history). [Digital Markets Act](https://digital-markets-act.ec.europa.eu/gatekeepers-portal_en);
   corroborated via TechCrunch, "EU confirms six (mostly US) tech giants are subject to Digital
   Markets Act," 6 September 2023, [TechCrunch](https://techcrunch.com/2023/09/06/dma-gatekeepers-named/),
   and Library of Congress Global Legal Monitor coverage of the same designation — used for the
   six-gatekeeper roster, the Booking.com and iPadOS additions (2024), and the Facebook
   Marketplace un-designation (23 April 2025) (A-claims; fetched via search synthesis this
   session).
4. European Commission, "Commission finds Apple and Meta in breach of the Digital Markets Act"
   (press release, IP/25/1085), 23 April 2025. [Digital Markets Act](https://digital-markets-act.ec.europa.eu/commission-finds-apple-and-meta-breach-digital-markets-act-2025-04-23_en)
   — used for the fine amounts (€500m Apple, €200m Meta), the anti-steering and consent-or-pay
   findings, and confirmation that Meta's revised November 2024 model remained under separate
   assessment (A-claim; primary Commission statement; press-release HTML fetched this session,
   full legal decision text not independently retrieved).
5. Goodwin Procter, "10 Key Takeaways From the European Commission's Recent DMA Decisions Against
   Apple and Meta," June 2025. [Goodwin](https://www.goodwinlaw.com/en/insights/publications/2025/06/insights-practices-antc-10-key-takeaways-from-the-european)
   — used for the specific DMA articles breached (Apple: Art. 5(4) anti-steering; Meta: Art. 5(2)
   consent-or-pay) (A-claim; major law firm's client-alert analysis of the Commission decisions;
   fetched this session).
6. 9to5Mac, "Apple formally appeals €500 million DMA fine in the EU," 7 July 2025.
   [9to5Mac](https://9to5mac.com/2025/07/07/apple-formally-appeals-e500-million-dma-fine-in-the-eu/);
   Verdict, "Apple appeals EC's €500m fine over App Store restrictions" — used for Apple's General
   Court appeal date; Meta's appeal (reported as filed 4 July 2025 across multiple secondary
   sources consulted this session) is corroborated across search results but not independently
   confirmed against a single primary filing record, so its exact date should be re-verified
   before precise reuse (A/B-claims; journalistic sources; fetched via search synthesis this
   session).
7. Meta, "Messaging Interoperability: WhatsApp enables third-party chats for users in Europe"
   (Meta Newsroom), 14 November 2025. [about.fb.com](https://about.fb.com/news/2025/11/messaging-interoperability-whatsapp-enables-third-party-chats-for-users-in-europe/)
   — used for the BirdyChat/Haiket launch, the "three-year collaboration" framing, and the
   preserved end-to-end-encryption claim (A-claim; primary company statement, self-interested
   party reporting its own compliance; fetched via search synthesis this session).
8. Mozilla, "Browser choice? Here's how EU's DMA is helping make it real" (Mozilla Blog).
   [blog.mozilla.org](https://blog.mozilla.org/en/firefox/eu-digital-markets-act/) — used for the
   "every 10 seconds," 6-million-selections, and Germany (+99%)/France (+111%) iOS DAU figures
   (B-claim; vendor-reported outcome data, not independently audited; flagged in Honest Limits;
   fetched this session).
9. AppleInsider, "Epic Games shifts strategies in EU after missing app store goal by 71 million
   users," 23 January 2025. [AppleInsider](https://appleinsider.com/articles/25/01/23/epic-games-shifts-eu-app-store-strategy-after-missing-target-by-71-million-users);
   Epic Games, "App Store Economy is Far From Open" (Epic Games news). [Epic Games](https://www.epicgames.com/site/en-US/news/app-store-economy-is-far-from-open-despite-efforts-by-epic-developers-and-regulators-in-the-eu)
   — used for the 29-million-install figure against the 100-million target, the "scare screens"
   and Eligibility Requirements friction, and the 5-million-blocked-installs figure (B-claim;
   Epic is an interested party in active litigation and business competition with Apple, so its
   own framing of *why* adoption stalled is presented as Epic's claim, not adopted as fact;
   fetched via search synthesis this session).
10. Amit P. Mehta, U.S. District Judge, *United States v. Google LLC*, Memorandum Opinion on
    Remedies, D.D.C., 2 September 2025 (further detail 5 December 2025) — used for the rejection
    of Chrome/Android divestiture, the "cannot find that Google's market dominance is sufficiently
    attributable to its illegal conduct" and "incredibly messy and highly risky" language, and the
    AI-competition rationale (A-claim; primary opinion; text corroborated via CNBC, DLA Piper, and
    California Lawyers Association case commentary rather than independently machine-extracted
    from the opinion itself this session).
    [DLA Piper summary](https://www.dlapiper.com/en/insights/publications/2025/09/federal-court-orders-remedies-in-google-antitrust-case) ·
    [CNBC](https://www.cnbc.com/2025/12/05/judge-finalize-remedies-in-google-antitrust-case.html)
11. U.S. Department of Justice, "Department of Justice Wins Significant Remedies Against Google"
    (press release). [justice.gov](https://www.justice.gov/opa/pr/department-justice-wins-significant-remedies-against-google)
    — used for the exclusivity ban on default-placement contracts (≤1-year term), and the
    search-index/user-interaction data-sharing and syndication remedy for "Qualified Competitors"
    (five-year license, 40%-of-queries year-one cap) (A-claim; primary DOJ statement; fetched this
    session).
12. Leonie Brinkema, U.S. District Judge, *United States v. Google LLC* (ad tech), E.D. Va.,
    liability opinion, 17 April 2025 — used for the finding of unlawful monopolization of the
    publisher ad-server and ad-exchange markets and the dismissal of the advertiser-ad-network
    claim (A-claim; primary opinion; corroborated via Simpson Thacher's client summary,
    [stblaw.com](https://www.stblaw.com/about-us/publications/view/2025/04/25/district-court-rules-google-is-a-monopolist-in-ad-tech),
    rather than independently machine-extracted from the opinion this session).
13. MarketingBrew, "Google returns to court for remedy phase of DOJ ad-tech antitrust trial," 18
    September 2025, [MarketingBrew](https://www.marketingbrew.com/stories/2025/09/18/google-remedy-adtech-antitrust-trial);
    Norton Rose Fulbright, "What you need to know from closing arguments in US v. Google"
    [Norton Rose Fulbright](https://www.nortonrosefulbright.com/en/knowledge/publications/cb2c3ded/what-you-need-to-know-from-closing-arguments-in-us-v-google)
    — used for the AdX/DFP divestiture and open-source-algorithm/interoperability-API remedy
    proposals, the September–November 2025 remedies trial and 21 November 2025 closing-arguments
    date, and confirmation that no ruling had issued as of this research pass (A/B-claims;
    journalistic and law-firm sources; fetched via search synthesis this session).
14. James E. Boasberg, U.S. District Judge, *FTC v. Meta Platforms, Inc.*, D.D.C., opinion, 18
    November 2025 — used for the finding that the FTC failed to prove current monopoly power in
    personal social networking and the market-definition ruling including TikTok and YouTube
    (A-claim; primary opinion; corroborated via NPR, Sullivan & Cromwell, and ITIF commentary
    rather than independently machine-extracted from the opinion this session).
    [NPR](https://www.npr.org/2025/11/18/nx-s1-5495626/meta-ftc-instagram-whatsapp-antitrust-ruling) ·
    [Sullivan & Cromwell](https://www.sullcrom.com/insights/memo/2025/December/Meta-Prevails-FTC-Monopolization-Case)
15. Federal Trade Commission, "FTC Appeals Ruling in Meta Monopolization Case" (press release,
    January 2026). [FTC](https://www.ftc.gov/news-events/news/press-releases/2026/01/ftc-appeals-ruling-meta-monopolization-case)
    — used for the notice-of-appeal fact and date (A-claim; primary agency statement; fetched via
    search synthesis this session).
16. ITIF, "Schumpeter's Vindication: The Enduring Link Between Scale and Innovation," 16 October
    2025. [ITIF](https://itif.org/publications/2025/10/16/schumpeters-vindication-the-enduring-link-between-scale-and-innovation/)
    — used for the 95-studies/655-estimates meta-analysis finding a positive average firm-size/
    innovation relationship, the inverted-U concentration pattern, and the R&D-spending-scale
    argument (D-claim; policy-institute analysis broadly sympathetic to large-firm innovation
    capacity, presented as that institute's argued position, not adopted as settled fact; fetched
    this session).
17. International Center for Law & Economics (ICLE), "Network Effects and Interoperability."
    [laweconcenter.org](https://laweconcenter.org/resources/network-effects-and-interoperability/)
    — used for the "mandates have tended to focus on markets that already have low switching
    costs" critique and the competition-for-the-market substitute-mechanism argument (D-claim;
    ICLE is a law-and-economics research center whose funding and output skew toward lighter-touch
    antitrust positions; presented as an attributed critical position, not adopted as settled
    fact; fetched this session).
18. Jenny Blessing & Ross Anderson (2023, rev. 2023), "One Protocol to Rule Them All? On Securing
    Interoperable Messaging," arXiv:2303.14178 (Cambridge University). [arXiv](https://arxiv.org/abs/2303.14178)
    — used for the specific technical security/privacy complications of mandated cross-platform
    messaging (content moderation, authentication, key management, metadata leakage across
    provider boundaries) (C-claim; academic preprint by established security researchers, not
    formally peer-reviewed as fetched; fetched this session).
19. Cybernews, "Signal CEO criticizes WhatsApp — Metadata is deadly," and TechCrunch, "To comply
    with DMA, WhatsApp and Messenger will become interoperable via Signal protocol" — used for
    Signal President Meredith Whittaker's stated conditions for interoperability (no security
    compromise "on the backend"; will not lower its own privacy/security standards) and Meta's
    choice to build its DMA-compliant bridge on the Signal protocol (B/D-claims; journalistic
    sources reporting direct statements from an interested party; fetched via search synthesis
    this session).
    [Cybernews](https://cybernews.com/privacy/signal-ceo-criticizes-whatsapp/) ·
    [TechCrunch](https://techcrunch.com/2024/03/06/to-comply-with-dma-whatsapp-and-messenger-will-become-interoperable-via-signal/)