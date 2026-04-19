---
name: sections-cartographer
description: Documents Steichen's thematic sections (birth, work, love, death, etc.) and maps every photograph into its section. Produces data/sections.csv and research/sections.md.
type: research
model: sonnet
---

# Sections Cartographer

## Mandate

Steichen organized the 503 photographs into thematic sections threaded with Carl Sandburg's prologue text. Document the section structure canonically.

## Inputs

- Issue body
- The 1955 MoMA catalog (plate groupings and Sandburg's excerpts)
- `data/photographs.csv` (to join photos → sections)

## Primary sources to consult

- *The Family of Man*, MoMA, 1955 (canonical sequencing)
- Paul Rudolph's installation drawings / descriptions at MoMA Archive
- Sandeen 1995, *Picturing an Exhibition* (critical reconstruction of the thematic argument)

## Output

- `data/sections.csv` (`id, title, theme, order, photo_ids, sandburg_prologue_excerpt, source_ids, notes`)
- `research/sections.md` — narrative overview of the sections and their thematic logic

## Acceptance criteria

- [ ] Every photograph in `data/photographs.csv` references a valid `section` id
- [ ] Sandburg excerpts quoted verbatim with the catalog as cited source
- [ ] Critical reading of the sectioning logic acknowledged (Sandeen 1995; Barthes 1957)
- [ ] Perspective notes present (curatorial + critical)
