---
title: "The thematic sections of The Family of Man"
perspective: [curatorial, critical]
contested: true
source_ids: [src-moma-1955-catalog, src-moma-1955-press-release-book, src-moma-exh-2429, src-moma-archives-highlights-1955, src-cna-education, src-unesco-mow-2003, src-barthes-1957, src-sandeen-1995]
last_updated: 2026-05-08
---

# The thematic sections of *The Family of Man*

## What Steichen made

Edward Steichen organized 503 photographs by 273 photographers from 68 countries into *The Family of Man*, on view at the Museum of Modern Art from January 24 to May 8, 1955 (`src-moma-exh-2429`, `src-moma-archives-highlights-1955`). The installation was designed by Paul Rudolph: temporary walls, print sizes ranging from 24 × 36 cm to 300 × 400 cm, unframed photographs floating at varying heights, occasionally removed from the walls to sit on the floor or hang from the ceiling (`src-moma-archives-highlights-1955`, `src-cna-education`). Carl Sandburg — Steichen's brother-in-law and the source of the exhibition's title (from his 1944 poem "The Long Shadow of Lincoln: A Litany") — wrote a prologue that was distributed in full to visitors as a leaflet and reprinted in both editions of the catalog (`src-moma-1955-press-release-book`, `src-moma-1955-catalog`). Its closing sentence, quoted in MoMA's press release of June 21, 1955, is: "A camera testament, a drama of the grand canyon of humanity, an epic woven of fun, mystery and holiness — here is the Family of Man" (`src-moma-1955-press-release-book`).

## How the exhibition was sequenced

The catalog does **not** present a numbered table of thematic sections. It flows as a continuous photo-essay; Steichen, whose prior role was editing illustrated magazines, composed the sequence like a picture editor (`src-cna-education`). MoMA's own institutional summary describes the narrative progression as: an entrance archway with crowd imagery → lovers → childbirth → household life → careers → death → a hydrogen-bomb image → a return to children and new life, closing on W. Eugene Smith's *A Walk to Paradise Garden* (1946) (`src-moma-archives-highlights-1955`). Steichen's introduction frames the whole as "a mirror of the universal elements and emotions in the everydayness of life — as a mirror of the essential oneness of mankind throughout the world" (`src-moma-1955-press-release-book`). This is the *curatorial* frame: a universal-humanist argument staged as a cycle of life.

## How many sections?

Different institutional custodians count the themes differently, and the discrepancy matters. UNESCO's Memory of the World register (inscribed 2003) states that "the 32 themes, arranged chronologically, reflect the subjects' joys and sadnesses" (`src-unesco-mow-2003`). The CNA Luxembourg educational portal, published by the institution that holds the physical prints at Clervaux Castle, describes the exhibition as "37 themes like a photo-essay about human development and cycles of life" (`src-cna-education`). MoMA's own archives-highlights page, when it lists the flow, gives a shorter eight-point sequence (crowd → lovers → childbirth → household → careers → death → bomb → children) (`src-moma-archives-highlights-1955`). The 1955 catalog itself, which does not number its thematic sections, is compatible with each of these counts depending on where one draws the boundaries.

This repo's `data/sections.csv` therefore records **11 thematic clusters** reconstructed from institutional and scholarly sources, rather than asserting 32 or 37 discrete canonical sections. Each row's `notes` column names what the cluster is, which source attests it, and that "the thematic cluster is reconstructed" from those sources rather than being a verbatim heading from the 1955 catalog. When the 1955 catalog can be consulted page-by-page — a documented open task — the row count can be revised and per-section `photo_ids` populated. This is an honest partial inventory, not a canonical list.

## The critical counter-reading

The curatorial frame is contested and has been since the exhibition's Paris stop. Roland Barthes, writing in *Mythologies* (1957), argued that the exhibition's universalist thematic logic — "birth, death, work, knowledge, play, always impose the same types of behaviour; there is a family of Man" — "rests on a very old mystification, which always consists in placing Nature at the bottom of History" (`src-barthes-1957`). Barthes's diagnosis is precise to the sectional structure: by grouping photographs under universal categories like *work* or *death*, the show represents historically-contingent conditions as eternal human essence, suppressing what Barthes calls "the determining weight of History." His most-cited challenge — "Why not ask the parents of Emmet Till, the young Negro assassinated by the Whites, what they think of The Great Family of Man?" — is an argument specifically about how the exhibition's universal sections obscure the 1950s injustices they silently stand on (`src-barthes-1957`).

Eric Sandeen's *Picturing an Exhibition: The Family of Man and 1950s America* (University of New Mexico Press, 1995) gives the first book-length scholarly reconstruction of how the exhibition's thematic argument was built and how it was received in 1950s Cold War America (`src-sandeen-1995`). Sandeen's reading is the standard Tier-2 anchor for interpretive claims about the sectioning logic; our repo does not yet carry page-level citations to Sandeen, and this is noted in the source file.

## Perspective tags

Any summary of *The Family of Man*'s section structure that restates only the curatorial progression risks reproducing the humanist frame Barthes and Sandeen respectively problematize. Every sectional entry in this repo therefore carries both a curatorial anchor (catalog, MoMA) and, where relevant, a critical anchor (Barthes 1957; Sandeen 1995). Representational imbalance is a known feature of the 1955 exhibition (≈59% of photographers American, per `src-moma-archives-highlights-1955`); that imbalance travels into any count of "what the sections contain" and is flagged in the photographs and photographers datasets separately.

