---
id: src-wikipedia-kessel-pointer
title: "Dmitri Kessel"
author: "Wikipedia contributors"
year: 2024
type: website
publisher: "Wikimedia Foundation"
url: "https://en.wikipedia.org/wiki/Dmitri_Kessel"
accessed: 2026-05-19
tier: 3
language: en
tags: [photographer-bio, kessel, wikipedia, pointer, life-magazine, war-photography]
verified: true
pointer_only: true
---

## Citation

Wikipedia contributors. "Dmitri Kessel." Wikipedia, The Free Encyclopedia. Accessed 2026-05-19. https://en.wikipedia.org/wiki/Dmitri_Kessel

## Relevance

Pointer-tier source for day-month-level birth/death tokens, career narrative, and FoM inclusion statement for Dmitri Kessel. Per CREDIBILITY.md, Wikipedia is a pointer only.

## Key excerpts (verbatim, fetched 2026-05-19)

- "born August 20, 1902, in Kiev"
- "died March 26, 1995, in Southampton, New York"
- "emigrated to the United States in 1923 and became a naturalized citizen in 1929"
- "photojournalist and staff photographer on Life magazine"
- "Worked for Fortune beginning in 1935, joined Life as a staffer in 1944, remained there until 1972"
- "In 1955, curator Edward Steichen selected eight of Kessel's photographs for the Museum of Modern Art's traveling exhibition. His images depicted subjects across multiple continents—from a French voter and Chinese couples to Italian harvest workers and Congolese miners—contributing to an exhibition 'seen by 9 million visitors.'"

## Notes

- DATE DISCREPANCY: Wikipedia gives birth "August 20, 1902" and death "March 26, 1995, in Southampton, New York." The pre-existing src-nyt-1995-kessel-obit (in repo, `verified: false`) recorded birth "August 26, 1902, Kiev" and death "March 19, 1995, Paris, France." These are materially different on both day-month and death location. Neither can be promoted to Tier-1 this round — the NYT obituary is paywalled and the Wikipedia dates cite no source. Both variants are noted in the research file; resolution requires a successful fetch of the NYT obituary or another Tier-1 biographical source.
- The eight-plate claim in Wikipedia is consistent with the eight Kessel plates counted in data/photographs.csv via strict-match grep (2026-05-19).
- Cache artifact: `.scratch/cache-en.wikipedia.org-kessel.html`
