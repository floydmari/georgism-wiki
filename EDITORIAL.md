# EDITORIAL.md — The Wiki Constitution

This is the single source of editorial truth for the Georgism wiki. Every model and
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
  named thinker.
- **Source-quality hierarchy** (prefer the highest available):
  1. Primary source / statute / official report / original paper / canonical book / dataset
  2. Peer-reviewed academic source
  3. Government, university, or established research institute
  4. Well-regarded policy institute or expert publication
  5. Serious journalistic source
  6. Advocacy source — only to represent that advocate's own position
  7. Wiki page or blog — navigation only, never primary evidence
- **Every source used must have a row in `sources/registry.csv`** (add one if missing).

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
- `outcomes/`: `evidence_strength` (string), `supported_by` (list of research slugs),
  optional `challenged_by` (list of research slugs), `related_people`, `related_places`.
- `objections/`: `status` (short assessment string).
- `narratives/`: `narrative_type` (`moral|economic|practical|environmental|historical`),
  `supported_by`, `related_people`, `related_places`.
- `people/`: optional `born`, `died`. `places/`, `events/`, `organizations/`: as existing.

**Bidirectional linking is enforced by lint:** if outcome X lists `supported_by: [r]`, research
`r` should list `supports_outcomes: [x]`. Same for `challenged_by` / `related_*`.

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
(→ `outcomes/`, `research/`) · Research that challenges it or is missing · Counter-arguments &
Georgist responses (→ `objections/`) · Historical examples (→ `places/`, `events/`) ·
How to deploy it (framing tips, audience guidance).

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
