---
layout: default
title: Timeline
permalink: /timeline/
---

<div class="tl-header wrap">
  <div class="kicker">1950 to present</div>
  <h1>Timeline</h1>
  <p class="tl-intro">A chronological record of <em>The Family of Man</em>: from the 1955 MoMA opening through the USIA world tour, the Luxembourg donation, the Clervaux permanent installation, the 2003 UNESCO inscription, the 2010–2013 restoration, and the 70th anniversary in 2025. Every row cites at least one source in this wiki.</p>
  <p class="tl-source-note">Source of truth: <code><a href="https://github.com/danlex/thefamilyofman/blob/main/data/timeline-events.csv">data/timeline-events.csv</a></code> — single source of truth for this page; future research agents add rows to that file.</p>
</div>

<div class="tl-body wrap-wide">

{% assign events = site.data["timeline-events"] | sort: "year" %}

{% assign prev_year = "" %}

{% for ev in events %}
  {% assign yr = ev.year | to_integer %}
  {% assign decade = yr | divided_by: 10 | times: 10 %}
  {% assign prev_decade = prev_year | to_integer | divided_by: 10 | times: 10 %}

  {% if decade != prev_decade %}
  <div class="tl-decade-marker">
    <span class="tl-decade-label">{{ decade }}s</span>
  </div>
  {% endif %}

  {% assign ev_kind = ev.kind %}
  <div class="tl-event{% if ev_kind == 'source' %} tl-event--source{% elsif ev_kind == 'photo' %} tl-event--photo{% endif %}">
    <div class="tl-date-col">
      <span class="tl-year">{{ ev.year }}</span>
      {% if ev.month and ev.month != "" %}
        <span class="tl-month">
          {% assign m = ev.month | to_integer %}
          {% case m %}
            {% when 1 %}Jan
            {% when 2 %}Feb
            {% when 3 %}Mar
            {% when 4 %}Apr
            {% when 5 %}May
            {% when 6 %}Jun
            {% when 7 %}Jul
            {% when 8 %}Aug
            {% when 9 %}Sep
            {% when 10 %}Oct
            {% when 11 %}Nov
            {% when 12 %}Dec
          {% endcase %}
          {% if ev.day and ev.day != "" %} {{ ev.day }}{% endif %}
        </span>
      {% endif %}
    </div>

    <div class="tl-connector">
      <div class="tl-dot"></div>
      <div class="tl-line"></div>
    </div>

    <div class="tl-content">
      <h3 class="tl-event-title">
        {% if ev.links and ev.links != "" %}
          <a href="{{ ev.links | relative_url }}">{{ ev.title }}</a>
        {% else %}
          {{ ev.title }}
        {% endif %}
      </h3>
      <p class="tl-event-body">{{ ev.body_short }}</p>
      {% if ev.source_id and ev.source_id != "" %}
        <div class="tl-event-source">
          <a href="{{ '/sources/' | append: ev.source_id | replace: 'src-', '' | relative_url }}" class="tl-src-link">Source: {{ ev.source_id }}</a>
        </div>
      {% endif %}
    </div>
  </div>

  {% assign prev_year = ev.year %}
{% endfor %}

</div>

<div class="wrap" style="margin-top: 3rem;">
  <div class="perspective-note">
    <strong>Source discipline.</strong>
    Every row in this timeline cites at least one source already in <code>sources/</code> or <code>research/</code>. Claims that lack Tier-1 or Tier-2 backing are noted in <code>body_short</code>. Two rows carry explicit uncertainty flags: the 1963 Washington meeting between Steichen and Grand Duchess Charlotte (rests on a Tier-3 chronicle.lu source; not corroborated by the CNA collections pages); and the Moscow 1959 venue identification as Sokolniki Park (widely repeated in secondary literature but the CNA source confirms only year and city). No new external claims were introduced for this page; all dates and attributions derive from sources fetched and recorded in prior wiki passes.
  </div>
</div>
