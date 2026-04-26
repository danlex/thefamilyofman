// Vanilla client-side search with Apple-style icon-toggle drawer.
// - Magnifying-glass button in header → drawer slides down below nav with input + results
// - Lazy-loads /search.json on first open, caches in memory
// - Substring matching with three-tier score (title > subtitle > body), top 10
// - "/" focuses (when drawer closed → opens it). Esc closes. Click outside closes.
// No dependencies. No tracking.

(function () {
  var toggle = document.getElementById('site-search-toggle');
  var drawer = document.getElementById('site-search-drawer');
  var input = document.getElementById('site-search');
  var results = document.getElementById('site-search-results');
  var closeBtn = document.getElementById('site-search-close');
  if (!toggle || !drawer || !input || !results) return;

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
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function score(item, q) {
    var t = (item.title || '').toLowerCase();
    var s = (item.subtitle || '').toLowerCase();
    var b = (item.body || '').toLowerCase();
    if (t.indexOf(q) !== -1) return t.indexOf(q);
    if (s.indexOf(q) !== -1) return 100 + s.indexOf(q);
    if (b.indexOf(q) !== -1) return 1000 + b.indexOf(q);
    return -1;
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
    return scored.slice(0, 10).map(function (x) { return x.item; });
  }

  function render(query, items) {
    if (!query) { results.innerHTML = ''; results.hidden = true; return; }
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

  function openDrawer() {
    drawer.hidden = false;
    document.body.classList.add('site-search-open');
    toggle.setAttribute('aria-expanded', 'true');
    setTimeout(function () { input.focus(); input.select(); }, 30);
    if (!index) loadIndex();
  }
  function closeDrawer() {
    drawer.hidden = true;
    document.body.classList.remove('site-search-open');
    toggle.setAttribute('aria-expanded', 'false');
    input.value = '';
    render('', []);
    toggle.focus();
  }
  function isOpen() { return !drawer.hidden; }

  toggle.addEventListener('click', function () { isOpen() ? closeDrawer() : openDrawer(); });
  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);

  var debounce;
  input.addEventListener('input', function () {
    var q = input.value.trim();
    if (!q) { render('', []); return; }
    clearTimeout(debounce);
    debounce = setTimeout(function () {
      loadIndex().then(function () { render(q, filter(q)); });
    }, 80);
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && isOpen()) { e.preventDefault(); closeDrawer(); return; }
    if (e.key === '/' && document.activeElement !== input) {
      // Don't hijack typing in other input fields
      var t = e.target;
      if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable)) return;
      e.preventDefault();
      if (!isOpen()) openDrawer(); else input.focus();
    }
  });

  document.addEventListener('click', function (e) {
    if (!isOpen()) return;
    if (drawer.contains(e.target) || toggle.contains(e.target)) return;
    closeDrawer();
  });
})();
