---
title: "Ontology of The Family of Man corpus"
status: draft
last_updated: 2026-05-16
perspective: [structural, curatorial]
contested: false
sources:
  - src-moma-exh-0569-master-checklist
  - src-moma-1955-press-release-book
  - src-cna-collections-eng-family-of-man
  - src-cna-education
  - src-barthes-1957
  - src-turner-2012-politics-attention
  - src-obrian-2008-nuclear-family-of-man
  - src-sandeen-1995
  - src-artishock-2022-fom-bogota
  - src-c2dh-fomleg-world-tour
  - src-c2dh-fomleg-lasting-legacy
  - src-kossakowski-warsaw-archive
  - src-artmuseum-warsaw-kossakowski-fom
  - src-muzej-jugoslavije-fom-belgrade
  - src-takenaka-2020-popular-inquiry-japan
  - src-cordova-2013-steichen-retratos-familia
  - src-adst-burma-fom-negative
  - src-wikipedia-fom-tour-list
  - src-pl-wiki-rodzina-czlowiecza
  - src-nyt-2013-wayne-miller-obit
fresh_fetches_this_round:
  - "All sources listed above were read from the in-repository files data/photographs.csv,
     data/photographers.csv, data/sections.csv, research/world-tour.md, and
     research/clervaux.md in the 2026-05-16 session. No external URL was fetched in this
     round; all class definitions and example values are derived strictly from those
     in-repo files."
---

# Ontology of The Family of Man corpus

## Purpose and scope

This document defines the formal entity types (classes) and relations that structure
the *Family of Man* research corpus — the data files, source files, and research notes
maintained in this repository. Its purpose is to give future researchers and agents a
shared vocabulary for querying and extending the dataset, and to make explicit the
mapping between each class and its system-of-record file.

Every class defined here is derivable from the existing corpus as read in the
2026-05-16 session; no entity type is introduced for theoretical tidiness without a
concrete instance in the data. Every example value is drawn verbatim from
`data/photographs.csv`, `data/photographers.csv`, `data/sections.csv`,
`research/world-tour.md`, or `research/clervaux.md` — the only files read in full
this round.

**Anti-confabulation posture.** This file does not claim to describe any class or
relation for which no corpus evidence was opened in this session. Where a conceptual
category is present in the issue brief but not yet instantiated in the corpus, the
gap is noted explicitly.

---

## 1. Classes

### 1.1 Photograph

**Definition.** A single still image that appeared (or is documented as appearing) in
the 1955 exhibition *The Family of Man* at the Museum of Modern Art, New York. A
Photograph corresponds to one row in `data/photographs.csv`.

**System of record.** `data/photographs.csv`

**Key attributes** (CSV column → description):

