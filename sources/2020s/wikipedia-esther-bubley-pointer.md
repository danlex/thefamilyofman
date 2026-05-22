---
id: src-wikipedia-esther-bubley-pointer
title: "Esther Bubley"
author: "Wikipedia contributors"
year: 2026
type: website
publisher: "Wikipedia / Wikimedia Foundation"
url: "https://en.wikipedia.org/wiki/Esther_Bubley"
accessed: 2026-05-09
tier: 3
language: en
verified: true
pointer_only: true
tags: [esther-bubley, photographer-biography, owi, standard-oil, family-of-man, pointer-source]
---

## Citation

*Esther Bubley.* Wikipedia. Fetched 2026-05-09 from `https://en.wikipedia.org/wiki/Esther_Bubley`.

## Tier justification

Tier 3: Wikipedia is **pointer-only** per `CREDIBILITY.md`. Used here for day-month tokens (February 16 / March 16), the Phillips, Wisconsin birthplace, the New York City place-of-death token, and the explicit Family-of-Man inclusion that the Tier-1 ICP page does not state.

## Key excerpts / pages

Verbatim claims from the article (fetched 2026-05-09; opening sentence, infobox, and Family-of-Man paragraph):

- **Opening sentence:** "Esther Bubley (February 16, 1921 – March 16, 1998) was an American photographer who specialized in expressive photos of ordinary people in everyday lives."
- **Infobox:** Born "February 16, 1921" in "Phillips, Wisconsin". Died "March 16, 1998" (aged 77) in "New York City, New York".
- **Family of Man (verbatim):** "In 1955, Steichen included her work in his monumental *The Family of Man* exhibition." (also listed in the exhibitions list: "Family of Man, Museum of Modern Art, New York, NY, 1955.")
- **Family origins (verbatim):** "Esther Bubley was born in Phillips, Wisconsin, the fourth of five children of Russian Jewish immigrants Louis and Ida Bubley."
- **OWI / Standard Oil arc (verbatim):** "In the fall of 1942, Roy Stryker hired her as a darkroom assistant at the Office of War Information (OWI), where his photographic unit had recently been transferred from the Farm Security Administration."
- "In late 1943, when Stryker left the OWI to work on a public relations project for the Standard Oil Company (New Jersey), she accompanied him, producing a profile of Tomball, Texas, an oil boom town."

## Notes

- Per `CREDIBILITY.md`, Wikipedia is treated as a pointer source — the February 16, 1921 / March 16, 1998 day-month tokens and the Phillips / New York City place tokens should be promoted to Tier 1/2 against the March 1998 *New York Times* obituary (`https://www.nytimes.com/1998/03/19/arts/esther-bubley-77-photographer-with-rich-and-versatile-eye.html` — not attempted via curl in this round) or against the Library of Congress P&P record before being treated as authoritative for downstream training data.
- The 1921 / 1998 year-only resolution is independently anchored at Tier 1 by the ICP archive page (src-icp-esther-bubley-archive); the year-tokens are not in dispute.
- The three-plate count in FoM is independently verified by strict-match grep against `data/photographs.csv` (2026-05-09).
