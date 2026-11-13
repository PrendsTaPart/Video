// Rend une miniature 1280×720 à partir du gabarit miniature.html (aucun service externe).
// Usage : node miniature.cjs --product crm --num CRM02 --title "..." --em "..." --tag "..." [--shot capture.png] --out miniature.png
const path = require('path');
const { pathToFileURL } = require('url');
const { chromium } = require('playwright');
const args = {}; const a = process.argv.slice(2);
for (let i = 0; i < a.length; i += 2) args[a[i].replace(/^--/, '')] = a[i + 1];
(async () => {
  const q = new URLSearchParams();
  for (const k of ['product', 'num', 'title', 'em', 'kicker', 'tag']) if (args[k]) q.set(k, args[k]);
  if (args.shot) q.set('shot', pathToFileURL(path.resolve(args.shot)).href);
  const url = pathToFileURL(path.join(__dirname, 'miniature.html')).href + '?' + q.toString();
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
  await p.goto(url, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(800);
  await p.screenshot({ path: args.out || 'miniature.png' });
  await b.close();
  console.log('miniature →', args.out || 'miniature.png');
})();
