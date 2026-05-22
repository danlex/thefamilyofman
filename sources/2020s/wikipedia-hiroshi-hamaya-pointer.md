---
id: src-wikipedia-hamaya-pointer
title: "Hiroshi Hamaya"
author: "Wikipedia contributors"
year: 2026
type: website
publisher: "Wikipedia / Wikimedia Foundation"
url: "https://en.wikipedia.org/wiki/Hiroshi_Hamaya"
accessed: 2026-05-10
tier: 3
language: en
verified: true
pointer_only: true
tags: [hiroshi-hamaya, photographer-biography, japanese-photography, magnum, family-of-man, pointer-source]
---

## Citation

*Hiroshi Hamaya.* Wikipedia. Fetched 2026-05-10 from `https://en.wikipedia.org/wiki/Hiroshi_Hamaya`.

## Tier justification

Tier 3: Wikipedia is **pointer-only** per `CREDIBILITY.md`. Used here strictly to record day-month tokens (28 March 1915 / 6 March 1999), the explicit *Family of Man* attribution, and the Magnum membership-class refinement ("first Japanese photographer to join Magnum Photos in 1960, as an associate member") that the Tier-1 ICP page records only as "A member since 1960".

## Key excerpts / pages

Verbatim claims from the article (fetched 2026-05-10):

- **Short description:** "Japanese photographer (1915–1999)"
- **Lead (verbatim, with the day-month tokens that anchor pointer-only resolution):** "Hiroshi Hamaya (濱谷 浩, Hamaya Hiroshi; 28 March 1915 – 6 or 15 March 1999) was a Japanese photographer active from 1935 to 1999. In particular, Hamaya was known for his photographs of rural Japan."
- **Birthplace (verbatim):** "Hamaya was born in Shitaya, Tokyo, Japan, on 28 March 1915."
- **Death-date narrative (verbatim):** "Hamaya died on 6 March 1999."
- **Family of Man inclusion (verbatim, plate-level identification):** "By 1955 one of Hiroshi Hamaya's photographs, a high-angle view of kimono-clad springtime dancers led by his wife, was included by curator Edward Steichen in the world-touring Museum of Modern Art exhibition *The Family of Man* that was seen by more than 9 million visitors."
- **Snow Country / Yukiguni publication (verbatim):** "In 1956, Hamaya published his acclaimed photobook 'Snow Country' (*Yukiguni*) featuring photographs of Japan's frigid northeastern Tōhoku region in winter."
- **Magnum membership (verbatim, anchors associate-class wording):** "Hamaya was the first Japanese photographer to join Magnum Photos in 1960, as an associate member."
- **ICP recognition (verbatim):** "He received the Master of Photography Award from the International Center of Photography (New York) in 1986."

## Notes

- Per `CREDIBILITY.md`, Wikipedia is treated as a pointer source. The 28 March 1915 / 6 March 1999 day-month tokens are not corroborated against any second source fetched in this round at the day-level (Wikidata Q1386695 corroborates 1915-03-28 / 1999-03-06 in the structured-data record `.scratch/wikidata-hamaya.json`; this is the same Wikipedia community's record and is not strictly an independent fetch); they remain pointer-only at the day-level. The 1915 / 1999 year-only resolution is independently anchored at Tier 1 by the ICP page (`src-icp-hiroshi-hamaya`).
- Wikipedia is the only source consulted in this round that names *The Family of Man* explicitly on Hamaya's biography page. The plate-level identification ("a high-angle view of kimono-clad springtime dancers led by his wife") is consistent with the FoM "Section 24 Ring Around the Rosy" plate (photo-0263) which is the single Hamaya plate in the FoM checklist (verified by strict-match grep against `data/photographs.csv` 2026-05-10), but the photograph-attribution mapping should NOT be promoted to a print-record claim without a fetched MoMA installation print or original-print attribution — the Master Checklist (`src-moma-exh-0569-master-checklist`, in repo) prints the entry with photographer + nationality + dimensions only, not a title.
- The Magnum membership-class refinement (associate vs full member) is independently corroborated only by Wikipedia in this round; the ICP page records the year (1960) but not the class. Magnum Photos's own photographer page for Hamaya was attempted at `https://www.magnumphotos.com/photographer/hiroshi-hamaya/` and returned **HTTP 404** (2026-05-10); Magnum's public site does not host a Hamaya photographer profile.
- Wayback Machine verification not performed in this round.
- Verified against fetched source on 2026-05-10 via `curl -fsSL https://en.wikipedia.org/wiki/Hiroshi_Hamaya` (HTTP 200, 122,384 bytes). Saved at `.scratch/wikipedia-hamaya.html`. Wikidata structured-data backup saved at `.scratch/wikidata-hamaya.json`.
