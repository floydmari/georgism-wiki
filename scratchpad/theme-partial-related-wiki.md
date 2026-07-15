# Option 1 "Related on the wiki" box — RESOLVED: already shipped in the theme

**Finding (2026-07-14, after attaching floydmari/progress-org-theme):** the theme's
`post.hbs` (lines ~68–102 at commit d806f8b) already contains the tag-driven wiki box:
a `{{^has tag="#wiki"}}` guard wrapping a `{{#has tag="<topic display name>"}}` chain
over all seven `wiki-research-*` topics, each rendering `partials/wiki-related-card.hbs`
("From the Georgism Wiki", 4 entries + start-here/dashboard/how-we-verify footer links)
via `{{#get "posts" filter="tag:wiki+tag:wiki-research-<topic>"}}`.

**Verified live (all seven topic branches render on progress.org):**
| topic tag | display name (matches has-chain) | live article checked |
|---|---|---|
| wiki-research-lvt | LVT Studies | how-appraisers-value-land ✅ |
| wiki-research-housing | Housing & Land Values | build-to-rent-isnt-the-problem ✅ |
| wiki-research-georgism | Georgist Thought & History | decades-of-wisdom-…-josh-vincent ✅ |
| wiki-research-inequality | Inequality & Distribution | gbi-vs-ubi ✅ |
| wiki-research-finance | Finance & Crises | 18-6-year-real-estate-cycle ✅ |
| wiki-research-urban | Urban Economics | dont-reject-data-centers-negotiate-harder ✅ |
| wiki-research-resources | Resource Rents & Dividends | a-georgist-approach-to-emissions-rights ✅ |

Tag coverage on-server: 413/608 legacy articles carry a topic tag (2026-07-12 pass intact);
the 195 untagged are deliberately off-topic. Every topic tag has 23–67 wiki posts to serve,
so no tagged article renders an empty box.

**Maintenance notes (the only follow-ups Option 1 could ever need):**
- `{{#has}}` matches tag display NAMES; the `{{#get}}` filters match slugs. If a
  wiki-research-* tag is ever renamed in Ghost admin, the corresponding branch fails
  silently — keep post.hbs in sync (the comment in post.hbs says the same).
- First-match-wins: an article with 2+ topic tags shows only its first topic's box (84
  articles have >1 topic tag). Acceptable; a merged multi-topic box would be the only
  enhancement worth considering.
- The earlier draft in this file proposed an all-tags `{{#get}}` interpolation partial;
  superseded by the shipped implementation. See git history of this file if ever wanted.
