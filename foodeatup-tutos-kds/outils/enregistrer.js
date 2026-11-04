// Enregistre un rush de l'application KDS (mode démo hors ligne) avec un faux curseur.
// Usage : node enregistrer.js scenario.json dossier_sortie
// scenario : {"url":"http://127.0.0.1:8123/","w":1280,"h":800,"actions":[
//   {"t":"wait","ms":1500} | {"t":"click","x":..,"y":..} | {"t":"long","x":..,"y":..,"ms":700}
//   | {"t":"key","k":"Escape"} | {"t":"shot","nom":"x"} | {"t":"goto","hash":"/station"} ]}
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const sc = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const out = process.argv[3]; fs.mkdirSync(out, { recursive: true });
  const w = sc.w || 1280, h = sc.h || 800;
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: sc.dpr || 1,
    recordVideo: sc.video === false ? undefined : { dir: out, size: { width: w, height: h } } });
  const p = await ctx.newPage();
  const curseur = () => p.evaluate(() => {
    if (document.getElementById('faux-curseur')) return;
    const c = document.createElement('div'); c.id = 'faux-curseur';
    c.style.cssText = 'position:fixed;left:0;top:0;width:34px;height:34px;margin:-17px 0 0 -17px;border-radius:50%;background:rgba(255,165,0,.55);border:3px solid #fff;box-shadow:0 2px 10px rgba(0,0,0,.4);z-index:2147483647;pointer-events:none;transition:transform .12s;';
    document.body.appendChild(c);
    document.addEventListener('mousemove', e => { c.style.left = e.clientX + 'px'; c.style.top = e.clientY + 'px'; }, true);
    document.addEventListener('mousedown', () => c.style.transform = 'scale(.7)', true);
    document.addEventListener('mouseup', () => c.style.transform = 'scale(1)', true);
  });
  const t0 = Date.now(); const marques = [];
  await p.goto(sc.url || 'http://127.0.0.1:8123/'); await p.waitForTimeout(sc.demarrage || 6000);
  await curseur(); let pos = { x: w / 2, y: h / 2 }; await p.mouse.move(pos.x, pos.y);
  const aller = async (x, y) => { await p.mouse.move(x, y, { steps: 18 }); pos = { x, y }; };
  for (const a of sc.actions) {
    marques.push({ s: (Date.now() - t0) / 1000, a });
    if (a.t === 'wait') await p.waitForTimeout(a.ms);
    else if (a.t === 'click') { await aller(a.x, a.y); await p.waitForTimeout(150); await p.mouse.down(); await p.waitForTimeout(90); await p.mouse.up(); await p.waitForTimeout(a.ms ?? 600); }
    else if (a.t === 'long') { await aller(a.x, a.y); await p.mouse.down(); await p.waitForTimeout(a.ms || 800); await p.mouse.up(); await p.waitForTimeout(600); }
    else if (a.t === 'move') await aller(a.x, a.y);
    else if (a.t === 'key') { await p.keyboard.press(a.k); await p.waitForTimeout(a.ms ?? 500); }
    else if (a.t === 'goto') { await p.evaluate(hh => location.hash = hh, a.hash); await p.waitForTimeout(a.ms ?? 2500); await curseur(); }
    else if (a.t === 'shot') await p.screenshot({ path: path.join(out, a.nom + '.png') });
  }
  fs.writeFileSync(path.join(out, 'marques.json'), JSON.stringify(marques, null, 1));
  const v = p.video(); await ctx.close(); await b.close();
  if (v) { const f = await v.path(); fs.renameSync(f, path.join(out, 'rush.webm')); }
})();
