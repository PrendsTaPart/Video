// usage: node render.js outDir from to [times...]
const { chromium } = require('playwright');
(async () => {
  const [out, from, to, ...times] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({viewport:{width:1080,height:1920}});
  await p.goto('http://127.0.0.1:8781/index.html'); await p.evaluate(()=>document.fonts.ready);
  await p.waitForTimeout(500);
  const list = times.length ? times.map(Number) : null;
  if (list) { for (const t of list) { if (t<0) await p.evaluate(()=>thumb()); else await p.evaluate(t=>render(t), t); await p.waitForTimeout(150); await p.screenshot({path:`${out}/t${t}.jpg`, quality:85}); } }
  else { for (let f=+from; f<+to; f++) { await p.evaluate(t=>render(t), f/30); await p.screenshot({path:`${out}/${String(f).padStart(5,'0')}.jpg`, quality:92}); } }
  await b.close();
})();
