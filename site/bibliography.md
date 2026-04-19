---
layout: list
title: Bibliography
namespace: Sources
lede: Every source used to build this wiki, with its tier and the decade it belongs to. Credibility rubric at /about/#credibility.
permalink: /bibliography/
edit_dir: site
---

<div class="list-filters">
  <input id="q" type="search" placeholder="Search author, title…" autocomplete="off">
  <select id="tier" aria-label="Filter by tier">
    <option value="">All tiers</option>
    <option value="1">Tier 1 — primary / archival</option>
    <option value="2">Tier 2 — peer-reviewed / academic</option>
    <option value="3">Tier 3 — reputable press / museum</option>
  </select>
  <select id="decade" aria-label="Filter by decade"><option value="">All decades</option></select>
</div>

{% if site.sources.size > 0 %}
<table class="entity-table" id="sources-table">
  <thead>
    <tr>
      <th>Author</th>
      <th>Title</th>
      <th>Year</th>
      <th>Type</th>
      <th>Tier</th>
    </tr>
  </thead>
  <tbody>
    {% for s in site.sources %}
    <tr>
      <td>{{ s.author }}</td>
      <td><a href="{{ s.url | relative_url }}">{{ s.title }}</a></td>
      <td>{{ s.year }}</td>
      <td>{{ s.type }}</td>
      <td>{{ s.tier }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
{% else %}
<div class="empty">
  The bibliography is being built — three librarian agents (Primary / Critical / Contemporary eras) will populate this as Phase 2 proceeds.
</div>
{% endif %}

<script src="{{ '/assets/js/filter.js' | relative_url }}" defer></script>
