#!/usr/bin/env python3
"""
build_figure_queue.py — the deterministic pre-pass for the figure-sourcing loop
(LOOP-FIGURES.md). Scans the corpus and writes sources/figure-queue.md: a scored,
prioritized queue of wiki entries whose source paper likely carries a load-bearing
chart worth embedding under EDITORIAL §3c.

What it does (no LLM, no network by default — pure corpus arithmetic):

  1. Scans research/ and books/ entries (the pages ABOUT sources — §3c says the
     figure's canonical home is the entry about the paper that published it).
  2. Skips entries that already embed a <figure> or are in scripts/source_figures.py's
     FIGURES manifest.
  3. Scores each remaining entry on structural proxies for "the chart matters here":
       tier            core=3, important=2, else=1   (editorial weight)
       outcomes        +1 per supports_outcomes/bears_on_objections link, capped at 4
                       (evidence-bearing entries have findings a chart can carry)
       inbound         +1 per 3 inbound /wiki/ links from the rest of the corpus,
                       capped at 4 (how much the wiki leans on this page)
       most-cited      +1
       pdf             +2 if source_url looks like an open, directly fetchable PDF;
                       +1 if it's a known open-access host (abstract page, PDF one
                       hop away); 0 if paywalled/DOI-only/book — those need a
                       working-paper mirror first (note says so)
  4. Emits sources/figure-queue.md sorted by score, with a worked-status checkbox
     column the loop stamps as it goes, plus a second section listing re-embed
     placement candidates: outcome/problem/benefit pages wired (via
     supports_outcomes) to entries that already carry a hosted figure.

With --check-urls it additionally HEADs each candidate's source_url (10s timeout)
and records reachability + content-type — slower, network-dependent, run it when
refreshing the queue for a real shift.

Usage:
    python3 scripts/build_figure_queue.py               # rebuild the queue
    python3 scripts/build_figure_queue.py --check-urls  # + verify PDF reachability
    python3 scripts/build_figure_queue.py --top 25      # limit queue length (default 40)
"""
import os, re, sys, glob

import frontmatter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "sources", "figure-queue.md")

# folders whose pages are ABOUT sources — canonical homes for source figures (§3c)
SOURCE_FOLDERS = ["research", "books"]
# folders scanned for inbound links and for re-embed placement candidates
ALL_FOLDERS = ["concepts", "people", "places", "events", "problems", "benefits",
               "research", "organizations", "objections", "narratives", "books",
               "guides", "texts"]

OPEN_PDF_HINTS = (".pdf",)
OPEN_HOST_HINTS = ("nber.org", "hal.science", "arxiv.org", "ssrn.com", "cesifo",
                   "brookings", "archive.org", ".gov", "bea.gov", "oecd.org",
                   "imf.org", "worldbank.org", "bankofengland", "bundesbank",
                   "dallasfed", "github.io", "core.ac.uk", "repec", "econstor",
                   "lincolninst", "gutenberg.org")
PAYWALL_HINTS = ("doi.org", "jstor.org", "sciencedirect", "academic.oup",
                 "journals.uchicago", "tandfonline", "wiley.com", "springer",
                 "aeaweb.org/articles", "amazon.", "goodreads.")


def manifest_keys():
    """Entries already covered by scripts/source_figures.py's FIGURES manifest."""
    src = open(os.path.join(ROOT, "scripts", "source_figures.py")).read()
    return set(re.findall(r'"entry":\s*"([^"]+)"', src))


def load(folder):
    for path in sorted(glob.glob(os.path.join(ROOT, folder, "*.md"))):
        if os.path.basename(path).startswith("_"):
            continue
        try:
            fm = frontmatter.load(path)
        except Exception:
            continue
        yield os.path.relpath(path, ROOT), fm


def pdf_class(url):
    """(points, label) for how gettable the source PDF looks."""
    if not url:
        return 0, "no source_url"
    u = url.lower()
    if any(u.endswith(h) or (h in u and "download" in u) for h in OPEN_PDF_HINTS) \
       or ".pdf" in u:
        return 2, "direct PDF"
    if any(h in u for h in PAYWALL_HINTS):
        return 0, "paywalled/DOI — needs WP mirror"
    if any(h in u for h in OPEN_HOST_HINTS):
        return 1, "open host"
    return 0, "unknown host"


