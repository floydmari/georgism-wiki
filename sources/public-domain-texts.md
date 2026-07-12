# Public-domain sources → `texts/` conversion tracker

Per EDITORIAL §3b: sources we cite that are **out of copyright** (published pre-1931, or author dead ≥70 years for non-US works) may be reproduced **in full**. Short works (≤~25k words — speeches, essays, single chapters, pamphlets) become **`texts/` wiki pages**; full books go to **`sources/publicdomain/<slug>.md`** beside their `books/` summary.

This tracker drives Floyd's standing request: *add as `texts/` any and all public-domain sources we cite.* It's worked through incrementally across VERIFY-sweep shifts.

## Done — already `texts/` pages
- Thomas Paine, *Agrarian Justice* (1797) → texts/agrarian-justice
- Henry George, *The Crime of Poverty* (1885) → texts/crime-of-poverty
- Henry George, *Thy Kingdom Come* (1889 sermon) → texts/thy-kingdom-come
- Henry George, open letter to Pope Leo XIII / *The Condition of Labour* (1891) → texts/open-letter-to-pope-leo-xiii
- Lloyd George, People's Budget speech (Commons, 29 Apr 1909) → texts/peoples-budget-speech-1909
- (Moses / land-ethics excerpt) → texts/moses

## To add — short works, full text in hand (do these first)
- [x] **Lloyd George, Limehouse speech (30 July 1909)** → texts/limehouse-speech-1909 *(created 2026-07-07)*
- [x] **Winston Churchill, "The Mother of All Monopolies" — King's Theatre, Edinburgh, 17 July 1909** → texts/churchill-mother-of-monopolies-1909 *(created 2026-07-07)*
- [x] **Herbert Spencer, *Social Statics* (1851), Ch. IX "The Right to the Use of the Earth"** → texts/social-statics-right-to-use-earth *(created 2026-07-07)*

## To add — short works, need to fetch/confirm full text
- [x] **John Stuart Mill, *Programme of the Land Tenure Reform Association, with an Explanatory Statement* (1871)** → texts/land-tenure-reform-programme-1871 *(created 2026-07-09; text from Toronto Collected Works Vol. V via OLL PDF, articles verified against D&D IV 1875 scan at archive.org dli.bengal.10689.4992)*
- [x] **Churchill, "The Budget Resolutions" — House of Commons, 4 May 1909** → texts/churchill-budget-resolutions-1909 *(created 2026-07-09; text from Liberalism and the Social Problem via Gutenberg #18419)*

## To add — confirmed fetchable, next up
- [x] **Henry George, *The Irish Land Question* (1881, Appleton)** → texts/irish-land-question-1881 *(created 2026-07-10; ~31.5k words, 17 chapters, programmatic transcription from archive.org irishlandquestio00geor with T1 artifact pass; T2 image-proofread queued)*
- [ ] Henry George Jr., *The Life of Henry George* (1900) — PD, full text at archive.org (lifeofhenrygeorg00geor); large (book-length) → `sources/publicdomain/` channel; already cited as a primary on 3+ pages.

## Full public-domain BOOKS we cite (→ `sources/publicdomain/`, not `texts/`)
These are on Gutenberg/archive and could be mirrored in full to the publicdomain store beside their `books/` summary; large, so lower priority than the short works above.
- [ ] J.S. Mill, *Principles of Political Economy* (1848) — Gutenberg #30107. (research/mill-principles-land)
- [ ] Henry George, *Progress and Poverty* (1879) — Gutenberg #55308.
- [ ] Ebenezer Howard, *Garden Cities of To-morrow* (1902) — Gutenberg #46134. (books/garden-cities-of-to-morrow)
- [~] A. C. Pigou, *The Economics of Welfare* — **handled as a research page, not a full ingest (2026-07-11).** COPYRIGHT: the Econlib text is the **1932 4th ed.** (US PD status unestablished — do NOT ingest it). The **1st ed. (1920)** IS public domain (pub. 1920) and is machine-readable at archive.org [`economicsofwelfa00pigouoft`](https://archive.org/details/economicsofwelfa00pigouoft) (Macmillan 1920). The LVT-relevant material is a coherent ~15-page block (Part IV, Ch. III "Taxes on Windfalls," pp. 600–608, incl. increment duties; Ch. IV "Taxes on the Public Value of Land," pp. 609–615) but analytical and OCR-dirty, so it was extracted as verbatim quotes + page cites in **research/pigou-land-taxation.md** rather than reproduced as a `texts/` page. Verdict on substance: Pigou grants the LVT/site-value efficiency case in full ("leave the national dividend wholly unaffected," p. 612) but limits its scope on equity grounds ("their scope is strictly limited," p. 615) — a cautious, qualified supporter, not a Georgist. (concepts/pigouvian-taxation)
- [x] Homer Hoyt, *One Hundred Years of Land Values in Chicago* (1933) — **RENEWAL CHECKED 2026-07-11: NOT renewed → US PUBLIC DOMAIN.** No renewal for Homer Hoyt / this title appears in the Catalog of Copyright Entries book-renewal records for 1959–1962 (the full valid renewal window for a 1933 work; searched the machine-readable CCE renewal transcriptions, Project Gutenberg #11819–11826). A 1933 work whose 28-year term lapsed without renewal entered the public domain in 1961. Corroborated by the Internet Archive hosting the full scan **openly** (not controlled-lending; collections `americana`/`prelinger_library`; `possible-copyright-status: NOT_IN_COPYRIGHT`). Scan source: [`onehundredyearso00hoytrich`](https://archive.org/details/onehundredyearso00hoytrich). Do NOT ingest now (book-length, xxxii+519 pp.) — verdict recorded here and in research/hoyt-chicago-land-values.md. (research/hoyt-chicago-land-values)

## Method
When adding a `texts/` page: full frontmatter (`category: texts`, `public_domain: true`, `provenance: "<edition/source + transcription URL>"`), an editorial headnote, the full text, ≥2 inbound links, and a **registry.csv row** with an external provenance URL (Format `Text`). Then re-run `build_inventory.py`.
