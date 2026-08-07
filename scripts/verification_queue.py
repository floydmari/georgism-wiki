#!/usr/bin/env python3
"""Generate the Fact-Check Desk's two ledgers (stdlib only; LOOP.md step 6):

  sources/verification-queue.md  — every [CITATION NEEDED]/[VERIFY] flag on the wiki,
                                   grouped by WHO can resolve it (the full ledger)
  sources/hermes-workorder.md    — the ready-to-work order for Hermes's next run:
                                   the web-blocked and book-copy items in actionable
                                   form, capped and prioritized (the field assignment)

Every unverified claim on the wiki is an open fact-check with an owner. This script is
how routing happens — regenerate it whenever markers change.

MERGE, DON'T CLOBBER (2026-08-05). These two files are part machine census, part hand
curation: T1 classifies markers into DELIBERATE-SCOPED / RETRYABLE / BLOCKED buckets and
records what was attempted and why it failed — judgment this script cannot reproduce.
Earlier versions overwrote the whole file, destroying that curation (a 25-marker curated
ledger was replaced by an 85-marker raw dump; see LOOPLOG 2026-08-05). So:

  * The script owns ONLY the region between the AUTOGEN markers:
        <!-- AUTOGEN:START --> ... <!-- AUTOGEN:END -->
    Everything outside them is hand-maintained and is never touched.
  * A marker whose page is ALREADY routed by hand (its path appears in the curated
    region) is considered dispositioned and is left out of the generated block. The
    generated block is therefore "markers not yet routed by a human" — a worklist,
    not a census.
  * If a target file has no AUTOGEN markers, the script REFUSES to write it and says
    so, rather than clobbering. Use --init to append an empty block to a file once.

Usage:
    python3 scripts/verification_queue.py            # merge into the AUTOGEN blocks
    python3 scripts/verification_queue.py --check    # report drift, write nothing (CI)
    python3 scripts/verification_queue.py --init     # add a missing AUTOGEN block
"""
import glob, os, re, sys, datetime

CATS = ["concepts", "people", "places", "organizations", "objections", "events",
        "problems", "benefits", "narratives", "research", "books", "texts", "guides"]

BUCKETS = [
 ("needs-owner-input", ["owner", "floyd", "supply bio"]),
 ("needs-book-copy (see sources/wanted-books.md)", ["book", "lending", "e-copy", "full text of the book"]),
 ("needs-unblocked-web (proxy allowlist or manual fetch)", ["proxy", "blocked", "fetch", "web access", "network access", "unblocked", "direct read", "primary text", "pdf"]),
 ("needs-new-source (research/forage task)", ["strongest", "study", "empirical", "academic statement", "citation for", "source for"]),
]
UNCLASSIFIED = "unclassified (T1 triage)"

QUEUE_PATH = "sources/verification-queue.md"
ORDER_PATH = "sources/hermes-workorder.md"
START, END = "<!-- AUTOGEN:START -->", "<!-- AUTOGEN:END -->"
CAP = 60   # one overnight run's worth; regenerate after each Hermes PR merges


def bucket(text):
    t = text.lower()
    for name, keys in BUCKETS:
        if any(k in t for k in keys):
            return name
    return UNCLASSIFIED


def _tidy(t):
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)        # [text](url) -> text
    t = re.sub(r"[*`_]+", "", t)
    return " ".join(t.split()).lstrip(":—-– ").strip()


def _inline_detail(body, i):
    """Text inside a `[VERIFY: ...]` marker: scan to its real closing bracket.

    A plain `]`-search stops at the first markdown link inside the marker, which is
    what produced the old mangled rows. Track depth instead, and give up (returning
    None) if the marker never closes within a paragraph — that means the bracket
    belongs to something else.
    """
    depth, out = 1, []
    for ch in body[i:i + 1200]:
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                return _tidy("".join(out))
        out.append(ch)
        if "".join(out[-2:]) == "\n\n":
            return None
    return None


def _following_sentence(body, i):
    """For a self-closed `[VERIFY]`, the claim it flags is the sentence after it."""
    tail = body[i:i + 600]
    tail = tail.split("\n\n")[0]
    m = re.search(r"(?<=[.!?])(\s|$)", tail)
    if m:
        tail = tail[:m.start()]
    return _tidy(tail)


