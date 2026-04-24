# Credibility rubric

Every claim in this repository must cite ≥1 credible source. Every training example must cite ≥1 Tier-1 or Tier-2 source. Judge-Credibility rejects PRs that violate this rule.

## Tiers

### Tier 1 — primary / archival
Original, authoritative, or institutional records.
- **MoMA archives** (moma.org, MoMA Library, MoMA Exhibition History Archive)
- **CNA Luxembourg** (Centre national de l'audiovisuel — steichencollections.lu, cna.public.lu)
- **UNESCO Memory of the World** register and nomination files
- **The 1955 exhibition catalog** (*The Family of Man*, MoMA, 1955) and its subsequent authorized editions
- **Steichen's own writings** — *A Life in Photography* (1963), correspondence, interviews of record
- **Carl Sandburg's prologue** to the 1955 catalog (primary text)
- **Archival photographs** with documented museum provenance (MoMA, CNA, USIA, Library of Congress, Eastman Museum)
- **USIA records** (National Archives, RG 306) for the world tour

### Tier 2 — peer-reviewed / academic press
Scholarly work by recognized authorities.
- **University presses**: Eric Sandeen, *Picturing an Exhibition: The Family of Man and 1950s America* (University of New Mexico Press, 1995); Blake Stimson, *The Pivot of the World* (MIT Press, 2006); Fred Turner, *The Democratic Surround* (University of Chicago Press, 2013)
- **Peer-reviewed journals**: *History of Photography*, *October*, *Art Bulletin*, *Aperture* (editorial content), *Afterimage*
- **Critical theory of record**: Roland Barthes, "The Great Family of Man," *Mythologies* (1957); Susan Sontag, *On Photography* (1977); Allan Sekula's essays on photographic meaning
- **Exhibition catalogs** from major research museums with named curatorial authors

### Tier 3 — reputable museums / press
Secondary sources from institutions with editorial standards.
- **Major museums**: Met, Tate, National Gallery, Eastman Museum, ICP — publications with named authors
- **Newspapers of record** with named authors: *New York Times*, *The Guardian*, *Le Monde*, *Luxemburger Wort*, *Tageblatt*
- **Established photography magazines** (reportage, not blog posts): *LensCulture*, *1000 Words* editorial pieces with named editors
- **Encyclopedia entries** with named authors and visible references (*Grove Art*, *Encyclopedia Britannica*)

### Rejected
- Personal blogs, Medium posts, Substack (unless the author is a Tier-2 authority and the post links to their primary work)
- Pinterest, Tumblr, Instagram captions, Twitter/X posts
- Social media as primary evidence
- Unverified Wikipedia claims — Wikipedia is allowed **only** as a pointer to cited primary/secondary sources; the actual citation in our repo is to those primary/secondary sources, not to Wikipedia
- AI-generated content presented as primary research
- Forums, Q&A sites (Quora, Reddit)
- Auction-house blurbs (unless they cite primary provenance documents — then cite those)

## Required citation fields

Every entry in `sources/` carries YAML frontmatter with:

```yaml
---
id: src-<slug>                    # stable, kebab-case
title: "…"
author: "…"                       # or "authors: […]" for multiple
year: 1955
type: book | article | catalog | archive | website | interview | film
publisher: "…"                    # press / journal / institution
url: "https://…"                  # permalink where possible
accessed: 2026-04-19              # ISO date
tier: 1 | 2 | 3
language: en | fr | de | lb | …
tags: [exhibition, reception, clervaux, …]
---
```

Body of the file: bibliographic citation in plain text + optional notes on relevance / key quotes / page ranges.

## Language coverage

CNA Luxembourg and European scholarship on Clervaux are often in **French** or **German**. Exclude these only at our peril — the Luxembourg chapter of the story is largely francophone. The workflow accepts sources in `en`, `fr`, `de`, `lb`. Translations of quotes must be cited with the translator named.

## URL stability

Prefer:
- DOIs where available
- Stable museum permalinks (moma.org/collection/works/…)
- JSTOR stable URLs
- archive.org snapshots for anything volatile

`scripts/check_credibility.py` verifies link health periodically and flags link rot.

## When no source exists

If a factual claim cannot be sourced to a Tier-1/2/3 reference, the claim does not enter the repo. Speculation and inference are labeled as such and placed in a dedicated `## Open questions` section of the relevant research file — never mixed with sourced statements.

## Anti-confabulation policy (museum-grade accuracy)

**Credibility says what sources are allowed. Anti-confabulation says what you are allowed to claim about sources.**

Never write, in any committed file, that a specific source (URL, book, archive, author, publication, institution) corroborates a fact unless that source was actually fetched / read / opened in the current working session.

If you want to mention a source you did not consult, use explicit non-consultation language:
- "NOT consulted in this round"
- "not re-fetched"
- "claim carried from the pre-existing citation"
- "cited in secondary literature but not accessed here"

Never use corroboration-implying language about unfetched sources:
- ❌ "also recorded on [site.com]"
- ❌ "well-attested in [archive]"
- ❌ "corroborated by [scholar year]"
- ❌ "the [institution] collection confirms"

See `CLAUDE.md` § *Museum-grade accuracy* for the full protocol and the `tvl-tech-bias-validator` pre-delivery audit gate. A real audit (2026-04-24, issue #9) caught a committed note citing the MoMA press release and Master Checklist as attesting Wayne Miller's curatorial-assistant role on *The Family of Man* — neither document actually supported the claim; the citation was false; the validator blocked it before the PR reached the museum.
