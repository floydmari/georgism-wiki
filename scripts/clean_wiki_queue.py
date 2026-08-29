#!/usr/bin/env python3
"""
clean_wiki_queue.py — drop scanner-resurrected items from sources/wiki-queue.json.

The daily scan's triage sometimes re-emits URLs the loop has already dispositioned.
Per the loop's never-resurrect rule, such items are dropped from the pending queue
without touching the ledger — an item that was already dispositioned keeps its
original disposition. Three distinct same-content-different-URL patterns have
recurred often enough to be worth catching automatically rather than by ad hoc
per-session Python (each discovered the hard way, across many loop passes):

  1. Exact URL match against the consumed ledger (the original, simplest case).
  2. Mirror/slug match — same /p/<slug> path published under two domains, notably
     progressandpoverty.substack.com migrating to blog.landeconomics.org in 2026-08;
     the scanner's own dedup can't see across the domain change.
  3. DOI match, normalized across URL formats — the same DOI reached via
     doi.org/<doi>, an NBER paper via 10.3386/wNNNNN vs nber.org/papers/wNNNNN, or a
     publisher's own /doi/<doi> path (e.g. journals.sagepub.com/doi/<doi> vs the
     doi.org redirect) all denote the same underlying paper even though the URL
     strings differ completely.

Run after every union-merge of a scanner commit:
    python3 scripts/clean_wiki_queue.py

Idempotent; prints what it dropped. The real fix belongs scanner-side (its dedup
should read the consumed ledger and normalize DOIs); this guard just makes the
leak harmless in the meantime.
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUEUE = os.path.join(ROOT, "sources", "wiki-queue.json")

SLUG_RE = re.compile(r"/p/([a-z0-9-]+)")
NBER_RES = [re.compile(r"10\.3386/(w\d+)"), re.compile(r"nber\.org/papers/(w\d+)")]
DOI_RES = [
    re.compile(r"doi\.org/(10\.\d{4,9}/\S+)", re.I),
    re.compile(r"/doi/(?:abs/|full/|pdf/)?(10\.\d{4,9}/\S+)", re.I),
    re.compile(r"identifierValue=(10\.\d{4,9}/\S+?)(?:&|$)", re.I),
]


def _clean_doi(doi: str) -> str:
    # strip trailing punctuation/query fragments picked up by a greedy URL match
    return doi.strip().rstrip("/").split("?")[0].split("#")[0].lower()


def slug_key(url: str):
    m = SLUG_RE.search(url)
    return m.group(1) if m else None


def nber_key(url: str):
    for pat in NBER_RES:
        m = pat.search(url)
        if m:
            return m.group(1).lower()
    return None


def doi_key(url: str):
    for pat in DOI_RES:
        m = pat.search(url)
        if m:
            return _clean_doi(m.group(1))
    return None


def main():
    with open(QUEUE) as f:
        q = json.load(f)
    consumed = q.get("consumed", [])
    consumed_urls = {it.get("url", "") for it in consumed}
    consumed_slugs = {slug_key(u) for u in consumed_urls if slug_key(u)}
    consumed_nber = {nber_key(u) for u in consumed_urls if nber_key(u)}
    consumed_dois = {doi_key(u) for u in consumed_urls if doi_key(u)}

    kept, dropped = [], []
    for it in q.get("queue", []):
        u = it.get("url", "")
        reason = None
        if u in consumed_urls:
            reason = "exact URL"
        elif slug_key(u) and slug_key(u) in consumed_slugs:
            reason = f"mirror slug '{slug_key(u)}'"
        elif nber_key(u) and nber_key(u) in consumed_nber:
            reason = f"NBER id '{nber_key(u)}'"
        elif doi_key(u) and doi_key(u) in consumed_dois:
            reason = f"DOI '{doi_key(u)}'"
        (dropped if reason else kept).append((it, reason))

    if dropped:
        q["queue"] = kept_items = [it for it, _ in kept]
        with open(QUEUE, "w") as f:
            json.dump(q, f, indent=2, ensure_ascii=False)
            f.write("\n")
        for it, reason in dropped:
            print(f"dropped resurrected ({reason}): {it.get('url','')}")
    else:
        kept_items = [it for it, _ in kept]
    print(f"queue: {len(kept_items)} pending, {len(consumed)} consumed, "
          f"{len(dropped)} resurrected item(s) dropped")


if __name__ == "__main__":
    main()
