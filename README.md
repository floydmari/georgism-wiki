# Georgism Wiki — Source of Truth

Markdown source files for the Georgism & Land Value Taxation wiki at [progress.org/wiki](https://www.progress.org/wiki/).

Content is synced to Ghost CMS via the Ghost Admin API. Each file maps to a Ghost post tagged `wiki`.

## Categories
- `concepts/` — Economic concepts (LVT, economic rent, deadweight loss, etc.)
- `people/` — Economists and thinkers (Henry George, Mason Gaffney, Fred Harrison)
- `places/` — Jurisdictions that have implemented LVT (Estonia, Denmark, Harrisburg PA)
- `theories/` — Academic frameworks and books (Progress and Poverty, ATCOR)

## License
CC BY 4.0 — freely reusable with attribution.

## Contributing
See [AI Editor Instructions](https://www.notion.so/AI-Editor-Instructions-How-to-Push-Updates-to-the-Wiki-372e068c43f58175b5ccfecdf757c236) for how to add or edit articles.


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
