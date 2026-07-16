#!/usr/bin/env python3
"""
gen_social_cards.py — social share thumbnails (og:image) for wiki pages.

Style (locked with Floyd, 2026-07-15): title + progress.org logo lockup ONLY —
paper background #fbfaf6, real logo mark, wordmark with accent dot, giant
Source Serif 4 SemiBold title (auto-fit <=3 lines, thin-space-widened word gaps).
Nothing else: no deck, no chips, no footer. Thumbnails must read in one second
at 500px. Use SHORT display titles (pre-colon rule), not full page titles.

Requires: rsvg-convert (brew install librsvg) + Source Serif 4 installed
(brew install --cask font-source-serif-4). Logo: scripts/progress-logo.png.

Deployed 2026-07-15: 37 cards — 23 posts (guides, portals, core entries) via
post og_image/twitter_image; 13 category tags + the wiki tag via tag og_image;
the /wiki/ hub via theme block "social_image" in page-wiki.hbs (the collection
index has no ghost_head social image and no matchable {{#is}} context).
To card a NEW page: add it to POSTS below, run, then upload + PUT og_image
(see scratchpad wire_cards.py pattern or sync tooling).
"""

import html, subprocess, base64, os, json
INK="#253122"; PEACH="#e0481f"; PAPER="#fbfaf6"
SERIF="'Source Serif 4',Georgia,serif"
W,H=1200,630
logo64=base64.b64encode(open(os.path.join(os.path.dirname(__file__),"progress-logo.png"),"rb").read()).decode()
def esc(s): return html.escape(s, quote=True)
def wrap(words, maxc):
    lines=[]; cur=""
    for w in words.split():
        if len(cur)+len(w)+1<=maxc: cur=(cur+" "+w).strip()
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines

def card(title, out):
    s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
       f'<rect width="{W}" height="{H}" fill="{PAPER}"/>',
       f'<image href="data:image/png;base64,{logo64}" x="80" y="66" width="56" height="56"/>',
       f'<text x="152" y="106" font-family="{SERIF}" font-size="34" font-weight="600" fill="{INK}">progress<tspan fill="{PEACH}">.</tspan>org</text>']
    for fs in [132,116,102,90,78,68,58]:
        maxc=max(6,int((W-160)/(fs*0.58)))
        lines=wrap(title,maxc)
        if len(lines)<=3: break
    lines=lines[:3]
    lh=fs*1.05; block=len(lines)*lh
    y0=int(140 + (H-140-block)/2 + fs*0.76)
    for i,ln in enumerate(lines):
        s.append(f'<text x="80" y="{int(y0+i*lh)}" font-family="{SERIF}" font-size="{fs}" font-weight="600" fill="{INK}">{esc(ln).replace(" ","\u2009 ")}</text>')
    s.append('</svg>')
    svg=f"cards/{out}.svg"; png=f"cards/{out}.png"
    open(svg,"w").write("\n".join(s))
    r=subprocess.run(["rsvg-convert","-w",str(W),"-h",str(H),svg,"-o",png],capture_output=True)
    return png if r.returncode==0 else None

# ---- targets ----
POSTS = {  # ghost post slug -> display title
 "rebuttal-cards":"Rebuttal Cards",
 "quotable-quotes":"Quotable Quotes",
 "argument-chains":"Argument Chains",
 "advocates-arsenal":"The Advocate’s Arsenal",
 "policymakers-brief":"The Policymaker’s Brief",
 "implementation-scorecard":"Implementation Scorecard",
 "evidence-dashboard":"The Evidence Dashboard",
 "how-we-verify":"How We Verify",
 "start-here":"Start Here",
 "building-the-wiki":"How This Wiki Was Built",
 "portal-housing":"Housing",
 "portal-cycles-and-crises":"Cycles & Crises",
 "portal-tax-design":"Tax Design",
 "portal-climate-and-commons":"Climate & the Commons",
 "portal-history-and-people":"History & People",
 "portal-case-studies":"Case Studies",
 "portal-objections-answered":"Objections, Answered",
 "portal-rent-frontier":"The Rent Frontier",
 # core load-bearing entries (the Start-Here five)
 "land-value-tax":"Land Value Tax",
 "economic-rent":"Economic Rent",
 "georgism":"Georgism",
 "henry-george":"Henry George",
 "progress-and-poverty":"Progress and Poverty",
}
TAGS = {  # ghost tag slug -> display title (category pages)
 "wiki-concepts":"Concepts",
 "wiki-research":"Studies",
 "wiki-people":"People",
 "wiki-places":"Places",
 "wiki-benefits":"Benefits",
 "wiki-problems":"Problems",
 "wiki-objections":"Objections",
 "wiki-organizations":"Organizations",
 "wiki-events":"Events",
 "wiki-books":"Books",
 "wiki-narratives":"Narratives",
 "wiki-texts":"Source Texts",
 "wiki-guides":"Guides",
 "wiki":"The Progress Wiki",   # the /wiki/ collection itself
}
manifest={}
for slug,title in {**POSTS,**{f"tag--{k}":v for k,v in TAGS.items()}}.items():
    png=card(title, slug.replace("tag--","tag_"))
    manifest[slug]=png
    print(("ok " if png else "FAIL ")+slug)
json.dump(manifest, open("cards/manifest.json","w"), indent=1)
print(f"\n{len(manifest)} cards rendered")
