#!/usr/bin/env python3
"""
build_dashboard.py — regenerate guides/evidence-dashboard.md, the single page where a
reader sees the whole graded case at a glance.

Like build_inventory.py this is a PURE FUNCTION of the repo: it reads the frontmatter of
every problems/*.md and benefits/*.md page and deterministically writes two GFM tables —
one per claim lane — each row carrying the claim (linked), a strength badge parsed from
`evidence_strength`, the count of supporting and challenging research pages, and the first
sentence of the excerpt as a one-line verdict. Rows sort strongest-first, then by supporter
count. The hand-written intro lives IN THIS SCRIPT (INTRO below) so it survives every
regeneration — do not hand-edit the generated page.

    python3 scripts/build_dashboard.py            # rewrite the dashboard
    python3 scripts/build_dashboard.py --check     # exit 1 if it is stale (CI)

Stdlib only, so any model's loop can invoke it.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "guides", "evidence-dashboard.md")
LANES = ["problems", "benefits"]

# Strength badge: parse the leading word of evidence_strength into a canonical grade and a
# sort rank (lower = stronger). Compound leads ("Moderate–strong", "Moderate-to-strong")
# collapse to one grade between Strong and Moderate.
GRADES = {
    "strong": ("Strong", 0),
    "moderate-strong": ("Moderate–Strong", 1),
    "moderate": ("Moderate", 2),
    "mixed": ("Mixed", 3),
    "emerging": ("Emerging", 4),
    "contested": ("Contested", 5),
    "theoretical": ("Theoretical", 6),
}
UNKNOWN_RANK = 50


def parse_frontmatter(text):
    """Minimal YAML reader (scalars, inline [a, b] and bullet lists) — no PyYAML."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw = text[3:end].strip("\n")
    body = text[end + 4:]
    meta, key = {}, None
    for line in raw.split("\n"):
        if not line.strip() or line.strip().startswith("#"):
            continue
        if re.match(r"^\s*-\s+", line) and key:
            meta.setdefault(key, [])
            if isinstance(meta[key], list):
                meta[key].append(_scalar(re.sub(r"^\s*-\s+", "", line)))
            continue
        m = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val == "":
            meta[key] = []
        elif val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            meta[key] = [_scalar(x) for x in inner.split(",")] if inner else []
        else:
            meta[key] = _scalar(val)
    return meta, body


def _scalar(v):
    v = v.strip()
    if len(v) >= 2 and v[0] in "\"'" and v[-1] == v[0]:
        v = v[1:-1]
    return v.strip()


def grade(evidence_strength):
    """(label, rank) from the leading word of an evidence_strength string."""
    token = (evidence_strength or "").strip().split()[:1]
    token = token[0] if token else ""
    norm = token.lower().replace("–", "-").replace("—", "-")
    norm = norm.replace("-to-", "-").rstrip(":;,.")
    if norm in GRADES:
        return GRADES[norm]
    return (token.rstrip(":;,.").title() or "Ungraded", UNKNOWN_RANK)


# Abbreviations whose trailing period must not end a sentence.
_ABBREV = {"u.s", "u.k", "e.g", "i.e", "vs", "etc", "cf", "al", "no", "fig",
           "dr", "mr", "mrs", "ms", "st", "approx", "est"}


def first_sentence(excerpt):
    """First sentence of the excerpt — the one-line verdict. Splits on . ! ? followed by a
    capital, but not after a known abbreviation or an initial like 'U.S.'."""
    s = (excerpt or "").strip()
    if not s:
        return ""
    for m in re.finditer(r"[.!?]+\s+(?=[\"'A-Z])", s):
        head = s[:m.start()]
        tok = re.search(r"(\S+)$", head)
        tok = tok.group(1) if tok else ""
        bare = tok.strip(".").lower()
        # skip initials (U.S.), dotted abbreviations, and the known-abbreviation set
        if "." in tok or bare in _ABBREV or (len(bare) <= 2 and tok[:1].isupper()):
            continue
        return s[:m.start() + 1].strip()
    return s


def cell(text):
    """Escape a value for a GFM table cell."""
    return (text or "").replace("|", "\\|").replace("\n", " ").strip()


def load_claims(lane):
    claims = []
    for path in sorted(glob.glob(os.path.join(ROOT, lane, "*.md"))):
        slug = os.path.splitext(os.path.basename(path))[0]
        if slug.startswith("_"):
            continue
        meta, _ = parse_frontmatter(open(path, encoding="utf-8").read())
        label, rank = grade(meta.get("evidence_strength", ""))
        claims.append({
            "slug": slug,
            "title": meta.get("title", slug),
            "label": label,
            "rank": rank,
            "supporters": len(meta.get("supported_by") or []),
            "challengers": len(meta.get("challenged_by") or []),
            "verdict": first_sentence(meta.get("excerpt", "")),
        })
    # strongest first, then most-supported first, then alphabetical for stability
    claims.sort(key=lambda c: (c["rank"], -c["supporters"], c["slug"]))
    return claims


