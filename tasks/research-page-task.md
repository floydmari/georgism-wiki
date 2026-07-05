# Standard task: READ & MINE one source into a research page (at the Mirrlees bar)

This is the **READ & MINE** step of the wiki's flywheel (LOOP.md): you are reading one piece
of the land-question literature for the definitive, honest reference on Georgism — and a
source is not "done" when summarized; it is done when what it teaches (findings at their true
strength, caveats, and the people/events/counterarguments it surfaces) has somewhere to live
on the wiki. Skeptics will read your page; it persuades only by accuracy and fairness.

You are a staff writer (T2) at /home/user/georgism-wiki. You create exactly ONE new file
(specified by the orchestrator). Do NOT edit any other file, do NOT edit
sources/registry.csv or BACKLOG.md, do NOT run git.

READ FIRST: EDITORIAL.md (§2 claim taxonomy A–F, §3 citations, §4 claim-strength + banned-certainty
list, §5 research frontmatter schema, §6 Standard article + annotated Sources, §1 never fabricate)
and the quality exemplar research/mirrlees-review.md — match its depth, structure, claim-level
citation density, and NPOV tone. Skim the outcomes/ and concepts/ file listings so every
/wiki/<slug>/ link you write resolves (broken links fail lint).

THE PAGE (structure, adapted to the source):
## Summary (what it is, who wrote it, venue, why it carries weight) · ## The Core
Argument/Findings (with claim-level citations; report empirical findings with their stated scope)
· ## Relation to the Georgist Case (precisely — supporting, complicating, or challenging; never
overstate) · ## Nuances and Limits (methodology caveats, what it does NOT show, notable critiques)
· ## Bears On (bulleted links to the outcome/objection/concept pages it informs, with one-line
whys) · ## See Also (3+ existing slugs) · ## Sources (annotated "— used for …").

FRONTMATTER (§5): title, category: research, tags, authors (verified), year (verified),
tier (as assigned), source_url (real, stable — DOI/NBER/SSRN/publisher/archive; verify it),
stub: false, excerpt (≤300 chars), last_reviewed: 2026-07-03, supports_outcomes: [exactly the
outcome slugs the orchestrator assigns — verify each exists in outcomes/].

RESEARCH HONESTY: you have web access, but this environment's egress proxy 403s many domains.
Verify via whatever fetches succeed + multiple agreeing search snippets. NEVER fabricate a
finding, number, quote, page, or URL — use [CITATION NEEDED: …] / [VERIFY: …] instead. Quotes
≤50 words. If the assigned paper turns out not to exist as described (wrong author/year/title),
say so in your report and write the page about the REAL closest source — never force a fake.

VALIDATE: run `python3 scripts/lint_wiki.py` — introduce no ERRORs (orphan + bidirectional-gap
warnings are expected; the orchestrator wires links).

RETURN (concise): (1) lint status; (2) the registry row (Title, Category, Author(s), Year, URL,
Tier, Format); (3) confirmed supports_outcomes (drop any the source doesn't actually support —
honesty beats coverage) and whether it belongs in challenged_by somewhere instead; (4) suggested
inbound links; (5) markers left.
