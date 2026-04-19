---
name: <agent-name>
type: research | operational | review | training
model: opus | sonnet | haiku
---

# Agent: <name>

## Mandate

<1–2 sentences: what this agent is responsible for.>

## Inputs

- Issue body (the brief)
- <other required inputs: CSVs, existing research files, source entries>

## Primary sources to consult

- <source or archive>
- <source or archive>

## Outputs

- <file(s) produced or modified — exact paths>
- PR with `Closes #<n>`

## Acceptance criteria

- [ ] All statements cite ≥1 source in `sources/`
- [ ] Every citation meets `CREDIBILITY.md` Tier 1 / 2 / 3
- [ ] Schema passes `scripts/validate_schema.py`
- [ ] Perspective tags declared for any interpretive content
- [ ] No confabulated dates, names, quotes, or URLs

## Workflow

1. <step>
2. <step>
3. Open PR with the standard template.
4. Wait for the 4-judge panel.

## Out of scope

- <what this agent should NOT do>

## Escalation

If blocked, comment on the issue with `blocked: <reason>` and apply the `blocked` label.
