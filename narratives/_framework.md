---
title: "Narrative Framework — Design Index for the Narratives Section"
category: narratives
tags: [narratives, framework, index, strategy, editorial]
stub: false
excerpt: "The design blueprint for the wiki's twelve persuasive narratives: taxonomy, slugs, core claims, promoters, evidence maps, honest gaps, related objections, and deployment notes. This is the index T2 drafters work from; it is not itself a reader-facing narrative page."
last_reviewed: 2026-07-03
---

## Purpose

This page is the **framework index** for the `narratives/` section — the blueprint from
which the individual narrative pages are drafted. A *narrative* here is a persuasive
story used by advocates of [Georgism](/wiki/georgism/) and the
[land value tax](/wiki/land-value-tax/). Narrative pages **report** these stories in
NPOV voice ("advocates argue…"), map the evidence for and against them honestly, and
end with practical deployment guidance. They are the wiki's bridge between the evidence
base (`outcomes/`, `research/`) and real-world persuasion.

**Exemplar:** [Narrative: The Unearned Increment](/wiki/unearned-increment-narrative/)
is the completed model page. Match its structure, sourcing density, and tone.

## Drafting rules (binding for T2)

1. **Template** (EDITORIAL.md §6): Core Claim · Who Promotes It · Research That
   Supports It · Research That Challenges It — or Is Missing · Counter-Arguments and
   Georgist Responses · Historical Examples · How to Deploy It · See Also ·
   annotated Sources.
2. **Frontmatter:** `title`, `category: narratives`, `tags`, `stub: false`, `excerpt`,
   `narrative_type` (`moral|economic|practical|environmental|historical`),
   `supported_by` (existing **outcome** slugs), `related_people`, `related_places`
   (must resolve), `last_reviewed`.
3. **Slug convention:** where a narrative shares a name with an existing concept page,
   the narrative slug takes a `-narrative` suffix (slugs are global in Ghost — a
   duplicate is a lint error). Otherwise use the descriptive phrase below.
4. **Honesty is the persuasion strategy.** The "challenges / missing" section is
   mandatory and must be substantive. Never assert the narrative's claim in wiki voice;
   attribute it. Match language to evidence strength (EDITORIAL.md §4).
5. **Linking:** every narrative page links its evidence pages, its objection pages,
   at least two sibling narratives, and this index's exemplar where relevant, so no
   narrative page is an orphan. Never link a slug that does not exist yet — write
   planned slugs as inline code (as this page does).

## The Twelve Narratives

| # | Proposed slug | Title | Type | Core claim (short) |
|---|---------------|-------|------|--------------------|
| 1 | [`single-tax-narrative`](/wiki/single-tax-narrative/) ✅ | The Single Tax | practical | One levy on land values could replace taxation of work and enterprise |
| 2 | [`tax-land-not-labor`](/wiki/tax-land-not-labor/) ✅ | Tax Land, Not Labor | economic | Shift taxes off wages and investment onto land, which cannot shrink when taxed |
| 3 | [`unearned-increment-narrative`](/wiki/unearned-increment-narrative/) ✅ | The Unearned Increment | moral | Rising land values are created by the community, not the owner |
| 4 | [`the-rentier-economy`](/wiki/the-rentier-economy/) ✅ | The Rentier Economy | economic | Growing income flows reward asset ownership and rent extraction over production |
| 5 | [`community-creates-land-value`](/wiki/community-creates-land-value/) ✅ | The Community Creates Land Value | moral | Location value is produced by public investment and the surrounding community |
| 6 | [`land-speculation-causes-cycles`](/wiki/land-speculation-causes-cycles/) ✅ | Land Speculation Causes Boom and Bust | economic | Speculative land-price cycles drive credit booms and crashes |
| 7 | [`the-housing-crisis-is-a-land-crisis`](/wiki/the-housing-crisis-is-a-land-crisis/) ✅ | The Housing Crisis Is a Land Crisis | practical | Housing is dear because land is dear; tax land, free the land market |
| 8 | [`citizens-dividend-narrative`](/wiki/citizens-dividend-narrative/) ✅ | A Dividend from Common Wealth | moral | Rent from land and resources, shared equally, gives everyone a stake |
| 9 | `ecological-rent` | Green Georgism: Charging for the Earth | environmental | Pollution and extraction are unpaid takings of common natural wealth |
| 10 | [`the-tax-you-cant-dodge`](/wiki/the-tax-you-cant-dodge/) ✅ | The Tax You Can't Dodge | practical | Land cannot be hidden or moved offshore — the hardest base to avoid |
| 11 | `the-corruption-of-economics` | The Corruption of Economics | historical | Early neoclassical economics buried land as a factor, advocates argue |
| 12 | `the-great-land-robbery` | The Great Land Robbery | historical | Land titles descend from dispossession; rent capture is bloodless restitution |

