// Génère, pour chaque épisode de contenu.json : formation-NN.pdf (nuit), formation-NN-blanc.pdf, formation-NN.jpg (1600×900)
// et le PDF du lead magnet. Usage : node gen.js <dossier_sortie>
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const DIR = __dirname, OUT = path.resolve(process.argv[2] || 'out');
const C = JSON.parse(fs.readFileSync(path.join(DIR, 'contenu48.json'), 'utf8'));
const MINI = { 48: 'episode48-la-methode/episode48-miniature.png', 49: 'episode49-rapidocms-reseaux/episode49-miniature.png', 37: '../../../../tmp/claude-0/-home-user/9bdae596-b3e0-5331-a9c6-bc0f21d8cfc9/scratchpad/v37/thumb.png', 33: 'episode33-boites-pizza-costumes-halloween/episode33-miniature.jpg', 34: 'episode34-salle-live/episode34-miniature.jpg', 35: 'episode35-la-chaine-fraternelles/episode35-miniature.png', 36: 'episode36-app-haccp-google-play/episode36-miniature.png' };
const b64 = f => 'data:image/' + (f.endsWith('png') ? 'png' : 'jpeg') + ';base64,' + fs.readFileSync(f).toString('base64');
const PHOTO = b64('/home/user/Video/videos/episode32-email-nurturing-claude-lovable/composition/a/michael.jpg');
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/\[([^\]]+)\]/g, '<mark>[$1]</mark>');

const css = (nuit) => `
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
@page{size:A4;margin:0}*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Poppins,sans-serif;font-size:10.5pt;line-height:1.5;color:${nuit ? '#E8EDF2' : '#16242F'};background:${nuit ? '#0F1A23' : '#fff'};-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;padding:16mm 15mm 18mm;position:relative;page-break-after:always;overflow:hidden;background:${nuit ? '#0F1A23' : '#fff'}}
.foot{position:absolute;left:15mm;right:15mm;bottom:8mm;display:flex;justify-content:space-between;font-size:7.5pt;color:#7d8ea3}
.lab{font-size:8pt;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;color:#FFA500;margin-bottom:4px}
h1{font-size:25pt;line-height:1.15;margin:6px 0 10px}h2{font-size:16pt;margin-bottom:10px}h3{font-size:12pt;margin-bottom:4px}
.card{background:${nuit ? '#16242F' : '#F4F7FA'};border:1px solid ${nuit ? '#22384a' : '#dde5ec'};border-radius:10px;padding:12px 14px;margin-bottom:10px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}
ul{list-style:none}li{padding-left:16px;position:relative;margin:3px 0}li:before{content:"✓";position:absolute;left:0;color:#22c55e;font-weight:700}
ul.dot li:before{content:"•";color:#FFA500}
.badge{display:inline-block;background:#007BFF;color:#fff;border-radius:999px;padding:3px 12px;font-weight:600;font-size:8.5pt}
.cover{background:${nuit ? 'linear-gradient(160deg,#0F1A23 40%,#16324a)' : 'linear-gradient(160deg,#fff 40%,#e8f2ff)'}}
.mini{width:100%;border-radius:12px;margin:8mm 0 6mm;box-shadow:0 10px 30px rgba(0,0,0,.35)}
.auteur{display:flex;gap:12px;align-items:center;position:absolute;left:15mm;bottom:20mm}.auteur img{width:44px;height:44px;border-radius:50%;object-fit:cover;border:2px solid #007BFF}
.step{border-left:4px solid #007BFF;padding:12px 14px;margin-bottom:12px;background:${nuit ? '#16242F' : '#F4F7FA'};border-radius:0 10px 10px 0;page-break-inside:avoid}
.num{display:inline-flex;width:26px;height:26px;border-radius:50%;background:#007BFF;color:#fff;align-items:center;justify-content:center;font-weight:700;margin-right:8px}
.prompt{background:${nuit ? '#0b141c' : '#fff'};border:1px solid ${nuit ? '#2c4558' : '#d5dee6'};border-radius:8px;padding:10px 12px;margin:8px 0;font-size:9.5pt}
.prompt b{display:block;font-size:7.5pt;color:#c96442;letter-spacing:1px;text-transform:uppercase;margin-bottom:4px}
mark{background:#fff1d6;color:#7a4b00;border-radius:3px;padding:0 2px}
.res{display:grid;grid-template-columns:1fr 1fr;gap:8px;font-size:9pt}.res div{border-radius:8px;padding:8px 10px}
.ok{background:${nuit ? '#123a26' : '#e8f8ee'}}.ko{background:${nuit ? '#3a1d12' : '#fdeee8'}}
.res small{display:block;font-weight:700;font-size:7pt;letter-spacing:1px;text-transform:uppercase;opacity:.8}
a{color:#4da3ff;text-decoration:none}`;

