#!/usr/bin/env python3
"""Generate sources/verification-queue.md — the worked queue of every [CITATION NEEDED]
and [VERIFY] marker in the wiki, grouped by what unblocks it. Regenerate at each wave
wrap-up (LOOP.md step). Stdlib only."""
import glob, os, re, datetime

CATS = ["concepts","people","places","organizations","objections","events","outcomes","narratives","research"]
BUCKETS = [
 ("needs-owner-input", ["owner", "floyd", "supply bio"]),
 ("needs-book-copy (see sources/wanted-books.md)", ["book", "lending", "e-copy", "full text of the book"]),
 ("needs-unblocked-web (proxy allowlist or manual fetch)", ["proxy", "blocked", "fetch", "web access", "network access", "unblocked", "direct read", "primary text", "pdf"]),
 ("needs-new-source (research/forage task)", ["strongest", "study", "empirical", "academic statement", "citation for", "source for"]),
]

def bucket(text):
    t = text.lower()
    for name, keys in BUCKETS:
        if any(k in t for k in keys): return name
    return "unclassified (T1 triage)"

rows = {}
total = 0
for cat in CATS:
    for path in sorted(glob.glob(f"{cat}/*.md")):
        body = open(path, encoding="utf-8").read()
        for m in re.finditer(r"\[(CITATION NEEDED|VERIFY)[:\]]([^\]]*)\]?", body):
            kind = m.group(1)
            detail = " ".join(m.group(2).split())[:160]
            rows.setdefault(bucket(detail), []).append(f"- `{path}` — **{kind}** {detail}")
            total += 1

out = [f"# Verification Queue — every [CITATION NEEDED] / [VERIFY] marker, by unblock channel",
       f"", f"Generated {datetime.date.today()} by `scripts/verification_queue.py` ({total} markers). ",
       "Markers are the wiki's anti-fabrication firewall (EDITORIAL rule 2). Resolve by channel; ",
       "delete the marker only when the underlying fact is verified or the claim is removed.", ""]
order = [b for b,_ in BUCKETS] + ["unclassified (T1 triage)"]
for b in order:
    if b not in rows: continue
    out.append(f"## {b} ({len(rows[b])})\n")
    out.extend(rows[b]); out.append("")
open("sources/verification-queue.md","w").write("\n".join(out) + "\n")
print(f"verification-queue: {total} markers -> sources/verification-queue.md")
for b in order:
    if b in rows: print(f"  {b}: {len(rows[b])}")
