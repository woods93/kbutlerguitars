// Mobile menu + photo lightbox. No dependencies.
(function () {
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  var box = document.querySelector('.lightbox');
  if (!box) return;
  var big = box.querySelector('img');
  var last = null;
  function close() {
    box.hidden = true;
    big.removeAttribute('src');
    if (last) last.focus();
  }
  document.addEventListener('click', function (e) {
    var shot = e.target.closest('.shot');
    if (shot) {
      last = shot;
      big.src = shot.getAttribute('data-full');
      big.alt = shot.querySelector('img').alt;
      box.hidden = false;
      box.querySelector('.lb-close').focus();
      return;
    }
    if (!box.hidden && (e.target === box || e.target.classList.contains('lb-close'))) close();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && !box.hidden) close();
  });
})();
