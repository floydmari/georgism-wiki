# Mason Gaffney corpus — triage ledger

*Created 2026-07-16 (session 2z2oww). Basis: Floyd's directive with hosting permission —
masongaffney.org's webmaster granted permission to host and work on everything on the site
(Gaffney d. 2020, NYT obit linked from the site); Floyd additionally curates a priority list
in Notion (pending access — see BACKLOG). Local mirror of worked texts: `sources/gaffney/`.*

**Already covered on the wiki** (research/): gaffney-atcor, gaffney-neoclassical-stratagem,
gaffney-synergistic-city, gaffney-hidden-taxable-capacity, gaffney-land-distinctive-factor,
gaffney-after-the-crash, gaffney-causes-of-downturns, gaffney-land-booms-destroy-capital,
gaffney-europes-fatal-affair-with-vat, gaffney-full-employment-tax-reform,
gaffney-excess-burden-shiftable-taxes, gaffney-philosophy-of-public-finance,
gaffney-alaska-oil-leasing, gaffney-land-market-distortions, gaffney-california-severance-tax,
gaffney-financial-maturity-timber, gaffney-forest-taxation, gaffney-soil-depletion-land-rent,
gaffney-capital-gains-free-enterprise, gaffney-montana-land-policy,
gaffney-rising-inequality-farm-property-tax, gaffney-urban-land-rent,
gaffney-containment-policies-urban-sprawl, gaffney-land-as-element-of-housing-costs,
gaffney-water-rent-taxation; narratives/the-corruption-of-economics; people/mason-gaffney.

**2026-07-18 (K-series — history-of-economic-thought cluster):** Surveyed all
unchecked K rows. Two were already resolved before this wave started: K142
("Two Centuries of Economic Thought on Taxation of Land Rents") was already
mined into [research/gaffney-two-centuries-land-taxation](/wiki/gaffney-two-centuries-land-taxation/)
as of 2026-07-17 (contrary to this wave's initial briefing, which assumed it
might still be unmined), and K1 ("Neo-classical Stratagem") had its checkbox
reconciliation-fixed in a prior wave. Of the five genuinely unchecked K rows,
three were mined and two declined. **Mined:** K9 (Stabile's "Henry George's
Influence on John Bates Clark," *AJES* 54(3) 1995, with Gaffney's appended
comment) and K2008 ("Keeping Land in Capital Theory," *AJES* 67(1) 2008) —
both folded as deltas into
[concepts/marginal-productivity](/wiki/marginal-productivity/),
[people/john-bates-clark](/wiki/john-bates-clark/), and
[people/philip-wicksteed](/wiki/philip-wicksteed/) (K9's Wicksteed-priority
claim); K2008 additionally reconciled a prior-wave loose end — it was already
quoted once on [research/gaffney-financial-maturity-timber](/wiki/gaffney-financial-maturity-timber/)
but had never been registered in sources/registry.csv and its issue number was
miscited (67(2) instead of 67(1)), both now fixed. K17 (Gaffney's "Alfred
Russel Wallace's Campaign to Nationalize Land," *AJES* 56(4) 1997) was mined
as a delta into the existing [people/alfred-russel-wallace](/wiki/alfred-russel-wallace/)
page, with a light cross-link into [people/john-stuart-mill](/wiki/john-stuart-mill/).
**Declined, no fold:** K18 (McGlynn/Leo XIII) and K2012 (Going My Way? —
Georgism and Catholicism) are both substantive but are religious/political
history, not history-of-economic-thought, and their factual content on the
1886–1892 McGlynn/Corrigan/Rome conflict is already better-sourced (primary
correspondence, not a secondary conference paper) on the existing
[people/edward-mcglynn](/wiki/edward-mcglynn/) page. **Motive-claims handling:**
K9's appended Gaffney comment is sharply more motive-attributing than the
Stabile article it responds to ("Clark never intended to follow George except
as a U-Boat stalks a troopship"; "Clark's main objective was to fuse and
confuse land with capital") and Gaffney's Wicksteed-priority argument is his
own polemical framing — both carried under the same attributed D-claim
convention established on C9, cross-linked to
[Missemer & Pottier](/wiki/missemer-pottier-land-labor-capital/)'s
peer-reviewed counter-read wherever the claim touches Clark's land/capital
merger specifically. **OCR notes:** K9, K17, and K18 are 300dpi scanned images
with a garbled legacy OCR text layer baked into the PDF (using standard
WinAnsi-encoded base-14 fonts rather than embedded fonts — misreading
"Gaffney" as "GFrFx," "Marx" as "Maix," etc.); K2008's embedded text layer was
completely empty. All three re-OCR'd this session at 250–300dpi with
Tesseract 5.3.4, resolving the K9/K17 garbling and producing K2008's only
usable text; canonical `.txt` files saved to `sources/gaffney/text/`.
Registry: three new rows (K9 and K2008 tier `core`, Scan Depth Heavy; K17
tier `important`, Scan Depth Heavy). `lint_wiki.py`: 0 errors.

**2026-07-18 (H-series complete — water cluster triage finished):** Follow-on
wave completing the H-series (water) rows opened by the prior batch-6 wave,
which mined H3+H21 into [research/gaffney-water-rent-taxation](/wiki/gaffney-water-rent-taxation/).
Skimmed/read all remaining unchecked H rows (H4, H5, H8, H18, H19, H20 ×3
files, H22) against that page under a strict-delta rule. **Six works folded**
(H4, H8, H18, H19, H20, H22 — see individual checkbox entries below for full
verdicts), **one declined** (H5 — garbled OCR conference-talk restatement of
H3/H8), **one non-primary** (H20's standalone bibliography PDF, checked but
not separately cited). No dedicated second water page was created; every
fold went into the existing page as new sections/subsections, consistent
with the strict-delta instruction that a second page would need
substantively distinct ground, which none of these six works cleared on
their own (they extend and complement H3/H21 rather than opening a new
topic). **Notable findings reversing the prior wave's predictions:** H4,
flagged "mirror 404, not pursued" in the batch-6 narrative, turned out to be
a genuine scholarly reply (JFE 1962) to a published critique of H3 by a law
school dean (Frank Trelease) — recovered via the same `%26`-encoded-URL
fetch used for E15's ampersand-filename mirror problem, and folded into a
correction of the page's "no third-party peer review" characterization. H8,
dismissed as an "also-ran" 14pp survey, proved to be a systematic
nine-criterion doctrine comparison plus a primary-source economic-theory
account of irrigation-district financing, complementing (not duplicating)
[research/california-irrigation-districts](/wiki/california-irrigation-districts/).
H19, dismissed as "too short" at 4pp, contained a genuinely distinct
market-design mechanism (advance-bidding, watermaster-cleared spot
pricing) absent from every other H-series item. H22 (1997), not even
individually named as a candidate in the prior wave's survey beyond "large,
unread, lower priority," turned out to be Gaffney's most mature single
treatment of water marketing and became this wave's largest addition (new
"Part III" on the water page): the "yield-cutting substitute" concept,
WTP/WTA entitlement economics illustrated with Native American treaty
rights, named 1990s water-permit speculators, and an avoided-cost/Henry
George theoretical link. H20 confirmed the prior wave's "likely overlapping
with H21" prediction for roughly a third of its 18 fallacies, but contributed
two genuinely distinct facts (the Owens Valley "Chinatown Syndrome"/"Great
Water Treadmill" account, later restated near-verbatim in H22 itself, and
an Irvine Water District land-based-franchise voting-rights fact). Registry:
six new rows (H4/H8 Medium, H18/H19 Light, H20 Medium, H22 Heavy), no row
for declined H5 (decline precedent). Text mirrors saved to
`sources/gaffney/text/` for all six folded works; H5 not mirrored (brief
skim only, per the C2/E1 "save only if cited" convention).
`lint_wiki.py`: 0 errors. This closes out the H-series; no unchecked H rows
remain.

**2026-07-18 (tier-2 batch 6 — E-series skim-verdicts + WATER cluster, a wholly new
resource-rent domain):** Two-part wave. **(1) E-series skim verdicts:** E13,
"Changes in Land Policy: How Fundamental Are They?" (1976 WAEA conference
paper), and E15, a book review of Heilbrun's *Real Estate Taxes and Urban
Housing* (1966), were read in full and both **declined dedicated pages**.
E13 is genuinely substantive (a rich 1970s diagnosis of exclusionary
zoning) but its policy core overlaps E3/E10/E11/E12/E14, all already mined
this session; its one clean delta — the "grants to governments are grants
to landowners" fiscal argument and a utility zonal-rate cross-subsidy
incentive for exclusionary zoning — was wired as a light addition to the
stub page [concepts/nimbyism](/wiki/nimbyism/) instead of a full mining
pass, proportionate to a skim-verdict item (registry row added, Light
scan, per the E1 reversal precedent). E15 is thin as expected: a two-page
book review restating already-covered ATCOR-precursor and tax-incidence
material with no primary Gaffney research; zero-addition verdict, no
registry row (C2 precedent). E15's ampersand-filename mirror problem
recurred (236-byte cached 404 stub) and was resolved the usual way
(`%26` direct fetch from masongaffney.org). **(2) Corpus-wide picks —
WATER:** surveyed the full remaining unchecked-row pool (F environmental,
G property-tax-miscellany, H water, I capital/employment, K history-of-
thought, L/N/O/Z singles, plus workpapers and essays) for genuine wiki
gaps rather than restatements of the strong-hands/timing material now
covered 4+ times. **Water rights emerged as the strongest gap**:
[concepts/resource-rents](/wiki/resource-rents/) names water in its own
opening definition of resource-rent domains but had developed zero content
on it, and no other wiki page covers water rights, western water law, or
water markets at all. Skimmed the H-series water cluster by file size and
opening pages (H18 Water Giveaway, H19 How a Water Market Might Work — 4pp,
too short; H20 Whose Water — Ours, abridged/unabridged pair, likely
overlapping with H21; H22 What Price Water Marketing, unread — large but
lower priority once H21 covered the core argument; H4 Water Law &
Economic Transfers Reply — mirror 404 stub, not pursued; H5 Comparison of
Market Pricing, H8 Economic Aspects of Water Resource Policy — 14pp
survey, also-ran) and picked the two most substantive: **H3, "Diseconomies
Inherent in Western Water Laws: A California Case Study"** (1961) and
**H21, "The Taxable Surplus in Water Resources"** (1992), combined onto
[research/gaffney-water-rent-taxation](/wiki/gaffney-water-rent-taxation/)
as a career-spanning pair (empirical diagnosis, then mature policy
proposal), the same two-work-combination pattern already used for
B1/B4+B13/E11+E12. **H3 also yields a priority finding**: delivered
January 23, 1961, it predates "The Unwieldy Time-Dimension of Space"
(October 1961) by nine months, making it the earliest-dated
professional/academic conference paper so far identified in the corpus
(after the 1957 timber monograph and 1958 *Yearbook of Agriculture*
essay) — though it does not contain the "strong hands" credit-
concentration mechanism, so C4's specific priority claim on
concepts/land-monopoly stands unaffected (see the new page's dedicated
priority-note section, cross-referenced from people/mason-gaffney).
**OCR note:** H3's masongaffney.org PDF carries a poor-quality legacy-scan
text layer; re-OCR'd this session at 250dpi with Tesseract 5.3.4, which
recovered substantially cleaner text (17,195 vs. ~13,437 words) — flagged
`[VERIFY]` on the page regardless, since the underlying scan quality is
still a limiting factor for exact figures. H21 is native, cleanly
`pdftotext`-extractable text. **Bonus reconciliation:** while surveying
the candidate pool, found K1 (`K1Neo-classical_Stratagem.CV.pdf`) already
cited by [research/gaffney-neoclassical-stratagem](/wiki/gaffney-neoclassical-stratagem/)
and twice in the registry — its triage checkbox had simply never been
flipped; fixed, no content change. Wired (delta additions, not
restatement): concepts/resource-rents (new "Water as a Resource Rent"
section), benefits/resource-rent-capture-works (an eighth institutional-
failure mode — water rights assigned by legal doctrine rather than price
— distinct from the seven leasing/tax-code/ownership modes already there),
and people/mason-gaffney (replaced a vague unlinked "Research on water
rights and natural resource taxation" placeholder bullet with a proper
linked entry plus the priority note). Registry: two new rows (both tier
`core`, Scan Depth Heavy) for H3/H21, one new row (tier `supplementary`,
Scan Depth Light) for E13. `lint_wiki.py`: 0 errors.

**2026-07-18 (tier-2 batch 4 — priority correction + farm-subsidy incidence + time-indivisibility):**
Three publications read, drafted, and wired: C4 (1961), D3 (1966), and E10
(1969), all previously-unread tier-2 items. **C4, "The Unwieldy
Time-Dimension of Space"** (*AJES* 20(5), October 1961), is the earliest
dated work in the wiki's Gaffney corpus — see
[research/gaffney-time-dimension-of-space](/wiki/gaffney-time-dimension-of-space/).
It derives, algebraically, the theoretical root of the "strong hands"
credit-concentration mechanism already covered from the 1972–73, 1992, and
1994 essays: because land ownership requires financing a perpetual claim
("time-indivisibility") and interest rates differ by wealth, land gravitates
to low-interest holders regardless of productivity, with price appreciation
widening the gap. Per the delta rule already applied when this recurring
mechanism turned up a third time in B1, **the leverage/concentration
conclusion is corroboration, not new evidence** — the genuine deltas are the
priority correction (1961, not 1972–73, is the earliest known statement,
corrected on concepts/land-monopoly) and the wholly new
leasing/lending-as-imperfect-time-dividers argument. **D3, "The Benefits of
Farm Programs: Incidence, Shifting, and Dissipation"** (*AJES*, 1966; a 1965
AFEA conference paper) — see
[research/gaffney-benefits-farm-programs](/wiki/gaffney-benefits-farm-programs/) —
is a Ricardian-incidence analysis of 1960s US farm subsidies: price
supports, land-idling payments, and (its richest content) a catalogue of
rural public works — reclamation, subsidized power/water rates, rural roads,
RFD, subsidized farm credit — that capitalize into farmland value, a
pre-1970s, agricultural-domain instance of the capitalization mechanism
distinct from the wiki's existing transit-focused literature. Also
original: the **"intensity quotient"** concept (the ratio of non-land costs
to gross revenue), explaining why owners of highly-leveraged marginal land
become the most politically mobilized rent-seekers in cartelized commodity
programs — wired as a new mechanism into problems/rent-seeking-drags-growth.
**E10, "Land Planning and the Property Tax"** (*AIP Journal*, May 1969) —
see [research/gaffney-land-planning-property-tax](/wiki/gaffney-land-planning-property-tax/) —
turned out to be **the primary 1969 source of material the wiki already
carried via a 1998 restatement**: the Milwaukee "isovalic" renewal study
(20%/50% estimates) and the Marine Plaza "chain reaction" illustration on
research/gaffney-philosophy-of-public-finance, which reuses phrasing from
this article nearly verbatim ("galloping merger movement"). Corrected the
priority there, parallel to the earlier ATCOR (1998-not-2005) and C9
(1994-not-2004) corrections. Per the delta rule, that overlapping material
was **not** re-derived on the new page; E10's genuine deltas are a
credit-leverage account of how the building tax's financing structure delays
renewal, and a seven-point argument — addressed to professional planners, an
audience distinct from the 1998 chapter's — that a land-value tax base
*increases* planning power rather than substituting the market for planners.
Wired (delta additions only): concepts/land-monopoly and
problems/high-land-rents-suppress-productivity (C4); problems/public-investment-capitalizes-into-land
and problems/rent-seeking-drags-growth (D3); research/gaffney-philosophy-of-public-finance
(priority correction), benefits/split-rate-increases-construction (citation
correction plus the financing mechanism), and benefits/lvt-reduces-sprawl
(the open-space-planning argument) (E10). Registry: three new rows (all
tier `important`, Scan Depth Heavy). Mirror note: none of the three
masongaffney.org filenames contain a literal ampersand, so all three
extracted cleanly via `pdftotext -layout` from the local mirror with no
`%26` workaround needed.

