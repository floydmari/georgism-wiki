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
this pass.

**Update 2026-08-12 (daily loop wave).** Live count **31 → 29**. Two markers resolved
against primary sources read this run, both from the `needs-new-source` bucket:
`research/nef-modern-system-fair-rents.md` (the skeptical rent-control literature —
Autor–Palmer–Pathak on Cambridge and Diamond–McQuade–Qian on San Francisco, both read
in full from free NBER/Stanford PDFs) and `people/henry-george-jr.md` (the December 2,
1897 marriage, resolved against three contemporary wire-service reports via LOC
*Chronicling America*, which also **corrected** the wedding's location from Orleans
Parish to Chicago). No marker was deleted without a cited resolution.

Markers are the wiki's anti-fabrication firewall (EDITORIAL rule 2).
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

## DELIBERATE-SCOPED (18) — stay in place, no action needed

*Routed 2026-08-11 (T1 triage of the unclassified channel) — monitoring-type markers
awaiting a future event or a channel this environment cannot work; revisit notes per row:*

- `places/canada.md` (L58) — negative result honestly recorded: no evidence of any
  Saskatchewan land-only-tax consideration after two search passes (2026-08-10).
  Nothing to fetch; revisit only if new Saskatchewan coverage appears in the queue.
- `places/germany.md` (L28) — calendar-gated: plaintiff associations announced intent
  to file a Verfassungsbeschwerde against the Baden-Württemberg law, but no BVerfG
  case number or filing date exists yet (checked 2026-08-10). Revisit ~quarterly.
- `places/washington-state.md` (L32) — calendar-gated: whether Mayor Wilson's office
  takes post-inauguration action on the LVT commitment (legislative agenda, Vibrant
  Cities Act support). Revisit on Seattle news or ~2026-10.
- `places/south-korea.md` (L28) — needs direct inquiry or Korean-language archival
  search to pin the Land+Freedom Institute ↔ Landforall.kr relationship; not
  resolvable from English-language web. Leave until a Korean-capable channel exists.
- `concepts/dalt-depreciation-assisted-lvt.md` (L25) — documents an absence: no
  independent economic modelling of DALT exists yet (mechanism newly named in 2026).
  The marker is the honest state of the literature; revisit ~2027 or on new citation.

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
*Regenerated 2026-08-12: 14 of 29 marker(s) not yet routed by hand (25 page(s) already curated above).*

### needs-unblocked-web (proxy allowlist or manual fetch) (14)

- `people/elizabeth-magie.md` — **VERIFY** exact publication date of the Realtor.com piece not confirmed — the page could not be directly fetched and this is drawn from a search-engine summary of its content.
- `people/silvio-gesell.md` — **VERIFY** this page's account of Gesell's own doctrine (source 1, Die natürliche Wirtschaftsordnung) still rests on standard secondary reference knowledge, not a fresh read of Gesell's primary text or of Loehr's full body text thi
- `people/sun-yat-sen.md` — **VERIFY** the wiki still has not read this paper's body text — direct fetch of the Wiley article page returned HTTP 403/a bot-CAPTCHA wall via three independent methods this session (direct fetch, curl with a browser user-agent, a
- `places/australia.md` — **VERIFY** exact article URL/slug reconstructed via search rather than direct fetch — the page returned a fetch error, likely a paywall or bot block
- `places/united-states.md` — **VERIFY** needs-unblocked-web — exact enactment date not confirmed; the 2012 KCMO report PDF returned 403 (manual fetch needed). Attempted 2026-08-10: the Kansas City Clerk's legislation portal (clerk.kcmo.gov) surfaces only curre
- `events/1886-nyc-mayoral-election.md` — **VERIFY** needs-unblocked-web — abstract only; full text not retrievable, Wiley blocked automated access across retrieval methods
- `narratives/the-great-land-robbery.md` — **VERIFY** full text not accessible this session — needs-unblocked-web
- `research/fiorentino-moogan-agglomeration.md` — **VERIFY** exact modelling approach, calibration, and any quantitative results once full text is accessible — needs-unblocked-web.
- `research/kakumu-kenya-site-value-tax.md` — **VERIFY** full text unread. Re-confirmed closed on 2026-08-10 via Unpaywall (isoa: false), a direct SAGE fetch (paywalled), and the author's own Academia.edu profile (access error, no self-archived copy found).
- `research/loehr-george-gesell-odd-couple.md` — **VERIFY** needs-unblocked-web — the wiki has not read this paper's body text; full text remains genuinely CC-BY licensed but mechanically unreachable (Wiley bot-detection); four retrieval methods failed identically across two revi
- `research/obeng-odoom-rodney-legacy.md` — **VERIFY** needs-unblocked-web — the wiki has not read this paper's body text; full text remains genuinely CC-BY licensed but mechanically unreachable (Wiley bot-detection); four retrieval methods failed identically across two revi
- `research/xu-huang-li-china-hcrs-george.md` — **VERIFY** full text unread — Wiley's bot-detection has now blocked four independent retrieval methods across two review passes (2026-07-26, 2026-08-10); the depth of the analogy, and any qualifications the authors attach to it, ca
- `research/yang-split-rate-spillover-employment.md` — **VERIFY** confirm whether the published 2024 version updates the 1980–2010 sample period or coefficient magnitudes reported in the 2015 working paper — needs-unblocked-web, a proxy or institutional-access channel this environment
- `books/bird-the-land-trap.md` — **VERIFY** original study(ies) behind this range not independently identified this session — cited via Doucet's review, not read in Bird's primary text
<!-- AUTOGEN:END -->
