#!/usr/bin/env python3
"""
build_corpus_digest.py — emit the full-wiki corpus digest for the T0 context engine.

One line per page: category/slug <TAB> title <TAB> tags <TAB> inbound-link count
<TAB> stub flag <TAB> excerpt. A pure function of the repo (like build_inventory.py),
so it is regenerated fresh at the start of every loop wave and NOT committed — it is
an LLM input artifact, not a census. inbound_links comes from sources/wiki-inventory.csv
when present (demand signal for the T0 agent's cross-link suggestions).

Usage:
    python3 scripts/build_corpus_digest.py            # digest to stdout
    python3 scripts/build_corpus_digest.py --out F    # write to file F
    python3 scripts/build_corpus_digest.py --stats    # page/char counts to stderr too

Consumed by the T0 brief step documented in LOOP.md ("T0 — the context engine").
"""
import argparse
import csv
import glob
import os
import re
import sys

CATEGORIES = [
    "concepts", "people", "places", "events", "organizations", "objections",
    "research", "problems", "benefits", "books", "narratives", "guides", "texts",
]

FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)


def fm_field(fm: str, key: str) -> str:
    m = re.search(rf"^{key}:\s*(.+)$", fm, re.M)
    if not m:
        return ""
    val = m.group(1).strip().strip('"').strip("'")
    return val


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    ap.add_argument("--stats", action="store_true")
    args = ap.parse_args()

    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    inbound = {}
    inv = os.path.join(repo, "sources", "wiki-inventory.csv")
    if os.path.exists(inv):
        with open(inv, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                inbound[row["slug"]] = row.get("inbound_links", "")

    lines = []
    for cat in CATEGORIES:
        for path in sorted(glob.glob(os.path.join(repo, cat, "*.md"))):
            slug = os.path.splitext(os.path.basename(path))[0]
            if slug in ("index", "README"):
                continue
            with open(path, encoding="utf-8") as f:
                text = f.read()
            m = FM_RE.match(text)
            fm = m.group(1) if m else ""
            title = fm_field(fm, "title") or slug
            tags = fm_field(fm, "tags").strip("[]")
            stub = fm_field(fm, "stub") or "false"
            excerpt = fm_field(fm, "excerpt")
            lines.append(
                f"{cat}/{slug}\t{title}\t{tags}\t{inbound.get(slug, '')}\t"
                f"{'STUB' if stub == 'true' else ''}\t{excerpt}"
            )

    header = (
        f"# CORPUS DIGEST — {len(lines)} pages — "
        "columns: category/slug<TAB>title<TAB>tags<TAB>inbound_links<TAB>stub<TAB>excerpt\n"
    )
    out = header + "\n".join(lines) + "\n"
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(out)
    else:
        sys.stdout.write(out)
    if args.stats or args.out:
        print(
            f"corpus digest: {len(lines)} pages, {len(out):,} chars "
            f"(~{len(out)//4:,} tokens)",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
