---
id: src-magnum-werner-bischof
title: "Werner Bischof — Photographer Profile, Magnum Photos"
author: "Magnum Photos"
year: 2026
type: website
publisher: "Magnum Photos"
url: "https://www.magnumphotos.com/photographer/werner-bischof/"
accessed: 2026-05-09
tier: 1
language: en
verified: true
tags: [photographer-bio, bischof, magnum, swiss, post-war-photojournalism]
---

## Citation

Magnum Photos. "Werner Bischof — Photographer Profile." Magnum cooperative photographer page. Accessed 2026-05-09. https://www.magnumphotos.com/photographer/werner-bischof/

## Relevance

Tier-1 institutional page from Bischof's own cooperative agency (Magnum Photos, of which he was an early full member) for the biographical anchor of `pher-werner-bischof` in `data/photographers.csv`. Bischof is represented by six plates in *The Family of Man* per strict-match grep against `data/photographs.csv` (2026-05-09).

## Key excerpts / pages

**Header (rendered under the photographer's name, fetched 2026-05-09):**

- The right-hand sidebar prints (across separate `<p>` tags in the page source): "b. 1916", "d. 1954", "Swiss", "Estates", "Personal website".
- Pull-quote attributed to Bischof: "I felt compelled to venture forth and explore the true face of the world. Leading a satisfying life of plenty had blinded many of us to the immense hardships beyond our borders."

**Biography body (verbatim, fetched 2026-05-09):**

- "Werner Bischof was born in Switzerland in 1916. He studied photography with Hans Finsler in his native Zurich at the School for Arts and Crafts, then opened a photography and advertising studio."
- "In 1942, he became a freelancer for Du magazine, which published his first major photo essays in 1943. Bischof received international recognition after the publication of his 1945 reportage on the devastation caused by the Second World War."
- "Bischof died in a road accident in the Andes on May 16, 1954, only nine days before Magnum founder Robert Capa lost his life in Indochina."

## Notes

- Perspective: institutional / cooperative-agency. Magnum's pages are constituent-archive equivalents to ICP's; per repo precedent (cf. `src-icp-cartier-bresson-archive` and `src-magnum-photographer-bios` lessons) cooperative-agency biographies of their own members are treated as Tier 1 institutional pages.
- The text "his native Zurich" is the only reference to a city of birth. The 26 April 1916 day-month token of birth is NOT corroborated on this Magnum page; carried from the existing `src-nyt-1954-bischof-obit` citation (in repo, marked `verified: false`).
- The Magnum page does not name *The Family of Man*. The connection is made via the MoMA Master Checklist (src-moma-exh-0569-master-checklist, in repo) at the plate level.
- Cross-check with `src-icp-werner-bischof-archive` (created in this round): both pages give 1916–1954 dates and Swiss nationality, both name his early training in Zurich; Magnum names the teacher (Hans Finsler) and the Zurich training institution as "the School for Arts and Crafts" while ICP names it as "the Zürich School of Arts and Crafts" — agreement at the institution level.
- Verified against fetched source on 2026-05-09 via `curl` (HTTP 200) into `.scratch/bischof_magnum.html`.
