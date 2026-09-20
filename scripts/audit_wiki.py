#!/usr/bin/env python3
"""Deterministic audit for generation artifacts in reader-facing wiki text.

Classes (see sources/audit/PLAN.md):
  A1  process narration in body prose (sessions, fetchers, HTTP codes, "as of this writing")
  A2  claim-grade codes ("B-claim") in body prose
  A3  leaked internal markers ([VERIFY...], [CITATION NEEDED...], needs-unblocked-web)
  A4  first-person process narration inside the Sources section ("this session/environment")

Usage: audit_wiki.py [--json OUT] [--summary]
Exit status is 0; this is a reporting tool, lint_wiki.py stays the gate.
"""
import argparse, glob, json, re, sys, collections

BODY_PATTERNS = {
    'A1': [
        r"\bthis (?:session|pass|environment|research environment|run)\b",
        r"\bthis wiki's (?:research|session|fetcher|environment)\b",
        r"\bthe (?:default )?fetcher\b",
        r"\b(?:WebFetch|WebSearch|r\.jina\.ai|curl|Googlebot|user-agent|Wayback)\b",
        r"\bHTTP\s*\d{3}\b|\b(?:returned|got|gave|a|an)\s+40[34]\b|\(40[34]\)",
        r"\bCloudflare\b",
        r"\bas of this writing\b",
        r"\bfetch(?:ed)? (?:blocked|failed|and read)\b|\bfetch blocked\b",
        r"\breconstructed from (?:a |the )?(?:WebSearch|search|listing|abstract|snippet)",
        r"\b(?:could not|was not|were not|has not been|not) (?:be )?(?:obtained|retrieved|located|accessed|fetched|independently (?:extracted|retrieved|fetched))\b(?:[^.]{0,60}(?:session|pass|environment|method))?",
        r"\bnot independently (?:verified|confirmed|checked)\b[^.]{0,40}\b(?:this session|this pass|this environment)\b",
        r"\bindependently (?:extracted|re-extracted) ",
        r"\bthis (?:page|entry) (?:is|was) (?:built|reconstructed) from\b",
        r"\b(?:Corrected|Reattempted|Re-?verified|Confirmed|Verified|Re-?fetched|Fetched|Sharpened|Updated|Checked(?: again)?|Resolved|FLAGGED|RESOLVED)\s*(?:verbatim\s*)?(?:on\s*)?\(?20\d\d-\d\d-\d\d\b",
        r"\bChannels (?:tried|exhausted)\b",
        r"\b(?:this wiki's|the wiki's) (?:egress|drafting session|discovery(?: notes| report| summary)?|existing verified summary)\b",
        r"\bverified (?:verbatim )?this (?:session|pass)\b|\bthis (?:session|pass)['\u2019]s\b",
        r"^#+ .*\b(?:honesty notes?|Verification note|Editor'?s note|Note on sourcing|Sourcing note)\b",
        r"\b[Tt]his wiki (?:has not|has yet|should|does not|cannot|will|is not|was not|treats|has assembled|has verified|has confirmed)\b|\bthe wiki should\b",
        r"\bA verification note\b|\bVerification note:",
        r"\*\*(?:Verification note|Editor'?s note|Note on sourcing|Sourcing note|Access note)",
        r"\b(?:pdftoppm|Tesseract|pdftotext|pypdf|Semantic Scholar API|Crossref API|OpenAlex)\b",
        r"\bHermes\b|\bT[012] (?:agent|pass|quote-verification|fact-check)\b",
        r"\[STILL OPEN[^\]]*\]?", r"\[EDITORIAL[^\]]*\]?", r"\(EDITORIAL taxonomy [A-F]\)", r"\bEDITORIAL taxonomy\b",
    ],
    'A2': [r"\b[A-D]-claim\b"],
    'A3': [r"\[VERIFY[^\]]*\]?", r"\[CITATION NEEDED[^\]]*\]?", r"\[CITE[^\]]*\]", r"needs-unblocked-web",
           r"\[STILL OUTSTANDING[^\]]*\]?", r"\[Attempted[^\]]*\]?", r"\*\*Attempted\*\*", r"\bChannel: needs-", r"discovery notes\b",
           r"\[(?:BLOCKED|SHARPENED|PENDING|TODO|NOTE TO|EDITOR|GAP|OPEN|RESOLVED|UNRESOLVED|DEFERRED)\b[^\]]*\]?", r"\bpass is queued\b", r"\bqueued for (?:a |an )?(?:re-?read|proofread|verification)"],
}
SOURCES_PATTERNS = {
    'A4': [
        r"\bthis (?:session|pass|environment|research environment)\b",
        r"\bthis wiki's (?:research|session|fetcher|environment)\b",
        r"\bto this session\b",
    ],
    'A3': [r"\[VERIFY[^\]]*\]?", r"\[CITATION NEEDED[^\]]*\]?", r"needs-unblocked-web", r"\[STILL OUTSTANDING[^\]]*\]?", r"\bChannel: needs-", r"\[(?:BLOCKED|SHARPENED|PENDING|TODO|GAP|OPEN|UNRESOLVED|DEFERRED)\b[^\]]*\]?"],
}
SKIP_DIRS = ('sources/', 'scripts/', 'guides/', 'docs/', 'texts/', 'scratchpad/', 'tasks/')  # editor-facing or verbatim public-domain texts

