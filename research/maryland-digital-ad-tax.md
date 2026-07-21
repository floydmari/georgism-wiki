---
authors:
- Paul Romer
- State of Maryland
- U.S. Court of Appeals for the Fourth Circuit
category: research
excerpt: 'Romer''s proposal did not stay theoretical: Maryland enacted the first US
  digital advertising tax in 2021 after Romer testified for it.'
last_reviewed: 2026-07-18
source_url: https://services.marylandcomptroller.gov/taxes?id=kb_article_view&sysparm_article=KB0010082
stub: false
subcategory: wiki-research-lvt
tags:
- research
- digital-advertising
- romer
- maryland
- tax-incidence
- platform-economy
- data-rents
- geoism
- rent-gradient
- first-amendment
tier: Important
title: 'Digital Advertising Taxes After Romer: Maryland''s Real-World Test'
year: 2021
---

## Summary

[Romer's proposal](/wiki/romer-digital-advertising-tax/) — a progressive tax on
targeted-digital-advertising revenue, designed to push platforms from ads toward
subscriptions rather than primarily to raise money — did not stay a thought
experiment. In 2021 Maryland enacted the **Digital Advertising Gross Revenues
Tax**, the first US state tax explicitly aimed at digital advertising, after
Romer personally testified for the bill. This page does not re-derive Romer's
mechanism (see the linked page for the full design and its "if big is bad, tax
big" logic); it covers what happened when a version of the idea became law: the
statute's actual design (which departs from Romer's in several respects), the
revenue it has raised against its own projections, the litigation that has
consumed most of its life so far — culminating in a **unanimous Fourth Circuit
ruling (August 2025) striking down the tax's "pass-through ban" on First
Amendment grounds** — and the still-open question of whether platform
advertising revenue is the kind of thing a rent tax should be reaching at all.

## From Op-Ed to Statute

Romer's May 2019 *New York Times* op-ed proposing a progressive ad-revenue tax
reached Maryland's legislature directly. The state Senate President introduced a
digital-advertising-tax bill in January 2020, and the Senate Budget and Taxation
Committee invited Romer to testify in its favor on 20 February 2020 — his
testimony is preserved in the Maryland General Assembly's own committee-testimony
archive.[1] Romer told the committee he wanted targeted digital advertising to
stop, not merely to be taxed, and that he "would be happy" if a tax built to his
specification raised no revenue at all, because that would mean the targeted-ad
business model had disappeared.[1][2] He separately praised Maryland's specific
effort as an attempt to "claw back for the citizens of Maryland revenue which has
been sucked out of their state."[2]

The 2020 bill passed with veto-proof majorities but was vetoed by Governor Larry
Hogan; the legislature overrode the veto in February 2021, and the tax took
effect **14 March 2021**, applying retroactively to tax year 2021.[3][4]

## The Statute — Where It Follows Romer, and Where It Doesn't

Maryland's Digital Advertising Gross Revenues Tax (Md. Tax-General Article, Title
7.5) is a **graduated tax on gross revenue derived from digital advertising
services in Maryland** ("banner advertising, search engine advertising,
interstitial advertising, and other comparable advertising services"), with
audio-only and non-programmatic advertising, and advertising on broadcast or news
media entities' own platforms, excluded by later amendment.[3][5]

**Rate schedule.** The rate that applies to a company's Maryland ad revenue (the
"assessable base") is set by the company's **global annual gross revenue**, not
by how much of that revenue is Maryland-sourced:[3][4]

| Global annual gross revenue | Rate on Maryland digital-ad revenue |
|---|---|
| $100 million – $1 billion | 2.5% |
| >$1 billion – $5 billion | 5.0% |
| >$5 billion – $15 billion | 7.5% |
| >$15 billion | 10.0% |

A person must file if their Maryland digital-advertising revenue is at least $1
million annually.[4] The Tax Foundation's analysis flags a structural quirk this
table implies: the rate applies to a company's *entire* Maryland assessable base
once it crosses a global-revenue threshold, not just to revenue above that
threshold — a "cliff" rather than a marginal-bracket structure, which can make a
firm just over a threshold worse off than a slightly smaller competitor and
creates an incentive to understate global revenue or restructure below a
cliff.[6]

