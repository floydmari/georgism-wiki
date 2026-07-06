#!/usr/bin/env python3
"""exa_enrich.py — Exa-powered enrichment for people/ pages (stdlib only).

Usage:
  python3 scripts/exa_enrich.py "Karl Widerquist" [--context "basic income Georgist"] [--n 5]

Reads EXA_API_KEY from the environment (set it in the cloud environment's env
settings for future sessions; NEVER commit the key). Emits a structured
markdown enrichment report to stdout: top sources with URLs, publish dates,
and text extracts — raw material for a T1 editor to verify and cite. This
script REPORTS ONLY; it never edits pages (the T1 gate writes the page).

Wired into LOOP.md: every people/ page creation or backfill runs this first
when the key + network access exist; the report's facts get cited at claim
level per EDITORIAL.md (Exa is retrieval, not a source — cite what it finds).

NOTE 2026-07-06: this environment's egress proxy currently blocks api.exa.ai
(CONNECT 403). The script works from any unblocked environment (e.g. Hermes)
or once api.exa.ai is allowlisted in the network policy.
"""
import json, os, sys, urllib.request

API = "https://api.exa.ai/search"

def enrich(name, context="Georgism land value tax economist", n=5):
    key = os.environ.get("EXA_API_KEY")
    if not key:
        sys.exit("EXA_API_KEY not set (add it to the environment settings)")
    body = json.dumps({
        "query": f"{name} {context}".strip(),
        "numResults": n,
        "type": "auto",
        "contents": {"text": {"maxCharacters": 2500}},
    }).encode()
    req = urllib.request.Request(API, data=body, headers={
        "x-api-key": key, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=45) as r:
        data = json.load(r)
    print(f"# Exa enrichment report: {name}\n")
    print("REPORT-ONLY raw material — verify before citing; Exa is retrieval, not a source.\n")
    for res in data.get("results", []):
        print(f"## {res.get('title','(untitled)')}")
        print(f"- URL: {res.get('url')}")
        if res.get("publishedDate"): print(f"- published: {res['publishedDate']}")
        if res.get("author"): print(f"- author: {res['author']}")
        text = (res.get("text") or "").strip()
        if text: print(f"\n> {text[:2500]}\n")
    return 0

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args: sys.exit(__doc__)
    name = args[0]
    ctx = "Georgism land value tax economist"
    n = 5
    if "--context" in args: ctx = args[args.index("--context")+1]
    if "--n" in args: n = int(args[args.index("--n")+1])
    enrich(name, ctx, n)
