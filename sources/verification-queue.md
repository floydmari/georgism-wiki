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

## RETRYABLE (0) — none open; the prior 6 were worked this pass

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
