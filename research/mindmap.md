---
title: Research mindmap
last_updated: 2026-04-29
---

> **Note.** This document was last bumped on 2026-04-29 (10-day refresh from 2026-04-19). Catalog: **265 rows** (53% of 503), via PRs #4 (47), #7 (47), #11 (98), #16 (25), #49 (24), #53 (24). Photographers: 20 rows + 4 short bios + 20 source entries (PR #8). Issue #9 closed via PR #12 on 2026-04-24 — the re-verification pass concluded that **18 of 20** photographer-source files cannot be directly fetched (institutional 403s / paywalls) and remain `verified: false`. The access-barrier problem is real and ongoing, but is documented under "Methodological gaps" below, not under issue #9 (which is closed). Five overview pages are now substantive: `/exhibition/` (PR #41), `/clervaux/` (PR #43), `/unesco/` (PR #45), `/tour/` (PR #47), `/reception/` (PR #27). Live on the site.

# Research mindmap

A living map of **what we know** (with sources) and **what we need to investigate** (gaps). Update this file after every merged research PR and whenever a new gap is identified.

## Overview

<pre class="tree">
<span class="tree-root">The Family of Man</span>
│   <i>Status legend: ✓ covered (substantive page or done) &middot; ⧗ partial / in progress &middot; ☐ planned &middot; ! blocked on external access</i>
│
├─ <b>1955 Exhibition</b> ✓ &mdash; <i>see <a href="{{ '/exhibition/' | relative_url }}">/exhibition/</a></i>
│  ├─ Museum of Modern Art, New York; 24 January &ndash; 8 May 1955
│  ├─ Edward Steichen, curator (assisted by Wayne Miller)
│  ├─ Paul Rudolph, installation design (temporary walls; print sizes 24&times;36 to 300&times;400&nbsp;cm)
│  ├─ Carl Sandburg, prologue (leaflet at the entrance)
│  ├─ ~270,000 NY visitors
│  └─ Closing image: W. Eugene Smith, <i>A Walk to Paradise Garden</i> (1946)
│
├─ <b>Catalog</b> ⧗ 53% (265/503)
│  ├─ 503 photographs / 273 photographers / 68 countries
│  ├─ 265 rows seeded (53%) &mdash; <i>see <a href="{{ '/photographs/' | relative_url }}">/photographs/</a></i>
│  ├─ 11 individual missing plate numbers in the printed checklist (#5, #7, #8, #61, #88, #90, #145, #149, #216, #246, #261)
│  └─ Selection process (~2&nbsp;million submissions commonly cited; primary source not yet verified)
│
├─ <b>Photographers</b> ⧗ 7% (20/273; 4 bios)
│  ├─ 20 of 273 photographer rows seeded (PR #8) &mdash; <i>see <a href="{{ '/photographers/' | relative_url }}">/photographers/</a></i>
│  ├─ 4 short bios (Capa, Wayne Miller, Doisneau, DeCarava)
│  └─ <b>!</b> 18 of 20 batch-1 source URLs remain <code>verified: false</code> (institutional 403s); access-barrier blocker for further batches
│
├─ <b>World Tour 1955&ndash;c.1962/1964/1965</b> ✓ &mdash; <i>see <a href="{{ '/tour/' | relative_url }}">/tour/</a></i>
│  ├─ 1955&ndash;56 US 6-city tour (Minneapolis &rarr; Pittsburgh)
│  ├─ International edition first stop: Corcoran Gallery, Washington D.C., 30 Jun&ndash;31 Jul 1955
│  ├─ USIA commissioning: 10 copies, ~160 towns, ~10M visitors (per CNA)
│  ├─ Verified abroad: Guatemala City 1955, Tokyo 1956, Johannesburg 1958, Moscow 1959 (year-only)
│  ├─ Three-way end-date discrepancy: 1962 (CNA collections) vs 1964 (CNA education) vs 1965 (CNA bio)
│  └─ 1992&ndash;94 second wave: Toulouse, Tokyo, Hiroshima (per UNESCO MoW register)
│
├─ <b>Clervaux, Luxembourg</b> ✓ &mdash; <i>see <a href="{{ '/clervaux/' | relative_url }}">/clervaux/</a></i>
│  ├─ 1964&ndash;66 US Government donation, at Steichen's request
│  ├─ 1966 Steichen Clervaux visit (CNA: <i>"expresses his wish for permanent installation"</i>)
│  ├─ 1974&ndash;89 partial exhibition at Clervaux Castle
│  ├─ 1994 permanent installation (year only; curator unattested)
│  ├─ 2010&ndash;13 second restoration: Studio Berselli, Milan + Nathalie Jacoby (NJOY) rooms
│  └─ Custodian: Centre national de l'audiovisuel (CNA)
│
├─ <b>UNESCO 2003</b> ✓ &mdash; <i>see <a href="{{ '/unesco/' | relative_url }}">/unesco/</a></i>
│  ├─ Memory of the World programme (founded 1992; 14-member IAC; 570 inscriptions to April 2026)
│  ├─ Submitted 2002 by Luxembourg; inscribed 2003
│  ├─ Justification: <i>"greatest photographic enterprise"</i>; <i>"memory of an entire era, that of the Cold War and McCarthyism"</i>
│  └─ Nomination-form PDFs linked but not yet read (URLs recorded)
│
├─ <b>Thematic clusters</b> ⧗ 8/11 used in catalog &mdash; <i>see <a href="{{ '/sections/' | relative_url }}">/sections/</a></i>
│  ├─ 11 clusters covering 22 MoMA-numbered checklist sections
│  ├─ UNESCO's "32 themes" / CNA's "37 themes" / our 11 clusters &mdash; documented discrepancy
│  └─ 8 clusters now used in the catalog; <code>sec-eating-everyday</code> first used in PR #53
│
└─ <b>Critical reception</b> ✓ (in repo) / ⧗ (Sekula, Turner pointers only) &mdash; <i>see <a href="{{ '/reception/' | relative_url }}">/reception/</a></i>
   ├─ Barthes 1957 &mdash; <i>The Great Family of Man</i> (in repo, verbatim)
   ├─ Sontag 1977 &mdash; <i>On Photography</i>
   ├─ Sekula 1981 &mdash; <i>The Traffic in Photographs</i> (NOT in repo, named only)
   ├─ Sandeen 1995 &mdash; <i>Picturing an Exhibition</i> (in repo; ToC visible, body borrow-only)
   ├─ Stimson 2006 &mdash; <i>The Pivot of the World</i>
   └─ Turner 2013 &mdash; <i>The Democratic Surround</i> (NOT in repo, named only)
</pre>

---

## What we know (with sources)

### Exhibition — 1955 MoMA *(substantive — PR #41)*
- **Opened 24 January 1955; closed 8 May 1955** at the Museum of Modern Art, New York. *Source: `src-moma-archives-highlights-1955`.*
- **Curator: Edward Steichen, assisted by Wayne Miller.** *Source: same.*
- **Installation design: Paul Rudolph** with temporary walls and print sizes ranging from **24 × 36 cm to 300 × 400 cm.** *Source: same.*
- **Prologue: Carl Sandburg**, distributed as a leaflet at the entrance and reprinted in both editions of the catalog. *Source: `src-moma-1955-press-release-book`.*
- **Two catalog editions published 21 June 1955** — deluxe ($10) and paper ($1) — both designed by Leo Lionni and printed by R.R. Donnelley. *Source: same.*
- **Scale: 503 photographs by 273 photographers from 68 countries.** *Source: `src-moma-archives-highlights-1955`; cross-anchored on `src-unesco-mow-2003` and `src-cna-collections-eng-family-of-man`.*
- **NY attendance: ~270,000.** *Source: `src-moma-archives-highlights-1955` (Relevance summary).*
- **Closing image: W. Eugene Smith, *A Walk to Paradise Garden* (1946).** *Source: same.*

### Thematic structure *(merged via PR #3; 8 of 11 clusters now used in catalog)*
- The 1955 catalog does **not** present a canonical numbered list of sections. Three institutional figures circulate: UNESCO's **32 themes** (`src-unesco-mow-2003`), CNA's **37 themes** (`src-cna-education`), and our working reconstruction of **11 thematic clusters** (`sec-prologue` through `sec-rededication-future`). The discrepancy is recorded in `research/sections.md` and surfaced on `/sections/`.
- **PR #53 first use of `sec-eating-everyday`** — Section 23 Food (#254-#268) maps to this cluster; this is the eighth cluster used in the catalog.

### Catalog — through plate #276 (265 rows, 53%)
- **Anchor source: MoMA Master Checklist for Exhibition #569** (`src-moma-exh-0569-master-checklist`, Tier 1) — gives per-plate photographer, agency/publication, nationality, "where taken," and print dimensions verbatim.
- **265 of 503 plates seeded** as of 2026-04-29, via PRs #4 (47), #7 (47), #11 (98), #16 (25), #49 (24), #53 (24). 238 plates remain.
- **11 individual missing plate numbers** in the printed checklist, distributed across 7 distinct gap events: **#5, #7, #8** (Prologue); **#61** (Mothers and Babies); **#88, #90** (Family Activities); **#145, #149** (Work A); **#216** (Adult Play); **#246** (between Sections 21–22); **#261** (in Section 23 Food). Reasons not stated in the document. Each adjacent row's `notes` records the gap.
- **Out-of-order plates documented**: #115 (Section 14 Land), #168 (Section 14 mid-flow), #194 (Section 19 Classical Music — Bischof at photo-0192), #269 (Section 25 Relationships — Ansel Adams at photo-0258, printed under the Section 25 heading on page 14 between #268 and #270). Three-digit plates #505 and #506 also appear inside sections 14–15 (deferred).
- **Photographer-name OCR corrections (PR #51)**: photo-0210 'Nick de Morgol?' → 'Nick de Morgoli' (French Vogue photographer); photo-0216 'Walter Sanner' → 'Walter Sanders' (German-born American LIFE staff photographer 1944-1961). Both verified against MoMA's own artist database.
- **Edward Steichen first appears as a plate photographer at #264 (photo-0253, Section 23 Food)** — a documented fact, not a curatorial-bias signal.
- **The Master Checklist records no titles and no dates for individual plates.** Steichen deprived the images of titles. Any year or title we add must be backed by a separate Tier-1/2 citation; secondary identifications are preserved with "reported, not primary-verified" caveats.
- **National attribution preserved verbatim** from the checklist — Capa "American," Erwitt "American," Horvat "Italian." Re-framing is a separate editorial decision, never a silent correction.

### Photographers — batch 1 seeded (PR #8)
- **20 photographer rows** covering every unique individual named in the first 47 catalog plates. 4 short bios exist (Capa, Wayne Miller, Doisneau, DeCarava) — the remaining 16 are CSV rows only.
- **20 source entries added** with `verified: false` flags (NYT obituaries, Magnum, ICP, CCP, Moderna Museet, etc.) because WebFetch returned 403 during the seed session. **Issue #9 closed via PR #12** (2026-04-24): the re-verification pass *was done* and concluded that 18 of 20 sources still cannot be directly fetched. The access-barrier problem persists and constrains scaling more photographer batches; tracked under "Methodological gaps" below.
- **Gender column blank** on all 20 rows per project tagging policy.

### World tour 1955–c.1962/1964/1965 *(substantive — PR #47)*
- **USIA commissioning attribution** verbatim: *"Commissioned by the USIA (United States Information Agency), an American governmental unit created during the Cold War to promote a positive image of the United States in front of the Russian propaganda."* *Source: `src-cna-education` (re-verified 2026-04-29).*
- **1955–56 US domestic 6-city tour**: Minneapolis → Dallas → Cleveland → Philadelphia → Baltimore → Pittsburgh, Jun 1955 – Nov 1956. *Source: `src-moma-1955-press-release-book` p. 2.*
- **International edition first stop**: Corcoran Gallery, Washington D.C., 30 Jun – 31 Jul 1955 (preceding Minneapolis by nine days). *Source: same.*
- **Multi-copy operational model**: *"ten copies with minor changes sent to nearly 160 towns. Each of the copies was weighing one tonne and a half, was packed in twenty-three crates and required more than six days to be mounted/installed."* *Source: `src-cna-education`.*
- **Verifiable international venues** (image captions on CNA portal): Palacio Protocolo, Guatemala City, 24 Aug – 18 Sept 1955; Takashimaya Department Store, Tokyo, March – April 1956; Government Pavilion, Johannesburg, 30 Aug – 13 Sept 1958; Moscow, USSR, 1959 (year-only). *Source: `src-cna-education`.*
- **Aggregate attendance**: ~10 million per CNA (both English collections page and education portal); ~9 million widely cited in secondary literature. The 91 venues / 37 countries figure is unverified pending NARA RG 306 (USIA records).
- **Three-way end-date discrepancy** (all CNA-published Tier 1): **1962** (`src-cna-collections-eng-family-of-man`), **1964** (`src-cna-education`), **1965** (`src-cna-edu-steichen-bio`). Documented openly; no winner picked without primary archival evidence.
- **1992–94 second tour wave**: restored versions touring internationally — Toulouse, Tokyo, Hiroshima named. *Source: `src-unesco-mow-2003` (re-verified 2026-04-29).*
- **Sandeen 1995 chapter titles** *"The family of man on the move"* and *"The family of man in Moscow"* confirmed at ToC level via Internet Archive; body text borrow-only and not accessed. *Source: `src-sandeen-1995` (Internet Archive ToC re-verification 2026-04-29).*

### Clervaux (Luxembourg) *(substantive — PR #43)*
- **1964–66 donation**: US Government donates *"the last complete version of the travelling exhibition"* to Luxembourg at Steichen's request. *Source: `src-cna-collections-eng-family-of-man` and `src-cna-collections-deu-family-of-man`.*
- **1966 Steichen Clervaux visit**: *"Edward Steichen visits his native country and expresses his wish for 'The Family of Man' to be exhibited permanently at Clervaux Castle."* *Source: `src-cna-collections-eng-family-of-man`.*
- **1963 White House meeting** with Grand Duchess Charlotte / *"I am a Luxembourgish boy"* / 1966 *"ideal place"* remark — Tier 3 only (`src-chronicle-lu-2025-cercle-cite-steichen`); not anchored to Tier 1 archives in this round.
- **1974–89 partial exhibition** at Clervaux Castle. *Source: `src-cna-collections-eng-family-of-man`.*
- **1994 permanent installation** (year only — exact date and curator of record not on either CNA collections page consulted). *Source: same.*
- **2010–13 second restoration**: closure September 2010, reopening July 2013. Conservation team: **Studio Berselli, Milan** (Silvia Berselli, Roberta Piantavigna, Francesca Vantellini, Isabel Dimas). Renovated rooms designed by **Nathalie Jacoby (NJOY)**. *Source: `src-cna-collections-eng-family-of-man`.*
- **Custodian: Centre national de l'audiovisuel (CNA).** *Source: `steichencollections-cna.lu`.*

### UNESCO Memory of the World *(substantive — PR #45)*
- **Memory of the World programme founded 1992**; 14-member International Advisory Committee appointed by UNESCO's Director-General; two-step inscription pathway (IAC recommendation + Executive Board endorsement); 2015 UNESCO Recommendation Concerning Preservation of, and Access to, Documentary Heritage. *Source: `src-unesco-mow-programme`.*
- **2003 inscription**: registration year 2003, submission year **2002** by **Luxembourg**; region Europe and North America; document type "Books." *Source: `src-unesco-mow-2003` (re-verified 2026-04-29).*
- **Justification language carried on register**: *"503 photographs taken by 273 photographers... from 68 countries"*; *"32 themes, arranged chronologically"*; *"Regarded as the 'greatest photographic enterprise ever undertaken'"*; *"the memory of an entire era, that of the Cold War and McCarthyism."* *Source: same.*
- **570 inscribed items** on the International Register as of 2026-04-29 fetch. *Source: `src-unesco-mow-programme`.*
- **Nomination form PDFs** (English and French) linked from the register page; URLs recorded in `src-unesco-mow-2003`; **content not read in any session so far** (access denied).

### Critical reception — major landmarks *(substantive — PR #27 + PR #43/#47 cross-references)*
- **Roland Barthes, "The Great Family of Man"** (in *Mythologies*, 1957). Foundational critique. *Source: `src-barthes-1957` (verbatim text via PR #3).*
- **Susan Sontag, *On Photography*** (1977). Related sentimentalism critique.
- **Allan Sekula, "The Traffic in Photographs"** *Art Journal* 1981 — Marxist ideological reading. **NOT in repo, not consulted; named only as pointer.**
- **Eric Sandeen, *Picturing an Exhibition: The Family of Man and 1950s America*** (U. New Mexico Press, 1995). Standard historical study. *Source: `src-sandeen-1995` (review-metadata + ToC level only).*
- **Blake Stimson, *The Pivot of the World*** (MIT Press, 2006). Re-reads the show within post-war photographic modernism.
- **Fred Turner, *The Democratic Surround*** (U. Chicago Press, 2013). Liberal-democratic design culture. **NOT in repo, not consulted; named only as pointer.**

---

## Roadmap — what will be covered

This section is **forward-looking** — what topics are planned next, in priority order. Items here are not yet merged. The boundary between this section and *"What we need to investigate"* is intent: roadmap items are work we intend to dispatch (the next 3-5 PRs at the front, longer-tail behind); investigation gaps are documented work-needed that may or may not be scheduled. Items move from this section into "What we know" as PRs merge.

### Scheduled (next 1–3 PRs)

These are concrete intended next dispatches. They have no open issues yet at time of writing; issues are opened when each PR begins.

- **Catalog batch #277–301** — 25 plates from the MoMA Master Checklist (continuing from photo-0265). Mechanical, ~30 min, well-understood pattern after PRs #49 and #53.
- **`/tour/` map visualisation** — visualise the verified venues attested in `/tour/` (6 US domestic, 4 international, 1 Moscow year-only, 3 1992-94 second-wave) on a static SVG / Leaflet map. No new external claims; the venue data already lives in source entries.
- **Photographer biographies batch 2** — gated on the access-barrier resolution; either via `gh api` / academic-library proxy / archive.org snapshots, or by accepting Tier 3 carries with explicit `verified: false` until institutional sites become reachable.

### Backlog (planned, not yet scheduled)

Known work, intent established, sequence not yet pinned.

- **Catalog completion** — 8 more 25-plate batches to reach 503/503 (#302–326, #327–351, #352–376, #377–401, #402–426, #427–451, #452–476, #477–503). Plus the out-of-range three-digit plates (#505, #506).
- **Photographer biographies batches 3–12** — sequential after batch 2.
- **Steichen-the-photographer page deepening** — current page covers the life arc; could extend with the curatorial-period detail and the relationship to *The Family of Man* itself.
- **1955 catalog plate-titles + dates** — needs a primary read of the printed 1955 catalog. Expected source: Luxembourg National Library, or an unrestricted Internet Archive scan once CDL borrow is completed.
- **Verbatim Sandburg prologue with page numbers** — same blocker as plate-titles.
- **1994 Clervaux inauguration day-level detail** — *Luxemburger Wort* / *Tageblatt* press archives for the inauguration date, programme, and named curator.
- **1964–1974 Luxembourg storage decade** — Luxembourg cultural-affairs ministry archival pass for where the prints physically lived between donation and the 1974 partial-display opening.
- **"First" restoration phase before 2010–13** — date, scope, conservator-of-record. Implied by the German source's *"second restoration phase"* wording.
- **1992–94 second-wave full itinerary** — UNESCO register names Toulouse, Tokyo, Hiroshima as a sample; CNA records would carry the full venue list.
- **2013 + 2023 inscription anniversary events** — CNA annual reports + Luxembourg cultural press coverage for the two decennial milestones.
- **1955 installation specifics** — Paul Rudolph's installation drawings at MoMA Archives.
- **1955 NY opening reception** — contemporary reviews in *NYT*, *Art News*, *Aperture*, 1955-56.
- **Per-photograph provenance pages** — phase 3 long-tail (one article per photograph, 503 total).
- **Theme-count reconciliation essay** — a written treatment of the 32 (UNESCO) / 37 (CNA) / 11 (this wiki) discrepancy, beyond the current `research/sections.md` notes.

### Stretch (long-horizon, gated on external access)

Items that depend on archival access, scholarly literature acquisition, or other external blockers. May or may not become tractable.

- **USIA RG 306 (NARA)** — the single most consequential gap. Would resolve the 9M visitors / 91 venues / 37 countries headline aggregate, the 1962-vs-1964-vs-1965 end-date discrepancy, and per-copy disposition. Multiple fetch attempts denied across sessions.
- **Sandeen 1995 full text** — particularly the *"on the move"* and *"in Moscow"* chapters. CDL borrow not yet completed; ToC visible at archive.org.
- **Turner 2013** *(The Democratic Surround)* as in-repo source — would supply the strongest recent reading of the exhibition's liberal-internationalist visual culture.
- **Sekula 1981/1986 essays** as in-repo sources — would supply the strongest Marxist critique of the show as ideological work.
- **UNESCO 2002 nomination forms** (English + French PDFs) — URLs recorded in `src-unesco-mow-2003`; access denied to date. Would carry the formal IAC justification text.
- **MoMA International Program records** — would resolve per-copy tour log and itinerary.
- **Critical reception in non-English scholarship** — French (CNA publications, *Revue des musées de France*), German (1994 Clervaux opening press), Luxembourgish.

---

## What we need to investigate (prioritized gaps)

### P0 — foundational (blocks everything else)
- **Catalog plates 277–end** — 238 plates remain after PR #53. Continue with the MoMA Master Checklist; also catalog the out-of-range three-digit plates (#505, #506).
- **Plate titles and dates** — the Master Checklist has neither. Need the *printed 1955 catalog* (the book) or Steichen's curatorial correspondence. Expected primary source: the Luxembourg National Library or a non-restricted scan.
- **Verbatim Sandburg prologue text with page numbers** — same blocker.
- **Canonical 1955 catalog pages** for the headline figures (503/273/68) — currently anchored on three institutional summaries (MoMA Archives Highlights, UNESCO register, CNA collections page); a primary-source citation to specific pages of the 1955 catalog is still missing.

### P1 — core (phase 2)
- **273 photographer biographies** — 4/273 done; 269 remain. Each needs dates, nationality, and a Tier-1/2 source. The PR #8 re-verification pass (closed via PR #12) concluded that 18 of 20 batch-1 source URLs cannot be directly fetched — a persistent access-barrier problem (see "Methodological gaps" below) that constrains scaling further batches.
- **NARA RG 306 (USIA records)** — the single most consequential gap for the world-tour aggregate (9M/91/37). Fetch attempts denied. A future pass should consult the RG 306 finding aid (Exhibits Division), per-copy / per-venue tour logs, and closing-administration date (which would resolve the 1962/1964/1965 end-date discrepancy).
- **MoMA International Program records** — would close the per-copy disposition question (one copy went to Luxembourg as the donation; fates of the other nine copies unknown).
- **Sandeen 1995 full text** — particularly the *"on the move"* and *"in Moscow"* chapters. CDL borrow not completed.
- **Turner 2013** *(The Democratic Surround)* and **Sekula's essays** — not in repo; future entries under `sources/2010s/` and `sources/1980s/`.
- **Moscow 1959 detail** — confirm Sokolniki Park / American National Exhibition identification, dates, attendance, press reception. Eisenhower Presidential Library holdings would be the natural primary source.
- **1994 Clervaux inauguration detail** — exact date, curator of record, installation design, opening programme. *Luxemburger Wort* and *Tageblatt* press archives, or a CNA press release of the day.
- **1964–1974 storage decade** — where the prints physically lived between donation and the 1974 partial-display opening at Clervaux. Luxembourg cultural-affairs ministry archives.
- **The "first" restoration phase** — implied by the German page's *"second restoration phase 2010–13"* wording. Date, scope, conservator-of-record all unattested.
- **2010–13 conservation methodology** — Studio Berselli's published record + CNA annual reports for the period.
- **1992–94 second-wave full itinerary** — UNESCO register names Toulouse, Tokyo, Hiroshima as a sample; the full venue list would be in CNA records.
- **UNESCO nomination form PDFs (2002)** — both English and French; URLs recorded in `src-unesco-mow-2003` but access denied. The formal IAC justification text submitted in 2002 is the strongest available primary source for the inscription's stated rationale.
- **2013 and 2023 UNESCO inscription anniversary events** — no records consulted; CNA annual reports + Luxembourg cultural press are the natural sources.
- **1963 Charlotte / Steichen meeting** — currently rests on Tier 3 only (`src-chronicle-lu-2025-cercle-cite-steichen`). Verifiable against Cour grand-ducale or U.S. State Department diplomatic records.
- **1955 installation photographs** — Paul Rudolph's drawings at MoMA Archives.
- **Opening reception** — contemporary reviews in *NYT*, *Art News*, *Aperture*, 1955–56.
- **Critical reception in non-English scholarship** — French and German writing, especially from Clervaux-era CNA.

### P2 — enrichment (phase 3)
- **Per-photograph provenance** for each of the 503 — one article per photograph.
- **Photographer compensation and consent** arrangements.
- **Selection process** — how the submission pool was cut to 503 (Wayne Miller's role).
- **Exhibition funding and sponsorship** in 1955.
- **Current CNA curatorial practice** — rotation schedule, loans, ongoing conservation.
- **Anniversary events** — 50th (2005), 60th (2015), 70th (2025) of the original 1955 opening.

### Language gaps
- **Francophone scholarship** (CNA publications, *Revue des musées de France*, French press 1994–present).
- **Germanophone scholarship** (1994 Clervaux opening press in *Luxemburger Wort*, *Tageblatt*; German reviews).
- **Luxembourgish-language coverage** of Clervaux.

### Methodological gaps
- **Theme-count reconciliation** — UNESCO 32, CNA 37, our 11. Cross-source treatment exists in `research/sections.md` but is not yet a published essay.
- **WebFetch access to institutional archives** — MoMA / Magnum / ICP / NYT / NARA returned 403 across several sessions, including the dedicated re-verification pass under PR #12 (which concluded 18 of 20 PR #8 sources remained inaccessible). Options to unblock: live audit pass with human-operated browser, archive.org snapshots, or a `gh api` / academic-library proxy. **Issue #9 is closed; the underlying access-barrier problem is the open item.**
- **Catalog-builder source-entry coverage** — the in-repo `src-moma-exh-0569-master-checklist` excerpt block covers Sections 1–7 only; the catalog rows beyond #50 cite the linked PDF (per the file's URL field) rather than verbatim Key excerpts. This is the established pattern (217+ rows so far) but worth eventually expanding into a comprehensive section-by-section source-entry transcription, particularly if the Tier-1 nomination flow strengthens further.

---

## Active investigations

| # | Title | State | Notes |
|---|---|---|---|
| [#1](https://github.com/danlex/thefamilyofman/issues/1) | Catalog plates 1–50 | `CLOSED` via PR #4 | 47 rows. |
| [#2](https://github.com/danlex/thefamilyofman/issues/2) | Thematic sections + prologue | `CLOSED` via PR #3 | Merged before judges; re-audit pending. |
| [#5](https://github.com/danlex/thefamilyofman/issues/5) | Catalog plates 48–100 | `CLOSED` via PR #7 | +47 rows. |
| [#6](https://github.com/danlex/thefamilyofman/issues/6) | Photographer bios batch 1 | `CLOSED` via PR #8 | 20 rows + 4 bios + 20 source entries. |
| [#9](https://github.com/danlex/thefamilyofman/issues/9) | Re-verify PR #8 citations | `CLOSED` via PR #12 | Re-verification pass done 2026-04-24; 18 of 20 sources remain `verified: false` due to access barriers. Underlying problem tracked in "Methodological gaps." |
| [#10](https://github.com/danlex/thefamilyofman/issues/10) | Catalog plates 101–200 | `CLOSED` via PR #11 | +98 rows. |
| [#15](https://github.com/danlex/thefamilyofman/issues/15) | Catalog plates 201–226 | `CLOSED` via PR #16 | +25 rows; pre-merge fixes from judge-bias and judge-grounding (photo-0201 character-type). |
| [#27](https://github.com/danlex/thefamilyofman/issues/27) | /reception/ expansion | `CLOSED` via PR #27 | Substantive overview merged. |
| [#41](https://github.com/danlex/thefamilyofman/issues/41) | /exhibition/ expansion | `CLOSED` via PR #41 | Substantive overview merged. |
| [#42](https://github.com/danlex/thefamilyofman/issues/42) | /clervaux/ expansion | `CLOSED` via PR #43 | Substantive overview; new source `src-cna-collections-eng-family-of-man`. |
| [#44](https://github.com/danlex/thefamilyofman/issues/44) | /unesco/ expansion | `CLOSED` via PR #45 | Substantive overview; new source `src-unesco-mow-programme`. |
| [#46](https://github.com/danlex/thefamilyofman/issues/46) | /tour/ expansion | `CLOSED` via PR #47 | Substantive overview; three source entries updated. |
| [#48](https://github.com/danlex/thefamilyofman/issues/48) | Catalog batch #227–251 | `CLOSED` via PR #49 | +24 rows (gap at #246). |
| [#50](https://github.com/danlex/thefamilyofman/issues/50) | Photo-0210 / photo-0216 name corrections | `CLOSED` via PR #51 | OCR-error corrections verified against MoMA artist database. |
| [#52](https://github.com/danlex/thefamilyofman/issues/52) | Catalog batch #252–276 | `CLOSED` via PR #53 | +24 rows (gap at #261); first use of `sec-eating-everyday`. |
| [#54](https://github.com/danlex/thefamilyofman/issues/54) | Bump mindmap + progress.yml | `OPEN` | This PR. |

---

## Update protocol

**Who updates this file:** anyone merging a research PR, and the maintainer when a new gap is identified.

**When to update:**
- After a PR merges that adds to `data/`, `sources/`, or `research/` — move the relevant item from the gaps list to the known list, with its source citation.
- When a judge rejects a claim as unsupported — move the item from known back to gaps with a reason.
- When a new investigation issue opens — add it to the **Active investigations** table.

**How to update:**
- Edit via `✏️ Edit this page` from the published wiki, or directly on GitHub.
- Bump `last_updated` in the frontmatter to today's date.
- PRs to this file go through the judge panel like any other research content.

**What not to put here:**
- Speculation unsupported by any source (use the `notes` column of the affected CSV row, or a research file's own "Open questions" section).
- Long excerpts from sources (those belong in `sources/<decade>/<slug>.md`).
- Photograph- or photographer-level detail (those belong in their respective wiki articles).
