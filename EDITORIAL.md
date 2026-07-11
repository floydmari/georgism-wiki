# EDITORIAL.md — The Wiki Constitution

## §0 The Mission (canonical statement — quoted by every executor prompt)

> We are building **the definitive, honest reference on Geoism — the economic system
> in which economic rents of every kind are captured for public good** — the source of
> truth behind progress.org/wiki. Georgism and the land value tax are its core and its
> historical root, and land remains the largest, best-evidenced case; but the scope is
> ALL rents and their capture instruments: land and location (LVT), natural resources
> (royalties, severance taxes, sovereign funds), the atmosphere and ecology (carbon
> pricing and dividends), spectrum and orbits (auctions), road space (congestion
> pricing), monopoly and regulatory privilege, finance and credit, platforms and data,
> intellectual-property privilege. A reader starting from any question — *does a land
> tax get passed on to renters? are modern corporate profits really rents? what
> happened when Norway captured its oil rent?* — should find the strongest available
> evidence, the strongest counterargument, and the primary sources, all cited. The wiki
> grows by **finding** the literature, **reading and mining** every source it touches,
> **synthesizing** what the sources collectively show into its argument pages, and
> **verifying** relentlessly — every claim we couldn't confirm says so, visibly, on the
> page.
>
> **The rent gradient (scope-expansion honesty rule, Floyd 2026-07-06):** land is the
> *clean* case — fixed supply, no incentive story to damage, a century of incidence
> evidence. Every step away from land is more contested: resource rents mix with
> extraction incentives; "monopoly rents" may be efficiency returns
> (the Autor/Crouzet–Eberly disputes the wiki already carries); innovation profits are
> largely *quasi-rents that ARE the incentive* — taxing them is not free the way taxing
> location is (the Schumpeterian objection, to be steelmanned). Pages must carry this
> gradient explicitly: never let the airtight land case lend its certainty to the
> contested frontier, and never flatten "is it a rent?" into an assumption.

This file is the single source of editorial truth for that mission. Every model and
human editing this repo must follow it. It is written to be **self-contained**: a model
with only this file, repo read access, and web search can produce compliant work.

The wiki is **persuasive because it is accurate, well-sourced, and intellectually fair** —
never because it asserts Georgist conclusions. A reader who disagrees should be able to see
that their strongest objection has been understood, sourced, and answered.

---

## 1. Golden rules (never break these)

1. **GitHub is the master record.** All work commits and pushes to the repo *first*.
   Publishing to Ghost happens *only afterward*, and *only* via `scripts/sync_to_ghost.py`.
2. **Never fabricate.** Never invent a source, quotation, author, date, page number, DOI,
   or URL. If you cannot find a source, write `[CITATION NEEDED: <what is needed>]`.
   If a claim seems too strong, soften it or mark `[VERIFY: <concern>]`.
3. **Never delete an article.** If one is wrong, open an issue or mark it for review.
4. **Neutral, encyclopedic tone (Wikipedia NPOV).** Report arguments; do not make them.
5. **≤ 50 words** quoted from any single copyrighted work. Prefer paraphrase + citation.
6. **Free/legal sources only** for links (SSRN, NBER, Lincoln Institute, IMF/OECD/World Bank,
   masongaffney.org, author pages, university repositories, Internet Archive). Note paywalls.
7. **Intra-wiki links are navigation, not evidence.** A claim's citation must be an external
   source; the linked wiki page must itself carry that citation.

---

## 2. Claim taxonomy — classify every substantive sentence

Review each page sentence by sentence. Classify each claim and cite it accordingly.

