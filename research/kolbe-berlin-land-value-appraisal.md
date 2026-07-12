---
title: "Land Value Appraisal Using Statistical Methods (Kolbe et al., Berlin)"
category: research
tags: [research, assessment, cama, hedonic-regression, valuation, lvt, germany]
authors: [Jens Kolbe, Rainer Schulz, Martin Wersing, Axel Werwatz]
year: 2019
tier: Important
source_url: https://edoc.hu-berlin.de/bitstream/handle/18452/20511/FORLand-2019-07.pdf
stub: false
excerpt: "The Berlin study behind the '0.845 correlation' assessability claim — statistical land-value estimates from property transactions matched against the city's official expert-assessed land-value map (BRW)."
last_reviewed: 2026-07-12
bears_on_objections: [land-cannot-be-assessed, lvt-austrian-critique]
---

## Summary

*Land Value Appraisal Using Statistical Methods* (FORLand Working Paper 07, 2019) by **Jens Kolbe, Rainer Schulz, Martin Wersing and Axel Werwatz** is the load-bearing empirical source behind the modern Georgist claim — popularised by [Lars Doucet](/wiki/doucet-does-georgism-work/) — that unimproved land value can be estimated at scale from ordinary transaction data. Written amid Germany's property-tax reform debate, it takes as its benchmark Berlin's official expert-assessed **standard land-value map** (*Bodenrichtwerte*, or **BRW**) — land values that local surveyor commissions (GAA) are already legally obliged to produce — and asks whether purely statistical methods, fed with the transactions the commissions collect, can reproduce that expert map.[1]

The paper's motivation is explicitly the cost objection to a value-based tax: "In light of the recent property tax reform discussion in Germany, it has been argued that a value-based tax therefore cannot be implemented at a reasonable cost."[1] Its answer is that "the methods are capable of producing land value estimates that match up well with expert based assessments" (abstract).[1]

## What It Establishes

The authors apply an escalating ladder of estimators to Berlin data and compare each to the BRW map:

- **Kernel regression** on sales of *undeveloped* land reproduces the expert map only in the outlying areas where vacant-land sales actually occur. Its correlation with the BRW values is **0.704**, and crucially it "could thus only be computed away from the city centre where sales of undeveloped land occurred" — in the dense, fully built-up core, where virtually all land is developed, it produces no estimate at all.[1] This is the concrete basis for the wiki's recurring note that pure-land interpolation fails in city centres.
- **Semiparametric regression** solves that gap by using transactions of *developed* properties: a first step differences out the land component to estimate building-characteristic coefficients from geographically close pairs, and a second step (adaptive-weights smoothing) recovers the land-value surface. Reporting the validation from their earlier study, the authors write: "In Kolbe et al. (2012), we calculated the correlation between the BRW values and our semiparametric land value estimates based on house transactions only. For this subset of the data, we found a strong positive correlation of **0.845**."[1]

The **0.845** figure — the one Doucet headlines — is therefore the correlation between the semiparametric estimates (from house transactions only) and the official expert map, carried over from the authors' 2012 companion paper; the 2019 working paper reproduces it as the validation for the semiparametric approach. Both figures are correlations against an *expert* benchmark (the BRW), not against realised sale prices, because — as the paper notes — no market benchmark for pure land value exists in built-up areas, which is precisely why the estimation problem is hard.[1]

## Relation to the Assessability Question

This paper is the primary evidence node under two wiki claims that otherwise rest on second-hand retelling:

- On the [mass-appraisal-methods](/wiki/mass-appraisal-methods/) concept page, the description of how kernel interpolation fails in the city centre and why semiparametric methods add building characteristics traces directly to Figures 5–8 here — not merely to Doucet's account of them.
- On the [land-cannot-be-assessed](/wiki/land-cannot-be-assessed/) objection, it supplies the strongest single quantitative rebuttal to "you cannot separate land value from building value in a dense city": a statistical model fed only with transaction data reaches ~0.85 correlation with the professional expert assessment across an entire major city.

It also grounds — with a verbatim figure — the number Doucet relays in [*Does Georgism Work?* Part 3](/wiki/doucet-does-georgism-work/). Doucet's gloss (0.845 semiparametric vs 0.704 kernel, the latter unable to estimate the city centre) is faithful to the paper; the one nuance the wiki should preserve is that 0.845 is a *house-transactions-only subset* result imported from Kolbe et al. (2012), and both correlations are validated against the expert BRW map rather than against an independent ground truth.

## Companion Paper: Adaptive-Weights Smoothing (Kolbe et al. 2015)

The **adaptive-weights-smoothing (AWS)** method that produces the nonparametric land-value surface in this line of work has its own dedicated publication: **Jens Kolbe, Rainer Schulz, Martin Wersing & Axel Werwatz, "Identifying Berlin's land value map using adaptive weights smoothing," *Computational Statistics*, Vol. 30, Issue 3 (2015), pp. 767–790** (a free discussion-paper version circulated as SFB 649 Discussion Paper 2015-003 / Humboldt-Universität edoc).[2] It is the methodological engine behind the "nonparametric adaptive-weights smoothing" that [Doucet](/wiki/doucet-does-georgism-work/) lists among the Part-3 estimation methods, and behind the semiparametric second step reused in the 2019 working paper above.

