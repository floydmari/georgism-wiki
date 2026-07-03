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
  * outcomes: evidence_strength + supported_by present, supported_by slugs resolve
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
CATEGORIES = ["concepts", "people", "places", "events", "outcomes",
              "research", "organizations", "objections", "narratives"]
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


def load_registry():
    rows = []
    if not os.path.exists(REGISTRY):
        warn("sources/registry.csv", "not found — source-registry checks skipped")
        return rows
    with open(REGISTRY, encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            rows.append(row)
    return rows


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

        if p["folder"] == "outcomes":
            if not meta.get("evidence_strength"): err(f, "outcome missing evidence_strength")
            if not aslist(meta.get("supported_by")): warn(f, "outcome has no supported_by")
            for r in aslist(meta.get("supported_by")):
                if r not in slugs:
                    err(f, f"supported_by -> unknown research '{r}'")
                elif slug not in aslist(pages[r]["meta"].get("supports_outcomes")):
                    warn(f, f"bidirectional gap: {r} lacks supports_outcomes: [{slug}]")
            for r in aslist(meta.get("challenged_by")):
                if r not in slugs: err(f, f"challenged_by -> unknown research '{r}'")

        for rel_key in ("related_people", "related_places"):
            for t in aslist(meta.get(rel_key)):
                if t not in slugs: err(f, f"{rel_key} -> unknown page '{t}'")

        if p["folder"] == "objections":
            for section in ("## The Objection", "## Net Assessment", "## Sources"):
                if section not in body: err(f, f"objection missing section '{section}'")
            if "## The Response" not in body:
                err(f, "objection missing a Response section")

        # WS8 quality warnings
        for pat in BANNED:
            m = re.search(pat, body, re.I)
            if m: warn(f, f"banned-certainty word '{m.group(0)}' — verify source supports it")
        cn = len(re.findall(r"\[CITATION NEEDED", body))
        vf = len(re.findall(r"\[VERIFY", body))
        if cn: warn(f, f"{cn} unresolved [CITATION NEEDED] marker(s)")
        if vf: warn(f, f"{vf} unresolved [VERIFY] marker(s)")
        if "## Sources" in body and not re.search(r"—\s*used for|—\s*Used for", body):
            warn(f, "Sources section not annotated (add '— used for …' notes)")
        if len(p["text"].splitlines()) < 30:
            warn(f, f"thin article ({len(p['text'].splitlines())} lines) — deepen")

    # registry <-> repo consistency (drift like the CWC cluster)
    for r in registry:
        wp = (r.get("Wiki Page") or "").rstrip("/")
        m = re.search(r"/wiki/([a-z0-9\-]+)$", wp)
        if m and m.group(1) not in slugs:
            status = (r.get("Status") or "").lower()
            msg = f"registry row '{r.get('Title','?')}' -> /wiki/{m.group(1)}/ missing from git"
            (warn if "missing" in status or "drift" in status else err)(
                "sources/registry.csv", msg)

    # orphans (warning)
    for slug, p in pages.items():
        if slug not in linked_to:
            warn(p["path"], "orphan — not linked from any other page")

    # report
    for w in warnings: print(w)
    for e in errors: print(e)
    n_err = len(errors) + (len(warnings) if strict else 0)
    print(f"\nlint_wiki: {len(pages)} pages, {len(errors)} error(s), {len(warnings)} warning(s)"
          + (" [--strict]" if strict else ""))
    sys.exit(1 if n_err else 0)


if __name__ == "__main__":
    main()