Type balance: moral ×3, economic ×3, practical ×3, environmental ×1, historical ×2.

---

### 1. The Single Tax — [`single-tax-narrative`](/wiki/single-tax-narrative/) (practical) — ✅ DRAFTED

- **Core claim:** Government could be funded by a single levy on land values, replacing
  taxation of work, enterprise, and exchange — radical simplification with no penalty
  on production. The historical brand of the movement (see the
  [Single Tax](/wiki/single-tax/) concept page, which covers the doctrine; the
  narrative page covers its persuasive use).
- **Who promotes it:** [Henry George](/wiki/henry-george/) (*Progress and Poverty*,
  Book VIII), [Tom L. Johnson](/wiki/tom-l-johnson/), [Leo Tolstoy](/wiki/leo-tolstoy/),
  [Sun Yat-sen](/wiki/sun-yat-sen/); institutionally the
  [Schalkenbach Foundation](/wiki/schalkenbach-foundation/) and
  [Henry George School](/wiki/henry-george-school/).
- **Supporting evidence:** [Land rent could fund a large share of government](/wiki/land-rent-could-fund-government/)
  (contested); [LVT can replace capital taxes without efficiency loss](/wiki/lvt-can-replace-capital-taxes-without-efficiency-loss/)
  (strong); [Gaffney's hidden taxable capacity](/wiki/gaffney-hidden-taxable-capacity/);
  [ATCOR](/wiki/atcor/); [Goodhart & Hudson stimulus model](/wiki/goodhart-stimulus/).
- **Weak or missing:** the *full-replacement* arithmetic is the contested step — ATCOR
  is largely untested empirically, and no modern economy funds itself from land revenue
  alone ([Hong Kong](/wiki/hong-kong/) and [Singapore](/wiki/singapore/) are partial
  precedents). Draft must not present sufficiency as settled.
- **Objections:** [LVT can't raise enough revenue](/wiki/lvt-not-enough-revenue/);
  [transition wealth shock](/wiki/lvt-transition-wealth-shock/).
- **Historical anchors:** [1886 NYC mayoral election](/wiki/1886-nyc-mayoral-election/);
  [single-tax colonies](/wiki/single-tax-colonies/).
- **Deployment:** tax-simplification and libertarian-leaning audiences; note that most
  modern advocates soften to "a much larger land tax" rather than literal single-tax
  purism — the page should say so.

### 2. Tax Land, Not Labor — [`tax-land-not-labor`](/wiki/tax-land-not-labor/) (economic) — ✅ DRAFTED

- **Core claim:** Taxes on wages and investment discourage the activity that creates
  wealth; a tax on land value discourages nothing, because the land is there regardless.
  So the burden should shift from labor and capital onto land.
- **Who promotes it:** [Milton Friedman](/wiki/milton-friedman/) ("least bad tax"),
  [William Vickrey](/wiki/william-vickrey/), [Joseph Stiglitz](/wiki/joseph-stiglitz/),
  [Nicolaus Tideman](/wiki/nicolaus-tideman/); survey in
  [The Modern Georgism of Respected Economists](/wiki/modern-georgism-respected-economists/).
- **Supporting evidence:** the strongest-evidenced narrative of the twelve —
  [LVT can replace capital taxes without efficiency loss](/wiki/lvt-can-replace-capital-taxes-without-efficiency-loss/)
  ([Bonnet et al.](/wiki/bonnet-land-is-back/));
  [landlords cannot pass LVT to tenants](/wiki/landlords-cannot-pass-lvt-to-tenants/);
  [a land value tax can be progressive](/wiki/land-value-tax-can-be-progressive/)
  ([Schwerhoff et al., IMF](/wiki/schwerhoff-imf-equity-efficiency/));
  [deadweight loss](/wiki/deadweight-loss/); [Goodhart stimulus](/wiki/goodhart-stimulus/).
- **Weak or missing:** magnitudes in calibrated models vary; clean large-scale "big
  shift" natural experiments are rare ([Estonia](/wiki/estonia/),
  [Denmark](/wiki/denmark/), [Pennsylvania](/wiki/pennsylvania/) are partial).
- **Objections:** [land can't be assessed](/wiki/land-cannot-be-assessed/);
  [LVT is just a property tax](/wiki/lvt-is-just-a-property-tax/).
- **Deployment:** economists, centrists, fiscal-policy audiences. Lead with efficiency,
  close with progressivity — the equity-plus-efficiency combination is the hook.

### 3. The Unearned Increment — [`unearned-increment-narrative`](/wiki/unearned-increment-narrative/) (moral) — ✅ DRAFTED

The exemplar page; see it for the full map. Distinct from the
[unearned increment](/wiki/unearned-increment/) *concept* page, which defines the term;
the narrative page covers its persuasive career from
[Mill](/wiki/john-stuart-mill/) through the
[1909 People's Budget](/wiki/1909-peoples-budget/) to modern capitalization evidence.

### 4. The Rentier Economy — [`the-rentier-economy`](/wiki/the-rentier-economy/) (economic) — ✅ DRAFTED

- **Core claim:** A rising share of income flows to those who own assets and extract
  [economic rent](/wiki/economic-rent/) — above all land under housing — rather than to
  those who produce; taxing rent redirects reward from extraction to creation.
- **Who promotes it:** [Michael Hudson](/wiki/michael-hudson/) (FIRE-sector analysis),
  [Mariana Mazzucato](/wiki/mariana-mazzucato/),
  [Josh Ryan-Collins](/wiki/josh-ryan-collins/).
- **Supporting evidence:** [capital-share rise is land](/wiki/capital-share-rise-is-land/)
  (strong: [Rognlie](/wiki/rognlie-capital-share/), [Bonnet et al.](/wiki/bonnet-land-is-back/));
  [high land rents suppress productivity](/wiki/high-land-rents-suppress-productivity/)
  (emerging: [Bakker](/wiki/bakker-land-rents-tfp/));
  [Mapping Modern Economic Rents](/wiki/mazzucato-mapping-rents/);
  [rent-seeking](/wiki/rent-seeking/); [Rothschild & Scheuer](/wiki/rothschild-scheuer-rent-seeking/);
  [Richards, Taxes and Rents](/wiki/richards-taxes-and-rents/);
  [digital-age rents](/wiki/soil-to-servers-digital-rents/).
- **Weak or missing:** where "rent" ends and legitimate return begins is contested;
  the extension from land to platform and financial rents is analytical, not settled;
  and the step from diagnosis to *land* taxation specifically needs explicit argument.
- **Objections:** [the Austrian critique](/wiki/lvt-austrian-critique/) (denies the
  land/capital distinction the narrative rests on).
- **Deployment:** left-leaning, heterodox, and inequality-focused audiences; the
  Rognlie decomposition of Piketty's data is the anchor fact.

### 5. The Community Creates Land Value — [`community-creates-land-value`](/wiki/community-creates-land-value/) (moral) — ✅ DRAFTED

- **Core claim:** Location value is produced by the surrounding community and by public
  investment, not by the titleholder — so recovering it for public use returns value to
  the people who created it.
- **Who promotes it:** [Henry George](/wiki/henry-george/),
  [Joseph Stiglitz](/wiki/joseph-stiglitz/) (via the
  [Henry George Theorem](/wiki/henry-george-theorem/)),
  [Ebenezer Howard](/wiki/ebenezer-howard/); institutionally the
  [Lincoln Institute](/wiki/lincoln-institute/) under the label
  [land value capture](/wiki/land-value-capture/).
- **Supporting evidence:** [public investment capitalizes into land](/wiki/public-investment-capitalizes-into-land/)
  (strong); [public goods fundable from land rent](/wiki/public-goods-fundable-from-land-rent/)
  ([Arnott & Stiglitz](/wiki/arnott-stiglitz-henry-george-theorem/),
  [Stiglitz 1977](/wiki/stiglitz-theory-local-public-goods/),
  [Behrens et al. second-best](/wiki/behrens-hgt-second-best/));
  [tax capitalization](/wiki/tax-capitalization/).
- **Weak or missing:** the HGT equality holds only under optimality conditions; isolating
  how much of a parcel's value a *specific* public action created is empirically hard.
- **Objections:** [transition wealth shock](/wiki/lvt-transition-wealth-shock/);
  [assessment](/wiki/land-cannot-be-assessed/).
- **Deployment:** local officials and infrastructure-funding debates; make it concrete
  ("who paid for the subway that raised that lot's value?"). Overlaps deliberately with
  the [unearned-increment narrative](/wiki/unearned-increment-narrative/): this one is
  forward-looking finance, that one is backward-looking fairness.

### 6. Land Speculation Causes Boom and Bust — [`land-speculation-causes-cycles`](/wiki/land-speculation-causes-cycles/) (economic) — ✅ DRAFTED

- **Core claim:** Recurrent land-price speculation, financed by credit, drives the boom
  and the crash (advocates describe an [~18-year cycle](/wiki/18-year-land-cycle/));
  taxing land values would dampen the cycle at its source.
- **Who promotes it:** [Fred Harrison](/wiki/fred-harrison/) (called the 2008 crash in
  advance), [Fred Foldvary](/wiki/fred-foldvary/), [Akhil Patel](/wiki/akhil-patel/),
  [Mason Gaffney](/wiki/mason-gaffney/); George's own version is in *Progress and
  Poverty* ([research page](/wiki/progress-and-poverty/)).
- **Supporting evidence:** [LVT dampens land speculation](/wiki/lvt-dampens-land-speculation/)
  (moderate); [speculative vacancy](/wiki/speculative-vacancy/);
  [Oxford Review survey](/wiki/oxford-review-george-2025/);
  [land monopoly](/wiki/land-monopoly/).
- **Weak or missing:** the cycle literature is largely practitioner-authored, not
  peer-reviewed; the prediction record is anecdotal rather than systematic; direct
  causal evidence that LVT dampens cycles is thin
  ([Estonia](/wiki/tomson-estonia-lvt/) is suggestive only). The wiki also lacks an
  objection page for the mainstream view that cycles are chiefly monetary/financial —
  flag for the objections backlog.
- **Objections:** none on file yet (see gap above).
- **Deployment:** investors, macro commentators, and post-crash windows; keep the
  deterministic "18 years" attributed to Harrison/Patel, never asserted.

### 7. The Housing Crisis Is a Land Crisis — [`the-housing-crisis-is-a-land-crisis`](/wiki/the-housing-crisis-is-a-land-crisis/) (practical) — ✅ DRAFTED

- **Core claim:** Housing is expensive mainly because the land under it is expensive;
  taxing land values discourages speculation and underuse and — with permissive zoning —
  channels land into homes.
- **Who promotes it:** [Lars Doucet](/wiki/lars-doucet/),
  [Josh Ryan-Collins](/wiki/josh-ryan-collins/), [Dominic Frisby](/wiki/dominic-frisby/);
  [Prosper Australia](/wiki/prosper-australia/) (speculative-vacancy studies),
  [Center for Land Economics](/wiki/center-for-land-economics/).
- **Supporting evidence:** [split-rate increases construction](/wiki/split-rate-increases-construction/)
  (moderate–strong: [Oates & Schwab](/wiki/oates-schwab-pittsburgh/),
  [Plassmann & Tideman](/wiki/plassmann-tideman-construction/));
  [LVT improves housing affordability](/wiki/lvt-improves-housing-affordability/)
  (**contested** — the page itself says LVT is not sufficient alone);
  [capital-share rise is land](/wiki/capital-share-rise-is-land/) (housing is the
  channel); [Detroit LVT proposal](/wiki/detroit-lvt-proposal/).
- **Weak or missing:** the direct affordability evidence is weaker than the construction
  evidence, and [Singapore](/wiki/singapore/)/[Hong Kong](/wiki/hong-kong/) show value
  capture without cheap housing. The page must foreground the zoning pairing, not bury it.
- **Objections:** [capture didn't make housing cheap](/wiki/land-capture-didnt-make-housing-cheap/);
  [LVT is just a property tax](/wiki/lvt-is-just-a-property-tax/).
- **Deployment:** YIMBY/urbanist audiences and city politics; present LVT and zoning
  reform as a single package to preempt the strongest objection.

### 8. A Dividend from Common Wealth — [`citizens-dividend-narrative`](/wiki/citizens-dividend-narrative/) (moral) — ✅ DRAFTED

- **Core claim:** Rent from land and natural resources is common property; paid out as
  an equal [citizen's dividend](/wiki/citizens-dividend/), it gives every person a
  visible stake in the commons — a basic income funded by what nobody made.
- **Who promotes it:** [Henry George](/wiki/henry-george/) (public spending of rent),
  [Alanna Hartzok](/wiki/alanna-hartzok/); the geolibertarian strand
  ([geolibertarianism](/wiki/geolibertarianism/)) and parts of the modern UBI movement.
- **Supporting evidence:** [resource-rent dividends work](/wiki/resource-rent-dividends-work/)
  (strong — decades of the [Alaska Permanent Fund](/wiki/alaska-permanent-fund/));
  [land rent could fund government](/wiki/land-rent-could-fund-government/) (contested —
  sets the ceiling on dividend size); [resource rents](/wiki/resource-rents/).
- **Weak or missing:** Alaska's dividend is oil rent, not location rent — no
  jurisdiction has run a *land*-rent dividend at scale; and
  [Colombia evidence](/wiki/martinez-colombia-resource-rents/) warns that rent windfalls
  can weaken local tax effort and accountability. The narrative page must carry both.
- **Objections:** [not enough revenue](/wiki/lvt-not-enough-revenue/).
- **Deployment:** UBI and tech audiences; populist "your share of what we own together"
  framing; Alaska's cross-partisan durability is the anchor fact.

### 9. Green Georgism: Charging for the Earth — `ecological-rent` (environmental)

- **Core claim:** Pollution, carbon emission, and resource extraction are uncompensated
  takings of common natural wealth; charging for them extends the Georgist rent
  principle to ecology ([ecological Georgism](/wiki/ecological-georgism/)), and LVT
  itself is said to promote compact land use over sprawl.
- **Who promotes it:** [Alanna Hartzok](/wiki/alanna-hartzok/),
  [Karl Fitzgerald](/wiki/karl-fitzgerald/);
  [Earthsharing Australia](/wiki/earthsharing-australia/).
- **Supporting evidence:** [resource-rent dividends work](/wiki/resource-rent-dividends-work/)
  (for the capture side); [Tallinn density findings](/wiki/tomson-estonia-lvt/)
  (suggestive on compactness); [resource rents](/wiki/resource-rents/).
- **Weak or missing:** **the largest evidence gap of the twelve.** The wiki has no
  research page on LVT and sprawl or environmental outcomes, and none connecting
  carbon pricing to the rent framework. Source before drafting; expect heavy use of
  "advocates argue".
- **Objections:** [LVT hurts farmers](/wiki/lvt-hurts-farmers/) (adjacent rural/land-use
  worry); no ecological-specific objection page exists yet.
- **Deployment:** climate-concerned audiences; frame carbon charges as rent for using a
  commons rather than a punitive tax; do not oversell LVT itself as climate policy.

### 10. The Tax You Can't Dodge — [`the-tax-you-cant-dodge`](/wiki/the-tax-you-cant-dodge/) (practical) — ✅ DRAFTED

- **Core claim:** Land cannot be hidden, moved offshore, or re-domiciled; its ownership
  and value are public and local. That makes land the hardest tax base to avoid in an
  era of international tax competition and avoidance.
- **Who promotes it:** [Dominic Frisby](/wiki/dominic-frisby/),
  [Lars Doucet](/wiki/lars-doucet/); the "it can be taxed" theme of
  [Bonnet et al.](/wiki/bonnet-land-is-back/).
- **Supporting evidence:** [IMF, Taxing Immovable Property](/wiki/imf-taxing-immovable-property/);
  [World Bank property-tax determinants](/wiki/world-bank-property-tax-determinants/);
  [property tax raises welfare in developing countries](/wiki/property-tax-raises-welfare-developing/)
  ([Brockmeyer et al.](/wiki/brockmeyer-property-tax-developing/)).
- **Weak or missing:** avoidance mutates rather than vanishes — assessment appeals,
  exemption lobbying, and political suppression of valuations
  ([Murphy & Seegert](/wiki/murphy-seegert-implicit-land-taxes/) document systematic
  underassessment); ownership can still be obscured through entities even when the
  land cannot move. The page must treat "can't dodge" as *relative*, not absolute.
- **Objections:** [land can't be assessed](/wiki/land-cannot-be-assessed/).
- **Deployment:** anti-avoidance politics and state-capacity/development audiences;
  works across the spectrum wherever "the rich don't pay tax" resonates.

### 11. The Corruption of Economics — `the-corruption-of-economics` (historical)

- **Core claim:** Advocates — principally Gaffney — argue that early neoclassical
  economists, some patronized by landed and railroad interests, collapsed land into
  "capital" and thereby buried the classical three-factor analysis and George's reform
  case. (Named for the 1994 Gaffney–Harrison book.)
- **Who promotes it:** [Mason Gaffney](/wiki/mason-gaffney/)
  ([Neo-classical Economics as a Stratagem](/wiki/gaffney-neoclassical-stratagem/)),
  [Fred Harrison](/wiki/fred-harrison/).
- **Supporting evidence:** Gaffney's own documented history is the primary source;
  circumstantially, land's disappearance from and return to mainstream analysis
  ([Land is Back](/wiki/bonnet-land-is-back/),
  [modern Georgism of respected economists](/wiki/modern-georgism-respected-economists/)).
- **Weak or missing:** the *intentionality* thesis is contested historiography resting
  heavily on one scholar's work, with no independent peer-reviewed replication in the
  wiki; standard histories attribute the two-factor simplification to analytic
  convenience. The page must be written entirely as "Gaffney argues" and should link a
  counter-source once one is registered — flag for sourcing.
- **Objections:** none on file; the mainstream-historiography counter needs a home.
- **Deployment:** movement insiders and heterodox academics; use sparingly with general
  audiences (easily heard as conspiracy). Its best general-audience use is answering
  "if this is so good, why haven't I heard of it?"

### 12. The Great Land Robbery — `the-great-land-robbery` (historical)

- **Core claim:** Existing land titles descend from enclosure, conquest, and
  dispossession, not from anyone's production; capturing land rent going forward is
  restitution that requires no confiscation — the bloodless remedy, advocates argue.
- **Who promotes it:** [Henry George](/wiki/henry-george/)
  ([The Land Question](/wiki/the-land-question/);
  [A Perplexed Philosopher](/wiki/a-perplexed-philosopher/) against Spencer's
  recantation), [Alfred Russel Wallace](/wiki/alfred-russel-wallace/) (land
  nationalisation), [Leo Tolstoy](/wiki/leo-tolstoy/).
- **Supporting evidence:** primarily historical-textual (the George works above);
  [land monopoly](/wiki/land-monopoly/) for the structural claim.
- **Weak or missing:** the wiki has no page on enclosure or colonial land history —
  the narrative's factual backbone needs dedicated sourcing; and historical injustice
  does not by itself select LVT over rival remedies (restitution-in-kind,
  redistribution) — that bridge argument must be attributed, not assumed. Handle
  indigenous land claims with care: rent capture is not "land back".
- **Objections:** [transition wealth shock](/wiki/lvt-transition-wealth-shock/)
  (today's owners bought in good faith — the strongest reply).
- **Deployment:** justice-oriented audiences; emotionally the most powerful and the
  easiest to overreach — keep every historical claim specific, dated, and sourced.

---

## Cross-cutting notes for drafters

- **Audience map:** economists → 2; left/heterodox → 4, 12; libertarian → 1, 10;
  urbanist/YIMBY → 7; climate → 9; UBI/tech → 8; local government → 5; investors → 6;
  broad-moral → 3; movement-internal → 11.
- **Evidence-strength ranking** (strongest first, per the outcome pages):
  2 · 5 · 3 · 4 · 7 · 10 · 8 · 6 · 1 · 12 · 11 · 9. Narratives 9, 11, and 12 need new
  sources registered before their claims sections can be written to standard.
- **Inbound links:** when a narrative page ships, add a link *to* it from its concept
  twin (e.g., [unearned increment](/wiki/unearned-increment/) →
  [the narrative page](/wiki/unearned-increment-narrative/)), from the relevant
  outcome pages' See Also, and from [Georgism](/wiki/georgism/) once a
  "Narratives" section exists there.

## See Also

- [Narrative: The Unearned Increment](/wiki/unearned-increment-narrative/) — the exemplar page
- [Georgism](/wiki/georgism/) · [Land Value Tax](/wiki/land-value-tax/) — the ideas the narratives sell
- [LVT research priorities](/wiki/lvt-research-priorities-2025/) — the evidence agenda the gaps above feed into

## Sources

1. Henry George, *Progress and Poverty*, 1879. https://www.gutenberg.org/ebooks/55308 —
   used for the origin of narratives 1, 3, 5, 6, and 12 in George's own argument.
2. John Stuart Mill, *Principles of Political Economy*, 1848, Book V, Ch. II, §5.
   https://www.econlib.org/library/Mill/mlP.html — used for the pre-Georgist lineage of
   narrative 3 (the unearned increment).
3. Murray Rothbard, "The Single Tax: Economic and Moral Implications," FEE, 1957.
   https://mises.org/library/single-tax-economic-and-moral-implications — used as the
   representative opposing source narratives 3 and 4 must answer.
4. Evidence mappings above otherwise cite the wiki's own `outcomes/` and `research/`
   pages, each of which carries its external citations (navigation per EDITORIAL.md §1.7).
