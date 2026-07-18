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

This wave resolved **5** (see `sources/verification-backlog.md` for the dated entry) —
down from 30 at the start of this pass. Markers are the wiki's anti-fabrication
firewall (EDITORIAL rule 2). **Never delete a marker without either resolving the
claim (cite what was verified) or downgrading it (weaken the claim to what's
verifiable, note the downgrade).**

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

## RETRYABLE (6) — candidates for the next wave

- `research/august-rental-financialization.md` — cross-check the Herongate Tenants
  mirror page-by-page against the official Taylor & Francis PDF (DOI-resolved).
  Approach: Unpaywall API for a green-OA copy, or SOAS/author-repository mirror
  (same channel that worked for other T&F-blocked papers this session, e.g.
  Lapavitsas — worth retrying periodically as Cloudflare challenges are session-
  dependent).
- `research/gaffney-alaska-oil-leasing.md` (L322) — publication/circulation history of
  the 1977 report beyond delivery to the Alaska Legislature/DNR. Approach: WorldCat
  record, Alaska State Library catalog, or a citing-paper search (Google Scholar) for
  contemporaneous reception.
- `research/gaffney-forest-taxation.md` (L205) — Clawson's $42-billion National Forest
  valuation and 1974 cash-receipts/outlay figures. Approach: search for Marion
  Clawson's own 1970s RFF (Resources for the Future) publications/working papers
  directly (attempted this session via general web search with no hit; RFF's own
  archive or a WorldCat/library search for the specific Clawson report is the next
  step, not yet tried).
- `research/gaffney-land-distinctive-factor.md` (L112) — Gaffney's polemical framing of
  Howard Jarvis's "services to property, not services to people" slogan. Approach:
  Jarvis's own book (*I'm Mad As Hell*, 1979) or contemporaneous Prop. 13 campaign
  literature — a light web search this session found no verbatim primary source;
  needs a book/archival pass, not another web search.
- `research/gaffney-soil-depletion-land-rent.md` (L173) — independent citation
  count/reception history for the paper. Approach: Google Scholar citation count,
  RePEc/IDEAS citation graph.
- `research/gaffney-land-market-distortions.md` (L41) — exact publication date of
  WP041/WP042. **Attempted this session** (masongaffney.org's own publications and
  workpapers listings show no date for either entry; Wayback Machine's earliest
  capture is 2024-07-13, which is an archive date, not an authorship date) — kept
  RETRYABLE rather than BLOCKED because a dated citing source (e.g., a paper citing
  WP041/042 with a year) hasn't been searched for yet.

## BLOCKED (3) — attempted, not resolvable this wave

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
