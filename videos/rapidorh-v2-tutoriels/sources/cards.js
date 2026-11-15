// Cartes d'introduction / de fin et miniature (1280×720), charte violette RapidoRH.
const { chromium } = require('playwright');
const EP = require('./episodes');
const fs = require('fs');
const id = process.argv[2]; const e = EP[id];
const html = (body) => `<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0}body{width:1280px;height:720px;font-family:Inter,sans-serif;background:radial-gradient(1200px 700px at 85% 15%,#9b84e0 0%,#7B61C4 45%,#4b2f96 100%);color:#fff;display:flex;flex-direction:column;justify-content:center;padding:0 110px;position:relative;overflow:hidden}
.k{font-size:26px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;opacity:.85}.t{font-size:74px;font-weight:800;line-height:1.05;margin:22px 0 26px;max-width:1000px}
.t span{background:#fff;color:#4b2f96;padding:0 14px;border-radius:12px;-webkit-box-decoration-break:clone;box-decoration-break:clone}.d{font-size:28px;opacity:.92;max-width:920px;line-height:1.35}
.f{position:absolute;bottom:56px;left:110px;right:110px;display:flex;justify-content:space-between;font-size:22px;opacity:.85}
.c{position:absolute;right:-120px;top:-120px;width:520px;height:520px;border-radius:50%;border:60px solid rgba(255,255,255,.08)}</style></head><body><div class="c"></div>${body}</body></html>`;
const hl = (t, a) => t.includes(a) ? t.replace(a, `<span>${a}</span>`) : t;
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  fs.mkdirSync(`out/${id}`, { recursive: true });
  await p.setContent(html(`<div class="k">RapidoRH · Tutoriel ${id.replace('RHV2-', '')}</div><div class="t">${hl(e.titre, e.accent)}</div><div class="d">${e.description}</div><div class="f"><span>Académie Rapido</span><span>${e.niveau} · données de démonstration fictives</span></div>`));
  await p.waitForTimeout(300); await p.screenshot({ path: `out/${id}/intro.png` });
  await p.setContent(html(`<div class="k">C'est terminé !</div><div class="t">Retrouvez tous les <span>tutoriels</span></div><div class="d">Dans l'Académie Rapido — RapidoRH, vos équipes humaines et IA réunies.</div><div class="f"><span>Académie Rapido</span><span>RapidoRH</span></div>`));
  await p.waitForTimeout(300); await p.screenshot({ path: `out/${id}/outro.png` });
  await b.close();
})();
