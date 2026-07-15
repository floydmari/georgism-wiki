#!/usr/bin/env python3
"""
render_concept_manifest.py — Option 3, stage 2. Render the GLM candidate mappings
(scratchpad/cache/concept-candidates.jsonl) as ONE reviewable Markdown manifest:
    article -> anchor words -> claim page (relation, rationale)
NOTHING is applied by this script; Floyd's sign-off on the manifest is the gate.
Ungrounded anchors (phrase not found verbatim in the article) are listed separately —
they are NOT applicable as in-text links without a human picking the anchor.
"""
import collections, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.environ.get("CONCEPT_OUT",
                     os.path.join(ROOT, "scratchpad", "cache", "concept-candidates.jsonl"))
OUT = os.path.join(ROOT, "scratchpad", "concept-link-manifest.md")

rows = [json.loads(l) for l in open(SRC)]
rows.sort(key=lambda r: r["title"].lower())
total = sum(len(r["mappings"]) for r in rows)
grounded = sum(1 for r in rows for m in r["mappings"] if m["grounded"])
witharts = sum(1 for r in rows if r["mappings"])
claims = collections.Counter(m["claim"] for r in rows for m in r["mappings"])
rel = collections.Counter(m["relation"] for r in rows for m in r["mappings"])

L = [
    "# Conceptual (proof-point) link manifest — REVIEW COPY (nothing applied)",
    "",
    f"*{total} candidate mappings across {witharts}/{len(rows)} articles "
    f"({grounded} grounded = anchor phrase found verbatim in the article; "
    f"{total-grounded} ungrounded, listed but not auto-applicable). "
    f"Relations: " + ", ".join(f"{k} {v}" for k, v in rel.most_common()) + ".*",
    "",
    "Model: " + (rows[0].get("model", "?") if rows else "?")
    + " on Ollama Cloud (external-model rule: candidates only, review gates apply).",
    "",
    "## Most-mapped claim pages",
    "",
]
L += [f"- `{c}` × {n}" for c, n in claims.most_common(20)]
L += ["", "---", ""]

for r in rows:
    if not r["mappings"]:
        continue
    L.append(f"### [{r['title']}]({r['url']})")
    for m in r["mappings"]:
        slug = m["claim"].split("/", 1)[1]
        flag = "" if m["grounded"] else " ⚠️ *ungrounded anchor*"
        L.append(f"- **{m['relation']}** [`{m['claim']}`](https://progress.org/wiki/{slug}/)"
                 f" — anchor: **“{m['anchor_phrase']}”**{flag}")
        if m.get("page_claim"):
            L.append(f"  - page's claim: {m['page_claim']}")
        if m.get("anchor_sentence"):
            L.append(f"  - sentence: …{m['anchor_sentence'][:240]}…")
        if m.get("why"):
            L.append(f"  - why: {m['why']}")
    L.append("")

open(OUT, "w").write("\n".join(L) + "\n")
print(f"{total} mappings / {witharts} articles -> {OUT}")
