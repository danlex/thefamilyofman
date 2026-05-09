---
id: src-britannica-david-seymour
title: "David Seymour | Polish-American photojournalist | Britannica"
author: "Encyclopædia Britannica Editors"
year: 2026
type: website
publisher: "Encyclopædia Britannica, Inc."
url: "https://www.britannica.com/biography/David-Seymour"
accessed: 2026-05-09
tier: 3
language: en
verified: true
tags: [david-seymour, chim, photographer-biography, magnum, suez, britannica]
---

## Citation

Editors of Encyclopædia Britannica. "David Seymour." Encyclopædia Britannica. Accessed 2026-05-09. https://www.britannica.com/biography/David-Seymour

## Tier justification

Tier 3 per `CREDIBILITY.md` — encyclopedia entries (Britannica, Grove Art) are explicitly Tier 3. Recorded here as one of three independent biographical anchors (alongside `src-magnum-david-seymour` at Tier 1 and `src-wikipedia-david-seymour-pointer` at Tier 3) for the dates and place-of-birth tokens in `pher-david-seymour`. The Britannica entry independently corroborates the November 20, 1911 birth and November 10, 1956 death day-month tokens.

## Relevance

David Seymour has 4 plates in *The Family of Man* per strict-match grep against `data/photographs.csv` (2026-05-09). Britannica's biographical anchor for `pher-david-seymour` matches the Magnum and Wikipedia fetches at the year and day-month levels.

## Key excerpts / pages

Verbatim from the article (fetched 2026-05-09):

- **Header subtitle:** "born American photojournalist who is best known for his empathetic pictures of people, especially children." (The "born" here is the truncated lead from the page metadata; the full opening sentence as fetched continues into the dates and biographical narrative.)
- **Dates:** "born November 20, 1911" and "November 10, 1956, near Suez Canal,"
- **Career:** "Seymour studied graphic arts in Warsaw and in 1931 went to Paris to study at the Sorbonne, where he became interested in photography."

## Notes

- Perspective: encyclopedic / general-reference. Tier 3 per `CREDIBILITY.md`.
- The Britannica entry corroborates the November 20, 1911 / November 10, 1956 day-month tokens that `src-magnum-david-seymour` (Tier 1) gives only at year-level resolution.
- Britannica describes Seymour as a "Polish-American photojournalist" in the page title — the 1942 U.S. naturalization that is the basis for "American" is not given a precise year on this page.
- The "near Suez Canal" location for his death is a wider geographic framing than Magnum's "near the Suez Canal to cover a prisoner exchange"; the canonical site is El Qantara, Egypt (which is on the Suez Canal) per the existing `pher-david-seymour` row notes — that town-level token is NOT confirmed by the Britannica entry as fetched in this round.
- The description "empathetic pictures of people, especially children" frames the curatorial fit with FoM's children-section plates (photo-0064, photo-0276, photo-0320).
- Britannica does NOT name *The Family of Man* on this page (verified by string-search 2026-05-09).
- Verified against fetched source on 2026-05-09 via `curl -fsSL https://www.britannica.com/biography/David-Seymour` (HTTP 200) into `.scratch/britannica-david-seymour.html`.