| Type | Examples | Sourcing requirement |
|------|----------|----------------------|
| **A. Factual / historical** | dates, people, events, policy changes, who coined a term, what a report concluded | A reliable source. |
| **B. Empirical** | effects, magnitudes, tax incidence, housing supply, productivity, historical results | The *best available* empirical source (peer-reviewed paper, official dataset, gov report, canonical book). Do not present as settled unless the evidence is. |
| **C. Theoretical** | ATCOR, EBCOR, deadweight loss, Ricardian rent, LVT neutrality, capitalization | Primary theoretical source (+ secondary explainer where useful). Distinguish "the theorem states" vs "proponents argue" vs "standard theory holds" vs "critics dispute" vs "evidence suggests". |
| **D. Interpretive / argumentative** | "the strongest argument for LVT is…", "this objection confuses acreage with value" | Cite a source that makes the argument, **or** rephrase explicitly as analysis. Never present interpretation as fact. |
| **E. Objection** | (objection pages) the case against | Cite the **strongest** available version — serious academic critique, opposing policy paper, a real implementation failure, a respected economist's argument. No strawmen. |
| **F. Definition** | "LVT means…", "ATCOR stands for…", "economic rent is…" | Canonical/primary source: original text, textbook, encyclopedia, or authoritative institution. |

---

## 3. Citations

- **Claim-level, not just page-level.** Attach the citation to the specific claim. A bottom
  "Sources: Gaffney, Harrison" list is *not* sufficient.
- **Full reference format:** author or institution · title · year · publisher/venue ·
  direct stable URL (DOI / SSRN / JSTOR / gov / repository / Internet Archive) ·
  page/chapter/section · access date where useful. Avoid generic homepages when a specific
  document exists.
- **Source quotations** — include a short (≤50-word) quote where wording matters: theoretical
  claims, canonical definitions, contested claims, objections, statements attributed to a
  named thinker. **Public-domain exemption (Floyd, 2026-07-06):** the 50-word cap is a
  *copyright* rule, not a style rule — it does not apply to public-domain works (see §3b).
  Style still applies: pages quote what serves the reader; full texts live on dedicated
  primary-text pages, not inside argument pages.
- **Evidence ordering (Floyd, 2026-07-06):** wherever a page lists supporting research —
  an outcome's `supported_by` frontmatter, an "Evidence" section, a concept's research
  list — order by **evidential weight, descending**: (1) top-journal peer-reviewed and
  quasi-experimental designs, (2) other peer-reviewed work, (3) official/institutional
  reports (IMF, OECD, government), (4) working papers, (5) practitioner and advocacy
  sources. Within a class, more prominent/more-cited first. The reader who stops after the
  first item should have met the strongest evidence, not the first-drafted. (Counter-evidence
  in `challenged_by` follows the same rule — strongest challenge first.)
- **Source-quality hierarchy** (prefer the highest available):
  1. Primary source / statute / official report / original paper / canonical book / dataset
  2. Peer-reviewed academic source
  3. Government, university, or established research institute
  4. Well-regarded policy institute or expert publication
  5. Serious journalistic source
  6. Advocacy source — only to represent that advocate's own position
  7. Wiki page or blog — navigation only, never primary evidence
- **Every source used must have a row in `sources/registry.csv`** (add one if missing).
  `registry.csv` is **sources only** — external works, identified by
  Title+Author+Year+URL, with the `Wiki Page` column a "where used" annotation
  (never a wiki self-reference). The wiki's own pages and their backlink counts
  live in `sources/wiki-inventory.csv`. Public-domain `texts/` pages ARE sources
  and need a `registry.csv` row with their external provenance URL. See
  `sources/README.md` for the full contract and the regenerate-from-sources
  rationale.

### §3b Public-domain full texts (Floyd, 2026-07-06)

Works past copyright may be held **in full** on the wiki — old debates, speeches,
pamphlets, and books are exactly the primary record a definitive reference should carry,
not merely summarize. Rules:

- **Eligibility test (conservative):** published **before 1931** (US 95-year rule as of
  2026) AND, for non-US authors, author dead ≥70 years — or otherwise clearly
  public domain. When the two regimes disagree (e.g., Churchill's 1909 speeches: PD in the
  US, not yet in the UK), note the jurisdiction split on the page and prefer works clear
  in both.