def split(text):
    m = re.match(r'(?s)^---\n.*?\n---\n', text)
    fm = text[:m.end()] if m else ''
    body = text[m.end():] if m else text
    i = body.find('\n## Sources')
    if i < 0:
        return fm, body, ''
    return fm, body[:i], body[i:]

def scan_file(path):
    text = open(path, encoding='utf-8').read()
    fm, body, sources = split(text)
    hits = []
    for cls, pats in BODY_PATTERNS.items():
        for p in pats:
            for m in re.finditer(p, body):
                s = max(0, m.start() - 70); e = min(len(body), m.end() + 70)
                hits.append({'class': cls, 'where': 'body', 'match': m.group(0),
                             'context': body[s:e].replace('\n', ' ')})
    for cls, pats in SOURCES_PATTERNS.items():
        for p in pats:
            for m in re.finditer(p, sources):
                s = max(0, m.start() - 70); e = min(len(sources), m.end() + 70)
                hits.append({'class': cls, 'where': 'sources', 'match': m.group(0),
                             'context': sources[s:e].replace('\n', ' ')})
    # excerpt in frontmatter counts as body (it is reader-facing on the site)
    em = re.search(r'(?m)^excerpt:\s*"(.*)"\s*$', fm)
    if em:
        ex = em.group(1)
        for cls, pats in BODY_PATTERNS.items():
            for p in pats:
                for m in re.finditer(p, ex):
                    hits.append({'class': cls, 'where': 'excerpt', 'match': m.group(0), 'context': ex})
    return hits

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--json'); ap.add_argument('--summary', action='store_true')
    ap.add_argument('files', nargs='*')
    a = ap.parse_args()
    files = a.files or sorted(f for f in glob.glob('*/*.md') if not f.startswith(SKIP_DIRS))
    report = {}
    for f in files:
        h = scan_file(f)
        if h:
            report[f] = h
    if a.json:
        json.dump(report, open(a.json, 'w'), indent=1, ensure_ascii=False)
    c = collections.Counter(); pc = collections.defaultdict(set)
    for f, hs in report.items():
        for h in hs:
            c[(h['class'], h['where'])] += 1; pc[h['class']].add(f)
    print(f"audit_wiki: {len(files)} pages scanned, {len(report)} with hits")
    for k in sorted(c):
        print(f"  {k[0]} in {k[1]:8s}: {c[k]:4d} hits")
    for k in sorted(pc):
        print(f"  {k}: {len(pc[k])} pages")
    if a.summary:
        return
    for f in sorted(report):
        for h in report[f]:
            print(f"{f} [{h['class']}/{h['where']}] {h['match']!r}")

if __name__ == '__main__':
    main()