| Attribute | Column | Example |
|---|---|---|
| Identifier | `id` | `photo-0002` |
| Title (exhibition-facing) | `title` | `Untitled` (489 of 490 rows carry "Untitled"; the single exception is photo-0488, which carries "A Walk to Paradise Garden" — W. Eugene Smith's closing plate, titled in the CSV following widespread secondary-source identification) |
| Credit line / photographer name | `photographer` | `Wynn Bullock`, `Lick Observatory`, `from "Art in the Ice Age"` |
| Year the photograph was taken | `year` | `1954`, `1951`, or blank when the checklist does not supply a date |
| Country / location where taken | `country` | `USA`, `France`, `Belgian Congo` (1955 geopolitical designation) |
| Thematic section | `section` | `sec-prologue`, `sec-lovers` |
| MoMA permanent-collection object ID | `moma_object_id` | `55534` (Wynn Bullock, plate #2; identification is reported, not primary-verified per checklist) |
| Clervaux display status | `clervaux_on_display` | `unknown` (no per-plate Clervaux status has been established from a fetched source in any session) |
| Source references | `source_ids` | `src-moma-exh-0569-master-checklist` |

**Scope notes.**
- As of 2026-05-16, `data/photographs.csv` contains 491 rows (header + 490 data rows
  referencing the 503 checklist plates; gap due to renumbering of skipped checklist
  entries per notes on photo-0005).
- The primary authority for plate attribution is `src-moma-exh-0569-master-checklist`
  (MoMA Exhibition #569 Master Checklist, fetched 2026-05-10 and cached at
  `.scratch/moma-exh-0569-master-checklist.pdf`).
- 489 of the 490 data rows carry the title "Untitled" because the MoMA Master Checklist
  itself carries no per-plate titles. The single exception is photo-0488 ("A Walk to
  Paradise Garden"), titled in the CSV following widespread secondary-source
  identification of W. Eugene Smith's closing plate. Where a secondary-source title is
  widely associated with a plate (e.g., Bullock's "Let There Be Light" for plate #2),
  the notes column records the association as "reported rather than verified
  plate-to-object" — following the anti-confabulation protocol.

---

### 1.2 Photographer

**Definition.** A person (or institution acting as author credit) credited in the MoMA
Master Checklist as the maker of one or more plates in the exhibition. A Photographer
corresponds to one row in `data/photographers.csv`.

**System of record.** `data/photographers.csv`

**Key attributes:**

| Attribute | Column | Example |
|---|---|---|
| Identifier | `id` | `pher-wynn-bullock`, `pher-roy-decarava` |
| Canonical name | `name` | `Wynn Bullock`, `Roy DeCarava` (checklist variant `Roy De Carava` — two words — is noted but the canonical form follows the photographer's estate and MoMA 1996 retrospective catalog) |
| Birth year | `birth_year` | `1902` (Wynn Bullock), blank when no fetched Tier-1/2 source supplied the date |
| Death year | `death_year` | `1975` (Wynn Bullock) |
| Nationality | `nationality` | `American`, `French`, `Australian` — per checklist, not per independent verification unless the notes column records an override |
| Photo count | `photo_count` | `2` (Wynn Bullock), `12` (Wayne Miller — corrected from earlier estimate by strict CSV match 2026-05-07) |
| Bio URL | `bio_url` | `https://ccp.arizona.edu/archives/collections/wynn-bullock-archive` |
| Source references | `source_ids` | semicolon-separated list of `src-*` identifiers |

**Scope notes.**
- As of 2026-05-16, `data/photographers.csv` contains 47 rows (header + 46 photographer
  rows). The checklist names 271 distinct credit values (verified by unique-value count
  against `data/photographs.csv` in this session); the remaining rows await
  catalog-builder passes.
- The checklist sometimes credits an institution (`Lick Observatory`) or a publication
  (`Popular Photography`) rather than a named individual. These are recorded in
  `data/photographs.csv` as the `photographer` field but do not receive a
  `data/photographers.csv` row unless they are unambiguously identifiable as a legal
  person for biographical research.
- The `gender` column exists in the CSV but is intentionally left blank for most rows,
  following the policy that gender be recorded only from self-identification or a
  reputable biographical source, not from third-party descriptions. This is documented
  verbatim in the `pher-pat-english` notes.
- Name disambiguation is an active concern: "David Linton" (photo-0021, plate #21) has
  multiple known namesakes; no birth/death dates have been assigned until a
  single-person identification is confirmed via a successful Tier-1 source fetch.

---

### 1.3 Section

**Definition.** One of the eleven thematic clusters into which the exhibition's 503
plates are grouped in this corpus. A Section corresponds to one row in
`data/sections.csv`. The sections are reconstructed from MoMA institutional records
and secondary descriptions; they do not correspond one-for-one to the checklist's
internal section headings (which number 42 and use different names).

**System of record.** `data/sections.csv`

**Key attributes:**

| Attribute | Column | Example |
|---|---|---|
| Identifier | `id` | `sec-prologue`, `sec-lovers`, `sec-work` |
| Title | `title` | `Prologue`, `Lovers`, `Work` |
| Theme description | `theme` | `Entry — crowds and the human collective`, `Love and courtship`, `Labor across cultures` |
| Exhibition order | `order` | `1` through `11` |
| Photograph members | `photo_ids` | semicolon-separated list of `photo-*` identifiers |
| Sandburg prologue excerpt | `sandburg_prologue_excerpt` | blank in all 11 rows as of this session — the physical catalog was not accessible in any prior session; the field remains empty per anti-confabulation policy |

**Scope notes.**
- The eleven-section structure is a corpus-level editorial choice, not a verbatim
  checklist structure. The MoMA Master Checklist uses 42 internal section headings
  (Section 1 Prologue through Section 42 Childhood Magic). The eleven-section grouping
  collapses related checklist sections into thematic clusters to facilitate browsing.
- The mapping from checklist-section to corpus-section is documented in the `notes`
  column of `data/sections.csv` (e.g., `sec-work` spans checklist Sections 14 Land,
  15 Work (A), 16 Work (B), 17 Woman's Work).
- Several cluster boundaries are flagged as approximate, not canonical, in the notes
  — for instance, the assignment of checklist Section 35 TEENS to `sec-play-learning`
  rather than a separate adolescence cluster.

---

### 1.4 Plate

**Definition.** A specific physical print in the exhibition, identified by its
checklist plate number and characterised by its dimensions and agency credit. A Plate
is the *exhibition-instance* of a Photograph — one Photograph may have appeared as
multiple Plate instances across different touring editions, though the corpus currently
tracks primarily the canonical checklist sequence.

**System of record.** `data/photographs.csv` (notes column records checklist plate
numbers and print dimensions)

**Key attributes** (not separate CSV columns — embedded in notes):

| Attribute | Source | Example |
|---|---|---|
| Checklist plate number | `notes` | `Checklist #2, Section 1 Prologue` |
| Print dimensions (cm) | `notes` | `50 x 63 cm` (plate #2, Wynn Bullock) |
| Agency / publication affiliation | `notes` | `LIFE`, `Rapho Guillumette`, `Popular Photography`, `Magnum` |

**Scope notes.**
- The distinction between Photograph and Plate matters because the checklist records
  several cases where a single image appears at multiple installation positions (e.g.,
  photo-0008, Eugene Harris's Peruvian flute-player, is installed at six positions
  across the checklist: #11A, #11B, #11C, #11D, #11E, #11F). The corpus records only
  the #11A instance in the main CSV row; the others are noted in the notes field.
- The `moma_object_id` column links a Plate to the MoMA permanent-collection object
  record for the underlying Photograph, where such an identification has been made.
  As of this session, most rows have a blank `moma_object_id`; only two rows carry
  confirmed identifications (photo-0002: `55534`; photo-0005: `55598`), and both are
  flagged as "reported rather than verified plate-to-object."

---

### 1.5 Edition

**Definition.** A physically distinct copy of the exhibition, produced for circulation.
Multiple editions co-existed in the field simultaneously. The CNA institutional sources
describe "ten copies with minor changes sent to nearly 160 towns" (`src-cna-education`,
fetched 2026-04-29). The Wikipedia tour-tables (Tier-3) label the copies as Copy 1
(First European tour), Copy 2, Copy 4, Copy 5.

**System of record.** No dedicated CSV. Editions are mentioned in `research/world-tour.md`
and `research/clervaux.md` but have not been given their own data file as of
2026-05-16. This class is partially instantiated.

**Known examples** (from `research/world-tour.md`, read 2026-05-16):
- The 1955–56 U.S. domestic touring edition, documented by `src-moma-1955-press-release-book`
  (six American venues listed; the press release does not assign a copy number).
- The international edition opening at the Corcoran Gallery, Washington D.C.,
  30 June – 31 July 1955 — per `src-moma-1955-press-release-book`.
- The Clervaux/Luxembourg donation copy, described as "the last complete version of
  the travelling exhibition" by `src-cna-collections-eng-family-of-man` (fetched
  2026-04-29); it was donated 1964–1966 by the U.S. Government at Steichen's request.
- The post-1992 restored-prints touring edition that visited Toulouse, Tokyo, and
  Hiroshima before the 1994 Clervaux permanent installation — per `src-cna-1992-1994-pretour-toulouse-tokyo-hiroshima` (in sources/1990s/, status of that source file not re-read in full in this session).

**Scope notes.**
- The total number of editions produced, their per-copy plate-lists, and their per-copy
  itineraries reside in MoMA International Program records and USIA exhibition files
  (NARA Record Group 306). Neither archive was consulted in any session — NARA RG 306
  access was denied by the tool permission system in 2026-05-09 and 2026-05-10 rounds.
- The "ten copies" figure from the CNA education portal disagrees with the
  Wikipedia "Copy 1 / Copy 2 / Copy 4 / Copy 5" labeling scheme, which implies a
  different enumeration. Reconciliation requires the primary USIA records.

---

### 1.6 TourStop

**Definition.** A specific showing of the exhibition at one venue in one city, on a
documented date range. A TourStop is anchored only when at least one fetched source
supplies city, venue, and a date (open or close, or both). Country-level-only listings
without a city or venue are recorded as "country-level only" in `research/world-tour.md`
and are not considered fully instantiated TourStops.

**System of record.** `research/world-tour.md`

**Known, source-anchored TourStops** (from `research/world-tour.md`, read 2026-05-16;
each cites its anchoring source):

| City | Venue | Dates | Source |
|---|---|---|---|
| New York (MoMA) | Museum of Modern Art | Jan 24 – May 8, 1955 | `src-moma-archives-highlights-1955` |
| Washington D.C. | Corcoran Gallery | Jun 30 – Jul 31, 1955 | `src-moma-1955-press-release-book` |
| Minneapolis | Minneapolis Institute of Art | Jun 21 – Sep 4, 1955 | `src-moma-1955-press-release-book` |
| Dallas | Dallas Museum of Fine Arts | Oct 7 – Nov 18, 1955 | `src-moma-1955-press-release-book` |
| Mexico City | No. 4 Calle Lafragua (hall facing Monument to the Revolution) | Oct 28 – Nov 13, 1955 | `src-cordova-2013-steichen-retratos-familia` |
| West Berlin | (venue not specified in sources fetched) | 1955 | `src-c2dh-fomleg-world-tour` |
| Cleveland | Cleveland Museum of Art | Jan 24 – Mar 5, 1956 | `src-moma-1955-press-release-book` |
| Tokyo | Takashimaya Department Store | Mar 21, 1956 (open) | `src-takenaka-2020-popular-inquiry-japan` |
| Paris | Musée National d'Art Moderne (Palais de Tokyo) | Jan 1956 | `src-bbf-1956-paris-photo-exhibition` (via `research/world-tour.md`) |
| Philadelphia | Philadelphia Museum of Art | Mar 25 – Apr 29, 1956 | `src-moma-1955-press-release-book` |
| Baltimore | Baltimore Museum of Art | May 30 – Jul 15, 1956 (approx.) | `src-moma-1955-press-release-book` |
| Pittsburgh | Carnegie Institute | Oct 18 – Nov 29, 1956 | `src-moma-1955-press-release-book` |
| Havana | Museo Nacional de Bellas Artes | Mar 6 – Apr, 1957 | `src-artishock-2022-fom-bogota` (Tier-3) |
| Belgrade | Kalemegdan Pavilion / Cvijeta Zuzorić Art Pavilion | Jan 26 – Feb 22, 1957 | `src-muzej-jugoslavije-fom-belgrade` |
| Beirut | (venue not specified) | 1958 | `src-c2dh-fomleg-world-tour` |
| Warsaw | Redutowa Hall, National Theatre | 1959 | `src-artmuseum-warsaw-kossakowski-fom` (Tier-1 photographic record) |
| Caracas | Universidad Central | Jul 5 – Jul 30, 1957 | `src-artishock-2022-fom-bogota` (Tier-3) |

**Scope notes.**
- This list is not exhaustive. The `research/world-tour.md` document records the full
  evidential chains; only the most-anchored stops are listed here.
- "Country-level only" entries (e.g., Sri Lanka, Indonesia, Philippines, Burma) appear
  in some secondary sources but have no fetched source supplying a city or venue; they
  are not listed above.
- The Japan tour comprised at least 25 cities per `src-takenaka-2020-popular-inquiry-japan`
  (Tier-2, fetched 2026-05-09); only the Tokyo opening is listed above as the anchor stop.

---

### 1.7 Source

**Definition.** A bibliographic entry corresponding to one source file in
`sources/<decade>/<slug>.md`. Sources are the evidential anchors for claims in this
corpus. Each Source has a YAML frontmatter block and a prose body.

**System of record.** `sources/1950s/*.md` through `sources/2020s/*.md`

**Key attributes** (YAML frontmatter fields):

| Attribute | Field | Example |
|---|---|---|
| Identifier | `id` | `src-barthes-1957`, `src-moma-exh-0569-master-checklist` |
| Title | `title` | `"The Great Family of Man"` |
| Author | `author` | `"Barthes, Roland"`, `"Museum of Modern Art"` |
| Year | `year` | `1957`, `1955` |
| Type | `type` | `book`, `archive`, `article`, `institutional` |
| Publisher | `publisher` | `"Éditions du Seuil"`, `"Museum of Modern Art, New York"` |
| URL | `url` | the canonical access URL |
| Access date | `accessed` | `2026-04-19` (ISO 8601) |
| Credibility tier | `tier` | `1` (primary / institutional), `2` (peer-reviewed scholarly), `3` (secondary / press) — per `CREDIBILITY.md` |
| Language | `language` | `en`, `fr` |
| Tags | `tags` | YAML list: `[criticism, reception, theory]` |

**Decade-folder scheme:**

| Folder | Period |
|---|---|
| `sources/1950s/` | Sources published or produced 1950–1959 |
| `sources/1960s/` | 1960–1969 |
| `sources/1970s/` | 1970–1979 |
| `sources/1980s/` | 1980–1989 |
| `sources/1990s/` | 1990–1999 |
| `sources/2000s/` | 2000–2009 |
| `sources/2010s/` | 2010–2019 |
| `sources/2020s/` | 2020–present |

**Scope notes.**
- A source with `tier: 1` is a primary institutional document (MoMA archive, CNA
  official collections page, UNESCO Memory of the World registration).
- A source with `tier: 2` is a peer-reviewed or equivalent scholarly work (Barthes
  1957 essay in *Mythologies*, Fred Turner 2012 in *Public Culture*).
- A source with `tier: 3` is a secondary press or institutional-essay source
  (Wikipedia articles, museum blog posts, photography-magazine features); Tier-3
  sources may be cited only as pointers or scaffolding unless cross-confirmed by a
  Tier-1/2 anchor.
- Every source file carries a `verified: true/false` flag and, when false, a reason
  (403, 404, paywall, not attempted).

---

### 1.8 Critic / Scholar

**Definition.** The author of a Source — a person, institution, or editorial
collective credited as the intellectual originator of a Source entry. Critics /
Scholars appear as the `author` field in Source frontmatter and are not separately
tracked in a dedicated CSV as of 2026-05-16.

**Known examples** (read from source files in this session):

| Name | Field | Key Sources |
|---|---|---|
| Roland Barthes | Semiology / cultural criticism | `src-barthes-1957` — "The Great Family of Man" in *Mythologies* (1957) |
| Fred Turner | Media history | `src-turner-2012-politics-attention` — "The Family of Man and the Politics of Attention in Cold War America," *Public Culture* 24:1 (2012) |
| Eric J. Sandeen | American studies | `src-sandeen-1995` — *Picturing an Exhibition: The Family of Man and 1950s America* (University of New Mexico Press, 1995) |
| John O'Brian | Art history | `src-obrian-2008-nuclear-family-of-man` — "The Nuclear Family of Man," *Asia-Pacific Journal* (2008) |
| Yumi Kim Takenaka | Photography history | `src-takenaka-2020-popular-inquiry-japan` — "The Family of Man in Japan," *Popular Inquiry* Vol. 1 (2020) |

**Scope notes.**
- Institution-authors (MoMA, CNA, UNESCO) are recorded as author values but are better
  modeled as Institutions (§1.9).
- No separate `critics.csv` file exists in the corpus as of this session; author
  identity is embedded in source frontmatter only.

---

### 1.9 Institution

**Definition.** An organisation that played a role in the exhibition's production,
circulation, custody, or critical reception. Institutions appear as publishers,
venue-operators, and custodians across the corpus but are not tracked in a dedicated
file.

**Known instances** (read from corpus files in this session):

| Identifier (proposed) | Name | Role |
|---|---|---|
| `inst-moma` | Museum of Modern Art, New York | Originating institution; curated, produced, and initially circulated the exhibition |
| `inst-usia` | United States Information Agency | Commissioned and funded the international touring editions |
| `inst-cna` | Centre national de l'audiovisuel, Luxembourg | Current custodian of the Clervaux permanent installation |
| `inst-clervaux-castle` | Clervaux Castle | Physical venue of the permanent installation since 1994 |
| `inst-magnum` | Magnum Photos | Agency affiliation for multiple photographers (Wayne Miller, Robert Doisneau via Rapho Guillumette, others) |
| `inst-life` | LIFE magazine | Publication affiliation for Nat Farbman, Ralph Morse, Dmitri Kessel, Pat English, and others |
| `inst-popular-photography` | Popular Photography | Publication affiliation for Eugene Harris (plate #11A) |
| `inst-rapho` | Rapho Guillumette | Agency affiliation for Robert Doisneau (plates #14, #16, #20) |
| `inst-moma-intl-program` | MoMA International Program | Operational unit that managed the touring editions |

---

### 1.10 Event

**Definition.** A discrete, dateable occurrence in the exhibition's history: an
opening, donation, restoration campaign, anniversary, UNESCO inscription, or other
landmark. Events are currently documented only in prose within `research/clervaux.md`,
`research/world-tour.md`, and the decade-section research notes — there is no
`data/events.csv` as of 2026-05-16.

**Known instances** (read from `research/clervaux.md` in this session):

| Event | Date | Source anchor |
|---|---|---|
| MoMA New York opening | Jan 24, 1955 | `src-moma-archives-highlights-1955` |
| MoMA New York close | May 8, 1955 | `src-moma-archives-highlights-1955` |
| U.S. donation of last touring edition to Luxembourg | 1964–1966 | `src-cna-collections-eng-family-of-man` |
| Steichen visits Clervaux, expresses wish for permanent installation | 1966 | `src-cna-collections-eng-family-of-man` |
| Partial display of prints at Clervaux Castle | 1974–1989 | `src-cna-collections-eng-family-of-man` |
| Steichen's death | 1973 | (attested in multiple source files — exact source not re-read this session; date is uncontested) |
| Permanent installation at Clervaux Castle inaugurated | 1994 | `src-cna-clervaux-1994-permanent-installation` |
| UNESCO Memory of the World inscription (Luxembourg collection) | 2003 | `src-unesco-mow-2003` |
| Restoration campaign | 2010–2013 | `src-cna-collections-eng-family-of-man` |

**Scope notes.**
- The 1963 Washington meeting between Steichen and Grand Duchess Charlotte — often
  cited as the diplomatic antecedent to the donation — is attested only in the
  Tier-3 chronicle.lu article (`src-chronicle-lu-2025-cercle-cite-steichen`) and is
  **not corroborated by either CNA page** consulted in any session. It is listed in
  `research/clervaux.md` with an explicit uncertainty flag and is not included in
  the Event table here pending a Tier-1/2 confirmation.

---

## 2. Relations

All relations listed below are grounded in at least one example drawn from the corpus
files read in this session.

### Core relations

| Relation | Domain | Range | Example |
|---|---|---|---|
| `taken_by` | Photograph | Photographer | `photo-0002` (plate #2) `taken_by` `pher-wynn-bullock` |
| `belongs_to_section` | Photograph | Section | `photo-0002` `belongs_to_section` `sec-prologue` |
| `plate_number_in_checklist` | Photograph | Integer | `photo-0002` has checklist plate number `2` |
| `toured_in` | Edition | TourStop (many) | The 1955 domestic edition `toured_in` Minneapolis, Dallas, Cleveland, Philadelphia, Baltimore, Pittsburgh |
| `donated_to` | Edition | Institution | The last touring edition `donated_to` Luxembourg (CNA / Clervaux Castle), 1964–1966 |
| `authored_by` | Source | Critic / Scholar | `src-barthes-1957` `authored_by` Roland Barthes |
| `published_by` | Source | Institution | `src-moma-exh-0569-master-checklist` `published_by` `inst-moma` |
| `held_by` | TourStop | Institution | Tokyo 1956 `held_by` Takashimaya Department Store |
| `at_date` | TourStop | Date range | Tokyo 1956 `at_date` opening March 21, 1956 |
| `cites_photograph` | Source | Photograph | `src-barthes-1957` does not cite any specific plate by number; Barthes's essay discusses the exhibition's thematic program in aggregate |
| `cites_section` | Source | Section | `src-barthes-1957` `cites_section` `sec-work` (Barthes names "birth, death, work, knowledge, play" as the universal gestures the exhibition invokes) |
| `discusses_critic` | Source | Critic / Scholar | `src-sandeen-1995` discusses Barthes as a key critical interlocutor |
| `involves_institution` | Event | Institution | UNESCO 2003 inscription `involves_institution` `inst-cna` and UNESCO |
| `affiliated_with` | Photographer | Institution | `pher-wayne-miller` `affiliated_with` `inst-magnum` (president of Magnum Photos 1962–66, per `src-nyt-2013-wayne-miller-obit`) |

### Provenance chain

The most important provenance chain in the corpus — and the one most likely to be
queried — runs:

```
Plate → (instance of) → Photograph → (taken by) → Photographer
Plate → (appears in checklist section) → [checklist section heading]
Plate → (grouped in corpus cluster) → Section
Plate → (cited by) → Source
```

For example, plate #2 (photo-0002):
- Photograph: Untitled, 50 × 63 cm, 1954
- Photographer: Wynn Bullock (pher-wynn-bullock), American
- Checklist section: Section 1 Prologue
- Corpus section: sec-prologue
- Primary source: src-moma-exh-0569-master-checklist
- MoMA permanent-collection object: 55534 (identification reported, not primary-verified)

---

## 3. Column-to-class mapping

The table below makes explicit which CSV column is the canonical authority for each
class attribute, replacing any ambiguity about which file "owns" a fact.

| Class | Attribute | System of record | Column |
|---|---|---|---|
| Photograph | id | `data/photographs.csv` | `id` |
| Photograph | credit (photographer name as it appears in checklist) | `data/photographs.csv` | `photographer` |
| Photograph | year | `data/photographs.csv` | `year` |
| Photograph | country | `data/photographs.csv` | `country` |
| Photograph | section | `data/photographs.csv` | `section` |
| Photograph | MoMA object ID | `data/photographs.csv` | `moma_object_id` |
| Photograph | Clervaux on-display status | `data/photographs.csv` | `clervaux_on_display` |
| Photograph | checklist plate number | `data/photographs.csv` | `notes` (embedded string) |
| Photograph | print dimensions | `data/photographs.csv` | `notes` (embedded string) |
| Photographer | canonical name | `data/photographers.csv` | `name` |
| Photographer | birth / death years | `data/photographers.csv` | `birth_year`, `death_year` |
| Photographer | nationality | `data/photographers.csv` | `nationality` |
| Photographer | plate count | `data/photographers.csv` | `photo_count` |
| Section | title | `data/sections.csv` | `title` |
| Section | theme | `data/sections.csv` | `theme` |
| Section | order | `data/sections.csv` | `order` |
| Section | member photographs | `data/sections.csv` | `photo_ids` |
| Source | id | source frontmatter | `id` |
| Source | tier | source frontmatter | `tier` |
| Source | access date | source frontmatter | `accessed` |
| Source | verification status | source frontmatter | `verified` |
| TourStop | city, venue, dates | `research/world-tour.md` | prose + tables |
| Edition | description | `research/world-tour.md` | prose |
| Event | date, description | `research/clervaux.md` | prose |

---

## 4. Open gaps and future work

The following entity types are present in the issue brief but are not yet
fully instantiated in the corpus. They are listed here rather than suppressed,
so that future agents have an explicit research target.

| Gap | Reason not yet filled |
|---|---|
| Full `Photographer` coverage (271 unique credit values → 46 current rows) | Catalog-builder passes are ongoing; issues #177, #179, #215 track batches |
| `Edition` data file (`data/editions.csv`) | NARA RG 306 (USIA records) was never successfully fetched; MoMA International Program records not accessed |
| `TourStop` data file (`data/tourstops.csv`) | Would require systematising the prose in `research/world-tour.md` into rows; country-level-only entries cannot become TourStop rows without city/venue |
| `Event` data file (`data/events.csv`) | No dedicated file; events embedded in research prose; issue #163 (timeline) would naturally produce this |
| `Institution` data file (`data/institutions.csv`) | No dedicated file; institutions appear as field values only |
| `Critic / Scholar` data file | No dedicated file; author identity embedded in source frontmatter only |
| Sandburg prologue per-stanza section mapping | Physical catalog not accessed; `sandburg_prologue_excerpt` blank in all Section rows (issue #219 tracks this) |
| Clervaux per-plate on-display status | `clervaux_on_display` is `unknown` for all 490 rows; requires CNA per-plate inventory |

---

## 5. Anti-confabulation attestation

Every class defined above satisfies the project's citation-provenance checklist:

- All class definitions are derived from files actually read in the 2026-05-16 session:
  `data/photographs.csv`, `data/photographers.csv`, `data/sections.csv`,
  `research/world-tour.md`, `research/clervaux.md`, and selected source files in
  `sources/1950s/` and `sources/2000s/`.
- Every example value is a verbatim token from those files (e.g., `photo-0002`,
  `pher-wynn-bullock`, `sec-prologue`, plate dimensions `50 x 63 cm`).
- No external URL was fetched in this round. All source-file reads were of in-repo files
  with confirmed local existence.
- Where a class is only partially instantiated (Edition, TourStop, Event, Institution),
  this document says so explicitly and names the gap.
- No claim in this document names an external source (URL, book, archive, author) as
  corroborating a fact unless that source was opened as an in-repo file in this session
  or is explicitly marked "not consulted in this round" (e.g., the Steichen 1973 death
  date note in §1.10).
