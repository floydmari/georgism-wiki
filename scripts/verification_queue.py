#!/usr/bin/env python3
"""Generate the Fact-Check Desk's two ledgers (stdlib only; LOOP.md step 6):

  sources/verification-queue.md  — every [CITATION NEEDED]/[VERIFY] flag on the wiki,
                                   grouped by WHO can resolve it (the full ledger)
  sources/hermes-workorder.md    — the ready-to-work order for Hermes's next run:
                                   the web-blocked and book-copy items in actionable
                                   form, capped and prioritized (the field assignment)

Every unverified claim on the wiki is an open fact-check with an owner. This script is
how routing happens — regenerate it whenever markers change."""
import glob, os, re, datetime

CATS = ["concepts","people","places","organizations","objections","events","problems","benefits","narratives","research","books"]
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

# ---- Hermes work order: the routed field assignment (gap-1 machinery, 2026-07-06) ----
CAP = 60   # one overnight run's worth; regenerate after each Hermes PR merges
hermes_buckets = [b for b in order if b.startswith("needs-book-copy") or b.startswith("needs-unblocked-web")]
wo = ["# Hermes Work Order — Fact-Check Desk field assignment",
      "",
      f"Generated {datetime.date.today()} by `scripts/verification_queue.py`. This is the",
      "routed slice of the verification queue that ONLY Hermes's environment can work",
      "(unblocked web + Floyd's book library). Protocol: `sources/inbox/README.md` —",
      "verbatim quotes with locators, CONFIRMED/CORRECTED/NOT-FOUND verdicts, legal",
      "provenance only, PR to a hermes/* branch, never self-merged.",
      "",
      f"Capped at {CAP} items per run; the full ledger is `sources/verification-queue.md`.",
      ""]
n = 0
for b in hermes_buckets:
    items = rows.get(b, [])
    if not items: continue
    take = items[:max(0, CAP - n)]
    if not take: break
    wo.append(f"## {b} — {len(take)} of {len(items)}\n")
    wo.extend(take); wo.append("")
    n += len(take)
wo.append(f"\n*{n} items assigned this order. When a page's flags are all resolved, note it "
          "in the PR so the editor can upgrade its scan depth.*")
open("sources/hermes-workorder.md","w").write("\n".join(wo) + "\n")
print(f"hermes-workorder: {n} items -> sources/hermes-workorder.md")
