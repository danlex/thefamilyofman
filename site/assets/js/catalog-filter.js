// catalog-filter.js — client-side filter for the plate catalog grid.
// No dependencies, no build step. Under 2 KB minified.
// Reads data-* attributes from .cg-card elements and reflects filter
// state into the URL hash so filtered views are shareable.

(function () {
  "use strict";

  var grid = document.getElementById("cg-grid");
  if (!grid) return;

  var cards = Array.from(grid.querySelectorAll(".cg-card"));
  if (!cards.length) return;

  var qInput        = document.getElementById("cg-q");
  var yearFrom      = document.getElementById("cg-year-from");
  var yearTo        = document.getElementById("cg-year-to");
  var sectionSelect = document.getElementById("cg-section");
  var countrySelect = document.getElementById("cg-country");
  var resetBtn      = document.getElementById("cg-reset");
  var resetBtn2     = document.getElementById("cg-reset-2");
  var emptyState    = document.getElementById("cg-empty");
  var countEl       = document.getElementById("cg-count");

  // --- Attach listeners ---
  if (qInput)        qInput.addEventListener("input",  debounce(apply, 100));
  if (yearFrom)      yearFrom.addEventListener("input", debounce(apply, 100));
  if (yearTo)        yearTo.addEventListener("input",   debounce(apply, 100));
  if (sectionSelect) sectionSelect.addEventListener("change", apply);
  if (countrySelect) countrySelect.addEventListener("change", apply);
  if (resetBtn)      resetBtn.addEventListener("click", reset);
  if (resetBtn2)     resetBtn2.addEventListener("click", reset);

  // Restore from URL hash on load
  restoreFromHash();
  apply();

  // --- Core filter ---
  function apply() {
    var needle    = (qInput ? qInput.value : "").toLowerCase().trim();
    var yFrom     = yearFrom && yearFrom.value ? parseInt(yearFrom.value, 10) : null;
    var yTo       = yearTo   && yearTo.value   ? parseInt(yearTo.value,   10) : null;
    var secFilter = sectionSelect ? sectionSelect.value : "";
    var cntFilter = countrySelect ? countrySelect.value : "";

    var visible = 0;

    for (var i = 0; i < cards.length; i++) {
      var card = cards[i];
      var year = card.dataset.year ? parseInt(card.dataset.year, 10) : null;
      var photographer = (card.dataset.photographer || "").toLowerCase();
      var section  = card.dataset.section  || "";
      var country  = card.dataset.country  || "";
      var caption  = (card.querySelector(".cg-caption") || { textContent: "" }).textContent.toLowerCase();

      var show = true;

      // text search
      if (needle) {
        var haystack = photographer + " " + (card.dataset.year || "") + " " + country.toLowerCase() + " " + caption;
        if (haystack.indexOf(needle) === -1) show = false;
      }

      // year range
      if (show && yFrom !== null && !isNaN(yFrom)) {
        if (year === null || year < yFrom) show = false;
      }
      if (show && yTo !== null && !isNaN(yTo)) {
        if (year === null || year > yTo) show = false;
      }

      // section
      if (show && secFilter && section !== secFilter) show = false;

      // country
      if (show && cntFilter && country !== cntFilter) show = false;

      card.hidden = !show;
      if (show) visible++;
    }

    // Update count
    if (countEl) countEl.textContent = visible;

    // Empty state
    if (emptyState) emptyState.hidden = (visible > 0);

    // Persist to hash
    updateHash();
  }

  function reset() {
    if (qInput)        qInput.value = "";
    if (yearFrom)      yearFrom.value = "";
    if (yearTo)        yearTo.value = "";
    if (sectionSelect) sectionSelect.value = "";
    if (countrySelect) countrySelect.value = "";
    apply();
    history.replaceState(null, "", window.location.pathname);
  }

  // --- URL hash persistence ---
  // Hash format: #q=TEXT&yr=1935-1955&sec=sec-lovers&cnt=USA
  function updateHash() {
    var parts = [];
    if (qInput && qInput.value)        parts.push("q=" + encodeURIComponent(qInput.value));
    if (yearFrom && yearFrom.value)    parts.push("yr=" + yearFrom.value + "-" + (yearTo && yearTo.value ? yearTo.value : ""));
    if (yearTo && yearTo.value && !(yearFrom && yearFrom.value)) parts.push("yr=-" + yearTo.value);
    if (sectionSelect && sectionSelect.value) parts.push("sec=" + encodeURIComponent(sectionSelect.value));
    if (countrySelect && countrySelect.value) parts.push("cnt=" + encodeURIComponent(countrySelect.value));
    var hash = parts.length ? "#" + parts.join("&") : window.location.pathname;
    history.replaceState(null, "", parts.length ? "#" + parts.join("&") : window.location.pathname);
  }

  function restoreFromHash() {
    var hash = window.location.hash.replace(/^#/, "");
    if (!hash) return;
    var params = {};
    hash.split("&").forEach(function (p) {
      var idx = p.indexOf("=");
      if (idx === -1) return;
      params[p.slice(0, idx)] = decodeURIComponent(p.slice(idx + 1));
    });
    if (params.q && qInput)        qInput.value = params.q;
    if (params.yr) {
      var parts = params.yr.split("-");
      if (parts[0] && yearFrom) yearFrom.value = parts[0];
      if (parts[1] && yearTo)   yearTo.value   = parts[1];
    }
    if (params.sec && sectionSelect) sectionSelect.value = params.sec;
    if (params.cnt && countrySelect) countrySelect.value = params.cnt;
  }

  // --- Utility ---
  function debounce(fn, ms) {
    var timer;
    return function () {
      clearTimeout(timer);
      timer = setTimeout(fn, ms);
    };
  }

})();
