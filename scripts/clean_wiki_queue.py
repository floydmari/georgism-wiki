#!/usr/bin/env python3
"""
clean_wiki_queue.py — drop scanner-resurrected items from sources/wiki-queue.json.

The daily scan's triage sometimes re-emits URLs the loop has already dispositioned
(exact matches against the consumed ledger; recurring since 2026-08-01 with two
progressandpoverty.substack.com items). Per the loop's never-resurrect rule, such
items are dropped from the pending queue without touching the ledger — an item that
was already dispositioned keeps its original disposition.

Run after every union-merge of a scanner commit:
    python3 scripts/clean_wiki_queue.py

Idempotent; prints what it dropped. The real fix belongs scanner-side (its dedup
should read the consumed ledger); this guard just makes the leak harmless.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUEUE = os.path.join(ROOT, "sources", "wiki-queue.json")


def main():
    with open(QUEUE) as f:
        q = json.load(f)
    consumed_urls = {it.get("url", "") for it in q.get("consumed", [])}
    kept, dropped = [], []
    for it in q.get("queue", []):
        (dropped if it.get("url", "") in consumed_urls else kept).append(it)
    if dropped:
        q["queue"] = kept
        with open(QUEUE, "w") as f:
            json.dump(q, f, indent=2, ensure_ascii=False)
        for it in dropped:
            print(f"dropped resurrected: {it.get('url','')}")
    print(f"queue: {len(kept)} pending, {len(q.get('consumed', []))} consumed, "
          f"{len(dropped)} resurrected item(s) dropped")


if __name__ == "__main__":
    main()
