#!/usr/bin/env python3
"""
source_figures.py — extract key figures from source PDFs and host them on Ghost.

Some research papers carry one load-bearing chart that does more work than a page
of prose (e.g. Bonnet et al. 2021 Figure 1 — the land/housing decomposition of the
wealth-to-income ratio). This script makes embedding those figures reproducible:

  1. downloads the source PDF (cached in .figure-cache/, git-ignored),
  2. renders a declared page region to a high-res PNG with PyMuPDF,
  3. uploads the PNG to the Ghost image store (/ghost/api/admin/images/upload/),
  4. prints the hosted URL + a ready-to-paste <figure> block for the entry.

The FIGURES manifest below is the record of what was extracted from where — the
PNGs themselves are not committed (same convention as gen_social_cards.py: the
script is the source of truth, Ghost hosts the bytes).

Editorial rules for embedded figures (see EDITORIAL.md "Figures from sources"):
  * only where the chart itself is doing evidential work the prose can't;
  * one figure per entry, placed after the Summary;
  * every figure carries a <figcaption> crediting author(s), year, figure number,
    and journal/publisher — third-party figures are excerpts reproduced for
    comment and review and are NOT covered by the wiki's CC BY 4.0 license;
  * crop the figure body only (no LaTeX caption/notes) and restate what matters
    in our own caption, so the image works at wiki column width.

Usage:
    python3 scripts/source_figures.py            # process all manifest entries
    python3 scripts/source_figures.py bonnet-fig1   # just one, by key
    python3 scripts/source_figures.py --no-upload   # render only (inspect PNGs)

Requires: pip install pymupdf requests PyJWT + Ghost admin credentials
(GHOST_ADMIN_KEY / GHOST_URL via env or 1Password — same as sync_to_ghost.py).
"""
import os, sys, time, html

import fitz  # PyMuPDF
import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, ".figure-cache")

