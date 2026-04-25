---
layout: list
title: Photographers
namespace: Index
lede: The photographers who contributed to the 1955 exhibition. Nationality is recorded per the MoMA Master Checklist's own attribution; scholarly alternatives are noted in each row's source file.
permalink: /photographers/
edit_dir: site
---

<figure class="list-hero list-hero-portraits">
  <img src="{{ '/assets/images/sandburg-1955-nywts.jpg' | relative_url }}" alt="Carl Sandburg, 1955">
  <img src="{{ '/assets/images/steichen-1902-self-portrait.jpg' | relative_url }}" alt="Edward Steichen self-portrait, 1901">
  <img src="{{ '/assets/images/charlotte-1919-grand-duchess.jpg' | relative_url }}" alt="Grand Duchess Charlotte, 1919">
  <figcaption>The author and his circle: Carl Sandburg (prologue, 1955); Edward Steichen (curator, self-portrait 1901); Grand Duchess Charlotte (the 1963 White House meeting that brought the show to Luxembourg). Read the <a href="{{ '/steichen/' | relative_url }}">Steichen memorial</a>.</figcaption>
</figure>

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
