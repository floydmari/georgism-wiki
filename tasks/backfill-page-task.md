# Standard task: backfill a stub into a full page (the flywheel's second half)

You are a T2 editor backfilling ONE existing stub page (specified by the orchestrator) into a
full article per EDITORIAL.md. The defining step — before any web research:

1. **RE-MINE THE CORPUS.** `grep -rl "<topic terms>" research/ concepts/ outcomes/ narratives/
   objections/` and READ every page that mentions your topic. The wiki has already ingested
   dozens of sources; earlier pages were written before this stub existed, so their material was
   never extracted FOR it. Pull the relevant findings, quotes-with-citations, and cross-links out
   of the existing corpus first — cite the underlying sources (via the registry), not the wiki
   pages themselves (wiki links are navigation, not evidence).
2. Then web-research to fill remaining gaps (never fabricate; [CITATION NEEDED]/[VERIFY]).
3. Rewrite the stub in place: full template for its category (EDITORIAL.md §6), flip
   `stub: false`, set `last_reviewed`, wire supports_outcomes/related_* as justified.
4. Wire NEW inbound links: every corpus page you re-mined that discusses this topic should link
   here — list them in your report (orchestrator applies; or edit them yourself ONLY if the
   orchestrator's task assignment says so).
5. Validate: `python3 scripts/lint_wiki.py` — no new ERRORs.

RETURN: (1) lint status; (2) registry updates (sources cited); (3) corpus pages re-mined and the
inbound links they should carry; (4) DISCOVERED candidates (all categories — backfilling often
surfaces more); (5) markers left.
