#!/usr/bin/env python3
"""
build_preview.py — render the whole repo/branch to a browsable static HTML site under preview/.

The local review gate: no credentials, never touches Ghost. Serves a faithful-enough render of
every article with working cross-links and quality badges, so a human can eyeball everything the
loops produced *before* anything is published to progress.org.

Usage:
    python3 scripts/build_preview.py
    python3 -m http.server -d preview 8000     # then open http://localhost:8000

Fidelity: uses python-markdown (same converter as sync_to_ghost.py) when available; otherwise a
minimal built-in converter (headings/paras/links/lists) so it still runs with zero deps.
"""
import os, re, glob, html, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lint_wiki import parse_frontmatter, aslist

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "preview")
CATEGORIES = ["concepts", "people", "places", "events", "outcomes",
              "research", "organizations", "objections", "narratives"]

try:
    import markdown as _md
    def to_html(text): return _md.markdown(text, extensions=["extra", "toc"])
    RENDERER = "python-markdown"
except Exception:
    RENDERER = "builtin(minimal)"
    def to_html(text):
        out, in_ul = [], False
        for line in text.split("\n"):
            h = re.match(r"^(#{1,6})\s+(.*)$", line)
            if h:
                if in_ul: out.append("</ul>"); in_ul = False
                lvl = len(h.group(1)); out.append(f"<h{lvl}>{_inline(h.group(2))}</h{lvl}>")
            elif re.match(r"^\s*[-*]\s+", line):
                if not in_ul: out.append("<ul>"); in_ul = True
                item = _inline(re.sub(r"^\s*[-*]\s+", "", line))
                out.append(f"<li>{item}</li>")
            elif line.strip() == "":
                if in_ul: out.append("</ul>"); in_ul = False
            else:
                if in_ul: out.append("</ul>"); in_ul = False
                out.append(f"<p>{_inline(line)}</p>")
        if in_ul: out.append("</ul>")
        return "\n".join(out)
    def _inline(s):
        s = html.escape(s)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
        return s


def changed_vs_main():
    try:
        base = subprocess.run(["git", "-C", ROOT, "merge-base", "HEAD", "origin/main"],
                              capture_output=True, text=True).stdout.strip() or "origin/main"
        out = subprocess.run(["git", "-C", ROOT, "diff", "--name-only", base, "--", "*.md"],
                             capture_output=True, text=True).stdout
        return {os.path.splitext(os.path.basename(p))[0] for p in out.split() if p.endswith(".md")}
    except Exception:
        return set()


CSS = """
:root{--fg:#1a1a1a;--muted:#666;--line:#e2e2e2;--accent:#0b6;--bg:#fff}
*{box-sizing:border-box}body{font:16px/1.6 -apple-system,Segoe UI,Roboto,sans-serif;
color:var(--fg);background:var(--bg);margin:0}
.wrap{max-width:820px;margin:0 auto;padding:24px}
header.site{border-bottom:1px solid var(--line);position:sticky;top:0;background:var(--bg);z-index:2}
header.site .wrap{display:flex;gap:16px;flex-wrap:wrap;align-items:baseline;padding:14px 24px}
header.site a{color:var(--fg);text-decoration:none;font-size:14px}
header.site a:hover{color:var(--accent)}
h1{margin:.2em 0}.cat{color:var(--muted);text-transform:uppercase;font-size:12px;letter-spacing:.08em}
a{color:#06c}.badge{display:inline-block;font-size:11px;padding:2px 8px;border-radius:10px;
margin:0 4px 4px 0;border:1px solid var(--line)}
.badge.changed{background:#fff0c8;border-color:#e8c860}.badge.stub{background:#ffe0e0}
.badge.orphan{background:#eee;color:#888}.badge.cite{background:#ffe6e6;color:#900}
.badge.ev{background:#e6f7ee;color:#064}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:10px}
.card{border:1px solid var(--line);border-radius:8px;padding:12px}
.card h3{margin:.1em 0;font-size:15px}.excerpt{color:var(--muted);font-size:13px}
footer{color:var(--muted);font-size:12px;border-top:1px solid var(--line);margin-top:40px}
table{border-collapse:collapse}td,th{border:1px solid var(--line);padding:6px 10px}
code{background:#f4f4f4;padding:1px 4px;border-radius:4px}
"""

NAV = '<header class="site"><div class="wrap"><a href="{root}index.html"><b>Georgism Wiki — Preview</b></a>' \
      + "".join(f'<a href="{{root}}{c}.html">{c}</a>' for c in CATEGORIES) + "</div></header>"


