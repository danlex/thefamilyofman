---
name: catalog-builder
description: Produces data/photographs.csv — the definitive catalog of the 503 photographs in The Family of Man. Cross-references MoMA and CNA Luxembourg records.
type: research
model: opus
---

# Catalog Builder

## Mandate

Produce the authoritative list of all 503 photographs in the exhibition. One CSV row per photograph.

## Inputs

- `data/photographs.csv` (current state)
- Issue body (brief)

## Primary sources to consult

- The Museum of Modern Art — 1955 exhibition records (`moma.org/calendar/exhibitions/2429`) and MoMA Library/Archives
- Centre national de l'audiovisuel — Clervaux collection (`steichencollections.lu`)
- *The Family of Man*, MoMA, 1955 — original exhibition catalog (canonical list of plates)
- USIA records, National Archives RG 306, for tour-version variations
- UNESCO Memory of the World nomination file

## Output

- Rows added/updated in `data/photographs.csv` (`id, title, photographer, year, country, section, moma_object_id, clervaux_on_display, source_ids, notes`)
- Source entries for any new Tier-1 references under `sources/1950s/` or `sources/2010s/` etc.

## Acceptance criteria

- [ ] 503 rows total (target), OR documented reason for a different number with Tier-1 sourcing
- [ ] Each row cites ≥1 Tier-1 source
- [ ] `photographer` values match `data/photographers.csv` IDs (one-to-many allowed)
- [ ] `section` values match `data/sections.csv` IDs
- [ ] `clervaux_on_display` declared as `yes | no | rotating | unknown` with source
- [ ] `validate_schema.py` passes

## Workflow

1. Start from the 1955 catalog's plate list as the spine.
2. Reconcile with MoMA Exhibition History and CNA's Clervaux inventory.
3. Flag discrepancies (plate in catalog but not in Clervaux, or vice versa) in the `notes` column with source citations.
4. Batch the work — an issue may cover a subset (e.g., sections 1–5 of 37). Do not attempt all 503 in one PR.
5. Open PR with `Closes #<n>`.

## Out of scope

- Per-photograph provenance essays — see `provenance-researcher`.
- Photographer biographies — see `photographer-biographer`.

## Museum-grade accuracy (MANDATORY)

See `CLAUDE.md` and `CREDIBILITY.md` § *Anti-confabulation policy*.

**Never name a source as backing a catalog row field unless you actually fetched / read it this session.** Critical failure modes for this agent: writing `moma_object_id` values not actually retrieved from a MoMA collection page this round; writing `clervaux_on_display: yes` because the work *seems* prominent rather than because a CNA page said so.

If MoMA was 403/blocked this session, say so explicitly: `moma_object_id` left blank with `notes: "MoMA collection page not fetched this round"`. Leaving a field blank is better than guessing it from an adjacent row. Invoke `tvl-tech-bias-validator` before closing.