- **Where they live** (separation from `books/` ratified by Floyd, 2026-07-06: `books/` is a
  page ABOUT a work we may not reproduce — copyright machinery applies; `texts/` IS the work —
  the quote cap is exempt, and on progress.org the two tags can carry distinct templates/styling:
  a browsable shelf of digested literature vs a reading room of original documents):
  short-to-medium documents (speeches, debates, pamphlets, essays,
  letters — roughly ≤25k words) become **`texts/` pages** (`category: texts`,
  `public_domain: true`, provenance/edition stated, ≥2 inbound links like any page).
  Full BOOKS stay summarized in `books/` with the complete text stored at
  `sources/publicdomain/<slug>.md` (repo-hosted and linked from the book page — GitHub
  renders it; it is not itself a wiki page).
- **Provenance still required:** name the edition/transcription source (Gutenberg,
  Internet Archive, HathiTrust, cooperative-individualism.org). Public domain waives the
  quote cap, not the accuracy rules — transcriptions get spot-checked like any source.
- **Priority acquisitions:** the era this wiki covers is uncommonly rich in PD material —
  George's complete works, Ricardo, Mill, Paine's *Agrarian Justice*, the 1890 Saratoga
  debate proceedings, Johnson's 1914 critique, Post's *Deportations Delirium* (1923),
  the People's Budget speeches. Route acquisition through the Hermes work order (its
  environment fetches freely); each delivery is a `texts/` page or `sources/publicdomain/`
  file plus the usual discovery pass.

### Scan Depth policy — Tier sets the target
`Scan Depth` records how much of a source's extractable value is actually in the wiki, so it must
track **Tier** and **source size**, not just whether the source was ever cited:

| Tier | Target depth |
|------|--------------|
| Core | **Heavy** — systematically mined; findings woven into multiple pages |
| Important | **Medium minimum; Heavy for books/major reports** |
| Supplementary | Light acceptable |

- **Light** = one or two points pulled incidentally (a quote, a single finding). Fine for a
  short article or a two-paragraph remark (a Light scan of Friedman's 1978 symposium comment is
  effectively complete); inadequate for a book.
- Any registry row with **Tier ≥ Important and Scan Depth = Light** (where the source is more than
  a few pages) is an open task: add a `[DEEPEN-SCAN tier:T2]` item to `BACKLOG.md` to mine it and,
  where warranted, give it a dedicated `research/` page.

## 4. Claim-strength language

Match wording to evidence. Prefer: "According to…", "Gaffney argues…", "The theorem states…",
"Empirical evidence from X suggests…", "One criticism is…", "This remains contested…",
"Under standard assumptions…".

**Banned unless the cited source justifies that strength:** `proves`, `always`, `all taxes`,
`the only`, `there is no evidence`, `clearly`, `undeniable`, `everyone agrees`. `lint_wiki.py`
flags these for review.

---

## 5. Frontmatter schema (YAML)

**All pages:** `title` (quoted), `category` (must equal the folder), `tags` (list),
`stub` (bool), `excerpt` (≤ 300 chars). Add `last_reviewed: YYYY-MM-DD` when you revise a page.

**Category-specific:**
- `research/`: `authors` (list), `year`, `tier` (`Core|Important|Supplementary`), `source_url`,
  optional `supports_outcomes` (list of outcome slugs).
- `problems/` and `benefits/` (the claim pages — split from the old `outcomes/`,
  Floyd 2026-07-10; see §5b): `evidence_strength` (string), `claim_type` (`problem` in
  `problems/`, `benefit` in `benefits/` — REQUIRED, must match folder, enforced by lint),
  `supported_by` (list of research slugs), optional `challenged_by`, `related_people`,
  `related_places`. The research-side field name stays `supports_outcomes` for continuity.
- `objections/`: `status` (short assessment string).
- `narratives/`: `narrative_type` (`moral|economic|practical|environmental|historical`),
  `supported_by`, `related_people`, `related_places`.
