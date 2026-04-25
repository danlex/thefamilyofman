---
layout: list
title: Photographers
namespace: Index
lede: The photographers who contributed to the 1955 exhibition. Nationality is recorded per the MoMA Master Checklist's own attribution; scholarly alternatives are noted in each row's source file.
permalink: /photographers/
edit_dir: site
---

<div class="list-filters">
  <input id="q" type="search" placeholder="Search name, nationality…" autocomplete="off">
  <select id="nationality" aria-label="Filter by nationality"><option value="">All nationalities</option></select>
</div>

{% assign rows = site.data.photographers %}
{% if rows and rows.size > 0 %}
<div class="list-meta">{{ rows.size }} of 273 rows seeded.</div>
<table class="entity-table" id="photographers-table">
  <thead>
    <tr>
      <th>Name</th>
      <th>Nationality</th>
      <th>Dates</th>
      <th>Plates</th>
      <th>Biography</th>
    </tr>
  </thead>
  <tbody>
    {% for p in rows %}
    <tr>
      <td><a href="{{ '/photographers/' | append: p.id | append: '/' | relative_url }}">{{ p.name }}</a></td>
      <td>{{ p.nationality }}</td>
      <td>{% if p.birth_year and p.birth_year != "" %}{{ p.birth_year }}{% endif %}{% if p.death_year and p.death_year != "" %}–{{ p.death_year }}{% endif %}</td>
      <td>{{ p.photo_count }}</td>
      <td>
        {% if p.bio_url and p.bio_url != "" -%}
        <a href="{{ p.bio_url }}" rel="noopener">institutional</a>
        {%- else -%}
        —
        {%- endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
{% else %}
<div class="empty">
  No photographer rows yet.
</div>
{% endif %}

<script src="{{ '/assets/js/filter.js' | relative_url }}" defer></script>
