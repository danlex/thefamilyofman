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

- [ ] Tier declared and justified per the **Tier rules** below (not the brief's suggestion — apply the rules)
- [ ] Every "verbatim" quote re-fetched and diff-checked per the **Verbatim-quote protocol** below
- [ ] Anglophone-bias / coexistence framing cross-referenced to the existing perspective notes (do not create a new one)
- [ ] Page ranges for key arguments noted in each entry's "Key excerpts" section
- [ ] Sandeen's critique is the anchor — every entry cross-referenced to it where relevant

## Museum-grade accuracy (MANDATORY)

See `CLAUDE.md` and `CREDIBILITY.md` § *Anti-confabulation policy* for the full protocol.

**Never name a specific source as corroborating a fact unless you actually fetched / read / opened it in the current working session.** Phrases like *"also recorded on [site]"*, *"well-attested in [archive]"*, *"corroborated by [scholar year]"*, *"the [institution] collection confirms"* are confabulation when the named source was not fetched this round.

If you want to mention a source you did not consult, use explicit non-consultation language: *"NOT consulted in this round"*, *"not re-fetched"*, *"claim carried from the pre-existing citation"*, *"cited in secondary literature but not accessed here"*.

Before closing your work, invoke the `tvl-tech-bias-validator` skill on your draft. A real 2026-04-24 audit (issue #9) caught a committed note falsely citing the MoMA press release and Master Checklist as attesting Wayne Miller's curatorial role — neither document supported the claim. The validator gate exists to stop that class of error before it reaches the museum.

## Tier rules (apply strictly)

Recurring failure mode in past batches: tier inflation. Apply these rules even when the brief suggests otherwise.

- **Tier 1** = institutional / primary archival ONLY. The URL must point to the underlying primary archival object (1955 catalog edition scan, MoMA archives, NARA RG 306, CNA institutional page that has been directly fetched, UNESCO MoW page directly fetched, Steichen's own writings). An institution's *summary page* about its archive is NOT Tier 1 unless the primary object is the URL.
- **Tier 2** = enumerated peer-reviewed venues per `CREDIBILITY.md` (post-PR #91 amendment: *History of Photography*, *October*, *Art Bulletin*, *Aperture* editorial, *Afterimage*, *Camera Obscura*, *Screen*, *Visual Studies*, *Art Journal*, *Public Culture*, *Oxford Art Journal*, *Parachute*) PLUS university-press monographs PLUS named-author critical theory of record (Barthes, Sontag, Sekula, Krauss, Crimp, Foster, Phillips, Tagg, Burgin, Rosler, Solomon-Godeau, Stimson, Turner — all have parity).
- **Tier 3** = default for everything else: institutional summary pages, research-centre news articles, conference event pages, ArtHist-style notice boards, grant-database records, named newspaper-of-record articles by named authors, regional press, photography trade press (*Modern Photography*, *Popular Photography*, *Art Digest*).

If you declare Tier 1 with `verified: false` because the primary URL was not fetchable, **the file body must explicitly state that Tier 1 applies to the underlying institution and that the URL is a placeholder**. Otherwise downgrade to Tier 3.

## Verbatim-quote protocol (apply strictly)

**Recurring failure mode in past batches: synthesised paraphrases labelled "verbatim".** PRs #94 and #95 each had this exact failure caught by the grounding judge. Apply this protocol before any commit.

For every string in any entry that is presented as a quotation:

1. **Re-fetch the URL the quote is attributed to** — within the current session, not relying on a fetch from an earlier round.
2. **Diff the quoted string against the page text** — character-for-character. Word substitutions ("the museum" → "the Clervaux museum"), connective insertions ("following", "after", "drawing"), and clause-order inversions all count as fabrication.
3. **If the diff fails**, rewrite the quote to match the page exactly, OR demote the claim from "verbatim" to "paraphrase" with explicit "(paraphrase, not verbatim)" labelling.
4. **If the URL is unfetchable this round**, do not present any string as verbatim; explicitly say "the page was not fetched this round; the following claim is carried from secondary citation".

Do **not** synthesise across sentences. If two facts come from two different sentences on a page, quote the two sentences separately or paraphrase explicitly.

## Cross-reference instead of duplicate

The repo already has these perspective notes, written for prior batches:
- `research/reception-1970s-critical-theory.md` (Anglophone-bias flag, Bourdieu / Flusser / Eco gap)
- `research/reception-1980s-critical-theory.md` (coexistence-not-supersession, Phillips 1982 placement, Anglophone bias)
- `research/reception-1990s-clervaux-installation.md` (CNA institutional voice, Sandeen 1995 as peer-received-not-settled)
- `research/reception-1950s-us-press.md` (geographic concentration in NYC press, verification-status framing)

**Do not create a new per-batch perspective note** unless the bias judge specifically requests one for content not already covered. Cross-reference an existing note from the relevant entries instead. The bias judge's repeated "missing perspective note" flag has been a per-batch tax — closing it requires linking, not writing.

## Recurring traps (do not re-introduce)

- **Wayne Miller's curatorial-assistant claim** is the textbook CLAUDE.md worked example. Never assert without primary verification. Hedge as: "asserted in secondary literature; NOT corroborated by primary in-repo MoMA documents fetched this round."
- **Wikipedia is pointer-only** (CREDIBILITY.md). Cite as "fetched [date]" with the specific phrase returned, never as "well-known fact."
- **Aperture (commercial / store / print pages)** are Tier 2 only on the editorial-content-of-record path; product/store pages should be Tier 3 unless they directly anchor a Tier-2 claim.
- **Bay Press, Macmillan academic, Routledge teaching anthology** all qualify as Tier 2 via "critical theory of record" not via "university press." Flag this in the tier justification.
- **Trade publishers (Clarkson Potter, David R. Godine, etc.)** are NOT academic presses. If the author is named as a Tier-2 critical-theory-of-record figure (Niven, Malcolm), the tier holds via the author clause, not the publisher clause — say so.
