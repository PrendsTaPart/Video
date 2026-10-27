const { chromium } = require('playwright');
(async () => {
  const [mode, ...ns] = process.argv.slice(2);
  const blanc = mode === 'blanc';
  const b = await chromium.launch();
  const base = 'http://127.0.0.1:8820/';
  for (const n of ns.map(Number)) {
    const nn = String(n).padStart(2, '0');
    if (mode === 'cover') {
      const p = await b.newPage({ viewport: { width: 1600, height: 900 } });
      await p.goto(`${base}cover.html?n=${n}`); await p.waitForSelector('body[data-ok]');
      await p.screenshot({ path: `out/covers/formation-${nn}.jpg`, quality: 86 }); await p.close();
    } else {
      const p = await b.newPage();
      await p.goto(`${base}pdf.html?n=${n}${blanc ? '&t=blanc' : ''}`); await p.waitForSelector('body[data-ok]');
      await p.pdf({ path: `out/pdf/formation-${nn}${blanc ? '-blanc' : ''}.pdf`, format: 'A4', printBackground: true, preferCSSPageSize: true,
        displayHeaderFooter: true, headerTemplate: '<span></span>',
        footerTemplate: `<div style="width:100%;font-family:sans-serif;font-size:7pt;color:${blanc ? '#73726C' : '#AEB8C2'};padding:0 15mm;display:flex;justify-content:space-between"><span>Michael Kebail-Ali · Épisode ${n}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>` });
      await p.close();
    }
  }
  await b.close();
})();
