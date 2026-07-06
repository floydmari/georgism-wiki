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
              "research", "organizations", "objections", "narratives", "books", "texts"]

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
:root{
  --bg:#f7f7f4;--panel:#fefefe;--fg:#1c2420;--muted:#5c6b63;--line:#d9ddd6;
  --accent:#1f7a5a;--link:#146c53;
  --changed-bg:#fbeecb;--changed-fg:#7a5a12;--changed-ln:#e0c877;
  --stub-bg:#f7dede;--stub-fg:#8a2f2f;--orphan-bg:#eceee9;--orphan-fg:#8a8f88;
  --cite-bg:#f7dede;--cite-fg:#8a2f2f;--ev-bg:#e2f1e9;--ev-fg:#1f5f45;
  --serif:Palatino,"Palatino Linotype","Iowan Old Style",Georgia,"Times New Roman",serif;
  --sans:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
}
@media (prefers-color-scheme:dark){:root{
  --bg:#12160f;--panel:#181d15;--fg:#e7ebe4;--muted:#93a094;--line:#2b332b;
  --accent:#4fbf8f;--link:#6fce9f;
  --changed-bg:#3a3211;--changed-fg:#e6cd7e;--changed-ln:#6b5a1e;
  --stub-bg:#3a1d1d;--stub-fg:#eb9d9d;--orphan-bg:#232722;--orphan-fg:#8a938a;
  --cite-bg:#3a1d1d;--cite-fg:#eb9d9d;--ev-bg:#173028;--ev-fg:#7fd7b1;
}}
:root[data-theme="light"]{
  --bg:#f7f7f4;--panel:#fefefe;--fg:#1c2420;--muted:#5c6b63;--line:#d9ddd6;
  --accent:#1f7a5a;--link:#146c53;--changed-bg:#fbeecb;--changed-fg:#7a5a12;--changed-ln:#e0c877;
  --stub-bg:#f7dede;--stub-fg:#8a2f2f;--orphan-bg:#eceee9;--orphan-fg:#8a8f88;
  --cite-bg:#f7dede;--cite-fg:#8a2f2f;--ev-bg:#e2f1e9;--ev-fg:#1f5f45;
}
:root[data-theme="dark"]{
  --bg:#12160f;--panel:#181d15;--fg:#e7ebe4;--muted:#93a094;--line:#2b332b;
  --accent:#4fbf8f;--link:#6fce9f;--changed-bg:#3a3211;--changed-fg:#e6cd7e;--changed-ln:#6b5a1e;
  --stub-bg:#3a1d1d;--stub-fg:#eb9d9d;--orphan-bg:#232722;--orphan-fg:#8a938a;
  --cite-bg:#3a1d1d;--cite-fg:#eb9d9d;--ev-bg:#173028;--ev-fg:#7fd7b1;
}
*{box-sizing:border-box}
body{font:16px/1.65 var(--sans);color:var(--fg);background:var(--bg);margin:0;
  -webkit-font-smoothing:antialiased}
.wrap{max-width:820px;margin:0 auto;padding:24px}
header.site{border-bottom:1px solid var(--line);position:sticky;top:0;background:var(--bg);z-index:2}
header.site .wrap{display:flex;gap:16px;flex-wrap:wrap;align-items:baseline;padding:14px 24px}
header.site a{color:var(--fg);text-decoration:none;font-size:13.5px}
header.site a:hover{color:var(--accent)}
h1,h2,h3{font-family:var(--serif);font-weight:600;text-wrap:balance;line-height:1.2}
h1{margin:.15em 0 .1em;font-size:2rem}h2{font-size:1.35rem;margin:1.4em 0 .4em}
h3{font-size:1.05rem}
.cat{color:var(--muted);text-transform:uppercase;font-size:11.5px;letter-spacing:.09em}
a{color:var(--link);text-decoration-thickness:1px;text-underline-offset:2px}
a:hover{color:var(--accent)}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:2px}
hr{border:0;border-top:1px solid var(--line);margin:1em 0}
.badge{display:inline-block;font-size:11px;font-weight:600;padding:2px 9px;border-radius:999px;
  margin:0 5px 5px 0;border:1px solid transparent;letter-spacing:.02em}
.badge.changed{background:var(--changed-bg);color:var(--changed-fg);border-color:var(--changed-ln)}
.badge.stub{background:var(--stub-bg);color:var(--stub-fg)}
.badge.orphan{background:var(--orphan-bg);color:var(--orphan-fg)}
.badge.cite{background:var(--cite-bg);color:var(--cite-fg)}
.badge.ev{background:var(--ev-bg);color:var(--ev-fg)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:12px}
.card{border:1px solid var(--line);border-radius:10px;padding:14px;background:var(--panel)}
.card h3{margin:.1em 0;font-size:15px}.card h3 a{text-decoration:none}
.excerpt{color:var(--muted);font-size:13px;margin-top:4px}
footer{color:var(--muted);font-size:12px;border-top:1px solid var(--line);margin-top:44px;
  padding-top:14px;display:flex;gap:6px;align-items:center;flex-wrap:wrap}
