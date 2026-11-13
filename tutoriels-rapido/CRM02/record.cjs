// Enregistre les vrais écrans de RapidoCRM (lancé en local, données fictives)
// au rythme de la voix off, et note la position des zones mises en avant.
// Usage : node record.cjs http://127.0.0.1:8124 demo@rapido.test motdepasse paragraphes.json
//   paragraphes.json = { "intro":0.1, "stats":8.6, ... , "end":55.2 } (débuts de paragraphe, en s)
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const [, , BASE, EMAIL, PASSWORD, PARAS] = process.argv;
const T = JSON.parse(fs.readFileSync(PARAS, 'utf8'));
const OUT = path.join(__dirname, 'captures');
fs.mkdirSync(OUT, { recursive: true });

(async () => {
    const browser = await chromium.launch();
    // 1) Connexion hors enregistrement
    const login = await browser.newContext({ viewport: { width: 1920, height: 1080 } });
    const lp = await login.newPage();
    await lp.goto(`${BASE}/login`, { waitUntil: 'networkidle' });
    await lp.fill('input[name="email"]', EMAIL);
    await lp.fill('input[name="password"]', PASSWORD);
    await Promise.all([lp.waitForNavigation({ waitUntil: 'networkidle' }).catch(() => {}), lp.press('input[name="password"]', 'Enter')]);
    const state = await login.storageState();
    await login.close();

    // 2) Enregistrement
    const ctx = await browser.newContext({ viewport: { width: 1920, height: 1080 }, storageState: state, recordVideo: { dir: OUT, size: { width: 1920, height: 1080 } } });
    const page = await ctx.newPage();
    const t0 = Date.now();
    await page.goto(`${BASE}/dashboard`, { waitUntil: 'networkidle' });
    await page.waitForTimeout(2000); // animations des graphiques
    const ready = (Date.now() - t0) / 1000; // instant de la capture où la voix démarre
    const at = async (s) => { const w = ready + s - (Date.now() - t0) / 1000; if (w > 0) await page.waitForTimeout(w * 1000); };

    // Curseur visible dans la capture (Playwright n'enregistre pas le pointeur système)
    await page.addStyleTag({ content: '#rx-cursor{position:fixed;z-index:99999;width:26px;height:26px;pointer-events:none;transition:transform .08s;background:url("data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 24 24\'%3E%3Cpath d=\'M4 2l16 9-7 2-3 7z\' fill=\'%23111\' stroke=\'white\' stroke-width=\'1.5\'/%3E%3C/svg%3E") no-repeat}' });
    await page.evaluate(() => { const c = document.createElement('div'); c.id = 'rx-cursor'; document.body.appendChild(c); document.addEventListener('mousemove', (e) => { c.style.left = e.clientX + 'px'; c.style.top = e.clientY + 'px'; }); });
    let mouse = { x: 960, y: 540 };
    const moveTo = async (x, y, steps = 30) => { await page.mouse.move(x, y, { steps }); mouse = { x, y }; };
    await moveTo(1100, 500, 1);

    const boxes = {};
    // Fait défiler jusqu'à une section (titre exact) et note la zone titre → section suivante, en coordonnées d'écran.
    const section = async (key, title) => {
        await page.evaluate((title) => {
            const h = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].find((n) => n.textContent.trim() === title);
            if (h) window.scrollTo({ top: h.getBoundingClientRect().top + window.scrollY - 110, behavior: 'smooth' });
        }, title);
        await page.waitForTimeout(1100);
        const box = await page.evaluate((title) => {
            const hs = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].filter((n) => n.offsetParent);
            const i = hs.findIndex((n) => n.textContent.trim() === title);
            if (i < 0) return null;
            const top = hs[i].getBoundingClientRect().top - 12;
            const next = hs.slice(i + 1).find((n) => n.getBoundingClientRect().top > top + 40);
            const bottom = Math.min(next ? next.getBoundingClientRect().top - 24 : window.innerHeight, window.innerHeight - 10);
            const main = hs[i].closest('.container-xxl, .content-wrapper, main') || document.body;
            const r = main.getBoundingClientRect();
            return { x: Math.max(r.left, 300), y: Math.max(top, 0), w: Math.min(r.width, 1920 - Math.max(r.left, 300)), h: bottom - Math.max(top, 0) };
        }, title);
        if (box) boxes[key] = box;
        return box;
    };
    const glide = async (box) => { if (!box) return; await moveTo(box.x + box.w * 0.35, box.y + Math.min(box.h * 0.55, 260)); };

    await at(T.stats);   glide(await section('stats', 'Statistique générale'));
    await at(T.crm);     glide(await section('crm', 'Crm'));
    await at(T.marketing); glide(await section('marketing', 'Marketing'));
    await at(T.commercial); glide(await section('commercial', 'Commercial'));
    await at(T.segmentation); glide(await section('segmentation', 'Segmentation'));

    await at(T.menu);
    await page.evaluate(() => window.scrollTo({ top: 0, behavior: 'smooth' }));
    await page.waitForTimeout(600);
    const menu = {};
    for (const label of ['Clients', 'Pipeline', 'Factures', 'Campagnes']) {
        const el = page.locator('aside a, nav a, .menu-link, .layout-menu a').filter({ hasText: new RegExp(`^\\s*${label}\\s*$`) }).first();
        if (await el.count()) { const b = await el.boundingBox(); if (b) menu[label] = { x: b.x, y: b.y, w: b.width, h: b.height }; }
    }
    boxes.menu = menu;
    for (const [i, label] of ['Clients', 'Pipeline', 'Factures', 'Campagnes'].entries()) {
        const b = menu[label]; if (!b) continue;
        await page.waitForTimeout(i ? 700 : 0);
        await moveTo(b.x + 60, b.y + b.h / 2, 20);
        await page.locator('aside a, nav a, .menu-link, .layout-menu a').filter({ hasText: new RegExp(`^\\s*${label}\\s*$`) }).first().hover().catch(() => {});
    }

    await at(T.outro);
    await moveTo(1100, 520);
    await at(T.end + 0.8);
    await page.screenshot({ path: path.join(OUT, 'fin.png') });

    const video = page.video();
    await ctx.close();
    fs.renameSync(await video.path(), path.join(OUT, 'ecran.webm'));
    fs.writeFileSync(path.join(OUT, 'timing.json'), JSON.stringify({ voiceStartInCapture: ready, paragraphs: T, boxes }, null, 2));
    await browser.close();
    console.log('capture ok — voix à', ready.toFixed(2), 's dans la capture ; zones :', Object.keys(boxes).join(', '));
})();
