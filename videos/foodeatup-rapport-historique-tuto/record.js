const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const context = await browser.newContext({
    viewport: { width: 1280, height: 720 },
    recordVideo: {
      dir: __dirname + '/work/rec',
      size: { width: 1280, height: 720 },
    },
  });
  const page = await context.newPage();
  const file = 'file://' + path.resolve(__dirname, 'scene.html');
  await page.goto(file);
  await page.waitForTimeout(42000);
  await context.close();
  await browser.close();
  console.log('done');
})();
