// Copy-link button for the article share row.
(function () {
  var btn = document.getElementById("copy-link");
  if (!btn) return;
  function done() {
    var m = document.getElementById("share-done");
    if (m) {
      m.hidden = false;
      setTimeout(function () { m.hidden = true; }, 2000);
    }
  }
  function fallback(url) {
    var t = document.createElement("textarea");
    t.value = url;
    t.style.position = "fixed";
    t.style.opacity = "0";
    document.body.appendChild(t);
    t.select();
    try { document.execCommand("copy"); done(); } catch (e) {}
    document.body.removeChild(t);
  }
  btn.addEventListener("click", function () {
    var url = btn.getAttribute("data-url");
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(done, function () { fallback(url); });
    } else {
      fallback(url);
    }
  });
})();
