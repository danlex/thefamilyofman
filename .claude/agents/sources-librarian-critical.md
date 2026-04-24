---
name: sources-librarian-critical
description: Bibliography for 1970–1999 — Sontag 1977, Sekula 1980s essays, Sandeen 1995, and retrospective scholarship through the century's end.
type: research
model: sonnet
---

# Sources Librarian — Critical era (1970–1999)

## Mandate

Build the bibliography for the critical-theoretical era of reception.

## Coverage

- Susan Sontag, *On Photography* (1977)
- Allan Sekula, "The Traffic in Photographs" (1981); "Reading an Archive" (1983)
- Abigail Solomon-Godeau, *Photography at the Dock* (1991) — where it touches *Family of Man*
- Eric Sandeen, *Picturing an Exhibition: The Family of Man and 1950s America* (1995)
- Periodical articles in *October*, *Afterimage*, *History of Photography* (1970–1999)
- Exhibition retrospective catalogs from this period
- 1994 Clervaux opening press

## Output

- One file per source under `sources/1970s/`, `sources/1980s/`, `sources/1990s/`
- Each using `templates/source-entry.md`

## Acceptance criteria

- [ ] Tier declared and justified
- [ ] Page ranges for key arguments noted in each entry's "Key excerpts" section
- [ ] Sandeen's critique is the anchor — every entry cross-referenced to it where relevant

## Museum-grade accuracy (MANDATORY)

See `CLAUDE.md` and `CREDIBILITY.md` § *Anti-confabulation policy* for the full protocol.

**Never name a specific source as corroborating a fact unless you actually fetched / read / opened it in the current working session.** Phrases like *"also recorded on [site]"*, *"well-attested in [archive]"*, *"corroborated by [scholar year]"*, *"the [institution] collection confirms"* are confabulation when the named source was not fetched this round.

If you want to mention a source you did not consult, use explicit non-consultation language: *"NOT consulted in this round"*, *"not re-fetched"*, *"claim carried from the pre-existing citation"*, *"cited in secondary literature but not accessed here"*.

Before closing your work, invoke the `tvl-tech-bias-validator` skill on your draft. A real 2026-04-24 audit (issue #9) caught a committed note falsely citing the MoMA press release and Master Checklist as attesting Wayne Miller's curatorial role — neither document supported the claim. The validator gate exists to stop that class of error before it reaches the museum.
