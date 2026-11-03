// Soutenance RapidoCRM : tout dépend du temps t (render(t)). Les vidéos du Drive sont incrustées
// ensuite par post.py dans la zone #stage (CLIPS ci-dessous) ; le HTML dessine le reste.
const C = window.CFG;
const cl = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const eo = x => 1 - Math.pow(1 - x, 3);
const w = (k, after = 0) => { const x = C.words.find(v => v[1] >= after && v[0].toLowerCase().includes(k.toLowerCase())); return x ? x[1] : after; };
const $ = s => document.querySelector(s);
const CH = [[0, 'Ouverture', '<em>RapidoCRM</em>'], [11.3, '01', 'Prospecter et <em>enregistrer</em>'], [34.7, '02', 'Suivre dans le <em>pipeline</em>'],
  [50.5, '03', 'Piloter le CRM par l\'IA avec <em>MCP</em>'], [74.1, '04', 'Agent <em>vocal</em> et historique'], [96.9, '05', 'Automatiser avec un <em>workflow</em>'], [117.86, 'Fin', 'Une seule <em>plateforme</em>']];
// Incrustations (lues par post.py) : [fichier, début, fin, point de départ dans le fichier, vitesse]
window.CLIPS = [
  ['dashboard.mp4', 3.6, 11.3, 0, 1], ['siret.mp4', 11.3, 29.0, 0.8, 1], ['ajout-segment.mp4', 29.0, 34.7, 2, 1],
  ['histo-entreprise.mp4', 46.0, 50.5, 1, 1], ['pack-vocal.mp4', 74.1, 79.0, 3.6, 1], ['agenda.mp4', 88.1, 91.0, 2, 1],
  ['wf-creer.mp4', 96.9, 106.1, 8, 1.4], ['wf-stats.mp4', 111.4, 117.86, 1, 1], ['dashboard.mp4', 117.86, 124.0, 4, 1]];
const URL = [[0, 'app.rapidocrm · tableau de bord'], [11.3, 'app.rapidocrm · prospection'], [34.7, 'app.rapidocrm · pipeline'], [50.5, 'Claude · connecté au serveur MCP RapidoCRM'],
  [67.2, 'app.rapidocrm · bibliothèque de prompts'], [74.1, 'app.rapidocrm · agent vocal'], [88.1, 'app.rapidocrm · agenda'], [91.0, 'app.rapidocrm · historique des appels'],
  [96.9, 'app.rapidocrm · workflows'], [117.86, 'app.rapidocrm · tableau de bord']];

const stage = $('#stage'), side = $('#side');
const L = [];   // couches de l'écran : [el, t0, t1]
const lay = (t0, t1, html) => { const e = document.createElement('div'); e.className = 'lay'; e.innerHTML = html; stage.appendChild(e); L.push([e, t0, t1]); return e; };
const S = [];   // éléments animés : [el, t0, t1, fx]
const CALLS = [];
const at = (el, t0, t1 = 1e9, fx = 'up') => { S.push([el, t0, t1, fx]); return el; };
const call = (t0, t1, y, html, cls = '') => { const e = document.createElement('div'); e.className = 'call ' + cls; e.style.top = y + 'px'; e.innerHTML = html; side.appendChild(e); CALLS.push([e, t0, t1]); return at(e, t0, t1, 'left'); };
const img = (src, kb = 1) => `<div class="img"><img src="a/${src}" data-kb="${kb}"></div>`;

// ── 1. Prospecter
call(w('trois'), 34.7, 0, '<b>PROSPECTION</b><div class="big">3 <small>modes de recherche</small></div>');
const md = call(w('spécialité'), 34.7, 0, '<b>LES 3 MODES</b><div id="m1">① Spécialité + ville <span style="color:#9aa6c8;font-size:17px">· Google Places</span></div><div id="m2">② Raison sociale + code NAF</div><div id="m3">③ Numéro SIRET <span style="color:#9aa6c8;font-size:17px">· API de l\'État</span></div>', 'hot');
at($('#m2'), w('raison'), 34.7); at($('#m3'), w('siret'), 34.7);
call(w('workflows'), 34.7, 464, '<b>EN COULISSE</b>Recherches via workflows n8n');
call(w('enregistre', 22), 34.7, 554, '<b>UN CLIC</b>« Enregistrer » ou « Enregistrer tout »');
call(w('doublons'), 34.7, 644, '<b>CONTRÔLE</b>⚠️ Doublons détectés avant insertion', 'hot');
call(w('rejoint'), 34.7, 734, '<b>AUTOMATIQUE</b>→ pipeline + segments');

