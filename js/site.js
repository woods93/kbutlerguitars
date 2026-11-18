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

// Contact form: send through Web3Forms without leaving the page.
(function () {
  var form = document.getElementById('contact-form');
  if (!form) return;
  var status = form.querySelector('.form-status');
  var btn = form.querySelector('button[type="submit"]');
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    status.className = 'form-status';
    status.textContent = 'Sending…';
    btn.disabled = true;
    fetch(form.action, {
      method: 'POST',
      headers: { 'Accept': 'application/json' },
      body: new FormData(form)
    }).then(function (r) { return r.json(); }).then(function (d) {
      if (d.success) {
        status.className = 'form-status ok';
        status.textContent = 'Thanks! Your message was sent. We’ll get back to you soon.';
        form.reset();
      } else {
        throw new Error(d.message || 'failed');
      }
    }).catch(function () {
      status.className = 'form-status err';
      status.textContent = 'Sorry, that didn’t go through. Please email kbutler@kbutlerguitars.com or call 615-815-5119.';
    }).then(function () { btn.disabled = false; });
  });
})();
