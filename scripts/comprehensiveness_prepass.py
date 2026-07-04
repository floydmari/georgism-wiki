#!/usr/bin/env python3
"""Phase 0 of LOOP-COMPREHENSIVENESS.md — deterministic pre-pass over sources/registry.csv.

Emits (stdout, and preview/comprehensiveness_batches.json for the orchestrator):
  1. the sweep list: external-source rows chunked into agent batches
  2. the authors channel: repeat/Core authors lacking a people/ page
  3. under-mined flags: Status=Referenced rows and Scan Depth below Tier target

Usage: python3 scripts/comprehensiveness_prepass.py [--batch-size N] [--full]
Watermark: reads the "Comprehensiveness loop" watermark line in BACKLOG.md
(`watermark: <N> rows`) and, unless --full, sweeps only rows beyond it.
Stdlib only.
"""
import csv, json, os, re, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE_CATS = {"Concepts", "People", "Places", "Events", "Outcomes", "Objections", "Website/Org"}
NON_PERSON = {
    "various", "world bank", "imf", "unattributed [verify]", "province of british columbia",
    "imf fiscal affairs department (baer et al.)", "lincoln institute of land policy",
    "progress and poverty institute", "transparency international uk", "earthsharing australia",
    "ifs / james mirrlees et al.", "mises et al.", "kumar et al.", "kumar et al",
}


def person_slug(name: str) -> str:
    s = re.sub(r"\(eds?\.\)", "", name).strip()
    s = re.sub(r"[^a-zA-Z\- ]", "", s).lower().strip()
    return re.sub(r"\s+", "-", s)


def main() -> None:
    batch_size = 11
    full = "--full" in sys.argv
    if "--batch-size" in sys.argv:
        batch_size = int(sys.argv[sys.argv.index("--batch-size") + 1])

    rows = list(csv.DictReader(open(os.path.join(ROOT, "sources/registry.csv"))))
    ext = [r for r in rows if (r["Category"] or "").strip() not in PAGE_CATS]

    watermark = 0
    backlog = open(os.path.join(ROOT, "BACKLOG.md")).read()
    m = re.search(r"comprehensiveness watermark: (\d+) external-source rows", backlog)
    if m and not full:
        watermark = int(m.group(1))
    sweep = ext[watermark:] if watermark else ext

    # authors channel
    people = {f[:-3] for f in os.listdir(os.path.join(ROOT, "people"))}
    authors = collections.Counter()
    tiers = collections.defaultdict(set)
    titles = collections.defaultdict(list)
    for r in ext:  # authors channel always looks at the FULL registry
        for a in (r["Author(s)"] or "").split(";"):
            a = re.sub(r"\(eds?\.\)", "", a).strip()
            if not a or a.lower() in NON_PERSON:
                continue
            authors[a] += 1
            tiers[a].add((r["Tier"] or "").strip().lower())
            titles[a].append(r["Title"])

    def has_page(name: str) -> bool:
        sl = person_slug(name)
        if sl in people:
            return True
        parts = sl.split("-")
        if len(parts) < 2:
            return False
        last, first_initial = parts[-1], parts[0][:1]
        return any(
            p.split("-")[-1] == last and p.split("-")[0][:1] == first_initial for p in people
        )

    author_candidates = [
        {"name": a, "sources": c, "tiers": sorted(tiers[a]), "titles": titles[a]}
        for a, c in authors.most_common()
        if not has_page(a) and (c >= 2 or "core" in tiers[a])
    ]

    # under-mined flags
    target = {"core": 3, "important": 2, "supplementary": 1}   # heavy=3 medium=2 light=1
    depth = {"heavy": 3, "medium": 2, "light": 1, "—": 0, "": 0}
    under = []
    for r in ext:
        t = (r["Tier"] or "").strip().lower()
        d = (r["Scan Depth"] or "").strip().lower()
        if (r["Status"] or "").strip().lower() == "referenced":
            under.append({"title": r["Title"], "why": "Status=Referenced (never scanned)"})
        elif t in target and depth.get(d, 0) < target[t]:
            under.append({"title": r["Title"], "why": f"Scan Depth {d or 'none'} < {t} target"})

    batches = [sweep[i : i + batch_size] for i in range(0, len(sweep), batch_size)]
    out = {
        "external_rows_total": len(ext),
        "watermark_used": watermark,
        "sweep_count": len(sweep),
        "batches": [
            [
                {k: r[k] for k in ("Title", "Author(s)", "Year", "Tier", "URL", "Wiki Page")}
                for r in b
            ]
            for b in batches
        ],
        "author_candidates": author_candidates,
        "under_mined": under,
    }
    os.makedirs(os.path.join(ROOT, "preview"), exist_ok=True)
    dest = os.path.join(ROOT, "preview/comprehensiveness_batches.json")
    json.dump(out, open(dest, "w"), indent=1)
    print(
        f"comprehensiveness_prepass: {len(ext)} external rows, watermark {watermark}, "
        f"sweeping {len(sweep)} in {len(batches)} batches of ~{batch_size} -> {dest}"
    )
    print(f"author candidates (no people page, >=2 sources or Core): {len(author_candidates)}")
    for a in author_candidates:
        print(f"  - {a['name']} ({a['sources']} sources, {a['tiers']})")
    print(f"under-mined sources: {len(under)}")


if __name__ == "__main__":
    main()
