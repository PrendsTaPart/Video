// node stills.js <dir> t1 t2 ... : planche de contrôle <dir>/stills.png
const {chromium} = require('playwright');
const path = require('path');
(async () => {
  const dir = path.resolve(process.argv[2]);
  const ts = process.argv.slice(3).map(Number);
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 1080, height: 1920}});
  await p.goto('file://' + dir + '/index.html', {waitUntil: 'networkidle'});
  await p.evaluate(() => document.fonts.ready);
  for (const [i, t] of ts.entries()) { await p.evaluate(t => render(t), t); await p.screenshot({path: `${dir}/still-${i}.png`}); }
  await b.close();
})();