// ── 2. Pipeline (animation : la carte du prospect avance)
const ST = [['Nouveau prospect', '1'], ['Qualification', '2'], ['Contact établi', '3'], ['', '4'], ['', '5'], ['', '6'], ['Fermé gagné', '7'], ['Fermé perdu', '8']];
const kan = lay(34.7, 46.0, `<div class="kan"><h4>Pipeline par défaut · 8 étapes</h4>${ST.map(([n, k]) => `<div class="col"><p><span>ÉTAPE ${k}</span>${n || '…'}</p></div>`).join('')}
 <div class="card" id="pc">Agence immobilière<span>Lyon · nouveau prospect</span></div>
 <div class="hist" id="ph"><h5>Historique de l'opportunité</h5><div><b>Nouveau prospect</b> → Qualification · par Sadok</div><div><b>Qualification</b> → Contact établi · par Sadok</div><div>Probabilité de l'étape reportée sur l'opportunité ✓</div></div></div>`);
call(36.2, 50.5, 0, '<b>PIPELINE</b><div class="big">8 <small>étapes, de « Nouveau prospect » à « Fermé gagné » ou « perdu »</small></div>');
call(w('glisser'), 50.5, 196, '<b>GESTE</b>Glisser-déposer', 'hot');
call(w('historique', 43), 50.5, 286, '<b>TRAÇABILITÉ</b>Chaque déplacement enregistré : départ, arrivée, auteur');
call(w('probabilité'), 50.5, 414, '<b>PRÉVISIONS</b>La probabilité de l\'étape suit l\'opportunité');
const tMove1 = w('glisser') - .3, tMove2 = tMove1 + 1.2, tHist = w('historique', 43);
at($('#ph'), tHist, 46.0);

// ── 3. MCP
const typ = (el, txt, t0, cps = 28) => { el.dataset.txt = txt; el.dataset.t0 = t0; el.dataset.cps = cps; return el; };
lay(50.5, 57.4, img('claude-mcp.png'));
call(51.0, 57.4, 0, '<b>DEMANDE 1</b>« Donne-moi la fiche de l\'entreprise et dis-moi à quelle étape du pipeline elle se trouve. »', 'hot');
call(w('langage'), 57.4, 250, '<b>PROTOCOLE MCP</b>Claude lit et pilote le CRM en langage naturel');
call(53.4, 57.4, 380, '<b>CAPTURE RÉELLE</b><span style="font-size:18px;color:#9aa6c8">Rapport de stage · Claude ↔ RapidoCRM (fiche de test)</span>');
lay(57.4, 63.3, img('arch.png'));
call(w('135'), 74.1, 0, '<b>SERVEUR HUB</b><div class="big" id="n135">0 <small>outils</small></div>', 'hot');
call(w('neuf'), 74.1, 150, '<b>ORGANISATION</b><div class="big">9 <small>serveurs métier</small></div>');
call(w('droits'), 74.1, 300, '<b>SÉCURITÉ</b>Toujours dans la limite des droits de l\'utilisateur');
const chat2 = lay(63.3, 67.2, `<div class="chat"><div class="head"><img src="a/claude.webp"> · connecté à RapidoCRM</div>
 <div class="msg"><span id="q2"></span><span class="cur"></span></div><div id="tl"><span class="tool">rapidocrm · create_task</span></div>
 <div class="ans" id="a2">✓ Tâche créée : <b>rappeler l'entreprise jeudi</b>. Elle apparaît dans RapidoCRM, sans passer par l'interface.</div></div>`);
typ($('#q2'), 'Crée une tâche pour rappeler cette entreprise jeudi.', 63.5, 30);
at($('#tl'), 65.0, 67.2); at($('#a2'), 65.6, 67.2);
lay(67.2, 74.1, img('prompts.png'));
call(w('169'), 74.1, 410, '<b>BIBLIOTHÈQUE</b><div class="big" id="n169">0 <small>prompts</small></div>', 'hot');
call(w('23'), 74.1, 560, '<b>RANGÉS EN</b><div class="big">23 <small>catégories</small></div>');

