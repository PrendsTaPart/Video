// GSAP master timeline for the hero composition. The DOM itself (all clips,
// subtitles, audio elements) is now static markup baked into index.html by
// scripts/build-static.mjs from data/hero.json — this file only drives the
// animated bits: the blue wipe / grey snap progress variable, and the two
// motion-graphic beats (multi-canal convergence, Iris notification cascade).
// Deterministic only: no Date.now(), no Math.random(), no network fetch.
(function () {
  var dataEl = document.getElementById('hero-data');
  var data = JSON.parse(dataEl.textContent);
  var stage = document.getElementById('hero');

  var tl = gsap.timeline({ paused: true });

  data.wipe.sansToAvec.atSeconds.forEach(function (t) {
    tl.fromTo(
      stage,
      { '--wipe-progress': 0 },
      { '--wipe-progress': 1, duration: data.wipe.sansToAvec.durationSeconds, ease: 'power2.inOut' },
      t - data.wipe.sansToAvec.durationSeconds / 2
    );
  });
  data.wipe.avecToSans.atSeconds.forEach(function (t) {
    tl.fromTo(
      stage,
      { '--wipe-progress': 1 },
      { '--wipe-progress': 0, duration: data.wipe.avecToSans.durationSeconds, ease: 'none' },
      t - data.wipe.avecToSans.durationSeconds / 2
    );
  });

  // Beat A convergence: four nodes slide to the centre pill, back.out(1.4), 900ms.
  var beatA = document.querySelector('.converge-stage');
  if (beatA) {
    var nodes = beatA.querySelectorAll('.converge-node');
    var line = beatA.querySelector('.converge-line');
    var beatAStart = 100; // s4-beatA-multicanal fromSeconds
    tl.to(nodes, { opacity: 0, scale: 0.7, duration: 0.9, ease: 'back.in(1.4)', stagger: 0.05 }, beatAStart + 4);
    tl.to(line, { opacity: 1, scale: 1, duration: 0.9, ease: 'back.out(1.4)' }, beatAStart + 4.1);
  }

  // Beat D notification cascade: three toasts arriving in sequence, 1.5s total.
  var toasts = document.querySelectorAll('.iris-device .toast');
  if (toasts.length) {
    var beatDStart = 134; // s4-beatD-iris fromSeconds
    toasts.forEach(function (toast, i) {
      tl.to(toast, { opacity: 1, y: 0, duration: 0.4, ease: 'power2.out' }, beatDStart + 1 + i * 0.5);
    });
  }

  tl.duration(data.durationSeconds);
  window.__timelines = window.__timelines || {};
  window.__timelines['hero'] = tl;
})();
