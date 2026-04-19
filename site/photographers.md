---
layout: list
title: Photographers
namespace: Index
lede: The 273 photographers whose work appeared in the exhibition.
permalink: /photographers/
edit_dir: site
---

<div class="list-filters">
  <input id="q" type="search" placeholder="Search name, nationality…" autocomplete="off">
  <select id="nationality" aria-label="Filter by nationality"><option value="">All nationalities</option></select>
</div>

{% if site.photographers.size > 0 %}
<table class="entity-table" id="photographers-table">
  <thead>
    <tr>
      <th>Name</th>
      <th>Nationality</th>
      <th>Dates</th>
      <th>Works in the exhibition</th>
    </tr>
  </thead>
  <tbody>
    {% for p in site.photographers %}
    <tr>
      <td><a href="{{ p.url | relative_url }}">{{ p.name }}</a></td>
      <td>{{ p.nationality }}</td>
      <td>{% if p.birth_year %}{{ p.birth_year }}{% endif %}{% if p.death_year %}–{{ p.death_year }}{% endif %}</td>
      <td>{{ p.photo_count }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
{% else %}
<div class="empty">
  No photographer articles yet.
</div>
{% endif %}

<script src="{{ '/assets/js/filter.js' | relative_url }}" defer></script>