// ── 4. Agent vocal
call(w('vocal', 74), 96.9, 0, '<b>AGENT VOCAL</b>Appelle les prospects au nom de l\'entreprise, avec son propre numéro');
call(76.2, 79.0, 128, '<b>À L\'ÉCRAN</b>Solde de minutes · aucun identifiant de téléphonie affiché');
const cfgEl = lay(79.0, 83.4, `<div class="kan" style="display:block;padding:60px 120px"><h4>Configuration de l'agent vocal</h4>${[['Argumentaire', 'Présenter RapidoCRM aux agences'], ['Secteur', 'Immobilier'], ['Objectif des appels', 'Rendez-vous'], ['Ton', 'Professionnel et chaleureux'], ['Produits à présenter', 'RapidoCRM · agent vocal']].map(([k, v], i) => `<div class="cf" style="background:#fff;border-radius:14px;padding:16px 22px;margin-bottom:14px;display:flex;justify-content:space-between;font-size:24px;color:#1b2340;box-shadow:0 6px 16px rgba(27,35,64,.08)"><b>${k}</b><span style="color:#6c5ce7;font-weight:700">${v}</span></div>`).join('')}<div style="font-family:'JetBrains Mono';font-size:16px;color:#8a93b2">exemple de configuration</div></div>`);
[...cfgEl.querySelectorAll('.cf')].forEach((e, i) => at(e, 79.2 + i * .55, 83.4));
const ph = lay(83.4, 88.1, `<div class="phone"><div class="ph"><div class="av">🤖</div><div style="font-size:24px;font-weight:800">Agent vocal</div><div class="wave">${'<i></i>'.repeat(14)}</div><div style="font-size:18px;color:#9aa6c8">appel en cours</div></div>
 <div class="steps"><div class="st" id="s1">📢 « Ceci est un appel automatisé »</div><div class="st" id="s2">🎯 Qualifie le besoin</div><div class="st" id="s3">📅 Propose un rendez-vous</div></div></div>`);
const sOn = [['#s1', w('annonce')], ['#s2', w('qualifie')], ['#s3', w('propose')]];
sOn.forEach(([s, t]) => at($(s), t, 88.1));
call(w('agenda', 85), 96.9, 250, '<b>AGENDA</b>Le rendez-vous est inscrit chez le commercial', 'hot');
lay(91.0, 93.7, img('appels-histo.png'));
lay(93.7, 96.9, img('appels-transcript.png'));
call(w('restitué'), 96.9, 380, '<b>DANS LE CRM</b>Résultat · résumé · transcription');
call(91.4, 96.9, 506, '<b>CAPTURES RÉELLES</b><span style="font-size:18px;color:#9aa6c8">Rapport de stage · noms de test masqués</span>');

// ── 5. Workflow
call(w('automatisé', 96), 117.86, 0, '<b>AUTOMATISATION</b>Tout le parcours, sans écrire de code', 'hot');
call(w('déclencheurs'), 117.86, 128, '<b>ÉDITEUR VISUEL</b>Déclencheurs · actions · délais · branches');
const wf = lay(106.1, 111.4, img('workflow.png') + `<div class="tag" style="left:30px;top:24px">Modèle « Prospection complète avec agent IA »</div><div class="chain">${['⚡ Déclencheur', '🔎 Recherche d\'entreprises', '⏱ Délai', '📞 Appel vocal', '📊 Pipeline', '👥 Segment'].map((n, i) => `${i ? '<span class="arrow">→</span>' : ''}<div class="node${i === 2 ? ' d' : ''}">${n}</div>`).join('')}</div>`);
[...wf.querySelectorAll('.node,.arrow')].forEach((e, i) => at(e, 106.4 + i * .28, 111.4));
call(w('brouillon'), 117.86, 256, '<b>CYCLE DE VIE</b><div style="display:flex;align-items:center;gap:12px;margin-top:6px">Brouillon <div class="sw" id="sw"><i></i></div> Actif</div>');
call(w('journalisée'), 117.86, 376, '<b>SUIVI</b>Chaque exécution journalisée, nœud par nœud');

// ── Clôture
call(119.0, 124.0, 0, '<b>DU PROSPECT</b>…jusqu\'au rendez-vous dans l\'agenda', 'hot');

