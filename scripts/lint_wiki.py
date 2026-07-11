#!/usr/bin/env python3
"""
lint_wiki.py — mechanical quality gate for the Georgism wiki.

Zero external dependencies (standard library only) so it runs in any environment and any
model's loop can invoke it. It parses YAML frontmatter with a small purpose-built reader —
it does NOT need PyYAML.

Exit code 0 = clean (warnings allowed). Exit code 1 = errors (blocks publish).

Checks (errors unless noted):
  * frontmatter present + parseable; required fields per category
  * category field matches folder
  * internal /wiki/<slug>/ links resolve to a real .md file
  * duplicate slugs across folders (slugs are global in Ghost)
  * research: source_url + year present
  * problems/benefits: evidence_strength + claim_type + supported_by present, slugs resolve
  * bidirectional integrity: supported_by <-> supports_outcomes,
    challenged_by (research must exist), related_people/related_places resolve
  * every source referenced in frontmatter (sources/supported_by/challenged_by) whose id is a
    research slug exists; every research page appears in sources/registry.csv (warning)
  * registry<->repo: every registry row whose Wiki Page is /wiki/<slug>/ has a matching .md
    (ERROR) — catches drift like the Common Wealth Canada cluster
  * objections: required sections present (The Objection / a Response / Net Assessment / Sources)
  * WS8: banned-certainty words (warning), [CITATION NEEDED]/[VERIFY] marker counts (warning),
    annotated Sources section present (warning), thin articles < 30 lines (warning)
  * orphans: pages linked from nowhere (warning)

Usage:  python3 scripts/lint_wiki.py [--strict]
        --strict promotes warnings to errors.
"""
import os, re, sys, csv, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATEGORIES = ["concepts", "people", "places", "events", "problems", "benefits",
              "research", "organizations", "objections", "narratives", "books", "texts"]
REGISTRY = os.path.join(ROOT, "sources", "registry.csv")

BANNED = [r"\bproves\b", r"\balways\b", r"\ball taxes\b", r"\bthe only\b",
          r"\bthere is no evidence\b", r"\bclearly\b", r"\bundeniable\b",
          r"\beveryone agrees\b"]

errors, warnings = [], []
def err(f, m): errors.append(f"ERROR  {f}: {m}")
def warn(f, m): warnings.append(f"WARN   {f}: {m}")


def parse_frontmatter(text):
    """Return (meta_dict, body). Minimal YAML: scalars and [a, b] / bullet lists."""
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    raw = text[3:end].strip("\n")
    body = text[end + 4:]
    meta, key = {}, None
    for line in raw.split("\n"):
        if not line.strip() or line.strip().startswith("#"):
            continue
        if re.match(r"^\s*-\s+", line) and key:            # bullet list item
            meta.setdefault(key, [])
            if isinstance(meta[key], list):
                meta[key].append(_scalar(re.sub(r"^\s*-\s+", "", line)))
            continue
        m = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val == "":
            meta[key] = []                                 # maybe a bullet list follows
        elif val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            meta[key] = [_scalar(x) for x in _split_list(inner)] if inner else []
        else:
            meta[key] = _scalar(val)
    return meta, body


def _split_list(s):
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch == "," and depth == 0:
            out.append(cur); cur = ""
        else:
            if ch in "[{": depth += 1
            elif ch in "]}": depth -= 1
            cur += ch
    if cur.strip():
        out.append(cur)
    return out


def _scalar(v):
    v = v.strip()
    if len(v) >= 2 and v[0] in "\"'" and v[-1] == v[0]:
        v = v[1:-1]
    if v.lower() in ("true", "false"):
        return v.lower() == "true"
    return v


def load_all():
    pages = {}   # slug -> dict(path, folder, meta, body, text, slug)
    for cat in CATEGORIES:
        for path in glob.glob(os.path.join(ROOT, cat, "*.md")):
            slug = os.path.splitext(os.path.basename(path))[0]
            if slug.startswith("_"):
                continue                       # _-prefixed = internal design doc, not an article
            text = open(path, encoding="utf-8").read()
            meta, body = parse_frontmatter(text)
            rel = os.path.relpath(path, ROOT)
            if meta is None:
                err(rel, "missing or unparseable frontmatter")
                meta, body = {}, text
            if slug in pages:
                err(rel, f"duplicate slug also at {pages[slug]['path']}")
            pages[slug] = dict(path=rel, folder=cat, meta=meta, body=body,
                               text=text, slug=slug)
    return pages