# ─── the manifest: every hosted figure, its provenance, and its crop ──────────
# page is 1-based; clip is (x0, y0, x1, y1) in PDF points (72/inch).
# To find a clip: render the whole page (clip=None) at dpi=150, measure pixels,
# divide by dpi/72. Keep dpi ~200 so charts stay sharp at 2x column width.
FIGURES = [
    {
        "key": "bonnet-fig1",
        "entry": "research/bonnet-land-is-back.md",
        "pdf_url": ("https://amu.hal.science/hal-03238443/file/"
                    "Land%20is%20back%2C%20it%20should%20be%20taxed%2C"
                    "%20it%20can%20be%20taxed.pdf"),
        "page": 7,
        "clip": (28, 58, 592, 652),
        "dpi": 200,
        "alt": ("Six-panel chart decomposing national capital as a percentage of "
                "national income, 1860s to 2010s, for France, the United Kingdom, "
                "Canada, Germany and the United States: housing (land plus "
                "structure), agricultural land, developed land, housing structures, "
                "net foreign assets and other domestic capital. In every country "
                "the post-1950 rise in capital is driven by housing land, while "
                "structures and other capital stay roughly flat; a sixth panel "
                "shows land's share of housing value rising toward 40-55% by 2015."),
        "caption": ("Figure 1 from the paper: the value of national capital "
                    "(% of national income) decomposed by component, 1860s–2010s. "
                    "In all five countries the modern rise in the wealth-to-income "
                    "ratio is a rise in <em>land under housing</em> (hatched area), "
                    "not in structures or other produced capital — panel (f) shows "
                    "land's share of housing value climbing to 40–55% by 2015. "
                    "<span class=\"figure-credit\">Source: Bonnet, Chapelle, "
                    "Trannoy &amp; Wasmer (2021), Figure 1, <em>European Economic "
                    "Review</em> 134 — reproduced for comment and review.</span>"),
    },
    {
        "key": "rognlie-fig3",
        "entry": "research/rognlie-capital-share.md",
        "pdf_url": "https://mrognlie.github.io/papers/brookings_capitalshare.pdf",
        "page": 44,
        "clip": (74, 64, 549, 331),
        "dpi": 200,
        "alt": ("Line chart of the net capital share of private domestic value "
                "added for G7 countries, 1948 to 2010, split into housing and "
                "non-housing sectors. The housing series climbs steadily from "
                "about 3% to about 10%, while the non-housing series ends lower "
                "than it began, drifting from roughly 24% down to 17-20%."),
        "caption": ("Figure 3 from the paper: the net capital share of private "
                    "domestic value added for G7 countries, 1948–2010, split into "
                    "housing (h) and non-housing (nh) sectors, weighted (w) and "
                    "unweighted (uw). Housing's share roughly triples from ~3% to "
                    "~10% while the non-housing share ends <em>below</em> where it "
                    "began — the long-run rise in the capital share is entirely a "
                    "housing story. <span class=\"figure-credit\">Source: Rognlie "
                    "(2015), Figure 3, <em>Brookings Papers on Economic "
                    "Activity</em> — reproduced for comment and review.</span>"),
    },
    {
        "key": "great-mortgaging-fig2",
        "entry": "research/great-mortgaging.md",
        "pdf_url": "https://www.nber.org/system/files/working_papers/w20501/w20501.pdf",
        "page": 11,
        "clip": (66, 104, 549, 377),
        "dpi": 200,
        "alt": ("Line chart of the average ratio of bank lending to GDP across 17 "
                "advanced economies, 1870 to 2011, with separate lines for mortgage "
                "and non-mortgage lending. Non-mortgage lending rises from roughly "
                "0.17 to 0.49 of GDP; mortgage lending rises from under 0.1 to "
                "about 0.7, overtaking non-mortgage lending in the 1990s and "
                "surging steeply after 1980."),
        "caption": ("Figure 2 from the paper: average bank mortgage and "
                    "non-mortgage lending to GDP for 17 advanced economies, "
                    "1870–2011. Non-mortgage lending roughly triples over 140 "
                    "years while mortgage lending rises about eightfold, "
                    "overtaking it in the 1990s — nearly all modern growth in "
                    "bank credit is lending against real estate. "
                    "<span class=\"figure-credit\">Source: Jordà, Schularick "
                    "&amp; Taylor (2014), Figure 2, NBER Working Paper 20501 — "
                    "reproduced for comment and review.</span>"),
    },
    {
        "key": "kss-fig27",
        "entry": "research/knoll-schularick-steger-house-prices.md",
        "pdf_url": "https://www.cesifo.org/DocDL/cesifo1_wp5006.pdf",
        "page": 31,
        "clip": (125, 118, 462, 322),
        "dpi": 300,
        "alt": ("Scatter-line chart of mean real house prices and mean real "
                "imputed land prices across 14 advanced economies, 1870 to 2012, "
                "indexed to 1990=100, with the two world wars shaded. Both series "
                "are roughly flat until about 1950, then rise together; after the "
                "1990s land prices accelerate past house prices, reaching an index "
                "of about 250 versus 155 by the late 2000s."),
        "caption": ("Figure 27 from the working paper: mean real house prices and "
                    "mean imputed real land prices, 14 advanced economies, "
                    "1870–2012 (index 1990&nbsp;=&nbsp;100; world wars shaded). "
                    "Flat for eight decades, land prices surge after 1950 and "
                    "outpace house prices — the decomposition behind the headline "
                    "finding that rising land prices explain about 80% of the "
                    "postwar house-price boom. <span class=\"figure-credit\">"
                    "Source: Knoll, Schularick &amp; Steger, <em>No Price Like "
                    "Home</em> (CESifo Working Paper 5006, 2015 version), Figure "
                    "27; published in <em>American Economic Review</em> 107(2), "
                    "2017 — reproduced for comment and review.</span>"),
    },
    {
        "key": "glaeser-gyourko-fig3",
        "entry": "research/glaeser-gyourko-housing-supply.md",
        "pdf_url": "https://www.nber.org/system/files/working_papers/w23833/w23833.pdf",
        "page": 27,
        "clip": (60, 92, 675, 505),
        "dpi": 200,
        "alt": ("Labeled scatter plot of 98 US metropolitan areas: house-price to "
                "minimum-profitable-production-cost ratio in 2013 against permits "
                "issued 2000-2013 as a share of the 2000 housing stock. Most metros "
                "cluster at ratios near or below 1; a coastal tail sits far above — "
                "San Francisco near 2.8, Urban Honolulu about 2.6, Los Angeles and "
                "San Diego around 2 — and these high-ratio metros issued the fewest "
                "permits, with a downward-sloping fit line."),
        "caption": ("Figure 3 from the working-paper version: house price divided by "
                    "minimum profitable production cost (MPPC) in 2013 versus "
                    "permitting intensity, 98 US metros. Most of the country builds "
                    "at prices near production cost (ratio ≈ 1); the expensive tail "
                    "— San Francisco ≈ 2.8, Honolulu, coastal California, New York — "
                    "is exactly where the fewest permits were issued, and the gap is "
                    "the price of land under regulatory scarcity. "
                    "<span class=\"figure-credit\">Source: Glaeser &amp; Gyourko, "
                    "NBER Working Paper 23833 (2017), Figure 3; published in "
                    "<em>Journal of Economic Perspectives</em> 32(1), 2018 — "
                    "reproduced for comment and review.</span>"),
    },
    {
        "key": "jones-marinescu-fig2",
        "entry": "research/jones-marinescu-alaska-pfd.md",
        "pdf_url": "https://www.nber.org/system/files/working_papers/w24312/w24312.pdf",
        "page": 35,
        "clip": (95, 88, 480, 610),
        "dpi": 200,
        "alt": ("Two-panel synthetic-control chart. Panel (a): Alaska's employment "
                "rate 1977-2014 tracks its synthetic control closely both before and "
                "after the dividend begins (dashed vertical line at 1981), with no "
                "visible post-dividend gap. Panel (b): the Alaska-minus-synthetic "
                "difference stays near zero and well inside the band of placebo "
                "states over more than 30 years of event time."),
        "caption": ("Figure 2 from the working-paper version: Alaska's employment "
                    "rate versus its synthetic control, 1977–2014. After the "
                    "Permanent Fund Dividend begins (dashed line), actual Alaska "
                    "tracks the no-dividend counterfactual with no detectable "
                    "employment decline, and panel (b) shows the difference sits "
                    "well inside the placebo band. (The paper's other headline — a "
                    "~1.8&nbsp;pp rise in part-time work — is a real response; see "
                    "text.) <span class=\"figure-credit\">Source: Jones &amp; "
                    "Marinescu, NBER Working Paper 24312, Figure 2; published in "
                    "<em>American Economic Journal: Economic Policy</em> 14(2), "
                    "2022 — reproduced for comment and review.</span>"),
    },
    {
        "key": "larson-fig3",
        "entry": "research/larson-us-land-value.md",
        "pdf_url": "https://www.bea.gov/sites/default/files/papers/WP2015-3.pdf",
        "page": 21,
        "clip": (138, 92, 470, 338),
        "dpi": 300,
        "alt": ("Line chart of the aggregate value of land in the lower 48 US "
                "states, 2000 to 2009, in current trillions of dollars. The line "
                "rises from about 20.8 trillion in 2000 to a peak of 26.2 trillion "
                "in 2006, then falls to 23.0 trillion by 2009."),
        "caption": ("Figure 3 from the paper: the aggregate value of land in the "
                    "contiguous United States, 2000–2009 (current dollars). Land "
                    "value rose 26% from $20.8&nbsp;trillion to $26.2&nbsp;trillion "
                    "at the 2006 peak, then fell 12% to the paper's headline "
                    "$23&nbsp;trillion in 2009 — the US government's own estimate "
                    "of the land base, swinging with the property cycle. "
                    "<span class=\"figure-credit\">Source: Larson (2015), Figure 3, "
                    "BEA Working Paper WP2015-3. US federal government work — "
                    "public domain.</span>"),
    },
    {
        "key": "gyourko-krimmel-fig4",
        "entry": "research/gyourko-krimmel-zoning-tax.md",
        "pdf_url": "https://www.nber.org/system/files/working_papers/w28993/w28993.pdf",
        "page": 41,
        "clip": (68, 86, 545, 378),
        "dpi": 220,
        "alt": ("Dot plot of the 25th percentile, median, and 75th percentile "
                "zoning tax per quarter acre in 24 US metros, in thousands of 2018 "
                "dollars. San Francisco's median is about 410 thousand with a 75th "
                "percentile near 760 thousand; Los Angeles, Seattle and New York "
                "have medians around 150-200 thousand; most interior metros — "
                "Nashville, Columbus, Dallas, Cincinnati — sit near zero."),
        "caption": ("Figure 4 from the working paper: the interquartile range of "
                    "estimated \"zoning taxes\" — how much regulation bids up the "
                    "price of a quarter-acre of land — across 24 metros (2018 "
                    "dollars). The median gap is about $400k in San Francisco and "
                    "$150–200k in Los Angeles, Seattle and New York, but near zero "
                    "in most lightly regulated interior metros. "
                    "<span class=\"figure-credit\">Source: Gyourko &amp; Krimmel, "
                    "NBER Working Paper 28993 (2021), Figure 4; published in "
                    "<em>Journal of Urban Economics</em> 126 — reproduced for "
                    "comment and review.</span>"),
    },
    {
        "key": "dors-fig1",
        "entry": "research/dors-land-taxes-housing-prices.md",
        "pdf_url": ("https://dors.dk/files/media/publikationer/arbejdspapirer/"
                    "2017/02_arbejdspapir_land_tax.pdf"),
        "page": 9,
        "clip": (140, 375, 455, 572),
        "dpi": 300,
        "alt": ("Line chart of average prices for Danish single-family homes, "
                "2000 to 2008, in thousands of DKK, split into areas where the "
                "land tax would later fall versus rise. The two lines track each "
                "other until the 2004 reform announcement (first vertical line), "
                "then diverge: by the 2007 implementation (second vertical line) "
                "homes in lower-land-tax areas sell for roughly 100,000 DKK more, "
                "about 1,600 versus 1,490 thousand DKK by 2008."),
        "caption": ("Figure 1 from the paper: average single-family house prices "
                    "in Danish municipalities where the 2007 amalgamation reform "
                    "lowered versus raised the land tax (grundskyld). Identical "
                    "trends before the 2004 announcement (first line); after it, "
                    "prices rise less where the land tax rose — the visible "
                    "quasi-experiment behind the paper's finding that land-tax "
                    "changes are fully capitalized into prices. "
                    "<span class=\"figure-credit\">Source: Høj, Jørgensen &amp; "
                    "Schou, <em>Land Taxes and Housing Prices</em>, De Økonomiske "
                    "Råd Working Paper 2017:1, Figure 1 — reproduced for comment "
                    "and review.</span>"),
    },
    {
        "key": "hoyt-fig76",
        "entry": "research/hoyt-chicago-land-values.md",
        "pdf_url": ("https://ia801602.us.archive.org/32/items/"
                    "onehundredyearso00hoytrich/onehundredyearso00hoytrich_bw.pdf"),
        "page": 384,
        "clip": (26, 102, 342, 418),
        "dpi": 300,
        "alt": ("Hand-drawn semi-log chart from 1933 titled 'The Trend of Chicago "
                "Land Values, Population and Manufacturing, 1835-1933'. Four "
                "series climb roughly a thousand-fold over the century: aggregate "
                "land value in current dollars, population, value of manufactures, "
                "and site land value measured in days of unskilled labor. The land "
                "value line surges and pauses in repeated waves, with visible "
                "peaks in the 1830s, 1850s, early 1870s, early 1890s, and late "
                "1920s."),
        "caption": ("Figure 76 from the book (p. 348): a century of Chicago land "
                    "values, population, and manufacturing on a logarithmic "
                    "scale, 1835–1933. Aggregate land value climbs roughly a "
                    "thousand-fold with the city's growth — but in recurring "
                    "waves, with the peaks (1836, 1856, 1873, 1892, 1926) that "
                    "later cycle theorists built on. "
                    "<span class=\"figure-credit\">Source: Homer Hoyt, <em>One "
                    "Hundred Years of Land Values in Chicago</em> (University of "
                    "Chicago Press, 1933), Fig. 76; scan via Internet Archive — "
                    "reproduced for comment and review.</span>"),
    },
    {
        "key": "bakker-fig61",
        "entry": "research/bakker-land-rents-tfp.md",
        "pdf_url": ("https://www.imf.org/-/media/Files/Publications/WP/2023/"
                    "English/wpiea2023170-print-pdf.ashx"),
        "page": 28,
        "clip": (88, 219, 522, 424),
        "dpi": 220,
        "alt": ("Two-panel line chart of total factor productivity in Hong Kong "
                "and Singapore, 1970 to 2020, indexed to 1970=100. Left panel, "
                "official Penn World Tables: Hong Kong rises to about 175 while "
                "Singapore stays flat near 100. Right panel, corrected for urban "
                "land rents: both rise strongly, Singapore more than doubling to "
                "about 230 and Hong Kong reaching about 320."),
        "caption": ("Figure 6.1 from the paper (index 1970&nbsp;=&nbsp;100): "
                    "measured versus corrected TFP for Singapore and Hong Kong. "
                    "In official Penn World Tables data Singapore's productivity "
                    "appears flat for fifty years; once the ~25% of GDP flowing "
                    "to urban land rents is separated from capital income, its "
                    "true TFP more than doubles — recorded \"capital\" income was "
                    "substantially land rent. <span class=\"figure-credit\">"
                    "Source: Bakker, IMF Working Paper 23/170 (2023), Figure 6.1 "
                    "— reproduced for comment and review.</span>"),
    },
]


