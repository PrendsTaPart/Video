const path = require('path');
const { chromium } = require(path.join(process.env.GROOT, 'playwright'));
(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox', '--force-color-profile=srgb'] });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve(__dirname, 'teaser.html'));
  await page.evaluate(async () => { await document.fonts.ready; });
  const N = 450, FPS = 30;
  for (let i = 0; i < N; i++) {
    await page.evaluate((t) => window.render(t), i / FPS);
    await page.screenshot({ path: path.join(__dirname, 'work/frames', `f${String(i).padStart(4,'0')}.png`),
      clip: { x: 0, y: 0, width: 1920, height: 1080 } });
    if (i % 90 === 0) console.log('frame', i);
  }
  await browser.close();
  console.log('DONE', N, 'frames');
})().catch(e => { console.error(e); process.exit(1); });
