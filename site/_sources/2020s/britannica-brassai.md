---
id: src-britannica-brassai
title: "Brassaï — Encyclopædia Britannica"
author: "Britannica Editors"
year: 2026
type: website
publisher: "Encyclopædia Britannica, Inc."
url: "https://www.britannica.com/biography/Brassai"
accessed: 2026-05-09
tier: 3
language: en
verified: true
tags: [photographer-bio, brassai, britannica, encyclopedia, paris-by-night]
---

## Citation

Encyclopædia Britannica, Inc. "Brassaï | French Photographer, Surrealist & Sculptor." Encyclopædia Britannica online edition. Accessed 2026-05-09. https://www.britannica.com/biography/Brassai

## Tier justification

Tier 3 per `CREDIBILITY.md` ("Encyclopedia entries with named authors and visible references (*Grove Art*, *Encyclopedia Britannica*)"). Encyclopedia entries are explicitly NOT Tier 2 even when carefully edited.

## Relevance

Pointer / corroborating biographical anchor for `pher-brassai` in `data/photographers.csv`. Brassaï has six plates in *The Family of Man* per strict-match grep against `data/photographs.csv` (2026-05-09). Used in this round to corroborate the day-month-resolution birth/death tokens (which the Tier-1 ICP page only provides at year resolution).

## Key excerpts / pages

**Lead paragraph (verbatim, fetched 2026-05-09):**

- "Brassaï (born September 9, 1899, Brassó, Transylvania, Austria-Hungary [now Romania]—died July 8, 1984, Eze, near Nice, France) was a Hungarian-born French photographer, poet, draughtsman, and sculptor, known primarily for his dramatic photographs of Paris at night. His pseudonym, Brassaï, is derived from his native city."

**"Quick Facts" panel (verbatim, fetched 2026-05-09):**

- "Original name: Gyula Halász"
- "French: Jules Halasz"
- "Born: September 9, 1899, Brassó, Transylvania, Austria-Hungary [now Romania]"
- "Died: July 8, 1984, Eze, near Nice, France (aged 84)"

**Body excerpts (verbatim, fetched 2026-05-09):**

- "Brassaï trained as an artist and settled in Paris in 1924. There he worked as a sculptor, painter, and journalist and associated with such artists as Pablo Picasso, Joan Miró, Salvador Dalí, and the writer Henry Miller."
- "His pictures were published in a successful book, Paris de nuit (1933; Paris After Dark, also published as Paris by Night), which caused a stir because of its sometimes scandalous subject matter."
- "His next book, Voluptés de Paris (1935; 'Pleasures of Paris'), made him internationally famous."
- "When the German army occupied Paris in 1940, Brassaï escaped southward to the French Riviera, but he returned to Paris to rescue the negatives he had hidden there."
- "The Museum of Modern Art in New York City held a retrospective exhibition of Brassaï's work in 1968."

## Notes

- Perspective: encyclopedia / general-reference; named editor team ("Britannica Editors") rather than a single named scholar.
- Place-of-death discrepancy with `src-wikipedia-brassai-pointer` (in repo): Britannica says "Eze, near Nice"; Wikipedia infobox says "Beaulieu-sur-Mer". Both are communes on the French Riviera near Nice (Eze and Beaulieu-sur-Mer are adjacent communes on the same coastal stretch). Recorded as discrepancy; not adjudicated in this round.
- *Paris de nuit* publication-year token: Britannica gives 1933 — agreement with Wikipedia (also 1933) and disagreement with `src-icp-brassai-archive` (which renders "1932"). The 1933 date is the more frequently corroborated.
- Britannica also names the 1968 MoMA retrospective — distinct from the 1956 MoMA Brassaï exhibition mentioned in `src-wikipedia-brassai-pointer`. Both are plausible; Britannica focuses on the 1968 retrospective.
- The page does not name *The Family of Man*. The connection is made via the MoMA Master Checklist (src-moma-exh-0569-master-checklist, in repo) at the plate level.
- Verified against fetched source on 2026-05-09 via `curl` (HTTP 200) into `.scratch/brassai_britannica.html`.
