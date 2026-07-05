# The Wiki Improvement Loop — visual map

> **Sync rule (Floyd, 2026-07-06):** this diagram must always reflect what the loops actually
> do. Any change to LOOP.md's structure (steps, gates, lanes, roles) updates this file in the
> same commit. GitHub renders the Mermaid blocks natively — view this file on GitHub to see
> the pictures.

## 1. One iteration (LOOP.md steps 1–11)

Every wave, regardless of who runs it, walks this pipeline. The T1 gate is the only door to
`main`; nothing publishes from inside the loop (deployment to progress.org is Floyd's separate
process).

```mermaid
flowchart TD
    A["1 · Sync & gate\ngit pull · lint · inbox sweep"] --> B["2 · Pick ONE task\nfrom BACKLOG, matching your tier"]
    B --> C["3 · Do the work\nweb-research first · cite at claim level\nnever fabricate — use [VERIFY]/[CITATION NEEDED]\npeople pages: Exa enrichment first"]
    C --> D["5 · Self-review\nQUALITY_RUBRIC + T1 adversarial pass\nbody-parity · synthesis de-referencing"]
    D --> E["6 · Lint until clean\n+ DEBT RATCHET: warnings/markers may not\nrise un-routed · regenerate verification queue"]
    E --> F["7 · Preview build"]
    F --> G["8 · Harvest discoveries → stubs\naccept bar: ≥2 inbound-demand pages\nquota: ~8 stubs/wave"]
    G --> H["9-10 · Update BACKLOG · commit · push · PR"]
    H --> I{"T1 REVIEW GATE\n(Fable — the only\npath to main)"}
    I -->|approved| J["merge to main\n= source of truth for progress.org/wiki"]
    I -->|issues| B
```

## 2. The growth flywheel (why the loop compounds)

Each turn of the wheel makes every earlier ingest more valuable: new pages re-mine old
sources, and every source scanned surfaces new warranted topics.

```mermaid
flowchart LR
    ING["INGEST\nsources → research/ pages\n+ books/ summary pages"] --> EXT["EXTRACT\nclaims wired into outcomes,\nconcepts, objections, narratives"]
    EXT --> DISC["DISCOVER\nuniversal discovery: every source\nyields candidates in ALL categories\n(research · people · events · places\nconcepts · organizations · objections · books)"]
    DISC --> STUB["STUB\naccepted candidates become\nvisible, sourced stubs (quota ~8/wave)"]
    STUB --> PRI["PRIORITIZE (T1)\nrank stubs by inbound-link demand\n+ evidence already in corpus"]
    PRI --> BF["BACKFILL\ntop stubs → full pages,\nre-mining the existing corpus first"]
    BF --> ING
    BF -.->|"new pages cite new sources"| ING
    ING -.->|"every ~10 ingests"| SYN["SYNTHESIS (T1)\nwhat does the set collectively justify?\nnew outcome / concept / objection / narrative"]
    SYN -.-> STUB
```

## 3. Lanes and agents (who runs what)

Two content lanes never collide: the campaign branch does new content; Hermes works
marker-carrying pages, books, and the verification queue. Both end at the same T1 gate.

```mermaid
flowchart TD
    subgraph CLOUD["Campaign branch (this container: claude/georgism-wiki-campaign-*)"]
        T1["T1 Fable — judgment, review,\nflagship pages, the publish gate"]
        T2["T2/T3 subagents — drafting,\nforage/verify (≤3-4 concurrent)"]
    end
    subgraph HERMES["Hermes lane (Floyd's machine: hermes/* branches)"]
        HB["Full DRAFT loops on the verification\nqueue + book scans (private library,\nlegal copies only — never libgen)\n+ universal discovery reports"]
    end
    subgraph BLOCKED["Structurally blocked debt"]
        Q["verification-queue.md\nby unblock channel:\nneeds-unblocked-web → Hermes\nneeds-book-copy → Hermes/Floyd\nneeds-owner-input → Floyd"]
    end
    T2 --> T1
    Q -->|routed, not carried| HB
    HB -->|PR, never self-merged| T1
    T1 -->|merge| MAIN["main = master record\n(registry exports committed in-repo;\nDrive sync de-scoped)"]
    MAIN -->|"Floyd's separate process"| GHOST["progress.org/wiki (Ghost)"]
```

## 4. The honesty machinery (what keeps it truthful)

- **Never fabricate** → unverifiable claims carry `[CITATION NEEDED]` / `[VERIFY]` markers;
  `scripts/verification_queue.py` ledgers every marker by unblock channel.
- **Lint gates** (`scripts/lint_wiki.py`): frontmatter schema · link resolution · bidirectional
  evidence wiring · BODY-PARITY · banned-certainty words · quote-length cap · conflict-marker
  and `[[wikilink]]` detection · registry duplicates · shadow-library provenance ban.
- **Counter-evidence at full strength**: outcomes carry `challenged_by`; objections are
  steelmanned; advocacy sources are labeled as advocacy (C/D-claims, never B).
- **T1 adversarial review** on everything before merge: *"what would a skeptical economist
  dispute, and does each claim's wording match its source's strength?"*
