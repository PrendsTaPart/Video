// Enregistreur générique des tutoriels Rapido.
// Usage : node _gabarit/record.cjs <EP> <BASE_URL> <email> <mot_de_passe>
// Lit <EP>/tuto.json (scènes) et <EP>/paragraphes.json (débuts de paragraphe de la voix, en s),
// filme l'application au rythme de la voix et écrit <EP>/captures/{ecran.webm,timing.json,fin.png}.
//
// Une scène (tuto.json → "scenes") :
//   { "at": "clé du paragraphe", "goto": "/chemin" (optionnel), "scroll": "Titre exact" | "css",
//     "eval": "js exécuté dans la page avant le clic", "hover": "css", "click": "css", "fill": [["css","texte"]...], "select": [["css","libellé"]], "drag": ["source","cible"], "wait": 0.8,
//     "zone": "css" | "Titre exact" | [x,y,w,h], "label": "Libellé du chapitre", "zoom": 1.25 }
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const [, , EP, BASE, EMAIL, PASSWORD] = process.argv;
const cfg = JSON.parse(fs.readFileSync(path.join(EP, 'tuto.json'), 'utf8'));
const T = JSON.parse(fs.readFileSync(path.join(EP, 'paragraphes.json'), 'utf8'));
const OUT = path.join(EP, 'captures');
fs.mkdirSync(OUT, { recursive: true });

const CURSOR_CSS = '#rx-cursor{position:fixed;z-index:2147483647;width:28px;height:28px;margin:-3px 0 0 -4px;pointer-events:none;background:url("data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 24 24\'%3E%3Cpath d=\'M4 2l16 9-7 2-3 7z\' fill=\'%23111\' stroke=\'white\' stroke-width=\'1.6\'/%3E%3C/svg%3E") no-repeat}#rx-cursor.down{transform:scale(.85)}';

