# Georgism Wiki — Source of Truth

Markdown source files for the Georgism & Land Value Taxation wiki at [progress.org/wiki](https://www.progress.org/wiki/).

Content is synced to Ghost CMS via the Ghost Admin API. Each file maps to a Ghost post tagged `wiki`.

## Categories
- `concepts/` — Ideas & terms (LVT, economic rent, ATCOR, deadweight loss, unearned increment)
- `people/` — Thinkers & reformers (Henry George, Gaffney, Harrison, Mill, Ricardo)
- `places/` — Jurisdictions & their land-tax record (Estonia, Denmark, Harrisburg, Taiwan)
- `events/` — Events & Campaigns: political attempts & movements (1886 NYC race, 1909 People's Budget)
- `outcomes/` — Evidence-backed claims about what LVT/rent policy actually does (links to research/)
- `research/` — The papers, studies & datasets themselves (the source index, one entry each)
- `organizations/` — Institutions carrying the movement (Lincoln Institute, Schalkenbach, HG School)
- `objections/` — Serious counterarguments and their responses

## License
CC BY 4.0 — freely reusable with attribution.

## Contributing
See [AI Editor Instructions](https://www.notion.so/AI-Editor-Instructions-How-to-Push-Updates-to-the-Wiki-372e068c43f58175b5ccfecdf757c236) for how to add or edit articles.

### Editorial system (in-repo, model-agnostic)
- **[`EDITORIAL.md`](EDITORIAL.md)** — the constitution: claim taxonomy, citation & evidence rules, source-quality hierarchy, per-category templates, publishing rules. Read this first.
- **[`QUALITY_RUBRIC.md`](QUALITY_RUBRIC.md)** — the 6-dimension scoring rubric.
- **[`LOOP.md`](LOOP.md)** — the tiered improvement loop any model runs (T1 Fable / T2 Sonnet / T3 Flash-Haiku).
- **[`LOOPLOG.md`](LOOPLOG.md)** — the descriptive record of what each loop actually changed (the history behind `LOOP.md`).
- **[`BACKLOG.md`](BACKLOG.md)** — the prioritized task queue and persistent memory.
- **`sources/registry.csv`** — the source register (mirror of the master Google Sheet). Regenerate/seed with `python3 scripts/seed_registry.py`.

### Tooling
```bash
python3 scripts/lint_wiki.py                       # quality gate (zero deps); --strict for CI
python3 scripts/build_preview.py                   # render the branch to preview/
python3 -m http.server -d preview 8000             # browse locally before publishing
python3 scripts/pull_from_ghost.py <folder> <slug> # reconcile a page that drifted onto Ghost
```
Nothing publishes until `scripts/sync_to_ghost.py` runs — GitHub is the master record.


## Publishing to Ghost — three critical gotchas

The wiki is served by Ghost (`progress-org.ghost.io`). Markdown here is the source of
truth; `scripts/sync_to_ghost.py` pushes it to Ghost via the Admin API. **Any agent or
script publishing wiki entries via the API must get all three of these right** — each one
fails *silently*:

| # | Rule | What breaks if you skip it |
|---|------|----------------------------|
| 1 | Append **`?source=html`** to the create/update URL when sending an `html` field | Ghost stores Lexical, not HTML — the body is dropped and the page renders empty (title + excerpt only) |
| 2 | Set **`custom_template: "custom-wiki-entry"`** on every wiki post | Ghost has no primary-tag→template resolution; the entry renders with the plain article template instead of the wiki layout |
| 3 | Primary tag must be **`wiki`** (first in the list) + a category tag (`wiki-concepts`, `wiki-people`, `wiki-places`, `wiki-theories`, `wiki-events`, `wiki-inventions`) | The entry won't route to `/wiki/{slug}/` and will leak into the essays homepage |

`scripts/sync_to_ghost.py` bakes all three in — use it (or copy its logic) rather than
hand-rolling Admin API calls.
