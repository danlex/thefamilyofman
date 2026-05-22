---
id: src-wikipedia-carl-mydans-pointer
title: "Carl Mydans"
author: "Wikipedia contributors"
year: 2026
type: website
publisher: "Wikipedia / Wikimedia Foundation"
url: "https://en.wikipedia.org/wiki/Carl_Mydans"
accessed: 2026-05-09
tier: 3
language: en
verified: true
pointer_only: true
tags: [carl-mydans, photographer-biography, life-magazine, fsa, pointer-source]
---

## Citation

*Carl Mydans.* Wikipedia. Fetched 2026-05-09 from `https://en.wikipedia.org/wiki/Carl_Mydans`.

## Tier justification

Tier 3: Wikipedia is **pointer-only** per `CREDIBILITY.md`. Used here for day-month tokens (May 20 / August 16), the Medford, Massachusetts birthplace and Larchmont, New York place-of-death tokens, the canonical *Life* original-staff roster, and to flag the year-of-birth discrepancy with the ICP archive page (1907 vs ICP's 1906).

## Key excerpts / pages

Verbatim claims from the article (fetched 2026-05-09; opening sentence, infobox, and Life-staff paragraph):

- **Opening sentence:** "Carl Mydans (May 20, 1907 – August 16, 2004) was an American photographer who worked for the Farm Security Administration and Life magazine."
- **Infobox:** Born "May 20, 1907" in "Medford, Massachusetts". Died "August 16, 2004" (aged 97) in "Larchmont, New York".
- **Life staff roster (verbatim):** "In 1936, he joined Life as one of its earliest staff photographers (Alfred Eisenstaedt, Margaret Bourke-White, Thomas McAvoy and Peter Stackpole were the original staff photographers) and a pioneering photojournalist."
- **FSA period (verbatim):** "After college, he went to New York as a writer for American Banker and then in 1935 to Washington to join a group of photographers in the Farm Security Administration. There he worked with other photographers like Dorothea Lange and Ben Shahn to document the conditions of the American rural workers."
- "In 1941, the photographer and Shelley Mydans were the first husband and wife team on the magazine's staff. Shelley and Carl were captured by the invading Japanese forces in the Philippines and interned for nearly a year at the Santo Tomas Internment Camp in Manila, then for another year in Shanghai, China, before they were released as part of a prisoner-of-war exchange in December 1943."

## Notes

- Per `CREDIBILITY.md`, Wikipedia is treated as a pointer source — the May 20, 1907 birth, August 16, 2004 death, Medford / Larchmont place tokens should be promoted to Tier 1/2 against the August 2004 *New York Times* obituary (`https://www.nytimes.com/2004/08/17/obituaries/carl-mydans-97-magazine-photographer-known-for-images-of-war.html` — attempted via curl 2026-05-09 and returned HTTP 403) before being treated as authoritative for downstream training data.
- **DATE DISCREPANCY:** ICP records Mydans's birth year as **1906**; Wikipedia records **1907** in both the opening sentence and infobox. The "aged 97" death-age annotation in the Wikipedia infobox is consistent with a 1907 birth (97 years to August 2004) and inconsistent with a 1906 birth (which would yield 97 only if Mydans died after May 20, which he did — so technically both are arithmetically possible, but the canonical 1907 token is the one printed in the body text and infobox). This repo records 1907 in `data/photographers.csv` per the Wikipedia text and flags the ICP discrepancy.
- Wikipedia does not mention *The Family of Man* on Mydans's article (verified 2026-05-09; no occurrence of "Family of Man" in the fetched HTML).
- The three-plate count in FoM is independently verified by strict-match grep against `data/photographs.csv` (2026-05-09).
- Mydans's "one of the four" Life-launch framing on the ICP page does not match the Wikipedia infobox roster (Eisenstaedt, Bourke-White, McAvoy, Stackpole) — he is described on Wikipedia as "one of its earliest staff photographers" rather than one of the original four. The two ICP pages already in repo (src-icp-eisenstaedt-archive and src-icp-bourke-white-archive) confirm the four-name canonical roster excluding Mydans.
