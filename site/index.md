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

<section class="wrap">
{% include image.html
   src="/assets/images/moma-1955-opening.jpg"
   alt="Visitors at a Family of Man installation, captioned 'Opening Day'"
   caption="A Family of Man tour-edition installation, captioned “Opening Day” by the U.S. Information Agency. Photographic record from the USIA's documentation of the show's traveling editions, 1955–1962 — not the 24 January 1955 MoMA opening itself."
   credit="U.S. National Archives · DPLA · Public domain"
   credit_url="https://commons.wikimedia.org/wiki/File:%22Family_of_Man%22_Exhibit,_Opening_Day_-_DPLA_-_bd5b1ae514db1f2e31d7bec695ee2d88.jpg" %}
</section>

<section class="wrap" style="margin-top: 2.5rem;">
  <div class="action-head">
    <div class="kicker">Use this wiki</div>
    <h2 class="action-h2">What are you looking for?</h2>
  </div>
  <div class="action-row">
    <a class="action-card" href="{{ '/photographs/' | relative_url }}">
      <div class="action-kicker">Find</div>
      <h3>A photograph</h3>
      <p>{{ site.data.photographs.size }} of 503 plates catalogued — searchable by photographer, country, section, year.</p>
    </a>
    <a class="action-card" href="{{ '/photographers/' | relative_url }}">
      <div class="action-kicker">Find</div>
      <h3>A photographer</h3>
      <p>{{ site.data.photographers.size }} of 273 contributors profiled — biographies linked to institutional archives.</p>
    </a>
    <a class="action-card" href="{{ '/sections/' | relative_url }}">
      <div class="action-kicker">Read about</div>
      <h3>A thematic section</h3>
      <p>The 11 clusters Steichen sequenced — from Prologue through Rededication, threaded with Sandburg.</p>
    </a>
    <a class="action-card" href="{{ '/bibliography/' | relative_url }}">
      <div class="action-kicker">Cite a</div>
      <h3>Source</h3>
      <p>{{ site.sources.size }} sources across eight decades, tier-graded for academic and museum use.</p>
    </a>
  </div>
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

<section class="wrap" style="margin-top: 4rem;">
  <figure class="pull-quote">
    <blockquote>
      <p>“A camera testament, a drama of the grand canyon of humanity, an epic woven of fun, mystery and holiness — here is the Family of Man.”</p>
    </blockquote>
    <figcaption>
      Carl Sandburg, closing line of the prologue distributed to visitors as a leaflet
      and reprinted in both editions of the catalog. Quoted in
      <a href="{{ '/sources/moma-1955-press-release-book/' | relative_url }}">MoMA's press release</a>
      announcing the book on 21 June 1955.
    </figcaption>
  </figure>
</section>

<section class="wrap-wide" style="padding: 0 1.25rem; margin-top: 4rem;">
  <div class="home-section-head">
    <div>
      <div class="kicker">In memoriam · 1879–1973</div>
      <h2>Edward Steichen — the author of the gallery</h2>
      <p class="lead">Born in Bivange (Béiweng), Luxembourg, on 27 March 1879. Director of the Department of Photography at MoMA from 1947 to 1962. The single curatorial author of <em>The Family of Man</em>. Died 25 March 1973 in West Redding, Connecticut, two days short of his 94th birthday.</p>
    </div>
    <a class="more" href="{{ '/steichen/' | relative_url }}">Read the memorial →</a>
  </div>
  <div class="memorial-card">
    <a class="memorial-portrait" href="{{ '/steichen/' | relative_url }}">
      <img src="{{ '/assets/images/steichen-1902-self-portrait.jpg' | relative_url }}" alt="Edward Steichen self-portrait, 1901" loading="lazy">
      <div class="memorial-portrait-credit">Self-portrait, 1901 · Public domain</div>
    </a>
    <div class="memorial-body">
      <blockquote class="memorial-quote">
        “I am a Luxembourgish boy.”
        <cite>Steichen introducing himself to Grand Duchess Charlotte at the White House, 1963 — the meeting that would lead, the next year, to the U.S. government's donation of <em>The Family of Man</em> to Luxembourg.</cite>
      </blockquote>
      <p class="memorial-prose">
        He bought his first camera at sixteen, was naturalised American at twenty-one, photographed for <em>Vogue</em> and <em>Vanity Fair</em> for fifteen years, commanded the U.S. Naval Aviation Photographic Unit in the Pacific, then assembled — over three years and across 503 photographs by 273 photographers — the most-visited photography exhibition of the twentieth century. The collection he gathered returned to his birthplace in 1994 and is on continuous public display at <a href="{{ '/clervaux/' | relative_url }}">Clervaux Castle</a> today.
      </p>
      <a class="memorial-cta" href="{{ '/steichen/' | relative_url }}">Read the full memorial →</a>
    </div>
  </div>
