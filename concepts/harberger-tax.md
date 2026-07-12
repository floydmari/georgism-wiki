---
title: "Harberger Tax (COST)"
category: concepts
tags: [concepts, harberger-tax, cost, radical-markets, self-assessment]
stub: false
excerpt: "A self-assessed property tax under which owners name their own price and must sell at it — a modern extension of Georgist principles popularized by Radical Markets."
---

## Definition

A **Harberger tax**, also called a **Common Ownership Self-Assessed Tax (COST)**, requires owners to **self-assess** the value of an asset, pay a tax on that value, and **stand ready to sell at the declared price** to any buyer. This neatly solves the assessment problem (owners reveal true values) and the holdout problem (assets are continuously for sale), while taxing the value of holding the asset.

## Relationship to Georgism

COST is a generalisation of the Georgist idea: it captures the holding value of assets — most powerfully **land** — and discourages unproductive hoarding. Applied to land, it functions like a self-assessed [land value tax](/wiki/land-value-tax/) that also keeps sites liquid. It directly addresses the [objection that land can't be assessed](/wiki/land-cannot-be-assessed/).

## Origins and Reception

Named after economist Arnold Harberger, the mechanism was popularised by Eric Posner and Glen Weyl in [*Radical Markets*](/wiki/radical-markets/) (2018). As the wiki's [book page](/wiki/posner-weyl-radical-markets/) details, COST is a deliberate hybrid of Henry George's land value tax and Harberger's 1962 self-assessment proposal — owners declare their property's value publicly, pay tax on the declaration, and must sell to any bidder at that price — and it **departs from George** by extending the tax to *all* property, capital included, not just land.

It has been influential in technology and crypto circles — Ethereum's [Vitalik Buterin endorsed it](/wiki/buterin-on-radical-markets/) as a tool for property and digital-asset reform, exploring applications to domain names and other scarce digital resources; that endorsement is part of why the modern Georgist revival has strong roots in the tech world. COST-style designs also appear among the candidate instruments for [taxing platform and data rents](/wiki/taxing-tech-rents/).

## Mechanism-Design Kin

The self-assessment idea recurs across the Georgist mechanism-design tradition:

- **[Sun Yat-sen](/wiki/sun-yat-sen/)** proposed that Chinese landowners self-declare land values, with the state taxing those values and capturing the increment — an early-20th-century precursor of the same self-assessment logic.
- **[Tideman and Plassmann's land-assembly mechanisms](/wiki/tideman-plassmann-land-assembly/)** use auctions and self-assessed values to defeat the [holdout problem](/wiki/holdout-problem/), a friction closely related to the one COST's continuously-for-sale rule dissolves.

## Evidence

How much do we actually know about whether self-assessed taxation works? The honest answer is: **the theory is well developed, the field record is thin, and the most COST-like feature — the standing obligation to sell to any bidder — has never been implemented at scale.** The evidence should be graded accordingly.

**Theory and mechanism design (strong).** The self-assessment idea is old — Arnold Harberger proposed it for Latin American property taxation in the 1960s — and the modern formalisation is robust. E. Glen Weyl and Anthony Lee Zhang's "Depreciating Licenses" (*American Economic Journal: Economic Policy*, 2022) models the core trade-off directly: perpetual ownership gives owners strong incentives to invest in an asset but "impede[s] efficient reallocation of resources to higher-valued entrants," while a depreciating license "owner annually announces a valuation at which she commits to sell" and pays a fee proportional to it, producing "time-stationary investment incentives" while keeping the asset allocable.[3] The key result is that the *optimal* tax rate is strictly positive but less than full — i.e. **partial** common ownership, not the 100% turnover rate a naive reading of COST implies. Earlier peer-reviewed variants (e.g. Dieter Gstach's self-assessment mechanism in *Metroeconomica*, 2009, where the authority commits to buy some declared parcels to induce truthful reporting) reach compatible conclusions.[4] This is genuine mechanism-design theory, not just advocacy.

**Field precedent (partial, one long-running case).** The closest thing to a real-world test is not a modern COST pilot but **[Taiwan](/wiki/taiwan/)'s self-assessment regime**, rooted in [Sun Yat-sen](/wiki/sun-yat-sen/)'s "equalization of land rights." Under the Equalization of Land Rights Act, owners self-declare their land value, and — crucially — the state carries a **purchase right against under-declaration**: "If the land value declared by the owner is lower than 80 percent of the announced land values, the government reserves the right to purchase his land at the announced land value."[5] This is a live, decades-old instance of the COST enforcement logic (name your price, and the state may take it at that price). But it is a *weak* form: the purchase right is a one-directional floor against low-balling, anchored to an official "announced value," not the continuous, symmetric, must-sell-to-any-private-buyer market that COST envisions. It disciplines self-assessment; it does not turn land into a perpetually contestable auction.

**What is missing (the honest gap).** There is **no controlled field trial** of a full Harberger tax on land, and — as the wiki's [*Radical Markets*](/wiki/radical-markets/) page notes — direct behavioral evidence on how accurately real owners self-assess under a genuine must-sell rule, and on how much the forced-sale "anxiety cost" of losing a home one values above its price would deter participation, remains thin. Buterin's own sympathetic treatment flags exactly this: the mechanism trades allocative efficiency against owners' security of possession, and where that trade lands for homes (as opposed to spectrum, domain names, or other fungible licenses) is an empirical question the literature has not settled.[6] **Grade: strong theory, one partial institutional precedent, essentially no field or large-sample experimental evidence for COST as such — most confident for fungible, low-attachment assets (licenses, digital resources), least tested for owner-occupied land.**

## Role in Answering Objections

- Against the valuation strand of the [Austrian critique](/wiki/lvt-austrian-critique/), COST shows owners can be made to reveal values directly, so assessment need not depend on state estimation.
- Against the [public-choice critique](/wiki/public-choice-critique/), self-assessment is cited as a discretion-removing design: it takes valuation out of assessors' and politicians' hands.

## See Also

- [Weyl & Zhang (2017): Depreciating Licenses](/wiki/weyl-zhang-depreciating-licenses/) — the academic paper formalizing the investment-vs-allocative-efficiency tradeoff that underpins the COST/Harberger-tax design
- [Arnold Harberger](/wiki/arnold-harberger/) — the Chicago economist whose 1962 self-assessment proposal is the namesake and origin of this mechanism
- [Radical Markets](/wiki/radical-markets/) — the broader Posner & Weyl program this mechanism comes from
- [Posner & Weyl, *Radical Markets* (book page)](/wiki/posner-weyl-radical-markets/) — the full COST design, lineage, and departures from George
- [Land Value Tax](/wiki/land-value-tax/) · [Land Monopoly](/wiki/land-monopoly/) · [Holdout Problem](/wiki/holdout-problem/)

## Sources

1. Eric Posner & Glen Weyl (2018), *Radical Markets*, Princeton University Press — used for the COST design and its Georgist lineage (A-claims; Deep scan on [the book page](/wiki/posner-weyl-radical-markets/)). [Publisher](https://press.princeton.edu/books/hardcover/9780691177502/radical-markets)
2. Vitalik Buterin (2018), "On Radical Markets" — used for the sympathetic-critique reception (C-claims). [wiki summary](/wiki/buterin-on-radical-markets/) · [Essay](https://vitalik.eth.limo/general/2018/04/20/radical_markets.html)
3. E. Glen Weyl & Anthony Lee Zhang, "Depreciating Licenses," *American Economic Journal: Economic Policy* 14(3), 2022. [DOI 10.1257/pol.20200426](https://doi.org/10.1257/pol.20200426) · working-paper text [PDF (Stanford)](https://inequality.stanford.edu/sites/default/files/Zhang-paper.pdf) — mechanism-design theory; used (verified against the working-paper text) for the investment-vs-reallocation trade-off, the depreciating-license design ("owner annually announces a valuation at which she commits to sell"), and the result that the optimal fee corresponds to *partial* rather than full common ownership. (B-claim; theory.)
4. Dieter Gstach, "A Property Taxation Mechanism With Self-Assessment," *Metroeconomica* 60(3), 2009, pp. 400–408. [IDEAS/RePEc](https://ideas.repec.org/a/bla/metroe/v60y2009i3p400-408.html) — peer-reviewed self-assessment variant in which the tax authority commits to purchase some declared parcels to induce truthful reporting; cited as compatible theoretical support. (B-claim; theory.)
5. The Equalization of Land Rights Act (Republic of China / Taiwan), Article 16, Laws & Regulations Database of the Republic of China. [law.moj.gov.tw](https://law.moj.gov.tw/ENG/LawClass/LawAll.aspx?pcode=D0060009) — used (verified quotation) for the self-declaration regime and the government's purchase right where the owner's declared land value falls below 80% of the announced value; the closest live field precedent for the COST enforcement mechanism, and its limits. (A-claim; primary legal text.)
6. Vitalik Buterin (2018), "On Radical Markets," and the wiki's [*Radical Markets*](/wiki/radical-markets/) page — used for the honest gap: the forced-sale security-of-possession trade-off and the thinness of behavioral evidence on real-world self-assessment accuracy, especially for owner-occupied homes. [Essay](https://vitalik.eth.limo/general/2018/04/20/radical_markets.html) (C-claim.)
