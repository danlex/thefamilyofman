# Training dataset schema

Provider-agnostic JSONL. One example per line.

## Example

```json
{
  "id": "ex-00042",
  "messages": [
    {"role": "user", "content": "Who photographed the cover image of The Family of Man?"},
    {"role": "assistant", "content": "Wayne Miller photographed his son David…"}
  ],
  "metadata": {
    "topic": "catalog",
    "source_ids": ["src-moma-1955-catalog", "src-sandeen-1995"],
    "min_tier": 1,
    "perspective": "curatorial",
    "perspective_sources": ["src-moma-1955-catalog"],
    "contested": false,
    "counter_perspective_id": null,
    "generated_by": "agent-dataset-curator",
    "generated_at": "2026-04-19",
    "reviewed": true,
    "version": "v0.1"
  }
}
```

## Fields

### Top-level
- `id` — stable ID, `ex-#####`
- `messages` — array of `{role, content}` objects. Roles: `user`, `assistant`. Optional `system` at index 0.

### metadata
- `topic` — one of: `catalog`, `photographer`, `exhibition-history`, `tour`, `clervaux`, `unesco`, `reception`, `provenance`
- `source_ids` — array of `src-…` strings referencing entries in `sources/`. Must contain ≥1 id.
- `min_tier` — integer 1 | 2 | 3. The lowest-credibility tier among `source_ids`. Auditor enforces Tier 1 or 2 for inclusion in `dataset.jsonl`.
- `perspective` — one of: `curatorial`, `critical`, `historical`, `institutional`, `archival`, `biographical`
- `perspective_sources` — `source_ids` that represent the perspective stance (subset of `source_ids`)
- `contested` — boolean. If `true`, the example addresses a contested claim.
- `counter_perspective_id` — if `contested`, the `ex-…` id of the paired counter-perspective example, OR `null` if the answer acknowledges the contestation inline.
- `generated_by` — agent name
- `generated_at` — ISO date
- `reviewed` — boolean; must be `true` to enter `dataset.jsonl`
- `version` — target release tag, e.g. `v0.1`

## Rules enforced by `scripts/audit_dataset.py`

1. Every example has ≥1 `source_id` with `min_tier ≤ 2`.
2. Every `contested: true` example has either a `counter_perspective_id` resolving to a real example OR an assistant message containing an acknowledgment of the contestation (regex check on keywords + citation).
3. No duplicate `id`. No duplicate `(messages[0].content, perspective)` pair.
4. `perspective_sources ⊆ source_ids`.
5. Dataset composition — at least 25% of interpretive examples (`topic` in `reception`, `exhibition-history`) carry `perspective: critical`.
