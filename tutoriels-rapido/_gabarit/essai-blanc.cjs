// Essai à blanc d'un tutoriel : vérifie chaque sélecteur des scènes de <EP>/tuto.json, sans voix ni vidéo.
// Usage : node _gabarit/essai-blanc.cjs <EP> <BASE_URL> [email] [mot_de_passe]
// Affiche, scène par scène, les cibles introuvables (click, hover, scroll, zone, fill, select, goto)
// et le temps de chargement de la première page. Code de sortie 1 si une cible manque.
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const [, , EP, BASE, EMAIL = 'demo@rapido.test', PASSWORD = 'Demo-Rapido-2026'] = process.argv;
const cfg = JSON.parse(fs.readFileSync(path.join(EP, 'tuto.json'), 'utf8'));

(async () => {
    const browser = await chromium.launch({ args: ['--lang=fr-FR'] });
    const ctx = await browser.newContext({ viewport: { width: 1920, height: 1080 }, locale: 'fr-FR', timezoneId: 'Europe/Paris' });
    const page = await ctx.newPage();
    if (!cfg.public) {
        await page.goto(`${BASE}${cfg.login_path || '/login'}`, { waitUntil: 'load' });
        await page.fill(cfg.login_email || 'input[name="email"]', EMAIL);
        await page.fill(cfg.login_password || 'input[name="password"]', PASSWORD);
        await Promise.all([page.waitForNavigation({ waitUntil: 'load' }).catch(() => {}), page.press(cfg.login_password || 'input[name="password"]', 'Enter')]);
    }
    for (const m of cfg.mocks || []) {
        await page.route(m.url, (route) => (m.file ? route.fulfill({ path: path.isAbsolute(m.file) ? m.file : path.join(EP, m.file) })
            : route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify(m.json) })));
    }
    const t = Date.now();
    await page.goto(`${BASE}${cfg.start_path || '/dashboard'}`, { waitUntil: 'load' });
    const idle = await page.waitForLoadState('networkidle', { timeout: 20000 }).then(() => true).catch(() => false);
    console.log(`page de départ ${cfg.start_path} : ${((Date.now() - t) / 1000).toFixed(1)} s, réseau au repos : ${idle ? 'oui' : 'NON (cause probable de TimeoutError)'} — URL ${page.url()}`);

    const resolve = async (target) => {
        if (!target || Array.isArray(target)) return true;
        try { const l = page.locator(target).first(); if (await l.count()) return l; } catch (e) { /* texte */ }
        const esc = target.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        let l = page.locator('h1,h2,h3,h4,h5,h6').filter({ hasText: new RegExp(`^\\s*${esc}\\s*$`) }).first();
        if (await l.count()) return l;
        l = page.getByText(target, { exact: true }).first();
        return (await l.count()) ? l : null;
    };
    let manquants = 0;
    for (const [i, sc] of cfg.scenes.entries()) {
        if (sc.goto) { await page.goto(/^https?:/.test(sc.goto) ? sc.goto : `${BASE}${sc.goto}`, { waitUntil: 'load', timeout: 15000 }).catch((e) => console.log(`  ✗ scène ${i} goto ${sc.goto} : ${e.message.split('\n')[0]}`)); await page.waitForTimeout(800); }
        const cibles = [['click', sc.click], ['hover', sc.hover], ['scroll', sc.scroll], ['zone', sc.zone],
            ...(sc.fill || []).map(([s]) => ['fill', s]), ...(sc.fill_now || []).map(([s]) => ['fill_now', s]), ...(sc.select || []).map(([s]) => ['select', s])];
        for (const [k, c] of cibles) {
            if (!c) continue;
            const el = await resolve(c);
            const vis = el && el !== true ? await el.isVisible().catch(() => false) : true;
            if (!el) { manquants++; console.log(`  ✗ scène ${i} (${sc.at}) ${k} introuvable : ${c}`); }
            else if (!vis) console.log(`  ~ scène ${i} (${sc.at}) ${k} présent mais masqué : ${c}`);
        }
        if (sc.eval) await page.evaluate(sc.eval).catch(() => {});
        // Saisies : faites d'un coup (pas de frappe animée) pour que la suite du scénario soit dans le bon état.
        for (const [sel, txt] of [...(sc.fill || []), ...(sc.fill_now || [])]) { const el = await resolve(sel); if (el && el !== true) await el.fill(txt).catch(() => {}); }
        for (const [sel, label] of sc.select || []) { const el = await resolve(sel); if (el && el !== true) await el.selectOption(typeof label === 'object' ? label : { label }).catch(() => {}); }
        for (const [sel, fichier] of sc.upload || []) { const el = await resolve(sel); if (el && el !== true) await el.setInputFiles(path.isAbsolute(fichier) ? fichier : path.join(EP, fichier)).catch((e) => console.warn('upload', e.message)); }
        if (sc.click) { const el = await resolve(sc.click); if (el && el !== true) { await el.click({ timeout: 5000 }).catch((e) => console.log(`  ✗ scène ${i} clic impossible : ${e.message.split('\n')[0]}`)); await page.waitForLoadState('networkidle', { timeout: 3000 }).catch(() => {}); await page.waitForTimeout(500); } }
        if (sc.scroll) { const el = await resolve(sc.scroll); if (el && el !== true) await el.scrollIntoViewIfNeeded().catch(() => {}); }
    }
    console.log(manquants ? `${manquants} cible(s) introuvable(s)` : 'toutes les cibles sont trouvées');
    await browser.close();
    process.exit(manquants ? 1 : 0);
})();