table{border-collapse:collapse;font-variant-numeric:tabular-nums}
td,th{border:1px solid var(--line);padding:7px 12px;text-align:left}
th{background:var(--panel);font-family:var(--sans);font-size:13px;letter-spacing:.03em}
code{background:var(--panel);border:1px solid var(--line);padding:1px 5px;border-radius:5px;
  font-family:var(--mono);font-size:.88em}
blockquote{border-left:3px solid var(--accent);margin:1em 0;padding:.2em 1em;color:var(--muted)}
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


def build_single(pages, changed, linked):
    """Emit one self-contained, content-only HTML file (no doctype/head/body) with client-side
    hash navigation — works opened locally AND as a Claude Artifact. All articles inlined."""
    def badges_for(slug, p):
        b = []
        if slug in changed: b.append('<span class="badge changed">changed</span>')
        if p["meta"].get("stub") is True: b.append('<span class="badge stub">stub</span>')
        if slug not in linked: b.append('<span class="badge orphan">orphan</span>')
        if p["meta"].get("evidence_strength"):
            b.append(f'<span class="badge ev">{html.escape(str(p["meta"]["evidence_strength"]))}</span>')
        nc = len(re.findall(r"\[CITATION NEEDED", p["body"])) + len(re.findall(r"\[VERIFY", p["body"]))
        if nc: b.append(f'<span class="badge cite">{nc} needs-citation</span>')
        return "".join(b)

    sections = []
    # home
    cat_counts = {c: sum(1 for x in pages.values() if x["cat"] == c) for c in CATEGORIES}
    home = [f"<h1>Georgism Wiki — preview</h1><p class='muted'>{len(pages)} articles · "
            f"{len(changed)} changed vs origin/main · renderer {RENDERER}. Click any title; "
            f"use the top bar to browse categories.</p>"]
    for c in CATEGORIES:
        items = sorted((s, p) for s, p in pages.items() if p["cat"] == c)
        links = " · ".join(f"<a href='#{s}'>{html.escape(p['meta'].get('title', s))}</a>"
                           for s, p in items)
        home.append(f"<h2 id='cat-{c}'>{c} ({cat_counts[c]})</h2><p class='cats'>{links}</p>")
    sections.append(f"<section class='view' id='home'>{''.join(home)}</section>")
    # articles
    for slug, p in sorted(pages.items()):
        body = re.sub(r"/wiki/([a-z0-9\-]+)/", r"#\1", p["body"])   # cross-links -> hash nav
        sections.append(
            f"<section class='view article' id='{slug}'>"
            f"<div class='cat'>{p['cat']} · <a href='#cat-{p['cat']}'>all {p['cat']}</a></div>"
            f"<h1>{html.escape(p['meta'].get('title', slug))}</h1>"
            f"<div class='badges'>{badges_for(slug, p)}</div><hr>{to_html(body)}</section>")

    nav = "".join(f"<a href='#cat-{c}'>{c}</a>" for c in CATEGORIES)
    script = ("<script>function show(){var h=(location.hash||'#home').slice(1);"
              "document.querySelectorAll('.view').forEach(function(v){v.style.display='none'});"
              "var el=document.getElementById(h)||document.getElementById('home');"
              "el.style.display='block';window.scrollTo(0,0);}"
              "window.addEventListener('hashchange',show);window.addEventListener('load',show);</script>")
    doc = (f"<style>{CSS}\n.topbar{{position:sticky;top:0;background:var(--bg);border-bottom:1px "
           f"solid var(--line);padding:10px 16px;display:flex;gap:14px;flex-wrap:wrap;z-index:5}}"
           f".topbar a{{color:var(--fg);text-decoration:none;font-size:13px}}.topbar a:hover{{color:var(--accent)}}"
           f".view{{max-width:820px;margin:0 auto;padding:20px 16px}}.article{{display:none}}"
           f".cats{{font-size:13px;line-height:1.9}}.muted{{color:var(--muted)}}.badges{{margin:6px 0}}</style>"
           f"<div class='topbar'><a href='#home'><b>Georgism Wiki Preview</b></a>{nav}</div>"
           f"{''.join(sections)}{script}")
    path = os.path.join(OUT, "wiki-preview.html")
    open(path, "w", encoding="utf-8").write(doc)
    print(f"build_preview --single: wrote {os.path.relpath(path, ROOT)} "
          f"({len(pages)} articles, self-contained)")


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

    build_single(pages, changed, linked)   # also emit the self-contained single-file preview

    print(f"build_preview: wrote {len(pages)+len(CATEGORIES)+1} html files to preview/ "
          f"({len(changed)} changed vs main) · renderer={RENDERER}")
    print("serve:  python3 -m http.server -d preview 8000  → http://localhost:8000")
    print("single: open preview/wiki-preview.html directly (no server needed)")


if __name__ == "__main__":
    main()
