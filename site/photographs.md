---
layout: list
title: Photographs
namespace: Catalog
lede: The catalog of photographs in the 1955 exhibition, as recorded in the MoMA Master Checklist for Exhibition #569. Per the image policy, thumbnails are not hosted — each row links out to the photograph at MoMA or Clervaux.
permalink: /photographs/
edit_dir: site
---

<figure class="list-hero">
  <img src="{{ '/assets/images/family-of-man-schoolchildren.jpg' | relative_url }}" alt="Schoolchildren viewing The Family of Man" loading="lazy">
  <figcaption>Schoolchildren viewing a tour-edition installation of <em>The Family of Man</em>. USIA / National Archives · DPLA · Public domain.</figcaption>
</figure>

<aside class="page-context">
  <p>Most of the 503 plates remain under copyright; this index links out to the photograph at MoMA or Clervaux for each. A small number have entered the public domain — see the <a href="{{ '/' | relative_url }}#plates-we-can-show">"Plates we can show"</a> gallery on the homepage for the four PD examples currently hosted (Lange, Lee, Delano, Brady).</p>
</aside>

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
      <td><a href="{{ '/photographs/' | append: p.id | append: '/' | relative_url }}">{{ p.id }}</a></td>
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
