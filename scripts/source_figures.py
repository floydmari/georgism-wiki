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
    {
        "key": "lacava-fig4",
        "entry": "research/la-cava-housing-capital-share.md",
        "pdf_url": "https://www.bis.org/publ/work572.pdf",
        "page": 16,
        "clip": (120, 100, 470, 362),
        "dpi": 250,
        "alt": ("Line chart of net housing capital income as a share of total net "
                "domestic income in the United States, 1960 to 2014. The actual "
                "series falls from about 6.6% to 5.3% by 1979, then climbs to "
                "about 8% by 2014 with a peak of 8.4%. A second series holding "
                "relative housing prices constant at their 1980 level stays flat "
                "between 5% and 6% for the whole period."),
        "caption": ("Figure 4 from the paper: net housing capital income as a "
                    "share of total net US domestic income, 1960–2014. Since 1980 "
                    "the actual share climbs from about 5.3% to 8% — but holding "
                    "relative housing prices at their 1980 level (lower line) it "
                    "goes nowhere. The rise in housing's income share is a rise "
                    "in the relative <em>price</em> of housing, not in housing "
                    "services produced. <span class=\"figure-credit\">Source: "
                    "La Cava, BIS Working Paper 572 / RBA RDP 2016-04 (2016), "
                    "Figure 4 — reproduced for comment and review.</span>"),
    },
    {
        "key": "loffler-siegloch-fig2",
        "entry": "research/loffler-siegloch-german-pass-through.md",
        "pdf_url": "https://docs.iza.org/dp14195.pdf",
        "page": 21,
        "clip": (92, 98, 500, 318),
        "dpi": 220,
        "alt": ("Event-study chart of the estimated effect of a one percentage "
                "point property tax increase on gross rents in German "
                "municipalities, four years before to four years after reform. "
                "Pre-reform estimates sit near zero; after reform the estimates "
                "rise, reaching the dashed full-pass-through benchmark line by "
                "year three, with wide confidence intervals."),
        "caption": ("Figure 2 from the working paper: event-study estimates of a "
                    "one-percentage-point <em>Grundsteuer</em> increase on gross "
                    "rents in German municipalities. Pre-trends are flat; about a "
                    "third of the tax reaches rents within two years and point "
                    "estimates hit full pass-through after three — the wiki's "
                    "strongest contrasting evidence on property-tax incidence. "
                    "(Germany's Grundsteuer taxes land <em>and</em> buildings; "
                    "the pure-land component is the part incidence theory says "
                    "cannot shift.) <span class=\"figure-credit\">Source: "
                    "Löffler &amp; Siegloch, IZA Discussion Paper 14195 (2021), "
                    "Figure 2 — reproduced for comment and review.</span>"),
    },

    {
        "key": "garden-cities-magnets",
        "entry": "books/garden-cities-of-to-morrow.md",
        "pdf_url": ("https://ia800505.us.archive.org/30/items/"
                    "gardencitiesofto00howa/gardencitiesofto00howa_bw.pdf"),
        "page": 21,
        "clip": (12, 78, 288, 400),
        "dpi": 300,
        "alt": ("Ebenezer Howard's 1898 'Three Magnets' diagram. Two magnets "
                "labeled Town and Country list their attractions and drawbacks — "
                "the Town's high wages but high rents and foul air; the Country's "
                "beauty of nature but low wages and lack of society. A third "
                "magnet, Town-Country, promises beauty of nature with social "
                "opportunity, low rents with high wages, pure air, freedom and "
                "co-operation. In the center: 'The People — where will they go?'"),
        "caption": ("The book's famous opening diagram: Town and Country each "
                    "attract and repel — only the planned Town–Country magnet "
                    "offers \"low rents, high wages\" together, the combination "
                    "Howard proposed to finance by capturing the community-created "
                    "rise in land values. <span class=\"figure-credit\">Source: "
                    "Ebenezer Howard, <em>Garden Cities of To-morrow</em> (1902 "
                    "edition), \"The Three Magnets\"; scan via Internet Archive. "
                    "Public domain.</span>"),
    },
    {
        "key": "kolbe-fig1",
        "entry": "research/kolbe-berlin-land-value-appraisal.md",
        "pdf_url": "https://edoc.hu-berlin.de/bitstream/handle/18452/20511/FORLand-2019-07.pdf",
        "page": 10,
        "clip": (120, 205, 480, 572),
        "dpi": 200,
        "alt": ("Choropleth map of Berlin colored by official expert-assessed "
                "standard land values (Bodenrichtwerte) in euros per square "
                "meter, capped at 1500. Values peak in a deep-red city center "
                "and fade to pale yellow at the periphery, with parks and water "
                "shown in green and blue."),
        "caption": None,  # embedded as the first panel of a paired figure
    },
    {
        "key": "kolbe-fig5",
        "entry": "research/kolbe-berlin-land-value-appraisal.md",
        "pdf_url": "https://edoc.hu-berlin.de/bitstream/handle/18452/20511/FORLand-2019-07.pdf",
        "page": 18,
        "clip": (120, 222, 480, 586),
        "dpi": 200,
        "alt": ("Map of Berlin colored by statistically estimated land values "
                "from kernel regression on transaction data, same color scale as "
                "the expert map: deep-red center, pale-yellow periphery, green "
                "parks and blue water — closely resembling the expert-assessed "
                "map above it."),
        "caption": None,  # embedded as the second panel of a paired figure
    },
    {
        "key": "sz-fig1",
        "entry": "research/saez-zucman-wealth-inequality.md",
        "pdf_url": "https://eml.berkeley.edu/~saez/SaezZucman2016QJE.pdf",
        "page": 3,
        "clip": (68, 74, 382, 240),
        "dpi": 300,
        "alt": ("Line chart of the share of total US household wealth owned by "
                "the richest 0.1% of families, 1913 to 2012. The share falls from "
                "about 25% in the late 1920s to about 7% in 1978, then climbs "
                "steadily back to about 22% by 2012 — a U-shaped century."),
        "caption": ("Figure I from the paper: the top 0.1% share of total US "
                    "household wealth, 1913–2012 — from ~25% in 1929 down to 7% "
                    "in 1978 and back to ~22% by 2012, the U-curve at the heart "
                    "of the modern wealth-concentration debate. "
                    "<span class=\"figure-credit\">Source: Saez &amp; Zucman "
                    "(2016), Figure I, <em>Quarterly Journal of Economics</em> "
                    "131(2), author-posted PDF — reproduced for comment and "
                    "review.</span>"),
    },
    {
        "key": "msv-fig2",
        "entry": "research/mian-sufi-verner-household-debt.md",
        "pdf_url": "https://bfi.uchicago.edu/wp-content/uploads/MianSufiVerner_worlddebt-1.pdf",
        "page": 55,
        "clip": (140, 219, 560, 510),
        "dpi": 220,
        "alt": ("Line chart of estimated effects of a three-year rise in debt to "
                "GDP on subsequent GDP growth over one to five year horizons, "
                "with confidence bands. The household-debt coefficient falls "
                "steadily to about minus 0.6 by year five; the non-financial "
                "firm-debt coefficient stays near zero."),
        "caption": ("Figure 2 from the working-paper version: the effect of a "
                    "three-year rise in debt-to-GDP on subsequent growth. A "
                    "household-debt expansion predicts progressively weaker "
                    "growth over the next five years, while an equal firm-debt "
                    "expansion predicts none — the household/mortgage credit "
                    "channel that drives boom-bust cycles. "
                    "<span class=\"figure-credit\">Source: Mian, Sufi &amp; "
                    "Verner, <em>Household Debt and Business Cycles "
                    "Worldwide</em> (working paper), Figure 2; published in "
                    "<em>Quarterly Journal of Economics</em> 132(4), 2017 — "
                    "reproduced for comment and review.</span>"),
    },
    {
        "key": "borio-g1",
        "entry": "research/borio-financial-cycle.md",
        "pdf_url": "https://www.bis.org/publ/work395.pdf",
        "page": 9,
        "clip": (70, 459, 548, 684),
        "dpi": 220,
        "alt": ("Chart of the financial cycle versus the business cycle in the "
                "United States, early 1970s to 2011. A blue financial-cycle line "
                "(credit and property prices) traces long, large waves peaking "
                "around 1989 and 2007; a red GDP-cycle line wiggles in much "
                "shorter, smaller cycles around zero. Grey bands mark NBER "
                "recessions; orange and green bars mark financial-cycle peaks "
                "and troughs."),
        "caption": ("Graph 1 from the paper: the financial cycle (credit plus "
                    "property prices, blue) against the GDP business cycle (red) "
                    "in the United States, 1970–2011. The financial cycle runs "
                    "far longer and larger than the business cycle — and its "
                    "peaks (1989, 2007) sit just before the deepest recessions. "
                    "<span class=\"figure-credit\">Source: Borio, BIS Working "
                    "Paper 395 (2012), Graph 1 — there reproduced from Drehmann, "
                    "Borio &amp; Tsatsaronis (2012) — reproduced for comment and "
                    "review.</span>"),
    },
    {
        "key": "cs-fig2",
        "entry": "research/case-shiller-2003-bubble.md",
        "pdf_url": "https://www.brookings.edu/wp-content/uploads/2003/06/2003b_bpea_caseshiller.pdf",
        "page": 12,
        "clip": (55, 94, 375, 622),
        "dpi": 220,
        "alt": ("Three stacked line charts of the ratio of home prices to per "
                "capita personal income, 1985 to 2002, for California, "
                "Massachusetts and Wisconsin. California swings between 6 and "
                "8.5, Massachusetts between 4.3 and 6.6, both in boom-bust "
                "waves; Wisconsin stays flat around 2.2 throughout."),
        "caption": ("Figure 2 from the paper: home prices relative to per-capita "
                    "income, 1985–2002. California and Massachusetts swing "
                    "through boom–bust waves while Wisconsin never leaves ~2.2 — "
                    "glamour-market prices decouple from income while most of "
                    "the country tracks fundamentals, the pattern Case and "
                    "Shiller used to diagnose bubble psychology in 2003. "
                    "<span class=\"figure-credit\">Source: Case &amp; Shiller "
                    "(2003), Figure 2, <em>Brookings Papers on Economic "
                    "Activity</em> 2003:2 — reproduced for comment and "
                    "review.</span>"),
    },
    {
        "key": "barr-fig4",
        "entry": "research/barr-smith-kulkarni-manhattan-land.md",
        "pdf_url": ("https://sasn.rutgers.edu/sites/default/files/2024-02/"
                    "Whats%20Mahattan%20Worth%20v3.1%20Oct%202015.pdf"),
        "page": 27,
        "clip": (70, 94, 437, 318),
        "dpi": 220,
        "alt": ("Line chart on a log scale of a Manhattan land values index and a "
                "Manhattan real estate sales price index, 1950 to 2014. The two "
                "series track each other: roughly flat to 1970, a deep trough in "
                "the mid-1970s for land, then both climbing steeply from about "
                "1980 to 2014, with land swinging harder than sales prices."),
        "caption": ("Figure 4 from the working-paper version: Manhattan land "
                    "values against real-estate sales prices (log scale), "
                    "1950–2014. Land tracks the market but swings harder — "
                    "collapsing in the 1970s, then climbing relentlessly from "
                    "1980 — the century-scale appreciation behind the paper's "
                    "estimate that Manhattan's land alone was worth about "
                    "$1.74 trillion by 2014. <span class=\"figure-credit\">"
                    "Source: Barr, Smith &amp; Kulkarni, <em>What's Manhattan "
                    "Worth?</em> (working paper, 2015), Figure 4; published in "
                    "<em>Regional Science and Urban Economics</em> 70, 2018 — "
                    "reproduced for comment and review.</span>"),
    },
    {
        "key": "dlu-fig1",
        "entry": "research/de-loecker-eeckhout-unger-markups.md",
        "pdf_url": "https://www.nber.org/system/files/working_papers/w23687/w23687.pdf",
        "page": 10,
        "clip": (170, 214, 448, 392),
        "dpi": 250,
        "alt": ("Line chart of the sales-weighted average markup of US firms, "
                "1960 to 2014. The line drifts between 1.16 and 1.32 until about "
                "1980, dips to 1.18, then climbs steadily to 1.67 by 2014."),
        "caption": ("Figure 1 from the working-paper version: the sales-weighted "
                    "average markup of US firms, 1960–2014. Flat around 1.2–1.3 "
                    "for two decades, then climbing from 1980 to 1.67 — the "
                    "average firm charged 67% over marginal cost in 2014 versus "
                    "18% in 1980, the rise-of-market-power finding this entry "
                    "documents. <span class=\"figure-credit\">Source: De "
                    "Loecker, Eeckhout &amp; Unger, NBER Working Paper 23687 "
                    "(2017), Figure 1; published in <em>Quarterly Journal of "
                    "Economics</em> 135(2), 2020 — reproduced for comment and "
                    "review.</span>"),
    },
    {
        "key": "piketty-53",
        "entry": "research/piketty-capital-21st-century.md",
        "pdf_url": ("http://piketty.pse.ens.fr/files/capital21c/en/"
                    "Piketty2014FiguresTables.pdf"),
        "page": 33,
        "clip": (35, 35, 815, 550),
        "dpi": 200,
        "alt": ("Line chart titled 'Figure 5.3. Private capital in rich "
                "countries, 1970-2010': the value of private capital as a "
                "percent of national income for the US, Japan, Germany, France, "
                "the UK, Italy, Canada and Australia. All eight countries rise "
                "from roughly 200-350% in 1970 to 400-700% by 2010, with "
                "Japan's late-1980s bubble spiking to 700% before falling "
                "back."),
        "caption": ("Figure 5.3 from the book's author-posted figure set: "
                    "private capital as a share of national income in eight rich "
                    "countries, 1970–2010 — from 2–3.5 years of national income "
                    "in 1970 to 4–7 years by 2010. This is the return-of-capital "
                    "trend whose composition the wiki's capital-share cluster "
                    "(Rognlie, Bonnet et al., Knoll et al.) decomposes into land. "
                    "<span class=\"figure-credit\">Source: Piketty, <em>Capital "
                    "in the Twenty-First Century</em> (2014), Figure 5.3, from "
                    "the freely posted figure files at "
                    "piketty.pse.ens.fr/capital21c — reproduced for comment and "
                    "review.</span>"),
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
            if fig.get("caption"):
                print(figure_block(fig, hosted))
                print()


if __name__ == "__main__":
    main()
