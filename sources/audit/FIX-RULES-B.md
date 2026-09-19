# Fix rules — class B (attribution and notability). For opus fixers. Read fully before editing.

Floyd's rule (EDITORIAL.md §4c): a person cited to show that an idea has support must be
prominent — a recognised scholar, a canonical author, an official body. Practitioner-authors,
advocates, bloggers, newsletter writers and movement organisations (Tier 2 in
`sources/audit/people-tiers.json`) may be cited as the ORIGIN or a PROPONENT of a term or
claim, with their status stated, but never as evidence the claim is right — and never in the
lead of a concept, theory, objection, benefit, problem, narrative, event or place page as if
they were an authority.

Your worklist lists, per page, every sentence in the body (Sources and See Also excluded)
that mentions a Tier-2 name, with a `lead` flag for the first ~1200 characters or the excerpt.
The regex is deliberately broad ("Harrison", "Barnes", "Cord", "Anderson's" will also match
unrelated people) — the first thing you do with each hit is decide whether it is the roster
person at all. If not, skip it.

## Classify each genuine mention into ONE role

- **subject** — the page is about this person or their work (a `research/` page on Harrison's
  *The Power in the Land*, a `places/` page recounting what Common Wealth Canada proposed).
  Leave it. Their claims are reported as theirs; that is the page's job.
- **origin** — the sentence says this person coined, named, popularised or first proposed the
  term/idea ("the term Akhil Patel uses for…", "Barnes's sky-trust proposal"). Leave it, but
  make sure the status is stated on first mention if the page is not about them: "the
  practitioner-author Akhil Patel", "the investment writer Phillip J. Anderson", "the advocacy
  organisation Common Wealth Canada". One short status phrase, once per page.
- **proponent-section** — the mention sits in a clearly labelled "Who promotes it", "Current
  debate", "In the land-cycle literature", "Advocacy" section. Leave it.
- **support** — the person is used to corroborate that a claim is TRUE: "as Harrison shows",
  "Patel's book makes the same point", "catalogued by both Anderson and Patel as a cycle
  peak", "Doucet reports that land is ~40% of US household wealth", "used … as evidence
  that…", "Harrison, Foldvary and Patel all find…", or a Tier-2 name listed alongside Tier-1
  names as an equal. **Fix these.**
- **lead-authority** — any Tier-2 name in the lead or `excerpt:` of a non-people, non-books
  page presented as an authority (not as the subject). **Fix these**, and they take priority.

## How to fix a support / lead-authority mention

In order of preference:
1. **Substitute a Tier-1 source the page (or the wiki) already carries for the same point.**
   If the page's own Sources include an academic or official source that makes the claim, cite
   that instead and drop the Tier-2 name from the sentence. If another wiki page carries the
   Tier-1 source, you may link that page for navigation, but the citation must be the external
   source (EDITORIAL golden rule 7) — add it to Sources with a "— used for" note only if you
   can copy its full reference from the other page; never invent one.
2. **Demote to origin/proponent.** Rewrite so the sentence reports the claim as the person's
   claim, with status: "Practitioner cycle writers such as Phillip J. Anderson and Akhil Patel
   list 1907 among their historical peak years" — and move it out of the lead into the body's
   debate/literature section if it was in the lead. This is the usual fix for the events pages
   that certify a panic as a "land-cycle peak" by citing Anderson and Patel.
3. **Hedge and drop.** If the point has no Tier-1 support anywhere on the wiki and cannot stand
   as a bare proponent claim, rewrite to "proponents argue…" and delete the name; keep the
   Sources entry (it is the origin of the claim) but change its "— used for" note to say so.

Do not delete the underlying claim if a Tier-1 source for it exists on the page; do not add
new claims; do not touch Sources beyond the "— used for" note; do not restructure sections
except to relocate a single sentence out of the lead. Keep an eye on EDITORIAL §4b as you
rewrite — no grade codes or process talk may creep back in.

## Specific rulings (fable, 2026-09-19)
- **Fred Harrison** is Tier 2 for *support* purposes despite his prominence in the movement:
  his cycle books are practitioner works, not peer-reviewed. He remains the natural *origin*
  citation for the 18-year cycle claim and may be named as such everywhere. Where a page uses
  him as evidence that the cycle exists or that a crash was cycle-driven, demote per rule 2.
- **Michael Hudson, Guy Standing, Fred Foldvary (academic papers), Brett Christophers,
  Mariana Mazzucato, Josh Ryan-Collins, Jean Drèze** are Tier 1. Not in your worklist; leave.
- **Peter Barnes** is Tier 2 but is the origin of the sky-trust / dividend design; origin
  mentions are fine. Fix only where his estimates are used as empirical support.
- **Ted Gwartney** is a practising assessor; he may be cited on assessment *practice* as a
  practitioner authority ("the assessor Ted Gwartney's method"), not on economic effects.
- **Lars Doucet, Common Wealth Canada, Prosper Australia, Dan Neidle/TPA, PolicyEngine,
  Positive Money, Henry George Foundation** — advocacy or modelling organisations and writers.
  Their *models and figures* may be reported as theirs ("Common Wealth Canada's modelling
  projects…"); they may not be used as the evidence that a mechanism is real. Where a page
  already says "the organisation's own modelling, not independently verified", that is the
  correct form; leave it.

## Procedure
1. Read the page in full and its worklist entries. Classify every genuine hit.
2. Fix support and lead-authority hits. Leave subject / origin / proponent-section hits (add
   the status phrase on first mention where missing).
3. Run `python3 scripts/lint_wiki.py 2>&1 | tail -1` → `0 error(s)`; run
   `python3 scripts/audit_wiki.py <files>` → no new A-class hits.
4. Do NOT commit. Report per page: hits classified (counts by role), what you changed, and any
   support mention you left because a Tier-1 substitute would have had to be invented.
