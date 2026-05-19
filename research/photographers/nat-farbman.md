# Nat Farbman (1907–1988)

Nat Farbman (full form: N. R. Farbman) was an American photojournalist and LIFE magazine staff photographer, best known for his sustained coverage of Bechuanaland (today Botswana) bush communities and his wide-ranging international reportage. Wikipedia (fetched 2026-05-19) records his birth as 1907 in Poland, immigration to the USA in 1911, and death as 1988 in the United States (src-wikipedia-nat-farbman-pointer). The LIFE archive page (fetched 2026-05-19) corroborates the 1907–1988 dates verbatim: "N.R. Farbman (1907–1988)" (src-life-archive-farbman-bio).

## Career

Wikipedia (fetched 2026-05-19) records that Farbman studied electrical engineering at the University of Santa Clara before becoming a photojournalist. The LIFE archive page (fetched 2026-05-19) confirms: "During his 15 years as a LIFE staffer, 'Nat' was considered one of its most versatile practitioners, covering stories in the US and extensively abroad" (src-life-archive-farbman-bio). Wikipedia gives his LIFE tenure as "from 1946 to 1961," with his first LIFE assignment covering Greek elections in April 1946, followed by international assignments across Italy, Austria, and South Africa (src-wikipedia-nat-farbman-pointer).

Farbman worked as part of a husband-and-wife photography team with Pat English. There is a discrepancy in the fetched sources about the marriage date: the LIFE archive page (src-life-archive-farbman-bio, fetched 2026-05-19) says he "married the former fashion model and photographer Pat English in 1940"; Wikipedia (src-wikipedia-nat-farbman-pointer, fetched 2026-05-19) gives the marriage year as 1938 and names her "Patsy (Pat) English." Neither is a Tier-1 source; the discrepancy is noted and not resolved here. Wikipedia adds that Pat English "learned photography from Ansel Adams" whom she met in 1936 working as his commercial model (src-wikipedia-nat-farbman-pointer) — this claim is not corroborated by any other fetched source this round.

## Connection to *The Family of Man*

Farbman is the most represented single photographer in the MoMA Master Checklist among the batch researched here. A strict-match grep against `data/photographs.csv` (2026-05-19) returns nine Farbman plates, confirming and correcting the `photo_count=1` carried in the original CSV row (which reflected only the first plate visible at the time of initial CSV creation):

| id | checklist # | country | section |
|----|-------------|---------|---------|
| photo-0004 | #4 | Belgian Congo | Prologue |
| photo-0062 | #66 | Bechuanaland | Children A |
| photo-0103 | #109 | Bechuanaland | Fathers and Sons |
| photo-0109 | #116 | Bechuanaland | Family Groups |
| photo-0117 | #123 | Bechuanaland | Land |
| photo-0306 | #317 | France | Relationships |
| photo-0317 | #328 | Bechuanaland | Learning |
| photo-0330 | #342 | USA | Learning |
| photo-0419 | #434 | France | Man's Judgment |

This nine-plate presence is the largest FoM representation among the four photographers in this batch. The LIFE archive page (fetched 2026-05-19) states verbatim that Farbman's "work on tribes in Botswana was included in the Museum of Modern Art's Family of Man exhibit" (src-life-archive-farbman-bio). Wikipedia (fetched 2026-05-19) specifies that "six photographs from his Bechuanaland series were featured in *The Family of Man*, with the most renowned being 'Kung San storyteller'" (src-wikipedia-nat-farbman-pointer). The Wikipedia claim of six Bechuanaland plates is consistent with the checklist Bechuanaland subset (six of his nine plates are set in Bechuanaland); the Wikipedia article's framing omits his Belgian Congo, France, and USA plates.

The geographic distribution of Farbman's nine plates — Belgian Congo (×1), Bechuanaland (×6), France (×2), USA (×1) — reflects a sustained editorial focus on sub-Saharan African communities unusual among FoM contributors, most of whom drew on more geographically dispersed material.

## Open questions

- Marriage year (1938 per Wikipedia vs 1940 per LIFE archive): not resolvable from fetched sources.
- The specific subjects of the Bechuanaland plates beyond the general "bushmen tribes" framing: the MoMA checklist records no captions or subject identifiers for these plates; "Kung San storyteller" is claimed by Wikipedia but not confirmed in any fetched Tier-1 source this round.
- Pat English's biographical dates: remain unverified (noted in the existing `pher-pat-english` CSV row).

## References

- src-moma-exh-0569-master-checklist — MoMA Exhibition #569 Master Checklist (Tier 1, in repo)
- src-life-archive-farbman-bio — LIFE archive page (Tier 3, fetched 2026-05-19 and 2026-04-24)
- src-wikipedia-nat-farbman-pointer — Wikipedia pointer (Tier 3, fetched 2026-05-19)
