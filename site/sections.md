---
layout: list
title: Sections
namespace: Index
lede: Steichen's thematic groupings, threaded with Carl Sandburg's prologue.
permalink: /sections/
edit_dir: site
---

{% if site.sections_articles.size > 0 %}
<table class="entity-table">
  <thead>
    <tr><th>Order</th><th>Title</th><th>Theme</th></tr>
  </thead>
  <tbody>
    {% assign sorted = site.sections_articles | sort: "order" %}
    {% for s in sorted %}
    <tr>
      <td>{{ s.order }}</td>
      <td><a href="{{ s.url | relative_url }}">{{ s.title }}</a></td>
      <td>{{ s.theme }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
{% else %}
<div class="empty">
  The sectional structure is pending research — a Phase 1 investigation covers this.
</div>
{% endif %}