def collect_markers():
    """Every live [CITATION NEEDED]/[VERIFY] marker, as (path, kind, detail).

    Two marker shapes, extracted differently:
      `[VERIFY: why]` / `[VERIFY — why]`  -> the text inside the brackets
      `[VERIFY]`                          -> the sentence that follows it
    """
    found = []
    for cat in CATS:
        for path in sorted(glob.glob(f"{cat}/*.md")):
            body = open(path, encoding="utf-8").read()
            for m in re.finditer(r"\[(CITATION NEEDED|VERIFY)(\s*[:—–]|\])", body):
                kind, sep = m.group(1), m.group(2)
                if sep == "]":
                    detail = _following_sentence(body, m.end())
                else:
                    detail = _inline_detail(body, m.end())
                    if detail is None:          # unterminated: treat as self-closed
                        detail = _following_sentence(body, m.end())
                found.append((path, kind, (detail or "(no detail given)")[:220].rstrip()))
    return found


def read_file(path):
    return open(path, encoding="utf-8").read() if os.path.exists(path) else None


def split_autogen(text):
    """-> (before, generated, after) or None if the file has no AUTOGEN block."""
    if text is None or START not in text or END not in text:
        return None
    before, rest = text.split(START, 1)
    generated, after = rest.split(END, 1)
    return before, generated, after


def curated_paths(before, after):
    """Page paths a human has already routed outside the generated block."""
    return set(re.findall(r"`([a-z0-9_-]+/[a-z0-9._-]+\.md)`", before + after))


def render_rows(markers, order):
    rows = {}
    for path, kind, detail in markers:
        rows.setdefault(bucket(detail), []).append(f"- `{path}` — **{kind}** {detail}")
    out = []
    for b in order:
        if b not in rows:
            continue
        out.append(f"### {b} ({len(rows[b])})\n")
        out.extend(rows[b])
        out.append("")
    return rows, out


def write_merged(path, before, after, body_lines, label, check):
    new = before + START + "\n" + "\n".join(body_lines).rstrip() + "\n" + END + after
    old = before + START + "" + END + after  # placeholder, only used for compare below
    current = read_file(path)
    if current == new:
        print(f"  {label}: already current")
        return False
    if check:
        print(f"  {label}: DRIFT — generated block is stale (run without --check)")
        return True
    open(path, "w", encoding="utf-8").write(new)
    print(f"  {label}: generated block updated")
    return True


def ensure_block(path, heading):
    text = read_file(path)
    if text is None:
        print(f"  {path}: missing — create the curated file first", file=sys.stderr)
        return False
    if split_autogen(text):
        print(f"  {path}: AUTOGEN block already present")
        return True
    open(path, "a", encoding="utf-8").write(
        f"\n\n## {heading}\n\n"
        "*Machine-maintained by `scripts/verification_queue.py`. Everything above this\n"
        "heading is hand-curated and is never rewritten. Rows here are markers no human\n"
        "has routed yet; route one by moving it into a curated bucket above.*\n\n"
        f"{START}\n{END}\n")
    print(f"  {path}: AUTOGEN block appended")
    return True


def main():
    check = "--check" in sys.argv
    if "--init" in sys.argv:
        ok = ensure_block(QUEUE_PATH, "Unrouted markers (auto-generated)")
        ok &= ensure_block(ORDER_PATH, "Unrouted field items (auto-generated)")
        return 0 if ok else 1

    markers = collect_markers()
    order = [b for b, _ in BUCKETS] + [UNCLASSIFIED]
    stamp = datetime.date.today()
    drift = False

    for path, label, hermes_only in ((QUEUE_PATH, "verification-queue", False),
                                     (ORDER_PATH, "hermes-workorder", True)):
        parts = split_autogen(read_file(path))
        if not parts:
            print(f"  {label}: NO AUTOGEN BLOCK — refusing to write (would clobber "
                  f"curation). Run with --init to add one.", file=sys.stderr)
            drift = True
            continue
        before, _, after = parts
        routed = curated_paths(before, after)
        pending = [m for m in markers if m[0] not in routed]
        rows, body = render_rows(pending, order)
        if hermes_only:
            keep = [b for b in order
                    if b.startswith("needs-book-copy") or b.startswith("needs-unblocked-web")]
            capped = []
            n = 0
            for b in keep:
                items = rows.get(b, [])[:max(0, CAP - n)]
                if not items:
                    continue
                capped.append(f"### {b} ({len(items)} of {len(rows.get(b, []))})\n")
                capped.extend(items)
                capped.append("")
                n += len(items)
            body = capped
            head = (f"*Regenerated {stamp}: {n} unrouted field item(s), cap {CAP}. "
                    f"{len(routed)} page(s) already routed by hand above.*\n")
        else:
            head = (f"*Regenerated {stamp}: {len(pending)} of {len(markers)} marker(s) "
                    f"not yet routed by hand ({len(routed)} page(s) already curated above).*\n")
        if not body:
            body = ["*Nothing unrouted — every live marker is accounted for above.*"]
        drift |= write_merged(path, before, after, [head] + body, label, check)

    print(f"verification_queue: {len(markers)} live marker(s) across the wiki")
    if check and drift:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
