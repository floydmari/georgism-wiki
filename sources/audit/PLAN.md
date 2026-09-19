# Wiki irregularity audit — plan and rules (started 2026-09-19, Floyd's ask)

Floyd's report: (1) "strange wiki generation artifacts on some of the pages, like mentions of
missing verifications"; (2) "questionable choice of referencing some of the wiki people on
concepts" — Akhil Patel cited early on a page as supporting an idea, as if notable. Rule from
Floyd: if a person is referenced as social proof to bolster an idea, it should be someone
prominent — a famous PhD, or someone on Adam Smith's level.

Method (Floyd's spec): cheap models find, fable assesses and plans, opus implements; loop until done.

## Taxonomy

- **A1 — process narration in reader-facing prose.** "this session / this pass / this
  environment", fetch/403/Cloudflare/curl/WebFetch/r.jina.ai, "reconstructed from a WebSearch",
  "as of this writing", "not independently retrieved this session", dated notes of the wiki's
  own retrieval attempts, bracketed editor asides.
- **A2 — claim-grade codes in prose.** "(B-claim)", "A-claim", "C/D-claim" outside Sources.
- **A3 — leaked internal markers.** `[VERIFY: …]`, `[VERIFY: wiki page?]`, `[CITATION NEEDED]`,
  `[CITE]`, "needs-unblocked-web", `[Attempted …]` logs.
- **A4 — process narration inside Sources annotations.** Access and grade notes belong there,
  but phrased impersonally and dated: not "fetch blocked (403) to this session 2026-08-30" but
  "full text not accessible at last review (2026-08-30); summary rests on the abstract".
- **B1 — non-notable person used as support.** A Tier 2/3 name (below) presented as
  corroboration for an idea — "as X argues", "X shows", "according to X" — in the lead or
  body of a concept / objection / benefit / problem / narrative / theory page, or listed
  alongside Tier 1 names as an equal.
- **B2 — "discovery source" given authority weight.** The source through which the wiki
  first found a topic presented as if it were the authority on it.
- **C — other.** Anything a scanner notices that reads as machine-generated rather than
  encyclopedic: duplicated sentences, half-finished sections, template text, "this wiki"
  self-reference in the lead, editor-facing headings.

## Resolution rules

**A1/A2/A3 (prose):** The *status of a claim* stays visible to the reader in encyclopedic
terms — "reported only in X", "abstract-level summary", "the author's own figure, not
independently tested", "unverified". The *history of the wiki's attempts* does not: no
sessions, fetchers, HTTP codes, dates of attempts, or grade codes. Bracketed `[VERIFY …]`
markers are resolved (link/cite/soften) or removed; `[VERIFY: wiki page?]` is resolved by
linking if the page exists, else dropping the bracket. Never delete the underlying claim
without replacing it with a correctly-hedged sentence; never fabricate a citation to close a
marker (EDITORIAL rule 2) — if a claim cannot stand without the marker, soften it to what the
cited source supports.

**A4 (Sources):** keep the grade code and the access status; rewrite in the impersonal past
with a date ("not accessible at last review, 2026-09-06"); delete tool names and retry logs.

**B1/B2 (attribution):**
- *Tier 1 — may be cited as support anywhere:* canonical thinkers (George, Smith, Ricardo,
  Mill, Marshall, Pigou, Vickrey, Stiglitz, Friedman, Samuelson, Solow, Tobin, Ostrom, Nobel
  laureates); established academics with a peer-reviewed body of work on the topic (Gaffney,
  Tideman, Oates, Schwab, Plassmann, Foldvary in his academic work, Glaeser, Piketty, Zucman,
  Saez, Ryan-Collins, Christophers as an academic); official and standing bodies (OECD, IMF,
  World Bank, ONS, IFS/Mirrlees, Lincoln Institute, IAAO, central banks, statutory reviews);
  canonical historical figures for their own acts and words.
- *Tier 2 — may be cited as the ORIGIN or PROPONENT of a term or claim, with status stated
  ("the practitioner-author Akhil Patel's name for…"), never as evidence the claim is right:*
  practitioner-authors, investors, advocates, journalists, bloggers, think-tank and movement
  staff, Substack writers (Akhil Patel, Phil Anderson, Fred Harrison in his popular books,
  Lars Doucet, Common Wealth Canada, HGF authors, Progress and Poverty newsletter).
- *Tier 3 — only as the subject of a page or for their own actions and statements:*
  politicians on policy, business people, op-ed writers, anonymous or pseudonymous sources.
- Fix: rephrase to state status and role; move Tier 2/3 support-citations out of the lead into
  a "Who promotes it" / "Current debate" position; where a Tier 1 source for the same point
  exists on the wiki, substitute it; where none exists, hedge the sentence to "proponents
  argue" and keep the Tier 2 source only as the origin.

## Loop

1. `scripts/audit_wiki.py` → `sources/audit/deterministic-<date>.json` (A1–A4 spans).
2. Haiku fan-out (25 pages/agent) → `sources/audit/haiku/batch-NN.jsonl` (all classes; B
   requires judgement). Flag only.
3. Fable: sample precision, consolidate → `sources/audit/worklist-<date>.json`; amend
   EDITORIAL.md (§4b prose-vs-sources; §4c attribution and notability).
4. Opus fixers per class/batch with rule sheet; lint 0 errors; commit per batch with file lists.
5. Re-run 1 (must be zero for A1–A3 body hits) and a haiku re-check on touched pages; repeat.
6. LOOPLOG entry, merge to main, Ghost-sync touched pages, spot-check.