- `people/`: optional `born`, `died`. `places/`, `events/`, `organizations/`: as existing.
- `texts/` (added 2026-07-06, Floyd — public-domain primary texts, EDITORIAL §3b):
  `authors` (list), `year`, `public_domain: true` (REQUIRED — activates the quote-cap
  exemption in lint), `provenance` (edition/transcription source), plus the universal
  fields. Body = a short editorial headnote (what it is, why it matters, PD status),
  then the full text.
- `books/` (added 2026-07-06, Floyd): `authors` (list), `year`, `tier`, optional `publisher`,
  `isbn`, `page_count`, `scanned_by` (e.g. `hermes`), `scan_date`. The universal fields
  (`title`/`category`/`tags`/`stub`/`excerpt`) are REQUIRED here like everywhere — book pages
  arriving from Hermes's pipeline with its native schema get normalized to this at T1 merge
  review, not rejected.

**Bidirectional linking is enforced by lint:** if outcome X lists `supported_by: [r]`, research
`r` should list `supports_outcomes: [x]`. Same for `challenged_by` / `related_*`.

### §5b Problems and benefits (Floyd, 2026-07-10 — see PLAN-problems-and-benefits.md)

The old `outcomes/` category is split into two directories (Phase 3 executed 2026-07-10,
on Floyd's sign-off). Every claim page is one of two kinds, by directory and `claim_type`:

- **`problem`** — the diagnosis: an empirical claim about the world that geoism identifies
  (e.g. "the capital-share rise is land", "public investment capitalizes into land values").
- **`benefit`** — the prescription's measured effects: an empirical claim about what geoist
  policy delivers (e.g. "split-rate taxation increases construction").

Reader-facing indexes: `/wiki/problems/` and `/wiki/benefits/` group the claims with
evidence grades — **keep both indexes current when adding, retitling, or regrading a
claim page.**

**Acceptance rule per page:** ≥ 2 independent big-name/peer-reviewed anchors, fetched and
claim-level verified, before a page leaves stub status; `evidence_strength` graded
(Strong / Moderate / Emerging / Contested / Theoretical); a counter-evidence section is
mandatory. **Advocate-readability standard:** first screen = the claim + the 3 strongest
citations + one honest-limits line — a reader should be able to quote the page in an
argument in 30 seconds and not get burned. Rent-gradient rules apply unchanged: land-core
claims may be stated strongly when evidence is strong; frontier claims stay attributed.

(Phase 3 — the directory split — was executed 2026-07-10 after Floyd's sign-off. New
claim pages go directly into `problems/` or `benefits/`; there is no `outcomes/`.)

---

## 6. Page templates

Every page ends with `## See Also` (3+ cross-links) and `## Sources` (annotated — see below).

### Standard article (concepts, people, places, events, organizations, research)
`## Overview/Definition` → body sections → `## See Also` → `## Sources`.

### Objection pages — use this structure
```
## The Objection        (the strongest version, cited to the best opposing source)
## Why People Worry About This   (the factual/historical/administrative/economic basis)
## The Response         (cited evidence and theory — do not dismiss without evidence)
## Limits and Caveats   (where the objection is partly valid: transition effects,
                         liquidity, poor assessment, short-run incidence, special sectors)
## Net Assessment       (balanced conclusion reflecting the evidence)
## See Also
## Sources
```
(The existing 8 objection pages use The Objection / The Response / Net Assessment / Sources —
that is the enforced minimum; add the fuller structure when revising.)

### Theory pages (ATCOR, EBCOR, Ricardian rent, deadweight loss, LVT neutrality, HGT)
Identify the primary source / origin → state the concept **as a claim, not fact** → state the
assumptions under which it holds → cite supporting theoretical work → cite critics/limits →
distinguish theoretical prediction from empirical confirmation. Use "proponents argue" /
"under this model" for contested theorems.

### Narrative pages (`narratives/`)
Core claim (1–2 sentences) · Who promotes it (→ `people/`) · Research that supports it
(→ `problems/`/`benefits/`, `research/`) · Research that challenges it or is missing · Counter-arguments &
Georgist responses (→ `objections/`) · Historical examples (→ `places/`, `events/`) ·
How to deploy it (framing tips, audience guidance).

### Book pages (`books/` — added 2026-07-06)
The wiki's citable reference for a book, especially one held privately (Floyd's library) whose
file can NEVER be committed. Structure: `## Bibliographic Information` → `## Core Thesis` →
structure/argument walk-through → key claims with **page-cited quotes ≤50 words** → limits and
reception → `## See Also` → `## Sources`. A book page is a *summary and index*, not a
reproduction: no long excerpts, no chapter-length paraphrase. Wiki pages citing the book link
to its `books/` page so page-level cites have an on-wiki anchor. Every book page ships with its
discovery report (see LOOP-COMPREHENSIVENESS / inbox README): the papers, people, events,
places, concepts, organizations, and further books it surfaces.

