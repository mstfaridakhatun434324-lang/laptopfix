// Lightweight client-side search over the Hugo-generated /index.json.
(function () {
  var input = document.getElementById("site-search");
  var box = document.getElementById("search-results");
  if (!input || !box) return;
  var index = null, timer = null;

  function esc(s) {
    return s.replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  input.addEventListener("input", function () {
    clearTimeout(timer);
    var q = input.value.trim().toLowerCase();
    if (q.length < 2) { box.classList.remove("open"); box.innerHTML = ""; return; }
    timer = setTimeout(function () {
      function run(data) {
        var hits = data.filter(function (p) {
          return (p.title + " " + p.excerpt + " " + p.category).toLowerCase().indexOf(q) !== -1;
        }).slice(0, 8);
        if (!hits.length) { box.classList.remove("open"); box.innerHTML = ""; return; }
        box.innerHTML = hits.map(function (p) {
          return '<a href="' + p.url + '" role="option"><span class="sr-cat">' + esc(p.category) +
            '</span><br>' + esc(p.title) + "</a>";
        }).join("");
        box.classList.add("open");
      }
      if (index) { run(index); return; }
      fetch("index.json").then(function (r) { return r.json(); }).then(function (data) {
        index = data; run(data);
      }).catch(function () {});
    }, 180);
  });

  document.addEventListener("click", function (e) {
    if (!box.contains(e.target) && e.target !== input) box.classList.remove("open");
  });
})();
