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

<section class="wrap-wide" style="padding: 0 1.25rem; margin-top: 2.5rem;">
  <h2 style="font-family: var(--serif); font-weight: 500; font-size: 1.6rem; margin-bottom: 0.25rem;">Explore</h2>
  <p style="font-family: var(--sans); font-size: 0.92rem; color: var(--mid); margin-bottom: 1.25rem;">Eight entry points into the exhibition's story.</p>

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
