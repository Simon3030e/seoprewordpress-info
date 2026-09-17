/**
 * Email audit popup. Appears once per session after 8 seconds (or 45% scroll).
 * Form: web + email -> FormSubmit -> hello@noktostudio.com. GDPR note included.
 * Close on X, overlay click, or Escape. sessionStorage prevents re-showing.
 */
(function () {
  'use strict';

  var SHOWN_KEY = 'auditPopupShown';
  var DELAY_MS = 8000;
  var SCROLL_PCT = 45;

  function endpoint() {
    return 'https://formsubmit.co/ajax/hello@noktostudio.com';
  }

  function build() {
    var overlay = document.createElement('div');
    overlay.className = 'audit-popup-overlay';
    overlay.id = 'auditPopup';
    overlay.innerHTML =
      '<div class="audit-popup" role="dialog" aria-modal="true" aria-label="Bezplatný audit webu">' +
      '  <button class="audit-popup-close" type="button" aria-label="Zavrieť">&times;</button>' +
      '  <div class="ap-form-wrap">' +
      '    <div class="audit-popup-icon">🔍</div>' +
      '    <h3 data-ap-h>Bezplatný audit vášho webu</h3>' +
      '    <p class="ap-sub" data-ap-sub>Napíšte adresu webu a e-mail. Do 3 dní vám pošlem vstupný audit: čo brzdí váš web v Google a čo by SEO mohlo u vás znamenať. Zadarmo, bez záväzku.</p>' +
      '    <form class="ap-form">' +
      '      <div class="ap-field"><input type="url" name="web" placeholder="Adresa vášho webu (https://...)" required></div>' +
      '      <div class="ap-field"><input type="email" name="email" placeholder="Váš e-mail" required></div>' +
      '      <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">' +
      '      <input type="hidden" name="_subject" value="Žiadosť o bezplatný audit (popup)">' +
      '      <button type="submit" class="btn btn-primary">Chcem bezplatný audit</button>' +
      '      <p class="ap-note">Odoslaním súhlasíte so spracovaním e-mailu na účel zaslania auditu. Žiadny spam, žiadny predaj dát.</p>' +
      '    </form>' +
      '  </div>' +
      '  <div class="ap-success"><p>✓ Ďakujeme! Audit vám pošleme do 3 dní na e-mail.</p></div>' +
      '</div>';
    document.body.appendChild(overlay);
    return overlay;
  }

  function show(overlay) {
    overlay.classList.add('open');
    try { sessionStorage.setItem(SHOWN_KEY, '1'); } catch (e) {}
  }

  function init() {
    try {
      if (sessionStorage.getItem(SHOWN_KEY)) return;
    } catch (e) {}
    var overlay = build();

    var closeBtn = overlay.querySelector('.audit-popup-close');
    closeBtn.addEventListener('click', function () { overlay.classList.remove('open'); });
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) overlay.classList.remove('open');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') overlay.classList.remove('open');
    });

    var form = overlay.querySelector('.ap-form-wrap form');
    var wrap = overlay.querySelector('.ap-form-wrap');
    var success = overlay.querySelector('.ap-success');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = form.querySelector('button');
      btn.disabled = true;
      btn.textContent = 'Odosielam...';
      var data = {};
      new FormData(form).forEach(function (v, k) { data[k] = v; });
      fetch(endpoint(), {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify(data)
      }).then(function () {
        wrap.style.display = 'none';
        success.style.display = 'block';
        setTimeout(function () { overlay.classList.remove('open'); }, 6000);
      }).catch(function () {
        btn.disabled = false;
        btn.textContent = 'Chcem bezplatný audit';
        // graceful fallback: mailto
        window.location.href = 'mailto:hello@noktostudio.com?subject=Bezplatný audit (popup)' +
          '&body=Web: ' + encodeURIComponent(data.web || '') + '%0D%0AE-mail: ' + encodeURIComponent(data.email || '');
      });
    });

    var timer = setTimeout(function () { show(overlay); }, DELAY_MS);
    var scrolled = false;
    window.addEventListener('scroll', function () {
      if (scrolled) return;
      var pct = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
      if (pct >= SCROLL_PCT) { scrolled = true; show(overlay); }
    }, { passive: true });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
