---
id: src-wikipedia-homer-page-pointer
title: "Homer Page [Wikipedia article — fetched 2026-05-09; pointer-only per CREDIBILITY.md]"
author: ""
year: 2026
type: website
publisher: "Wikipedia / Wikimedia Foundation"
url: "https://en.wikipedia.org/wiki/Homer_Page"
accessed: 2026-05-09
tier: 3
language: en
verified: true
tags: [homer-page, photographer-biography, fom-mention, guggenheim-1949, dorothea-lange, pointer-source]
---

## Citation

*Homer Page.* Wikipedia. Fetched 2026-05-09 from `https://en.wikipedia.org/wiki/Homer_Page`.

## Tier justification

Tier 3: Wikipedia is **pointer-only** per `CREDIBILITY.md`. Recorded here as the available biographical anchor for `pher-homer-page` in `data/photographers.csv`. ICP returns 404 for `homer-page` (verified 2026-05-09 via curl) and MoMA's artist page returned 403 in this round; the Nelson-Atkins Hallmark Photographic Collection (which holds ~100 Page prints per the Wikipedia text below) was attempted at one URL and returned 404 — no institutional Tier-1 page was successfully fetched for Page in this round.

## Relevance

Homer Page has **ten** plates in *The Family of Man* per strict-match grep against `data/photographs.csv` (2026-05-09): photo-0097, photo-0120, photo-0150, photo-0151, photo-0162, photo-0168, photo-0278, photo-0374, photo-0399, photo-0484. This places Page among the top contributors to FoM by plate count (after "Photographer unknown" at 14, Wayne Miller at 12, Henri Cartier-Bresson at 11; Page tied with Dorothea Lange at 9–10 in the leaders' band per the Lange row's 2026-05-07 audit).

## Key excerpts / pages

Verbatim from the article (fetched 2026-05-09):

- **Lead:** "**Homer Page** (1918–1985) was an American documentary photographer whose most famous photographs were taken in New York City in 1949–1950, after he received a grant from the Guggenheim Foundation."
- **Categorical metadata (page categories block):** "1918 births", "1985 deaths", "20th-century American photographers", "University of California, Berkeley alumni".
- **Background:** "Page was born in Oakland, California, and studied art and social psychology at the University of California, graduating in 1940. He worked in the shipyards in the Oakland-San Francisco Bay Area during World War II. His neighbor and later his mentor, photographer Dorothea Lange, encouraged him to take up photography in 1944. By 1947, he was featured in a major show at the Museum of Modern Art in New York."
- **Guggenheim and NY work:** "Page received a Guggenheim Fellowship in 1949 and spent a year documenting modern urban culture, primarily by photographing people on the streets of New York City. Most of his subjects appear unaware of his presence."
- **FoM inclusion (verbatim):** "Some of Page's photographs were included in Edward Steichen's landmark *Family of Man* exhibition at the Museum of Modern Art in 1955. His photographs appeared in publications including Harper's Magazine, and books such as *The Little World of Laos*. In 1966, he published a collection of his photographs, titled *Puerto Rico: The Quiet Revolution*."
- **WHO assignments:** "Page produced several photo stories for the World Health Organization from 1957 to 1960. Most of his photographs focused on health in the United States, but he also traveled to Latin America, Asia and Africa to photograph topics including rural health, yaws and trachoma."
- **Career arc and obscurity:** "The bulk of Page's career was spent as a magazine photographer, and, as a result, few of his photographs were in private hands and his work was largely forgotten by the time of his death in 1985, at the age of 67."
- **Posthumous rediscovery:** "Keith F. Davis, Curator of Photography at the Nelson-Atkins Museum of Art, while researching and writing the first edition of *An American Century of Photography*, published in 1995, became aware of Page's non-magazine work. Davis searched for Page's photographs, leading to the discovery of a 'lost' photographic treasure. After negotiations with the Page estate, Nelson-Atkins purchased about 100 prints for the museum's Hallmark Photographic Collection, including many that were one of a kind."

## Notes

- Per `CREDIBILITY.md` Wikipedia is treated as a pointer source — the 1918 / 1985 year-level dates, the Oakland birthplace, and the 1949 Guggenheim Fellowship should be promoted to Tier 1 / Tier 2 against the Davis-edited 2009 Yale University Press monograph *Homer Page: The Guggenheim Year, New York, 1949–50* (cited in the Wikipedia article's external links) or against the Nelson-Atkins / Hallmark Collection's catalog before being cited as authoritative.
- ICP and MoMA archive pages were attempted (ICP returned 404 for `/browse/archive/constituents/homer-page`; MoMA returned 403 for `/artists/4474`) — no Tier-1 institutional anchor was successfully fetched for Page in this round.
- The Wikipedia article's death-age arithmetic is internally consistent: born 1918, died 1985, "at the age of 67" — matching a death in 1985 and a birth in 1918 (or possibly mid-1917 / mid-1918 depending on the unstated month — the day-month tokens are not in the Wikipedia article as fetched).
- The Lange-Page mentor relationship (Lange as Page's neighbor in Oakland encouraging him into photography in 1944) is an interesting biographical detail that situates Page in the same FSA-adjacent California documentary milieu as Lange herself; this link is the single biggest curatorial-pathway hint for how Page's ten FoM plates reached Steichen.
- Cross-references: `src-moma-exh-0569-master-checklist` (in repo, the source for Page's ten FoM plates), `src-icp-lange-archive` (in repo, fetched 2026-05-07; Lange's bio confirms 1929 onwards in San Francisco / Berkeley area).
