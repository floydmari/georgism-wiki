# How the Georgism Wiki Grows — visual map

> **Sync rule (Floyd, 2026-07-06):** this diagram must always reflect what the loops actually
> do. Any change to LOOP.md's structure (steps, gates, lanes, roles) updates this file in the
> same commit. GitHub renders the Mermaid blocks natively — view this file on GitHub to see
> the pictures.

**The mission:** the definitive, honest reference on Geoism — the capture of ALL economic
rents for public good, with Georgism/land as core and root (scope expanded 2026-07-06) —
every claim cited, every counterargument steelmanned, every important source read and mined,
and the rent gradient kept honest (land is the clean case; the frontier is contested). The
loop is the research desk that builds it.

## 1. One editorial shift (LOOP.md steps 1–11)

Every shift — whoever runs it — moves one piece of the wiki forward and leaves the
Fact-Check Desk cleaner than it found it. The editor's review is the only door to `main`.

```mermaid
flowchart TD
    A["1 · Catch up on the desk\ngit pull · lint · Hermes inbox first\n(delivered evidence un-blocks shipped pages)"] --> B["2 · Choose one piece of work\nfrom BACKLOG, matching your role"]
    B --> C["3 · Research & write it\nread sources first · cite every claim\nnever guess — flag what you can't verify\nnew people pages start with an Exa pass"]
    C --> D["5 · Review as a skeptical economist\nwould each claim's wording survive\na hostile expert reader?\nbody-parity · work the literature itself"]
    D --> E["6 · Run the Fact-Check Desk\nevery open flag gets an owner\nHermes work order auto-generated\ncampsite rule: clear or route ≥5 debts"]
    E --> F["7 · Preview the wiki as a reader"]
    F --> G["8 · Grow the map\nreading surfaced new topics? accept if\n≥2 pages demand them · ≤8 stubs/shift\ndigest before you scan"]
    G --> H["9-10 · Log the shift · commit · push · PR"]
    H --> I{"EDITOR'S REVIEW (T1)\nthe only path to main"}
    I -->|approved| J["main — source of truth\nfor progress.org/wiki"]
    I -->|issues| B
```

## 2. The coverage flywheel (why the wiki compounds)

Reading Harrison's 1983 book gave the wiki Australian construction evidence for two outcome
pages, bios-in-waiting for the critics he cites, four books for the wanted list, and the
Japanese land bubble as a historical episode. Each of those, built out, cites new sources —
which get read, which surface more.

```mermaid
flowchart LR
    FIND["FIND the literature\npapers · books · sites · critics\nreading list: registry.csv + wanted-books"] --> READ["READ & MINE each source\nresearch/ and books/ pages\neverything it teaches gets a home"]
    READ --> SYN["SYNTHESIZE into the case\noutcomes: what evidence shows\nobjections: what critics say, steelmanned\nnarratives: how to tell it · concepts: how it works"]
    SYN --> DISC["DISCOVER new ground\nevery source surfaces people, events,\nplaces, mechanisms, counterarguments,\nfurther books worth covering"]
    DISC --> STUB["STUB what's warranted\naccept bar: ≥2 pages demand it\nsourced, visible, tracked"]
    STUB --> PRI["PRIORITIZE (editor)\nwhich stubs does the wiki\nlink to most?"]
    PRI --> BUILD["BUILD OUT the top stubs\nre-mine the existing corpus first —\nolder pages hold evidence for new topics"]
    BUILD --> FIND
    READ -.->|"every ~10 sources read"| SP["SYNTHESIS pass (editor)\nwhat does the recent reading\ncollectively justify? new outcome?\nnew objection? new narrative?"]
    SP -.-> STUB
```

## 3. Lanes — who covers what (so agents never collide)

```mermaid
flowchart TD
    subgraph CAMPAIGN["Campaign desk (this container, claude/* branch)"]
        ED["T1 editor — judgment, review,\nflagship pages, the publish gate"]
        WR["T2/T3 writers & copy desk\n(≤3-4 concurrent subagents)"]
    end
    subgraph FIELD["Hermes — the field agent (Floyd's machine, hermes/* branches)"]
        HB["Works the auto-generated\nsources/hermes-workorder.md:\nblocked-web fact-checks + book scans\n(Floyd's library, legal copies only)\n+ files discovery reports"]
    end
    subgraph DESK["The Fact-Check Desk (gap-1 machinery)"]
        Q["Every unverified claim = an open\nfact-check with an owner:\nblocked web → Hermes\nmissing books → wanted-books + Floyd\nowner-only facts → Floyd\nworkable here → this shift"]
    end
    WR --> ED
    Q -->|"work order, regenerated\neach shift"| HB
    HB -->|"PR — never self-merged"| ED
    ED -->|merge| MAIN["main = master record"]
    MAIN -->|"Floyd's separate process"| GHOST["progress.org/wiki"]
```

## 4. The honesty machinery (what keeps it truthful)

- **Never fabricate** → an unverifiable claim gets a visible `[CITATION NEEDED]` / `[VERIFY]`
  flag; the Fact-Check Desk ledgers every flag by owner and the count must trend down
  (the ratchet — new honest flags are fine, un-routed drift is not).
- **Lint gates** (`scripts/lint_wiki.py`): frontmatter schema · link resolution · bidirectional
  evidence wiring · body-parity · banned-certainty words · quote-length cap (public-domain
  works exempt — they may be held in full, EDITORIAL §3b) · conflict-marker and `[[wikilink]]`
  detection · registry duplicates · shadow-library provenance ban.
- **One finding, one home** (the delta rule): enrichments add only what's new to the wiki's
  coverage and link to a finding's home page rather than restating it.
- **Strongest evidence first**: supporting-research lists read in descending evidential
  weight — the reader who stops at item one has met the best evidence, not the first-drafted.
- **Counter-evidence at full strength**: outcomes carry `challenged_by`; objections are
  steelmanned (the homevoter objection is rated the wiki's strongest); advocacy sources are
  labeled advocacy (C/D-claims, never B).
- **The editor's adversarial pass** on everything before merge: *"what would a skeptical
  economist dispute, and does each claim's wording match its source's strength?"*
