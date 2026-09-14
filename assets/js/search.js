(function () {
  "use strict";

  var container = document.getElementById("search");
  if (!container) return;
  var query = new URLSearchParams(window.location.search).get("q") || "";

  try {
    new PagefindUI({
      element: "#search",
      bundlePath: container.dataset.bundlePath,
      baseUrl: container.dataset.baseUrl,
      showEmptyFilters: false,
      showSubResults: true,
      showImages: false,
      autofocus: false,
      translations: { placeholder: "Search lessons, terms, and resources" }
    });
    if (query) {
      var input = container.querySelector("input");
      input.value = query;
      input.dispatchEvent(new Event("input", { bubbles: true }));
    }
  } catch (error) {
    container.hidden = true;
    document.getElementById("search-status").hidden = false;
  }
}());
