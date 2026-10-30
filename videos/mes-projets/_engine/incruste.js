// node incruste.js <dossier épisode> : lit window.CLIPS de la page et incruste les vidéos du projet dans frames.mp4 (zone P.ECRAN).
const {chromium} = require('playwright'); const {execFileSync} = require('child_process'); const path = require('path'); const fs = require('fs');
(async () => {
  const d = path.resolve(process.argv[2]);
  const b = await chromium.launch(); const p = await b.newPage({viewport: {width: 1080, height: 1920}});
  await p.goto('file://' + d + '/index.html', {waitUntil: 'networkidle'});
  const {clips, E} = await p.evaluate(() => ({clips: window.CLIPS, E: P.ECRAN})); await b.close();
  const inp = ['-i', d + '/frames.mp4'], flt = []; let last = '0:v';
  const M = clips.length + 1;
  clips.forEach(([f]) => inp.push('-i', path.resolve(d, f)));
  inp.push('-loop', '1', '-i', path.join(__dirname, 'masque-ecran.png'));
  flt.push(`[${M}:v]format=gray,split=${clips.length}${clips.map((_, k) => `[m${k}]`).join('')}`);
  clips.forEach(([f, t0, t1, ss, sp], k) => {
    const ln = t1 - t0;
    flt.push(`[${k + 1}:v]trim=${ss}:${ss + ln * sp},setpts=(PTS-STARTPTS)/${sp},scale=${E.w}:${E.h}:force_original_aspect_ratio=increase,crop=${E.w}:${E.h},fps=30[v${k}];[m${k}]fps=30,trim=duration=${ln},setpts=PTS-STARTPTS[mm${k}];` +
      `[v${k}][mm${k}]alphamerge,setpts=PTS+${t0}/TB,fade=t=in:st=${t0}:d=0.25:alpha=1,fade=t=out:st=${t1 - 0.2}:d=0.2:alpha=1[c${k}]`);
    flt.push(`[${last}][c${k}]overlay=${E.x}:${E.y}:eof_action=pass[x${k}]`); last = `x${k}`;
  });
  flt.push(`[${last}]format=yuv420p[v]`);
  execFileSync('ffmpeg', ['-y', '-v', 'error', ...inp, '-filter_complex', flt.join(';'), '-map', '[v]', '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', d + '/frames_ov.mp4'], {stdio: 'inherit'});
  fs.renameSync(d + '/frames_ov.mp4', d + '/frames.mp4'); console.log('incrusté', clips.length, 'clips');
})();