</section>

<section class="wrap-wide" style="padding: 0 1.25rem; margin-top: 4rem;">
  <div class="home-section-head">
    <div>
      <h2>The people behind the exhibition</h2>
      <p class="lead">Beyond the 273 photographers whose plates fill the galleries, four people shaped what visitors actually saw — and one Luxembourg head of state brought the prints home.</p>
    </div>
  </div>
  <div class="people-grid">
    <article class="person-card">
      <div class="person-portrait">
        <img src="{{ '/assets/images/sandburg-1955-nywts.jpg' | relative_url }}" alt="Carl Sandburg, 1955" loading="lazy">
      </div>
      <div class="person-body">
        <h3>Carl Sandburg</h3>
        <div class="person-dates">1878 – 1967 · poet</div>
        <p>Steichen's brother-in-law (he married Lilian Steichen in 1908) and the author of the prologue distributed to every visitor of the 1955 show as a leaflet, reprinted in both catalog editions. The closing line — <em>"A camera testament, a drama of the grand canyon of humanity…"</em> — is quoted in MoMA's press release for the book.</p>
        <div class="person-credit">Photo: Al Ravenna for World Telegram, 1955 · Library of Congress · Public domain</div>
      </div>
    </article>
    <article class="person-card">
      <div class="person-portrait person-portrait-glyph">
        {% include section-glyph.html slug="work" %}
      </div>
      <div class="person-body">
        <h3>Paul Rudolph</h3>
        <div class="person-dates">1918 – 1997 · architect</div>
        <p>Designed the gallery installation: temporary walls, prints ranging from 24 × 36 cm to 300 × 400 cm, photographs floating at varying heights — sometimes set on the floor, sometimes hung from the ceiling. Rudolph would later chair Yale's School of Architecture from 1958 to 1965 and become a defining figure of late-modernist American building.</p>
      </div>
    </article>
    <article class="person-card">
      <div class="person-portrait">
        <img src="{{ '/assets/images/charlotte-1919-grand-duchess.jpg' | relative_url }}" alt="Charlotte, Grand Duchess of Luxembourg, 1919" loading="lazy">
      </div>
      <div class="person-body">
        <h3>Grand Duchess Charlotte</h3>
        <div class="person-dates">1896 – 1985 · Luxembourg head of state</div>
        <p>Reigned 1919–1964. During a 1963 state visit to Washington, Steichen introduced himself to her with the words "I am a Luxembourgish boy." At his request, the U.S. government donated the last complete touring edition of <em>The Family of Man</em> to Luxembourg in 1964 — the act that gave Clervaux its present collection.</p>
        <div class="person-credit">Photo: unknown, 1919 · Public domain (PD-old)</div>
      </div>
    </article>
    <article class="person-card">
      <div class="person-portrait person-portrait-glyph">
        {% include section-glyph.html slug="family-and-children" %}
      </div>
      <div class="person-body">
        <h3>Wayne Miller</h3>
        <div class="person-dates">1918 – 2013 · Magnum photographer</div>
        <p>Magnum photographer (later Magnum's president, 1962–66) who contributed multiple plates to the exhibition. His role as Steichen's curatorial assistant on <em>The Family of Man</em> is asserted in the major secondary literature (Sandeen 1995; Steichen's own 1963 autobiography) but was not directly named in the in-repo MoMA press release or Master Checklist as of the most recent re-verification — flagged on his <a href="{{ '/photographers/pher-wayne-miller/' | relative_url }}">photographer page</a>.</p>
      </div>
    </article>
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
      <h2>By the numbers</h2>
      <p class="lead">A snapshot of the {{ site.data.photographs.size }} catalog rows seeded so far — country and section distributions, computed live from <code>data/photographs.csv</code>.</p>
    </div>
  </div>

  {% assign by_country = site.data.photographs | group_by: "country" | sort: "size" | reverse %}
  {% assign top_country_size = by_country | first %}
  {% assign top_country_count = top_country_size.items.size %}

  {% assign by_section = site.data.photographs | group_by: "section" %}

  <div class="numbers-grid">
    <div class="numbers-col">
      <h3 class="numbers-h3">Top countries of origin</h3>
      <div class="dist">
        {% for g in by_country limit: 8 %}
          {% assign g_count = g.items.size %}
          {% assign pct = g_count | times: 100 | divided_by: top_country_count %}
          <div class="dist-row">
            <span class="dist-label">{{ g.name | default: "—" }}</span>
            <span class="dist-bar"><span style="width: {{ pct }}%"></span></span>
            <span class="dist-num">{{ g_count }}</span>
          </div>
        {% endfor %}
      </div>
      <p class="dist-note">Top 8 of the {{ by_country.size }} countries seeded so far. The full exhibition draws from 68 countries.</p>
    </div>

    <div class="numbers-col">
      <h3 class="numbers-h3">Plates per section</h3>
      <div class="dist">
        {% assign sorted_sections_for_dist = site.data.sections | sort: "order" %}
        {% assign max_section_count = 0 %}
        {% for s in sorted_sections_for_dist %}
          {% assign match = by_section | where: "name", s.id | first %}
          {% if match %}
            {% assign mc = match.items.size %}
            {% if mc > max_section_count %}{% assign max_section_count = mc %}{% endif %}
          {% endif %}
        {% endfor %}
        {% if max_section_count == 0 %}{% assign max_section_count = 1 %}{% endif %}
        {% for s in sorted_sections_for_dist %}
          {% assign match = by_section | where: "name", s.id | first %}
          {% assign s_count = 0 %}
          {% if match %}{% assign s_count = match.items.size %}{% endif %}
          {% assign pct = s_count | times: 100 | divided_by: max_section_count %}
          {% assign sec_article = site.sections_articles | where: "order", s.order | first %}
          <div class="dist-row">
            <span class="dist-label">
              {% if sec_article -%}
              <a href="{{ sec_article.url | relative_url }}">{{ s.title }}</a>
              {%- else -%}
              {{ s.title }}
              {%- endif %}
            </span>
            <span class="dist-bar"><span style="width: {{ pct }}%"></span></span>
            <span class="dist-num">{{ s_count }}</span>
          </div>
        {% endfor %}
      </div>
      <p class="dist-note">Bars are scaled to the most-populated section in this snapshot. Empty rows are sections still awaiting catalog work.</p>
    </div>
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
      <h2>Recently added to the catalog</h2>
      <p class="lead">The latest plates seeded into <code>data/photographs.csv</code>, in reverse-checklist order.</p>
    </div>
    <a class="more" href="{{ '/photographs/' | relative_url }}">All photographs →</a>
  </div>
  {% assign recent = site.data.photographs | reverse %}
  <div class="recent-list">
    {% for p in recent limit: 6 %}
    <a class="recent-row" href="{{ '/photographs/' | append: p.id | append: '/' | relative_url }}">
      <span class="recent-id">{{ p.id }}</span>
      <span class="recent-name">{{ p.photographer }}</span>
      <span class="recent-meta">
        {%- assign psec = site.data.sections | where: "id", p.section | first -%}
        {% if psec %}{{ psec.title }}{% else %}{{ p.section }}{% endif %} · {{ p.country }}{% if p.year and p.year != "" %} · {{ p.year }}{% endif %}
      </span>
    </a>
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

<section class="wrap-wide" style="padding: 0 1.25rem; margin-top: 4rem;">
  <div class="home-section-head">
    <div>
      <h2>Help us finish this</h2>
      <p class="lead">The wiki is a work in progress, openly built on GitHub. Every gap below is a tracked issue waiting for a contributor — researchers, photographers' estates, and the archive community are all welcome.</p>
    </div>
    <a class="more" href="https://github.com/danlex/thefamilyofman/issues" rel="noopener">All issues →</a>
  </div>
  {% assign photos_open = 503 | minus: site.data.photographs.size %}
  {% assign photographers_open = 273 | minus: site.data.photographers.size %}
  {% assign photographers_no_dates = 0 %}
  {% for p in site.data.photographers %}
    {% if p.birth_year == "" or p.birth_year == nil %}
      {% assign photographers_no_dates = photographers_no_dates | plus: 1 %}
    {% endif %}
  {% endfor %}
  <div class="gaps-grid">
    <div class="gap-card">
      <div class="gap-num">{{ photos_open }}</div>
      <div class="gap-label">plates still to be catalogued</div>
      <p class="gap-meta">Of the 503 in the 1955 Master Checklist, {{ site.data.photographs.size }} have repository rows. Each remaining plate needs a checklist transcription and section assignment.</p>
      <a class="gap-link" href="https://github.com/danlex/thefamilyofman/issues?q=is%3Aissue+label%3Acatalog" rel="noopener">Catalog issues →</a>
    </div>
    <div class="gap-card">
      <div class="gap-num">{{ photographers_open }}</div>
      <div class="gap-label">photographers still to be profiled</div>
      <p class="gap-meta">Of the 273 contributors, {{ site.data.photographers.size }} have biographical rows. Each profile needs name, dates, nationality, and a Tier-1 or Tier-2 source.</p>
      <a class="gap-link" href="https://github.com/danlex/thefamilyofman/issues?q=is%3Aissue+label%3Aphotographer-bio" rel="noopener">Photographer issues →</a>
    </div>
    <div class="gap-card">
      <div class="gap-num">5</div>
      <div class="gap-label">overview essays still pending</div>
      <p class="gap-meta">The Exhibition · Clervaux · World Tour · Reception · UNESCO pages are stubs. Each needs a sourced research document before the site copy is written.</p>
      <a class="gap-link" href="https://github.com/danlex/thefamilyofman/issues?q=is%3Aissue+label%3Ainvestigation" rel="noopener">Investigation issues →</a>
    </div>
    {% if photographers_no_dates > 0 %}
    <div class="gap-card">
      <div class="gap-num">{{ photographers_no_dates }}</div>
      <div class="gap-label">profiled photographers still missing birth/death years</div>
      <p class="gap-meta">A row exists, but birth/death years remain blank because no Tier-1/2 source has been fetched. These need an institutional or peer-reviewed citation.</p>
      <a class="gap-link" href="https://github.com/danlex/thefamilyofman/issues?q=is%3Aissue+label%3Aphotographer-bio" rel="noopener">Help close them →</a>
    </div>
    {% endif %}
  </div>
</section>

<section class="wrap-wide" style="padding: 0 1.25rem; margin-top: 4rem;">
  <div class="home-section-head">
    <div>
      <h2>Sources</h2>
      <p class="lead">{{ site.sources.size }} cited references across eight decades — primary archive material from MoMA, LIFE, and the National Archives; obituaries and biographies from the major papers and museums; the Sandeen, Stimson, and Turner monographs.</p>
    </div>
    <a class="more" href="{{ '/bibliography/' | relative_url }}">All sources →</a>
  </div>

  {% assign tier1 = site.sources | where: "tier", 1 | size %}
  {% assign tier2 = site.sources | where: "tier", 2 | size %}
  {% assign tier3 = site.sources | where: "tier", 3 | size %}
  <div class="tier-strip">
    <div class="tier-stat"><span class="tier-num">{{ tier1 }}</span><span class="tier-label">Tier 1 — primary / archival</span></div>
    <div class="tier-stat"><span class="tier-num">{{ tier2 }}</span><span class="tier-label">Tier 2 — peer-reviewed academic</span></div>
    <div class="tier-stat"><span class="tier-num">{{ tier3 }}</span><span class="tier-label">Tier 3 — reputable press / museum</span></div>
  </div>

  {% assign recent_sources = site.sources | sort: "year" | reverse %}
  <div class="sources-strip">
    {% for src in recent_sources limit: 6 %}
    <a class="source-card" href="{{ src.url | default: src.url_archive | default: '#' }}" rel="noopener">
      <div class="source-year">{{ src.year }}</div>
      <div class="source-title">{{ src.title | truncate: 90 }}</div>
      <div class="source-meta">{% if src.author %}{{ src.author | truncate: 40 }} · {% endif %}Tier {{ src.tier }}</div>
    </a>
    {% endfor %}
  </div>
</section>

<section class="wrap" style="margin-top: 4rem;">
  <div class="cite-card">
    <div class="kicker">For academic and museum use</div>
    <h3 class="cite-h3">Cite this wiki</h3>
    <p class="cite-lead">Every page tracks its sources, its contributors, and its revision history. Suggested citation:</p>
    <pre class="cite-snippet">"<span id="cite-page">[Page title]</span>." <em>The Family of Man</em> wiki, edited by Alexandru Dan and contributors. {{ site.url }}{{ site.baseurl }}/. Accessed <span id="cite-date">[date]</span>.</pre>
    <p class="cite-foot">Per-page commits and revision history are public at <a href="https://github.com/danlex/thefamilyofman" rel="noopener">github.com/danlex/thefamilyofman</a>. Each article has an <em>Edit this page</em> link at its foot. Per the <a href="https://github.com/danlex/thefamilyofman/blob/main/CREDIBILITY.md" rel="noopener">credibility rubric</a>, claims are tier-graded; per the <a href="https://github.com/danlex/thefamilyofman/blob/main/CLAUDE.md" rel="noopener">museum-grade accuracy policy</a>, no source is cited that wasn't fetched in the working session.</p>
  </div>
  <script>
    (function () {
      var page = document.getElementById('cite-page');
      var date = document.getElementById('cite-date');
      if (page) page.textContent = document.title.split(' · ')[0] || 'The Family of Man';
      if (date) date.textContent = new Date().toISOString().slice(0, 10);
    })();
  </script>
</section>

<section class="wrap" style="margin-top: 4rem;">
  <div class="perspective-note">
    <strong>About this wiki</strong>
    A research project built openly on GitHub. Every article cites its sources.
    Every contribution is reviewed by a four-judge panel for credibility, grounding,
    schema conformance, and bias. Anyone can improve any page by clicking
    <em>Edit this page</em> at the bottom — see the
    <a href="https://github.com/danlex/thefamilyofman/blob/main/CONTRIBUTING.md">contributing guide</a>.
  </div>
</section>
