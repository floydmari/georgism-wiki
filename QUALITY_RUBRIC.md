# QUALITY_RUBRIC.md — Article Scoring Rubric

Score each article 1–5 on six dimensions. Used by T1 review and by `[AUDIT]` iterations.
An article is **publish-ready at ≥ 4 on every dimension** (flagships: 5 on Accuracy & Credibility).
Priority for improvement is weighted by the source **Tier** of the topic (Core > Important > Supplementary).

| # | Dimension | 1 (poor) | 3 (adequate) | 5 (excellent) |
|---|-----------|----------|--------------|---------------|
| 1 | **Accuracy & sourcing** | Claims unsourced or page-level only | Most substantive claims cited | Every A–F claim has a claim-level, correctly-tiered, linked citation; strength matches source |
| 2 | **Comprehensiveness** | Stub / major aspects missing | Covers the core | Covers origin, mechanism, evidence, counter-evidence, and context; nothing important omitted |
| 3 | **Credibility / neutrality** | Reads as advocacy; strawmans critics | Mostly neutral | NPOV throughout; the strongest opposing case is stated fairly before any response |
| 4 | **Narrative clarity** | Confusing; jargon undefined | Readable | Clear, well-structured; jargon defined on first use; strong lede |
| 5 | **Cross-link integration** | Orphan or ≤1 link | Some links | 3+ outbound, 2+ inbound; bidirectional research↔outcome links wired |
| 6 | **Freshness** | Stale dates, dead links, no `last_reviewed` | Mostly current | All data current, links live, `last_reviewed` set this cycle |

**Scoring output (per audited article):** the six scores, the single weakest dimension, and one
concrete next action. Feed low scorers back into `BACKLOG.md` with the appropriate tier tag.

**Red flags that cap a score at ≤ 2 regardless of other dimensions:**
- A fabricated or unverifiable citation (Accuracy → 1).
- A banned-certainty word unsupported by its source (Credibility → ≤ 2).
- An objection page that strawmans the objection (Credibility → 1).
