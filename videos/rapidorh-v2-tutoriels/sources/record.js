// Filme un épisode sur le produit réel (serveur local, données fictives), synchronisé
// avec les durées de narration. Usage : node record.js RHV2-01 [durees.json]
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const EP = require('./episodes')[process.argv[2]];
const ID = process.argv[2];
const OUT = path.join(__dirname, 'out', ID);
const BASE = 'http://127.0.0.1:8000';
const durations = process.argv[3] ? JSON.parse(fs.readFileSync(process.argv[3], 'utf8')) : EP.segments.map(() => 4);

const CURSOR = `
  (() => { const add = () => { if (document.getElementById('tuto-cursor')) return;
    const c = document.createElement('div'); c.id = 'tuto-cursor';
    c.style.cssText = 'position:fixed;z-index:2147483647;width:22px;height:22px;margin:-11px 0 0 -11px;border-radius:50%;background:rgba(123,97,196,.35);border:2px solid #7B61C4;pointer-events:none;transition:transform .12s;left:-50px;top:-50px';
    document.documentElement.appendChild(c);
    addEventListener('mousemove', e => { c.style.left = e.clientX + 'px'; c.style.top = e.clientY + 'px'; }, true);
    addEventListener('mousedown', () => { c.style.transform = 'scale(.7)'; }, true);
    addEventListener('mouseup', () => { c.style.transform = 'scale(1)'; }, true);
    const s = document.createElement('style'); s.textContent = '.debugbar, .phpdebugbar, .chat-assistant { display:none !important }'; document.documentElement.appendChild(s); };
    document.readyState === 'loading' ? addEventListener('DOMContentLoaded', add) : add(); })();`;

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch();
  // Connexion hors caméra.
  const login = await browser.newContext({ viewport: { width: 1280, height: 720 } });
  const lp = await login.newPage();
  await lp.goto(BASE + '/login');
  await lp.fill('input[name=email]', 'camille@studio-demo.test'); await lp.fill('input[name=password]', 'Demo-Tuto-2026!');
  await Promise.all([lp.waitForNavigation(), lp.click('button[type=submit]')]);
  const state = await login.storageState(); await login.close();

  const t_ctx = Date.now();
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 720 }, storageState: state, recordVideo: { dir: OUT, size: { width: 1280, height: 720 } }, locale: 'fr-FR', timezoneId: 'Europe/Paris' });
  await ctx.addInitScript(CURSOR);
  const page = await ctx.newPage();
  const errs = []; page.on('pageerror', e => errs.push(e.message));
  let mouse = { x: 640, y: 360 };
  const moveTo = async (loc) => {
    await loc.scrollIntoViewIfNeeded();
    const b = await loc.boundingBox(); if (!b) return;
    const x = b.x + Math.min(b.width / 2, 60), y = b.y + b.height / 2;
    await page.mouse.move(x, y, { steps: 18 }); mouse = { x, y }; await page.waitForTimeout(150);
  };
  const h = {
    go: async (u) => { await page.goto(BASE + u, { waitUntil: 'networkidle' }); await page.mouse.move(mouse.x, mouse.y); },
    wait: (s) => page.waitForSelector(s, { timeout: 15000 }),
    pause: (ms) => page.waitForTimeout(ms),
    click: async (s) => { const l = page.locator(s).first(); await moveTo(l); await l.click(); },
    clickText: async (t) => { const l = page.getByText(t, { exact: false }).first(); await moveTo(l); await l.click(); },
    hover: async (s) => { const l = page.locator(s).first(); await moveTo(l); await l.hover(); },
    check: async (s) => { const l = page.locator(s).first(); await moveTo(l); await l.check(); },
    select: async (s, v) => { const l = page.locator(s).first(); await moveTo(l); await l.selectOption(v); },
    type: async (s, txt) => { const l = page.locator(s).first(); await moveTo(l); await l.click(); await l.press('Control+a'); await page.keyboard.type(txt, { delay: 35 }); },
    typeIn: async (s, txt) => { const l = page.locator(s).first(); await moveTo(l); await l.click(); await page.keyboard.type(txt, { delay: 35 }); },
    typeKeys: (txt) => page.keyboard.type(txt, { delay: 45 }),
    fill: (s, v) => page.locator(s).first().fill(v),
    upload: async (s, file) => { const l = page.locator(s).first(); await moveTo(l); await l.setInputFiles(path.join(__dirname, file)); },
    press: (k) => page.keyboard.press(k),
    scrollIn: (s, px) => page.locator(s).first().evaluate((el, d) => el.scrollBy({ top: d, behavior: 'smooth' }), px),
    scrollTo: async (s) => { await page.locator(s).first().scrollIntoViewIfNeeded(); await page.waitForTimeout(400); },
  };
  await page.goto(BASE + '/dashboard', { waitUntil: 'networkidle' });
  const t0 = Date.now(); // début de la narration
  let target = 0; const marks = [];
  for (let i = 0; i < EP.segments.length; i++) {
    const start = (Date.now() - t0) / 1000;
    try { await EP.segments[i].a(h); } catch (e) { errs.push(`segment ${i + 1}: ${e.message.split('\n')[0]}`); }
    target += durations[i];
    const left = target * 1000 - (Date.now() - t0);
    if (left > 0) await page.waitForTimeout(left);
    marks.push({ i, start, end: (Date.now() - t0) / 1000 });
  }
  await page.waitForTimeout(600);
  const video = page.video(); await ctx.close();
  const src = await video.path();
  fs.renameSync(src, path.join(OUT, 'capture.webm'));
  fs.writeFileSync(path.join(OUT, 'capture.json'), JSON.stringify({ offset: (t0 - t_ctx) / 1000, marks, errs }, null, 1));
  await browser.close();
  console.log(JSON.stringify({ id: ID, offset: (t0 - t_ctx) / 1000, total: marks.at(-1).end, errs }));
})().catch(e => { console.error(e); process.exit(1); });
