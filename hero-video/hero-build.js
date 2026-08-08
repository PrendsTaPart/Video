// GSAP master timeline for the hero composition. The DOM itself (all clips,
// audio elements) is static markup baked into index.html by
// scripts/build-static.mjs from data/hero.json — this file only drives the
// animated bits: the blue wipe / grey snap progress variable, the generic
// beat-to-beat motion-design transition, and the two motion-graphic beats
// (multi-canal convergence, Iris notification cascade).
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

  // --- Generic motion-design transition on every cut ---
  // A soft fade + gentle scale-in on every timed clip (video/image/motion
  // graphic), never a fondu au blanc / zoom transition / glitch / wipe
  // circulaire / effet de particules — those are explicitly ruled out.
  // Audio and the signature wipe overlays run their own animation and are
  // excluded here.
  var bt = data.beatTransition || { durationSeconds: 0.35, easing: 'power1.out', scaleFrom: 0.98 };
  var clips = document.querySelectorAll('.clip');
  clips.forEach(function (el) {
    if (el.tagName === 'AUDIO' || el.classList.contains('wipe-sweep')) return;
    var start = parseFloat(el.getAttribute('data-start'));
    if (Number.isNaN(start)) return;
    tl.fromTo(
      el,
      { opacity: 0, scale: bt.scaleFrom },
      { opacity: 1, scale: 1, duration: bt.durationSeconds, ease: bt.easing },
      start
    );
  });

  // Beat A convergence: icons slide from the corners into the FoodEatUp
  // mark, back.out(1.4), 900ms. Two `.converge-stage` instances exist (the
  // narratrice's setup beat, then the real beatA) — only the second, real
  // one animates; the first sits static as a calm establishing frame.
  var convergeStages = document.querySelectorAll('.converge-stage');
  var beatA = convergeStages[convergeStages.length - 1];
  if (beatA) {
    var nodes = beatA.querySelectorAll('.converge-node');
    var target = beatA.querySelector('.converge-target');
    var beatAAnimStart = 107.8; // late in s4-beatA-multicanal (101.8 -> 112), lands before the beat ends
    tl.to(nodes, { opacity: 0, scale: 0.7, duration: 0.9, ease: 'back.in(1.4)', stagger: 0.08 }, beatAAnimStart);
    tl.to(target, { opacity: 1, scale: 1, duration: 0.9, ease: 'back.out(1.4)' }, beatAAnimStart + 0.15);
  }

  // Beat D notification cascade: three badges arriving in sequence.
  var toasts = document.querySelectorAll('.iris-device .toast');
  if (toasts.length) {
    var beatDStart = 134; // s4-beatD-iris fromSeconds
    toasts.forEach(function (toast, i) {
      tl.to(toast, { opacity: 1, y: 0, scale: 1, duration: 0.4, ease: 'back.out(2)' }, beatDStart + 1 + i * 0.5);
    });
  }

  tl.duration(data.durationSeconds);
  window.__timelines = window.__timelines || {};
  window.__timelines['hero'] = tl;
})();
