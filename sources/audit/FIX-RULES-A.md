# Fix rules — class A (process artefacts). For opus fixers. Read fully before editing.

You are removing the wiki's *research-process narration* from reader-facing pages while
keeping every *claim-status* signal the reader needs. EDITORIAL.md §4b is the rule; this
file is the worked version. The four golden constraints:

1. **Never weaken or delete a factual claim to get rid of an artefact.** The hedge stays; the
   diary goes. If a sentence says "X, though not independently verified this session", the
   result is "X, though this has not been independently verified" — not "X".
2. **Never fabricate.** Do not invent a citation, date, page number or source to close a
   `[VERIFY …]` marker. If the marker says a claim is unconfirmed, keep the claim hedged
   ("reported by X; unconfirmed") and drop the bracket. If the marker says a *wiki page*
   might exist (`[VERIFY: wiki page?]`), check `sources/wiki-inventory.csv`: link it if it
   exists, otherwise remove the bracket and leave plain text.
3. **Sources section keeps its instruments, loses its diary.** Grade codes (`A-claim` …
   `D-claim`) and access status STAY in Sources annotations. Rewrite them impersonally and
   dated. Delete tool names (curl, WebFetch, r.jina.ai, Wayback, Googlebot, user-agent),
   HTTP codes, proxy/egress talk, retry logs, and "this session / this pass / this
   environment / this wiki's fetcher".
4. **Body, lead and `excerpt:` keep NO grade codes and NO process talk at all.** Where a
   body sentence carried a grade code in parentheses, delete the parenthetical; if the
   parenthetical also carried a real hedge ("D-claim; the author's own recollection"), keep
   the hedge in plain words ("— the author's own recollection").

## Rewrite table

| Before (artefact) | After |
|---|---|
| "…, not independently verified this session." | "…, though this has not been independently verified." |
| "The full text could not be obtained this pass; this page rests on the abstract." | "Only the abstract is publicly available; the summary rests on it." |
| "(B-claim; abstract-level)" in body | *delete*; if needed: "an abstract-level reading" in plain prose |
| "(D-claim: incidence reasoning in an advocacy essay, not a peer-reviewed estimate.)" in body | "— incidence reasoning from an advocacy essay rather than a peer-reviewed estimate." |
| "as of this writing" | "as of <last_reviewed date>" or drop if the sentence works without it |
| "[VERIFY: wiki page?]" after a name | link `[Name](/wiki/slug/)` if the slug exists in the inventory; else remove bracket |
| "[VERIFY: needs-unblocked-web — full text not retrievable, Wiley blocked automated access]" | remove bracket; if the sentence needs it, "(full text not publicly accessible; summary from the abstract)" |
| "[VERIFY: internal inconsistency in the source — 82.9% vs 89.2%]" | plain prose: "The paper reports both 82.9% and 89.2% for this rate; the discrepancy is in the source itself." |
| "[VERIFY — PENDING: cannot be assessed until the year closes; revisit after 2026]" | "— a forecast whose window has only just opened and cannot yet be assessed." |
| "[CITATION NEEDED: … Channels tried this session … HTTP 429 … HathiTrust 403 …]" | drop the whole bracket; hedge the sentence to what is actually sourced; if nothing is sourced, "No published source for this has been located." |
| "**Attempted** (2026-07-18): general web search for … ; Semantic Scholar …" | *delete the whole log* |
| "Corrected 2026-08-10:" / "Reattempted 2026-08-10" in body | delete the stamp; keep the corrected content |
| "per the wiki's discovery notes on that book" / "drawn from the wiki's existing verified summary" | cite the work itself ("in *Title* (Ch. N)"); if the page cannot cite the work, hedge "reportedly" and drop the reference to notes |
| "## Two honesty notes" / editor-facing section headings | fold the substance into "Limits and Caveats" (or the page's equivalent) as ordinary prose; remove the heading |
| Sources: "fetch blocked (403) to this session 2026-08-29; summary drawn from a WebSearch-synthesized paraphrase" | "Full text not accessible at last review (2026-08-29); summary rests on secondary descriptions of the paper." |
| Sources: "WebFetch returned HTTP 403; retrieved via curl with a browser user-agent and read in full 2026-09-06" | "Read in full, 2026-09-06." |
| Sources: "verified verbatim this session" | "verified verbatim (2026-MM-DD)" using the page's `last_reviewed` if no other date is given |
| Sources: "(B-claim; abstract-level, full text not retrieved this pass)" | "(B-claim; abstract-level — full text not accessible at last review)" |
| Sources: "the bare host 403s to automated requests" | delete |

## Procedure per page
1. Read the page in full. Read its entry in the worklist (exact matches with context).
2. Fix every listed hit AND any other instance of the same classes you see — the regex is a
   floor, not a ceiling. Common misses: "this wiki's", "egress", "bot-check", "Client
   Challenge", "proxy", "fetcher", "automated access/fetch", "queued for", "STILL OPEN".
3. Do not change anything else: no restructuring, no new content, no link additions except
   the `[VERIFY: wiki page?]` resolution, no See Also edits, no frontmatter edits other than
   `excerpt:` if it carried an artefact.
4. Re-run `python3 scripts/audit_wiki.py --summary <the files you edited>`; body hits for
   A1/A2/A3 must be zero for those files (Sources A4 must be zero too). Then
   `python3 scripts/lint_wiki.py 2>&1 | tail -1` must show `0 error(s)`.
5. Do NOT commit. Report the files you changed and anything you could not resolve without
   fabricating (leave those hedged, and list them).
