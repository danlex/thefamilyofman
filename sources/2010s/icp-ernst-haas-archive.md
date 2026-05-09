---
id: src-icp-ernst-haas-archive
title: "Ernst Haas — International Center of Photography"
author: "International Center of Photography"
year: 2010
type: archive
publisher: "International Center of Photography, New York"
url: "https://www.icp.org/browse/archive/constituents/ernst-haas"
accessed: 2026-05-09
tier: 1
language: en
verified: true
tags: [photographer-bio, haas, archive, icp, magnum, color-photography, life-magazine]
---

## Citation

International Center of Photography. "Ernst Haas." Constituent page in the ICP archive-browse index. Accessed 2026-05-09. https://www.icp.org/browse/archive/constituents/ernst-haas

## Relevance

Tier-1 institutional archive page for Ernst Haas at ICP. Reference for his biographical anchor (1921–1986, naturalized American born in Vienna; trained at the Graphische Lehr- und Versuchsanstalt; joined Magnum in 1949 at Capa's invitation; pioneer of color photo essay in *LIFE*). Haas has six plates in *The Family of Man* per strict-match grep against `data/photographs.csv` (2026-05-09): photo-0021 (Lovers, USA), photo-0147 (Work A, USA), photo-0235 (Dance, New Mexico), photo-0287 (Relationships, USA), photo-0329 (Learning, USA), photo-0437 (post-Faces / pre-Bomb bridge, Italy).

## Key excerpts / pages

**Biographical dates and nationality (rendered cleanly in the right-hand panel of the page, fetched 2026-05-09):**

- "1921 - 1986"
- "American" — note that Magnum (`src-magnum-ernst-haas`, fetched this round) records him as "Austrian"; the Haas Estate (`src-haas-estate-biography`, fetched this round) writes "Haas was born in Vienna in 1921" without assigning a nationality string. Haas naturalized as a U.S. citizen at some point after his 1951 move to the United States; ICP's "American" reflects citizenship status, Magnum's "Austrian" reflects birth country. The MoMA Master Checklist of *The Family of Man* records him as "Austrian" verbatim.
- "126 items" archived
- Role: "Artist"

**Verbatim from the biography paragraph (fetched 2026-05-09):**

- "Ernst Haas was born in Vienna and began studying photography at the Graphische Lehr und Versuchsanstalt in Vienna six years before acquiring his first camera in 1946."
- "After several photography-related jobs, he was offered a position at Life, and his first feature article, 'Returning Prisoners of War,' was published in both Heute and Life in 1949. This prompted Robert Capa to invite Haas to join the Magnum agency, the international cooperative founded by Capa, Henri Cartier-Bresson, George Rodger and Chim (David Seymour)."
- "Also in 1949, Haas purchased a Leica and began experimenting with color photography, the medium in which his work is best known."
- "His 'Magic Images of New York,' a twenty-four-page color photo essay, which appeared in LIFE in 1951 was both his and LIFE's first long color feature in print."
- "Haas served as president of Magnum in 1959-60, and as second director for The Bible (John Huston was first director) in 1966."

**Bibliography references (rendered cleanly):**

- "Reflections in a Glass Eye: Works from the International Center of Photography Collection, New York: Bulfinch Press in association with the International Center of Photography, 1999, pp. 217-18."

## Notes

- Perspective: institutional / archival.
- The ICP page gives year-only resolution (1921 / 1986). Day-month tokens (2 March 1921 birth; 12 September 1986 death) are recorded against the existing `src-nyt-1986-haas-obit` (in repo, NOT re-fetched in this round; carries `verified: false`).
- The "first long color feature in print" claim differs in date between the ICP page ("1951") and the Haas Estate biography (`src-haas-estate-biography`, fetched this round, "1953"). Both refer to the same New York photo essay; the Estate's date is more recent provenance and may have been corrected. Recorded as a discrepancy, not adjudicated here.
- The ICP page does not name *The Family of Man*. The connection is made via the MoMA Master Checklist (src-moma-exh-0569-master-checklist, in repo) at the plate level.
- Verified against fetched source on 2026-05-09 via `curl` (HTTP 200) into `.scratch/haas_icp.html`.