(async () => {
    const browser = await chromium.launch();
    let state;
    if (!cfg.public) {
        const login = await browser.newContext({ viewport: { width: 1920, height: 1080 } });
        const lp = await login.newPage();
        await lp.goto(`${BASE}${cfg.login_path || '/login'}`, { waitUntil: 'networkidle' });
        await lp.fill(cfg.login_email || 'input[name="email"]', EMAIL);
        await lp.fill(cfg.login_password || 'input[name="password"]', PASSWORD);
        await Promise.all([lp.waitForNavigation({ waitUntil: 'networkidle' }).catch(() => {}), lp.press(cfg.login_password || 'input[name="password"]', 'Enter')]);
        state = await login.storageState();
        await login.close();
    }
    const ctx = await browser.newContext({ viewport: { width: 1920, height: 1080 }, storageState: state, recordVideo: { dir: OUT, size: { width: 1920, height: 1080 } } });
    const page = await ctx.newPage();
    // Remplacement de textes à l'affichage (ex. adresse locale → adresse publique), sans toucher au code de l'application.
    if (cfg.replace_text) {
        await page.addInitScript((pairs) => {
            const fix = (root) => {
                const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
                for (let n = w.nextNode(); n; n = w.nextNode()) {
                    for (const [a, b] of pairs) if (n.nodeValue.includes(a)) n.nodeValue = n.nodeValue.split(a).join(b);
                }
            };
            document.addEventListener('DOMContentLoaded', () => {
                fix(document.body);
                new MutationObserver((ms) => ms.forEach((m) => m.addedNodes.forEach((x) => fix(x.nodeType === 3 ? x.parentNode || document.body : x)))).observe(document.body, { childList: true, subtree: true });
            });
        }, Object.entries(cfg.replace_text));
    }
    const installCursor = async () => {
        await page.addStyleTag({ content: CURSOR_CSS }).catch(() => {});
        await page.evaluate(() => {
            if (document.getElementById('rx-cursor')) return;
            const c = document.createElement('div'); c.id = 'rx-cursor'; document.body.appendChild(c);
            const p = window.__rxMouse || { x: 1100, y: 520 }; c.style.left = p.x + 'px'; c.style.top = p.y + 'px';
            document.addEventListener('mousemove', (e) => { window.__rxMouse = { x: e.clientX, y: e.clientY }; c.style.left = e.clientX + 'px'; c.style.top = e.clientY + 'px'; });
            document.addEventListener('mousedown', () => c.classList.add('down'));
            document.addEventListener('mouseup', () => c.classList.remove('down'));
        }).catch(() => {});
    };
    page.on('load', installCursor);
    // Réponses simulées (IA, services externes) : interceptées dans le navigateur, le code de l'application n'est pas modifié.
    //   "mocks": [{ "url": "**/api/posts/generate_text", "delay": 2.5, "json": {...} | "file": "chemin/local.png" }]
    for (const m of cfg.mocks || []) {
        await page.route(m.url, async (route) => {
            if (m.delay) await new Promise((r) => setTimeout(r, m.delay * 1000));
            if (m.file) return route.fulfill({ path: path.isAbsolute(m.file) ? m.file : path.join(EP, m.file) });
            return route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify(m.json) });
        });
    }

    const t0 = Date.now();
    await page.goto(`${BASE}${cfg.start_path || '/dashboard'}`, { waitUntil: 'networkidle' });
    await installCursor();
    await page.waitForTimeout(1800);
    const ready = (Date.now() - t0) / 1000;
    const at = async (s) => { const w = ready + s - (Date.now() - t0) / 1000; if (w > 0) await page.waitForTimeout(w * 1000); };

    let mouse = { x: 1100, y: 520 };
    await page.mouse.move(mouse.x, mouse.y);
    const moveTo = async (x, y, steps = 28) => { await page.mouse.move(x, y, { steps }); mouse = { x, y }; };

    // Trouve un élément : sélecteur CSS, ou titre / texte exact
    const resolve = async (target) => {
        if (!target || Array.isArray(target)) return null;
        let loc = null;
        try { loc = page.locator(target).first(); if (await loc.count()) return loc; } catch (e) { /* pas un sélecteur valide */ }
        loc = page.locator('main h1,main h2,main h3,main h4,main h5,main h6,.content-wrapper h1,.content-wrapper h2,.content-wrapper h3,.content-wrapper h4,.content-wrapper h5,h1,h2,h3,h4,h5,h6').filter({ hasText: new RegExp(`^\\s*${target.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\\s*$`) }).first();
        if (await loc.count()) return loc;
        loc = page.getByText(target, { exact: true }).first();
        return (await loc.count()) ? loc : null;
    };
    const scrollTo = async (target) => {
        const el = await resolve(target);
        if (!el) return;
        await el.evaluate((n) => window.scrollTo({ top: n.getBoundingClientRect().top + window.scrollY - 120, behavior: 'smooth' }));
        await page.waitForTimeout(1000);
    };
    // Zone d'un titre = du titre jusqu'au titre de même niveau suivant ; zone d'un sélecteur = sa boîte
    const zoneOf = async (z, closest) => {
        if (Array.isArray(z)) return z;
        const el = await resolve(z);
        if (!el) return null;
        const r = await el.evaluate((n, closest) => {
            if (closest && n.closest(closest)) n = n.closest(closest);
            const isH = /^H[1-6]$/.test(n.tagName);
            let rect = n.getBoundingClientRect();
            if (isH) {
                const hs = [...document.querySelectorAll(n.tagName)].filter((h) => h.offsetParent);
                const next = hs.find((h) => h.getBoundingClientRect().top > rect.top + 30);
                const container = n.parentElement.closest('.container-xxl,.container-fluid,.container,.content-wrapper,main') || n.parentElement;
                const c = container.getBoundingClientRect();
                const bottom = next ? next.getBoundingClientRect().top - 16 : Math.min(c.bottom, window.innerHeight);
                return [c.left, rect.top - 10, c.width, bottom - rect.top + 10];
            }
            return [rect.left, rect.top, rect.width, rect.height];
        }, closest || null);
        let [x, y, w, h] = r.map((v) => Math.round(v));
        const pad = 14; x -= pad; y -= pad; w += 2 * pad; h += 2 * pad;
        x = Math.max(0, x); y = Math.max(0, y); w = Math.min(w, 1920 - x); h = Math.min(h, 1080 - y);
        return h > 20 && w > 20 ? [x, y, w, h] : null;
    };

    const zones = {};
    for (const sc of cfg.scenes) {
        await at(T[sc.at]);
        if (sc.goto) { await page.goto(`${BASE}${sc.goto}`, { waitUntil: 'load', timeout: 15000 }).catch(() => {}); await page.waitForLoadState('networkidle', { timeout: 1500 }).catch(() => {}); await installCursor(); await page.waitForTimeout(900); }
        if (sc.eval) await page.evaluate(sc.eval).catch((e) => console.warn('eval', e.message));
        if (sc.click) {
            const el = await resolve(sc.click);
            if (el) { await el.scrollIntoViewIfNeeded().catch(() => {}); const b = await el.boundingBox(); if (b) await moveTo(b.x + Math.min(b.width / 2, 120), b.y + b.height / 2); await page.waitForTimeout(250); await el.click().catch(() => {}); await page.waitForLoadState('networkidle', { timeout: 1500 }).catch(() => {}); await installCursor(); await page.waitForTimeout(800); }
        }
        if (sc.top) { await page.evaluate(() => window.scrollTo({ top: 0, behavior: 'smooth' })); await page.waitForTimeout(700); }
        if (sc.scroll) await scrollTo(sc.scroll);
        for (const [sel, txt] of sc.fill || []) {
            const el = await resolve(sel); if (!el) continue;
            const b = await el.boundingBox(); if (b) await moveTo(b.x + 30, b.y + b.height / 2);
            const typ = await el.getAttribute('type');
            if (typ === 'date' || typ === 'datetime-local' || typ === 'time') { await el.fill(txt).catch(() => {}); await page.waitForTimeout(400); continue; }
            await el.click().catch(() => {}); await el.fill('').catch(() => {});
            await el.pressSequentially(txt, { delay: cfg.type_delay || 45 }).catch(() => {});
            await page.waitForTimeout(250);
        }
        for (const [sel, label] of sc.select || []) {
            const el = await resolve(sel); if (!el) continue;
            const b = await el.boundingBox(); if (b) await moveTo(b.x + 40, b.y + b.height / 2);
            await page.waitForTimeout(250); await el.selectOption({ label }).catch(() => {}); await page.waitForTimeout(400);
        }
        if (sc.drag) { // glisser-déposer : [source, cible] (sélecteurs CSS)
            const a = await resolve(sc.drag[0]), z = await resolve(sc.drag[1]);
            const ba = a && await a.boundingBox(), bz = z && await z.boundingBox();
            if (ba && bz) {
                await moveTo(ba.x + ba.width / 2, ba.y + 30); await page.mouse.down(); await page.waitForTimeout(300);
                await moveTo(ba.x + ba.width / 2 + 20, ba.y + 50, 8);
                await moveTo(bz.x + bz.width / 2, bz.y + Math.min(bz.height / 2, 120), 40); await page.waitForTimeout(300);
                await page.mouse.up(); await page.waitForLoadState('networkidle', { timeout: 1500 }).catch(() => {}); await page.waitForTimeout(600);
            }
        }
        if (sc.hover) { const el = await resolve(sc.hover); if (el) { await el.evaluate((n) => { const r = n.getBoundingClientRect(); if (r.top < 90 || r.bottom > window.innerHeight - 40) window.scrollBy({ top: r.top - window.innerHeight / 2, behavior: 'smooth' }); }); await page.waitForTimeout(700); const b = await el.boundingBox(); if (b) await moveTo(b.x + Math.min(b.width / 2, 120), b.y + b.height / 2); } }
        if (sc.wait) await page.waitForTimeout(sc.wait * 1000);
        if (sc.zone) { const z = await zoneOf(sc.zone, sc.zone_closest); if (z) zones[sc.at] = z; }
        const lag = (Date.now() - t0) / 1000 - ready - T[sc.at]; if (lag > 4) console.warn(`retard scène ${sc.at} : ${lag.toFixed(1)} s`);
        if (!sc.hover && !sc.click && zones[sc.at]) { const [x, y, w, h] = zones[sc.at]; await moveTo(x + w * 0.45, y + Math.min(h * 0.5, 300)); }
    }
    await at(T.end + 0.8);
    await page.evaluate(() => window.scrollTo({ top: 0 })).catch(() => {});
    await page.waitForTimeout(300);
    await page.screenshot({ path: path.join(OUT, 'fin.png') });
    const video = page.video();
    await ctx.close();
    fs.renameSync(await video.path(), path.join(OUT, 'ecran.webm'));
    fs.writeFileSync(path.join(OUT, 'timing.json'), JSON.stringify({ voiceStartInCapture: ready, paragraphs: T, zones }, null, 2));
    await browser.close();
    console.log(`capture ok — voix à ${ready.toFixed(2)} s ; zones mesurées : ${Object.keys(zones).join(', ') || 'aucune'}`);
})();
