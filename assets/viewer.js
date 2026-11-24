(function () {
  var box = document.getElementById('pages');
  var src = box.getAttribute('data-pdf');
  var original = box.getAttribute('data-original');
  function fail() {
    box.innerHTML = '<div class="status">The preview could not be loaded here.<br><br><a href="' + original + '" target="_blank" rel="noopener">Open the brochure (PDF)</a></div>';
  }
  if (!window.pdfjsLib) { fail(); return; }
  pdfjsLib.GlobalWorkerOptions.workerSrc = '../assets/pdfjs/pdf.worker.min.js';
  pdfjsLib.getDocument({ url: src }).promise.then(function (pdf) {
    box.innerHTML = '';
    var ratio = Math.min(window.devicePixelRatio || 1, 2);
    var slots = [];
    for (var i = 1; i <= pdf.numPages; i++) {
      var c = document.createElement('canvas');
      c.setAttribute('aria-label', 'Page ' + i);
      c.dataset.page = i;
      c.style.aspectRatio = '1.414 / 1';
      box.appendChild(c);
      slots.push(c);
    }
    function render(c) {
      if (c.dataset.done) return;
      c.dataset.done = '1';
      pdf.getPage(+c.dataset.page).then(function (page) {
        var w = box.clientWidth || 800;
        var v1 = page.getViewport({ scale: 1 });
        var vp = page.getViewport({ scale: (w / v1.width) * ratio });
        c.width = vp.width; c.height = vp.height;
        c.style.aspectRatio = v1.width + ' / ' + v1.height;
        page.render({ canvasContext: c.getContext('2d'), viewport: vp });
      });
    }
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) { render(e.target); io.unobserve(e.target); } });
      }, { rootMargin: '800px 0px' });
      slots.forEach(function (c) { io.observe(c); });
    } else { slots.forEach(render); }
  }).catch(fail);
})();