**Two departures from Romer's own design are worth naming plainly.** First,
Maryland's tax reaches "digital advertising services" generally, not specifically
*targeted* advertising the way Romer's proposal was scoped — Romer's tax was
meant to exempt non-targeted formats (e.g., a plain banner ad not keyed to a
user's data) as part of the subscription-escape design; Maryland's statute left
this distinction largely to the Comptroller's regulations rather than writing
Romer's targeting-based exemption into the statute itself.[7] Second, Maryland's
graduated brackets are keyed to a firm's absolute size, which is directionally
Romer's "tax big" logic, but the statute contains no equivalent of Romer's
explicit **subscription escape hatch** or the incentive to split up rather than
grow — it is a size-graduated *revenue* tax on a broader ad-services base, closer
in mechanics to a [DST](/wiki/digital-services-taxes/) than to Romer's own
narrower, more surgical design.[3][6] The wiki should not describe Maryland's tax
as "Romer's tax enacted" — it is a state legislature's adaptation of Romer's
big-is-bad logic, filtered through ordinary state tax-drafting, and the two
instruments' incidence and legal exposure need not be identical.

## The Litigation — the Dominant Story So Far

No US jurisdiction has operated a tax like this for long enough, or with clean
enough revenue data, to generate a settled incidence record. What Maryland's tax
has generated instead is five years of litigation on two parallel tracks.

**State track: procedure, not merits, decided so far.** Comcast, Verizon and
other industry plaintiffs sued in Maryland state court in April 2021. In October
2022 an Anne Arundel County circuit judge invalidated the tax, agreeing that it
violated the federal **Internet Tax Freedom Act** (which bars states from
singling out electronic commerce for discriminatory taxation) and discriminated
against interstate commerce by keying its rate to companies' *global* revenue.[8]
The **Maryland Supreme Court reversed in 2023** (per curiam order 9 May 2023,
opinion 12 July 2023) — but only on a procedural ground: Comcast and Verizon had
not exhausted the state's administrative tax-appeal remedies before going to
court. The court's opinion **did not reach the constitutional or Internet Tax
Freedom Act arguments at all**.[9][10] The tax survives in force today because of
that procedural ruling, not because any court has yet upheld it on the merits — a
distinction several of the professional tax-law summaries covered here are
careful to preserve, and one the wiki should preserve too. A separate merits case
is still pending in the **Maryland Tax Court**.[11][12]

**Federal track: a First Amendment win against the state, on a narrow but real
provision.** A parallel federal suit — the U.S. Chamber of Commerce, NetChoice,
the Computer & Communications Industry Association and the Internet Association
v. Franchot (the Maryland Comptroller) — challenged the tax itself under the
Internet Tax Freedom Act, the Commerce Clause and Due Process, *and* separately
challenged a distinct statutory provision: Maryland's **"pass-through
prohibition,"** which barred a company subject to the tax from directly passing
its cost to Maryland customers through a separate fee, surcharge, or line
item.[12][13] In March 2022 the district court held the federal **Tax Injunction
Act** barred it from hearing the challenges to the tax itself (federal courts
generally cannot enjoin state tax collection where a state offers its own remedy)
but allowed the narrower pass-through claim to proceed, since blocking a *speech
restriction* is not the same as blocking *tax collection*.[12][13] The district
court dismissed even that claim as moot in December 2022; the Chamber
appealed.[12]

On **15 August 2025** a unanimous Fourth Circuit panel reversed, holding
Maryland's pass-through ban **unconstitutional under the First Amendment**. The
court characterized the provision as one designed to shield state lawmakers from
"criticism and political accountability" for the tax's real-world costs rather
than to serve any legitimate regulatory purpose — a company could raise its
prices to cover the tax, but Maryland's law required, in the reporting
characterization several outlets used, that it "do so in silence": no line item,
no surcharge, no itemized explanation naming the tax.[14][15][16] The case was
remanded to the district court, which entered final judgment on **15 October
2025** permanently enjoining Maryland from enforcing the pass-through ban in any
form.[16][17] The core tax itself was not struck down — it remains in force,
collectible, and separately contested in the pending Maryland Tax Court merits
case.[11][17]

**The pass-through ruling is itself an incidence-adjacent finding worth naming.**
A state legislature does not normally bother banning visible pass-through of a
tax whose incidence it expects to fall entirely on the nominally taxed firms; the
ban's own existence is circumstantial evidence that Maryland's drafters
anticipated — and wanted to suppress public attribution of — cost pass-through to
consumers. That is not a measured incidence estimate, and the wiki does not treat
it as one; it is a fact about the statute's design that the record supports and
that a reader assessing incidence should know.

## Revenue: Well Under Projection, and Not Officially Itemized

Maryland's own fiscal estimate for the bill projected up to **$250 million per
year**, largely earmarked for the "Blueprint for Maryland's Future" education
funding program.[17][18] Press reporting sourced to the Comptroller's office
puts actual collections at roughly **$93 million in FY2022** and **$82.5 million
in FY2023**, with a cumulative total of **roughly $419 million collected since
2022** by the time of an October 2025 report — averaging closer to $100-120
million per year than the projected $250 million.[7][18] **This figure needs an
honest caveat: it is drawn from secondary press reporting attributed to the
Comptroller's office, not from a Comptroller-published table this page could
independently fetch and verify** — one account explicitly notes exact
year-by-year revenue has not been made public in full, partly because of the
litigation.[18] The direction (well under the $250 million projection) is
corroborated by every source consulted; the exact annual figures should be
re-verified against a primary Comptroller report before being treated as precise.

## Is Advertising Revenue Rent? Arguing It Both Ways

This is the question the whole instrument stands or falls on, and the wiki's
[rent gradient](/wiki/geoism/) requires carrying both sides honestly rather than
assuming platforms' ad revenue behaves like land rent.

**The case that it is (at least partly) rent.** [Prat and Valletti's "Attention
Oligopoly"](https://www.aeaweb.org/articles?id=10.1257/mic.20200134) (*American
Economic Journal: Microeconomics*, 2022) models dominant digital platforms as
**attention brokers** — intermediaries with proprietary information about users'
preferences who sell targeted ad space to retailers competing for that
attention.[19] Their result: when attention brokers become more **concentrated**,
ad prices rise, fewer ads reach potential market entrants, and consumer welfare
in the underlying product markets falls — a mechanism in which a platform's scale
advantage, not just the quality of its matching technology, is what lets it
extract higher ad prices.[19] The paper also warns that competition-policy
assessments relying on aggregate platform usage "can be highly biased," implying
regulators may be underestimating how much of platform ad revenue reflects
bottleneck power rather than service quality.[19] This dovetails with the
[Furman Review](/wiki/furman-review-digital-competition/)'s finding that Google
and Facebook dominated an **£11.55 billion (2017) UK digital-advertising
market**, and its call for a dedicated market study into whether the
digital-advertising value chain is actually competitive — the same
"durable-position" evidence the wiki treats as the empirical precondition for
calling a return a rent rather than a transient lead.[20]

**The case that a meaningful share is not rent.** Targeted advertising funds real
services users value at a zero sticker price — search, maps, social
connectivity — and part of the revenue platforms earn reflects genuine matching
quality: better ad targeting is a real technology that raises advertiser return
on spend, not merely an extraction mechanism. The [Furman
Review](/wiki/furman-review-digital-competition/) itself, despite documenting the
concentration above, is explicit that "there is nothing inherently wrong about
being a large company or a monopoly" and that platform dominance often "reflect
efficiencies and benefits for consumers" — the [quasi-rent](/wiki/quasi-rent/)
reading the wiki refuses to assume away.[20] Romer's own framing, discussed on
the [instrument-comparison page](/wiki/taxing-tech-rents/), reinforces this: he
motivates his tax as a *behavioral* and *democratic* correction — he wants
targeted advertising discouraged because of its effect on political discourse and
attention markets, not because he has identified and measured a pure rent
component to be captured. A tax calibrated to make firms *abandon* the ad model
is, by construction, not calibrated to leave a genuine-service return
untouched — it is closer to a [Pigouvian](/wiki/pigouvian-taxation/) correction
than to a Georgist rent tax, a point this page inherits directly from the
proposal page.[2]

**What this means for the "is it rent" question, honestly stated.** Prat &
Valletti supply real evidence that *concentration* in attention markets raises ad
prices and harms downstream competition — that is evidence for a rent-like
component tied specifically to market power, not to the underlying
matching/targeting technology. It does not, and does not claim to, decompose
platform ad revenue into a rent share and a quasi-rent share the way the wiki can
point to for land. No source consulted in this research pass provides that
decomposition for advertising revenue specifically. The honest reading is the
gradient's own: **some** of platform ad revenue very likely reflects bottleneck
power over attention (the Attention Oligopoly mechanism, and the same
durable-position evidence the Furman Review documents), and **some** reflects a
genuine, valuable matching service — and no one has cleanly separated the two.

## Honest Limits

- **No ex-post incidence study of Maryland's tax itself was found.** Unlike the
  UK DST, which has [a real empirical pass-through estimate](/wiki/digital-services-tax-incidence/)
  (Muddasani & Langenmayr on Amazon), this research pass did not locate a
  comparable peer-reviewed or working-paper measurement of who actually bears
  Maryland's ad tax. The pass-through-ban litigation is suggestive of the
  legislature's own expectation, not a measured result, and the wiki does not
  present it as one.
- **Revenue figures rest on press reporting, not a fetched primary Comptroller
  table.** The $93m/$82.5m/~$419m-cumulative figures are consistently reported
  across multiple outlets citing the Comptroller's office, but this page could
  not independently verify them against an official, itemized Comptroller
  revenue report; they should be re-checked before being cited as precise.
- **The core constitutional merits case remains unresolved.** As of this
  session's research (mid-2026), the tax survives only because of the Maryland
  Supreme Court's 2023 procedural ruling and a Tax Injunction Act bar on the
  federal claims; the Internet Tax Freedom Act and Commerce Clause arguments that
  a state court once found persuasive on the merits (October 2022) have never
  been affirmed or rejected by an appellate court. This is a live, moving
  litigation and any "the tax survives" framing should be dated.
- **Maryland's statute is not a clean test of Romer's own design.** Because the
  enacted tax departs from Romer's proposal (broader ad-services base, a
  cliff-rate structure, no explicit subscription escape hatch), its legal and
  revenue troubles are evidence about *a* state ad-revenue tax, not a direct
  verdict on Romer's specific progressive-schedule mechanism.
