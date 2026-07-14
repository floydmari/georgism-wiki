# Draft: "Related on the wiki" theme partial (Option 1)

**Status:** draft only — the `progress-org-theme` repo is not attached to this session, so
this cannot ship as a PR yet. Ask: add `floydmari/progress-org-theme` to the session (or say
"add the theme repo") and this becomes a `claude/*` branch + PR for human merge.

**Audit result (2026-07-14, live from Ghost Admin API, read-only):**
- 413/608 legacy `/articles/` posts carry a `wiki-research-*` topic tag (the 2026-07-12
  tagging pass is intact on-server). The other 195 are deliberately untagged (off-topic).
- Wiki posts sharing each topic tag: georgism 32, lvt 67, finance 23, inequality 34,
  resources 61, urban 28, housing 44 — every tagged article will get a non-empty box.
- No body edits anywhere; the box renders purely from tag metadata. Reversible by
  reverting the theme commit.

## Partial: `partials/related-wiki.hbs` (new file)

```hbs
{{!-- Related on the wiki — tag-driven, zero body edits.
     Renders for legacy articles only (post.hbs guards against wiki posts).
     Matches wiki entries sharing ANY of this article's tags; the +tag:wiki
     clause keeps results inside the wiki. Articles without shared tags
     render nothing (the #if guard). --}}
{{#get "posts"
    filter="tags:[{{#foreach tags}}{{slug}}{{#unless @last}},{{/unless}}{{/foreach}}]+tag:wiki"
    limit="5"
    include="tags"
    as |wiki_related|}}
  {{#if wiki_related}}
    <aside class="related-wiki">
      <h3 class="related-wiki-title">Related on the Georgism Wiki</h3>
      <ul class="related-wiki-list">
        {{#foreach wiki_related}}
          <li><a href="{{url}}">{{title}}</a></li>
        {{/foreach}}
      </ul>
      <a class="related-wiki-more" href="/wiki/start-here/">Explore the wiki &rarr;</a>
    </aside>
  {{/if}}
{{/get}}
```

## Hook in `post.hbs`

Insert after the article body / before comments-or-footer, guarded so wiki entries
(which use `custom-wiki-entry.hbs` anyway) and any future wiki-tagged post never
show the box on themselves:

```hbs
{{#post}}
  ...existing body...
  {{^has tag="wiki"}}
    {{> "related-wiki"}}
  {{/has}}
  ...
{{/post}}
```

**Gotchas honoured:**
- `{{#has tag="wiki"}}` matches tag NAME, not slug — confirm in Ghost admin that the wiki
  tag's display name is exactly `wiki` (memory says name/slug match for this tag; verify in
  the PR). If the name differs, use the name here.
- Filter interpolation over ALL of the article's tags (not just `wiki-research-*`) is
  deliberate: Ghost filters can't prefix-match, wiki posts only share the topical tags, and
  the `+tag:wiki` clause bounds results. It also lets finer-grained shared tags (e.g.
  `taxation`) enrich matches for free.
- 84 articles carry >1 topic tag — the single `{{#get}}` handles that natively (any-match),
  no duplicate boxes.
- Minimal CSS to add (theme's tokens will override): `.related-wiki { border: 1px solid
  var(--color-border, #ddd); border-radius: 8px; padding: 1rem 1.25rem; margin: 2rem 0; }`

## Alternative already on file
BACKLOG (2026-07-12) notes a paste-ready code-injection guide was delivered to Floyd
(`from-the-wiki-theme-block.md`). The theme-repo partial supersedes it: versioned,
reviewable, auto-deployed on merge via the theme repo's GitHub Action.