function formation(e, f, nuit) {
  const foot = (n, t) => `<div class="foot"><span>Michael Kebail-Ali · Épisode ${e}</span><span>${n} / ${t}</span></div>`;
  const steps = f.etapes.map((s, i) => `<div class="step"><h3><span class="num">${i + 1}</span>${esc(s.titre)}</h3><p>${esc(s.explication)}</p>
    <div class="prompt"><b>Prompt à copier</b>${esc(s.prompt)}</div>
    <div class="res"><div class="ok"><small>Résultat attendu</small>${esc(s.resultat)}</div><div class="ko"><small>Piège à éviter</small>${esc(s.piege)}</div></div></div>`);
  const pages = [
    `<div class="page cover"><div class="lab">Formation · Michael Kebail-Ali</div><span class="badge">ÉPISODE ${e}</span>
      <div class="lab" style="margin-top:14px">Comment j'ai fait, étape par étape</div><h1>${esc(f.titre)}</h1><p>${esc(f.promesse)}</p>
      <img class="mini" src="${b64('/home/user/Video/videos/' + MINI[e])}" style="width:62%;display:block;margin:8mm auto 0">
      <div class="auteur"><img src="${PHOTO}"><div><b>Michael Kebail-Ali</b><br><span style="font-size:8.5pt;color:#7d8ea3">Fondateur de BraindCode, FoodEatUp et RapidoSoftware</span></div><span class="badge" style="margin-left:20mm">Formation gratuite</span></div>
      ${foot(1, 0)}</div>`,
    `<div class="page"><div class="lab">En bref</div><h2>Ce que vous allez apprendre</h2><div class="card">${esc(f.promesse)}</div>
      <div class="card"><div class="lab">Ce que vous saurez faire</div><ul>${f.objectifs.map(o => `<li>${esc(o)}</li>`).join('')}</ul></div>
      <div class="card"><div class="lab">Avant de commencer</div><ul class="dot">${f.prerequis.map(o => `<li>${esc(o)}</li>`).join('')}</ul></div>
      <div class="grid"><div class="card"><div class="lab">Pour qui ?</div>${esc(f.pour_qui)}</div><div class="card"><div class="lab">Au programme</div>${f.etapes.length} étapes · ${f.etapes.length} prompts à copier · environ ${f.duree} min</div></div>
      <div class="card"><div class="lab">Les outils</div>${f.outils.map(o => `<div style="display:flex;justify-content:space-between;border-bottom:1px solid #22384a33;padding:3px 0"><b>${o.nom}</b><a href="${o.url}">${o.url.replace('https://', '')}</a></div>`).join('')}</div>
      <div class="card"><div class="lab">L'épisode vidéo</div>Épisode ${e} de la série « Mon quotidien d'entrepreneur avec l'IA » : <a href="https://michael.foodeatup.fr/formations/${f.slug}">michael.foodeatup.fr/formations/${f.slug}</a></div>
      ${foot(2, 0)}</div>`,
  ];
  // Étapes : deux par page, puis garde-fous et état réel.
  for (let i = 0; i < steps.length; i += 2) pages.push(`<div class="page">${i ? '' : '<div class="lab">La méthode</div><h2>Étape par étape</h2>'}${steps.slice(i, i + 2).join('')}${foot(pages.length + 1, 0)}</div>`);
  pages.push(`<div class="page"><div class="lab">Les garde-fous</div><div class="card"><ul>${f.garde_fous.map(g => `<li>${esc(g)}</li>`).join('')}</ul></div>
    <div class="card" style="border-color:#22c55e"><div class="lab" style="color:#22c55e">Ce qui est réellement en place</div>${esc(f.etat_reel)}</div>
    <div class="lab" style="margin-top:14px">Pour aller plus loin</div><h2>Passez à la pratique</h2>
    <div class="card"><b>Je vous aide à le mettre en place</b><p>Prenez rendez-vous : on regarde ensemble votre cas, à votre rythme.</p><p style="margin-top:6px"><span class="badge">michael.foodeatup.fr</span></p></div>
    <div class="card">Toutes mes formations, vidéos et projets : <a href="https://michael.foodeatup.fr">michael.foodeatup.fr</a></div>${foot(pages.length + 1, 0)}</div>`);
  const t = pages.length;
  return `<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>${css(nuit)}</style></head><body>${pages.join('').replace(/ \/ 0</g, ` / ${t}<`)}</body></html>`;
}

