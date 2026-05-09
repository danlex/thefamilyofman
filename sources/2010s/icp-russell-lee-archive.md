---
id: src-icp-russell-lee-archive
title: "Russell Lee — International Center of Photography"
author: "International Center of Photography"
year: 2010
type: archive
publisher: "International Center of Photography, New York"
url: "https://www.icp.org/browse/archive/constituents/russell-lee"
accessed: 2026-05-09
tier: 1
language: en
verified: true
tags: [photographer-bio, russell-lee, archive, icp, fsa, depression-era]
---

## Citation

International Center of Photography. "Russell Lee." Constituent page in the ICP archive-browse index. Accessed 2026-05-09. https://www.icp.org/browse/archive/constituents/russell-lee

## Relevance

Tier-1 institutional archive page for Russell Lee at ICP. Reference for his biographical anchor (1903–1986, American; FSA photographer 1936–1942; later teaching position at the University of Texas, Austin until 1973). Russell Lee has two plates in *The Family of Man* per strict-match grep against `data/photographs.csv` (2026-05-09): photo-0080 and photo-0170 (both USA).

## Key excerpts / pages

**Biographical dates and nationality (rendered cleanly in the right-hand panel of the page, fetched 2026-05-09):**

- "1903 - 1986"
- "American"
- "94 items" archived
- Role: "Artist"

**Bibliography references (rendered cleanly):**

- "Phillips, Christopher, and Vanessa Rocco, eds. *Modernist Photography: Selections from the Daniel Cowin Collection*. New York: International Center of Photography and Göttingen, Germany: Steidl, 2005, pp. 111."
- "Brannan, Beverly, and Carl Fleischhauer. *Documenting America, 1935–1943*. Los Angeles: University of California Press, 1988."
- "Hurley, F. Jack. *Russell Lee, Photographer*. New York: Morgan and Morgan, 1978."

**Biography paragraph rendering issue (fetched 2026-05-09):** the page's `field--name-field-biography` div contains a malformed `<russell ...>`-prefixed paragraph that the browser parses as a tag and discards on render. The double-encoded literal text in the page source reads: "Russell Lee was born in Ottawa, Illinois, 1903 and did not take up photography until his thirties, after studying chemical engineering. Joining the photographic section of the Farm Securities Administration in fall 1936, he began to travel frequently to photograph rural and urban communities in the Midwest and Southwest, such as Pie Town, New Mexico, and San Augustine, Texas. The FSA's longest employed and most productive photographer, he worked diligently for the agency until its closure in 1942. ... War he photographed coal miners for the Department of Interior and the oil industry for Standard Oil. Following a 1965 retrospective exhibtiion [sic] at the University of Austin, Texas, he took a teaching position at the University, where he remained until his retirement in 1973." This text is not stably rendered in the live page — it is present only in the page source as broken markup. Treat the narrative as Tier-1-source-bound *only at the year-level dates* (1903 / 1986) and the nationality (American), which render cleanly in the side panel.

## Notes

- Perspective: institutional / archival.
- The ICP page gives year-only resolution (1903 / 1986). The July 21, 1903 / August 28, 1986 day-month tokens, the Ottawa, Illinois birthplace, and the Austin, Texas place-of-death token carry pointer status from src-wikipedia-russell-lee-pointer.
- The page does not name *The Family of Man*. The connection is made via the MoMA Master Checklist (src-moma-exh-0569-master-checklist, in repo) at the plate level.
- Verified against fetched source on 2026-05-09 via `curl -fsSL https://www.icp.org/browse/archive/constituents/russell-lee` (HTTP 200).
- The MoMA artists/collection page was attempted at `https://www.moma.org/artists/search?q=russell-lee` and returned 403; no MoMA collection corroboration in this round.
