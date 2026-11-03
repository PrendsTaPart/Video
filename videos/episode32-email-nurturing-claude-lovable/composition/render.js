// node render.js <dir> [fps] [from] [to] : rend <dir>/frames.mp4 (sans son) et <dir>/thumb.png
const {chromium} = require('playwright');
const {spawn} = require('child_process');
const path = require('path');
(async () => {
  const dir = path.resolve(process.argv[2]), fps = +(process.argv[3] || 30);
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 1080, height: 1920}});
  await p.goto('file://' + dir + '/index.html', {waitUntil: 'networkidle'});
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(800);
  const dur = await p.evaluate(() => window.CFG.dur);
  const from = +(process.argv[4] || 0), to = +(process.argv[5] || dur);
  await p.evaluate(() => thumb());
  await p.screenshot({path: dir + '/thumb.png'});
  if (process.argv[6] === 'thumb') { await b.close(); return; }
  const ff = spawn('ffmpeg', ['-y', '-v', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p', dir + '/frames.mp4'], {stdio: ['pipe', 'inherit', 'inherit']});
  const n = Math.round((to - from) * fps);
  for (let i = 0; i < n; i++) {
    await p.evaluate(t => render(t), from + i / fps);
    const buf = await p.screenshot({type: 'jpeg', quality: 92});
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (i % 300 === 0) console.log(dir.split('/').pop(), i, '/', n);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  await b.close();
})();