window.thumb = () => render(52.6);
function render(t) {
  const intro = t < 3.6, outro = t >= 124.0;
  $('#intro').style.display = intro ? 'flex' : 'none';
  $('#outro').style.display = outro ? 'flex' : 'none';
  $('#main').style.display = intro || outro ? 'none' : 'block';
  if (intro) { $('#intro').style.opacity = 1 - cl((t - 3.2) / .4); [...$('#intro').children].forEach((e, i) => { const p = eo(cl((t - .2 - i * .25) / .5)); e.style.opacity = p; e.style.transform = `translateY(${(1 - p) * 40}px)`; }); }
  if (outro) { [...$('#outro').children].forEach((e, i) => { const p = eo(cl((t - 124.2 - i * .35) / .5)); e.style.opacity = p; e.style.transform = `translateY(${(1 - p) * 40}px)`; }); }
  const ch = [...CH].reverse().find(c => t >= c[0]);
  $('#chip').textContent = ch[1]; $('#ttl').innerHTML = ch[2];
  $('#url').textContent = [...URL].reverse().find(u => t >= u[0])[1];
  for (const [e, a, b] of L) { const on = t >= a && t < b; e.style.display = on ? 'block' : 'none'; if (on) { e.style.opacity = cl((t - a) / .3) * (1 - cl((t - (b - .2)) / .2)); const im = e.querySelector('[data-kb]'); if (im) im.style.transform = `scale(${1 + .06 * cl((t - a) / (b - a))})`; } }
  for (const [e, a, b, fx] of S) {
    const p = eo(cl((t - a) / .45)), q = 1 - cl((t - (b - .25)) / .25);
    e.style.opacity = Math.min(p, q);
    e.style.transform = fx === 'left' ? `translateX(${(1 - p) * 60}px)` : `translateY(${(1 - p) * 30}px)`;
  }
  // encarts de droite empilés dans l'ordre d'apparition
  let y = 0; for (const [e, a, b] of CALLS) { if (t >= a && t < b) { e.style.display = 'block'; e.style.top = y + 'px'; y += e.offsetHeight + 14; } else e.style.display = 'none'; }
  // pipeline : la carte passe de la colonne 1 à 3
  const cw = (1376 - 52 - 7 * 12) / 8, cx = k => 26 + k * (cw + 12) + (cw - 150) / 2;
  const m1 = eo(cl((t - tMove1) / .6)), m2 = eo(cl((t - tMove2) / .6));
  const pc = $('#pc'); pc.style.left = (cx(0) + (cx(1) - cx(0)) * m1 + (cx(2) - cx(1)) * m2) + 'px';
  pc.style.top = (140 - 18 * Math.sin(Math.PI * (m1 < 1 ? m1 : m2))) + 'px';
  pc.querySelector('span').textContent = 'Lyon · ' + (m2 > .5 ? 'contact établi' : m1 > .5 ? 'qualification' : 'nouveau prospect');
  // texte tapé
  document.querySelectorAll('[data-txt]').forEach(e => { const n = Math.floor(cl(t - e.dataset.t0, 0, 99) * e.dataset.cps); e.textContent = e.dataset.txt.slice(0, n); });
  // compteurs
  const cnt = (id, v, t0) => { const e = $(id); if (e) e.firstChild.textContent = Math.round(v * eo(cl((t - t0) / 1.2))) + ' '; };
  cnt('#n135', 135, w('135')); cnt('#n169', 169, w('169'));
  // vagues de l'appel + interrupteur
  document.querySelectorAll('.wave i').forEach((e, i) => e.style.height = (16 + 60 * Math.abs(Math.sin(t * 7 + i * .8))) + 'px');
  sOn.forEach(([s, a]) => $(s).classList.toggle('on', t >= a));
  const sw = cl((t - w('activer')) / .4); $('#sw').style.background = sw > .5 ? '#22c3a6' : '#c7cbe0'; $('#sw i').style.left = (4 + 32 * eo(sw)) + 'px';
  // sous-titres mot à mot
  const ln = C.lines.find(l => t >= l.t0 - .1 && t < l.t1 + .5);
  if (!ln) $('#sub').innerHTML = '';
  else { const li = C.lines.indexOf(ln); $('#sub').innerHTML = C.words.filter(v => v[2] === li).map(v => t >= v[1] ? `<u>${v[0]}</u>` : `<i>${v[0]}</i>`).join(' '); }
  // progression des chapitres
  document.querySelectorAll('#prog i').forEach((e, k) => { const a = CH[k + 1][0], b = (CH[k + 2] || [124])[0]; e.style.width = 100 * cl((t - a) / (b - a)) + '%'; });
}
render(0);
