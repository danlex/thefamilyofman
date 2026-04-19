---
title: Research mindmap
last_updated: 2026-04-19
---

> **Note.** This document was last bumped on 2026-04-19. Catalog: **192 rows** seeded (PRs #4 + #7 + #11). Photographers: 20 rows + 4 short bios + 20 source entries seeded (PR #8). Live on the site. An unresolved bottleneck: obituary and museum-page citations in PR #8 carry `verified: false` flags because WebFetch was denied by MoMA / Magnum / ICP / NYT — issue #9 tracks the re-verification.

# Research mindmap

A living map of **what we know** (with sources) and **what we need to investigate** (gaps). Update this file after every merged research PR and whenever a new gap is identified.

## Overview

<pre class="tree">
<span class="tree-root">The Family of Man</span>
│
├─ <b>1955 Exhibition</b>
│  ├─ Museum of Modern Art, New York
│  ├─ Edward Steichen &mdash; curator
│  ├─ Paul Rudolph &mdash; installation design
│  ├─ Carl Sandburg &mdash; prologue
│  └─ Opened 24 January 1955
│
├─ <b>Catalog</b>
│  ├─ 503 photographs
│  ├─ 273 photographers
│  ├─ 68 countries of origin
│  └─ Selected from a large submission pool
│     <i>(commonly cited as &ldquo;2 million&rdquo;; primary source not yet verified)</i>
│
├─ <b>World Tour 1955&ndash;1962</b>
│  ├─ USIA sponsored
│  ├─ ~91 venues
│  ├─ 37 countries
│  ├─ ~9 million visitors
│  └─ Moscow 1959 &mdash; Sokolniki Park
│
├─ <b>Clervaux, Luxembourg</b>
│  ├─ Steichen&rsquo;s gift to his country of birth
│  ├─ CNA &mdash; Centre national de l&rsquo;audiovisuel
│  ├─ Permanent installation since 1994
│  └─ Restoration 2010&ndash;2013
│
├─ <b>UNESCO 2003</b>
│  └─ Memory of the World register
│
├─ <b>Thematic clusters</b> <i>(working reconstruction &mdash; see <a href="{{ '/sections/' | relative_url }}">/sections/</a>)</i>
│  ├─ Prologue
│  ├─ Lovers
│  ├─ Marriage &amp; birth
│  ├─ Family &amp; children
│  ├─ Play &amp; learning
│  ├─ Work
│  ├─ Eating &amp; everyday
│  ├─ Relationships
│  ├─ Hardship &amp; war
│  ├─ Death
│  └─ Rededication
│
└─ <b>Critical reception</b>
   ├─ Barthes 1957 &mdash; <i>The Great Family of Man</i>
   ├─ Sontag 1977 &mdash; <i>On Photography</i>
   ├─ Sekula 1981 &mdash; <i>The Traffic in Photographs</i>
   ├─ Sandeen 1995 &mdash; <i>Picturing an Exhibition</i>
   ├─ Stimson 2006 &mdash; <i>The Pivot of the World</i>
   └─ Turner 2013 &mdash; <i>The Democratic Surround</i>
</pre>

---

## What we know (with sources)

### Exhibition — 1955 MoMA
- **Opened 24 January 1955** at the Museum of Modern Art, New York. *Source: MoMA exhibition record #2429.*
- **Curator: Edward Steichen**, then Director of MoMA's Department of Photography.
- **Installation design: Paul Rudolph** (architect). *Source: MoMA Archives / archive-highlights page.*
- **Prologue: Carl Sandburg** (Steichen's brother-in-law), distributed as a leaflet at the entrance.
- **Scale: 503 photographs by 273 photographers from 68 countries.** *Citation status: not yet verified to pagination of the 1955 catalog in this repo; MoMA's public 2429 record is currently unreachable from our fetcher (confirmation needed before cite).*
- **Selection process** — figure of "~2 million submissions" is commonly cited but **not yet verified**; Wikipedia's published figure of ~4 million refers to the *book* submission pool rather than the exhibition. Do not use either figure without a primary-source citation (1955 catalog or Steichen's writings).
- **Entrance arch / crowd imagery opens the show.** *Source: MoMA archive-highlights page.*
- **Closing image: W. Eugene Smith, *A Walk to Paradise Garden* (1946).** *Source: MoMA archive-highlights page.*

### Thematic structure *(merged via PR #3)*
- The 1955 catalog does **not** present a canonical numbered list of sections. Scholarly reconstructions differ: UNESCO Memory of the World register gives "32 themes" (confirmed). A "37 themes" figure is reported on CNA Luxembourg's education portal but is **not yet independently verified** in this repo (CNA site was unreachable during the 2026-04-19 audit).
- **Our working reconstruction: 11 thematic clusters** (`sec-prologue` through `sec-rededication-future`) are live on the site under [/sections/](https://danlex.github.io/thefamilyofman/sections/). Each row in `data/sections.csv` is tagged "thematic cluster reconstructed" to avoid implying canonical status.
- **Governance note:** PR #3 was merged before the four-judge panel ran. The content should be re-audited — especially Judge-Grounding on the Barthes verbatim quotes and Judge-Bias on the theme-count treatment.

### Catalog — first rows seeded (PR #4 open)
- **New anchor source identified: MoMA Master Checklist for Exhibition #569** (`src-moma-exh-0569-master-checklist`, Tier 1). This 26-page internal checklist from MoMA Exhibitions is what PR #4 uses for every row — it gives per-plate photographer, agency/publication, nationality, "where taken," and print dimensions verbatim.
- **Plate numbers skipped by the primary source so far:** #5, #7, #8 (Prologue); #61 (Mothers and Babies); #88, #90 (Family Activities); #145, #149 (Work A). Reasons not stated in the document. Each skip is noted in the adjacent row's `notes`.
- **Out-of-order plates encountered in #101–200 range:** #115 opens Section 14 Land rather than closing Section 13; #168 appears mid-Section 14 between #141 and Section 15; #194 appears inside Section 19 Classical Music. Three-digit plates #505 and #506 also appear inside sections 14–15 (out of the 101–200 range) — deferred.
- **Through plate #200 the checklist contains 192 photographs.** Our row ids `photo-0001`…`photo-0192` are sequential (we do not echo the skipped numbers).
- **Joint-credit plates seeded:** #107 "Diane and Allan Arbus" (`photo-0101`); #173 "Fritz Goro with Robert Campbell" (`photo-0165`). Preserved as printed.
- **The MoMA Master Checklist records no titles and no dates for individual plates.** Steichen deprived the images of titles (per CNA education portal). Plate years are absent from the primary source. Any year or title we add to a photograph row must be backed by a separate Tier-1/2 citation — secondary identifications (e.g., Bullock's *Let There Be Light* = plate 2) are preserved only in `notes` with a "reported, not primary-verified" caveat.
- **The 7 subsections of the checklist** (Prologue, Lovers, Marriage, Pregnancy, Childbirth, Nursing Mothers, Births) map into 4 of our 11 thematic clusters (`sec-prologue`, `sec-lovers`, `sec-marriage-birth`, `sec-family-children`). Per-row mapping is documented in the CSV `notes` column.
- **National attribution is preserved verbatim** from the checklist — Capa is listed "American," Erwitt "American," Horvat "Italian," even where later scholarly convention differs. Any re-framing is a separate editorial decision, not a silent correction.

### Photographers — batch 1 seeded (PR #8)
- **20 photographer rows** covering every unique individual named in the first 47 catalog plates. 4 short bios exist (Capa, Wayne Miller, Doisneau, DeCarava) — the remaining 16 are CSV rows only.
- **Checklist nationality was preserved verbatim** — Capa "American," Horvat "Italian," Kessel "American" — with scholarly alternatives recorded in `notes`.
- **20 new source entries were added** (NYT obituaries, a *Le Monde* obituary, Magnum Photos, ICP, CCP, Moderna Museet, Fotostiftung Schweiz). These are **Tier 3** and were added by author/publication/year because WebFetch to the institutional sites returned 403 during the seed session. Every citation carries a "verification flag for judges" note — Judge-Grounding re-verification is an open task (see issue #9 below).
- **Gender is blank on all 20 rows** per the project's tagging policy.

### World tour 1955–1962
- **Sponsor: United States Information Agency (USIA).** Records held at National Archives, RG 306.
- **Commonly cited figures: ~91 venues, ~37 countries, ~9M visitors.** *Citation status: widely repeated but not yet verified to Tier-1 primary records in this repo.*
- **Notable stop: Moscow 1959 (Sokolniki Park, American National Exhibition).** *Citation status: attested, not yet formally sourced in this repo.*

### Clervaux (Luxembourg)
- **Permanent installation since 1994** at Clervaux Castle.
- **Custodian: Centre national de l'audiovisuel (CNA).** *Source: steichencollections.lu; cna.public.lu.*
- **Restoration campaign: 2010–2013.** *Citation status: reported by CNA, not yet formally sourced in this repo.*
- **Inscribed on UNESCO Memory of the World: 2003.** *Source: UNESCO register.*

### Critical reception — major landmarks
- **Roland Barthes, "The Great Family of Man"** (in *Mythologies*, 1957). Foundational critique: universalist humanism flattens history and politics. *Verbatim text extracted from a university-hosted PDF via PR #3.*
- **Susan Sontag, *On Photography*** (1977). Related sentimentalism critique.
- **Allan Sekula, "The Traffic in Photographs"** — Marxist ideological reading. *Citation status: widely attributed to* Art Journal *1981, but volume/issue/pages are not yet verified in this repo.*
- **Eric Sandeen, *Picturing an Exhibition: The Family of Man and 1950s America*** (U. New Mexico Press, 1995). Standard historical study; complicates both defense and critique.
- **Blake Stimson, *The Pivot of the World*** (MIT Press, 2006). Re-reads the show within post-war photographic modernism.
- **Fred Turner, *The Democratic Surround*** (U. Chicago Press, 2013). Liberal-democratic design culture.

---

## What we need to investigate (prioritized gaps)

### P0 — foundational (blocks everything else)
- **Catalog — plates 201–end** (after PR #11 the first 192 rows are seeded). Continue with the remainder of the MoMA Master Checklist #569; also record the out-of-range three-digit plates (#505, #506) that appeared early inside sections 14–15.
- **Plate titles and dates** — the Master Checklist has neither. We need the *printed 1955 catalog* (the book) or Steichen's curatorial correspondence to attach titles and years to plates. Expected primary source: the Luxembourg National Library or a Google Books preview of the catalog; the Internet Archive scans were access-restricted.
- **Verbatim Sandburg prologue text with page numbers.** Same blocker as above — access to a scan of the 1955 catalog.
- **Canonical source for exhibition-level figures** (503, 273, 68, ~2M submissions) traced to specific pages of the 1955 catalog, not MoMA's summary pages.

### P1 — core (phase 2)
- **273 photographer biographies.** Each needs dates, nationality, and a Tier-1/2 source for inclusion.
- **1955 installation specifics** — photograph sizes, layout, visitor flow. Paul Rudolph's drawings at MoMA Archives.
- **Opening reception** — contemporary reviews in *New York Times*, *Art News*, *Aperture*, 1955–56. Attendance figures for the MoMA run.
- **World tour venue-by-venue list** — venues, host institutions, dates, attendance. Primary source: USIA records, National Archives RG 306.
- **Moscow 1959** — confirm dates, location (Sokolniki), visitor figures, press reception.
- **Luxembourg provenance chain** — Steichen's deed of gift (date and terms), storage before 1994, exact 1994 opening details.
- **2010–13 restoration** — lead conservator(s), techniques, scope, funding source.
- **UNESCO nomination file (2003)** — text of the inscription and justification.
- **Critical reception in non-English scholarship** — French and German writing, especially from Clervaux-era CNA.

### P2 — enrichment (phase 3)
- **Per-photograph provenance** for each of the 503 — one article per photograph.
- **Photographer compensation and consent** arrangements.
- **Selection process** — how 2M submissions were cut to 503 (Wayne Miller's role as Steichen's assistant).
- **Exhibition funding and sponsorship** in 1955.
- **Current CNA curatorial practice** — rotation schedule, loans, ongoing conservation.
- **Anniversary events** — 50th (2005), 60th (2015), 70th (2025).

### Language gaps
- **Francophone scholarship** (CNA publications, *Revue des musées de France*, French press 1994–present).
- **Germanophone scholarship** (1994 Clervaux opening press in *Luxemburger Wort*, *Tageblatt*; German reviews).
- **Luxembourgish-language coverage** of Clervaux.

### Methodological gaps
- **Theme-count reconciliation** — UNESCO says 32, CNA says 37, our reconstruction proposes 11. Need a source-by-source treatment.
- **Attribution practice** — where our row cites multiple sources with semicolons, confirm CSV-reader compatibility with all tools (not just `validate_schema.py`).
- **WebFetch access to institutional archives** — MoMA (`moma.org`), Magnum (`magnumphotos.com`), ICP (`icp.org`), and NYT all returned 403 to our automated fetcher during the PR #8 session. Source entries added in that PR carry *unverified* permalinks. Options to unblock: (a) a live audit pass with a human-operated browser, (b) a cross-mirror reader (archive.org snapshot or `archive.today`), (c) a `gh api` or academic-library proxy path. Until this is resolved, avoid adding more photographer-bio batches that depend on web-fetched institutional pages.

---

## Active investigations

| # | Title | State | Agent | Notes |
|---|---|---|---|---|
| [#1](https://github.com/danlex/thefamilyofman/issues/1) | Catalog plates 1–50 | `CLOSED` via PR #4 | catalog-builder | 47 rows merged; MoMA Master Checklist #569 added as Tier-1 anchor. Judge panel not run. |
| [#2](https://github.com/danlex/thefamilyofman/issues/2) | Thematic sections + prologue | `CLOSED` via PR #3 | sections-cartographer | Merged without judge review — re-audit pending. |
| [#5](https://github.com/danlex/thefamilyofman/issues/5) | Catalog plates 48–100 | `CLOSED` via PR #7 | catalog-builder | 47 further rows merged (plate numbers 51–100, checklist-skipped #61, #88, #90). |
| [#6](https://github.com/danlex/thefamilyofman/issues/6) | Photographer bios batch 1 | `CLOSED` via PR #8 | photographer-biographer | 20 rows + 4 bios + 20 source entries merged. Obit/museum citations carry "not re-verified" flags — follow-up below. |
| [#9](https://github.com/danlex/thefamilyofman/issues/9) | Re-verify PR #8 citations | `needs-agent` | sources-librarian | Re-fetch the 20 source files via live + archive.org; mark `verified: true/false`. Blocks more photographer batches. |
| [#10](https://github.com/danlex/thefamilyofman/issues/10) | Catalog plates 101–200 | `CLOSED` via PR #11 | catalog-builder | 98 rows merged (`photo-0095`…`photo-0192`); skipped #145, #149; out-of-order #115, #168, #194. |

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
