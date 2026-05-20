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

### Difficulty mix (v0.1 seed)

- `easy` — 8
- `medium` — 24
- `hard` — 18

### Critical-perspective floor (v0.1 seed)

Of the rows whose schema-`topic` is interpretive (`reception`,
`exhibition-history`), the share carrying `perspective: critical`:

- `reception` rows: 5/5 = 100%
- `exhibition-history` rows: 0/5 (curatorial / institutional /
  archival only)
- combined interpretive: 5/10 = 50% — well above the 25% floor in
  `scripts/audit_dataset.py`.

## v0.1 batch 02 (+37 questions, 2026-05-20, issue #139)

Second batch, bringing the cumulative total from 48 to 85 (originally
drafted as 50; 13 rows were withdrawn before merge due to distribution-cap
violations, Tier-3-only sources, or narrow overlap with existing rows).

Questions are drawn from source files read in the authoring session:
ICP archive pages for Sander, Brassaï, Haas, Feininger, Shahn, Mili,
Brandt, Eisenstaedt, Erwitt, Mydans, Bubley, Lee, Hamaya, Yamahata
(all Tier 1); Takenaka 2020 (Tier 2) for the Japan tour; C²DH 2025
dispatch (Tier 2) for the world-tour "150 cities" figure and Beirut 1958;
Newbury 2024 (Tier 2) for USIA Africa photographic diplomacy; and the
MoMA Master Checklist / MoMA Szarkowski 1962 appointment file (Tier 1)
for exhibition-history and catalog rows. No external URL was fetched in
this batch; all evidence comes from in-repo source files.

### Cumulative distribution (85 questions)

| `eval_category`       | Count | Share |
|-----------------------|-------|-------|
| photographer          | 25    | 29%   |
| tour                  | 17    | 20%   |
| catalog               | 11    | 13%   |
| reception             | 9     | 11%   |
| clervaux              | 8     | 9%    |
| exhibition-history    | 7     | 8%    |
| unesco                | 7     | 8%    |
| sections              | 1     | 1%    |
| **Total**             | **85**| **100%** |

No category exceeds 30%.

### Withdrawn rows from batch 02 (13)

Withdrawn before merge for distribution, Tier-3, or overlap reasons:

- `eval-00053` — Brassaï plate count (narrow; overlaps eval-00052)
- `eval-00055` — Haas Magnum president years (narrow single-fact)
- `eval-00059` — Erwitt Magnum president year (narrow single-fact)
- `eval-00062` — Mydans birthyear ICP vs Wikipedia (narrow single-fact)
- `eval-00071` — Sander plate count/sections (narrow; overlaps eval-00051)
- `eval-00074` — Bubley plate count (narrow; 3 plates only)
- `eval-00075` — Russell Lee FSA duration (narrow; 2 plates only)
- `eval-00080` — Steichen Presidential Medal of Freedom 1963 (`src-steichen-1963-presidential-medal-freedom` is Tier 3; min_tier would be > 2)
- `eval-00088` — Mydans FSA/LIFE career + imprisonment (narrow; overlaps eval-00062)
- `eval-00092` — Bitter Years exhibition (`src-moma-1962-bitter-years-exhibition` is Tier 3; min_tier would be > 2)
- `eval-00094` — Mili MoMA exhibitions (narrow; overlaps eval-00058)
- `eval-00096` — Sander radio lecture title (very narrow; overlaps eval-00051)
- `eval-00097` — Hamaya birthplace (very narrow; overlaps eval-00063)

All `id`s left as gaps per convention.

### Difficulty mix (cumulative 85 rows)

- `easy` — 15
- `medium` — 38
- `hard` — 32

### Critical-perspective floor (cumulative 85 rows)

Of the rows whose schema-`topic` is interpretive (`reception`,
`exhibition-history`), the share carrying `perspective: critical`:

- `reception` rows: 9/9 = 100%
- `exhibition-history` rows: 0/7 (curatorial / institutional / archival only)
- combined interpretive: 9/16 = 56% — well above the 25% floor.

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

Batch 02 (eval-00051 … eval-00100, 13 withdrawn) was authored on
2026-05-20 against material merged through PR #246 (photog-bios batch 07,
origin/main = 7e87656). All evidence drawn from in-repo source files
read in the authoring session; no external URLs fetched in this batch.
Issue #139.
