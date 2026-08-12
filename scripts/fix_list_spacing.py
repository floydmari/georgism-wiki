#!/usr/bin/env python3
"""
fix_list_spacing.py — insert the blank line Markdown needs before a list.

THE BUG (found 2026-08-12, via the Ghost write-back). Python-Markdown — the
renderer sync_to_ghost.py uses — only starts a list when a blank line precedes
it. A list written directly under its lead-in paragraph:

    The book is organized in two parts:
    - **Part One**: ...
    - **Part Two**: ...

renders as ONE PARAGRAPH with literal "- " text in it, on the live site:

    <p>The book is organized in two parts: - <strong>Part One</strong>: ... - ...</p>

Verified live on progress.org/wiki/barker-henry-george-biography/ before this fix.
It was invisible for months because the markdown reads correctly in git and on
GitHub (whose renderer is lenient); only the published page is wrong. The Ghost
write-back surfaced it by round-tripping a rendered page back into source.

THE FIX: a blank line before the first item of each affected list. Nothing else
is touched — no words, no punctuation, no list content.

SAFETY: --check re-renders every modified page and refuses the write unless the
visible text is byte-identical before and after (tags stripped, whitespace
collapsed) AND the number of list elements went up. A change that alters text
is a bug in this script, not an edit, so it aborts rather than "fixing" prose.

Usage:
    python3 scripts/fix_list_spacing.py            # report only
    python3 scripts/fix_list_spacing.py --write    # apply (verifies first)
"""
import glob
import os
import re
import sys

import frontmatter
import markdown as md

FOLDERS = ["concepts", "people", "places", "events", "problems", "benefits",
           "research", "organizations", "objections", "narratives", "books",
           "guides", "texts"]

LIST_RE = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+\S")
# lines that legitimately precede a list with no blank line between them
SKIP_PREV = re.compile(r"^\s*(?:[-*+]|\d+\.)\s|^\s*>|^#{1,6}\s|^\s*\||^\s*$|^<|^\s{4,}\S|^\s*```")


def fix_body(body):
    """Return (new_body, insert_count)."""
    lines = body.split("\n")
    out, inserted, in_fence = [], 0, False
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if (not in_fence and i > 0 and LIST_RE.match(line)
                and not SKIP_PREV.match(lines[i - 1])):
            out.append("")
            inserted += 1
        out.append(line)
    return "\n".join(out), inserted


def visible_text(html):
    """Rendered text with markup removed — what a reader actually sees.

    Standalone bullet tokens are dropped: when a run-on paragraph becomes a real
    list, the literal "- " characters stop being text and become structure, and
    that is precisely the improvement we are making. Hyphens inside words are
    untouched, so a genuine wording change still shows up as a difference.
    """
    text = re.sub(r"<[^>]+>", " ", html)
    return " ".join(t for t in text.split()
                    if t not in {"-", "*", "+"} and not re.fullmatch(r"\d{1,3}\.", t))


def list_elements(html):
    return html.count("<ul>") + html.count("<ol>") + html.count("<li>")


def main():
    write = "--write" in sys.argv
    files = [p for f in FOLDERS for p in glob.glob(f"{f}/*.md")
             if not os.path.basename(p).startswith("_")]
    changed, refused, total_inserts = [], [], 0

    for path in sorted(files):
        # Split the raw text by hand and rewrite ONLY the body. frontmatter.dumps()
        # round-trips the YAML through a parser, which reorders keys alphabetically,
        # expands inline lists to block lists and re-wraps the excerpt — hundreds of
        # lines of churn in a change that is supposed to add blank lines and nothing
        # else (caught in review before it was committed, 2026-08-12).
        raw = open(path, encoding="utf-8").read()
        m = re.match(r"^(---\n.*?\n---\n)(.*)$", raw, re.S)
        if not m:
            continue
        fm_text, body = m.group(1), m.group(2)
        new_body, n = fix_body(body)
        if not n:
            continue
        before = md.markdown(body, extensions=["extra", "toc"])
        after = md.markdown(new_body, extensions=["extra", "toc"])
        # the whole point: same words, more list structure
        if visible_text(before) != visible_text(after):
            refused.append((path, "visible text would change"))
            continue
        if list_elements(after) <= list_elements(before):
            refused.append((path, "no new list structure — nothing gained"))
            continue
        changed.append((path, n))
        total_inserts += n
        if write:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(fm_text + new_body)

    print(f"pages needing the fix: {len(changed)}  (blank lines inserted: {total_inserts})")
    for path, n in changed[:15]:
        print(f"   {path}  (+{n})")
    if len(changed) > 15:
        print(f"   … and {len(changed) - 15} more")
    if refused:
        print(f"\nREFUSED (left untouched — verification failed): {len(refused)}")
        for path, why in refused[:10]:
            print(f"   {path}: {why}")
    print("\n" + ("WRITTEN" if write else "dry run — pass --write to apply"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
