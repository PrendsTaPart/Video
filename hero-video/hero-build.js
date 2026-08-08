// Builds the DOM for the hero composition from the embedded #hero-data JSON
// (data/hero.json, inlined into index.html at build time) and registers the
// GSAP master timeline HyperFrames expects on window.__timelines.
// Deterministic only: no Date.now(), no Math.random(), no network fetch —
// the timeline data lives inline in the page, it is never fetched.
(function () {
  var dataEl = document.getElementById('hero-data');
  var data = JSON.parse(dataEl.textContent);
  var stage = document.getElementById('hero');

  var STATE_CLASS = { avec: 'seq-avec', sans: 'seq-sans', neutre: 'seq-neutre' };
  var trackCounter = 0;

  function el(tag, cls, attrs) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (attrs) {
      for (var k in attrs) {
        if (attrs[k] !== undefined && attrs[k] !== null) e.setAttribute(k, attrs[k]);
      }
    }
    return e;
  }

  function addClip(parent, opts) {
    var cls = 'clip' + (opts.cls ? ' ' + opts.cls : '');
    var c = el('div', cls, {
      'data-start': opts.start,
      'data-duration': opts.duration,
      'data-track-index': opts.track
    });
    parent.appendChild(c);
    return c;
  }

  function addAudio(parent, file, start, duration, track) {
    var a = el('audio', 'clip', {
      src: file,
      'data-start': start,
      'data-duration': duration,
      'data-track-index': track,
      'data-volume': '1',
      'data-has-audio': 'true',
      preload: 'auto'
    });
    parent.appendChild(a);
    return a;
  }

  function buildMotionGraphic(key, beat) {
    if (key === 'carton-texte') {
      var card = el('div', 'card opening');
      var h1 = el('h1');
      h1.textContent = beat.text || '';
      card.appendChild(h1);
      return card;
    }
    if (key === 'convergence-multicanal') {
      var stg = el('div', 'converge-stage');
      var labels = ['QR Table 7', 'Site web', 'Agent vocal', 'Livraison'];
      var corners = ['tl', 'tr', 'bl', 'br'];
      corners.forEach(function (c, i) {
        var node = el('div', 'converge-node', { 'data-corner': c });
        node.textContent = labels[i];
        stg.appendChild(node);
      });
      var line = el('div', 'converge-line');
      line.textContent = 'Une seule file';
      stg.appendChild(line);
      return stg;
    }
    if (key === 'notification-cascade-iris') {
      var stg2 = el('div', 'iris-stage');
      for (var s = 1; s <= 3; s++) {
        var dev = el('div', 'iris-device', { 'data-slot': String(s) });
        var toast = el('div', 'toast');
        toast.textContent = 'Saumon ce soir — Iris';
        dev.appendChild(toast);
        stg2.appendChild(dev);
      }
      return stg2;
    }
    if (key === 'noir') {
      return el('div', 'black-frame');
    }
    if (key === 'logo-cta') {
      var ctaCard = el('div', 'cta-card');
      var logo = el('img', 'logo', { src: (beat.source && beat.source.logo) || 'assets/brand/foodeatup-logo-mascot.png', alt: 'FoodEatUp' });
      var slogan = el('div', 'slogan');
      slogan.textContent = beat.text || '';
      var cta = el('div', 'cta');
      cta.textContent = beat.cta || '';
      ctaCard.appendChild(logo);
      ctaCard.appendChild(slogan);
      ctaCard.appendChild(cta);
      return ctaCard;
    }
    if (key === 'trois-visages-silence') {
      var wrap = el('div', 'triptych');
      ['assets/video/hero-portrait-chef.mp4', 'assets/video/hero-portrait-serveur.mp4', 'assets/video/hero-portrait-directeur.mp4'].forEach(function (src) {
        var panel = el('div', 'panel');
        var v = el('video', null, { src: src, muted: 'muted', autoplay: 'true', playsinline: 'true' });
        panel.appendChild(v);
        wrap.appendChild(panel);
      });
      return wrap;
    }
    var fallback = el('div');
    fallback.style.position = 'absolute';
    fallback.style.inset = '0';
    fallback.style.background = '#111';
    return fallback;
  }

  function renderMedia(parent, beat, track) {
    var src = beat.source;
    var keys = Array.isArray(src.key) ? src.key : [src.key];

    if (keys.length > 1) {
      var clip = addClip(parent, { start: beat.fromSeconds, duration: beat.durationSeconds, track: track });
      var tri = el('div', 'triptych');
      keys.forEach(function (k) {
        var panel = el('div', 'panel');
        var v = el('video', null, { src: k, muted: 'muted', autoplay: 'true', playsinline: 'true' });
        panel.appendChild(v);
        tri.appendChild(panel);
      });
      clip.appendChild(tri);
      return;
    }

    var key = keys[0];
    var isVideo = /\.mp4$/i.test(key);
    var clip2 = addClip(parent, { start: beat.fromSeconds, duration: beat.durationSeconds, track: track, cls: 'media-fill' });
    var mediaEl = isVideo
      ? el('video', null, {
          src: key,
          muted: 'muted',
          autoplay: 'true',
          playsinline: 'true',
          'data-media-start': (src.mediaStartSeconds || 0)
        })
      : el('img', null, { src: key, alt: '' });
    clip2.appendChild(mediaEl);
  }

  function renderBeat(parent, beat, track) {
    var src = beat.source;
    if (src) {
      if (src.kind === 'footage' || src.kind === 'image') {
        renderMedia(parent, beat, track);
      } else if (src.kind === 'motion') {
        var clip = addClip(parent, { start: beat.fromSeconds, duration: beat.durationSeconds, track: track });
        clip.appendChild(buildMotionGraphic(src.key, beat));
      }
    }

    if (beat.speaker && beat.speaker !== 'narratrice') {
      var tag = addClip(parent, { start: beat.fromSeconds, duration: beat.durationSeconds, track: track + 500, cls: 'speaker-tag' });
      tag.textContent = beat.speaker;
    }

    if (beat.vo && beat.vo.text) {
      var sub = addClip(parent, { start: beat.fromSeconds, duration: beat.durationSeconds, track: track + 1000, cls: 'subtitle' });
      var span = el('span');
      span.textContent = beat.vo.subtitleFr || beat.vo.text;
      sub.appendChild(span);

      if (beat.vo.file) {
        addAudio(parent, beat.vo.file, beat.fromSeconds, beat.durationSeconds, track + 2000);
      }
    }
  }

  data.sequences.forEach(function (seq) {
    var seqWrap = el('div', STATE_CLASS[seq.state] || 'seq-avec');
    seqWrap.style.position = 'absolute';
    seqWrap.style.inset = '0';
    seqWrap.setAttribute('data-sequence-id', seq.id);
    stage.appendChild(seqWrap);

    seq.beats.forEach(function (beat) {
      var track = trackCounter++;
      renderBeat(seqWrap, beat, track);
    });
  });

  // --- The blue wipe (sans -> avec) and the grey snap (avec -> sans) ---
  // Single source of progress per occurrence, driving the line position AND
  // the desaturation removal together, per brief §5 "useWipeProgress".
  (data.wipe.sansToAvec.atSeconds || []).forEach(function (t, i) {
    var overlay = addClip(stage, {
      start: t - data.wipe.sansToAvec.durationSeconds / 2,
      duration: data.wipe.sansToAvec.durationSeconds,
      track: 9000 + i,
      cls: 'wipe-sweep'
    });
    overlay.appendChild(el('div', 'line'));
    overlay.setAttribute('data-wipe-kind', 'sans-to-avec');
  });

  (data.wipe.avecToSans.atSeconds || []).forEach(function (t, i) {
    var overlay = addClip(stage, {
      start: t - data.wipe.avecToSans.durationSeconds / 2,
      duration: data.wipe.avecToSans.durationSeconds,
      track: 9100 + i,
      cls: 'wipe-sweep snap-sweep'
    });
    overlay.appendChild(el('div', 'line'));
    overlay.setAttribute('data-wipe-kind', 'avec-to-sans');
  });

  // --- The "clin" (pass bell) — exactly 3 occurrences, per brief rule ---
  if (data.clin && data.clin.file) {
    (data.clin.atSeconds || []).forEach(function (t, i) {
      addAudio(stage, data.clin.file, t, 1.2, 9200 + i);
    });
  }

  // --- Music beds, one per sequence, matched to its avec/sans/resolution state ---
  if (data.musicBeds) {
    data.sequences.forEach(function (seq) {
      var bedKey = seq.music === 'silence' ? null : seq.music;
      var bed = bedKey && data.musicBeds[bedKey];
      if (bed) {
        addAudio(stage, bed.file, seq.fromSeconds, seq.durationSeconds, 9300 + trackCounter++);
      }
    });
  }

  // --- Punctual SFX cues (scanner, printer, Jarvis chimes, Iris) ---
  (data.sfxCues || []).forEach(function (cue, i) {
    addAudio(stage, cue.file, cue.atSeconds, 1.5, 9400 + i);
  });

  // --- GSAP master timeline, registered per HyperFrames convention ---
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
