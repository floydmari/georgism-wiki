# PLAN: Split "outcomes" into PROBLEMS and BENEFITS (Floyd direction, 2026-07-10)

## Motivation (Floyd, verbatim intent)

The current `outcomes/` category conflates two different kinds of claims:

1. **Problems / situational awareness** — empirical claims about the world that geoism
   *diagnoses* (e.g. "Corporate profits increasingly reflect economic rents", "High land
   rents suppress productivity", "Most of the modern rise in the capital share is land").
2. **Benefits** — empirical claims about what geoist *policy delivers* (e.g. "LVT dampens
   land speculation", "Resource-rent capture works where institutions are strong").

Goal: an advocate should be able to quickly read the problems geoists claim and feel
confident each is **real and backed by big-name research** (not just George's
observations), and that the claimed benefits are **empirically studied and backed**.

## Proposed taxonomy

- New categories: **`problems/`** (the diagnosis) and **`benefits/`** (the prescription's
  measured effects). Every page states one falsifiable claim in its title, carries
  `evidence_strength`, and leads with: the claim → the 2–4 strongest studies (big-name,
  peer-reviewed where possible) → honest limits/counter-evidence. Rent-gradient rules
  apply unchanged: land-core claims can be stated strongly when the evidence is strong;
  frontier claims (finance/IP/platform rents) stay attributed.
- **Phased migration** (don't break 400+ pages of links at once):
  - **Phase 1 — tag, don't move.** Add `claim_type: problem | benefit` frontmatter to every
    `outcomes/` page; build two index pages (`concepts/the-problems.md`,
    `concepts/the-benefits.md` or a front-page section) that group them for readers.
    Update lint to require `claim_type` on outcomes pages.
  - **Phase 2 — fill the gaps** (stub waves below), each new page born with `claim_type`.
  - **Phase 3 — directory split** once content settles: move files to `problems/` and
    `benefits/`, add redirects, rewrite inbound `/wiki/<slug>/` links (script-assisted),
    registry/inventory rebuild. Only after Floyd signs off on the Phase-1 grouping.

## Classification of existing outcomes pages (Phase 1 seed)

- **problem**: corporate-profits-increasingly-rents, high-land-rents-suppress-productivity,
  capital-share-rise-is-land, land-rent-could-fund-government (capacity = situational),
  public-investment-capitalizes-into-land, community-creates-land-value (mechanism/problem).
- **benefit**: lvt-dampens-speculation, resource-rent-capture-works,
  resource-rent-dividends-work, lvt-can-replace-capital-taxes-without-efficiency-loss,
  land-value-tax-can-be-progressive, split-rate-increases-construction,
  congestion-pricing-reduces-traffic.
- (T1 to finalize against the actual directory listing at execution time.)

## Gap analysis — new evidence-backed pages to build (stub waves)

### Problems (commonly written about; each needs ≥2 big-name anchors)
1. **Rising land values / housing costs drive poverty** (George's core thesis, modernized) —
   anchors to evaluate: housing-cost-adjusted poverty (US Supplemental Poverty Measure),
   Chetty et al. mobility geography, rent-burden literature, Albouy cost-of-living work;
   honest verdict on "has George's causal claim been studied as such?"
2. **Homelessness is a housing-cost problem** — Colburn & Aldern (2022) as the anchor;
   ties land supply/land cost to the most visible social failure.
3. **Housing unaffordability is a land problem, not a construction-cost problem** —
   Knoll-Schularick-Steger (80% of price rise is land — already Heavy-verified),
   Glaeser-Gyourko JEP (verified this shift), Hsieh-Moretti (verified).
4. **Rent-seeking drags growth** — Murphy-Shleifer-Vishny (1991/1993), Baumol
   (productive vs unproductive entrepreneurship); links existing rent-seeking concept.
5. **The young are locked out of land wealth (intergenerational divide)** — Resolution
   Foundation / OECD home-ownership-by-cohort data.
6. **Land underuse and speculative vacancy in high-demand cities** — Prosper speculative
   vacancies (already on wiki), vacant-lot literature (Gyourko-Krimmel).

### Benefits (Floyd's named misses first)
7. **Taxing land/rents increases productivity** — OECD WP620/EJ (verified, with Xing
   caveat carried honestly), Arnott-Stiglitz HGT, ATCOR/EBCOR as attributed theory;
   distinguish "least-harmful" evidence (strong) from "raises productivity" (weaker).
8. **Land value taxation reduces the cost of housing** — theory (tax capitalizes into
   land price: Oates verified this shift), empirics: Löffler-Siegloch German pass-through
   (verified), Plummer capitalization (verified), split-rate construction studies;
   honest distinction between "reduces land PRICES" (well-supported) vs "reduces RENTS
   paid" (weaker/mixed — say so).
9. **LVT/split-rate encourages construction and density** — exists
   (split-rate-increases-construction); deepen with Banzhaf-Lavery (verified this shift),
   Song-Zenou, Oates-Schwab Pittsburgh.
10. **Rent dividends reduce poverty and inequality** — Alaska evidence with the honest
    Goldsmith correction (this shift's purge), Jones-Marinescu, Segal (verified).

### Justice / reconciliation (frontier — normative + empirical hybrid; handle with care)
11. **Land justice and Indigenous reconciliation** — does geoism connect? Literature to
    triage: Aotearoa/NZ Māori land and rating history (NZ page primary-verified this
    shift), Canadian context (CWC's Basu mineral-wealth claim; treaty land entitlement),
    "Land Back" scholarship, George's own writings on indigenous dispossession
    (How the Indians Lost Their Land is Heavy-scanned). Present as: shared diagnosis
    (dispossession = enclosure of common wealth), divergent remedies (LVT vs restitution)
    — do NOT claim geoism = reconciliation; document the actual intersection honestly.
12. **Land and the Black-white wealth gap / recompense** — anchors: Pete Daniel
    *Dispossession* (Heavy-scanned), heirs'-property literature (USDA/Emergency Land
    Fund), Rothstein *The Color of Law* (wanted-books candidate), Darity & Mullen on
    reparations (frontier, attributed); Fairhope's segregation history as an honest
    in-movement failure case. Same rule: document the intersection, don't overclaim.

## Loop-system changes

- **New motion tags** in BACKLOG: `[PROBLEM-BUILD]` and `[BENEFIT-BUILD]` alongside
  FIND/READ&MINE/SYNTHESIZE/VERIFY/EXPAND.
- **Acceptance rule per page**: ≥2 independent big-name/peer-reviewed anchors fetched and
  claim-level verified before the page leaves stub status; `evidence_strength` graded
  (Strong / Suggestive / Contested / Theoretical); counter-evidence section mandatory.
- **Advocate-readability standard**: first screen = claim + 3 strongest citations + one
  honest-limits line. A reader should be able to quote the page in an argument in 30
  seconds and not get burned.
- **Wave pattern unchanged**: 3–4 subagents, 1–2 pages each, exclusive ownership,
  coordinator lints/inventories/commits; every quote spot-checked (re-grep) at T1.

## Immediate next actions (for the next session)
1. Phase-1 tagging + the two index pages (half a shift).
2. Stub wave A: problems 1–3. Stub wave B: benefits 7–8. Stub wave C: justice 11–12
   (T1 drafts the framing personally — highest editorial sensitivity).
3. Update EDITORIAL.md with the problems/benefits taxonomy and acceptance rule
   (short section; Floyd reviews via PR).
