---
layout: list
title: Photographs
namespace: Catalog
lede: The catalog of photographs in the 1955 exhibition, as recorded in the MoMA Master Checklist for Exhibition #569. Per the image policy, thumbnails are not hosted — each row links out to the photograph at MoMA or Clervaux.
permalink: /photographs/
edit_dir: site
---

<div class="list-filters">
  <input id="q" type="search" placeholder="Search title, photographer, country…" autocomplete="off">
  <select id="country" aria-label="Filter by country"><option value="">All countries</option></select>
  <select id="section" aria-label="Filter by section"><option value="">All sections</option></select>
</div>

{% assign rows = site.data.photographs %}
{% if rows and rows.size > 0 %}
<div class="list-meta">{{ rows.size }} rows. See <a href="https://github.com/danlex/thefamilyofman/blob/main/IMAGE_POLICY.md">image policy</a>.</div>
<table class="entity-table" id="photographs-table">
  <thead>
    <tr>
      <th style="width: 10%;">ID</th>
      <th>Photographer</th>
      <th>Year</th>
      <th>Country</th>
      <th>Section</th>
      <th>View</th>
    </tr>
  </thead>
  <tbody>
    {% for p in rows %}
    <tr>
      <td>{{ p.id }}</td>
      <td>{{ p.photographer }}</td>
      <td>{{ p.year }}</td>
      <td>{{ p.country }}</td>
      <td>{{ p.section }}</td>
      <td>
        {% if p.moma_object_id and p.moma_object_id != "" -%}
        <a href="https://www.moma.org/collection/works/{{ p.moma_object_id }}" rel="noopener">MoMA</a>
        {%- else -%}
        <a href="https://steichencollections.lu/" rel="noopener">Clervaux</a>
        {%- endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
{% else %}
<div class="empty">
  The catalog is being seeded — see <a href="https://github.com/danlex/thefamilyofman/issues?q=is%3Aissue+label%3Acatalog">the catalog issues on GitHub</a>.
</div>
{% endif %}

<script src="{{ '/assets/js/filter.js' | relative_url }}" defer></script>
