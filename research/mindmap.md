---
title: Research mindmap
last_updated: 2026-05-02
---

> **Note.** Last bumped 2026-05-02 to absorb the catalog-completion reconciliation pass: out-of-range three-digit plates **#505 (Lennart Nilsson, Belgian Congo) and #506 (William Garnett, USA)** are now seeded as `photo-0490` and `photo-0489`, and the gap between 488/503 has been formally reconciled in [`research/catalog-reconciliation-503.md`](catalog-reconciliation-503.md). Catalog row count: **490 rows** (closed corpus against `src-moma-exh-0569-master-checklist`). Also absorbed: PRs #102 (Africa-gap, issue #88), #103 (issue #61 hedge-cleanup), #105+#106 (new dedicated `/brancusi/` page with Steichen's 1922 portrait of Brâncuși). Per-PR breakdown (verified by `git show <commit> -- data/photographs.csv | grep -c '^+photo-'`): PRs #4 (47), #7 (47), #11 (98), #16 (25), #49 (24), #53 (24), #60 (25), #65 (25), #67 (24), #69 (23), #71 (24), #73 (25), #75 (25), #77 (25), #79 (27); sum = 488. All 11 thematic clusters are now used (final coverage). Two structural milestones: photo-0441 (#456) — H-bomb plate, Atomic Energy Commission, Marshall Islands, 96×120 cm; photo-0488 (#503) — *A Walk to Paradise Garden*, W. Eugene Smith, 1946 — the show's closing image. Photographers: 20 rows + 4 short bios + 20 source entries (PR #8); issue #9 closed via PR #12 (2026-04-24); 18 of 20 sources remain `verified: false` due to institutional 403s — access-barrier problem persists, tracked under "Methodological gaps". Five overview pages are substantive (`/exhibition/`, `/clervaux/`, `/unesco/`, `/tour/`, `/reception/`); `/tour/` carries a Leaflet venue-map (PR #62). Live on the site.

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
├─ <b>Catalog</b> ✓ closed corpus (490 rows; 488/503 reconciliation completed)
│  ├─ 503 photographs / 273 photographers / 68 countries
│  ├─ 490 rows seeded across 15 catalog batches + 1 reconciliation pass (PRs #4, #7, #11, #16, #49, #53, #60, #65, #67, #69, #71, #73, #75, #77, #79, and the present out-of-range-plates pass) &mdash; <i>see <a href="{{ '/photographs/' | relative_url }}">/photographs/</a></i>
│  ├─ 16 individual missing plate numbers in the printed checklist: #5, #7, #8 (Prologue) · #61 (Mothers and Babies) · #88, #90 (Family Activities) · #145, #149 (Work A) · #216 (Adult Play) · #246 (between Sections 21-22) · #261 (Section 23 Food) · #337, #346 (between Sections 26-27) · #362 (Section 28) · #399 (Section 32) · #425 (Section 35)
│  ├─ Out-of-order plates: #115, #168, #194, #269, #358, #422, and entire Section 38 block (#441&ndash;#445) printed after Section 39 on PDF page 23
│  ├─ Letter-suffix supplements: #404A (Warsaw Ghetto, German photographer unknown, photo-0390); #11A&ndash;#11F Eugene Harris recurring-coda series (single row at photo-0008 with inline notes at photo-0070, photo-0185, photo-0228, photo-0276, photo-0334)
│  ├─ <b>Structural milestones</b>: photo-0441 (#456) H-bomb plate, AEC/Marshall Islands, 96&times;120 cm &mdash; the show's narrative climax; photo-0488 (#503) <i>A Walk to Paradise Garden</i> by W. Eugene Smith, 1946 &mdash; the closing image (FIRST row in catalog with populated title + year + multi-source citation)
│  ├─ Three-digit plates #505, #506 documented in earlier batch notes (photo-0114, photo-0135, photo-0160) but not seeded as separate rows
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
├─ <b>Thematic clusters</b> ✓ 11/11 used in catalog (final coverage) &mdash; <i>see <a href="{{ '/sections/' | relative_url }}">/sections/</a></i>
│  ├─ 11 clusters covering 42 MoMA-numbered checklist sections
│  ├─ UNESCO's "32 themes" / CNA's "37 themes" / our 11 clusters &mdash; documented discrepancy
│  └─ All 11 clusters now used in <code>data/photographs.csv</code> after PR #79: <code>sec-prologue</code>, <code>sec-lovers</code>, <code>sec-marriage-birth</code>, <code>sec-family-children</code>, <code>sec-play-learning</code>, <code>sec-work</code>, <code>sec-eating-everyday</code>, <code>sec-relationships-community</code>, <code>sec-hardship-suffering-war</code>, <code>sec-death-mourning</code>, <code>sec-rededication-future</code>. SCHEMA-GAP NOTE: Sections 28 (Religious Expression), 29 (Aloneness), 30 (Aspirations), 41 (Couples), 42 (Childhood Magic) are mapped approximately to <code>sec-rededication-future</code> with explicit "approximate, not canonical" hedging on each row; a future schema PR may introduce finer-grained clusters.
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

### Thematic structure *(merged via PR #3; all 11 of 11 clusters now used after PR #79)*
- The 1955 catalog does **not** present a canonical numbered list of sections. Three institutional figures circulate: UNESCO's **32 themes** (`src-unesco-mow-2003`), CNA's **37 themes** (`src-cna-education`), and our working reconstruction of **11 thematic clusters** (`sec-prologue` through `sec-rededication-future`). The discrepancy is recorded in `research/sections.md` and surfaced on `/sections/`.
- **All 11 clusters are now used in the catalog** as of PR #79 (closing-image batch). First-use sequence: `sec-prologue`, `sec-lovers`, `sec-marriage-birth`, `sec-family-children` (PR #4); `sec-relationships-community`, `sec-work` (PRs #7, #11); `sec-eating-everyday` (PR #53); `sec-play-learning` (PR #67); `sec-hardship-suffering-war`, `sec-death-mourning` (PR #71); `sec-rededication-future` (PR #75).
- **SCHEMA-GAP FINDING**: Sections 28 RELIGIOUS EXPRESSION, 29 ALONENESS AND COMPASSION, 30 ASPIRATIONS, 41 COUPLES, and 42 CHILDHOOD MAGIC do not have direct cluster matches in `data/sections.csv` — all five map approximately to `sec-rededication-future` with explicit "approximate, not canonical" hedging on every affected row. A future schema PR may introduce finer-grained clusters (e.g., `sec-religious-expression`, `sec-aloneness`, `sec-couples`, `sec-childhood-magic`) or re-evaluate the existing 11-cluster reconstruction.

### Catalog — closed corpus (490 rows; #1-#503 + #404A + #505 + #506)
- **Anchor source: MoMA Master Checklist for Exhibition #569** (`src-moma-exh-0569-master-checklist`, Tier 1) — gives per-plate photographer, agency/publication, nationality, "where taken," and print dimensions verbatim.
- **490 plate rows seeded** — closed corpus against `src-moma-exh-0569-master-checklist`. 488 rows seeded as of PR #79 across 15 catalog batches (PRs #4 (47), #7 (47), #11 (98), #16 (25), #49 (24), #53 (24), #60 (25), #65 (25), #67 (24), #69 (23), #71 (24), #73 (25), #75 (25), #77 (25), #79 (27); sum = 488). The reconciliation pass at [`research/catalog-reconciliation-503.md`](catalog-reconciliation-503.md) writes up the precise 488/503 accounting: 503 numbered slots − 17 documented missing numbers + 1 (#11A unique row) + 1 (#404A added) + 2 (#505 + #506 as `photo-0490` and `photo-0489` in the present pass) = **490**. The 5 Eugene Harris recurring-image entries (#11B–F) remain noted inline at adjacent rows per the established convention.
- **Two structural milestones** during the catalog completion:
  - **photo-0441 (#456)**: H-bomb plate, Atomic Energy Commission, Marshall Islands, 96×120 cm — the show's narrative climax per `src-moma-archives-highlights-1955` (Tier 1).
  - **photo-0488 (#503)**: *A Walk to Paradise Garden* by W. Eugene Smith (1946), USA, 42½×36 cm — the canonical closing image per `src-moma-archives-highlights-1955`. **First row in the catalog with populated title + year + multi-source citation.**
- **16 individual missing plate numbers** in the printed checklist: #5, #7, #8 (Prologue); #61 (Mothers and Babies); #88, #90 (Family Activities); #145, #149 (Work A); #216 (Adult Play); #246 (between Sections 21-22); #261 (Section 23 Food); #337, #346 (between Sections 26-27); #362 (Section 28); #399 (Section 32); #425 (Section 35). Each adjacent row's `notes` records the gap.
- **Out-of-order plates documented**: #115, #168, #194, #269 (single-plate); #358 (Duncan, Saudi Arabia — physical Section 26 / numerical Section 27, mapped numerically per the established precedent at photo-0339); #422 (Crane, Germany — physical Section 34 / numerical Section 35, deliberately mapped to physical at photo-0400 with documented divergence); ENTIRE Section 38 GOVERNMENT block (#441-#445) printed on PDF page 23 AFTER Section 39 on page 22, recorded in numerical order per photo-0339 precedent.
- **Letter-suffix supplements**: #404A (Warsaw Ghetto, German photographer unknown, photo-0390 — distinct CSV row because the checklist prints distinct dimensions); Eugene Harris #11A-#11F recurring-coda series (single CSV row at photo-0008 with inline notes at photo-0070, photo-0185, photo-0228, photo-0276, photo-0334).
- **Three-digit out-of-range plates #505 and #506** documented in earlier batch notes (photo-0114, photo-0135, photo-0160) but NOT separately seeded as rows. A follow-up cleanup PR is needed if the project policy decides to add them.
- **Photographer-name OCR corrections (PR #51)**: photo-0210 'Nick de Morgol?' → 'Nick de Morgoli' (French Vogue photographer); photo-0216 'Walter Sanner' → 'Walter Sanders' (German-born American LIFE staff photographer 1944-1961). Both verified against MoMA's own artist database.
- **Edward Steichen as plate photographer**: first appearance at #264 (photo-0253, Section 23 Food, PR #53); second self-inclusion at #490 (photo-0475, Section 42 Childhood Magic, PR #79). Both occurrences are documented neutrally.
- **The Master Checklist records no titles and no dates for individual plates.** Steichen deprived the images of titles. Photo-0488 is the unique exception — its title and year come from `src-moma-archives-highlights-1955`, a separate Tier-1 source, in a multi-source citation.
- **National attribution preserved verbatim** from the checklist — Capa "American," Erwitt "American," Horvat "Italian." Re-framing is a separate editorial decision, never a silent correction.
- **Pre-existing-defect findings** from PRs #58, #71, #73, #75, #77, #79 documented inline for issue #61 family follow-up: unhedged biographical lines on photo-0068/0105 (Eisenstaedt), photo-0092 (Vishniac), photo-0124 (Duncan), photo-0146 (Sander), photo-0152/0337/0366 (Bourke-White), photo-0171 (Mili), photo-0173 (Morgan); photo-0280 "first Brackman Associates" miscount.

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

These are concrete intended next dispatches.

- ~~**Issue #61 family cleanup**~~ ✓ closed via PR #103 (2026-05-01).
- ~~**Out-of-range plates #505 #506 seeding**~~ ✓ closed via the present pass — `photo-0489` (#506 William Garnett) and `photo-0490` (#505 Lennart Nilsson).
- ~~**488→503 gap reconciliation audit**~~ ✓ written up at [`research/catalog-reconciliation-503.md`](catalog-reconciliation-503.md).
- **Photographer biographies — issue #104 batches** — anchor or hedge the ~25 unhedged immigrant/expatriate photographer biographicals (Brassai, Capa, Seymour, Erwitt, Arnold, Riwkin, Goro, Vishniac, Bourke-White, Brandt, Mili, Morgan, …). Either (a) source-anchored bios with new `sources/<decade>/<slug>.md` entries, (b) hedge sweep using the PR #103 template, or a hybrid prioritising the highest-profile names.
- **1960s bibliography batch** (issue #86) — thinnest decade at 15 sources. Prime targets: The Bitter Years 1962 archive, Sandburg 1967 death, *Aperture* 1962 (Steichen 80th birthday), USIA tour wind-down records, *Popular Photography* 1962 retrospective.

### Backlog (planned, not yet scheduled)

Known work, intent established, sequence not yet pinned.

- **Photographer biographies batches 2–12** — sequential after access-barrier resolution. Batch 1 (PR #8, 20 photographers) remains the only batch; ~253 photographers still need rows.
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
| [#54](https://github.com/danlex/thefamilyofman/issues/54) | Bump mindmap + progress.yml | `CLOSED` via PR #55 | First mindmap bump; absorbed PRs #43-#53. |
| [#56](https://github.com/danlex/thefamilyofman/issues/56) | Add Roadmap section to mindmap | `CLOSED` via PR #57 | Forward-looking tracking layer + status glyphs in Overview tree + Photographers branch. |
| [#58](https://github.com/danlex/thefamilyofman/issues/58) | Catalog batch #277–301 | `CLOSED` via PR #60 | +24 rows (Section 25 final + Section 26 begin). |
| [#59](https://github.com/danlex/thefamilyofman/issues/59) | Tour map visualisation | `CLOSED` via PR #62 | Leaflet map of 14 verified venues, three colour-coded waves. |
| [#61](https://github.com/danlex/thefamilyofman/issues/61) | Pre-existing biographical hedges | `CLOSED` via PR #63 | 3 Wayne Miller + 2 Eisenstaedt + 1 Eugene Harris stale-count rows hedged. |
| [#64](https://github.com/danlex/thefamilyofman/issues/64) | Catalog batch #302–326 | `CLOSED` via PR #65 | +24 rows; Section 25 Relationships continuation. |
| [#66](https://github.com/danlex/thefamilyofman/issues/66) | Catalog batch #327–351 | `CLOSED` via PR #67 | +24 rows; Sections 26 LEARNING + 27 DEATH begin; gaps at #337 + #346. |
| [#68](https://github.com/danlex/thefamilyofman/issues/68) | Catalog batch #352–376 | `CLOSED` via PR #69 | +23 rows; Sections 28 RELIGIOUS EXPRESSION + 29 ALONENESS begin; first schema-gap (no direct cluster for Section 28/29); gap at #362. |
| [#70](https://github.com/danlex/thefamilyofman/issues/70) | Catalog batch #377–401 | `CLOSED` via PR #71 | +24 rows; Sections 30/31/32/33 begin; gap at #399; sec-hardship-suffering-war first used. |
| [#72](https://github.com/danlex/thefamilyofman/issues/72) | Catalog batch #402–426 | `CLOSED` via PR #73 | +25 rows; Sections 34/35 begin; gap at #425; #404A letter-suffix; out-of-order #422. |
| [#74](https://github.com/danlex/thefamilyofman/issues/74) | Catalog batch #427–451 | `CLOSED` via PR #75 | +25 rows; Sections 36/37/38/39 begin; entire Section 38 block printed out-of-order; Joan Miller (#449) distinct from Wayne Miller. |
| [#76](https://github.com/danlex/thefamilyofman/issues/76) | Catalog batch #452–476 | `CLOSED` via PR #77 | +25 rows; **STRUCTURAL MILESTONE: H-bomb plate at photo-0441 (#456)**; Sections 40/41/42 begin. |
| [#78](https://github.com/danlex/thefamilyofman/issues/78) | Catalog batch #477–503 (final) | `CLOSED` via PR #79 | +27 rows; **STRUCTURAL MILESTONE: A Walk to Paradise Garden at photo-0488 (#503)** — closing image; FINAL CORPUS STATE. |
| [#80](https://github.com/danlex/thefamilyofman/issues/80) | Bump mindmap (final-corpus state) | `OPEN` | This PR. |

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
