# training/curated/ — Curation policy

This directory holds approved training examples for the Family of Man dataset.
They feed into `training/dataset.jsonl` via `scripts/build_dataset.py`.

## Relationship to training/eval/

`training/eval/eval.jsonl` is the held-out evaluation set and must NOT overlap
with examples in `training/curated/`. Every example here was checked against the
full eval.jsonl question list (85 rows, eval-00001 through eval-00100 with gaps)
before acceptance. No question in any `batch-*.jsonl` file duplicates a question
in eval.jsonl.

## Schema

Each line is a JSON object conforming to `training/schema.md`. Required fields:

- `id` — stable ID, format `ex-#####` (five digits, zero-padded)
- `messages` — `[{"role":"user","content":"..."},{"role":"assistant","content":"..."}]`
- `metadata.topic` — one of: `catalog`, `photographer`, `exhibition-history`,
  `tour`, `clervaux`, `unesco`, `reception`, `provenance`
- `metadata.source_ids` — array of `src-…` strings; must contain ≥1 Tier-1 or
  Tier-2 source
- `metadata.min_tier` — lowest credibility tier among `source_ids` (1 or 2 for
  inclusion in dataset.jsonl; 3 = blocked by auditor)
- `metadata.perspective` — `curatorial`, `critical`, `historical`,
  `institutional`, `archival`, or `biographical`
- `metadata.perspective_sources` — subset of `source_ids` representing the
  perspective stance
- `metadata.contested` — `true` if the example addresses a contested claim.
  Contested examples must either pair with a `counter_perspective_id` or
  acknowledge the contestation inline in the assistant message.
- `metadata.reviewed` — must be `true` for inclusion in `dataset.jsonl`

## Anti-confabulation rule (critical)

An example's assistant message may only name a specific source as corroborating a
fact if that source was actually read in the session that produced the example.
The curator agent must have either fetched the source via WebFetch/Read or read
an in-repo file that documents the source's content. Plausible-sounding citations
that were not actually consulted are confabulation and are blocked at the
Judge-Grounding stage.

Phrases that are safe in assistant messages:
- "not re-verified in this round"
- "cited in secondary literature but not consulted here"
- "flagged verified: false pending a future pass"

## Batch index

| File | IDs | Topics covered | Session |
|------|-----|----------------|---------|
| batch-01.jsonl | ex-00001 – ex-00025 | exhibition-history, catalog, reception (Barthes), photographer (Haas, Capa, Callahan), UNESCO, Clervaux, tour | 2026-05-21 |

## Perspective distribution target

Per plan.md §12 and AGENTS.md: at least 25% of interpretive examples
(`topic` in `reception`, `exhibition-history`) must carry `perspective: critical`.

Current distribution in batch-01:
- `critical`: ex-00005, ex-00006, ex-00019, ex-00024 (4 of 25 total; of the
  interpretive examples — topics reception/exhibition-history — 4 of 7,
  exceeding the 25% threshold)
- `institutional`: 12 examples
- `biographical`: 4 examples
- `historical`: 2 examples
- `curatorial`: 2 examples

## Build step

Run `scripts/build_dataset.py` to regenerate `training/dataset.jsonl` from all
approved `training/curated/batch-*.jsonl` files.
