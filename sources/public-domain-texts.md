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
- [ ] Churchill, House of Commons land-monopoly speech (4 May 1909) — companion to the Edinburgh speech.

## Full public-domain BOOKS we cite (→ `sources/publicdomain/`, not `texts/`)
These are on Gutenberg/archive and could be mirrored in full to the publicdomain store beside their `books/` summary; large, so lower priority than the short works above.
- [ ] J.S. Mill, *Principles of Political Economy* (1848) — Gutenberg #30107. (research/mill-principles-land)
- [ ] Henry George, *Progress and Poverty* (1879) — Gutenberg #55308.
- [ ] Ebenezer Howard, *Garden Cities of To-morrow* (1902) — Gutenberg #46134. (books/garden-cities-of-to-morrow)
- [ ] A. C. Pigou, *The Economics of Welfare* (1920) — Econlib full text. (concepts/pigouvian-taxation)
- [ ] Homer Hoyt, *One Hundred Years of Land Values in Chicago* (1933) — archive.org (US, 1933; check renewal). (research/hoyt-chicago-land-values)

## Method
When adding a `texts/` page: full frontmatter (`category: texts`, `public_domain: true`, `provenance: "<edition/source + transcription URL>"`), an editorial headnote, the full text, ≥2 inbound links, and a **registry.csv row** with an external provenance URL (Format `Text`). Then re-run `build_inventory.py`.