def main():
    top_n = 40
    if "--top" in sys.argv:
        top_n = int(sys.argv[sys.argv.index("--top") + 1])
    check_urls = "--check-urls" in sys.argv

    # carry non-todo stamps (no-chart, blocked:*, in-progress:*) across regenerations —
    # a stamp is a finding; regenerating the queue must never wipe it. `done` needs no
    # carrying: done entries embed a <figure> and drop out of the candidate set.
    carried = {}
    if os.path.exists(OUT):
        for m in re.finditer(r"^\|\s*\d+\s*\|\s*\[([^\]]+)\][^|]*\|(?:[^|]*\|){5}\s*([^|]+?)\s*\|\s*$",
                             open(OUT).read(), re.M):
            slug, status = m.group(1), m.group(2)
            if status != "todo":
                carried[slug] = status
        for m in re.finditer(r"^- `([^`]+)` — (no-chart|blocked:\S+)(?:\s+·\s+(.*))?$",
                             open(OUT).read(), re.M):
            carried[m.group(1)] = m.group(2) + (f" · {m.group(3)}" if m.group(3) else "")

    covered = manifest_keys()
    pages = {}          # relpath -> frontmatter post
    bodies = {}         # relpath -> body text
    for folder in ALL_FOLDERS:
        for rel, fm in load(folder):
            pages[rel] = fm
            bodies[rel] = fm.content

    # inbound link counts, by slug
    inbound = {}
    for rel in pages:
        slug = os.path.splitext(os.path.basename(rel))[0]
        pat = re.compile(r"/wiki/" + re.escape(slug) + r"/")
        inbound[slug] = sum(1 for other, body in bodies.items()
                            if other != rel and pat.search(body))

    candidates, has_figure = [], []
    for rel, fm in pages.items():
        folder = rel.split("/")[0]
        if folder not in SOURCE_FOLDERS:
            continue
        slug = os.path.splitext(os.path.basename(rel))[0]
        if "<figure" in fm.content or rel in covered:
            has_figure.append(rel)
            continue
        if fm.get("stub"):
            continue
        url = fm.get("source_url", "") or ""
        pdf_pts, pdf_note = pdf_class(url)
        tier = {"core": 3, "important": 2}.get(fm.get("tier"), 1)
        outcomes = (len(fm.get("supports_outcomes") or [])
                    + len(fm.get("bears_on_objections") or []))
        score = (tier
                 + min(outcomes, 4)
                 + min(inbound.get(slug, 0) // 3, 4)
                 + (1 if fm.get("most_cited") or "most-cited" in (fm.get("tags") or []) else 0)
                 + pdf_pts)
        candidates.append({
            "rel": rel, "slug": slug, "title": fm.get("title", slug),
            "tier": fm.get("tier", "-"), "outcomes": outcomes,
            "inbound": inbound.get(slug, 0), "url": url,
            "pdf_note": pdf_note, "score": score,
        })

    # split off stamped entries (no-chart / blocked) — they leave the queue but stay
    # recorded so the loop never re-fetches them
    stamped = [(c["slug"], carried[c["slug"]]) for c in candidates
               if carried.get(c["slug"], "todo") not in ("todo",)
               and not carried.get(c["slug"], "").startswith("in-progress")]
    stamped_slugs = {s for s, _ in stamped}
    candidates = [c for c in candidates if c["slug"] not in stamped_slugs]

    candidates.sort(key=lambda c: (-c["score"], c["rel"]))
    queue = candidates[:top_n]
    for c in queue:
        c["status"] = carried.get(c["slug"], "todo")

    if check_urls:
        import requests
        for c in queue:
            if not c["url"]:
                continue
            try:
                r = requests.head(c["url"], timeout=10, allow_redirects=True,
                                  headers={"User-Agent": "georgism-wiki-figure-queue"})
                ct = r.headers.get("content-type", "?").split(";")[0]
                c["pdf_note"] += f" · HEAD {r.status_code} {ct}"
            except Exception as e:
                c["pdf_note"] += f" · HEAD failed ({type(e).__name__})"

    # placements evaluated by a T1 shift and rejected — the chart does not carry that
    # page's headline claim (LOOP-FIGURES step 7). Keyed (target page, source slug).
    REJECTED_PLACEMENTS = {
        ("benefits/rent-dividends-reduce-poverty.md", "jones-marinescu-alaska-pfd"):
            "employment chart ≠ the poverty-reduction claim (wave 6)",
        ("benefits/lvt-can-replace-capital-taxes-without-efficiency-loss.md",
         "bonnet-land-is-back"):
            "Fig 1 shows wealth ratios, not the efficiency-swap result (wave 6)",
        ("benefits/lvt-improves-housing-affordability.md", "glaeser-gyourko-housing-supply"):
            "regulation price-cost gap ≠ the LVT-affordability claim (wave 9)",
        ("problems/speculative-vacancy-wastes-cities.md", "hoyt-chicago-land-values"):
            "century cycles ≠ vacancy claim (wave 9)",
        ("problems/speculative-vacancy-wastes-cities.md", "gyourko-krimmel-zoning-tax"):
            "zoning tax ≠ vacancy claim (wave 9)",
        ("benefits/lvt-dampens-land-speculation.md", "hoyt-chicago-land-values"):
            "cycle history ≠ LVT-dampens-speculation claim (wave 9)",
        ("benefits/lvt-dampens-land-speculation.md", "dors-land-taxes-housing-prices"):
            "capitalization evidence ≠ speculation-dampening claim (wave 9)",
        ("benefits/land-value-tax-can-be-progressive.md", "bonnet-land-is-back"):
            "aggregate wealth ratios ≠ ownership-distribution claim (wave 10)",
        ("benefits/land-value-tax-can-be-progressive.md", "rognlie-capital-share"):
            "income-share decomposition ≠ ownership-distribution claim (wave 10)",
        ("problems/young-locked-out-of-land-wealth.md",
         "knoll-schularick-steger-house-prices"):
            "land-price series is the premise, not the generational claim (wave 10)",
    }

    # re-embed placement candidates: evidence pages wired to figure-bearing entries
    placements = []
    for rel in sorted(has_figure):
        fm = pages[rel]
        fig_slug = os.path.splitext(os.path.basename(rel))[0]
        for out_slug in (fm.get("supports_outcomes") or []):
            for f in ("outcomes", "problems", "benefits"):
                target = f"{f}/{out_slug}.md"
                if (target in pages and "<figure" not in bodies[target]
                        and (target, fig_slug) not in REJECTED_PLACEMENTS):
                    placements.append((target, fig_slug))

    lines = [
        "# Figure queue — candidates for the figure-sourcing loop",
        "",
        f"*Generated by `scripts/build_figure_queue.py` — do not hand-edit rows except the",
        f"status column. Regenerate after each merged figure wave. Queue shows top {top_n}",
        f"of {len(candidates)} open candidates; {len(has_figure)} entries already carry a figure.*",
        "",
        "Statuses: `todo` · `in-progress:<branch>` · `done` · `no-chart` (paper has no",
        "load-bearing figure — stamp it so the loop never re-fetches) · `blocked:<why>`.",
        "",
        "## Queue (§3c bar: the chart must carry the entry's headline finding)",
        "",
        "| # | Entry | Tier | Score | Inbound | Outcomes | PDF access | Status |",
        "|---|-------|------|-------|---------|----------|------------|--------|",
    ]
    for i, c in enumerate(queue, 1):
        lines.append(
            f"| {i} | [{c['slug']}]({c['rel']}) | {c['tier']} | {c['score']} "
            f"| {c['inbound']} | {c['outcomes']} | {c['pdf_note']} | {c.get('status', 'todo')} |")
    lines += [
        "",
        "## Stamped — out of the queue, never re-fetched",
        "",
        "One line per entry: `- \\`slug\\` — no-chart · reason` or `blocked:<why>`.",
        "Stamps survive regeneration; delete a line to re-queue an entry.",
        "",
    ]
    for slug, status in sorted(stamped):
        lines.append(f"- `{slug}` — {status}")
    if not stamped:
        lines.append("*(none yet)*")
    lines += [
        "",
        "## Re-embed placement candidates (figure already hosted; §3c re-embed rule)",
        "",
        "Evidence pages wired to a figure-bearing source entry that do not yet show a",
        "figure themselves. Re-embed only where the chart directly evidences the page's",
        "headline claim; same caption + credit, link back to the source entry.",
        "",
    ]
    if placements:
        for target, fig_slug in sorted(set(placements)):
            lines.append(f"- [ ] `{target}` ← figure from `{fig_slug}`")
    else:
        lines.append("*(none right now)*")
    lines.append("")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        f.write("\n".join(lines))
    print(f"wrote {os.path.relpath(OUT, ROOT)}: {len(queue)} queued "
          f"({len(candidates)} candidates, {len(has_figure)} already figured, "
          f"{len(set(placements))} re-embed candidates)")


if __name__ == "__main__":
    main()
