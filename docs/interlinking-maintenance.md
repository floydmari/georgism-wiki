# Legacy-article ↔ wiki interlinking — standing maintenance design

*Decided 2026-07-15 (Floyd: "figure out the best way to maintain an option 2 & 3 level of
interlinking over the long term as the site evolves" — this file is that decision).*

## The three layers (all live as of 2026-07-15)

| layer | what | mechanism | maintenance |
|---|---|---|---|
| **Option 1** — "From the Georgism Wiki" box | topic-level related wiki entries under each tagged article | theme `post.hbs` + `wiki-related-card.hbs`, keyed on the article's `wiki-research-*` tag; content fetched at render time | ZERO for existing pages (auto-evolves). New articles need one topic tag at publish time (see checklist) |
| **Option 2** — in-text entity links | exact-phrase links to people/places/concepts/orgs/books pages | one-time bulk apply via `apply_intext_links.py` (lexical surgery post-2021, mobiledoc surgery pre-2021); ledger in `sources/interlink-ledger.jsonl` | wave script for new articles (below) |
| **Option 3** — conceptual proof-point links | links to problems/benefits/objections pages the article substantively bears on | GLM-4.7 on Ollama Cloud maps article→claims (`build_concept_manifest.py`); review manifest gates apply | same wave script |

## Why bulk-on-request waves, NOT publish-time auto-injection

1. **The review gate is the safety property.** These are edits to human-authored prose;
   Floyd reviews a manifest before anything is applied. An auto-injector at publish time
   has no reviewer. (Standing rule: no Ghost writes without Floyd's word.)
2. **Volume doesn't justify automation risk**: a handful of articles a month; a wave is
   minutes of compute.
3. **No infrastructure**: a webhook auto-linker needs hosted middleware + a stored admin
   key; the wave runs inside a normal Claude session with the 1Password-resolved key.

## The wave runbook (monthly, or whenever Floyd asks)

```
export OLLAMA_API_KEY=$(op read "op://cupqdml5deh2x6povtmqsxdzyu/qbvmc7zeawrsamsgd7bnr6ujqe/credential")
python3 scripts/interlink_wave.py          # read-only: fetch, select NEW articles,
                                           # option-2 scan + GLM prune, render review manifest
# -> send scratchpad/interlink-wave-<date>.md to Floyd
# -> AFTER approval:
python3 scripts/apply_intext_links.py --slugs <approved slugs>
# option 3 for the same slugs: build_concept_manifest.py + render_concept_manifest.py,
# review, then apply approved grounded anchors the same way.
```

State: `sources/interlink-scanned.txt` (articles already processed — the wave skips them);
`sources/interlink-ledger.jsonl` (every link ever applied, with method + date).

## New-article checklist (for whoever publishes)
1. Add ONE `wiki-research-*` topic tag in Ghost admin → the Option-1 box appears
   immediately, no code.
2. In-text links: wait for the next wave (or ask for one).

## Gotchas (hard-won, do not relearn)
- Pre-2021 posts store **mobiledoc**, post-2021 **lexical**; `apply_intext_links.py`
  handles both. NEVER use `?source=html` on card-bearing posts.
- The apply script verifies every edit (plain text byte-identical + links present) and
  auto-restores the snapshot on drift. Snapshots: `scratchpad/cache/apply-backups/`.
- `{{#has tag=...}}` in the theme matches tag display NAMES; renaming a `wiki-research-*`
  tag in Ghost admin silently kills that topic's box — keep `post.hbs` in sync.
- GLM-4.7 on Ollama Cloud is a thinking model: use `think:false` and extract the JSON
  block; `format:"json"` returns empty content.

## Post-incident addendum (2026-07-15)
- The injected segment must be built ONLY by `deliverable()` in
  generate_related_boxes.py — it strips nested markers, absolutizes hrefs (Ghost
  rewrites relative URLs in stored code injection), and emits the slot-guarded
  relocation script. Never hand-assemble the segment.
- Option 1 v1 (runtime {{#get}} topic box) was retired with theme PR #51; boxes are
  now precompiled per-article (Option A). Rollback = revert #51 (runtime box returns
  instantly; injected metadata is inert without the slot).