def fetch_pdf(url, key):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, f"{key}.pdf")
    if not os.path.exists(path):
        print(f"  fetching {url[:80]}...")
        r = requests.get(url, timeout=120)
        r.raise_for_status()
        with open(path, "wb") as f:
            f.write(r.content)
    return path


def render(fig):
    pdf = fetch_pdf(fig["pdf_url"], fig["key"])
    doc = fitz.open(pdf)
    page = doc[fig["page"] - 1]
    clip = fitz.Rect(*fig["clip"]) if fig.get("clip") else None
    pix = page.get_pixmap(dpi=fig.get("dpi", 200), clip=clip)
    out = os.path.join(CACHE, f"{fig['key']}.png")
    pix.save(out)
    print(f"  rendered {fig['key']}.png  {pix.width}x{pix.height}  "
          f"{os.path.getsize(out)//1024} KB")
    return out


def ghost_headers(content_type=None):
    import jwt
    from _secrets import require_ghost
    key, url = require_ghost()
    kid, secret = key.split(":")
    iat = int(time.time())
    token = jwt.encode({"iat": iat, "exp": iat + 300, "aud": "/admin/"},
                       bytes.fromhex(secret), algorithm="HS256",
                       headers={"alg": "HS256", "typ": "JWT", "kid": kid})
    h = {"Authorization": f"Ghost {token}"}
    if content_type:
        h["Content-Type"] = content_type
    return h, url.rstrip("/")