def page_shell(root, title, inner):
    return (f"<!doctype html><html><head><meta charset=utf-8>"
            f"<meta name=viewport content='width=device-width,initial-scale=1'>"
            f"<title>{html.escape(title)}</title><style>{CSS}</style></head><body>"
            f"{NAV.format(root=root)}<div class='wrap'>{inner}"
            f"<footer>Local preview · renderer: {RENDERER} · not published · "
            f"badges: <span class='badge changed'>changed</span>"
            f"<span class='badge stub'>stub</span><span class='badge orphan'>orphan</span>"
            f"<span class='badge cite'>needs-citation</span></footer></div></body></html>")


def main():
    os.makedirs(OUT, exist_ok=True)
    pages, texts = {}, []
    for cat in CATEGORIES:
        for path in glob.glob(os.path.join(ROOT, cat, "*.md")):
            slug = os.path.splitext(os.path.basename(path))[0]
            text = open(path, encoding="utf-8").read()
            meta, body = parse_frontmatter(text)
            pages[slug] = dict(cat=cat, meta=meta or {}, body=body, text=text)
            texts.append(text)
    changed = changed_vs_main()
    linked = set()
    for t in texts:
        linked |= set(re.findall(r"/wiki/([a-z0-9\-]+)/", t))

    # article pages
    for slug, p in pages.items():
        body = re.sub(r"/wiki/([a-z0-9\-]+)/", r"\1.html", p["body"])   # local cross-links
        badges = []
        if slug in changed: badges.append('<span class="badge changed">changed vs main</span>')
        if p["meta"].get("stub") is True: badges.append('<span class="badge stub">stub</span>')
        if slug not in linked: badges.append('<span class="badge orphan">orphan</span>')
        if p["meta"].get("evidence_strength"):
            badges.append(f'<span class="badge ev">{html.escape(str(p["meta"]["evidence_strength"]))}</span>')
        nc = len(re.findall(r"\[CITATION NEEDED", p["body"])) + len(re.findall(r"\[VERIFY", p["body"]))
        if nc: badges.append(f'<span class="badge cite">{nc} needs-citation</span>')
        inner = (f"<div class='cat'>{p['cat']}</div><h1>{html.escape(p['meta'].get('title', slug))}</h1>"
                 f"<div>{''.join(badges)}</div><hr>{to_html(body)}")
        open(os.path.join(OUT, f"{slug}.html"), "w", encoding="utf-8").write(
            page_shell("", p["meta"].get("title", slug), inner))

    # category index pages
    for cat in CATEGORIES:
        cards = []
        for slug, p in sorted(pages.items()):
            if p["cat"] != cat: continue
            chg = ' <span class="badge changed">changed</span>' if slug in changed else ""
            cards.append(f"<div class='card'><h3><a href='{slug}.html'>"
                         f"{html.escape(p['meta'].get('title', slug))}</a>{chg}</h3>"
                         f"<div class='excerpt'>{html.escape(str(p['meta'].get('excerpt','')))[:160]}</div></div>")
        inner = f"<div class='cat'>category</div><h1>{cat} ({len(cards)})</h1><div class='grid'>{''.join(cards)}</div>"
        open(os.path.join(OUT, f"{cat}.html"), "w", encoding="utf-8").write(
            page_shell("", f"{cat} — preview", inner))

    # homepage
    rows = "".join(
        f"<tr><td><a href='{c}.html'>{c}</a></td><td>{sum(1 for p in pages.values() if p['cat']==c)}</td>"
        f"<td>{sum(1 for s,p in pages.items() if p['cat']==c and s in changed)}</td></tr>"
        for c in CATEGORIES)
    inner = (f"<h1>Georgism Wiki — local preview</h1><p>{len(pages)} articles · "
             f"{len(changed)} changed vs <code>origin/main</code> · renderer {RENDERER}.</p>"
             f"<table><tr><th>Category</th><th>Articles</th><th>Changed</th></tr>{rows}</table>")
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(
        page_shell("", "Georgism Wiki preview", inner))

    print(f"build_preview: wrote {len(pages)+len(CATEGORIES)+1} html files to preview/ "
          f"({len(changed)} changed vs main) · renderer={RENDERER}")
    print("serve:  python3 -m http.server -d preview 8000  → http://localhost:8000")


if __name__ == "__main__":
    main()