def aslist(v):
    if v is None: return []
    return v if isinstance(v, list) else [v]


INVENTORY = os.path.join(ROOT, "sources", "wiki-inventory.csv")


def _read_csv(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def load_sources():
    """sources/registry.csv — external works only (the regeneration input set)."""
    if not os.path.exists(REGISTRY):
        warn("sources/registry.csv", "not found — source-registry checks skipped")
    return _read_csv(REGISTRY)


def load_registry():
    """The logical registry for drift/duplicate/link checks = sources only.
    sources/wiki-inventory.csv is a separate, regenerated page census (built by
    scripts/build_inventory.py) — a pure function of the repo, not a source list,
    so it is not consulted for source checks. See sources/README.md."""
    return load_sources()


# synthesis page types the wiki AUTHORS (not external sources). A row like this
# with no URL in registry.csv is the wiki citing itself — it belongs in the page
# census, never the sources file. (Guards against the hybrid drift Floyd flagged.)
SYNTHESIS_CATS = {"Concepts", "Outcomes", "Problems", "Benefits", "Objections", "People", "Places",
                  "Events", "Narratives"}


def main():
    strict = "--strict" in sys.argv
    pages = load_all()
    slugs = set(pages)
    registry = load_registry()

    # link graph for orphan detection
    linked_to = set()
    link_re = re.compile(r"/wiki/([a-z0-9\-]+)/")

    for slug, p in pages.items():
        f, meta, body = p["path"], p["meta"], p["body"]

        # required core fields
        for req in ("title", "category", "tags", "stub", "excerpt"):
            if req == "excerpt" and p["folder"] in ("concepts", "people", "places",
                                                    "events", "organizations", "research"):
                # excerpt strongly recommended but legacy pages may omit it
                if "excerpt" not in meta:
                    warn(f, "missing excerpt")
                continue
            if req not in meta:
                err(f, f"missing required frontmatter field: {req}")

        if meta.get("category") and meta["category"] != p["folder"]:
            err(f, f"category '{meta.get('category')}' != folder '{p['folder']}'")

        # internal links resolve
        for target in link_re.findall(p["text"]):
            linked_to.add(target)
            if target != slug and target not in slugs:
                # allow known live-but-not-in-git during transition only if in registry
                in_reg = any((r.get("Wiki Page") or "").rstrip("/").endswith("/" + target)
                             for r in registry)
                (warn if in_reg else err)(
                    f, f"internal link to /wiki/{target}/ has no matching .md"
                    + (" (present in registry — drift)" if in_reg else ""))

        # category-specific
        if p["folder"] == "research":
            if not meta.get("source_url"): warn(f, "research missing source_url")
            if not meta.get("year"): warn(f, "research missing year")
            for oc in aslist(meta.get("supports_outcomes")):
                if oc not in slugs: err(f, f"supports_outcomes -> unknown page '{oc}'")

        if p["folder"] in ("problems", "benefits"):
            if not meta.get("evidence_strength"): err(f, "claim page missing evidence_strength")
            # problems/ = the diagnosis (empirical claims about the world); benefits/ =
            # measured policy effects (Floyd's split, executed 2026-07-10 — see
            # PLAN-problems-and-benefits.md and EDITORIAL §5b). claim_type must match
            # the folder; the field name supports_outcomes is kept for continuity.
            expected = "problem" if p["folder"] == "problems" else "benefit"
            if meta.get("claim_type") != expected:
                err(f, f"claim_type must be '{expected}' in {p['folder']}/")
            if not aslist(meta.get("supported_by")): warn(f, "outcome has no supported_by")
            for r in aslist(meta.get("supported_by")):
                if r not in slugs:
                    err(f, f"supported_by -> unknown research '{r}'")
                elif slug not in aslist(pages[r]["meta"].get("supports_outcomes")):
                    warn(f, f"bidirectional gap: {r} lacks supports_outcomes: [{slug}]")
            for r in aslist(meta.get("challenged_by")):
                if r not in slugs: err(f, f"challenged_by -> unknown research '{r}'")
            # BODY-PARITY (added 2026-07-05, Floyd's rule): every evidence slug wired in
            # frontmatter must actually be discussed/linked in the page body. Frontmatter
            # feeds the COVERAGE gauge; a page whose body doesn't walk through its own
            # evidence is a drift bug (the "Doucet-only body" failure mode).
            unwalked = [r for r in (aslist(meta.get("supported_by")) + aslist(meta.get("challenged_by")))
                        if r in slugs and f"/wiki/{r}/" not in p["body"]]
            if unwalked:
                warn(f, "BODY-PARITY: frontmatter evidence not cited in body: " + ", ".join(unwalked))

        for rel_key in ("related_people", "related_places"):
            for t in aslist(meta.get(rel_key)):
                if t not in slugs: err(f, f"{rel_key} -> unknown page '{t}'")

        if p["folder"] == "objections":
            for section in ("## The Objection", "## Net Assessment", "## Sources"):
                if section not in body: err(f, f"objection missing section '{section}'")
            if "## The Response" not in body:
                err(f, "objection missing a Response section")

        # mechanical integrity (added 2026-07-06 — each of these shipped to main at least
        # once before the check existed)
        if re.search(r"^(<<<<<<< |>>>>>>> |=======$)", p["text"], re.M):
            err(f, "committed merge-conflict markers")
        if re.search(r"\[\[[^\]]+\]\]", body):
            err(f, "Obsidian-style [[wikilink]] — use [text](/wiki/slug/) markdown links")
        for q in ([] if meta.get("public_domain") is True else re.findall(r'"([^"\n]{200,}?)"', body)):
            # skip likely between-quote spans: real quotations rarely carry markdown,
            # and they start with a letter (spans start mid-sentence with space/punct)
            if any(ch in q for ch in ("*", "](", "[", "#")) or not q[:1].isalpha():
                continue
            if len(q.split()) > 50:
                warn(f, f"quote may exceed 50-word cap ({len(q.split())} words): \"{q[:60]}…\"")
                break
        if p["folder"] == "books" and "libgen" in p["text"].lower():
            err(f, "prohibited shadow-library provenance named — see sources/inbox/README.md")

        # WS8 quality warnings
        # public_domain full texts reproduce the original author's words verbatim
        # (EDITORIAL §3b); the banned-certainty rule (§4) governs the wiki's own
        # claim-strength language, not quoted primary sources — so exempt them,
        # exactly as the quote-cap check above does.
        if meta.get("public_domain") is not True:
            # the banned-certainty rule governs the wiki's own claim-strength
            # language, not words that fall inside a quoted source — skip matches
            # within a "double-quoted span", the same intent as the public_domain
            # exemption above.
            quoted = [(m.start(), m.end()) for m in re.finditer(r'"[^"\n]*"', body)]
            in_quote = lambda pos: any(s <= pos < e for s, e in quoted)
            # proper-noun acronym expansion that legitimately contains a banned
            # word: ATCOR = "All Taxes Come Out of Rent" (and its EBCOR sibling).
            allowed = [(m.start(), m.end()) for m in
                       re.finditer(r"all taxes come out of rent", body, re.I)]
            in_allowed = lambda pos: any(s <= pos < e for s, e in allowed)
            for pat in BANNED:
                for m in re.finditer(pat, body, re.I):
                    if not in_quote(m.start()) and not in_allowed(m.start()):
                        warn(f, f"banned-certainty word '{m.group(0)}' — verify source supports it")
                        break
        cn = len(re.findall(r"\[CITATION NEEDED", body))
        vf = len(re.findall(r"\[VERIFY", body))
        if cn: warn(f, f"{cn} unresolved [CITATION NEEDED] marker(s)")
        if vf: warn(f, f"{vf} unresolved [VERIFY] marker(s)")
        if "## Sources" in body and not re.search(r"—\s*[Uu]sed\s+(?:for|as|in|to)\b", body):
            warn(f, "Sources section not annotated (add '— used for …' notes)")
        if len(p["text"].splitlines()) < 30 and p["meta"].get("stub") is not True:
            warn(f, f"thin article ({len(p['text'].splitlines())} lines) — deepen")

    # registry duplicate rows (Title+Authors) — bit us in the w1 merge (Patel double row)
    seen_rows = {}
    for r in registry:
        k = ((r.get("Title") or "").strip().lower(), (r.get("Author(s)") or "").strip().lower())
        if k[0] and k in seen_rows:
            warn("sources/registry.csv", f"duplicate row: '{r.get('Title')}' ({r.get('Author(s)')})")
        seen_rows[k] = True

    # registry <-> repo consistency (drift like the CWC cluster)
    for r in registry:
        wp = (r.get("Wiki Page") or "").rstrip("/")
        m = re.search(r"/wiki/([a-z0-9\-]+)$", wp)
        if m and m.group(1) not in slugs:
            status = (r.get("Status") or "").lower()
            msg = f"registry row '{r.get('Title','?')}' -> /wiki/{m.group(1)}/ missing from git"
            (warn if "missing" in status or "drift" in status else err)(
                "sources/registry.csv", msg)

    # anti-hybrid guard: registry.csv is sources only. A synthesis-category row
    # with no external URL is a wiki page masquerading as a source — it belongs in
    # the page census (wiki-inventory.csv), not here.
    for r in registry:
        if (r.get("Category") or "").strip() in SYNTHESIS_CATS and not (r.get("URL") or "").strip():
            warn("sources/registry.csv",
                 f"row '{r.get('Title','?')}' looks like a wiki page, not a source "
                 "(synthesis category, no external URL) — remove it; pages live in "
                 "the census, not the sources file")

    # page census completeness: every page should appear in wiki-inventory.csv
    # (regenerate with scripts/build_inventory.py). Cheap drift catch; full
    # freshness (backlink counts) is verified by `build_inventory.py --check`.
    census = _read_csv(INVENTORY)
    if census:
        census_slugs = {(r.get("slug") or "").strip() for r in census}
        for slug, p in pages.items():
            if slug not in census_slugs:
                warn(p["path"], "missing from sources/wiki-inventory.csv "
                     "(run scripts/build_inventory.py)")

    # texts/ pages are reproduced primary sources — each must have a SOURCE row
    # (registry.csv), with external provenance, not just a wiki-inventory entry
    # (Floyd, 2026-07-06). A full public-domain text on the wiki that the sources
    # registry can't see is a provenance gap.
    source_page_slugs = set()
    for r in load_sources():
        wp = (r.get("Wiki Page") or "").rstrip("/")
        m = re.search(r"/wiki/([a-z0-9\-]+)$", wp)
        if m:
            source_page_slugs.add(m.group(1))
    for slug, p in pages.items():
        if p["folder"] == "texts" and slug not in source_page_slugs:
            warn(p["path"], "texts/ page has no source row in registry.csv "
                 "(add one with its external provenance URL)")

    # orphans (warning)
    for slug, p in pages.items():
        if slug not in linked_to:
            warn(p["path"], "orphan — not linked from any other page")

    # stub gauge: discovery-created pages awaiting backfill, by category
    stubs = {}
    for slug, p in pages.items():
        if p["meta"].get("stub") is True:
            stubs.setdefault(p["folder"], []).append(slug)
    if stubs:
        lines = [f"  {cat}: {len(sl)} ({', '.join(sorted(sl)[:6])}{'…' if len(sl)>6 else ''})"
                 for cat, sl in sorted(stubs.items())]
        warnings.append(f"STUBS awaiting backfill: {sum(len(v) for v in stubs.values())}\n"
                        + "\n".join(lines))

    # evidence-coverage gauge: every outcome should have >= 5 supporting research pages
    goal, met = 5, 0
    coverage = []
    for slug, p in sorted(pages.items()):
        if p["folder"] not in ("problems", "benefits"):
            continue
        n = len(aslist(p["meta"].get("supported_by")))
        met += n >= goal
        coverage.append(f"  {'✓' if n >= goal else '·'} {n}/{goal}  {slug}")
    if coverage:
        n_out = len(coverage)
        warnings.append(f"COVERAGE: {met}/{n_out} problem/benefit claims have >= {goal} supporting papers\n"
                        + "\n".join(coverage))

    # report
    for w in warnings: print(w)
    for e in errors: print(e)
    n_err = len(errors) + (len(warnings) if strict else 0)
    print(f"\nlint_wiki: {len(pages)} pages, {len(errors)} error(s), {len(warnings)} warning(s)"
          + (" [--strict]" if strict else ""))
    sys.exit(1 if n_err else 0)


if __name__ == "__main__":
    main()
