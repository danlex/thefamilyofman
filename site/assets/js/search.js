// Vanilla client-side search across photographs, photographers, sources, and top-level pages.
// Loads /search.json once, filters on substring match (lowercased), renders a dropdown of up to 10 results.
// No dependencies. No tracking. No analytics. Pure DOM.

(function () {
  var input = document.getElementById('site-search');
  var results = document.getElementById('site-search-results');
  if (!input || !results) return;

  var index = null;
  var indexLoading = false;
  var indexUrl = (document.documentElement.dataset.baseurl || '') + '/search.json';

  function loadIndex() {
    if (index || indexLoading) return Promise.resolve(index);
    indexLoading = true;
    return fetch(indexUrl)
      .then(function (r) { return r.ok ? r.json() : []; })
      .then(function (data) { index = data || []; indexLoading = false; return index; })
      .catch(function () { index = []; indexLoading = false; return index; });
  }

  function escapeHTML(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function score(item, q) {
    // Prefer matches in title, then subtitle, then body. Lower score = better.
    var t = (item.title || '').toLowerCase();
    var s = (item.subtitle || '').toLowerCase();
    var b = (item.body || '').toLowerCase();
    if (t.indexOf(q) !== -1) return t.indexOf(q);
    if (s.indexOf(q) !== -1) return 100 + s.indexOf(q);
    if (b.indexOf(q) !== -1) return 1000 + b.indexOf(q);
    return -1;
  }

  function render(query, items) {
    if (!query) {
      results.innerHTML = '';
      results.hidden = true;
      return;
    }
    if (!items.length) {
      results.innerHTML = '<div class="search-empty">No matches.</div>';
      results.hidden = false;
      return;
    }
    var html = items.map(function (it) {
      var kind = it.kind || '';
      return '<a class="search-hit search-hit-' + escapeHTML(kind) + '" href="' + escapeHTML(it.url) + '">'
        + '<span class="search-hit-kind">' + escapeHTML(kind) + '</span>'
        + '<span class="search-hit-title">' + escapeHTML(it.title) + '</span>'
        + (it.subtitle ? '<span class="search-hit-sub">' + escapeHTML(it.subtitle) + '</span>' : '')
        + '</a>';
    }).join('');
    results.innerHTML = html;
    results.hidden = false;
  }

  function filter(q) {
    if (!index) return [];
    q = q.toLowerCase();
    var scored = [];
    for (var i = 0; i < index.length; i++) {
      var sc = score(index[i], q);
      if (sc >= 0) scored.push({ item: index[i], score: sc });
    }
    scored.sort(function (a, b) { return a.score - b.score; });
    return scored.slice(0, 10).map(function (s) { return s.item; });
  }

  var debounce;
  input.addEventListener('input', function () {
    var q = input.value.trim();
    if (!q) { render('', []); return; }
    clearTimeout(debounce);
    debounce = setTimeout(function () {
      loadIndex().then(function () { render(q, filter(q)); });
    }, 80);
  });
  input.addEventListener('focus', function () { if (!index) loadIndex(); });
  input.addEventListener('blur', function () {
    // Slight delay so click on a hit registers before we hide
    setTimeout(function () { results.hidden = true; }, 150);
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { input.blur(); results.hidden = true; }
    if (e.key === '/' && document.activeElement !== input) {
      e.preventDefault();
      input.focus();
    }
  });
})();
