# thefamilyofman

Research project documenting Edward Steichen's **The Family of Man** — the 1955 MoMA exhibition of 503 photographs by 273 photographers, now permanently housed at Clervaux Castle, Luxembourg (UNESCO Memory of the World, 2003).

## What this is

A multi-agent, issue-driven research workflow that produces:

- A complete catalog of the 503 photographs
- Biographies of all 273 contributing photographers
- Narrative histories: 1955 MoMA exhibition, 1955–1962 world tour, Clervaux installation, UNESCO inscription, critical reception
- A comprehensive bibliography of credible sources from 1950 to present
- A training dataset (JSONL) for finetuning an AI on this corpus

## How it works

Every investigation is a GitHub issue. A **Dispatcher** agent claims an issue, spawns a **Worker** subagent to resolve it. The Worker opens a PR. A **panel of four judges** — Credibility, Grounding, Schema, and Bias — reviews in parallel. Unanimous structural approval + no bias REJECT auto-merges. A **Dataset Curator** then converts merged research into training examples.

See [plan.md](plan.md) for the full plan, [AGENTS.md](AGENTS.md) for the workflow contract, and [CREDIBILITY.md](CREDIBILITY.md) for the source-quality rubric.

## Repository layout

| Path | Purpose |
|---|---|
| `data/` | CSV catalogs: photographs, photographers, sections |
| `sources/{decade}/` | Bibliography — one source per markdown file |
| `research/` | Thematic essays |
| `templates/` | Entry templates for sources and photographs |
| `training/` | Training dataset pipeline |
| `scripts/` | Validation, credibility, dataset, eval, merge automation |
| `.github/ISSUE_TEMPLATE/` | Investigation issue forms |
| `.claude/agents/` | Subagent definitions for the 17 roles |

## Status

Phase 0 — infrastructure build. See [plan.md §14](plan.md) for phased execution.