The paper's own account of the method (verbatim from the published abstract): "We use adaptive weights smoothing (AWS)… to estimate a map of land values for Berlin, Germany. Our data are prices of undeveloped land that was transacted between 1996 and 2009. […]"[2] Observed land prices, the authors explain, indicate the underlying land value but carry transaction noise, which the iterative AWS reduces by applying piecewise constant regression and testing at each location for constancy.

Two points matter for how the wiki uses it:

- **It is the *undeveloped-land* estimator.** AWS is applied to **vacant-land sales** (1996–2009) — the same data family as the kernel estimator that scores 0.704 above. This is why the pure-land nonparametric approach reproduces the expert map only where vacant-land sales occur; AWS denoises those sales into a surface but cannot conjure a signal in the built-up core where such sales are absent. The semiparametric method's contribution is precisely to bring *developed*-property transactions to bear on that gap.
- **AWS is a denoiser, not a hedonic model.** It imposes no functional form on how location maps to value; it smooths the observed land-sale prices adaptively, merging neighbouring locations only where the data support treating them as one region. That makes it well suited to a spatial-smoothness argument — the same [spatial-smoothness](/wiki/mass-appraisal-methods/) claim Doucet leans on — but it also means the method is only as good as the vacant-land sales it is fed.

## Limits

- **The benchmark is itself an expert assessment.** Correlation of 0.845 means the statistical method reproduces what Berlin's surveyor commission already does by hand — it does not prove either against true (unobservable) market land value. The paper is candid that "lack of such a benchmark is the reason why land values have to be estimated" at all.[1]
- **0.845 ≈ ±15% is a spatial-average agreement, not parcel-level precision.** A high citywide correlation is consistent with sizable individual-parcel errors, which is what appeals processes exist to catch (see [Hefferan & Boyd](/wiki/hefferan-boyd-mass-appraisal-australia/) on objection rates).
- **Data-rich setting.** Berlin's GAA collects comprehensive transaction data by law and already publishes a fine-grained BRW atlas; jurisdictions with thin sales data or no cadastral infrastructure face a harder problem (a caveat [Almy](/wiki/almy-oecd-valuation-assessment/) develops internationally).
- **Working-paper status / imported headline figure.** The 0.845 result originates in the authors' 2012 publication and is reproduced here; the 2019 FORLand paper is a working paper, not a peer-reviewed journal article, though its authors are established valuation econometricians.

## See Also

- [Mass Appraisal Methods](/wiki/mass-appraisal-methods/)
- [Objection: Land value can't be assessed accurately](/wiki/land-cannot-be-assessed/)
- [Doucet, *Does Georgism Work?*](/wiki/doucet-does-georgism-work/)
- [Almy, *Valuation and Assessment of Immovable Property* (OECD)](/wiki/almy-oecd-valuation-assessment/)
- [Hefferan & Boyd, *Mass Appraisal Valuations in Australia*](/wiki/hefferan-boyd-mass-appraisal-australia/)
- [Site Value](/wiki/site-value/)

## Sources

1. Jens Kolbe, Rainer Schulz, Martin Wersing & Axel Werwatz (2019), *Land Value Appraisal Using Statistical Methods*, FORLand Working Paper 07, DFG Research Unit 2569 "Agricultural Land Markets," Humboldt-Universität zu Berlin (paper dated 18 January 2019). [PDF](https://edoc.hu-berlin.de/bitstream/handle/18452/20511/FORLand-2019-07.pdf) — used for: the kernel-regression correlation of **0.704** with the BRW map and its inability to estimate the built-up city centre; the semiparametric correlation of **0.845** (from house transactions only, carried over from the authors' Kolbe et al. 2012 companion study); the abstract claim that statistical methods "match up well with expert based assessments"; and the two-step semiparametric procedure using developed-property transactions. All figures verified verbatim against the PDF (2026-07-10). The expert benchmark is Berlin's official *Bodenrichtwerte* (BRW) standard-land-value map produced by the GAA surveyor commission.
2. Jens Kolbe, Rainer Schulz, Martin Wersing & Axel Werwatz (2015), "Identifying Berlin's land value map using adaptive weights smoothing," *Computational Statistics*, Vol. 30, Issue 3, pp. 767–790, [DOI 10.1007/s00180-015-0559-9](https://doi.org/10.1007/s00180-015-0559-9) (published version; paywalled). Free versions: SFB 649 Discussion Paper 2015-003 and the Humboldt-Universität edoc server; abstract and bibliographic record at [RePEc/EconPapers](https://econpapers.repec.org/RePEc:spr:compst:v:30:y:2015:i:3:p:767-790) — used for: the AWS method applied to undeveloped-land sales (1996–2009), the piecewise-constant iterative-smoothing/denoising description, and its role as the methodological companion to the semiparametric surface. Abstract quote verified verbatim against the published-version record (2026-07-11).