**2026-07-18 (urban-land-rent pair, T2 wave):** `E11-LandRentTaxation&PublicPolicy-
SourcesUrbanLandRent.CV.pdf` ("The Sources, Nature and Functions of Urban Land
Rent," *AJES* 31(3), July 1972) and `E12-...-TaxationUrbanLandRent.CV.pdf`
("Taxation and the Functions of Urban Land Rent," *AJES* 32(1), January 1973)
read as a pair and merged into one page,
[research/gaffney-urban-land-rent](/wiki/gaffney-urban-land-rent/) — they are
Parts I and II of a single argument based on a 1968 Regional Science
Association talk, not two independent works. **Mirror/encoding note (repeat of
the D1 problem):** both filenames contain a literal ampersand; the local mirror
at `scratchpad/cache/gaffney-mirror/publications/` held cached 404 HTML pages
for both (236 bytes each, `<title>404 Not Found</title>`) rather than the PDFs.
Worked around by fetching directly from masongaffney.org with the ampersand
percent-encoded (`%26`) in the request URL — confirms this is a general fix for
every `&`-bearing masongaffney.org filename, not a one-off for D1. Both PDFs
carry native, `pdftotext`-extractable text layers (no OCR needed), though the
text layer itself shows scanning-era OCR noise (e.g. "GPNEY" for "Gaffney,"
"dassical" for "classical") — quotes were checked against surrounding context
before use. E11 (18pp, ~8,000 words) derives a tripartite typology of urban
rent sources (natural features, public spending, "synergism") and argues rent
only *rations* land, never *elicits* its own supply. E12 (18pp, ~8,150 words)
argues five mechanisms by which taxing rent (not income/buildings) lets it
perform that function, the most developed being a credit-discrimination
"strong hands vs. weak hands" argument with a worked numerical leverage
example — the earlier (1972-73), fuller original of the mechanism Gaffney
restated in condensed form in the already-wired 1994 [Land as a Distinctive
Factor](/wiki/gaffney-land-distinctive-factor/) essay (there, B-8/B-9). Also
notable: an informal, pre-Stiglitz (1977) statement of the Henry George
Theorem's capitalization mechanism ("conservation of economic energy" /
explicit tax-capitalization arithmetic crediting Jensen 1931), and a
distinctive political-economy argument — untaxed rent biases public spending
toward **logrolling** — absent from the 1994 essay. Graded **Core** (like the
1994 essay): a first-principles, ~16,000-word pair developing the wiki's
central urban-rent-sources and taxation-mechanism arguments at length, not a
supplementary aside. Wired with surgical, non-duplicative additions (checked
against the just-expanded Henry George Theorem page and the already-deep
`benefits/lvt-reduces-sprawl` and `problems/public-investment-capitalizes-into-
land` evidence pages before adding — all Gaffney material added as attributed
historical/theoretical context, never as a substitute for the modern
econometric anchors already wired there): concepts/economic-rent (new
subsection, the tripartite typology), concepts/land-monopoly (the earlier
"strong hands" original with its leverage arithmetic, appended to the existing
Gaffney-1994 paragraph), benefits/lvt-reduces-sprawl and
problems/public-investment-capitalizes-into-land (both: prose context
paragraphs, cited but explicitly *not* added to `supported_by` — old advocacy
theory does not belong in a ranked empirical-evidence table), and light
See-Also cross-links from concepts/henry-george-theorem,
concepts/agglomeration-economies, research/gaffney-synergistic-city, and
people/mason-gaffney. `lint_wiki.py`: 0 errors.