- **The is-it-rent question is not resolved here and should not be treated as
  resolved.** Prat & Valletti's concentration mechanism and the Furman Review's
  durability findings are real evidence for a rent-like component; neither
  source, nor any other found in this pass, quantifies what share of platform ad
  revenue is rent versus quasi-rent.

## See Also

- [Romer's Progressive Tax on Digital Advertising](/wiki/romer-digital-advertising-tax/) — the proposal's own design, incidence logic, and the Acemoglu–Johnson variant, not repeated here
- [Taxing Tech Rents — Instrument Comparison](/wiki/taxing-tech-rents/) — where Romer's ad tax is graded C as a rent instrument against ACE/DBCFT, DSTs, data dividends, and antitrust/DMA dissolution
- [Digital Services Taxes and Their Incidence](/wiki/digital-services-tax-incidence/) — the sibling revenue-tax instrument and its one rigorous ex-post pass-through estimate (Amazon/UK)
- [Digital Services Taxes as Actually Implemented](/wiki/digital-services-taxes/) — the UK/France/India/Canada revenue and litigation record this page's Maryland case study parallels
- [Platform and Data Rents](/wiki/data-rents/) — the underlying rent-or-quasi-rent diagnosis this page's central question extends
- [Furman Review — Unlocking Digital Competition](/wiki/furman-review-digital-competition/) — the official UK diagnosis of digital-advertising-market concentration
- [Pigouvian Taxation](/wiki/pigouvian-taxation/) — the correction-not-capture framing Romer's tax shares with Acemoglu & Johnson
- [Geoism](/wiki/geoism/) — the rent gradient this page's honest-limits section applies

## Sources

1. Paul Romer, testimony to the Maryland Senate Budget and Taxation Committee, 20
   February 2020, Maryland General Assembly committee-testimony archive.
   [mgaleg.maryland.gov PDF](https://mgaleg.maryland.gov/cmte_testimony/2020/bat/1541_02202020_93326-878.pdf)
   — used for the fact and date of Romer's testimony (A-claim; primary legislative
   record; the PDF's text could not be machine-extracted this session, so its
   content is corroborated via [2] rather than quoted directly from the PDF
   itself).
2. Paul Romer, quoted in Kate Klonick / ProMarket, "If You Think Moderation is
   Censorship, You've Got a Competition Problem," 15 January 2021.
   [ProMarket](https://www.promarket.org/2021/01/15/paul-romer-facebook-competition-pigouvian-tax-digital-ads/)
   — used for the "would be happy if raised no revenue" framing, the progressive
   marginal-rate design description, and the "claw back for the citizens of
   Maryland" quote (D-claim; interview/journalistic source quoting Romer
   directly; fetched this session).
3. Maryland Tax-General Article, Title 7.5 (Digital Advertising Gross Revenues
   Tax), as summarized in Sales Tax Institute, "Maryland Enacts New Tax on
   Digital Advertising."
   [Sales Tax Institute](https://www.salestaxinstitute.com/resources/maryland-enacts-new-tax-on-digital-advertising)
   — used for the rate schedule, effective date (14 March 2021), $1 million
   filing threshold, and the assessable-base definition (F/A-claims; professional
   tax-advisory secondary source; the statute itself was not machine-readable via
   the sources tried this session — see note below).
4. Maryland Comptroller, "Tax Guidance — Digital Advertising Gross Revenues Tax,"
   official Taxpayer Services knowledge base.
   [services.marylandcomptroller.gov](https://services.marylandcomptroller.gov/taxes?id=kb_article_view&sysparm_article=KB0010082)
   — cited as the page's source_url (official primary guidance); corroborates the
   rate schedule and filing threshold reported via [3] (F-claim; official state
   guidance).
5. Description of "digital advertising services" scope (banner, search-engine,
   interstitial advertising; broadcast/news-media and audio-only/non-programmatic
   exclusions), as reported in web search synthesis of Maryland Comptroller
   Technical Bulletin No. 59 and related practitioner commentary — used for the
   statutory definition of the taxed activity (F-claim; the Technical Bulletin
   PDF itself could not be machine-extracted this session; content corroborated
   across multiple independent secondary summaries, not directly quoted).
6. Tax Foundation, "Worse Than Advertised: The Legal and Economic Pitfalls of
   Maryland's Digital Advertising Tax."
   [Tax Foundation](https://taxfoundation.org/research/all/state/maryland-digital-advertising-tax/)
   — used for the cliff-rate-structure critique, the Internet Tax Freedom Act and
   dormant Commerce Clause legal analysis, and the tax-pyramiding critique
   (D-claim; policy-institute analysis explicitly opposed to the tax, presented
   as that institute's own argued position, not adopted as settled fact; fetched
   this session).
7. Search-synthesized reporting on the gap between Romer's "targeted advertising"
   scope and Maryland's broader enacted definition, and on the ~$419 million
   cumulative revenue figure attributed to the Comptroller's office — used for
   the design-departure point and the cumulative revenue figure (B/D-claims;
   multiple secondary press/practitioner sources, not independently confirmed
   against a primary Comptroller dataset; flagged in Honest Limits).
8. Grant Thornton, "Maryland tax on digital-ad services still in effect," and RSM
   US, "Maryland digital advertising tax: Where are we now?" (2023) — used for
   the October 2022 Anne Arundel County circuit court ruling invalidating the tax
   on Internet Tax Freedom Act and dormant-Commerce-Clause grounds.
   [RSM](https://rsmus.com/insights/tax-alerts/2023/Maryland-digital-advertising-tax-where-are-we-now.html)
   (B/A-claims; professional tax-advisory secondary sources; fetched via search
   synthesis this session).
9. Comptroller of Maryland v. Comcast of California/Maryland, LLC, Maryland
   Supreme Court (per curiam order 9 May 2023, opinion 12 July 2023).
   [Maryland Courts PDF](https://www.mdcourts.gov/data/opinions/coa/2023/32a22.pdf)
   — cited for the case name and outcome; the PDF's text could not be
   machine-extracted this session, so the exhaustion-of-remedies holding and the
   court's non-reaching of the constitutional questions are corroborated via [10]
   rather than quoted directly from the opinion (A-claim; primary appellate
   opinion, content via secondary corroboration).
10. Aprio, "Maryland Supreme Court Ruling Keeps Digital Advertising Tax Alive . . .
    For Now," and Conduit Street (Maryland Association of Counties), coverage of
    the 2023 ruling — used for the procedural (exhaustion-of-remedies) basis of
    the reversal and confirmation that the constitutional and Internet Tax
    Freedom Act claims were not addressed (A-claim; corroborated across
    independent secondary legal-commentary sources; fetched via search synthesis
    this session).
11. Conduit Street (Maryland Association of Counties), "Federal Court Issues
    Final Ruling Blocking 'Pass-Through' Ban in Maryland's Digital Ad Tax," 21
    October 2025.
    [Conduit Street](https://conduitstreet.mdcounties.org/2025/10/21/federal-court-issues-final-ruling-blocking-pass-through-ban-in-marylands-digital-ad-tax/)
    — used for the 15 October 2025 final-judgment date, the permanent injunction
    against the pass-through ban, confirmation that the core tax remains
    enforceable, the pending Maryland Tax Court merits case, and the $250 million
    original revenue projection (A/B-claims; specialized state-government-adjacent
    policy tracker; fetched and read this session).
12. U.S. Chamber of Commerce Litigation Center, "Chamber of Commerce v.
    Franchot," case summary.
    [U.S. Chamber](https://www.uschamber.com/cases/jurisdiction-and-procedure/chamber-of-commerce-v-franchot)
    — used for the February/April 2021 filing and amended-complaint timeline, the
    March 2022 Tax Injunction Act ruling (barring the claims against the tax
    itself but allowing the pass-through First Amendment claim to proceed), and
    the December 2022 mootness dismissal that was later appealed (A-claim;
    litigant's own case-tracking page, corroborated by [13]; fetched this
    session).
13. Web search synthesis of Chamber of Commerce v. Franchot, 595 F. Supp. 3d 423
    (D. Md. 2022) case commentary (vLex, Davis+Gilbert) — used to corroborate the
    Tax Injunction Act ruling and the specific claims raised (ITFA, Commerce
    Clause, Due Process, First Amendment pass-through) (A-claim; corroborating
    secondary legal sources; fetched via search synthesis this session).
14. Chamber of Commerce of the United States of America v. Comptroller of
    Maryland, No. 24-1727 (4th Cir., 15 August 2025).
    [Fourth Circuit PDF](https://www.ca4.uscourts.gov/opinions/241727.P.pdf)
    — cited for the case name, number, and date; the PDF's text could not be
    machine-extracted this session, so the holding and reasoning are corroborated
    via [15][16] rather than quoted directly from the opinion (A-claim; primary
    appellate opinion, content via secondary corroboration).
15. BDO, "Fourth Circuit Finds Maryland's Digital Ad Tax Pass-Through Restriction
    Unconstitutional."
    [BDO](https://www.bdo.com/insights/tax/fourth-circuit-finds-marylands-digital-ad-tax-pass-through-restriction-unconstitutional)
    — used for the unanimous-panel holding, the "criticism and political
    accountability" characterization, and the confirmation that other methods of
    explaining a price increase remain permitted (A-claim; major accounting/tax
    advisory firm's legal-update summary; fetched this session).
16. Maryland Matters, "Appeals court rules provision of digital ad tax violates
    First Amendment protections," 15 August 2025; and NBC Washington / other
    outlets reporting Circuit Judge Julius Richardson's characterization that
    firms "must do so in silence." — used for the plain-language characterization
    of the pass-through ban and the "in silence" framing (A-claim; journalistic
    sources reporting the same ruling as [14][15]; corroborated via search
    synthesis, direct article fetch returned HTTP 403 this session).
17. Robert H. Smith School of Business, University of Maryland, "Digital Tax
    Debacle."
    [rhsmith.umd.edu](https://www.rhsmith.umd.edu/news/digital-tax-debacle)
    — used for the $250 million annual projection versus roughly $90 million/year
    actual collections, the "must do so in silence" quote attributed to Circuit
    Judge Julius Richardson, and the university's overall assessment that the tax
    fell well short of its revenue goal (B/D-claims; university business-school
    news summary, not a primary fiscal document; fetched and read this session).
18. Search-synthesized press reporting (multiple outlets citing the Maryland
    Comptroller's office) on FY2022 (~$93 million) and FY2023 (~$82.5 million)
    digital-ad-tax revenue and the ~$419 million cumulative total reported by
    October 2025 — used for the specific annual figures, flagged in Honest Limits
    as unverified against a primary Comptroller table (D-claim; press reporting,
    not independently confirmed this session).
19. Andrea Prat & Tommaso Valletti, "Attention Oligopoly," *American Economic
    Journal: Microeconomics* 14(3), August 2022 (working paper version 2019-2020).
    [AEA](https://www.aeaweb.org/articles?id=10.1257/mic.20200134) ·
    [working paper](https://www.cresse.info/wp-content/uploads/2020/08/2020_AttentionOligopoly.pdf)
    — used for the attention-broker model, the finding that concentration among
    attention brokers raises ad prices and reduces consumer welfare, and the
    caution against merger assessments based on aggregate usage alone (B/C-claims;
    peer-reviewed journal article; abstract and secondary summary fetched this
    session, full text not independently retrieved).
20. Digital Competition Expert Panel (Furman, chair), *Unlocking Digital
    Competition*, HM Treasury, March 2019 — used for the £11.55 billion (2017) UK
    digital-advertising market figure, the digital-advertising market-study
    recommendation, and the "nothing inherently wrong about being a large company
    or a monopoly" / efficiencies quote. Full citation and this page's own
    reading of the report are carried at
    [furman-review-digital-competition](/wiki/furman-review-digital-competition/);
    not re-fetched independently this session (A/D-claims via that page's own
    sourcing).