def render_table(claims):
    lines = ["| Claim | Strength | Supporting | Challenging | One-line verdict |",
             "| --- | --- | ---: | ---: | --- |"]
    for c in claims:
        title = f"[{cell(c['title'])}](/wiki/{c['slug']}/)"
        lines.append(f"| {title} | **{c['label']}** | {c['supporters']} | "
                     f"{c['challengers']} | {cell(c['verdict'])} |")
    return "\n".join(lines)


INTRO = """<!-- GENERATED FILE — regenerated by scripts/build_dashboard.py. Do not hand-edit;
     edits will be overwritten. The intro prose lives in that script's INTRO constant. -->

## What this is

The Evidence Dashboard is the whole graded case on one page: every empirical claim the wiki
makes about geoism — the **problems** it diagnoses and the **benefits** its policies deliver —
with the strength of the evidence, how many studies stand behind each claim, how many push
back, and a one-line verdict you can quote. It is built for the advocate who needs ammunition
fast and the policymaker's staffer who needs to know exactly how far each claim can be pushed.

## How to read the grades

The **Strength** badge is the wiki's honest read of the evidence, not a cheer:

- **Strong** — replicated, quasi-experimental, or near-unanimous; state it plainly.
- **Moderate–Strong / Moderate** — real evidence, but with contested magnitudes or a
  thinner causal chain; attribute it ("studies find…").
- **Mixed / Contested** — the evidence cuts both ways; lead with the caveat.
- **Emerging** — promising but still thin; flag it as early.

The land-core claims grade strongest; every step out toward resource, monopoly, and
innovation rents is more contested, and the grades say so. The **Supporting** and
**Challenging** counts are the research pages wired into each claim — click through to read
them, and see [How We Verify](/wiki/how-we-verify/) for what each grade requires.

New here? Start at [Start Here](/wiki/start-here/). Building an argument? Take the
[Advocate's Arsenal](/wiki/advocates-arsenal/); briefing a decision-maker? the
[Policymaker's Brief](/wiki/policymakers-brief/). Or enter by topic:
[Housing](/wiki/portal-housing/) ·
[Cycles & Crises](/wiki/portal-cycles-and-crises/) ·
[Tax Design](/wiki/portal-tax-design/) ·
[Climate & the Commons](/wiki/portal-climate-and-commons/) ·
[History & People](/wiki/portal-history-and-people/) ·
[Case Studies](/wiki/portal-case-studies/) ·
[Objections Answered](/wiki/portal-objections-answered/) ·
[The Rent Frontier](/wiki/portal-rent-frontier/).
"""


def render(problems, benefits):
    fm = ('---\n'
          'title: "The Evidence Dashboard"\n'
          'category: guides\n'
          'tags: [guides, evidence, dashboard]\n'
          'stub: false\n'
          'excerpt: "The whole graded case at a glance: every problem and benefit claim in '
          'the wiki, with its evidence grade, supporting and challenging study counts, and a '
          'one-line verdict."\n'
          'last_reviewed: 2026-07-12\n'
          '---\n\n'
          '# The Evidence Dashboard\n\n')
    body = INTRO + "\n"
    body += ("\n## Problems — what geoism diagnoses\n\n"
             "Empirical claims about how the world goes wrong when rent is left uncaptured. "
             "See the full lane at [Problems](/wiki/problems/).\n\n")
    body += render_table(problems) + "\n"
    body += ("\n## Benefits — what geoist policy delivers\n\n"
             "Measured effects of capturing rent and pricing the commons. "
             "See the full lane at [Benefits](/wiki/benefits/).\n\n")
    body += render_table(benefits) + "\n"
    return fm + body


def main():
    problems = load_claims("problems")
    benefits = load_claims("benefits")
    text = render(problems, benefits)
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        stale = cur.replace("\r\n", "\n") != text.replace("\r\n", "\n")
        print("build_dashboard --check:",
              "STALE (run scripts/build_dashboard.py)" if stale else "current")
        sys.exit(1 if stale else 0)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(text)
    ungraded = [c["slug"] for c in problems + benefits if c["rank"] == UNKNOWN_RANK]
    print(f"evidence-dashboard.md -> {len(problems)} problems, {len(benefits)} benefits")
    if ungraded:
        print("  ungraded (evidence_strength lead not recognized): " + ", ".join(ungraded))


if __name__ == "__main__":
    main()
