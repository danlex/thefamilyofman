---
id: src-moma-collection-artists-index
title: "MoMA Online Collection — Artists Index"
author: "The Museum of Modern Art"
year: 2024
type: website
publisher: "The Museum of Modern Art, New York"
url: "https://www.moma.org/collection/artists"
accessed: 2026-04-24
tier: 1
language: en
verified: false
tags: [photographer-bio, moma, directory, primary]
---

## Citation

The Museum of Modern Art. "Artists" — searchable index of artists represented in the MoMA online collection. Accessed 2026-04-19. https://www.moma.org/collection/artists

Individual artist pages follow the pattern `https://www.moma.org/artists/<numeric-id>` and carry MoMA's own biographical summary (birth/death dates, nationality, active years) alongside the museum's holdings of that artist's work.

## Relevance

Tier-1 institutional reference for the dates and nationality of photographers represented in MoMA's own collection — a high proportion of *The Family of Man* contributors. The MoMA artist page is the curatorial institution's working biographical record and is the reference point for internal attribution in `data/photographs.csv` and `data/photographers.csv` where a MoMA collection record exists.

## Key excerpts / pages

- Searchable by name and by medium (photography filter).
- Each artist page carries the museum's own short biography and a linked view of the works held.

## Notes

- This entry is an index-level pointer; per-artist pages are cited as needed in row `notes` but are not duplicated as separate source files for every photographer in the seed batch — doing so would multiply ~273 thin stub files for the full catalog. Deeper per-artist MoMA citations should be added when an individual `research/photographers/<slug>.md` article is written.
- Perspective: institutional / curatorial.
- Re-verification 2026-04-24 (issue #9): `https://www.moma.org/artists/` returned 403 and `https://collections.moma.org/` returned ECONNREFUSED to programmatic WebFetch — MoMA's public web surface was not accessible to this round's automated fetches. The page is widely cited in prior scholarship; verification must be done through a browser session. Flagged `verified: false` pending Chrome-session confirmation.
