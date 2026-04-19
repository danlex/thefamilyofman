---
layout: list
title: Photographs
namespace: Catalog
lede: All 503 photographs in the exhibition. Click a row to open its article.
permalink: /photographs/
edit_dir: site
---

<div class="list-filters">
  <input id="q" type="search" placeholder="Search title, photographer, country…" autocomplete="off">
  <select id="country" aria-label="Filter by country"><option value="">All countries</option></select>
  <select id="section" aria-label="Filter by section"><option value="">All sections</option></select>
</div>

{% if site.photographs.size > 0 %}
<table class="entity-table" id="photographs-table">
  <thead>
    <tr>
      <th style="width: 12%;">ID</th>
      <th>Title</th>
      <th>Photographer</th>
      <th>Year</th>
      <th>Country</th>
      <th>Section</th>
    </tr>
  </thead>
  <tbody>
    {% for p in site.photographs %}
    <tr>
      <td>{{ p.id }}</td>
      <td><a href="{{ p.url | relative_url }}">{{ p.title }}</a></td>
      <td>{{ p.photographer }}</td>
      <td>{{ p.year }}</td>
      <td>{{ p.country }}</td>
      <td>{{ p.section }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
{% else %}
<div class="empty">
  No photograph articles yet. The catalog is being built — see <a href="https://github.com/danlex/thefamilyofman/issues?q=is%3Aissue+label%3Acatalog">the catalog issues on GitHub</a>.
</div>
{% endif %}

<script src="{{ '/assets/js/filter.js' | relative_url }}" defer></script>
