// GSAP master timeline for the LinkedIn ad. DOM is static markup baked into
// index.html by scripts/build-ad.mjs from data/ad.json — this file only
// drives the fade + scale-in on every cut and the CTA card's logo/text
// reveal. Deterministic only: no Date.now(), no Math.random(), no network.
(function () {
  var dataEl = document.getElementById('ad-data');
  var data = JSON.parse(dataEl.textContent);
  var tl = gsap.timeline({ paused: true });

  var clips = document.querySelectorAll('.clip.beat');
  clips.forEach(function (el) {
    var start = parseFloat(el.getAttribute('data-start'));
    if (Number.isNaN(start)) return;
    tl.fromTo(el, { opacity: 0, scale: 0.98 }, { opacity: 1, scale: 1, duration: 0.3, ease: 'power1.out' }, start);
  });

  var cta = document.querySelector('.cta-card');
  if (cta) {
    var ctaStart = parseFloat(cta.getAttribute('data-start'));
    var logo = cta.querySelector('.logo');
    var line2 = cta.querySelector('.cta-line2');
    var explain = cta.querySelector('.cta-explain');
    var sub = cta.querySelector('.cta-sub');
    var voAt = data.cta.voFromSeconds;
    var explainAt = data.cta.explainFromSeconds;
    tl.fromTo(logo, { opacity: 0, scale: 0.85 }, { opacity: 1, scale: 1, duration: 0.5, ease: 'back.out(1.6)' }, ctaStart);
    tl.fromTo(line2, { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.4, ease: 'power1.out' }, voAt - 0.2);
    tl.fromTo(explain, { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.4, ease: 'power1.out' }, explainAt - 0.2);
    tl.fromTo(sub, { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.4, ease: 'power1.out' }, explainAt + 0.2);
  }

  tl.duration(data.durationSeconds);
  window.__timelines = window.__timelines || {};
  window.__timelines['ad'] = tl;
})();
