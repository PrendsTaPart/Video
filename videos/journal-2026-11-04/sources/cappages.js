const { chromium } = require('playwright');
const OUT = __dirname + '/../src';
const pages = process.argv.slice(2);
(async () => {
  const b = await chromium.launch();
  for (const u of pages) {
    const ctx = await b.newContext({ viewport: { width: 430, height: 900 }, deviceScaleFactor: 2 });
    const p = await ctx.newPage();
    await p.goto('https://foodeatup.com/' + u, { waitUntil: 'networkidle', timeout: 60000 }).catch(e=>console.log('goto',e.message));
    await p.locator('button:has-text("Refuser")').first().click({timeout:3000}).catch(()=>{});
    await p.waitForTimeout(500);
    const h = await p.evaluate(() => document.documentElement.scrollHeight);
    for (let y = 0; y < Math.min(h, 9000); y += 400) { await p.evaluate(v => window.scrollTo(0, v), y); await p.waitForTimeout(200); }
    await p.evaluate(() => document.querySelectorAll('img').forEach(i => { i.loading = 'eager'; }));
    await p.waitForTimeout(2500);
    await p.evaluate(() => window.scrollTo(0, 0)); await p.waitForTimeout(800);
    const n = 'page-' + u.replace(/\//g, '_') + '.png';
    await p.screenshot({ path: `${OUT}/${n}`, fullPage: true });
    require('fs').writeFileSync(`${OUT}/${n}.txt`, await p.evaluate(()=>document.body.innerText));
    console.log(n, h);
    await ctx.close();
  }
  await b.close();
})();
