# Verification Queue — every [CITATION NEEDED] / [VERIFY] marker, classified

Ground truth regenerated 2026-07-18 (T1 VERIFY-channel pass) by
`python3 scripts/verification_queue.py` (23 markers matching the script's strict
`[VERIFY:`/`[VERIFY]`/`[CITATION NEEDED:` regex) **plus 2 markers the script's regex
doesn't catch** (`[VERIFY — PENDING: ...]`, deliberately reformatted so they don't loop
back into the auto-queue — see narratives/land-speculation-causes-cycles.md) — **25
live markers total** across all content pages (`benefits/ books/ concepts/ events/
guides/ narratives/ objections/ organizations/ people/ places/ problems/ research/
texts/`; excludes `LOOPLOG.md`, `BACKLOG.md`, `sources/inbox/`, `sources/gaffney/text/`,
and this repo's own meta-docs, none of which carry live in-page markers).

This wave resolved **5**, then a same-day continuation pass worked the 6 RETRYABLE
rows queued below and resolved **3** more (see `sources/verification-backlog.md`
for both dated entries) — **22 live markers remain**, down from 30 at the start of
this pass. Markers are the wiki's anti-fabrication firewall (EDITORIAL rule 2).
**Never delete a marker without either resolving the claim (cite what was
verified) or downgrading it (weaken the claim to what's verifiable, note the
downgrade).**

Every marker below is classified into exactly one of three buckets:

- **DELIBERATE-SCOPED** — an honest, self-contained scope/limits note (OCR quality,
  session boundary, source-internal inconsistency, time-locked forecast, "this is as
  far as this session's read went"). These are not citation gaps waiting on a fetch;
  they are the wiki being honest about the edge of what it checked. **Leave in place.**
- **RETRYABLE** — a further fetch/search could plausibly resolve this. Listed with the
  channel/approach for the next pass.
- **BLOCKED** — attempted this wave (or a prior wave) and could not be resolved: book
  copy needed, paywalled with no free mirror found, or the underlying primary object
  doesn't appear to exist online (unpublished address, undated site, paywalled
   archive). Reason given per row.

## DELIBERATE-SCOPED (13) — stay in place, no action needed

- `narratives/land-speculation-causes-cycles.md` (×2, L58, L324) — Foldvary's 2026
  forecast is time-locked; cannot be assessed until the year closes. Revisit after
  year-end 2026 (already logged as SETTLED in `sources/verification-backlog.md`).
- `research/choi-sjoquist-atlanta-lvt-cge.md` (L57) — flags a genuine internal
  inconsistency **in the source itself** (added this session); nothing external to
  fetch, the inconsistency is the finding.
- `research/gaffney-alaska-oil-leasing.md` (L308) — "checked only against these
  appendices as OCR'd... not against any transmittal letter, legislative testimony,
  or correspondence" — an explicit scope boundary on a 155pp document already fully
  OCR'd and mined this session; further items (letters/testimony) may not survive in
  any archive.
- `research/gaffney-alaska-oil-leasing.md` (L427) — OCR-quality flag naming the
  specific garbled pages (Appendix C bar charts, Appendix K Moody's table) and
  confirming this page avoids quoting numbers from them. Textbook honest OCR caveat.
- `research/gaffney-capital-gains-free-enterprise.md` (L214) — "current status of each
  cited provision — out of scope for this page." Explicit scope statement, not a gap.
- `research/gaffney-financial-maturity-timber.md` (L35) — corrects a mischaracterization
  ("Duke dissertation-era") with the actual facts (NC State, 1957, one year after the
  Berkeley PhD) already stated in the same sentence; the marker wraps a correction
  already made, not an open question.
- `research/gaffney-financial-maturity-timber.md` (L244) — OCR-quality flag on
  mathematical/formula passages; page states it avoids quoting/restating the equations
  because of it.
- `research/gaffney-financial-maturity-timber.md` (L258) — backreference to the
  Samuelson-paywall note (see BLOCKED below), not an independent gap.
- `research/gaffney-land-distinctive-factor.md` (L209) — names exactly which of
  footnote 31's citations *was* independently read this session (the D1 companion
  piece) and which wasn't ("Who Owns Southern California?"); an honest partial-
  coverage record, not a blanket gap.
- `research/gaffney-new-life-in-old-cities.md` (L120) — "superlative claim, not
  benchmarked against an independent global cross-city dataset" — no such dataset is
  claimed to exist; this is an honest limits statement on a superlative, not a
  citation gap.
- `research/gaffney-rising-inequality-farm-property-tax.md` (L135) — describes a
  limitation **of the cited chapter itself** (no formal regression stats reported) —
  accurately characterizing the source's own evidentiary weight, not a wiki gap.
- `research/gaffney-soil-depletion-land-rent.md` (L186, L243) — the R2/archive-mirror
  ampersand-filename bug is an **infrastructure** issue (per `LOOPLOG.md`: "R2 upload
  BLOCKED on bucket access"), not a fact-check; the primary source itself is already
  confirmed reachable via two working free URLs (masongaffney.org + UNM repository).
- `research/giovannoni-labor-share-decomposition.md` — an analytical/theoretical
  caveat ("is this rent or a return to scarce skill?") the cited paper deliberately
  does not adjudicate; not resolvable by any fetch, it's an open question in the
  literature. (Note: the queue script mis-buckets this as `needs-book-copy` — a
  false-positive keyword match on "lending" inside the claim text, not an actual
  book-copy need.)

## RETRYABLE (1) — routed to Hermes

- `people/andy-burnham.md` (source note 4, added 2026-08-05) — the 2010 leadership-bid
  quotes ("an annual tax on the market rental value of land"; stamp duty as "a tax on
  the aspirations of young people") are carried on Wikipedia's authority only. A
  *Guardian* comment piece Burnham wrote during the 2010 contest arguing for taxing
  land values appears to be the primary. **Attempted** (2026-08-05): `theguardian.com`
  is not reachable by this environment's fetcher (blocked to the user agent), and web
  search returns only summaries partly derived from this wiki's own page and a 2026
  MoneyWeek explainer — circular, not verification. **Channel: needs-unblocked-web
  (Hermes).** Confirm the two quotes verbatim with headline and date, and settle
  whether Burnham framed the proposal as "aspirational socialism" — a phrase the
  MoneyWeek piece attributes to his 2010 position but which no primary source
  reachable from here supports, and which this wiki therefore does not assert.

## RETRYABLE — worked and cleared (the prior 6, 2026-07-18)

All 6 rows queued in the previous pass were worked in a same-day continuation
(2026-07-18). **3 resolved:**

- `research/august-rental-financialization.md` — resolved. A second independent
  mirror of the actual Taylor & Francis-typeset PDF (tandfonline.com branding,
  DOI cover page intact) was located via web search (a University of Waterloo-
  region community site) and extracted with `pdftotext`; every figure the wiki
  page cites was spot-checked line-for-line against the Herongate mirror and
  matched verbatim (164,498-suite REIT growth with footnote marker, the 290,712
  top-25 total, 15.8%→20.2% concentration, "27.8"/"one fifth" phrasing). Marker
  removed.
- `research/gaffney-forest-taxation.md` (L205) — resolved (partial). Identified
  Gaffney's likely source for the $42-billion figure: Marion Clawson, "The
  National Forests," *Science* 191(4228): 762–767 (1976) — its own abstract
  (read via PubMed; the article itself is paywalled) independently states
  "approximately $42 billion in assets" and "$400-500 million annually," which
  corroborates Gaffney's headline figure and revenue range. Gaffney's more
  granular $486-million 1974 receipts/outlays split remains his own citation of
  Clawson, not independently re-derived — noted honestly in place of the old
  blanket marker. New registry row added (Marion Clawson, "The National
  Forests," 1976, Light scan/abstract-only).
- `research/gaffney-soil-depletion-land-rent.md` (L173) — resolved. Semantic
  Scholar's paper-search API records 21 citations for Gaffney's 1965 paper.
  Marker removed.

**3 moved to BLOCKED** (see below): `gaffney-alaska-oil-leasing.md` (WorldCat
403'd in this environment), `gaffney-land-distinctive-factor.md` (Jarvis's book
is borrow-restricted on Internet Archive, no full-text search available), and
`gaffney-land-market-distortions.md` (no dated citing source found for
WP041/WP042 despite a fresh search).

## BLOCKED (6) — attempted, not resolvable this wave

- `research/gaffney-financial-maturity-timber.md` (L191) — Samuelson's "Economics of
  Forestry in an Evolving Society" (*Economic Inquiry*, 1976). **Attempted**: Wiley
  (paywalled), ResearchGate (HTTP 403). No free copy found. **Paid/library access**
  needed (JSTOR/Wiley or a university proxy).
- `research/gaffney-montana-land-policy.md` (L93) — the *Milwaukee Journal*, 29 August
  1971 article behind the "ten energy firms held 50% of Montana's federal coal
  leases" figure. **Attempted**: general web search found no free digitized copy.
  **Paid/library access** needed (newspapers.com, GenealogyBank, or the Milwaukee
  Journal Sentinel's own archive).
- `research/gaffney-new-life-in-old-cities.md` (L114) — an unpublished Andelson
  conference address (the source of "the city skyline froze for the next 75 years").
  **Attempted**: no trace of the address found online. **Likely unrecoverable** —
  unpublished conference remarks generally don't survive independently of the
  citing author's own account.
- `research/gaffney-alaska-oil-leasing.md` (L322) — publication/circulation history of
  the 1977 report beyond delivery to the Alaska Legislature/DNR. **Attempted**
  (2026-07-18): WorldCat (`worldcat.org` and `search.worldcat.org`) returned
  HTTP 403/429 on every access pattern tried in this environment; no citing
  paper or Alaska State Library catalog record surfaced via general web search.
  **Direct catalog access** needed (WorldCat outside this environment, or an
  Alaska State Library/legislative-archives lookup).
- `research/gaffney-land-distinctive-factor.md` (L112) — Gaffney's polemical framing of
  Howard Jarvis's "services to property, not services to people" slogan.
  **Attempted** (2026-07-18): general web search for the verbatim phrase found
  no primary source; Jarvis's *I'm Mad As Hell* (1979) exists on Internet
  Archive only as a borrow-restricted scan (no full-text search without a
  loan); a previously indexed third-party full-text mirror
  (members.tripod.com) no longer resolves (DNS failure). **Book/archival
  access** needed — a library loan of *I'm Mad As Hell* or contemporaneous
  Prop. 13 campaign literature.
- `research/gaffney-land-market-distortions.md` (L41) — exact publication date of
  WP041/WP042. **Attempted again** (2026-07-18): masongaffney.org's workpapers
  listing and vita/CV page still show no date for either entry; searched for
  other papers citing WP041/WP042 by title and found only one indirect mention,
  itself undated; two of Gaffney's own later papers that might cite these by
  date ("Keeping Land in Capital Theory" 2007, "The Role of Land Markets in
  Economic Crises" 2009) could not be text-searched reliably in this
  environment (PDF extraction failed on both — image/font-encoded streams).
  **Moved to BLOCKED**: circa-1993 remains the best-supported estimate; a
  genuinely dated citing source still hasn't been found across two separate
  passes. A cleaner PDF-text tool or direct access to Gaffney's own dated CV
  entries (if any exist offline) would be the next channel.

*(Book-copy items already tracked in `sources/verification-backlog.md`'s RETRYABLE
ledger and `sources/wanted-books.md` are not duplicated here to avoid a two-ledger
drift: `tideman-plassmann-losses-of-nations`, `widerquist-howard-pfd`,
`modelewska-value-capture-finance`, `lewis-building-cycles`,
`miller-dying-for-justice`, `cohen-coughlin-two-rate-taxation`,
`lapavitsas-financialization`, `miller-hoskins-college-town-lvt`,
`fernandez-milan-location-value-taxes`.)*

## How to work this queue

1. Regenerate ground truth: `python3 scripts/verification_queue.py` (rewrites this
   file's script-generated channel buckets — re-apply the DELIBERATE/RETRYABLE/BLOCKED
   classification by hand afterward, or diff against this version to see what's new).
2. Work RETRYABLE rows top-down: fetch → RESOLVE (cite what was verified, remove
   marker) or DOWNGRADE (weaken claim to what's verifiable, remove marker, note the
   downgrade) — never delete a marker silently.
3. A row that gets attempted and fails moves RETRYABLE → BLOCKED with a reason.
4. `sources/hermes-workorder.md` is the routed slice of this queue for Hermes's
   environment (unblocked web + Floyd's book library) — regenerate together.


## Unrouted markers (auto-generated)

*Machine-maintained by `scripts/verification_queue.py`. Everything above this
heading is hand-curated and is never rewritten. Rows here are markers no human
has routed yet; route one by moving it into a curated bucket above.*

<!-- AUTOGEN:START -->
*Regenerated 2026-08-07: 65 of 88 marker(s) not yet routed by hand (18 page(s) already curated above).*

### needs-book-copy (see sources/wanted-books.md) (1)

- `research/gaffney-mineral-leasing-tax-reform.md` — **VERIFY** exact publication year and venue not established this session — the essay reads as a book chapter or commissioned report for a Canadian audience, but no publisher or journal name survives in the text extracted

### needs-unblocked-web (proxy allowlist or manual fetch) (5)

- `concepts/land-value-capture.md` — **VERIFY** this characterization is drawn from the CaCHE project page's own description and consistent secondary summaries; the wiki could not retrieve the report's PDF directly (the Cardiff University ORCA repository copy sits beh
- `people/elizabeth-magie.md` — **VERIFY** exact publication date of the Realtor.com piece not confirmed — the page could not be directly fetched and this is drawn from a search-engine summary of its content.
- `places/australia.md` — **VERIFY** exact article URL/slug reconstructed via search rather than direct fetch — the page returned a fetch error, likely a paywall or bot block
- `research/gaffney-water-rent-taxation.md` — **VERIFY** OCR quality — the masongaffney.org PDF's embedded text layer is a low-quality legacy scan extraction; this page's quotations and figures are drawn from a fresh re-OCR (pdftoppm 250dpi + Tesseract 5.3.4) of the same PDF,
- `books/bird-the-land-trap.md` — **VERIFY** original study(ies) behind this range not independently identified this session — cited via Doucet's review, not read in Bird's primary text

### needs-new-source (research/forage task) (2)

- `concepts/dalt-depreciation-assisted-lvt.md` — **VERIFY** no antecedent academic source for this exact mechanism was found in a search beyond the NYC 1920s policy episode and Doucet's own piece — treat DALT as newly named/formalized in 2026 pending independent citation.
- `research/nef-modern-system-fair-rents.md` — **VERIFY** the wiki has not independently reviewed the broader empirical rent-control literature (including the specific Autor–Palmer–Pathak Cambridge, MA and Diamond–McQuade–Qian San Francisco quasi-experimental studies commonly c

### unclassified (T1 triage) (57)

- `concepts/dalt-depreciation-assisted-lvt.md` — **VERIFY** no independent economic modelling or evaluation of DALT located as of 2026-07-30.
- `concepts/land-value-capture.md` — **VERIFY** the wiki could not access the paper's full text (both the ScienceDirect publisher page and the authors' HAL preprint sit behind bot-protection this session); the summary above is built from the published abstract and con
- `concepts/land-value-capture.md` — **VERIFY** note above).
- `concepts/land-value-capture.md` — **VERIFY** note above).
- `concepts/spectrum-auctions.md` — **VERIFY** .)
- `people/silvio-gesell.md` — **VERIFY** full text of source 3 was not accessible — Wiley blocks automated retrieval even though Semantic Scholar records it as CC-BY open access; this page's account of Gesell's own doctrine (source 1) rests on standard secondar
- `people/sun-yat-sen.md` — **VERIFY** the wiki has not read this paper's body text; the relative weight the authors assign to Chinese versus Georgist roots cannot be assessed from the abstract alone
- `people/ted-gwartney.md` — **VERIFY** exact start year, 1975 vs. 1976, and parcel count, 1,350,000 vs. 1,500,000
- `places/british-columbia.md` — **VERIFY** full release not directly read
- `places/british-columbia.md` — **VERIFY** full Generation Squeeze article not directly read
- `places/canada.md` — **VERIFY** no evidence found this session of any Saskatchewan municipality or the province itself considering a full land-only tax; the CBC's 2026 coverage of a proposed AI data centre in the RM of Sherwood, near Regina, discusses
- `places/canada.md` — **VERIFY** full cultmtl.com article not directly read
- `places/canada.md` — **VERIFY** full article not directly read
- `places/canada.md` — **VERIFY** provincial primary-source page not directly read
- `places/ethiopia.md` — **VERIFY** the exact 2002 proclamation number appears inconsistently even within its own standard secondary source; not independently confirmed against Ethiopia's official gazette
- `places/germany.md` — **VERIFY** whether a Bundesverfassungsgericht complaint has actually been filed post-ruling was not confirmed this session — this pass found only that the door remains open, not that it has been used.
- `places/pennsylvania.md` — **VERIFY** the op-ed cites a Harvard-affiliated estimate of roughly 26,000 jobs having relocated out of Philadelphia because of the wage tax; this wiki has not independently verified that estimate, its authors, or the underlying pa
- `places/south-korea.md` — **VERIFY** Land+Freedom Institute's specific research outputs and any direct affiliation with Landforall.kr not confirmed this session
- `places/united-states.md` — **VERIFY** exact enactment date not confirmed this session
- `places/washington-state.md` — **VERIFY** whether Wilson's office has taken any further, post-inauguration action on this commitment — e.g., a formal city legislative-agenda item or public support for the Vibrant Cities Act — beyond the campaign-platform stateme
- `events/1886-nyc-mayoral-election.md` — **VERIFY** abstract only, full text not retrievable this session, Wiley blocks automated access
- `events/2026-state-lvt-enablement-wave.md` — **VERIFY** S1131's final 2026 disposition — this entry reflects its status as of the sources checked (amended to print 1131B, still in committee as of January 2026); if it advanced further before this page's last review, that shoul
- `benefits/resource-rent-capture-works.md` — **VERIFY** note; corroborating, not load-bearing).
- `narratives/the-great-land-robbery.md` — **VERIFY** full text not accessible this session
- `research/fiorentino-moogan-agglomeration.md` — **VERIFY** exact modelling approach, calibration, and any quantitative results once full text is accessible.
- `research/gaffney-benefits-farm-programs.md` — **VERIFY** volume/issue number
- `research/gaffney-benefits-farm-programs.md` — **VERIFY** .
- `research/gaffney-economics-of-abundance.md` — **VERIFY** exact publication year not given by the source; inferred from internal topical references only.
- `research/gaffney-extractive-resources-taxation.md` — **VERIFY** this page covers only Gaffney's editorial framing (Introduction and Conclusion); the volume's fourteen signed chapters by other contributors are not read or summarized here
- `research/gaffney-mineral-leasing-tax-reform.md` — **VERIFY** ed estimate from internal evidence; B13's factual claims (the 12.4% average tax rate, the 188-million-acre figure, the Getty reserve data) rest on Gaffney's own citations of 1980–82 trade press (Business Week, Los Angele
- `research/gaffney-mineral-leasing-tax-reform.md` — **VERIFY** .
- `research/gaffney-nonpoint-pollution.md` — **VERIFY** ), Vol.
- `research/gaffney-nonpoint-pollution.md` — **VERIFY** ).
- `research/gaffney-nonpoint-pollution.md` — **VERIFY** ), Vol.
- `research/gaffney-noyes-income-stimulating-property-tax.md` — **VERIFY** .)
- `research/gaffney-noyes-income-stimulating-property-tax.md` — **VERIFY** exact cell values in Tables 8:III and 8:IV
- `research/gaffney-water-rent-taxation.md` — **VERIFY** the "Chinatown Syndrome" attribution and the specific insider-prepurchase claim rest on Gaffney's own summary in both pieces; this page does not independently verify the Owens Valley land-purchase history against primary
- `research/gaffney-water-rent-taxation.md` — **VERIFY** H22's named-speculator and political-history claims are drawn from Gaffney's own citations to contemporary press and secondary sources (Fulton 1996; Worster 1985; Kirkendall 1964, 1966); this page relays them as Gaffney'
- `research/gaffney-water-rent-taxation.md` — **VERIFY** flag above — its text was recovered via fresh OCR of a poor legacy scan rather than a native text layer, so exact figures should be treated as approximate.
- `research/gaffney-water-rent-taxation.md` — **VERIFY** note above.
- `research/kakumu-kenya-site-value-tax.md` — **VERIFY** .
- `research/kakumu-kenya-site-value-tax.md` — **VERIFY** full text unread.
- `research/loehr-george-gesell-odd-couple.md` — **VERIFY** .
- `research/loehr-george-gesell-odd-couple.md` — **VERIFY** the wiki has not read this paper's body text.
- `research/obeng-odoom-rodney-legacy.md` — **VERIFY** .
- `research/obeng-odoom-rodney-legacy.md` — **VERIFY** the wiki has not read this paper's body text.
- `research/schlaepfer-swiss-resource-rents.md` — **VERIFY** the wiki has not read the paper's full body text — figures below come from the verified abstract plus a corroborating open-access companion paper, not from the complete methods/results sections.
- `research/schlaepfer-swiss-resource-rents.md` — **VERIFY** the CHF 298bn/42%-of-GDP figure in the framework paper and the CHF 159bn/~20%-of-GDP figure in the companion paper are not directly comparable on their face — they likely reflect a narrower category set or refined data i
- `research/schlaepfer-swiss-resource-rents.md` — **VERIFY** full methods and data-source detail — particularly how "resource gain" is separated from ordinary land-price appreciation, and how the external-cost figures underlying "resource externality" were sourced — should be conf
- `research/spring-ragain-lvt-dynamics.md` — **VERIFY** peer-review status — this is a preprint only; no journal publication, referee reports, or citations from established urban-economics scholars were found at time of writing.
- `research/spring-ragain-lvt-dynamics.md` — **VERIFY** author background
- `research/spring-ragain-lvt-dynamics.md` — **VERIFY** the paper is not yet peer-reviewed; its conclusions have not been independently checked by other economists at time of writing.
- `research/welsh-lvt-valuation-testing.md` — **VERIFY** Two pages already on this wiki — research/tpa-what-would-lvt-do and people/andy-burnham — cite this Welsh Government programme for the claim that it found "no [assessment] methodology...
- `research/xu-huang-li-china-hcrs-george.md` — **VERIFY** .
- `research/xu-huang-li-china-hcrs-george.md` — **VERIFY** full text unread — the depth of the analogy, and any qualifications the authors attach to it, cannot be assessed from the abstract.
- `research/yang-split-rate-spillover-employment.md` — **VERIFY** confirm whether the published 2024 version updates the 1980–2010 sample period or coefficient magnitudes reported in the 2015 working paper.
- `books/bird-the-land-trap.md` — **VERIFY** absence of Economist/WSJ reviews reflects a search gap, not necessarily their non-existence
<!-- AUTOGEN:END -->