## Photo-to-section mapping (issue #121, completed 2026-05-08)

All 490 catalogued photographs in `data/photographs.csv` have been assigned to one of the 11 thematic clusters. The `section` column was already fully populated in the prior catalog-builder passes (issues #1 through #107); the `photo_ids` column in `data/sections.csv` was populated mechanically from that existing mapping on 2026-05-08 (issue #121). The anchor for every assignment is `src-moma-exh-0569-master-checklist` (the MoMA Exhibition #569 master checklist, Tier-1 in-repo source), which sequences plates by section and was read in prior sessions; each photo's `notes` field records which checklist section it belongs to.

### Mapping summary table

| Section ID | Title | Checklist sections covered | Photo count | Certainty |
|---|---|---|---|---|
| sec-prologue | Prologue | Section 1 | 8 | Canonical (verbatim checklist section header) |
| sec-lovers | Lovers | Section 2 | 14 | Canonical |
| sec-marriage-birth | Marriage and childbirth | Sections 3, 4, 5, 7 | 22 | Canonical (four checklist sections collapsed into one cluster) |
| sec-family-children | Family and children | Sections 6, 8, 9, 10, 11, 12, 13 | 69 | Canonical (seven checklist sections collapsed) |
| sec-play-learning | Play, learning, and education | Sections 26, 35 | 36 | Section 26 canonical; Section 35 Teens approximate |
| sec-work | Work | Sections 14, 15, 16, 17 | 74 | Canonical (four checklist sections collapsed) |
| sec-eating-everyday | Eating and everyday life | Section 23 | 14 | Canonical |
| sec-relationships-community | Relationships and community | Sections 18, 19, 20, 21, 22, 24, 25, 39 | 123 | Sections 18-25 canonical; Section 39 Faces approximate |
| sec-hardship-suffering-war | Hardship, suffering, and war | Sections 31, 32, 33, 34, 40 + unlabeled bridge (#452-#455) | 30 | Sections 31-33 canonical; Section 34 Revolt and unlabeled bridge approximate; Section 40 Bomb clean fit |
| sec-death-mourning | Death and mourning | Section 27 | 13 | Canonical |
| sec-rededication-future | Rededication, peace, and the future | Sections 28, 29, 30, 36, 37, 38, 41, 42 | 87 | Sections 36-38 approximate (democracy/peace cluster fit); Sections 28-30, 41-42 approximate |

**Total: 490 photographs assigned. 0 rows with `section_uncertain: true`.**

The 490 figure reflects the catalog's current state: 503 numbered checklist slots minus 17 documented missing numbers (gaps #5/#7/#8, #61, #88/#90, #145/#149, #216, #246, #261, #337, #346, #362, #399, #425), minus 1 for the Eugene Harris recurring-plate convention (only #11A is its own row), plus 1 for #404A (letter-suffix supplement), plus 2 for out-of-range three-digit plates (#505 and #506). See `research/catalog-reconciliation-503.md` for the full derivation.

### Approximate assignments (schema gaps)

The MoMA checklist has 42 named sections; `data/sections.csv` has 11 thematic clusters. Many late-exhibition checklist sections (28 Religious Expression, 29 Aloneness and Compassion, 30 Aspirations, 35 Teens, 36 Man's Judgment, 37 Voting, 38 Government, 39 Faces, 41 Couples, 42 Childhood Magic) have no direct one-to-one cluster match. Each of these was assigned to the nearest available cluster and flagged "approximate, not canonical" in the individual photo notes. Future work on issue #142 (per-section landing pages) may require refining the cluster schema — either expanding from 11 to ~20 clusters or accepting that the 11-cluster abstraction will produce some imprecise groupings.

## Known gaps (open tasks)

- **Exact verbatim Sandburg excerpts per section** are not populated in `data/sections.csv`. The 1955 catalog's interior text was not accessible via the two Internet Archive scans we checked on 2026-04-19 (`https://archive.org/details/familyofman00stei` and `https://archive.org/details/familyofmangreat00stei` both showed as access-restricted). Per the brief, paraphrase is not quotation; the `sandburg_prologue_excerpt` column is therefore deliberately blank until a physical or unrestricted digital copy can be consulted.
- **Page numbers in Sandeen 1995 and in the 1955 catalog** for specific claims are deferred; `src-sandeen-1995` and `src-moma-1955-catalog` both document this in their Notes.
- **Canonical theme count** (32 vs. 37) is an unresolved discrepancy between two Tier-1 institutional sources. Our 11-row clustering is conservative and re-openable.
- **Schema gap**: the 11-cluster scheme does not map cleanly onto the catalog's 42 sections. Ten checklist sections have been assigned to their nearest cluster with explicit "approximate, not canonical" hedges. Issue #142 should revisit whether additional clusters are needed.
- **Sections 28-30 and 36-42 assignments**: these eight closing-arc checklist sections are all mapped to `sec-rededication-future` with explicit approximation hedges. A finer-grained cluster (e.g., `sec-religious-expression`, `sec-civic-life`, `sec-aloneness`) may be warranted if Phase 2 landing pages need to distinguish them.