**2026-07-18 (Alaska Part II backlog resolution):** *Oil and Gas Leasing Policy for
Alaska* (1977), **Part II: Appendices A–L**, read and mined — the companion volume
deliberately left unread when Part I was mined 2026-07-17. Image-scan PDF (155
pages, no usable embedded text); OCR'd this session (`pdftoppm -r 200` + Tesseract
5.3.4) and added as a new "Part II" section to
[research/gaffney-alaska-oil-leasing](/wiki/gaffney-alaska-oil-leasing/#part-ii-the-appendices-a-l),
resolving the page's `[VERIFY]` flag. Twelve appendices: Gaffney's own worked
numerical examples (A, B, C, H, I, J, unsigned K) plus three independently authored
contributed papers — Michael Crommelin (Melbourne) on non-competitive leasing
abroad, Richard Norgaard (UC Berkeley) regressing actual Cook Inlet lease-sale data
to find bonus bidding captured only 9–16% of realized rent there, and three papers
by consulting economist Robert F. Rooney on multipart royalty design,
exploration-expenditure bidding, and profit-share bidding. No contributor dissent
from Gaffney's ad valorem charge recommendation found — the appendices independently
corroborate his low ranking of bonus bidding and profit sharing without commenting
on the AVC directly. Norgaard's finding wired (delta addition, not restatement)
into benefits/resource-rent-capture-works and concepts/resource-rents as an
independent econometric plank alongside Gaffney's own design argument.

**2026-07-18 (T2 wave — tier-2 batch 3):** *"Capital" Gains and the Future of Free
Enterprise* (1991) and *Counter-colonial Land Policy for Montana* (1977) read,
drafted, and wired; *Corporations, Democracy, and the U.S. Supreme Court* (2010)
read and declined a research page (see the checklist entry below for the full
triage reasoning). **Capital Gains** — see
[research/gaffney-capital-gains-free-enterprise](/wiki/gaffney-capital-gains-free-enterprise/)
— is Gaffney's most developed single statement of the "capital gains are mostly
land gains" thesis: a documented Georgist-origins history of the U.S. income tax
(the 1894 Maguire amendment, the 16th Amendment, Warren Worth Bailey's role in the
1916 Revenue Act) plus a systematic tax-loophole catalogue (deferral, covert land
depreciation, step-up of basis at death, the Bishop Estate's 340,000 Hawaii acres
never triggering a taxable sale) and a symmetry critique of inflation-indexing
proposals. Wired as an ancestor-statement (not independent quantitative evidence)
into problems/capital-share-rise-is-land, as new tax-code mechanics into
concepts/unearned-increment, and as a historical natural-experiment (1960s
accelerated depreciation read as an implicit land-for-capital tax shift, via the
Commons→Groves→Heller lineage) into
benefits/lvt-can-replace-capital-taxes-without-efficiency-loss. **Montana** — see
[research/gaffney-montana-land-policy](/wiki/gaffney-montana-land-policy/) — frames
1970s Montana as an internal resource colony (absentee-held rail/finance
corporations, a copper property-tax loophole capped at the 19th-century patentee
price, concentrated federal coal leasing) and prescribes land value taxation,
illustrated with New Westminster BC and California Wright Act irrigation-district
case studies. Wired into concepts/resource-rents (new subsection) and
benefits/resource-rent-capture-works (a fifth institutional-failure mode:
concentrated absentee leasing plus a structurally weak extraction-only yield
tax). No `places/montana` page created — the accept bar (≥2 existing pages that
would naturally link to it) was not met. **Corporations, Democracy, and the U.S.
Supreme Court** was judged tangential to the rent-capture mission (a political
essay on corporate personhood and *Citizens United*, not primarily about rent
capture) and declined; its one on-topic claim cites a source
(Feldstein, *JPE* 1977) the wiki already carries independently.

**2026-07-18 (T2 wave — natural-resource-taxation cluster):** Four forestry/soil
publications read, drafted, and wired: *Concepts of Financial Maturity of Timber
and Other Assets* (1957, A.E. Information Series No. 62, NC State College — see
[research/gaffney-financial-maturity-timber](/wiki/gaffney-financial-maturity-timber/)),
*Alternative Ways of Taxing Forests* (1980) + *Greater Social Benefits from our
National Forests* (1977) combined on
[research/gaffney-forest-taxation](/wiki/gaffney-forest-taxation/), and *Soil
Depletion and Land Rent* (1965, *Natural Resources Journal* 4(3): 537-557 —
see [research/gaffney-soil-depletion-land-rent](/wiki/gaffney-soil-depletion-land-rent/)).
Notable findings: (1) the 1957 timber monograph is Gaffney's most externally,
academically cited single work (81 Semantic Scholar citations; credited by
Gaffney's own 2008 retrospective, and independently by D.H. Newman's 2002
*Journal of Forest Economics* historiography, with helping trigger the 1957-76
revival of Faustmann's formula that culminated in Samuelson's 1976 endorsement)
— graded **Important**, not Core, since its direct contribution to the Georgist
argument is one neutrality result plus a historical Faustmann-George linkage
Gaffney only made explicit in 2008, not a flagship rent-capture statement; (2)
the monograph is NOT Gaffney's PhD dissertation and has no Duke affiliation —
his actual dissertation is "Land Speculation as an Obstacle to Ideal Allocation
of Land" (UC Berkeley, 1956) — corrected on the new page; (3) *Soil Depletion
and Land Rent* (a peer-reviewed law-journal article) gives a formal economic
answer to the "depletable resources are used up" caveat in
objections/land-is-just-capital.md, wired there as a new Response point; (4) the
1977 National Forests address supplies a third institutional-failure mode
(chronic non-capture in an ongoing public asset, via agency accounting
doctrines) for benefits/resource-rent-capture-works.md, distinct from Norway/
Botswana (design succeeding) and California (capture built, then lost).
Extended (not restated) concepts/resource-rents.md with a new "Rent Capture in
Forestry" subsection. B5's masongaffney.org filename has a literal ampersand
that broke the automated R2 mirror (archive.progress.org 404s under every
encoding tried); the live masongaffney.org URL and the UNM Digital Repository
(the journal's own open-access host) are the working citations — flagged for a
mirror re-run, not fixed this session.

**2026-07-17 (T2 wave):** *Oil and Gas Leasing Policy for Alaska* (1977, Part I only —
Part II Appendices A-L not covered) read, drafted, and wired into
benefits/resource-rent-capture-works ("Design Before the Windfall — Alaska, 1977"),
concepts/resource-rents, and places/alaska — see
[research/gaffney-alaska-oil-leasing](/wiki/gaffney-alaska-oil-leasing/). Two short
undated working papers (WP041, WP042, internally dated circa 1993) combined onto one
page, [research/gaffney-land-market-distortions](/wiki/gaffney-land-market-distortions/):
WP041 restates the mechanism already on gaffney-land-booms-destroy-capital.md
(linked, not repeated); WP042's five-fold capital-misallocation taxonomy is wired
into problems/high-land-rents-suppress-productivity as a weakest-tier theoretical
precursor. Judged narratives/land-speculation-causes-cycles.md to already carry
enough Gaffney (Causes of Downturns Stage V, the land-booms-destroy-capital page) —
no new wiring added there per the delta rule.

**2026-07-16 (Floyd's Notion priority, top gap):** *The Philosophy of Public Finance* (1998,
Ch. 7 in Fred Harrison ed., *The Losses of Nations*, Othila Press) read, drafted, and wired
— see [research/gaffney-philosophy-of-public-finance](/wiki/gaffney-philosophy-of-public-finance/).
Notable finding: this 1998 chapter contains a section headed "4. The concept of ATCOR" naming
and stating the acronym seven years before the 2005 WP096 working paper the wiki previously
credited with coining it — corrected on research/gaffney-atcor.md and concepts/atcor.md.

**2026-07-16 tax-shift cluster (T2 wave):** Europe's Fatal Affair with VAT, Full Employment
through Total Tax Reform, and A Better Way of Gauging the Excess Burden of Shiftable Taxes
are read, drafted, and wired (see checkboxes below and the three `research/gaffney-*` pages
above) — wired into benefits/lvt-can-replace-capital-taxes-without-efficiency-loss,
benefits/taxing-land-raises-productivity, and concepts/deadweight-loss respectively, with
cross-links (not restatement) to research/gaffney-atcor and concepts/atcor per the delta rule.

**2026-07-18 (LAND-THEORY cluster, T2 wave):** Of three LAND-THEORY candidates
(C2 "Land and Rent in Welfare Economics," C9 "Land as a Distinctive Factor of
Production," D1 "Rising Inequality and Falling Property Tax Rates"), C9 and D1
proved the most substantive on reading and were mined; C2 was read but declined a
dedicated page this wave (see its checklist entry below). **C9** is Gaffney's
major theoretical essay from Nicolaus Tideman's *Land and Taxation* (1994,
Shepheard-Walwyn) — ten primary land/capital distinctions plus eighteen policy
consequences — and substantially replaces a one-paragraph stub that had been
sourced only to a 2004 web-expansion; the primary 1994 text (native, no OCR) is now
the citation. **D1** is a new page: a 1992 Westview Press book-chapter using US
Census of Agriculture data (1900-1987, 50-state cross-section) showing farm-property
concentration (Gini ratio) rose from 0.63 to 0.76 (0.92 adjusted for vanished farms)
as average farm property tax rates fell 40% after 1930, with a Wisconsin-vs-Florida
cross-state comparison tying higher property tax rates to more intensive land
improvement and more equal farm distribution. Both wired (delta additions, not
restatement) into concepts/land-monopoly (a new "credit access as a modern
concentration mechanism" subsection) and benefits/split-rate-increases-construction
(D1 as a farmland data point distinct from the existing urban-permit literature);
C9 additionally strengthens objections/land-is-just-capital's existing citation
with a specific credit-concentration quote. Registry: the pre-existing
gaffney-land-distinctive-factor row's Scan Depth upgraded Light -> Heavy (closing
the open Core-tier/Light-scan gap EDITORIAL's Scan Depth policy flags); one new row
added for D1.

**2026-07-18 (EXTRACTIVE-RESOURCES cluster, T2 wave):** Four publications read —
B1 (Editor's Introduction + Conclusion to *Extractive Resources and Taxation*,
1967), B4 ("Objectives of Government Policy in Leasing Mineral Lands," a
Canadian Crown-land leasing essay), and B13 ("Oil and Gas: The Unfinished Tax
Reform," 1982) — drafted onto two new pages per the delta rule: B1 alone on
[research/gaffney-extractive-resources-taxation](/wiki/gaffney-extractive-resources-taxation/)
and B4+B13 combined (both proved substantive, not fragments — companion
essays on the same theme of institutional rent leakage from two channels,
leasing design and tax law) on
[research/gaffney-mineral-leasing-tax-reform](/wiki/gaffney-mineral-leasing-tax-reform/).
Key finding on B1: the 1977 Alaska report's appended timing theory (Figure
C.4, the "ripeness" criterion — already wired via
[gaffney-alaska-oil-leasing](/wiki/gaffney-alaska-oil-leasing/)) turns out to
be *this same 1967 essay*, reused by Gaffney as a theoretical appendix a
decade later — so that material was **not** re-derived on the new page,
strictly applying the delta rule; the page instead covers B1's genuinely
uncovered content: a systematic property-tax-vs-income-tax instrument
comparison for exhaustible resources (Gaffney's earliest, 1967, academic
resource-tax treatment) and a nine-reason taxonomy of why institutions
overmotivate exploration. B4's eight named Crown-land leasing errors include
a formal rent/profit accounting identity (`Rent = Profit − Interest`) and
engage Canadian constitutional law (BNA Act s.125) directly — unique among
the wiki's Gaffney corpus for its Canadian-provincial framing. B13's
strongest original contribution is a set of three "invisible" US federal
tax loopholes Gaffney says the reform literature had entirely missed, led
by **leasehold abandonment**: because roughly four-fifths of exploratory
leases prove dry, and their cost is expensed as an ordinary loss rather than
capitalized as part of the one producing lease's true acquisition cost, "some
80% of the de facto cost of land acquisition is expensed at an early date" —
a genuine delta against the wiki's existing general land-gains-thesis page,
[gaffney-capital-gains-free-enterprise](/wiki/gaffney-capital-gains-free-enterprise/),
which does not cover oil/gas-specific mechanics (depletion, abandonment,
leasehold churning). B13's mirror filename has the same literal-ampersand
problem as D1/E11/E12/B5 (236-byte cached 404 stub); fetched directly from
masongaffney.org with `%26` percent-encoding, confirming the fix generalizes.
Wired (delta additions, not restatement) into concepts/resource-rents (two
new subsections: the instrument-comparison/overmotivation taxonomy, and the
leasing-design/tax-code rent-leakage pair) and benefits/resource-rent-capture-works
(a sixth and seventh institutional-failure mode, distinct from the five
already there — leasing-design errors that persist within any instrument
choice, and federal tax-code leakage that operates even where government
does not own the resource). The "strong hands" credit-concentration
mechanism recurs a third time in B1 (applied to extractive resources) but
was explicitly *not* wired as new evidence — flagged as corroboration only,
per the delta rule already applied on concepts/land-monopoly to the same
mechanism from C9/D1/E12.

**2026-07-18 (tier-2 batch 5 — URBAN-HOUSING cluster: reconciliation + sprawl
priority correction + housing-cost tax catalogue):** Started with a
reconciliation sub-task: E14 (`E14Synergistic_City.CV.pdf`) was listed
unchecked despite research/gaffney-synergistic-city already existing and
citing the same PDF. Fetched and fully read it (the page had previously been
built from an abstract-only read) — confirmed it is the identical work
("The Synergistic City," *Real Estate Issues*, Winter 1978), upgraded
registry Scan Depth from Light to Heavy, and enriched the page with two
findings the earlier partial read had missed (the pollution/open-space
myth-busting argument, and the postage-stamp cross-subsidy pricing
mechanism). Then fetched and skimmed all four URBAN-HOUSING candidates —
E1 (1958), E22 (1968), E37 (undated, ~late 1990s/2000s), E3 (1964) — and
mined the two most substantive: **E3, "Containment Policies for Urban
Sprawl"** (1964 University of Kansas book chapter) — see
[research/gaffney-containment-policies-urban-sprawl](/wiki/gaffney-containment-policies-urban-sprawl/) —
is a **priority correction**: the earliest Gaffney statement of the
land-value-tax anti-sprawl argument in the wiki's corpus, predating the
already-cited 1969 and 1972-73 essays by five to nine years, with a
concretely worked-out postage-stamp-utility-pricing mechanism and the "cheap
to buy, dear to hold" formulation later restated more abstractly in E14.
**E22, "Land as an Element of Housing Costs"** (1968 IDA/HUD study) — see
[research/gaffney-land-as-element-of-housing-costs](/wiki/gaffney-land-as-element-of-housing-costs/) —
contributes an early, pre-Oates capitalization argument specifically
explaining why land taxation helps credit-constrained low-income buyers, plus
an exhaustive Federal-income-tax-code holdout catalogue distinct from the
zoning/supply story already covered. Both wired as historical/theoretical
context (not empirical evidence), per the E10/E11/E12 convention already
established for Gaffney's own non-econometric arguments. E1 (1958,
*Yearbook of Agriculture* — now the earliest dated work in the wiki's
Gaffney corpus, predating C4 by three years) and E37 (the "Path to Justice"
chapter) were read but declined pages this wave — see their triage rows
below for the reasoning; E1 in particular is flagged as a strong
priority-correction candidate for a future wave.

## Inventory (masongaffney.org, fetched 2026-07-16: 190 files)

### /publications/ (87)
- [x] `1977_Counter-colonial_Land_Policy_for_Montana.pdf` — https://masongaffney.org/publications/1977_Counter-colonial_Land_Policy_for_Montana.pdf — [research/gaffney-montana-land-policy](/wiki/gaffney-montana-land-policy/), 2026-07-18. *Western Wildlands: A Natural Resource Journal*, Winter 1977, pp. 16-25. Wired into concepts/resource-rents (new subsection) and benefits/resource-rent-capture-works (fifth institutional-failure mode: concentrated absentee federal coal leasing plus a structurally weak yield tax). No `places/montana` page created — accept bar (≥2 existing pages that would naturally link to it) not met; only 5 wiki pages mention Montana at all, none as a subject.
- [x] `2006_New_Life_in_Old_Cities.pdf` — https://masongaffney.org/publications/2006_New_Life_in_Old_Cities.pdf — [research/gaffney-new-life-in-old-cities](/wiki/gaffney-new-life-in-old-cities/), 2026-07-16
- [x] `A1-1957_Financial_Maturity_of_Timber_final_unrepaginated.pdf` — https://masongaffney.org/publications/A1-1957_Financial_Maturity_of_Timber_final_unrepaginated.pdf — [research/gaffney-financial-maturity-timber](/wiki/gaffney-financial-maturity-timber/), 2026-07-18. Title/venue verified from the document: A.E. Information Series No. 62, NC State College, Sept. 1957 — NOT a Duke dissertation (Gaffney's actual PhD dissertation is a separate 1956 UC Berkeley work); graded Important on strong external academic standing (81 Semantic Scholar citations, Samuelson 1976 endorsement, credited with the 1957-76 Faustmann revival).
- [x] `A3-AlternativeWaysofTaxingForests.CV.pdf` — https://masongaffney.org/publications/A3-AlternativeWaysofTaxingForests.CV.pdf — combined with A5 into [research/gaffney-forest-taxation](/wiki/gaffney-forest-taxation/), 2026-07-18. Dated "Number 43, March 1980" in the document; publication venue/series not identified (`[VERIFY]` on page).
- [x] `A5-1977_Greater_Social_Benefits_from_our_National_Forests.pdf` — https://masongaffney.org/publications/A5-1977_Greater_Social_Benefits_from_our_National_Forests.pdf — combined with A3 into [research/gaffney-forest-taxation](/wiki/gaffney-forest-taxation/), 2026-07-18. Western Timber Association address, March 4, 1977.
- [x] `B03_OIL_AND_GAS_ALASKA_1977_PART_II_APPENDICES_A-L.pdf` — https://masongaffney.org/publications/B03_OIL_AND_GAS_ALASKA_1977_PART_II_APPENDICES_A-L.pdf — [research/gaffney-alaska-oil-leasing.md](/wiki/gaffney-alaska-oil-leasing/#part-ii-the-appendices-a-l), 2026-07-18. Image-scan PDF (155 pages), no usable text layer; OCR'd this session (`pdftoppm -r 200` + Tesseract 5.3.4) to `sources/gaffney/text/B03_OIL_AND_GAS_ALASKA_1977_PART_II_APPENDICES_A-L.txt`. Twelve appendices A-L: Gaffney's own worked AVC/DCF numerical examples and Alaska leaseholder-concentration data (A, B, C, H, I, J, K), plus three independently authored contributed papers (Crommelin on non-competitive leasing abroad, D; Norgaard's Cook Inlet bonus-bid regression, E; three Rooney papers on royalty design, exploration-expenditure bidding, and profit-share bidding, F/G/L). No contributor dissent from the AVC recommendation found. Resolves the `[VERIFY: Part II not yet read]` flag carried on the page since 2026-07-17.
- [x] `B03_OIL_AND_GAS_LEASING_POLICY_FOR_ALASKA_1977_Part_I.pdf` — https://masongaffney.org/publications/B03_OIL_AND_GAS_LEASING_POLICY_FOR_ALASKA_1977_Part_I.pdf — [research/gaffney-alaska-oil-leasing.md](/wiki/gaffney-alaska-oil-leasing/), 2026-07-17. Part II (Appendices A-L, line above) covered 2026-07-18.
- [x] `B13-Oil&amp;GasUnfinishedTaxReform.CV.pdf` — https://masongaffney.org/publications/B13-Oil&amp;GasUnfinishedTaxReform.CV.pdf — combined with B4 into [research/gaffney-mineral-leasing-tax-reform](/wiki/gaffney-mineral-leasing-tax-reform/), 2026-07-18. 1982 US federal oil-and-gas tax-loophole catalogue. Mirror filename has a literal ampersand (same problem as D1/E11/E12/B5); local mirror held only a 236-byte cached 404 stub — fetched directly from masongaffney.org with `%26` percent-encoding.
- [x] `B1Extractive_Resources_Conclusion.CV.pdf` — https://masongaffney.org/publications/B1Extractive_Resources_Conclusion.CV.pdf — combined with B1 Intro into [research/gaffney-extractive-resources-taxation](/wiki/gaffney-extractive-resources-taxation/), 2026-07-18. Editor's Conclusion to the 1967 TRED volume (~90pp); native text, no OCR needed.
- [x] `B1Extractive_Resources_Intro.CV.pdf` — https://masongaffney.org/publications/B1Extractive_Resources_Intro.CV.pdf — [research/gaffney-extractive-resources-taxation](/wiki/gaffney-extractive-resources-taxation/), 2026-07-18. Editor's Introduction to *Extractive Resources and Taxation* (1967, U. Wisconsin Press, TRED symposium); native text, no OCR needed.
- [x] `B4-ObjectivesofGovernmentPolicyinLeasingMineralLands.CV.pdf` — https://masongaffney.org/publications/B4-ObjectivesofGovernmentPolicyinLeasingMineralLands.CV.pdf — combined with B13 into [research/gaffney-mineral-leasing-tax-reform](/wiki/gaffney-mineral-leasing-tax-reform/), 2026-07-18. Canadian Crown-land mineral-leasing policy essay (undated, mid-1970s internal evidence); native text, no OCR needed.
- [x] `B5Soil_Depletion_&amp;_Land_Rent.CV.pdf` — https://masongaffney.org/publications/B5Soil_Depletion_&amp;_Land_Rent.CV.pdf — [research/gaffney-soil-depletion-land-rent](/wiki/gaffney-soil-depletion-land-rent/), 2026-07-18. Actually *Natural Resources Journal* 4(3): 537-557 (Jan. 1965), not undated as filename implies. Wired into objections/land-is-just-capital (Response point 5 + Limits caveat cross-reference). Note: the R2 mirror at this ampersand-containing key 404s (see `[VERIFY]` on the page) — masongaffney.org direct link and the UNM Digital Repository (open-access journal host) are the working free/legal sources.
- [ ] `C2-LandandRentinWelfareEconomics.CV.pdf` — https://masongaffney.org/publications/C2-LandandRentinWelfareEconomics.CV.pdf — read 2026-07-18 (native text, 27pp, no OCR needed) but declined a page this wave in favor of C9 and D1 (see LAND-THEORY cluster ledger entry below); confirmed via C9's own bibliography as Gaffney, "Land and Rent in Welfare Economics," in Clawson, Harriss & Ackerman (eds.), *Land Economics Research* (Johns Hopkins UP, 1962), pp. 141-67 — a philosophical essay on reintegrating land economics and welfare economics, largely conceptual/programmatic rather than data-driven; candidate for a future wave, possibly folded into concepts/economic-rent or a Gaffney historiography page rather than a standalone research page given overlap with gaffney-land-distinctive-factor and gaffney-neoclassical-stratagem.
- [x] `C4-UnwieldyTime-DimensionofSpace.CV.pdf` — https://masongaffney.org/publications/C4-UnwieldyTime-DimensionofSpace.CV.pdf — [research/gaffney-time-dimension-of-space](/wiki/gaffney-time-dimension-of-space/), 2026-07-18. *American Journal of Economics and Sociology* 20(5): 465–481 (October 1961) — the earliest dated work in the wiki's Gaffney corpus. Native text, no OCR needed.
- [x] `C6-Counter-ColonialLandPolicyforMontana.CV.pdf` — https://masongaffney.org/publications/C6-Counter-ColonialLandPolicyforMontana.CV.pdf — same essay as `1977_Counter-colonial_Land_Policy_for_Montana.pdf` above (identical title; different scan, 300KB vs 59KB — not separately reviewed), covered on [research/gaffney-montana-land-policy](/wiki/gaffney-montana-land-policy/), 2026-07-18.
- [x] `C9Land_Distinctive_Factor.CV.pdf` — https://masongaffney.org/publications/C9Land_Distinctive_Factor.CV.pdf — [research/gaffney-land-distinctive-factor](/wiki/gaffney-land-distinctive-factor/), 2026-07-18. This is the actual 1994 *Land and Taxation* (Tideman, ed.) book chapter (64pp, native text, no OCR); the page previously carried only Gaffney's later 2004 web-expansion (cooperative-individualism.org) as its source and was a one-paragraph stub. Substantially rewritten: ten primary distinctions (A-1 to A-10), major economic consequences (B-1 to B-15, notably the B-8/B-9 credit-access concentration mechanism and B-11 market-power argument), and the land-driven-booms-and-busts section (C-1 to C-3). Registry Scan Depth updated Light -> Heavy (this closes the open `[DEEPEN-SCAN tier:T2]`-class gap the Core/Light combination flagged per EDITORIAL's Scan Depth policy).
- [x] `D1Rising_Inequality_&amp;_Falling_Prop_Tax_Rates.CV.pdf` — https://masongaffney.org/publications/D1Rising_Inequality_%26_Falling_Prop_Tax_Rates.CV.pdf — [research/gaffney-rising-inequality-farm-property-tax](/wiki/gaffney-rising-inequality-farm-property-tax/), 2026-07-18. Confirmed via C9's bibliography as Chapter 10 in Gene Wunderlich (ed.), *Ownership, Tenure, and Taxation of Agricultural Land* (Westview Press, 1992). The R2-mirrored copy at this literal-ampersand filename is a cached 404 page (0.2KB), not the PDF — the working fetch requires percent-encoding the ampersand (`%26`); archive.progress.org's mirror also 404s on this file. Fetched directly from masongaffney.org this session (native text, 19pp, no OCR).
- [x] `D3-BenefitsofFarmPrograms.CV.CV.pdf` — https://masongaffney.org/publications/D3-BenefitsofFarmPrograms.CV.CV.pdf — [research/gaffney-benefits-farm-programs](/wiki/gaffney-benefits-farm-programs/), 2026-07-18. *American Journal of Economics and Sociology*, Parts I and II, 1966 (delivered at the American Farm Economics Association annual meeting, Stillwater, Oklahoma, August 1965); exact volume/issue `[VERIFY]`. Native text, no OCR needed.
- [x] `E10-Land_Planning_and_the_Property_Tax_AIP.pdf` — https://masongaffney.org/publications/E10-Land_Planning_and_the_Property_Tax_AIP.pdf — [research/gaffney-land-planning-property-tax](/wiki/gaffney-land-planning-property-tax/), 2026-07-18. *AIP Journal*, May 1969, pp. 178–183. **Priority finding:** this is the primary source of the Milwaukee "isovalic" study and Marine Plaza illustration the wiki previously credited only to its 1998 restatement (research/gaffney-philosophy-of-public-finance) — corrected there. Native text, no OCR needed.
- [x] `E11-LandRentTaxation&amp;PublicPolicy-SourcesUrbanLandRent.CV.pdf` — https://masongaffney.org/publications/E11-LandRentTaxation&amp;PublicPolicy-SourcesUrbanLandRent.CV.pdf — [research/gaffney-urban-land-rent](/wiki/gaffney-urban-land-rent/), 2026-07-18 (Part I; merged with E12). Confirmed via masongaffney.org as *American Journal of Economics and Sociology* 31(3): 241-258 (July 1972). Same literal-ampersand mirror-404 problem as D1; fetched directly from masongaffney.org with `%26` percent-encoding.
- [x] `E12-LandRentTaxation&amp;PublicPolicy-TaxationUrbanLandRent.CV.pdf` — https://masongaffney.org/publications/E12-LandRentTaxation&amp;PublicPolicy-TaxationUrbanLandRent.CV.pdf — [research/gaffney-urban-land-rent](/wiki/gaffney-urban-land-rent/), 2026-07-18 (Part II; merged with E11). Confirmed via masongaffney.org as *AJES* 32(1): 17-34 (January 1973). Same mirror/encoding workaround as E11/D1.
- [x] `E13Changes_in_Land_Policy.CV.pdf` — https://masongaffney.org/publications/E13Changes_in_Land_Policy.CV.pdf — skim-verdict 2026-07-18: read in full (27pp, native text, no OCR needed). "Changes in Land Policy: How Fundamental Are They?" (WAEA paper, Fort Collins, July 20, 1976) is a substantive, wide-ranging essay on 1970s exclusionary zoning (British Columbia's Agricultural Land Reserve, Vermont/Oregon anti-growth statutes, preferential farm assessment) with real analytical content — an environmental/fiscal-causes taxonomy, a "federal grants to governments are grants to landowners" argument, zonal-utility-rate cross-subsidy design, and BC Land Reserve Gini-ratio farmland-concentration data. **Declined a dedicated page this wave**: its policy core (LVT anti-sprawl, cross-subsidy zonal pricing, preferential-assessment critique) substantially overlaps E3/E10/E11/E12/E14, all mined this session. Genuinely new angle — a systematic economic diagnosis of *exclusionary* zoning specifically (as distinct from growth-boundary containment) — filled a real gap on the stub page [concepts/nimbyism](/wiki/nimbyism/) instead: wired as a new paragraph (the grants-to-landowners fiscal argument and the utility cross-subsidy incentive), a lightweight fix proportionate to the skim-verdict process rather than a full mining pass. Registry row added (Light scan, supplementary tier, 1 in-wiki citation: concepts/nimbyism), per the E1 precedent — a declined dedicated-page verdict does not exempt a source from the registry once it is directly cited from at least one page.
- [x] `E14Synergistic_City.CV.pdf` — https://masongaffney.org/publications/E14Synergistic_City.CV.pdf — reconciled 2026-07-18: confirmed this is the exact PDF already cited as the sole source of [research/gaffney-synergistic-city](/wiki/gaffney-synergistic-city/) (title page, venue, and date all match: Lincoln Institute Colloquium on Land Policy, Oct. 28, 1977; *Real Estate Issues*, Winter 1978, pp. 36-61). The page had previously been built from an abstract-only read (registry Scan Depth: Light); fetched and fully read the native-text PDF this session, upgraded Scan Depth to Heavy, and enriched the page's Overview with two findings not previously on it (the pollution/open-space myth-busting argument and the postage-stamp cross-subsidy pricing mechanism, the latter cross-linked to its earlier, more concrete 1964 statement in E3 below).
- [x] `E15-ReviewHeilbrunRealEstateTaxes&amp;UrbanHousing.CV.pdf` — https://masongaffney.org/publications/E15-ReviewHeilbrunRealEstateTaxes&amp;UrbanHousing.CV.pdf — skim-verdict 2026-07-18: the local mirror held only a 236-byte cached 404 stub (same ampersand-mirror problem as D1/E11/E12/B5/B13/E37); fetched directly from masongaffney.org with `%26` percent-encoding, confirming the fix generalizes yet again. The PDF is exactly what the filename promises: Gaffney's ~2-page book review of James Heilbrun, *Real Estate Taxes and Urban Housing* (Columbia UP, 1966), published in *The Journal of Business* (Univ. of Chicago Press; exact volume/issue `[VERIFY]` — the OCR'd masthead reads "277" as a page number but the journal name is legible), signed "University of Wisconsin — Milwaukee," dating it to Gaffney's brief Milwaukee period, mid-to-late 1960s. **Declined a dedicated page — thin as expected.** Content is almost entirely a critique of another author's dissertation-based book (four numbered "errors and omissions": no capital theory, understated site-value-tax revenue potential, a construction-cost/land-price-offset error, and misapplied housing-demand-elasticity studies treating a small open local jurisdiction like a closed economy), not primary Gaffney research. Its one recurring phrase of note — "a kind of law of conservation of economic energy" — is the same pre-ATCOR language already covered and correctly prioritized via the 1998 Philosophy of Public Finance chapter on [research/gaffney-atcor](/wiki/gaffney-atcor/) and [concepts/atcor](/wiki/atcor/); this review does not predate that citation (undated more precisely than "1960s" against ATCOR's already-corrected 1998 priority) and adds no new argument beyond restating existing tax-incidence points (local property taxes fall on land, not tenants, because local housing demand is highly elastic even though national closed-economy demand studies show inelasticity). No registry row added (zero-addition verdict; not cited from any wiki page), per the C2 precedent.
- [x] `E1Urban_Expansion_Stop.CV.pdf` — https://masongaffney.org/publications/E1Urban_Expansion_Stop.CV.pdf — read 2026-07-18 but declined a page this wave. *Urban Expansion — Will It Ever Stop?*, Yearbook Separate No. 2931, reprinted from the 1958 USDA *Yearbook of Agriculture*, pp. 503-522 — this is now the earliest dated work in the wiki's Gaffney corpus (predates C4, 1961, by three years), written while Gaffney was associate professor of agricultural economics at the University of Missouri. Rich, wide-ranging popular-press essay: an access/agglomeration argument that prefigures the 1964 and 1978 pieces below, plus a substantial diagnosis of land-speculation dynamics (capital-gains tax favoring speculators, property-tax assessment lag, land-boom financing leverage and collapse, population-forecast-driven overestimates of land demand) — but no explicit land-value-tax policy prescription in the excerpts read (the piece calls generally for "lowering the prices asked for urban land" without naming the mechanism). Declined a dedicated page this wave because its strongest material overlaps existing coverage (agglomeration/access economics duplicates the fuller E14 and E3 treatments below; land-boom dynamics overlaps [research/gaffney-land-booms-destroy-capital](/wiki/gaffney-land-booms-destroy-capital/), though that page's mechanism is a distinct, later 1993/2005 working paper) rather than being a clean own-topic fit for this wave's two picks. Flagged as a strong priority-correction candidate for a future wave (earliest-known-publication claim) or as an addition to [people/mason-gaffney](/wiki/mason-gaffney/)'s bibliography note. OCR not needed (native text via plain `pdftotext`, though the original two-column 1958 print layout causes some column interleaving in extraction — checked against context before any quoting). Text mirror: `sources/gaffney/text/E1Urban_Expansion_Stop.CV.txt`.

**Priority-correction pass, 2026-07-18 (cont.):** re-read in full against the two flagged targets. (1) [people/mason-gaffney](/wiki/mason-gaffney/) — added a one-line note identifying E1 as the earliest *land-policy* item in the corpus (three years before the 1961 AJES paper), explicitly distinguishing it from the single earliest-dated work overall (the 1957 forestry/Faustmann monograph, a distinct technical question). (2) [concepts/land-monopoly](/wiki/land-monopoly/)'s "earliest known (1961) statement of the credit/'strong hands' concentration mechanism" — **left untouched**: E1 discusses land-boom financing, credit-quality deterioration, and "financial power" letting large holders outwait smaller ones, but never states the specific self-reinforcing loop (ownership qualifies for credit, credit buys more land) the 1961 paper and land-monopoly.md's Schikele quote state; verdict is "land booms/agglomeration only," not the mechanism, so the 1961 priority attribution stands per the wave's own instruction. (3) [research/gaffney-land-booms-destroy-capital](/wiki/gaffney-land-booms-destroy-capital/) — added a one-line "Historical precursor" note: E1's 1819–1929 land-crash list and "national prosperity on the film of a land bubble" line anticipate the *general* land-boom-threatens-capital concern 24–47 years before the 1982/1993/2005 notes, but explicitly does not contain their specific CCA/capital-consumption-allowance accounting mechanism — noted as anticipation, not priority-correction. Registry row added (Light scan, 2 in-wiki citations: mason-gaffney + gaffney-land-booms-destroy-capital), since this pass cites E1 directly from two pages — reversing the earlier no-registry-row default now that it's wired in. No dedicated E1 page created (still declined, per this morning's verdict).
- [x] `E22-LandasanElementofHousingCosts.CV.pdf` — https://masongaffney.org/publications/E22-LandasanElementofHousingCosts.CV.pdf — [research/gaffney-land-as-element-of-housing-costs](/wiki/gaffney-land-as-element-of-housing-costs/), 2026-07-18. IDA Study S-324 / HUD H-931 (October 1968), Gaffney's own paper only (pp. 1-37 of a two-paper volume; Richard F. Muth's companion paper on housing demand not reviewed). Chosen as one of this wave's two picks: an early, pre-Oates capitalization argument specifically explaining why land taxation helps credit-constrained low-income buyers, plus an exhaustive catalogue of Federal income-tax provisions rewarding land holdout (covert depreciation write-off via understated assessor splits, exemption of imputed and unrealized income, Section 1031 barter, capital gains forgiven at death) — a mechanism for high housing costs distinct from the zoning/supply-constraint story already on benefits/lvt-improves-housing-affordability. Wired there as historical context (not empirical evidence), per the E11/E12 convention. Native text, no OCR needed.
- [x] `E37Ground_Rent_Urban_Decay_&amp;_Revival.CV.pdf` — https://masongaffney.org/publications/E37Ground_Rent_Urban_Decay_&amp;_Revival.CV.pdf — read 2026-07-18 but declined a page this wave. "The Role of Ground Rent in Urban Decay and Revival: How to Revitalize a Failing City," a chapter (pp. 58-83) in *The Path to Justice* (a Georgist anthology; internal evidence — a citation to "Schwab (1998)" and a note about the Japanese land-value crash — dates it to the late 1990s/2000s, exact year `[VERIFY]`). A warm, anecdotal, commencement-style essay (addressed to graduating students) restating the standard Georgist case for reviving declining cities via a land-value tax base, already thoroughly covered on the wiki via [research/gaffney-new-life-in-old-cities](/wiki/gaffney-new-life-in-old-cities/) (2006, empirical) and [research/gaffney-urban-land-rent](/wiki/gaffney-urban-land-rent/) (1972-73, theoretical). Genuinely new content is thin: a footnoted response to the environmentalist "LVT causes overdevelopment" objection ("the tax encourages more intensive development of the sites with greatest value, leaving sites of lesser value... undisturbed" — with a fallback endorsement of urban growth boundaries "in this imperfect world") is the one citable nugget, but it restates rather than extends the reasoning already carried on objections/lvt-causes-overdevelopment's supporting pages. Zero-addition/fold verdict: declined. Confirmed the ampersand-mirror-404 problem does NOT apply here — masongaffney.org serves the PDF directly with `%26` percent-encoding, same as D1/E11/E12/B5/B13. Native text, no OCR needed. Text mirror: `sources/gaffney/text/E37Ground_Rent_Urban_Decay_and_Revival.CV.txt`. No registry row added (not wired to a wiki page), per the C2 precedent.
- [x] `E3Containment_policies.CV.pdf` — https://masongaffney.org/publications/E3Containment_policies.CV.pdf — [research/gaffney-containment-policies-urban-sprawl](/wiki/gaffney-containment-policies-urban-sprawl/), 2026-07-18. Confirmed via web search as Chapter X in Richard L. Stauber (ed.), *Approaches to the Study of Urbanization* (Governmental Research Center, University of Kansas, 1964), pp. 115-133 (also reprinted as a Robert Schalkenbach Foundation pamphlet). Chosen as this wave's other pick: **priority correction** — the earliest Gaffney statement of the land-value-tax anti-sprawl argument in the wiki's corpus, predating the already-cited 1969 (E10) and 1972-73 (E11/E12) essays by five to nine years, with a concretely worked-out (not just asserted) postage-stamp-utility-pricing cross-subsidy mechanism and the "cheap to buy, dear to hold" formulation of site-value taxation. Wired into benefits/lvt-reduces-sprawl as historical-priority context (not empirical evidence), per the E10/E11/E12 convention, and cross-linked from research/gaffney-synergistic-city (E14 above), which restates the same cross-subsidy argument more abstractly fourteen years later. Native text, no OCR needed.
- [ ] `E4-TaxReformtoReleaseLand.CV.pdf` — https://masongaffney.org/publications/E4-TaxReformtoReleaseLand.CV.pdf
- [ ] `E5-WhenToBuildWhat-LocalServicePricingPolicies.CV.pdf` — https://masongaffney.org/publications/E5-WhenToBuildWhat-LocalServicePricingPolicies.CV.pdf
- [ ] `E7Prop_taxes_&amp;_Urban_Renewal.CV.pdf` — https://masongaffney.org/publications/E7Prop_taxes_&amp;_Urban_Renewal.CV.pdf
- [ ] `E9-TaxToolforMeetingUrbanFiscalCrisis.CV.pdf` — https://masongaffney.org/publications/E9-TaxToolforMeetingUrbanFiscalCrisis.CV.pdf
- [ ] `F2QWelfareEconomics_and_Environmental_Quality.CV.pdf` — https://masongaffney.org/publications/F2QWelfareEconomics_and_Environmental_Quality.CV.pdf
- [ ] `F7Nonpoint_Pollution.CV.pdf` — https://masongaffney.org/publications/F7Nonpoint_Pollution.CV.pdf
- [ ] `F8-NonpointPollution.CV.CV.pdf` — https://masongaffney.org/publications/F8-NonpointPollution.CV.CV.pdf
- [ ] `G13Partiality_of_Indexing_Capital_Gains-Original.pdf` — https://masongaffney.org/publications/G13Partiality_of_Indexing_Capital_Gains-Original.pdf
- [ ] `G17Property_Tax_Progressive_Tax.CV.pdf` — https://masongaffney.org/publications/G17Property_Tax_Progressive_Tax.CV.pdf
- [ ] `G18What_is_Prop_Tax_Reform.CV.pdf` — https://masongaffney.org/publications/G18What_is_Prop_Tax_Reform.CV.pdf
- [ ] `G19Many_Faces_of_Site_Value_Taxation.CV.pdf` — https://masongaffney.org/publications/G19Many_Faces_of_Site_Value_Taxation.CV.pdf
- [ ] `G1Adequacy_of_land.CV.pdf` — https://masongaffney.org/publications/G1Adequacy_of_land.CV.pdf
- [ ] `G20-NatlTaxAssnDiscussantonEnergyTaxes.CV.pdf` — https://masongaffney.org/publications/G20-NatlTaxAssnDiscussantonEnergyTaxes.CV.pdf
- [ ] `G2009-Hidden_Taxable_Capacity_of_Land_2009.pdf` — https://masongaffney.org/publications/G2009-Hidden_Taxable_Capacity_of_Land_2009.pdf
- [ ] `G21-PartialityofIndexingCapitalGains.CV.pdf` — https://masongaffney.org/publications/G21-PartialityofIndexingCapitalGains.CV.pdf
- [ ] `G28-AnAlternativeReform.CV.pdf` — https://masongaffney.org/publications/G28-AnAlternativeReform.CV.pdf
- [ ] `G29-TaxableCapacityofLand.pdf` — https://masongaffney.org/publications/G29-TaxableCapacityofLand.pdf
- [ ] `G2QCoordinating_Tax_Incentives.CV.pdf` — https://masongaffney.org/publications/G2QCoordinating_Tax_Incentives.CV.pdf
- [ ] `G2QTestimony_before_Sen_Douglas.CV.pdf` — https://masongaffney.org/publications/G2QTestimony_before_Sen_Douglas.CV.pdf
- [ ] `G34QEquity_Premises_and_Case_for_Socializing_Rent.CV.pdf` — https://masongaffney.org/publications/G34QEquity_Premises_and_Case_for_Socializing_Rent.CV.pdf
- [ ] `G39LandGains.CV.pdf` — https://masongaffney.org/publications/G39LandGains.CV.pdf
- [ ] `G4-AgendaforStrengtheningthePropertyTax1.CV.pdf` — https://masongaffney.org/publications/G4-AgendaforStrengtheningthePropertyTax1.CV.pdf
- [x] `G44Philosophy_of_Public_Finance.CV.pdf` — https://masongaffney.org/publications/G44Philosophy_of_Public_Finance.CV.pdf — [research/gaffney-philosophy-of-public-finance](/wiki/gaffney-philosophy-of-public-finance/), 2026-07-16 (local mirror filename: `G44_Philosophy_of_Public_Finance.pdf`/`.txt`, same work)
- [ ] `G45The_Income-Stimulating_Incentives_of_the_Property_Tax.pdf` — https://masongaffney.org/publications/G45The_Income-Stimulating_Incentives_of_the_Property_Tax.pdf
- [ ] `G4a-PropTax&amp;IntergovReltns.CV.pdf` — https://masongaffney.org/publications/G4a-PropTax&amp;IntergovReltns.CV.pdf
- [ ] `G60Cannan_hits_the_Mark.CV.pdf` — https://masongaffney.org/publications/G60Cannan_hits_the_Mark.CV.pdf
- [x] `H18_Water_Giveaway.pdf` — https://masongaffney.org/publications/H18_Water_Giveaway.pdf — read in full, 2026-07-18. "The Water Giveaway: A Critique of Federal Water Policy," in Robert Haveman & Robert Hamrin (eds.), *The Political Economy of Federal Policy* (Harper & Row, 1973), excerpted from Gaffney's 1969 JEC Subcommittee testimony. **Light fold** into [research/gaffney-water-rent-taxation](/wiki/gaffney-water-rent-taxation/): mostly restates the racing/logrolling/price-umbrella dynamic already on the page from H3, but adds a distinct fiscal driver (pre-1986 expensing of premature-development losses against ordinary income while land-value gains went untaxed) plus two concrete illustrations (Colorado River Compact critique, the Bureau of Reclamation's 1902 revolving fund never completing one revolution by 1969) — folded as item 6 of the Dynamic Pattern list. Native text, no OCR needed.
- [x] `H19-HowaWaterMarketMightWork.CV.pdf` — https://masongaffney.org/publications/H19-HowaWaterMarketMightWork.CV.pdf — read in full, 2026-07-18. "How a Water Market Might Work," notes to California's Governor's Commission on Water Rights Law Reform, July 27, 1977. **Light fold** into [research/gaffney-water-rent-taxation](/wiki/gaffney-water-rent-taxation/) as a new "Designing the Price Mechanism" subsection: a concrete advance-bidding, watermaster-cleared spot-market mechanism for pricing water period to period — a "how" complement to H21's "that we should price withdrawals" argument, not covered by any other H-series item read this session. Native text, no OCR needed. Only 4pp/974 words but substantively distinct, contra this wave's opening prediction that it was "too short" to be worth mining.
- [x] `H20WhoseWater--Ours.CV.pdf` (abridged/published version) and `H20Whose_Water_Ours_unabridged_reformatted.pdf` (unabridged, used as primary text) — https://masongaffney.org/publications/H20WhoseWater--Ours.CV.pdf / https://masongaffney.org/publications/H20Whose_Water_Ours_unabridged_reformatted.pdf — both read in full, 2026-07-18. "Whose Water? Ours? Clearing Fallacies about Implementing Common Rights," Institute for Environmental Studies public conference, University of Washington, Sept. 29–30, 1989, revised for publication April 1991. **Partial fold** into [research/gaffney-water-rent-taxation](/wiki/gaffney-water-rent-taxation/): 18 numbered fallacies, of which roughly 6 substantially overlap H21's six fallacies (real property, cost pass-through, development cost, consumptive use, tragedy of the commons, undermotivated sellers/rent-seeking) and a further several overlap H22's later, more polished treatment (below) — those were **not** separately mined, consistent with the strict-delta rule. Two genuinely distinct facts were folded: the "Great Water Treadmill"/"Chinatown Syndrome" account (Owens Valley 1913, LA/San Fernando Valley insider land purchases) into a new "Groundwater Treadmill" subsection, and the Irvine Water District land-based-franchise voting-rights fact (50,000 registered voters, only 4 eligible to vote in water district elections) contrasted with Wright Act districts' resident suffrage, cross-linked to [research/california-irrigation-districts](/wiki/california-irrigation-districts/). Native text, no OCR needed.
- [x] `H20Whose_Water_Ours_Bibliography.pdf` — https://masongaffney.org/publications/H20Whose_Water_Ours_Bibliography.pdf — checked, 2026-07-18. A standalone bibliography document for H20, not independent primary-source content; no separate registry row or citation (not a primary source itself).
- [x] `H21-TaxableSurplusinWaterResources.CV.pdf` — https://masongaffney.org/publications/H21-TaxableSurplusinWaterResources.CV.pdf — combined with H3 into [research/gaffney-water-rent-taxation](/wiki/gaffney-water-rent-taxation/), 2026-07-18. *Contemporary Policy Issues* 10 (Oct. 1992): 74-82, Western Economic Association International; revised from a paper delivered at the WEAI 66th Annual Conference, Seattle, July 1, 1991. Native text, no OCR needed. Chosen as one of this wave's two corpus-wide picks: a mature, six-fallacy systematic case for taxing water withdrawals, filling a total gap (water rent capture was previously undeveloped anywhere on the wiki despite being named in concepts/resource-rents' own opening definition).
- [x] `H22-WhatPriceWaterMarketing.CV.pdf` — https://masongaffney.org/publications/H22-WhatPriceWaterMarketing.CV.pdf — read in full, 2026-07-18. "What Price Water Marketing? California's New Frontier," *AJES* 56(4) (Oct. 1997): 475-520. **Heavy fold**, the largest single addition of this H-series-complete wave: a new "Part III" on [research/gaffney-water-rent-taxation](/wiki/gaffney-water-rent-taxation/) — Gaffney's most mature single treatment of water marketing, five years after H21 and substantially superseding H20's fallacy list for the material the two share. Genuinely new content folded: the "yield-cutting substitute" concept (more water per acre can mean lower yield per acre); a WTP/WTA entitlement-economics argument illustrated with Native American treaty-fishing-rights valuation; named 1990s water-permit speculators (Bass Brothers, Cadiz Land, Tenneco, PG&E Properties) updating H21's abstract rent-seeking fallacy; a concrete "win-win-lose" example (the Dec. 1988 Interior Dept. subsidized-water resale policy) with a Henry George "vested right to rob me" quote; the avoided-cost/FERC concept traced to Henry George's *Science of Political Economy*; and a McCarthy-era political history of suppression of federal water-marketing reformers (Bureau of Agricultural Economics staff denounced as "Communist"). Native, cleanly `pdftotext`-extractable text; no OCR needed.
- [x] `H3-DiseconomiesInherentinWesternWaterLaws21.CV.CV.pdf` — https://masongaffney.org/publications/H3-DiseconomiesInherentinWesternWaterLaws21.CV.CV.pdf — combined with H21 into [research/gaffney-water-rent-taxation](/wiki/gaffney-water-rent-taxation/), 2026-07-18. "Diseconomies Inherent in Western Water Laws: A California Case Study," read before the Western Agricultural Economics Research Council, Tucson, Jan. 23, 1961; published in *Economic Analysis of Multiple Use*, Report No. 9, pp. 55-82. **Priority finding:** delivered January 23, 1961 — nine months before "The Unwieldy Time-Dimension of Space" (October 1961) — making this the earliest-dated professional/academic conference paper so far identified in the corpus after the 1957 timber monograph and 1958 *Yearbook of Agriculture* essay; does not, however, contain the "strong hands" credit-concentration mechanism, so C4's specific priority claim on concepts/land-monopoly is unaffected (see the dedicated page's priority-note section). **OCR note:** the masongaffney.org PDF's embedded text layer is poor-quality legacy scan-era OCR (e.g. "£_", "1%. ,aiZ", heavily garbled body text in spots); re-OCR'd this session at 250dpi with Tesseract 5.3.4 (`pdftoppm -r 250` + per-page `tesseract --psm 6`), which recovered dramatically cleaner text (17,195 words vs. ~13,437 from the embedded layer) — flagged `[VERIFY]` on the page as a residual transcription-risk caveat for exact figures despite the improvement, since the source scan quality itself is poor. **2026-07-18 update:** H4 (below) establishes that H3's Kaweah case study was publicly challenged in print by Dean Frank Trelease (Univ. of Wyoming Law) and that Gaffney's factual rebuttal (zero appropriative-right transfers on the Kaweah system for decades) went unanswered — the page's "Standing and Limits" section was corrected accordingly.
- [x] `H4-WaterLaw&amp;EconomicTransfersReply1.CV.CV.pdf` — https://masongaffney.org/publications/H4-WaterLaw%26EconomicTransfersReply1.CV.CV.pdf — read in full, 2026-07-18. **Mirror 404 resolved:** the cached ampersand-filename mirror was a 236-byte 404 stub (same failure mode seen on E15 last wave); a direct `%26`-encoded fetch from masongaffney.org recovered the real 452KB/17pp PDF. "Water Law and Economic Transfers of Water: A Reply," *Journal of Farm Economics* 44(2) (May 1962): 427-34 — a direct scholarly reply to Dean Frank Trelease's published comment on H3's Kaweah case study. **Fold** into [research/gaffney-water-rent-taxation](/wiki/gaffney-water-rent-taxation/)'s "Standing and Limits" section: this corrects the page's prior "no third-party peer review" characterization — H3's central claim *was* publicly challenged by a law school dean and survived (Gaffney's zero-transfers-for-decades rebuttal went unanswered in print). Also documents an early (1962) version of the ad valorem land tax as an automatic spillover-compensation mechanism. Native text, no OCR needed. This was this wave's most valuable catch precisely because it had been marked "not pursued" as a dead 404 in the prior wave's narrative.
- [x] `H5Comparison_of_Market_Pricing.CV.pdf` — https://masongaffney.org/publications/H5Comparison_of_Market_Pricing.CV.pdf — skimmed, 2026-07-18. "Comparison of Market Pricing and Other Means of Allocating Water Resources," a paper delivered to a Southeastern land economics conference, reusing H3's Kaweah/San Joaquin Valley material (boron toxicity, riparian doctrine history) for a non-Western audience. **Declined, no fold, no registry row:** the masongaffney.org PDF's text layer is severely garbled legacy OCR (worse than H3's — e.g. "CQMP4RSON OF MARKET PRCNG", multi-line passages unreadable without re-OCR), and the readable portions show no content beyond what H3 and H8's systematic doctrine comparison already cover more cleanly on the wiki page; a full re-OCR pass was judged disproportionate for a conference-talk restatement (C2/E1 decline precedent — no text mirror saved since not cited).
- [x] `H8-EconomicAspectsofWaterResourcePolicy.CV.pdf` — https://masongaffney.org/publications/H8-EconomicAspectsofWaterResourcePolicy.CV.pdf — read in full, 2026-07-18. "Economic Aspects of Water Resource Policy," *AJES* 28(2) (April 1969): 131-44, based on a June 1968 Penn State colloquium paper. **Fold** into [research/gaffney-water-rent-taxation](/wiki/gaffney-water-rent-taxation/)'s doctrine-assignment section: a systematic nine-criterion riparian-vs-appropriative doctrine comparison generalizing H3's single-river Kaweah diagnosis, plus a primary-source economic-theory account of why California's Wright Act irrigation districts work (natural-monopoly conveyance economies, land-tax-financed settler credit, forced-inclusion compactness) — cross-linked to, and complementary with, [research/california-irrigation-districts](/wiki/california-irrigation-districts/), whose existing source is a secondary Georgist-movement account rather than Gaffney's own. Contra this wave's opening "also-ran" framing, this proved one of the stronger H-series finds. Native, cleanly `pdftotext`-extractable text; no OCR needed.
- [ ] `I11-TaxInducedSlowTurnoverofCapital.CV.CV.pdf` — https://masongaffney.org/publications/I11-TaxInducedSlowTurnoverofCapital.CV.CV.pdf
- [ ] `I16Environmental_Policies_and_Full_Employment.CV.pdf` — https://masongaffney.org/publications/I16Environmental_Policies_and_Full_Employment.CV.pdf
- [ ] `I1Full_Employment_Limited_Land_&amp;_Capital.CV.pdf` — https://masongaffney.org/publications/I1Full_Employment_Limited_Land_&amp;_Capital.CV.pdf
- [ ] `I2012Gaffney_Reverberations_AFEE_lecture_2012.pdf` — https://masongaffney.org/publications/I2012Gaffney_Reverberations_AFEE_lecture_2012.pdf
- [ ] `I2015-AJES-v74-n2-Real-assets-model.pdf` — https://masongaffney.org/publications/I2015-AJES-v74-n2-Real-assets-model.pdf
- [ ] `I6A-1996_Taxes_Capital_and_Jobs_1978_revised.pdf` — https://masongaffney.org/publications/I6A-1996_Taxes_Capital_and_Jobs_1978_revised.pdf
- [ ] `I6Taxes_Capital_and_Jobs.CV.pdf` — https://masongaffney.org/publications/I6Taxes_Capital_and_Jobs.CV.pdf
- [x] `K142_Centuries_Thought_Land_Taxation.CV.pdf` — https://masongaffney.org/publications/K142_Centuries_Thought_Land_Taxation.CV.pdf — [research/gaffney-two-centuries-land-taxation](/wiki/gaffney-two-centuries-land-taxation/), 2026-07-17
- [x] `K17-AlfredRusselWallacesCampaign.CV.pdf` — https://masongaffney.org/publications/K17-AlfredRusselWallacesCampaign.CV.pdf — read in full, 2026-07-18. "Alfred Russel Wallace's Campaign to Nationalize Land: How Darwin's Peer Learned from John Stuart Mill and Became Henry George's Ally," *AJES* 56(4) (Oct. 1997): 609–615. The wiki already carried a well-sourced [people/alfred-russel-wallace](/wiki/alfred-russel-wallace/) page built from Wallace's own primary texts (his 1880/1882 works) and NHM archival records, so this piece was folded as a **delta**, not a rewrite: the compensation-annuity's precise design (limited to "lives in being," based only on pre-nationalization net income, not highest-and-best-use), Mill's Land Tenure Reform Association personally recruiting Wallace (also folded, lightly, into [people/john-stuart-mill](/wiki/john-stuart-mill/)), the post-1873 turn to Wallace's own 1881 Society and his criticism of Parnell's peasant-proprietorship scheme, Asquith's "Tax or Buy" pincer slogan, the contrast with Huxley/Spencer/Sumner social Darwinism, and Gaffney's closing 1947-Planning-Act assessment. **OCR note:** the masongaffney.org PDF is a 300dpi scanned image with a garbled legacy OCR text layer (misread "Gaffney" as "GFrFx," "Marx" as "Maix," etc.); re-OCR'd this session at 300dpi with Tesseract 5.3.4, which resolved these before quotation.
- [x] `K18George_McGlynn_and_Leo_XIII.pdf` — https://masongaffney.org/publications/K18George_McGlynn_and_Leo_XIII.pdf — skimmed in full, 2026-07-18. **Declined, no fold, no registry row.** A 1997/2000 conference paper (34pp) on the McGlynn/Corrigan/Leo XIII church conflict, substantially personal/genealogical in its opening sections (Gaffney's own Fenian/Georgist family history) and otherwise a political-religious narrative largely superseded, for wiki purposes, by the existing [people/edward-mcglynn](/wiki/edward-mcglynn/) page — built from Henry George Jr.'s *Life of Henry George* with directly-quoted primary correspondence — which already covers the 1886 campaign, suspension, excommunication, and 1892 reinstatement in more granular, better-sourced detail. Grepped for economic-theory content (single tax, land value, rent, Ricardo, neoclassical, marginal) and found none beyond passing mentions of "the single tax" as a political label; this is religious/political history, not history-of-economic-thought, and out of this wave's cluster scope.
- [x] `K1Neo-classical_Stratagem.CV.pdf` — https://masongaffney.org/publications/K1Neo-classical_Stratagem.CV.pdf — reconciliation fix, 2026-07-18 (found while surveying this wave's candidate pool, not separately re-read): already the source for [research/gaffney-neoclassical-stratagem](/wiki/gaffney-neoclassical-stratagem/) and cited twice in sources/registry.csv (rows "Neo-classical Economics as a Stratagem Against Henry George" and "The Corruption of Economics") — the checkbox was simply never flipped when that page was built. No content change.
- [x] `K2008_Keeping_Land_in_Capital_Theory.pdf` — https://masongaffney.org/publications/K2008_Keeping_Land_in_Capital_Theory.pdf — read in full, 2026-07-18. "Keeping Land in Capital Theory: Ricardo, Faustmann, Wicksell, and George," *AJES* 67(1) (Jan. 2008): 119–142. **Reconciliation + delta:** this paper was already partially quoted (one sentence) on [research/gaffney-financial-maturity-timber](/wiki/gaffney-financial-maturity-timber/) — with the issue number miscited as 67(2) — but had never been registered in sources/registry.csv and its checkbox was never flipped; both fixed. Beyond the Faustmann-formula material already covered on that page, this paper's most valuable unmined content is (a) the historiographical link between the Austrian "period of production" concept and the Clark/Knight-vs-Austrians feud (citing Stigler 1941: 278) as further evidence for the land-capital-merger thesis, and (b) three specific Wicksell contributions to capital theory (the "grape-juice" coexistence model, the wages-fund-to-wages-flow reformulation, and explicitly folding site rent into the wages-flow) — none of which appeared anywhere else on the wiki. Both folded into [concepts/marginal-productivity](/wiki/marginal-productivity/) rather than the timber page, to keep that page's scope on Faustmann/forestry. **OCR note:** the masongaffney.org PDF's embedded text layer was completely empty (image-only scan, `pdftotext` returned 0 words); read via a full 25-page, 250dpi Tesseract 5.3.4 re-OCR this session.
- [x] `K2012_Going_My_Way.pdf` — https://masongaffney.org/publications/K2012_Going_My_Way.pdf — skimmed, 2026-07-18. **Declined, no fold, no registry row.** "Going My Way? Wending a Way Through the Stumbling Blocks between Georgism and Catholicism," *AJES* (2012; the source PDF is a pre-publication proof with volume/issue numbers left as placeholders, "Vol. ••, No. ••") — a wide-ranging essay on Georgist/Catholic social-doctrine tensions (social gospel vs. individual salvation, RCC sex-abuse scandals, Susan Pace Hamill's Alabama tax-reform campaign, etc.), explicitly building on and cross-referencing K18/McGlynn. Grepped for economic-theory content and found only passing policy mentions (land-value tax rates, generic references to taxing land values); no history-of-economic-thought content and no claims not already better-sourced elsewhere on the wiki (e.g. Hamill's Alabama campaign, if pursued, belongs with the wiki's US state tax-reform material, not this cluster). Out of this wave's scope; not pursued further.
- [ ] `K9-StabileHGInfluenceonJBClarkMGComments.CV.pdf` — https://masongaffney.org/publications/K9-StabileHGInfluenceonJBClarkMGComments.CV.pdf
- [ ] `L2018_Gaffney-Cobb-draft-Corporate-Power-&amp;-Military-2018-07-22.pdf` — https://masongaffney.org/publications/L2018_Gaffney-Cobb-draft-Corporate-Power-&amp;-Military-2018-07-22.pdf
- [ ] `L2Rent-Seeking_and_Global_Conflict.CV.pdf` — https://masongaffney.org/publications/L2Rent-Seeking_and_Global_Conflict.CV.pdf
- [ ] `N3Justice_in_Distribution.CV.pdf` — https://masongaffney.org/publications/N3Justice_in_Distribution.CV.pdf
- [ ] `O11Time_Taxes_Turnover.CV.pdf` — https://masongaffney.org/publications/O11Time_Taxes_Turnover.CV.pdf
- [ ] `O11aTaxes_on_Yield_Property_Income_and_Site.CV.pdf` — https://masongaffney.org/publications/O11aTaxes_on_Yield_Property_Income_and_Site.CV.pdf
- [ ] `O12-IrrigationDistricts&amp;EconomicDevelopmentSanJoaquinValley.CV.CV.pdf` — https://masongaffney.org/publications/O12-IrrigationDistricts&amp;EconomicDevelopmentSanJoaquinValley.CV.CV.pdf
- [ ] `O18Land_Ethics.CV.pdf` — https://masongaffney.org/publications/O18Land_Ethics.CV.pdf
- [ ] `Z1-LandasShareofWealthLACounty1971.CV.pdf` — https://masongaffney.org/publications/Z1-LandasShareofWealthLACounty1971.CV.pdf

### /workpapers/ (73)
- [ ] `1972_Benefits_of_Military_Spending.pdf` — https://masongaffney.org/workpapers/1972_Benefits_of_Military_Spending.pdf
- [x] `A_better_way_of_gauging_excess_burden_of_shiftable_taxes_2005.CV.pdf` — https://masongaffney.org/workpapers/A_better_way_of_gauging_excess_burden_of_shiftable_taxes_2005.CV.pdf — [research/gaffney-excess-burden-shiftable-taxes.md](/wiki/gaffney-excess-burden-shiftable-taxes/)
- [x] `Capital_Gains_and_Future_of_Free_Enterprise.pdf` — https://masongaffney.org/workpapers/Capital_Gains_and_Future_of_Free_Enterprise.pdf — [research/gaffney-capital-gains-free-enterprise](/wiki/gaffney-capital-gains-free-enterprise/), 2026-07-18. 1991 (rev. Dec. 1991) chapter for Richard Noyes (ed.), *Now the Synthesis*. Wired into problems/capital-share-rise-is-land (ancestor-statement to the modern Rognlie/Piketty capital-share decomposition), concepts/unearned-increment (new section: Georgist-origins history of the U.S. income tax + tax-loophole catalogue), and benefits/lvt-can-replace-capital-taxes-without-efficiency-loss (1960s accelerated-depreciation episode as an informal land-for-capital tax shift).
- [x] `Causes_of_downturn--Austro-Georgist_synthesis_1982.pdf` — https://masongaffney.org/workpapers/Causes_of_downturn--Austro-Georgist_synthesis_1982.pdf — [research/gaffney-causes-of-downturns.md](/wiki/gaffney-causes-of-downturns/)
- [x] `Factitious_Locational_Obsolescence_in_Land_Booms_WP041 .pdf` — https://masongaffney.org/workpapers/Factitious_Locational_Obsolescence_in_Land_Booms_WP041%20.pdf — [research/gaffney-land-market-distortions.md](/wiki/gaffney-land-market-distortions/), 2026-07-17
- [ ] `How_Religious_Awakenings_Presage_Radical_Reforms.pdf` — https://masongaffney.org/workpapers/How_Religious_Awakenings_Presage_Radical_Reforms.pdf
- [x] `How_Rising_rents_devour_ capital_1993_WP039.pdf` — https://masongaffney.org/workpapers/How_Rising_rents_devour_%20capital_1993_WP039.pdf — [research/gaffney-land-booms-destroy-capital.md](/wiki/gaffney-land-booms-destroy-capital/)
- [x] `How_a_Land_Boom_Destroys_Capital_10_2005.pdf` — https://masongaffney.org/workpapers/How_a_Land_Boom_Destroys_Capital_10_2005.pdf — [research/gaffney-land-booms-destroy-capital.md](/wiki/gaffney-land-booms-destroy-capital/)
- [ ] `How_an_interest_hike_destroys_capital_1996.pdf` — https://masongaffney.org/workpapers/How_an_interest_hike_destroys_capital_1996.pdf
- [x] `Land_Markets_Lead_to_Misallocating_Capital_WP042 .pdf` — https://masongaffney.org/workpapers/Land_Markets_Lead_to_Misallocating_Capital_WP042%20.pdf — [research/gaffney-land-market-distortions.md](/wiki/gaffney-land-market-distortions/), 2026-07-17
- [ ] `Logos_Abused.pdf` — https://masongaffney.org/workpapers/Logos_Abused.pdf
- [ ] `Oil_and_Gas_Leasing--a_Study_in_Pseudo-Socialism.pdf` — https://masongaffney.org/workpapers/Oil_and_Gas_Leasing--a_Study_in_Pseudo-Socialism.pdf
- [ ] `Philippines_Land_Reform_Through_Tax_Reform.pdf` — https://masongaffney.org/workpapers/Philippines_Land_Reform_Through_Tax_Reform.pdf
- [ ] `The_US_Canal_Boom_and_Bust_1820-42_WP01.pdf` — https://masongaffney.org/workpapers/The_US_Canal_Boom_and_Bust_1820-42_WP01.pdf
- [ ] `WP001 The_US_Canal_Boom_and_Bust_1820-42_WP01.pdf` — https://masongaffney.org/workpapers/WP001%20The_US_Canal_Boom_and_Bust_1820-42_WP01.pdf
- [ ] `WP014 Newark and the Office Building Model of Urban Renewal.pdf` — https://masongaffney.org/workpapers/WP014%20Newark%20and%20the%20Office%20Building%20Model%20of%20Urban%20Renewal.pdf
- [ ] `WP018 George's Economics of Abundance.pdf` — https://masongaffney.org/workpapers/WP018%20George's%20Economics%20of%20Abundance.pdf
- [ ] `WP019 George &amp; Danger of Favoring Capital Over Labor.pdf` — https://masongaffney.org/workpapers/WP019%20George%20&amp;%20Danger%20of%20Favoring%20Capital%20Over%20Labor.pdf
- [ ] `WP020 Economic Development as a Response to Stress.pdf` — https://masongaffney.org/workpapers/WP020%20Economic%20Development%20as%20a%20Response%20to%20Stress.pdf
- [ ] `WP024 Macroeconomics as a field of study.pdf` — https://masongaffney.org/workpapers/WP024%20Macroeconomics%20as%20a%20field%20of%20study.pdf
- [ ] `WP025 Labor Productivity and Farm Intensity.pdf` — https://masongaffney.org/workpapers/WP025%20Labor%20Productivity%20and%20Farm%20Intensity.pdf
- [ ] `WP028 Making jobs by changing factor proportions.pdf` — https://masongaffney.org/workpapers/WP028%20Making%20jobs%20by%20changing%20factor%20proportions.pdf
- [ ] `WP032 Capital-intensity of warfare.pdf` — https://masongaffney.org/workpapers/WP032%20Capital-intensity%20of%20warfare.pdf
- [ ] `WP038 George and Mill on Labor-Saving vs. Land-Saving Technology.pdf` — https://masongaffney.org/workpapers/WP038%20George%20and%20Mill%20on%20Labor-Saving%20vs.%20Land-Saving%20Technology.pdf
- [ ] `WP039 How_Rising_rents_devour_ capital_1993_WP039.pdf` — https://masongaffney.org/workpapers/WP039%20How_Rising_rents_devour_%20capital_1993_WP039.pdf
- [ ] `WP040 Chicago boom and bust - A cycle of capital waste.pdf` — https://masongaffney.org/workpapers/WP040%20Chicago%20boom%20and%20bust%20-%20A%20cycle%20of%20capital%20waste.pdf
- [ ] `WP041 Factitious_Locational_Obsolescence_in_Land_Booms_WP041 .pdf` — https://masongaffney.org/workpapers/WP041%20Factitious_Locational_Obsolescence_in_Land_Booms_WP041%20.pdf
- [ ] `WP042 Land_Markets_Lead_to_Misallocating_Capital_WP042 .pdf` — https://masongaffney.org/workpapers/WP042%20Land_Markets_Lead_to_Misallocating_Capital_WP042%20.pdf
- [ ] `WP043 Tax Policy and Capital Formation.pdf` — https://masongaffney.org/workpapers/WP043%20Tax%20Policy%20and%20Capital%20Formation.pdf
- [ ] `WP044 Farm Labor Productivity Tradeoff with Water Use.pdf` — https://masongaffney.org/workpapers/WP044%20Farm%20Labor%20Productivity%20Tradeoff%20with%20Water%20Use.pdf
- [ ] `WP045 Critique of Thorstein Veblen Victorian Firebrand by Jorgensens.pdf` — https://masongaffney.org/workpapers/WP045%20Critique%20of%20Thorstein%20Veblen%20Victorian%20Firebrand%20by%20Jorgensens.pdf
- [ ] `WP046 Measure C and Riverside Property Values.pdf` — https://masongaffney.org/workpapers/WP046%20Measure%20C%20and%20Riverside%20Property%20Values.pdf
- [ ] `WP048 Peace Dividends, Land Bubbles and Economic Disasters in U.S. History.pdf` — https://masongaffney.org/workpapers/WP048%20Peace%20Dividends,%20Land%20Bubbles%20and%20Economic%20Disasters%20in%20U.S.%20History.pdf
- [ ] `WP049 Peace Dividends and Land Booms in World History.pdf` — https://masongaffney.org/workpapers/WP049%20Peace%20Dividends%20and%20Land%20Booms%20in%20World%20History.pdf
- [ ] `WP050  Water as Yield-cutting Substitute.pdf` — https://masongaffney.org/workpapers/WP050%20%20Water%20as%20Yield-cutting%20Substitute.pdf
- [ ] `WP051 Who Owns Southern California.pdf` — https://masongaffney.org/workpapers/WP051%20Who%20Owns%20Southern%20California.pdf
- [ ] `WP053 Alaska's proposed tax on oil reserves in situ 1981.pdf` — https://masongaffney.org/workpapers/WP053%20Alaska's%20proposed%20tax%20on%20oil%20reserves%20in%20situ%201981.pdf
- [ ] `WP054 Oil_and_Gas_Leasing--a_Study_in_Pseudo-Socialism.pdf` — https://masongaffney.org/workpapers/WP054%20Oil_and_Gas_Leasing--a_Study_in_Pseudo-Socialism.pdf
- [ ] `WP055 Rent, Taxation, Dissipation and Federalism.pdf` — https://masongaffney.org/workpapers/WP055%20Rent,%20Taxation,%20Dissipation%20and%20Federalism.pdf
- [ ] `WP056 Full employment thru total tax reform.pdf` — https://masongaffney.org/workpapers/WP056%20Full%20employment%20thru%20total%20tax%20reform.pdf
- [ ] `WP057 Economics in support of environmentalism.pdf` — https://masongaffney.org/workpapers/WP057%20Economics%20in%20support%20of%20environmentalism.pdf
- [ ] `WP057 F3-EconomicsinSupportofEnvironmentalism.htm` — https://masongaffney.org/workpapers/WP057%20F3-EconomicsinSupportofEnvironmentalism.htm
- [ ] `WP058 Conservation in a World of Private Property Extremists.pdf` — https://masongaffney.org/workpapers/WP058%20Conservation%20in%20a%20World%20of%20Private%20Property%20Extremists.pdf
- [ ] `WP061 Token_Timber_Taxation_Mendocino_County_2000.pdf` — https://masongaffney.org/workpapers/WP061%20Token_Timber_Taxation_Mendocino_County_2000.pdf
- [ ] `WP062 Observed Behavior vs A Priori Dogmatism in Land Markets.pdf` — https://masongaffney.org/workpapers/WP062%20Observed%20Behavior%20vs%20A%20Priori%20Dogmatism%20in%20Land%20Markets.pdf
- [x] `WP067 A_better_way_of_gauging_excess_burden_of_shiftable_taxes_2005.CV.pdf` — https://masongaffney.org/workpapers/WP067%20A_better_way_of_gauging_excess_burden_of_shiftable_taxes_2005.CV.pdf — duplicate of the row above; see [research/gaffney-excess-burden-shiftable-taxes.md](/wiki/gaffney-excess-burden-shiftable-taxes/)
- [ ] `WP068 Raising output by removing tax bias.pdf` — https://masongaffney.org/workpapers/WP068%20Raising%20output%20by%20removing%20tax%20bias.pdf
- [ ] `WP070 Unearned Income as a Barrier to Free Enterprise.pdf` — https://masongaffney.org/workpapers/WP070%20Unearned%20Income%20as%20a%20Barrier%20to%20Free%20Enterprise.pdf
- [ ] `WP071 Prop 13 and the Decline of California.pdf` — https://masongaffney.org/workpapers/WP071%20Prop%2013%20and%20the%20Decline%20of%20California.pdf
- [ ] `WP072 When California had a Magnetic Tax System.pdf` — https://masongaffney.org/workpapers/WP072%20When%20California%20had%20a%20Magnetic%20Tax%20System.pdf
- [ ] `WP073 Property Tax Reform in Big Picture.pdf` — https://masongaffney.org/workpapers/WP073%20Property%20Tax%20Reform%20in%20Big%20Picture.pdf
- [ ] `WP074 Californias Balkanized Tax Base.pdf` — https://masongaffney.org/workpapers/WP074%20Californias%20Balkanized%20Tax%20Base.pdf
- [ ] `WP076 South African Diary, March 17-30, 1992.pdf` — https://masongaffney.org/workpapers/WP076%20South%20African%20Diary,%20March%2017-30,%201992.pdf
- [ ] `WP077 Enterprising Johannesburg and Sleepy Cape Town-A Contrast.pdf` — https://masongaffney.org/workpapers/WP077%20Enterprising%20Johannesburg%20and%20Sleepy%20Cape%20Town-A%20Contrast.pdf
- [ ] `WP078 Critique of South African Katz Commision (sic) Reports.pdf` — https://masongaffney.org/workpapers/WP078%20Critique%20of%20South%20African%20Katz%20Commision%20(sic)%20Reports.pdf
- [ ] `WP079 Privatization without giveaway-capitalism without kleptocracy.pdf` — https://masongaffney.org/workpapers/WP079%20Privatization%20without%20giveaway-capitalism%20without%20kleptocracy.pdf
- [ ] `WP080 Taxable Surplus in Russian Land.pdf` — https://masongaffney.org/workpapers/WP080%20Taxable%20Surplus%20in%20Russian%20Land.pdf
- [ ] `WP083 Russian Land rent in a tax-free economy.pdf` — https://masongaffney.org/workpapers/WP083%20Russian%20Land%20rent%20in%20a%20tax-free%20economy.pdf
- [ ] `WP084 Salestax Suicides Through History.pdf` — https://masongaffney.org/workpapers/WP084%20Salestax%20Suicides%20Through%20History.pdf
- [ ] `WP085 California Sales Tax Revenues by City and Type of Sales.pdf` — https://masongaffney.org/workpapers/WP085%20California%20Sales%20Tax%20Revenues%20by%20City%20and%20Type%20of%20Sales.pdf
- [ ] `WP086 Sales Tax Revenues vs Taxable Property Values, California Counties, 1993-1994.pdf` — https://masongaffney.org/workpapers/WP086%20Sales%20Tax%20Revenues%20vs%20Taxable%20Property%20Values,%20California%20Counties,%201993-1994.pdf
- [ ] `WP087 Salestax Leakages-Why Yield Less than Income Tax.pdf` — https://masongaffney.org/workpapers/WP087%20Salestax%20Leakages-Why%20Yield%20Less%20than%20Income%20Tax.pdf
- [ ] `WP088 Replacing California Sales Tax with Property Tax, Regional Impacts.pdf` — https://masongaffney.org/workpapers/WP088%20Replacing%20California%20Sales%20Tax%20with%20Property%20Tax,%20Regional%20Impacts.pdf
- [ ] `WP089 Cleveland's Explosive Growth under Mayors Tom Johnson and Newton Baker.pdf` — https://masongaffney.org/workpapers/WP089%20Cleveland's%20Explosive%20Growth%20under%20Mayors%20Tom%20Johnson%20and%20Newton%20Baker.pdf
- [ ] `WP091Chicago's growth spurt 1890-1900.pdf` — https://masongaffney.org/workpapers/WP091Chicago's%20growth%20spurt%201890-1900.pdf
- [ ] `WP095 2005 Temporal excess burden of Taxes on Buildings.pdf` — https://masongaffney.org/workpapers/WP095%202005%20Temporal%20excess%20burden%20of%20Taxes%20on%20Buildings.pdf
- [ ] `WP096 2005 The Physiocratic Concept of ATCOR.pdf` — https://masongaffney.org/workpapers/WP096%202005%20The%20Physiocratic%20Concept%20of%20ATCOR.pdf
- [ ] `WP097 2004 Unknown revenue potential of land 15 hidden elements.pdf` — https://masongaffney.org/workpapers/WP097%202004%20Unknown%20revenue%20potential%20of%20land%2015%20hidden%20elements.pdf
- [ ] `WP098 The Value of Land Seminar 2002.pdf` — https://masongaffney.org/workpapers/WP098%20The%20Value%20of%20Land%20Seminar%202002.pdf
- [ ] `WP099 2004 Housing and Income seminar January revision.pdf` — https://masongaffney.org/workpapers/WP099%202004%20Housing%20and%20Income%20seminar%20January%20revision.pdf
- [ ] `WP100 1999 OECD versus Harmful Tax Competition.pdf` — https://masongaffney.org/workpapers/WP100%201999%20OECD%20versus%20Harmful%20Tax%20Competition.pdf
- [ ] `WP101 1994 Land booms, Capital Stretch-out and Banking Collapse.pdf` — https://masongaffney.org/workpapers/WP101%201994%20Land%20booms,%20Capital%20Stretch-out%20and%20Banking%20Collapse.pdf
- [ ] `WP105 Why Should We Care About Land Value and Why Now.pdf` — https://masongaffney.org/workpapers/WP105%20Why%20Should%20We%20Care%20About%20Land%20Value%20and%20Why%20Now.pdf

### /essays/ (30)
- [x] `2006_Severance_Tax_on_California_Oil.pdf` — https://masongaffney.org/essays/2006_Severance_Tax_on_California_Oil.pdf — [research/gaffney-california-severance-tax](/wiki/gaffney-california-severance-tax/), 2026-07-16
- [ ] `Americas_Low_Savings_Rate_8-9_2005.pdf` — https://masongaffney.org/essays/Americas_Low_Savings_Rate_8-9_2005.pdf
- [ ] `Answer_to_Futilitarians_1998.pdf` — https://masongaffney.org/essays/Answer_to_Futilitarians_1998.pdf
- [x] `Corporations_Democracy_and_the_US_Supreme_Court.pdf` — https://masongaffney.org/essays/Corporations_Democracy_and_the_US_Supreme_Court.pdf — **read and triaged 2026-07-18, declined a research page.** A 2010 political essay on *Citizens United v. FEC* and the legal history of corporate personhood (Dartmouth College v. Woodward, Santa Clara v. Southern Pacific, Citizens United), using the falling share of federal revenue from the corporate income tax as a loose "metric" of corporate power. Its only rent-relevant claim — "the corporate income tax is mainly a tax on economic rent," citing Stiglitz and Martin Feldstein (*JPE* 85(2), April 1977, p. 357) — cites work the wiki already carries independently ([research/feldstein-incidence-pure-rent](/wiki/feldstein-incidence-pure-rent/), the same *JPE* 1977 issue) rather than adding new analysis. The remaining ~95% of the essay (corporate-personhood doctrine, campaign-finance remedies, U.S. constitutional history) is a political-history argument tangential to the rent-capture mission per EDITORIAL §0's scope rule, not a page-worthy contribution to it. Registry row added (`Corporations, Democracy, and the U.S. Supreme Court`, Status: Referenced, Scan Depth: Light, no Wiki Page) for provenance; moved to TIER 3 (archive-only) below.
- [ ] `Denying_Inflation--Who_Why_and_How_12_2005.pdf` — https://masongaffney.org/essays/Denying_Inflation--Who_Why_and_How_12_2005.pdf
- [ ] `Empty_Spaces_final_3-29.pdf` — https://masongaffney.org/essays/Empty_Spaces_final_3-29.pdf
- [ ] `Europes_Fatal_Affair_with_VAT_071713a.pdf` — https://masongaffney.org/essays/Europes_Fatal_Affair_with_VAT_071713a.pdf
- [x] `Europes_Fatal_Affair_with_VAT_Harrison_2016.pdf` — https://masongaffney.org/essays/Europes_Fatal_Affair_with_VAT_Harrison_2016.pdf — [research/gaffney-europes-fatal-affair-with-vat.md](/wiki/gaffney-europes-fatal-affair-with-vat/)
- [ ] `Four_vampires_of_capital.pdf` — https://masongaffney.org/essays/Four_vampires_of_capital.pdf
- [x] `Full_employment_thru_total_tax_reform_1993.pdf` — https://masongaffney.org/essays/Full_employment_thru_total_tax_reform_1993.pdf — [research/gaffney-full-employment-tax-reform.md](/wiki/gaffney-full-employment-tax-reform/)
- [ ] `GAffney_interview_in_Canada_Sun_Life_Financial.pdf` — https://masongaffney.org/essays/GAffney_interview_in_Canada_Sun_Life_Financial.pdf
- [x] `Georges_Economics_of_Abundance.pdf` — https://masongaffney.org/essays/Georges_Economics_of_Abundance.pdf — [research/gaffney-economics-of-abundance](/wiki/gaffney-economics-of-abundance/), 2026-07-16
- [ ] `Great_Crash_of_2008.pdf` — https://masongaffney.org/essays/Great_Crash_of_2008.pdf
- [ ] `Great_Expectations.pdf` — https://masongaffney.org/essays/Great_Expectations.pdf
- [ ] `Henry_George_100_Years_Later.pdf` — https://masongaffney.org/essays/Henry_George_100_Years_Later.pdf
- [ ] `How_to_Thaw_Credit.pdf` — https://masongaffney.org/essays/How_to_Thaw_Credit.pdf
- [ ] `I-920-OpEd.pdf` — https://masongaffney.org/essays/I-920-OpEd.pdf
- [ ] `I_bozze_Book_Review_of_Stabile_The_Living_Wage_2010.pdf` — https://masongaffney.org/essays/I_bozze_Book_Review_of_Stabile_The_Living_Wage_2010.pdf
- [ ] `NewCommonsDiscussion-1.pdf` — https://masongaffney.org/essays/NewCommonsDiscussion-1.pdf
- [ ] `Repopulating_New_Orleans_dollarsandsense.pdf` — https://masongaffney.org/essays/Repopulating_New_Orleans_dollarsandsense.pdf
- [ ] `Sales_Tax_Bias_Against_Turnover.pdf` — https://masongaffney.org/essays/Sales_Tax_Bias_Against_Turnover.pdf
- [ ] `Shrinking_Dollar_for_Insights_Dec_07.pdf` — https://masongaffney.org/essays/Shrinking_Dollar_for_Insights_Dec_07.pdf
- [ ] `Sleeping_with_the_Enemy.pdf` — https://masongaffney.org/essays/Sleeping_with_the_Enemy.pdf
- [ ] `Stimulus--the_False_and_the_True_2008.pdf` — https://masongaffney.org/essays/Stimulus--the_False_and_the_True_2008.pdf
- [ ] `Tax_Reforms_to_Promote_Saving_Would_Backfire_6_2005.pdf` — https://masongaffney.org/essays/Tax_Reforms_to_Promote_Saving_Would_Backfire_6_2005.pdf
- [ ] `The_Danger_of_Favoring_Capital_Over_Labor_Spring_2004.pdf` — https://masongaffney.org/essays/The_Danger_of_Favoring_Capital_Over_Labor_Spring_2004.pdf
- [ ] `The_Red_and_the_Blue_04-12.pdf` — https://masongaffney.org/essays/The_Red_and_the_Blue_04-12.pdf
- [ ] `The_Sales_Tax--History_of_a_Dumb_Idea_3_2005.pdf` — https://masongaffney.org/essays/The_Sales_Tax--History_of_a_Dumb_Idea_3_2005.pdf
- [ ] `What_Is_Consumption_10_2005.pdf` — https://masongaffney.org/essays/What_Is_Consumption_10_2005.pdf
- [ ] `Whats_the_Matter_with_Michigan.pdf` — https://masongaffney.org/essays/Whats_the_Matter_with_Michigan.pdf


## Tier decisions (T1, 2026-07-16 — wave 1)

**TIER 1 — READ&MINE now (mirrored to sources/gaffney/, OCR text in sources/gaffney/text/):**
| work | claim-lane target |
|---|---|
| Causes of Downturns: an Austro-Georgist Synthesis (1982) | cycles lane — precursor to Foldvary's synthesis; narratives/land-speculation-causes-cycles, objections/cycles-are-credit-not-land |
| How a Land Boom Destroys Capital (2005) + How Rising Rents Devour Capital (1993) | cycles/capital-destruction mechanism (pair) |
| Europe's Fatal Affair with VAT (Harrison ed. 2016) | ATCOR/tax-shift — benefits/lvt-can-replace-capital-taxes-without-efficiency-loss |
| Full Employment through Total Tax Reform (1993) | benefits/taxing-land-raises-productivity |
| New Life in Old Cities (2006) | urban revival — benefits/split-rate-increases-construction, problems/speculative-vacancy-wastes-cities |
| George's Economics of Abundance | narratives lane |
| A Severance Tax on California Oil (2006) | resource rents — benefits/resource-rent-capture-works |
| A Better Way of Gauging Excess Burden of Shiftable Taxes (2005) | concepts/deadweight-loss, ATCOR support |
| The Philosophy of Public Finance (1998, Ch. 7 of *The Losses of Nations*) | **done 2026-07-16** — ATCOR formal derivation, philosophy of site value taxation; problems/land-rent-could-fund-government, objections/lvt-not-enough-revenue, benefits/split-rate-increases-construction |

**TIER 2 — next waves (not yet mirrored):** Oil & Gas: Unfinished Tax Reform,
Americas Low Savings Rate, Four Vampires of Capital, Answer to Futilitarians. (The
Alaska leasing pair, Soil Depletion & Land Rent, Counter-colonial Land Policy for
Montana, Capital Gains and the Future of Free Enterprise, Land Markets Lead to
Misallocating Capital, Factitious Locational Obsolescence in Land Booms, the
timber/forest taxation trio, and Corporations Democracy & the US Supreme Court —
all listed here as of 2026-07-16 — are now done or triaged; see the dated entries
above and below.)

**2026-07-17:** *Two Centuries of Economic Thought on Taxation of Land Rents* (1982, in
Lindholm & Lynn eds., *Land Value Taxation: The Progress and Poverty Centenary*, Univ. of
Wisconsin Press for TRED — not a Lincoln Institute volume, confirmed via Stanford SearchWorks)
read, drafted, and wired — see
[research/gaffney-two-centuries-land-taxation](/wiki/gaffney-two-centuries-land-taxation/).
Registry row flipped Scanned/Heavy, tier core. Wired into
objections/marshall-single-tax-objection (Marshall's 1909 Lloyd George support),
objections/progress-and-poverty-outdated (Walras and Wicksell as marginalist-generation
economists reaching George's conclusion), and objections/land-is-just-capital (a genuine
complication: Gaffney's primary reading groups Wicksteed's *theory*, not his politics, with
Clark's land-erasing move — in tension with Blaug's grouping of Wicksteed with Walras);
enriched people/ pages for Ricardo, Mill, Marshall, Walras, Wicksteed, Smith, Quesnay, Turgot,
Vickrey, Commons, Knight, Clark, and Gaffney's own works list.

**TIER 3 — archive-only for now:** remainder of the 190 (interviews, duplicates of published
versions, narrow appendices). Full-site preservation mirror: recommend an R2 bucket rather
than this repo (190 PDFs = hundreds of MB); repo carries worked texts only.

**Hosting basis:** webmaster permission (Floyd, 2026-07-16 directive) — record retained here;
Gaffney d. July 2020 (NYT obituary linked from masongaffney.org). Wiki texts/ hosting of any
full work stays gated on Floyd's publish approval as usual.
