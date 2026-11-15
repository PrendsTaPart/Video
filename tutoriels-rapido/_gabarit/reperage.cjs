// Repérage d'un écran pour écrire un scénario : titres, onglets, boutons, liens, champs et leurs sélecteurs.
// Usage : node _gabarit/reperage.cjs <BASE_URL> <chemin> [chemin…]   (connexion demo@rapido.test / Demo-Rapido-2026)
// Lecture seule : ne clique sur rien, n'envoie aucun formulaire.
const { chromium } = require('playwright');
const [, , BASE, ...CHEMINS] = process.argv;
(async () => {
    const b = await chromium.launch();
    const p = await (await b.newContext({ viewport: { width: 1920, height: 1080 }, locale: 'fr-FR' })).newPage();
    await p.goto(`${BASE}/login`, { waitUntil: 'load' });
    await p.fill('input[name="email"]', process.env.EMAIL || 'demo@rapido.test');
    await p.fill('input[name="password"]', process.env.PASS || 'Demo-Rapido-2026');
    await Promise.all([p.waitForNavigation({ waitUntil: 'load' }).catch(() => {}), p.press('input[name="password"]', 'Enter')]);
    for (const chemin of CHEMINS) {
        await p.goto(`${BASE}${chemin}`, { waitUntil: 'load' });
        await p.waitForLoadState('networkidle', { timeout: 8000 }).catch(() => {});
        const r = await p.evaluate(() => {
            const vis = (n) => n.offsetParent !== null && !n.closest('aside,#layout-menu,.layout-menu,nav,.layout-navbar,footer');
            const txt = (n) => (n.innerText || n.value || n.getAttribute('aria-label') || n.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 70);
            const sel = (n) => n.id ? `#${n.id}` : n.name ? `${n.tagName.toLowerCase()}[name="${n.name}"]` : (n.className && typeof n.className === 'string' ? `${n.tagName.toLowerCase()}.${n.className.trim().split(/\s+/).slice(0, 2).join('.')}` : n.tagName.toLowerCase());
            const liste = (q) => [...document.querySelectorAll(q)].filter(vis).map((n) => `${txt(n)}  ⟶  ${sel(n)}${n.getAttribute('href') ? '  ' + n.getAttribute('href') : ''}`).filter((l) => !l.startsWith('  ⟶'));
            return {
                titre: document.title, url: location.pathname,
                titres: liste('h1,h2,h3,h4,h5,h6'),
                boutons: liste('button,.btn,[role=tab]').slice(0, 40),
                liens: liste('a:not(.btn)').slice(0, 40),
                champs: [...document.querySelectorAll('input:not([type=hidden]),select,textarea')].filter(vis).map((n) => `${n.tagName.toLowerCase()} ${n.type || ''} ${sel(n)} ${n.getAttribute('placeholder') || ''}`).slice(0, 40),
                hauteur: document.body.scrollHeight,
            };
        });
        console.log(`\n=== ${chemin} → ${r.url} (« ${r.titre} », hauteur ${r.hauteur}px)`);
        for (const k of ['titres', 'boutons', 'liens', 'champs']) { console.log(`-- ${k}`); r[k].forEach((l) => console.log('   ' + l)); }
    }
    await b.close();
})();
