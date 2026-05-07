# Evaluation set — `eval.jsonl`

Held-out evaluation questions for *The Family of Man* training/finetune
pipeline. **This file is locked.** Additions are made only via explicit
Eval-Designer PRs, never via auto-curation.

## Coverage and policy

- **Held-out integrity.** Every question in `eval.jsonl` is reserved
  from the training pipeline. Questions and their ground-truth answers
  must not be replicated verbatim in `training/dataset.jsonl`,
  `training/curated/`, or `training/raw/`. The auditor (`scripts/audit_dataset.py`)
  enforces no duplicate `(user-message, perspective)` pairs across files
  in the dataset path; the same convention is observed for eval rows.
- **Source-grounded.** Every row carries a non-empty `source_ids`
  array. `min_tier` is the lowest credibility tier among those sources,
  and is `≤ 2` for every entry in the v0.1 seed.
- **Schema.** Each line is one JSON object following
  `training/schema.md`, plus an `eval_category` and `difficulty` field
  inside `metadata`.

## v0.1 seed (48 questions, 2026-05-07, issue #121)

This is the first batch. Plan.md §11 targets ~200 questions at v0.1; this
seeds 48 (originally drafted as 50; two rows withdrawn during the judge
panel — see "Withdrawn rows" below).

### Distribution

| `eval_category`       | Count | Share |
|-----------------------|-------|-------|
| catalog               | 8     | 17%   |
| photographer          | 12    | 25%   |
| exhibition-history    | 3     | 6%    |
| tour                  | 8     | 17%   |
| clervaux              | 5     | 10%   |
| unesco                | 5     | 10%   |
| reception             | 5     | 10%   |
| sections              | 2     | 4%    |
| **Total**             | **48**| **100%** |

(`eval_category` is the eval-specific bucket. Top-level `topic` follows
`training/schema.md`'s enum: `catalog`, `photographer`,
`exhibition-history`, `tour`, `clervaux`, `unesco`, `reception`,
`provenance`. Eval categories `sections` and `exhibition-history` both
map to the schema `topic` `exhibition-history`.)

No category exceeds 30% of the 48 questions.

### Withdrawn rows (2)

Two rows were withdrawn during the judge panel for PR #131 because their
answers rest only on Tier-3 sources (CREDIBILITY.md and
`scripts/audit_dataset.py` require `min_tier ≤ 2`):

- `eval-00012` — Wayne Miller's Magnum-Photos presidency (1962–66). Sources
  cited: `src-magnum-photographer-bios` (Tier 3), `src-nyt-2013-wayne-miller-obit`
  (Tier 3). The presidency claim is not anchored in any Tier-1/2 in-repo source.
- `eval-00022` — Roy DeCarava's 1952 Guggenheim. Source cited:
  `src-nyt-2009-decarava-obit` (Tier 3). The 1952-Guggenheim claim is not
  anchored in any Tier-1/2 in-repo source.

Both `id`s are left as gaps (not renumbered) so the surviving rows keep
their original identifiers. A future v0.2 pass can either reframe these
questions to Tier-1/2-anchored substitutes (e.g., the MoMA Master Checklist's
plate-level credit for Miller and DeCarava — both Tier-1) or close the gaps
by adding Tier-1/2 sources for the original facts.

### Difficulty mix

- `easy` — 8
- `medium` — 24
- `hard` — 18

### Critical-perspective floor

Of the rows whose schema-`topic` is interpretive (`reception`,
`exhibition-history`), the share carrying `perspective: critical`:

- `reception` rows: 5/5 = 100%
- `exhibition-history` rows: 0/5 (curatorial / institutional /
  archival only)
- combined interpretive: 5/10 = 50% — well above the 25% floor in
  `scripts/audit_dataset.py`.

## Adding to the eval set

1. Open an issue tagged `eval-set`.
2. Draft new questions in a feature branch under
   `agent/eval-set-vN.M-...`.
3. Each new row must:
   - have a unique `eval-#####` id;
   - cite ≥1 `src-…` id that resolves to a file in `sources/` (the
     credibility checker enforces this);
   - have `min_tier ≤ 2`;
   - have a `topic` from the schema enum;
   - not duplicate (verbatim) any user-message in
     `training/dataset.jsonl`, `training/curated/*.jsonl`, or
     `training/raw/*.jsonl`;
   - carry `eval_category` and `difficulty` (`easy`|`medium`|`hard`).
4. Run `scripts/validate_schema.py`,
   `scripts/check_credibility.py`, and
   `scripts/audit_dataset.py training/eval/eval.jsonl` — all must pass.
5. Run the `tvl-tech-bias-validator` skill on the diff before merge.
6. PR title: `Eval set vN.M …`. Reviewer must explicitly confirm the
   held-out invariant for every new question.

## Provenance

The v0.1 seed (eval-00001 … eval-00050) was authored on 2026-05-07
against material merged through PR #111 (photographer-bios batch 02)
and PR #107 (catalog completion / 488–490 reconciliation). No questions
were drawn from material in open PRs.
