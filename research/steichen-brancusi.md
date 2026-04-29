---
title: "Steichen and Brancusi: friendship, Bird in Space, and the 1928 customs case"
type: research-note
namespace: steichen-brancusi
status: working-note
verified: false
last-updated: 2026-04-30
sources:
  - src-aperture-prints-brancusi-1925
  - wikipedia-bird-in-space (pointer-only, fetched 2026-04-30)
  - wikipedia-constantin-brancusi (pointer-only, fetched 2026-04-30)
  - bellevuecollege-brancusi-court-extract (pointer-only, fetched 2026-04-30)
---

# Steichen and Brancusi

This is a working research note. It documents what was *fetched* and *verified* in the
2026-04-30 round, and explicitly separates anchored facts from secondary-literature
pointers that have not been re-verified against a Tier-1 source.

## Anchored this round (Tier 1–2 fetched)

- **Steichen photographed Brancusi inside his Paris studio in 1925.**
  Source: `src-aperture-prints-brancusi-1925` (Aperture Foundation product page, fetched 2026-04-30).
  Verbatim title: "Brancusi in His Studio, Paris, 1925." This is the only Steichen-Brancusi
  photograph dating that is currently anchored at Tier 2 in this repo.

## Pointer-only this round (Wikipedia + secondary; not re-verified at Tier 1)

The following claims are recorded from Wikipedia raw text fetched 2026-04-30 and a
Bellevue College educational page (also Tier-3-equivalent) fetched 2026-04-30. Per
`CREDIBILITY.md` Wikipedia is pointer-only — these are documented here so future
researchers know what to verify against a Tier-1 source (MoMA, Met Museum, Centre
Pompidou, court reporter, or `src-steichen-1963-life`).

### The 1926 import and the 1928 customs case

- October 1926: a *Bird in Space* sculpture by Brancusi arrived in New York harbor on
  the steamship *Paris*, alongside 19 other Brancusi sculptures.
- The Wikipedia "Constantin Brâncuși" article (fetched 2026-04-30) says: "in 1926 …
  photographer Edward Steichen purchased it and shipped it to the United States."
- The Wikipedia "Bird in Space" article (fetched 2026-04-30) says Steichen "was to take
  possession of *Bird in Space* after exhibition" and "filed an appeal to the U.S.
  Customs' decision to reclaim the money" in November 1926.
- Customs imposed a 40% duty (~$230) classifying the object as a "manufactured metal
  object." The 1922 Tariff Act provided that art duty-free if "the original work of a
  professional sculptor."
- November 1928: Judges Young and Waite of the U.S. Customs Court found in favor of the
  artist. Justice Waite's opinion (quoted by both the Wikipedia article and the
  Bellevue College extract) acknowledged a "so-called new school of art, whose
  exponents attempt to portray abstract ideas rather than imitate natural objects."
- **Open question / contested in the secondary literature:** the Wikipedia "Bird in
  Space" article (fetched 2026-04-30) names Steichen among "Six major figures [who]
  testified for Brâncuši that *Bird in Space* was art." The Bellevue College page,
  which reproduces what it calls the actual court-extract record, contains Jacob
  Epstein's deposition and Justice Waite's judgment but **does not show Steichen as a
  testifying witness**; Steichen appears only in that page's introductory narrative as
  the importer who appealed the duty. The two pointer sources therefore disagree on
  whether Steichen personally took the witness stand, vs. being the appellant /
  consignee whose name is on the case caption. Resolving this requires a Tier-1 court
  reporter source (the actual *Brancusi v. United States* opinion text, 28 U.S.T.D.
  428) or the Niven 1997 biography or Steichen's own 1963 autobiography.

### The earlier Steichen-Brancusi friendship

- The Wikipedia "Constantin Brâncuși" article (fetched 2026-04-30) credits two earlier
  Steichen photographs: "Brâncuši's Paris studio, 1920, photograph by Edward Steichen"
  and "Photograph by Edward Steichen, 1922" (a portrait).
- Aperture's description (`src-aperture-prints-brancusi-1925`) calls Brancusi "one of
  the founding figures of modern sculpture" and Steichen "one of the founding figures
  of photography" — institutional / promotional framing.
- A WebSearch result (Google CSE, 2026-04-30) returned a Met Museum object record for
  "Edward J. Steichen — Brancusi's 'Endless Column' in Mr. Steichen's Garden,
  Voulangis, France" (Met search/687837), suggesting Brancusi gave or sold Steichen
  an *Endless Column* sculpture for installation at his Voulangis house in France.
  **Met catalog page returned HTTP 429 in this round; not anchored.**
- A WebSearch result also returned a MoMA object record "Edward Steichen. Constantin
  Brancusi in his Studio. 1927" (MoMA collection 48872). **MoMA catalog page returned
  HTTP 403 in this round; not anchored.**

### What the secondary literature implies but is *not* fetched here

- That Steichen and Brancusi met through Auguste Rodin. Repeated in tertiary sources
  (Wikipedia, blogs); not anchored to a Tier-1 source in this round.
- That Steichen was the 1926 *consignee* on the manifest (legal-procedural detail).
  Implied by both Wikipedia articles but not anchored from a court record.
- That Marcel Duchamp accompanied the sculptures from Europe (one Wikipedia variant)
  vs. that Steichen accompanied them (another variant). The two pointer sources differ.
- The page count, chapter, and verbatim text of Steichen's own account in *A Life in
  Photography* (1963) → see `src-steichen-1963-life` (`verified: false` until
  body text is read).

## What is safe to write on `/steichen/` without further fetches

- A short section noting that Steichen and Brancusi were friends; that Steichen
  photographed Brancusi's studio and Brancusi himself in the 1920s; that Steichen
  imported a *Bird in Space* sculpture in 1926 which U.S. Customs refused to recognize
  as art; that Steichen filed the appeal that became *Brancusi v. United States*; and
  that the U.S. Customs Court ruled in favor of the sculpture's status as art in
  November 1928.
- Each of these claims must be cited to the corresponding pointer source (Wikipedia
  raw, Bellevue College, Aperture print page) and the section must include a
  `verified: false` flag with a clear "to-do" pointing at primary sources for upgrade.

## Upgrade path (next research pass)

In priority order:

1. Read the relevant chapter of `src-steichen-1963-life` (Steichen's own autobiography)
   — Tier 1, primary, in-repo as a source entry but body text not yet accessed.
2. Read Niven 1997 (`src-niven-1997`) — Tier 2, in-repo but CDL-restricted.
3. Fetch the Met Museum catalog records (search/266850, search/687837) directly when
   the rate limit clears — for the 1920 studio photograph and the *Endless Column* in
   Steichen's Voulangis garden.
4. Fetch MoMA collection record 48872 directly — for the 1927 *Constantin Brancusi in
   his Studio*.
5. Locate the official court reporter citation for *Brancusi v. United States* (the
   1928 U.S. Customs Court decision) and quote the operative language directly. The
   conventional reporter citation form is commonly given in the secondary literature
   as "T.D. 43063, 54 Treas. Dec. 428 (Cust. Ct. 1928)"; this exact form has NOT been
   verified against any fetched primary source in this round and should not be cited
   without confirmation.
6. Fetch a Centre Pompidou Atelier Brancusi page (Pompidou holds the reconstruction of
   Brancusi's studio at the Impasse Ronsin) for institutional context on Brancusi's
   studio practice.
