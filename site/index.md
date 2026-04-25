---
layout: default
title: Home
permalink: /
---

<section class="wrap hero">
  <div class="kicker">A public wiki</div>
  <h1>The Family of Man</h1>
  <p class="lede">
    Edward Steichen's 1955 exhibition at the Museum of Modern Art —
    503 photographs by 273 photographers, from 68 countries, threaded
    with Carl Sandburg's prologue. Permanently housed since 1994 at
    Clervaux Castle, Luxembourg. Inscribed on UNESCO's Memory of the
    World register in 2003.
  </p>
</section>

<section class="wrap-wide" style="padding: 0 1.25rem;">
  <div class="stats">
    <div><span class="num">503</span><span class="label">photographs</span></div>
    <div><span class="num">273</span><span class="label">photographers</span></div>
    <div><span class="num">68</span><span class="label">countries of origin</span></div>
    <div><span class="num">91</span><span class="label">tour venues</span></div>
    <div><span class="num">9M</span><span class="label">visitors (1955–62)</span></div>
    <div><span class="num">2003</span><span class="label">UNESCO inscription</span></div>
  </div>
</section>

<section class="wrap-wide" style="padding: 0 1.25rem; margin-top: 4rem;">
  <div class="home-section-head">
    <div>
      <h2>In eleven movements</h2>
      <p class="lead">Steichen sequenced the 503 plates as a single arc — from the cosmos to childbirth, from work and play to war and rededication. Eleven thematic clusters, reconstructed from the 1955 catalog.</p>
    </div>
    <a class="more" href="{{ '/sections/' | relative_url }}">All sections →</a>
  </div>
  {% assign sorted_sections = site.sections_articles | sort: "order" %}
  <div class="section-grid">
    {% for s in sorted_sections %}
    <a class="section-card" href="{{ s.url | relative_url }}">
      {% include section-glyph.html slug=s.slug %}
      <div class="section-card-num">{{ s.order | prepend: "00" | slice: -2, 2 }}</div>
      <h3>{{ s.title }}</h3>
      <p>{{ s.theme }}</p>
    </a>
    {% endfor %}
  </div>
</section>

<section class="wrap-wide" style="padding: 0 1.25rem; margin-top: 4rem;">
  <h2 style="font-family: var(--serif); font-weight: 500; font-size: 1.6rem; margin-bottom: 0.25rem;">Explore</h2>
  <p style="font-family: var(--sans); font-size: 0.92rem; color: var(--mid); margin-bottom: 1.25rem;">Nine entry points into the exhibition's story.</p>

  <div class="entry-grid">
    <a href="{{ '/exhibition/' | relative_url }}">
      <div class="kicker">1955</div>
      <h3>The Exhibition</h3>
      <p>How Steichen curated the show, how Paul Rudolph staged it, how New York received it.</p>
      {% include progress.html p=site.data.progress.exhibition %}
    </a>
    <a href="{{ '/photographs/' | relative_url }}">
      <div class="kicker">503 works</div>
      <h3>Photographs</h3>
      <p>Browse every photograph in the exhibition — by photographer, country, section, year.</p>
      {% include progress.html p=site.data.progress.photographs %}
    </a>
    <a href="{{ '/photographers/' | relative_url }}">
      <div class="kicker">273 contributors</div>
      <h3>Photographers</h3>
      <p>Biographies of every photographer who contributed work to the show.</p>
      {% include progress.html p=site.data.progress.photographers %}
    </a>
    <a href="{{ '/sections/' | relative_url }}">
      <div class="kicker">Thematic</div>
      <h3>Sections</h3>
      <p>Steichen's thematic groupings, threaded with Carl Sandburg's prologue.</p>
      {% include progress.html p=site.data.progress.sections %}
    </a>
    <a href="{{ '/tour/' | relative_url }}">
      <div class="kicker">1955–1962</div>
      <h3>World Tour</h3>
      <p>Ninety-one venues, thirty-seven countries, nine million visitors.</p>
      {% include progress.html p=site.data.progress.tour %}
    </a>
    <a href="{{ '/clervaux/' | relative_url }}">
      <div class="kicker">Luxembourg</div>
      <h3>Clervaux</h3>
      <p>Steichen's gift to his birthplace; the castle installation and the 2010–13 restoration.</p>
      {% include progress.html p=site.data.progress.clervaux %}
    </a>
    <a href="{{ '/reception/' | relative_url }}">
      <div class="kicker">Critique</div>
      <h3>Reception</h3>
      <p>Barthes, Sontag, Sekula, Sandeen, Stimson, Turner — seven decades of critical reading.</p>
      {% include progress.html p=site.data.progress.reception %}
    </a>
    <a href="{{ '/bibliography/' | relative_url }}">
      <div class="kicker">Sources</div>
      <h3>Bibliography</h3>
      <p>Every source used to build this wiki, with its tier and relevance.</p>
      {% include progress.html p=site.data.progress.bibliography %}
    </a>
    <a href="{{ '/mindmap/' | relative_url }}">
      <div class="kicker">Meta</div>
      <h3>Mindmap</h3>
      <p>What we know, what we still need to investigate, and what's in flight — a living research status map.</p>
      {% include progress.html p=site.data.progress.mindmap %}
    </a>
  </div>
</section>

