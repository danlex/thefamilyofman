#!/usr/bin/env bash
# Sync research/mindmap.md → site/mindmap.md.
#
# research/mindmap.md is the canonical, editable source for the research
# mindmap. This script regenerates site/mindmap.md with Jekyll frontmatter
# so Jekyll renders it at /mindmap/ on the public wiki.
#
# Run manually after editing research/mindmap.md, or let the deploy
# workflow run it on every push to main.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/research/mindmap.md"
DST="$ROOT/site/mindmap.md"

[ -f "$SRC" ] || { echo "missing source: $SRC" >&2; exit 1; }

cat > "$DST" <<'FRONTMATTER'
---
layout: default
title: Research mindmap
namespace: Meta
permalink: /mindmap/
description: >-
  Living map of what we know and what we need to investigate about
  Edward Steichen's The Family of Man.
edit_dir: research
---

<!-- GENERATED FROM research/mindmap.md — DO NOT EDIT DIRECTLY.
     Edit the source and run scripts/sync_mindmap.sh. -->

<article class="wrap article" markdown="1">
  <div class="kicker">Research status</div>
  <h1 class="article-title">Mindmap</h1>
  <div class="article-meta">
    Canonical source: <a href="https://github.com/danlex/thefamilyofman/blob/main/research/mindmap.md">research/mindmap.md</a> ·
    updated after every merged research PR
  </div>
  <hr>

FRONTMATTER

# Strip the source's YAML frontmatter (the first ---…--- block) and any
# leading `# Research mindmap` title (the Jekyll layout already renders
# a title). Append everything else.
awk '
  BEGIN { in_fm = 0; fm_count = 0; skip_h1 = 0 }
  /^---$/ {
    fm_count++
    if (fm_count == 1) { in_fm = 1; next }
    if (fm_count == 2) { in_fm = 0; next }
  }
  in_fm { next }
  /^# Research mindmap$/ && skip_h1 == 0 { skip_h1 = 1; next }
  { print }
' "$SRC" >> "$DST"

cat >> "$DST" <<'CLOSER'

  {% include edit-links.html %}
</article>
CLOSER

echo "synced $SRC → $DST"
