const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 650, height: 620 } });
  for (const i of [1,2,3]) { await p.goto('file:///home/user/rapido-crm-film/public/assets/img/demo/newsletter-'+i+'.html'); await p.screenshot({ path: '/home/user/rapido-crm-film/public/assets/img/demo/newsletter-'+i+'.png' }); }
  await b.close(); })();
