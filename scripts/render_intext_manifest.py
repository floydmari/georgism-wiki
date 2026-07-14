#!/usr/bin/env python3
"""
render_intext_manifest.py — Option 2, stage 3. Merge the Haiku-pruned chunks against the
raw manifest (source of truth for phrase/target/sentence) and render the ONE reviewable
Markdown manifest Floyd asked for: every proposed in-text link, grouped by article, as
    article  ->  linked words  ->  wiki page
NOTHING is applied to Ghost by this script. Approval of the rendered manifest is the gate.

Inputs:  scratchpad/cache/intext_manifest.json, scratchpad/cache/pruned/chunk-*.json
Outputs: scratchpad/cache/intext_pruned_merged.json   (machine-readable, for the apply step)
         scratchpad/intext-link-manifest.md           (human review copy, committed)
"""
import collections, glob, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "scratchpad", "cache")

raw = {a["slug"]: a for a in json.load(open(os.path.join(CACHE, "intext_manifest.json")))}
rawidx = {}
for a in raw.values():
    for c in a["candidates"]:
        rawidx[(a["slug"], c["matched"].lower(), c["target"])] = c
        rawidx[(a["slug"], c["phrase"].lower(), c["target"])] = c

kept = collections.defaultdict(list)
drops, dropwhy, anomalies, seen = 0, collections.Counter(), 0, set()
for f in sorted(glob.glob(os.path.join(CACHE, "pruned", "chunk-*.json"))):
    for art in json.load(open(f)):
        slug = art["slug"]; seen.add(slug)
        for k in art.get("keep", []):
            key = (slug, k["phrase"].lower(), k["target"])
            if key in rawidx:
                c = rawidx[key]
                if not any(x["target"] == c["target"] for x in kept[slug]):
                    kept[slug].append(c)
            else:
                anomalies += 1          # agent invented a candidate — discard
        for d in art.get("dropped", []):
            drops += 1; dropwhy[d.get("why", "?")] += 1

json.dump(dict(kept), open(os.path.join(CACHE, "intext_pruned_merged.json"), "w"), indent=1)

nlinks = sum(len(v) for v in kept.values())
narts = sum(1 for v in kept.values() if v)
tgt = collections.Counter(c["target"] for v in kept.values() for c in v)

lines = [
    "# In-text wiki-link manifest — REVIEW COPY (nothing applied)",
    "",
    f"*Generated from {len(seen)} scanned articles; {nlinks} proposed links across {narts} articles.*",
    f"*Pruning dropped {drops} raw candidates: " +
    ", ".join(f"{w} {n}" for w, n in dropwhy.most_common()) +
    f". {anomalies} malformed agent entries discarded.*",
    "",
    "Approve, strike lines, or annotate — nothing is applied to any article until sign-off.",
    "Existing `/wiki/` links in each article were excluded up front (no double-linking).",
    "",
    "## Most-proposed wiki targets",
    "",
]
lines += [f"- `{t}` × {n}" for t, n in tgt.most_common(15)]
lines += ["", "---", ""]

# stable order: by article publish date (newest first), then slug
def pub(slug):
    return raw[slug].get("published_at") or ""
for slug in sorted(kept, key=lambda s: (pub(s), s), reverse=True):
    cands = kept[slug]
    if not cands:
        continue
    a = raw[slug]
    date = (a.get("published_at") or "")[:10]
    lines.append(f"### [{a['title']}]({a['url']})  ·  {date}")
    for c in cands:
        lines.append(f"- **“{c['matched']}”** → [/wiki/{c['target'].split('/',1)[1]}/]"
                     f"(https://progress.org/wiki/{c['target'].split('/',1)[1]}/) — {c['wiki_title']}")
        lines.append(f"  - context: …{c['sentence'][:220]}…")
    lines.append("")

out = os.path.join(ROOT, "scratchpad", "intext-link-manifest.md")
open(out, "w").write("\n".join(lines) + "\n")
print(f"{nlinks} links / {narts} articles -> {out}")
