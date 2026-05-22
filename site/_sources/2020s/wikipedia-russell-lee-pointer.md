---
id: src-wikipedia-russell-lee-pointer
title: "Russell Lee (photographer)"
author: "Wikipedia contributors"
year: 2026
type: website
publisher: "Wikipedia / Wikimedia Foundation"
url: "https://en.wikipedia.org/wiki/Russell_Lee_(photographer)"
accessed: 2026-05-09
tier: 3
language: en
verified: true
pointer_only: true
tags: [russell-lee, photographer-biography, fsa, pointer-source]
---

## Citation

*Russell Lee (photographer).* Wikipedia. Fetched 2026-05-09 from `https://en.wikipedia.org/wiki/Russell_Lee_(photographer)`.

## Tier justification

Tier 3: Wikipedia is **pointer-only** per `CREDIBILITY.md`. Used here strictly to record day-month tokens (July 21 / August 28), the Ottawa, Illinois birthplace, the Austin, Texas place-of-death token, the middle name "Werner", and contextual FSA-team co-membership that the Tier-1 ICP page (src-icp-russell-lee-archive) does not state at this granularity.

## Key excerpts / pages

Verbatim claims from the article (fetched 2026-05-09; opening sentence and infobox):

- **Opening sentence:** "Russell Werner Lee (July 21, 1903 – August 28, 1986) was an American photographer and photojournalist, best known for his work for the Farm Security Administration (FSA) during the Great Depression."
- **Infobox:** Born "July 21, 1903" in "Ottawa, Illinois, U.S.". Died "August 28, 1986" (aged 83) in "Austin, Texas, U.S."
- **FSA team membership (verbatim from the body):** "In the fall of 1936, during the Great Depression, Lee was hired for the federally sponsored Farm Security Administration (FSA) photographic documentation project of the Franklin D. Roosevelt administration. He joined a team assembled under Roy Stryker, along with Dorothea Lange, Arthur Rothstein, and Walker Evans."
- "His series on Pie Town, New Mexico (1940) is among his most recognized bodies of work, utilizing Kodachrome color film to document a homesteading community."

## Notes

- Per `CREDIBILITY.md`, Wikipedia is treated as a pointer source — the July 21, 1903 birth, August 28, 1986 death, and Ottawa / Austin place-of-birth and death tokens should be promoted to Tier 1/2 against the September 1986 *New York Times* obituary (`https://www.nytimes.com/1986/09/02/obituaries/russell-lee-photographer-83-recorded-rural-america.html` — attempted via curl 2026-05-09 and returned HTTP 403; no Wayback fetch in this round) or against the Hurley monograph *Russell Lee, Photographer* (Morgan and Morgan, 1978) before being treated as authoritative for downstream training data.
- The 1903 / 1986 year-only resolution is independently anchored at Tier 1 by the ICP archive page (src-icp-russell-lee-archive); the year-tokens are not in dispute. The day-month tokens carry pointer status.
- Wikipedia does not mention *The Family of Man* on Russell Lee's article (verified 2026-05-09; no occurrence of "Family of Man" in the fetched HTML).
- The two-plate count in FoM is independently verified by strict-match grep against `data/photographs.csv` (2026-05-09).
