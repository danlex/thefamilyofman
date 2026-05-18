---
layout: catalog
title: Plate Catalog
description: "The 503-plate MoMA Master Checklist for Edward Steichen's 1955 exhibition The Family of Man — browsable cards ordered by year and plate number with filters by photographer, section, and country."
permalink: /catalog/
# Comma-separated list of photo IDs that have a licensed image in
# site/assets/images/<id>.jpg.  Update this list when new plate images
# are added.  Maintained in tandem with scripts/generate_catalog_data.py.
plate_images: "photo-0080,photo-0093,photo-0134,photo-0170,photo-0376,photo-0377,photo-0379,photo-0441"
---

{% assign plate_image_set = page.plate_images | split: "," %}

<section class="wrap-wide cg-intro">
  <div class="home-section-head">
    <div>
      <h1>Plate Catalog</h1>
      <p class="lead">The plates of Edward Steichen's 1955 exhibition <em>The Family of Man</em>, as recorded in the MoMA Master Checklist for Exhibition #569 (503 plates total). This catalog currently covers <strong>{{ site.data.photographs | size }}</strong> plates; the remainder will be added as transcription continues. Ordered by year, then plate number. Thumbnails are shown only for photographs whose image is openly licensed and held in this repository. Per the <a href="https://github.com/danlex/thefamilyofman/blob/main/IMAGE_POLICY.md">image policy</a>, copyrighted plates link out to MoMA or Clervaux rather than hosting an image here.</p>
    </div>
  </div>
  <div class="cg-stats">
    <span id="cg-count">{{ site.data.photographs | size }}</span> plates
    &thinsp;·&thinsp;
    <span>{{ plate_image_set | size }} with in-repo image</span>
    &thinsp;·&thinsp;
    <span><a href="https://github.com/danlex/thefamilyofman/blob/main/data/photographs.csv">source CSV</a></span>
  </div>
</section>

<section class="wrap-wide cg-filters" aria-label="Filter controls">
  <div class="cg-filter-bar" id="cg-filter-bar">
    <label class="cg-filter-label" for="cg-q">Search</label>
    <input id="cg-q" class="cg-filter-input cg-filter-search"
           type="search"
           placeholder="Title, photographer, country…"
           autocomplete="off"
           aria-label="Search by title, photographer, or country">

    <label class="cg-filter-label" for="cg-year-from">Year</label>
    <div class="cg-filter-year-range">
      <input id="cg-year-from" class="cg-filter-input cg-filter-year"
             type="number" min="1840" max="1955" placeholder="From"
             aria-label="Year from">
      <span class="cg-year-sep">–</span>
      <input id="cg-year-to" class="cg-filter-input cg-filter-year"
             type="number" min="1840" max="1955" placeholder="To"
             aria-label="Year to">
    </div>

    <label class="cg-filter-label" for="cg-section">Section</label>
    <select id="cg-section" class="cg-filter-select" aria-label="Filter by section">
      <option value="">All sections</option>
      {% assign sections = site.data.photographs | map: "section" | uniq | sort %}
      {% for sec in sections %}
        {% if sec and sec != "" %}
        <option value="{{ sec }}">{{ sec | replace: "sec-", "" | replace: "-", " " | capitalize }}</option>
        {% endif %}
      {% endfor %}
    </select>

    <label class="cg-filter-label" for="cg-country">Country</label>
    <select id="cg-country" class="cg-filter-select" aria-label="Filter by country">
      <option value="">All countries</option>
      {% assign countries = site.data.photographs | map: "country" | uniq | sort %}
      {% for c in countries %}
        {% if c and c != "" %}
        <option value="{{ c }}">{{ c }}</option>
        {% endif %}
      {% endfor %}
    </select>

    <button id="cg-reset" class="cg-filter-reset" type="button" aria-label="Reset all filters">Reset</button>
  </div>
  <div id="cg-empty" class="cg-empty-state" hidden>
    No plates match the current filters. <button type="button" id="cg-reset-2" class="cg-inline-reset">Reset filters</button>
  </div>
</section>

<section class="wrap-wide cg-grid-wrap">
  {% comment %}
    Sort: year (ascending, unknowns/empty last), then plate number.
    Liquid does not have a stable multi-key sort, so we sort by id (which
    encodes plate order) and then accept that year-ordering within the same
    year group is by plate number — which is the checklist order.
  {% endcomment %}
  {% assign rows_with_year = site.data.photographs | where_exp: "p", "p.year and p.year != ''" | sort: "year" %}
  {% assign rows_no_year   = site.data.photographs | where_exp: "p", "p.year == nil or p.year == ''" %}

  <div class="cg-grid" id="cg-grid" aria-label="Photograph catalog">
    {% for p in rows_with_year %}
      {% include catalog-card.html p=p %}
    {% endfor %}
    {% for p in rows_no_year %}
      {% include catalog-card.html p=p %}
    {% endfor %}
  </div>
</section>

<section class="wrap-wide cg-coda">
  <p class="cg-coda-text">Source: MoMA Master Checklist for Exhibition #569 (<em>The Family of Man</em>, January 24 – May 8, 1955). Plate descriptions, photographer nationalities, and print dimensions are drawn verbatim from that checklist as transcribed in this repository. Date annotations where present are from the checklist; where absent the field is left blank. Copyright on most photographs rests with the photographers' estates.</p>
  <p class="cg-coda-text">See also: <a href="{{ '/photographs/' | relative_url }}">Photographs table</a> &nbsp;·&nbsp; <a href="{{ '/gallery/' | relative_url }}">Openly-licensed gallery</a> &nbsp;·&nbsp; <a href="{{ '/photographers/' | relative_url }}">Photographers</a></p>
</section>
