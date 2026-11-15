// Recette visuelle avant tournage : chaque écran filmé est vérifié à la taille de capture (1920×1080)
// et en mobile (390 px) — défilement horizontal, éléments qui sortent de leur conteneur, texte coupé,
// erreurs JavaScript. Usage : node _gabarit/qa-ecrans.cjs <BASE> <email> <mdp> /chemin1 /chemin2 …
// Sortie : liste des problèmes (code 1 s'il y en a) + captures dans /tmp/qa-ecrans/.
const { chromium } = require('playwright');
const fs = require('fs');
const [, , BASE, EMAIL, PASS, ...PATHS] = process.argv;
(async () => {
    fs.mkdirSync('/tmp/qa-ecrans', { recursive: true });
    const b = await chromium.launch({ args: ['--lang=fr-FR'], env: { ...process.env, LANG: 'fr_FR.UTF-8', LANGUAGE: 'fr', LC_ALL: 'fr_FR.UTF-8' } });
    const login = await b.newContext({ viewport: { width: 1920, height: 1080 } });
    const lp = await login.newPage();
    await lp.goto(`${BASE}/login`, { waitUntil: 'networkidle' });
    await lp.fill('input[name="email"]', EMAIL); await lp.fill('input[name="password"]', PASS);
    await Promise.all([lp.waitForNavigation({ waitUntil: 'networkidle' }).catch(() => {}), lp.press('input[name="password"]', 'Enter')]);
    const state = await login.storageState(); await login.close();
    const problems = [];
    for (const w of [1920, 390]) {
        const ctx = await b.newContext({ viewport: { width: w, height: w === 390 ? 844 : 1080 }, storageState: state, locale: 'fr-FR', timezoneId: 'Europe/Paris' });
        const p = await ctx.newPage();
        for (const u of PATHS) {
            const errs = []; p.removeAllListeners('pageerror'); p.on('pageerror', (e) => { if (!/isRtl|backdrop/.test(e.message)) errs.push(e.message); });
            const r = await p.goto(BASE + u, { waitUntil: 'networkidle' }).catch(() => null);
            await p.waitForTimeout(800);
            const res = await p.evaluate(() => {
                const W = document.documentElement.clientWidth, out = [];
                if (document.documentElement.scrollWidth > W + 1) out.push(`défilement horizontal (${document.documentElement.scrollWidth}px > ${W}px)`);
                for (const el of document.querySelectorAll('main *, .content-wrapper *, .container-xxl *')) {
                    const cs = getComputedStyle(el); if (cs.display === 'none' || cs.visibility === 'hidden' || !el.offsetParent) continue;
                    const r = el.getBoundingClientRect(); if (r.width <= 2 || r.height <= 2 || el.closest('.visually-hidden,.sr-only')) continue;
                    // contenu dans un conteneur qui défile ou découpe (tableau responsive, carrousel) : pas un débordement de page
                    let a = el.parentElement, contained = false;
                    while (a && a !== document.body) { const o = getComputedStyle(a).overflowX; if (o === 'auto' || o === 'scroll' || o === 'hidden') { contained = a.getBoundingClientRect().right <= W + 2; break; } a = a.parentElement; }
                    if (contained) continue;
                    if (r.right > W + 2 && cs.position !== 'fixed') { out.push(`sort de l'écran : ${el.tagName.toLowerCase()}.${[...el.classList].slice(0, 2).join('.')} (${Math.round(r.right)}px)`); if (out.length > 6) break; }
                    // texte coupé sans points de suspension
                    if (el.children.length === 0 && el.textContent.trim() && el.scrollWidth > el.clientWidth + 2 && cs.overflowX === 'hidden' && cs.textOverflow !== 'ellipsis') out.push(`texte coupé : « ${el.textContent.trim().slice(0, 40)} »`);
                }
                return [...new Set(out)].slice(0, 8);
            });
            const shot = `/tmp/qa-ecrans/${u.replace(/\W+/g, '_') || 'root'}-${w}.png`;
            await p.screenshot({ path: shot });
            const st = r ? r.status() : 0;
            if (st >= 400 || res.length || errs.length) problems.push({ w, u, status: st, res, errs: errs.slice(0, 2) });
            console.log(`${st >= 400 || res.length || errs.length ? '✗' : '✓'} ${w}px ${u} (${st})${res.length ? ' — ' + res.join(' ; ') : ''}${errs.length ? ' — JS : ' + errs[0].slice(0, 80) : ''}`);
        }
        await ctx.close();
    }
    await b.close();
    process.exit(problems.length ? 1 : 0);
})();
