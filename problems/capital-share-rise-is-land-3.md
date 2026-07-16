---
title: "Most of the modern rise in the capital share is land, not capital (v3 draft — evidence rail)"
category: problems
claim_type: problem
tags: [outcomes, capital-share, land, housing, inequality, piketty]
stub: false
evidence_strength: "Strong (independently replicated across US and European data)"
supported_by: [rognlie-capital-share, knoll-schularick-steger-house-prices, bonnet-land-is-back, la-cava-housing-capital-share, furman-orszag-firm-rents, bakker-land-rents-tfp, kerspien-madsen-strulik-buildings-labor-share, rognlie-piketty-note, stiglitz-land-credit-inequality, davis-heathcote-us-land]
challenged_by: [autor-superstar-firms, barkai-declining-shares]
excerpt: "Design-comparison draft v3: the claim page as a guided read with a sticky evidence rail replacing the sidebar — every wired source visible at all times while you read."
last_reviewed: 2026-07-16
---

<!--kg-card-begin: html-->
<style>
/* ── v3 evidence-rail template · page-scoped ─────────────────────────── */
.wiki-entry-aside{display:none!important}
.wiki-entry-body{grid-template-columns:1fr!important}
.wiki-entry-main{max-width:1340px!important;padding:48px clamp(24px,4vw,72px)!important}
.evx{display:grid;grid-template-columns:minmax(0,1fr) 400px;column-gap:56px;align-items:start}
.evx-main{max-width:680px}
.evx-note{font-family:var(--serif);font-style:italic;font-size:14px;color:var(--ink-2);margin:0 0 22px;line-height:1.5}
.evx-rail{position:sticky;top:16px;max-height:calc(100vh - 32px);overflow-y:auto;background:var(--surface,#faf0d2);border:1px solid var(--hair,#ecdcab);border-radius:10px;padding:18px 18px 10px;scrollbar-width:thin}
.evx-kicker{font-family:var(--sans);font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2)}
.evx-meter{display:flex;gap:2px;margin:12px 0 8px}
.evx-meter span{flex:1;height:12px;border-radius:3px;background:#1e82ab}
.evx-meter .ch{background:#e0481f}
.evx-count{font-family:var(--sans);font-size:13px;color:var(--ink);font-weight:600}
.evx-count b{color:#1e82ab}
.evx-count b.ch{color:#e0481f}
.evx-comp{font-family:var(--sans);font-size:11.5px;color:var(--ink-2);margin:3px 0 4px;line-height:1.5}
.evx-how{font-family:var(--serif);font-style:italic;font-size:12px;color:var(--ink-2);margin:8px 0 4px;line-height:1.45}
.evx-sub{font-family:var(--sans);font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--ink);margin:16px 0 8px}
.evc{background:var(--bg,#fff);border:1px solid var(--hair,#ecdcab);border-left:4px solid #1e82ab;border-radius:6px;padding:10px 12px;margin:0 0 10px}
.evc--ch{border-left-color:#e0481f}
.evc:target{box-shadow:0 0 0 2px rgba(30,130,171,.45)}
.evc--ch:target{box-shadow:0 0 0 2px rgba(224,72,31,.45)}
.evc-top{font-family:var(--sans);font-size:12.5px;font-weight:600;line-height:1.35;color:var(--ink)}
.evc-top a{border-bottom:none!important;color:var(--ink)}
.evc-top a:hover{color:var(--accent,#e0481f)}
.evc-num{display:inline-block;min-width:22px;color:#1e82ab;font-weight:700}
.evc--ch .evc-num{color:#e0481f}
.evc-venue{font-family:var(--sans);font-size:10.5px;letter-spacing:.04em;text-transform:uppercase;color:var(--ink-2);margin:3px 0 5px}
.evc-find{font-family:var(--serif);font-size:13.5px;line-height:1.5;color:var(--ink)}
.evc-tag{display:inline-block;font-family:var(--sans);font-size:10px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:#e0481f;margin-top:5px}
.evref{font-family:var(--sans);font-size:11px;font-weight:600;padding:0 6px;border:1px solid var(--hair,#ecdcab)!important;border-radius:10px;color:var(--ink-2)!important;white-space:nowrap;text-decoration:none}
.evref:hover{color:#1e82ab!important;border-color:#1e82ab!important}
.evx-jump{display:none}
.evx details{font-family:var(--sans);font-size:12.5px;color:var(--ink-2);margin:18px 0}
.evx details summary{cursor:pointer;font-weight:600;color:var(--ink)}
.evx details li{margin:6px 0;line-height:1.5}
@media(max-width:1080px){.evx{grid-template-columns:1fr}.evx-rail{position:static;max-height:none;margin-top:28px}.evx-jump{display:inline-block;font-family:var(--sans);font-size:12px;font-weight:600;margin:0 0 18px}}
</style>
<div class="evx">
<div class="evx-main">
<p class="evx-note">Design-comparison draft, v3 (2026-07-16). Same claim and evidence set as <a href="/wiki/capital-share-rise-is-land/">the page of record</a> and <a href="/wiki/capital-share-rise-is-land-2/">the v2 ledger draft</a>. Here the ledger becomes a standing evidence rail: the full roster stays in view while you read, the narrative cites into it by number, and the site sidebar is retired on this page so nothing competes with the proof point.</p>
<a class="evx-jump" href="#evidence-rail">Jump to the evidence rail ↓</a>
<h2>The Claim</h2>
<p>The rising share of national income flowing to "capital" in developed economies — popularised by Thomas Piketty's <em><a href="/wiki/piketty-capital-21st-century/">Capital in the Twenty-First Century</a></em> — is, when decomposed, <strong>almost entirely a rise in the housing sector</strong>, and therefore largely a rise in <strong>land rent</strong>. Reproducible capital (machines, equipment, structures) shows little long-run increase in its income share; land does.</p>
<h2>The Case, Guided</h2>
<p><strong>Start with the two core decompositions.</strong> <a href="/wiki/rognlie-capital-share/">Rognlie</a> <a class="evref" href="#ev-1">№1</a> showed that the long-run rise in the <em>net</em> capital share is concentrated in housing — strip housing out and capital's share is roughly flat. <a href="/wiki/bonnet-land-is-back/">Bonnet, Chapelle, Trannoy &amp; Wasmer</a> <a class="evref" href="#ev-2">№2</a> reached the same conclusion independently, with different countries and different methods: rising wealth-to-income ratios are driven by land prices, not produced capital. Two teams, two continents, one result — the "capital" in rising capital shares is mostly <strong>location</strong>.</p>
<p><strong>Then follow the chain that connects housing to land.</strong> <a href="/wiki/knoll-schularick-steger-house-prices/">Knoll, Schularick &amp; Steger</a> <a class="evref" href="#ev-3">№3</a> supply the price history: across 14 advanced economies, real house prices were roughly flat for eight decades, then surged after 1950 — and rising <em>land</em> prices explain about 80% of that boom. <a href="/wiki/davis-heathcote-us-land/">Davis &amp; Heathcote</a> <a class="evref" href="#ev-4">№4</a> provide the benchmark US series separating land from structures — residential land's share of housing value reached 46% by 2006. <a href="/wiki/la-cava-housing-capital-share/">La Cava</a> <a class="evref" href="#ev-6">№6</a> traces the income side down to the state level, where supply constraints concentrate the gains — a land-scarcity story.</p>
<p><strong>Then note how many independent angles corroborate it.</strong> <a href="/wiki/kerspien-madsen-strulik-buildings-labor-share/">Kerspien, Madsen &amp; Strulik</a> <a class="evref" href="#ev-5">№5</a> reach the real-estate reading from two centuries of factor-share data; <a href="/wiki/bakker-land-rents-tfp/">Bakker</a> <a class="evref" href="#ev-7">№7</a> restates the claim from the measurement side (recorded "capital income" is partly land rent); <a href="/wiki/stiglitz-land-credit-inequality/">Stiglitz</a> <a class="evref" href="#ev-8">№8</a> derives it from theory; <a href="/wiki/rognlie-piketty-note/">Rognlie's 2014 note</a> <a class="evref" href="#ev-9">№9</a> is the precursor result; and <a href="/wiki/furman-orszag-firm-rents/">Furman &amp; Orszag</a> <a class="evref" href="#ev-10">№10</a> connect the housing channel to the wider rents debate.</p>
<h2>The Counter-Case</h2>
<p>The honest counterweight comes from the firm-level literature — and it sits in the same rail, in red. <a href="/wiki/autor-superstar-firms/">Autor, Dorn, Katz, Patterson &amp; Van Reenen</a> <a class="evref" href="#ev-11">№11</a> explain the falling <em>labor</em> share without land at all: reallocation toward high-markup <a href="/wiki/superstar-firms/">"superstar firms,"</a> read substantially as an efficiency story. <a href="/wiki/barkai-declining-shares/">Barkai</a> <a class="evref" href="#ev-12">№12</a> measures a fall in <em>both</em> the labor share and the required-return capital share, offset by rising <strong>pure profits</strong> attributed to market power, not land. Neither paper rebuts the housing decomposition directly — they work on different data at a different level — but both cap how much of the economy-wide shift away from labor the land story can claim for itself. The wiki's <a href="/wiki/corporate-profits-increasingly-rents/">corporate-rents claim page</a> carries that side of the ledger in full.</p>
<h2>Strength of Evidence</h2>
<p><strong>Strong.</strong> The core result is independently replicated across US and European datasets by separate teams <a class="evref" href="#ev-1">№1</a><a class="evref" href="#ev-2">№2</a>, and the supporting chain runs through three literatures — price history <a class="evref" href="#ev-3">№3</a><a class="evref" href="#ev-4">№4</a>, factor shares <a class="evref" href="#ev-5">№5</a><a class="evref" href="#ev-6">№6</a>, and growth accounting <a class="evref" href="#ev-7">№7</a> — that share neither data nor methods. Two caveats the rail keeps visible: the challengers are published in top field journals, so the counter-case is not fringe — it limits the claim's <em>scope</em> (how much of the labor-share decline land explains), not its core; and Kerspien et al. <a class="evref" href="#ev-5">№5</a> frame the appreciating asset as "buildings," so the "buildings are land" step is supplied by Knoll et al. <a class="evref" href="#ev-3">№3</a>, not by that paper alone.</p>
<h2>Why It Matters</h2>
<p>If inequality's capital dimension is really a <strong>land</strong> dimension, a tax on land values targets the actual driver — without the efficiency cost of taxing productive capital. This connects 21st-century inequality research directly to Henry George's 19th-century diagnosis in <em><a href="/wiki/progress-and-poverty/">Progress and Poverty</a></em>.</p>
<h2>Context — Not in the Rail</h2>
<p>Adjacent evidence, deliberately excluded from the rail because it is not wired as direct support or challenge: <a href="/wiki/mckinsey-global-balance-sheet/">McKinsey's global balance sheet</a> (real estate dominates global net worth), <a href="/wiki/blanco-spain-two-lands/">Blanco et al. on Spain</a> (a national case study), <a href="/wiki/hornbeck-moretti-tfp-incidence/">Hornbeck &amp; Moretti</a> ("the split between labor and land is potentially more consequential… than the split between labor and capital"), and the concepts <a href="/wiki/economic-rent/">Economic Rent</a>, <a href="/wiki/unearned-increment/">Unearned Increment</a>, and <a href="/wiki/land-value-tax/">Land Value Tax</a>.</p>
<details>
<summary>Full citations (bibliographic detail for every rail card)</summary>
<ol>
<li>Matthew Rognlie (2015), "Deciphering the Fall and Rise in the Net Capital Share," <em>Brookings Papers on Economic Activity</em> — used for card №1. <a href="/wiki/rognlie-capital-share/">wiki summary</a> · <a href="https://mattrognlie.com/brookings_capitalshare.pdf">PDF</a></li>
<li>Odran Bonnet, Guillaume Chapelle, Alain Trannoy &amp; Étienne Wasmer (2021), "Land is Back, It Should Be Taxed, It Can Be Taxed," <em>European Economic Review</em> — used for card №2. <a href="/wiki/bonnet-land-is-back/">wiki summary</a></li>
<li>Katharina Knoll, Moritz Schularick &amp; Thomas Steger (2017), "No Price Like Home: Global House Prices, 1870–2012," <em>American Economic Review</em> 107(2) — used for card №3. <a href="/wiki/knoll-schularick-steger-house-prices/">wiki summary</a> · <a href="https://doi.org/10.1257/aer.20150501">DOI</a></li>
<li>Morris A. Davis &amp; Jonathan Heathcote (2007), "The Price and Quantity of Residential Land in the United States," <em>Journal of Monetary Economics</em> 54(8) — used for card №4. <a href="/wiki/davis-heathcote-us-land/">wiki summary</a> · <a href="https://doi.org/10.1016/j.jmoneco.2007.06.023">DOI</a></li>
<li>Jacob Kerspien, Jakob B. Madsen &amp; Holger Strulik (2025), "Capital Composition and the Decline of the Labor Share: Why Buildings Matter," <em>European Economic Review</em> — used for card №5. <a href="/wiki/kerspien-madsen-strulik-buildings-labor-share/">wiki summary</a></li>
<li>Gianni La Cava (2016), "Housing Prices, Mortgage Interest Rates and the Rising Share of Capital Income," RBA Research Discussion Paper — used for card №6. <a href="/wiki/la-cava-housing-capital-share/">wiki summary</a></li>
<li>Bas Bakker (2023), "Unveiling the Hidden Impact of Urban Land Rents on Total Factor Productivity," IMF working paper — used for card №7. <a href="/wiki/bakker-land-rents-tfp/">wiki summary</a></li>
<li>Joseph E. Stiglitz (2015), "New Theoretical Perspectives on the Distribution of Income and Wealth among Individuals: Part IV: Land and Credit," NBER WP 21192 — used for card №8. <a href="/wiki/stiglitz-land-credit-inequality/">wiki summary</a></li>
<li>Matthew Rognlie (2014), "A Note on Piketty and Diminishing Returns to Capital," working note — used for card №9. <a href="/wiki/rognlie-piketty-note/">wiki summary</a></li>
<li>Jason Furman &amp; Peter Orszag (2015), "A Firm-Level Perspective on the Role of Rents in the Rise in Inequality," conference paper — used for card №10. <a href="/wiki/furman-orszag-firm-rents/">wiki summary</a></li>
<li>David Autor, David Dorn, Lawrence Katz, Christina Patterson &amp; John Van Reenen (2020), "The Fall of the Labor Share and the Rise of Superstar Firms," <em>QJE</em> 135(2) — used for card №11. <a href="/wiki/autor-superstar-firms/">wiki summary</a> · <a href="https://www.nber.org/papers/w23396">NBER</a></li>
<li>Simcha Barkai (2020), "Declining Labor and Capital Shares," <em>The Journal of Finance</em> 75(5) — used for card №12. <a href="/wiki/barkai-declining-shares/">wiki summary</a> · <a href="https://doi.org/10.1111/jofi.12909">DOI</a></li>
</ol>
</details>
</div>
<aside class="evx-rail" id="evidence-rail">
<span class="evx-kicker">The Evidence — at a glance</span>
<div class="evx-meter"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span class="ch"></span><span class="ch"></span></div>
<div class="evx-count"><b>10 supporting</b> · <b class="ch">2 challenging</b></div>
<div class="evx-comp">Supporting: 5 peer-reviewed/flagship journals · 2 official-institution · 3 working/conference papers. Challenging: both top field journals.</div>
<p class="evx-how">Every source wired to this claim appears exactly once below, strongest first. The narrative cites cards by number. Full detail lives on each linked page.</p>
<div class="evx-sub">Supporting (10)</div>
<div class="evc" id="ev-1"><div class="evc-top"><span class="evc-num">1</span><a href="/wiki/rognlie-capital-share/">Rognlie (2015)</a></div><div class="evc-venue">Brookings Papers · decomposition · US + 7 economies</div><div class="evc-find">The long-run rise in the <strong>net</strong> capital share is concentrated in housing; ex-housing, capital's share is roughly flat.</div></div>
<div class="evc" id="ev-2"><div class="evc-top"><span class="evc-num">2</span><a href="/wiki/bonnet-land-is-back/">Bonnet et al. (2021)</a></div><div class="evc-venue">European Economic Review · decomposition · France/Europe</div><div class="evc-find">Rising wealth-to-income ratios are driven by <strong>land prices</strong>, not produced capital — independent replication of №1.</div></div>
<div class="evc" id="ev-3"><div class="evc-top"><span class="evc-num">3</span><a href="/wiki/knoll-schularick-steger-house-prices/">Knoll, Schularick &amp; Steger (2017)</a></div><div class="evc-venue">American Economic Review · price history · 14 economies, 1870–2012</div><div class="evc-find">Rising <strong>land</strong> prices explain about 80% of the global house-price boom since World War II.</div></div>
<div class="evc" id="ev-4"><div class="evc-top"><span class="evc-num">4</span><a href="/wiki/davis-heathcote-us-land/">Davis &amp; Heathcote (2007)</a></div><div class="evc-venue">J. Monetary Economics · land-price series · US</div><div class="evc-find">Residential land's share of US housing value reached <strong>46% by 2006</strong>; land prices ~3× more volatile than structures.</div></div>
<div class="evc" id="ev-5"><div class="evc-top"><span class="evc-num">5</span><a href="/wiki/kerspien-madsen-strulik-buildings-labor-share/">Kerspien, Madsen &amp; Strulik (2025)</a></div><div class="evc-venue">European Economic Review · panel · 16 economies, 2 centuries</div><div class="evc-find">The post-1980 labour-share decline is driven by the rising real price of <strong>buildings</strong>, not the quantity of capital.</div></div>
<div class="evc" id="ev-6"><div class="evc-top"><span class="evc-num">6</span><a href="/wiki/la-cava-housing-capital-share/">La Cava (2016)</a></div><div class="evc-venue">Reserve Bank of Australia · income-side decomposition · US data</div><div class="evc-find">Housing's income-share rise is overwhelmingly <strong>imputed rent</strong>, concentrated in supply-constrained states.</div></div>
<div class="evc" id="ev-7"><div class="evc-top"><span class="evc-num">7</span><a href="/wiki/bakker-land-rents-tfp/">Bakker (2023)</a></div><div class="evc-venue">IMF working paper · measurement</div><div class="evc-find">Growth decompositions overstate capital's contribution by missing the capital income that is really <strong>urban land rent</strong>.</div></div>
<div class="evc" id="ev-8"><div class="evc-top"><span class="evc-num">8</span><a href="/wiki/stiglitz-land-credit-inequality/">Stiglitz (2015)</a></div><div class="evc-venue">NBER working paper · theory</div><div class="evc-find">From first principles: most of the rising wealth-to-income ratio reflects rising <strong>land values</strong>, not productive capital.</div></div>
<div class="evc" id="ev-9"><div class="evc-top"><span class="evc-num">9</span><a href="/wiki/rognlie-piketty-note/">Rognlie (2014)</a></div><div class="evc-venue">Working note · precursor to №1</div><div class="evc-find">First showed the rise concentrates in housing/land; diminishing returns undercut Piketty's mechanical logic.</div></div>
<div class="evc" id="ev-10"><div class="evc-top"><span class="evc-num">10</span><a href="/wiki/furman-orszag-firm-rents/">Furman &amp; Orszag (2015)</a></div><div class="evc-venue">Conference paper · firm-level returns</div><div class="evc-find">Partial support: flags land-use-driven housing rents as an inequality contributor alongside firm-level rents.</div></div>
<div class="evx-sub">Challenging (2)</div>
<div class="evc evc--ch" id="ev-11"><div class="evc-top"><span class="evc-num">11</span><a href="/wiki/autor-superstar-firms/">Autor et al. (2020)</a></div><div class="evc-venue">Quarterly Journal of Economics · firm-level empirics</div><div class="evc-find">The falling labor share is explained by reallocation to high-markup "superstar firms" — no land needed.</div><span class="evc-tag">Challenges — scope cap</span></div>
<div class="evc evc--ch" id="ev-12"><div class="evc-top"><span class="evc-num">12</span><a href="/wiki/barkai-declining-shares/">Barkai (2020)</a></div><div class="evc-venue">Journal of Finance · factor-share decomposition</div><div class="evc-find">Labor <em>and</em> required-return capital shares both fell; the offset is <strong>pure profits</strong> from market power, not land.</div><span class="evc-tag">Challenges — scope cap</span></div>
</aside>
</div>
<!--kg-card-end: html-->
