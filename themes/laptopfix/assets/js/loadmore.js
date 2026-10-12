// Progressive "Load more" for article grids (homepage, category pages,
// all-articles page). Server renders the first batch for SEO; this script
// appends further batches from the Hugo-generated /index.json feed.
(function () {
  var grid = document.getElementById("article-grid");
  var btn = document.getElementById("load-more");
  if (!grid || !btn) return;

  var PAGE = 9;
  var offset = parseInt(grid.getAttribute("data-rendered") || "0", 10);
  var total = parseInt(grid.getAttribute("data-total") || "0", 10);
  var filter = grid.getAttribute("data-category") || "";
  var cache = null;
  var loading = false;

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function card(p) {
    var img = p.thumb
      ? '<img src="' + p.thumb + '" alt="' + esc(p.title) + '" loading="lazy" width="640" height="360">'
      : "";
    var badge = p.catName ? '<span class="badge">' + esc(p.catName) + "</span>" : "";
    return '<article><a class="acard" href="' + p.url + '">' +
      '<span class="thumb">' + img + "</span>" +
      '<span class="body">' + badge +
      "<h3>" + esc(p.title) + "</h3>" +
      '<p class="ex">' + esc(p.excerpt) + "</p>" +
      '<span class="meta"><span>' + esc(p.date) + '</span><span class="dot"></span>' +
      "<span>" + p.read + " min read</span></span>" +
      "</span></a></article>";
  }

  function render(list) {
    var slice = list.slice(offset, offset + PAGE);
    grid.insertAdjacentHTML("beforeend", slice.map(card).join(""));
    offset += slice.length;
    loading = false;
    if (offset >= list.length) {
      btn.style.display = "none";
    } else {
      btn.disabled = false;
      btn.textContent = "Load more fixes";
    }
  }

  btn.addEventListener("click", function () {
    if (loading) return;
    loading = true;
    btn.disabled = true;
    btn.textContent = "Loading…";
    if (cache) { render(filter ? cache.filter(match) : cache); return; }
    fetch("/index.json")
      .then(function (r) { return r.json(); })
      .then(function (data) {
        cache = data;
        render(filter ? data.filter(match) : data);
      })
      .catch(function () {
        loading = false;
        btn.disabled = false;
        btn.textContent = "Load more fixes";
      });
  });

  function match(p) { return p.category === filter; }

  // Nothing more to load (e.g. fewer articles than the first batch): hide now.
  if (total <= offset) btn.style.display = "none";
})();
