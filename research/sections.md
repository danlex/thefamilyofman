---
title: "The thematic sections of The Family of Man"
perspective: [curatorial, critical]
contested: true
source_ids: [src-moma-1955-catalog, src-moma-1955-press-release-book, src-moma-exh-2429, src-moma-archives-highlights-1955, src-cna-education, src-unesco-mow-2003, src-barthes-1957, src-sandeen-1995]
last_updated: 2026-04-19
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

## Known gaps (open tasks)

- **Exact verbatim Sandburg excerpts per section** are not populated in `data/sections.csv`. The 1955 catalog's interior text was not accessible via the two Internet Archive scans we checked on 2026-04-19 (`https://archive.org/details/familyofman00stei` and `https://archive.org/details/familyofmangreat00stei` both showed as access-restricted). Per the brief, paraphrase is not quotation; the `sandburg_prologue_excerpt` column is therefore deliberately blank until a physical or unrestricted digital copy can be consulted.
- **Page numbers in Sandeen 1995 and in the 1955 catalog** for specific claims are deferred; `src-sandeen-1995` and `src-moma-1955-catalog` both document this in their Notes.
- **Canonical theme count** (32 vs. 37) is an unresolved discrepancy between two Tier-1 institutional sources. Our 11-row clustering is conservative and re-openable.
- **Per-section `photo_ids`** are blank pending the catalog-builder work on issue #1.
