---
layout: list
title: Sections
namespace: Index
lede: Steichen's thematic groupings, threaded with Carl Sandburg's prologue. Eleven working clusters reconstructed from the 1955 catalog. Each glyph below is an original mark, not a reproduction of any exhibition photograph.
permalink: /sections/
edit_dir: site
---

{% if site.sections_articles.size > 0 %}
{% assign sorted = site.sections_articles | sort: "order" %}
<div class="section-grid">
  {% for s in sorted %}
  <a class="section-card" href="{{ s.url | relative_url }}">
    {% include section-glyph.html slug=s.slug %}
    <div class="section-card-num">{{ s.order | prepend: "00" | slice: -2, 2 }}</div>
    <h3>{{ s.title }}</h3>
    <p>{{ s.theme }}</p>
  </a>
  {% endfor %}
</div>
{% else %}
<div class="empty">
  The sectional structure is pending research — a Phase 1 investigation covers this.
</div>
{% endif %}