<section class="wrap-wide" style="padding: 0 1.25rem; margin-top: 4rem;">
  <div class="home-section-head">
    <div>
      <h2>Examined in detail</h2>
      <p class="lead">The first plates to receive a deep-dive provenance article — what the 1955 Master Checklist records, what was confirmed against archival sources, and what remains an open question.</p>
    </div>
    <a class="more" href="{{ '/photographs/' | relative_url }}">All photographs →</a>
  </div>
  {% assign featured_ids = "photo-0002,photo-0005,photo-0011,photo-0023,photo-0027" | split: "," %}
  <div class="featured-grid">
    {% for fid in featured_ids %}
      {% assign fp = site.data.photographs | where: "id", fid | first %}
      {% if fp %}
      <a class="featured-card" href="{{ '/photographs/' | append: fid | append: '/' | relative_url }}">
        <div class="kicker">Deep dive</div>
        <div class="photographer">{{ fp.photographer }}</div>
        <div class="meta">
          {% assign sec = site.data.sections | where: "id", fp.section | first %}{% if sec %}{{ sec.title }}{% else %}{{ fp.section }}{% endif %}<br>
          {{ fp.country }}{% if fp.year and fp.year != "" %} · {{ fp.year }}{% endif %} · <span style="font-family: var(--mono); letter-spacing: 0.05em;">{{ fid }}</span>
        </div>
      </a>
      {% endif %}
    {% endfor %}
  </div>
</section>

<section class="wrap-wide" style="padding: 0 1.25rem; margin-top: 4rem;">
  <div class="home-section-head">
    <div>
      <h2>Most-photographed contributors</h2>
      <p class="lead">From the {{ site.data.photographers.size }} photographer rows seeded so far, ranked by plate count in the 1955 Master Checklist. The full exhibition lists 273 contributors.</p>
    </div>
    <a class="more" href="{{ '/photographers/' | relative_url }}">All photographers →</a>
  </div>
  {% assign top = site.data.photographers | sort: "photo_count" | reverse %}
  <div class="contributor-list">
    {% for c in top limit: 8 %}
    <div class="contributor-row">
      <span class="rank">{{ forloop.index | prepend: "0" | slice: -2, 2 }}</span>
      <span class="name">{{ c.name }}</span>
      <span class="dates">
        {%- if c.birth_year and c.birth_year != "" -%}
          {{ c.birth_year }}{% if c.death_year and c.death_year != "" %}–{{ c.death_year }}{% endif %}
        {%- else -%}
          dates unconfirmed
        {%- endif -%}
        {% if c.nationality and c.nationality != "" %} · {{ c.nationality }}{% endif %}
      </span>
      <span class="count">{{ c.photo_count }} {% if c.photo_count == "1" %}plate{% else %}plates{% endif %}</span>
    </div>
    {% endfor %}
  </div>
</section>

<section class="wrap-wide" style="padding: 0 1.25rem; margin-top: 4rem;">
  <div class="home-section-head">
    <div>
      <h2>A timeline</h2>
      <p class="lead">Six anchor dates between the exhibition's opening and its current life at Clervaux.</p>
    </div>
  </div>
  <div class="timeline">
    <div class="timeline-row">
      <span class="date">24 Jan 1955</span>
      <span class="what">The exhibition opens at the <a href="{{ '/exhibition/' | relative_url }}">Museum of Modern Art</a> in New York. Galleries designed by Paul Rudolph; prologue leaflet by Carl Sandburg.</span>
    </div>
    <div class="timeline-row">
      <span class="date">1955–1962</span>
      <span class="what">Editions of the show <a href="{{ '/tour/' | relative_url }}">travel internationally</a> under the U.S. Information Agency — venues and visitor figures pending verification against the National Archives.</span>
    </div>
    <div class="timeline-row">
      <span class="date">1994</span>
      <span class="what">After decades in storage, the prints return to Luxembourg as Steichen's gift and go on permanent display at <a href="{{ '/clervaux/' | relative_url }}">Clervaux Castle</a>, curated by the Centre national de l'audiovisuel.</span>
    </div>
    <div class="timeline-row">
      <span class="date">2003</span>
      <span class="what">The Clervaux collection is inscribed on <a href="{{ '/unesco/' | relative_url }}">UNESCO's Memory of the World</a> register.</span>
    </div>
    <div class="timeline-row">
      <span class="date">2010–2013</span>
      <span class="what">A major restoration and re-installation of the Clervaux galleries is completed — see the <a href="{{ '/clervaux/' | relative_url }}">Clervaux page</a> for the CNA programme.</span>
    </div>
    <div class="timeline-row">
      <span class="date">Today</span>
      <span class="what">The wiki — a public, source-cited reconstruction of the show, its travels, and its critical reception. Latest progress: {{ site.data.progress.photographs.label }} of the catalog seeded.</span>
    </div>
  </div>
</section>

<section class="wrap" style="margin-top: 4rem;">
  <div class="perspective-note">
    <strong>About this wiki</strong>
    This wiki is a research project built openly on GitHub. Every article
    cites its sources. Every contribution is reviewed by a four-judge panel
    for credibility, grounding, schema conformance, and bias. Anyone can
    improve any page by clicking <em>Edit this page</em> at the bottom —
    see the <a href="https://github.com/danlex/thefamilyofman/blob/main/CONTRIBUTING.md">contributing guide</a>.
  </div>
</section>
