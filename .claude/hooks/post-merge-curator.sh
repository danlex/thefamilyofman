#!/bin/bash
# .claude/hooks/post-merge-curator.sh
#
# PostToolUse hook that logs merged PRs as candidates for the dataset-curator
# pipeline. Per plan.md §5, the dataset-curator should propose training examples
# after every merge of a source/research/data-touching PR. This hook writes one
# entry per merge to a queue file; a future scheduled agent (or manual
# /dataset-curator invocation) consumes the queue and opens a curation issue.
#
# Activation (per-user, in ~/.claude/settings.local.json or .claude/settings.local.json):
#
#   {
#     "hooks": {
#       "PostToolUse": [
#         {
#           "matcher": "Bash",
#           "hooks": [
#             { "type": "command",
#               "command": "bash $CLAUDE_PROJECT_DIR/.claude/hooks/post-merge-curator.sh" }
#           ]
#         }
#       ]
#     }
#   }
#
# Hook input (stdin) is the JSON event Claude Code sends for PostToolUse. We
# look for `tool_input.command` matching `gh pr merge`. On match, append a
# JSONL line to .claude/dataset-curator-queue.jsonl with the PR number, branch,
# files changed, and timestamp.
#
# This hook is intentionally minimal: it does NOT spawn an agent or call gh
# itself. The point is to capture the event for batch processing, not to
# expand the blast radius of every git operation.

set -euo pipefail

# Read the hook input from stdin
input="$(cat)"

# Extract the bash command that just ran. If jq is not available, fall back to
# grep — but jq is the standard tool for hook payloads.
if ! command -v jq >/dev/null 2>&1; then
  echo "post-merge-curator: jq not available; skipping" >&2
  exit 0
fi

cmd=$(printf '%s' "$input" | jq -r '.tool_input.command // ""')

# Only act on `gh pr merge` invocations. Match conservatively — the merge
# command can take various forms (with --squash, --merge, --rebase, etc.) but
# the literal substring "gh pr merge" is reliable.
if ! printf '%s' "$cmd" | grep -qE '\bgh[[:space:]]+pr[[:space:]]+merge\b'; then
  exit 0
fi

# Project root (Claude Code sets CLAUDE_PROJECT_DIR for hooks).
project_dir="${CLAUDE_PROJECT_DIR:-$(pwd)}"
queue_file="$project_dir/.claude/dataset-curator-queue.jsonl"

# Extract PR number from the command if present (`gh pr merge 123 --squash`).
pr_number=$(printf '%s' "$cmd" | grep -oE '\bgh[[:space:]]+pr[[:space:]]+merge[[:space:]]+[0-9]+' | grep -oE '[0-9]+$' || echo "")

# Capture context. Errors here should not block the merge; redirect to /dev/null.
timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
branch=$(git -C "$project_dir" rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown")
last_commit=$(git -C "$project_dir" log -1 --format=%H 2>/dev/null || echo "")
files=$(git -C "$project_dir" log -1 --format= --name-only 2>/dev/null | tr '\n' ';' || echo "")

# Append a JSONL line. Use jq to ensure correct escaping.
jq -n \
  --arg ts "$timestamp" \
  --arg pr "$pr_number" \
  --arg branch "$branch" \
  --arg sha "$last_commit" \
  --arg files "$files" \
  --arg cmd "$cmd" \
  '{event: "pr_merged", ts: $ts, pr: $pr, branch: $branch, sha: $sha, files: $files, cmd: $cmd}' \
  >> "$queue_file"

# Log to stderr for visibility in the harness transcript (Claude Code captures
# hook stderr in its event stream).
echo "post-merge-curator: queued PR #${pr_number:-?} for dataset-curator (queue: $queue_file)" >&2
