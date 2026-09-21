# Context briefs — T0 prompt template

Each loop pass commits one `<date>.json` here: the Sonnet T0 agent's per-item briefs for the
queue batch (advisory; the T1 editor re-verifies and may override, noting overrides in LOOPLOG).

The T0 prompt must carry these instructions verbatim so the rules survive session resets:

- Read `EDITORIAL.md` — §2 claim taxonomy; **§4b** (reader-facing prose never narrates the
  research process; grade codes and access notes live in Sources only, impersonally phrased;
  `[VERIFY]`, `[CITE]`, `[BLOCKED]` are work items, never published); **§4c**
  attribution-and-notability (practitioner-authors, bloggers, advocacy bodies, newsletters and
  law-firm marketing are Tier 2: origin/proponent only, never support; official bodies,
  recognised scholars and canonical authors are Tier 1; working list in
  `sources/audit/people-tiers.json`; unknown names are judged by the rubric, not assumed Tier 1).
- Access ladder when blocked: curl with a browser user-agent → r.jina.ai → Googlebot
  user-agent → save PDF and parse locally. Say plainly what could not be fetched.
- Brief schema per item: `url`, `title`, `what_was_fetched`, `verdict` (ENRICH <page> /
  NEW <page> / REJECT / DEFER with reason), `claim_grade` (A–D with the §4c tier of the
  source), `content_summary` (figures with their named sources), `existing_wiki_coverage`
  (from the corpus digest), `uncertainties`.
- Advisory only: T0 edits no wiki pages.

Writer prompts (Sonnet or Opus) carry the same §4b/§4c paragraph plus: quotes ≤50 words with
locators; every Sources entry annotated "— used for …" with its claim grade; new pages need
≥2 inbound links; run `python3 scripts/lint_wiki.py` (0 errors — it now includes the §4b
scanner) before handing back.