function leadMagnet(e, f) {
  const l = f.lm;
  return `<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>${css(false)}
  .box li:before{content:"☐";color:#007BFF}</style></head><body><div class="page">
  <div class="lab">${l.type === 'kit' ? 'Kit gratuit' : 'Check-list gratuite'} · Épisode ${e}</div><h1>${esc(l.nom)}</h1><p>${esc(l.description)}</p>
  ${l.items.map(([t, xs]) => `<div class="card"><div class="lab">${esc(t)}</div><ul class="box">${xs.map(x => `<li>${esc(x)}</li>`).join('')}</ul></div>`).join('')}
  <div class="card"><b>La formation complète, avec les prompts :</b> <a href="https://michael.foodeatup.fr/formations/${f.slug}">michael.foodeatup.fr/formations/${f.slug}</a></div>
  <div class="foot"><span>Michael Kebail-Ali · Épisode ${e}</span><span>michael.foodeatup.fr</span></div></div></body></html>`;
}

function image(e, f) {
  return `<!doctype html><html><head><meta charset="utf-8"><style>@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700;800&display=swap');
  *{margin:0;box-sizing:border-box}body{width:1600px;height:900px;font-family:Poppins;background:linear-gradient(135deg,#0F1A23 45%,#16324a);color:#fff;position:relative;overflow:hidden}
  .b{display:inline-block;background:#FFA500;color:#000;font-weight:700;border-radius:999px;padding:10px 28px;font-size:30px}
  .l{font-size:24px;font-weight:700;letter-spacing:5px;color:#FFA500;text-transform:uppercase;margin:28px 0 10px}
  h1{font-size:${f.titre.length > 60 ? 58 : 66}px;line-height:1.12;max-width:860px}
  .m{position:absolute;right:90px;top:70px;height:760px;border-radius:30px;box-shadow:0 30px 80px rgba(0,0,0,.6)}
  .a{position:absolute;left:90px;bottom:80px;display:flex;gap:22px;align-items:center;font-size:30px;font-weight:700}.a img{width:96px;height:96px;border-radius:50%;border:4px solid #007BFF;object-fit:cover}
  .a span{display:block;font-size:22px;color:#AEB8C2;font-weight:500}
  .g{position:absolute;right:90px;bottom:24px;background:#007BFF;padding:10px 26px;border-radius:14px;font-size:24px;font-weight:700}</style></head><body>
  <div style="position:absolute;left:90px;top:90px"><span class="b">ÉPISODE ${e}</span><div class="l">Comment j'ai fait, étape par étape</div><h1>${esc(f.titre)}</h1></div>
  <img class="m" src="${b64('/home/user/Video/videos/' + MINI[e])}"><div class="a"><img src="${PHOTO}"><div>Michael Kebail-Ali<span>BraindCode · FoodEatUp · RapidoSoftware</span></div></div><div class="g">Formation gratuite + PDF</div></body></html>`;
}

(async () => {
  fs.mkdirSync(path.join(OUT, 'pdf'), { recursive: true }); fs.mkdirSync(path.join(OUT, 'img'), { recursive: true });
  const b = await chromium.launch();
  for (const [e, f] of Object.entries(C)) {
    const p = await b.newPage();
    for (const nuit of [true, false]) {
      await p.setContent(formation(e, f, nuit), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready);
      await p.pdf({ path: path.join(OUT, 'pdf', `formation-${e}${nuit ? '' : '-blanc'}.pdf`), format: 'A4', printBackground: true });
    }
    await p.setContent(leadMagnet(e, f), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready);
    await p.pdf({ path: path.join(OUT, 'pdf', f.lm.fichier), format: 'A4', printBackground: true });
    await p.setViewportSize({ width: 1600, height: 900 });
    await p.setContent(image(e, f), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: path.join(OUT, 'img', `formation-${e}.jpg`), type: 'jpeg', quality: 88 });
    await p.close(); console.log('ok', e);
  }
  await b.close();
})();