def upload(png_path, key):
    headers, url = ghost_headers()  # no Content-Type: requests sets multipart boundary
    with open(png_path, "rb") as f:
        r = requests.post(f"{url}/ghost/api/admin/images/upload/",
                          headers=headers,
                          files={"file": (f"{key}.png", f, "image/png")},
                          data={"purpose": "image"}, timeout=120)
    r.raise_for_status()
    return r.json()["images"][0]["url"]


def figure_block(fig, hosted_url):
    alt = html.escape(fig["alt"], quote=True)
    return (f'<figure class="wiki-figure">\n'
            f'  <img src="{hosted_url}" alt="{alt}" loading="lazy" '
            f'style="width:100%;height:auto;"/>\n'
            f'  <figcaption>{fig["caption"]}</figcaption>\n'
            f'</figure>')


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    do_upload = "--no-upload" not in sys.argv
    targets = [f for f in FIGURES if not args or f["key"] in args]
    if not targets:
        sys.exit(f"no manifest entry matches {args} — keys: "
                 f"{[f['key'] for f in FIGURES]}")
    for fig in targets:
        print(f"• {fig['key']}  →  {fig['entry']}")
        png = render(fig)
        if do_upload:
            hosted = upload(png, fig["key"])
            print(f"  hosted: {hosted}\n")
            print(figure_block(fig, hosted))
            print()


if __name__ == "__main__":
    main()