### Stub standard (the discovery unit)
A **stub** is a valid minimal page created the moment a loop discovers a warranted topic, in ANY
category (concepts, people, places, organizations, objections, events, outcomes, narratives,
books):
full frontmatter with `stub: true`, a 2-4 sentence sourced definition/overview, >=2 wiki links
out, >=1 inbound link wired from the discovering page, and a Sources section citing at least the
source(s) that justified it. Stubs are honest scaffolding, not embarrassments — they carry the
`stub` tag on Ghost and appear in the lint STUBS gauge until backfilled via
`tasks/backfill-page-task.md`. Never create a stub without at least one real citation.

### Annotated Sources section
Each reference gets a one-line "used for" note:
```
## Sources
1. Mason Gaffney, "The Hidden Taxable Capacity of Land," 2009. <url> — used for the ATCOR
   formulation and the claim that taxes on labour/capital reduce rent.
2. Dye & England, *Assessing the Theory and Practice of LVT*, Lincoln Institute, 2010. <url>
   — used for practical design issues and agricultural incidence.
```

---

## 7. Per-page revision output (the `[CITE]` deliverable)

When you run a citation/evidence pass on a page, produce a sidecar report
`reports/<slug>.cite.md` (git-ignored is fine) or the PR description containing:
- **A.** revised article text with claim-level citations
- **B.** complete, linked Sources section
- **C.** claims that still need citations (`[CITATION NEEDED]` list)
- **D.** claims softened, qualified, or reframed (and why)
- **E.** stronger sources to find later (esp. empirical claims and opposing views)

---

## 8. Publishing (three Ghost gotchas — handled by the sync script)

`scripts/sync_to_ghost.py` bakes in all three; never hand-roll Admin API calls:
1. `?source=html` on create/update — or Ghost drops the body.
2. `custom_template: "custom-wiki-entry"` on every post — or it renders as a plain article.
3. Primary tag `wiki` (first) + a category tag (`wiki-concepts`, `wiki-people`, `wiki-places`,
   `wiki-events`, `wiki-outcomes`, `wiki-research`, `wiki-organizations`, `wiki-objections`,
   `wiki-narratives`).

**Preview before publishing:** `python3 scripts/build_preview.py && python3 -m http.server -d preview`
renders the whole branch locally with working cross-links and badges — the human review gate.

Commit-trailer and branch conventions are **runner-configurable** (each runner sets its own),
so this file does not hard-code them.

---

## 9. Model tiers (see `LOOP.md`)

Tasks in `BACKLOG.md` are tagged `tier:T1|T2|T3`. **T1 (frontier)** does judgment: evidence-
strength calibration, objection-steelmanning, narrative design, flagship articles, final review.
**T2 (mid)** drafts articles and citations. **T3 (bulk)** scans sources, wires cross-links,
backfills frontmatter, runs/fixes lint. Cheap tiers generate; T1 reviews and is the publish gate.
