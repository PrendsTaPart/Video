// Épisode 63 — Claude a tué le business des consultants en restauration (inspiré « 5 skills de Claude »)
const {t0,t1,w,h}=J;
J.init({episode:63,keyword:'CONSULTANT',duoLogo:'claude',stepLabel:'DEMANDE',
  theme:{cls:'clair',vars:{bg:'#EFECE4',bg2:'#E3DED2',surf:'#FFFFFF',line:'#E2DBCC',text:'#1E1C19',mute:'#8B8579',accent:'#C9603F',accent2:'#1E1C19',hlbg:'#1E1C19',hlfg:'#FFFFFF',title:"'Fraunces'"}},
  kw:['consultants','cinq','objectif','allergènes','carte','prix','avis','tableau','soirée.','CONSULTANT'],red:['tué']});
J.progress(5);
// Accroche
let s=J.hook(0,t0(1),{line:0,hl:['consultants'],y:300,sticker:'TRUC QUE PERSONNE NE FAIT'});
s.img(J.kit('editorial-mentaliste-restaurateur-pensif.png'),{x:540,w:520,y:760,at:.5,an:'up',css:{filter:'grayscale(.2)'}});
s.add('<div class="sticker" style="background:#d93025;color:#fff;font-size:70px">FINI ?</div>',{x:700,w:0,y:1020,at:w(0,'tué'),an:'stamp'});
// « Tout le monde… un mail » puis les cinq demandes
s=J.scene(t0(1),t0(2),{noCap:false});
s.add(`<div class="card" style="text-align:left"><div class="mute" style="font-size:26px;font-weight:700;letter-spacing:3px">CE QUE TOUT LE MONDE FAIT</div><div style="font-size:42px;font-weight:700;margin-top:10px">« Écris-moi un mail pour… »</div></div>`,{x:540,w:820,y:260,at:t0(1)});
s.add('<div style="height:8px;background:#d93025;border-radius:4px"></div>',{x:540,w:860,y:350,at:w(1,'mail')+.2,an:'left'});
s.text('<span style="font-size:96px">5 demandes</span><br><span class="mute" style="font-size:44px;font-weight:600">que presque personne ne fait</span>',{y:540,at:w(1,'moi')});
[1,2,3,4,5].forEach(i=>s.add(`<div class="numb" style="background:var(--accent);color:#fff;width:130px;height:130px">${i}</div>`,{x:540+(i-3)*170,w:130,y:860,at:w(1,'cinq')+i*.1,an:'pop'}));
// 1. Bras droit
s=J.step(J.scene(t0(2),t0(4)),1,'Mon bras','droit');
let z=J.window(s,3,{y:300,label:'UN SEUL OBJECTIF'});
J.inzone(s,z,h.chip('OBJECTIF : remplir le mardi soir','a'),{at:w(3,'objectif'),css:{left:'0',top:'0'}});
['Lundi · un post « menu du mardi »','Mardi midi · un message aux habitués','Mardi · une formule à deux','Mercredi · on regarde ce qui a marché'].forEach((x,i)=>J.inzone(s,z,h.check(x),{at:w(3,'plan')+i*.45,an:'up',css:{left:'0',right:'0',top:(90+i*100)+'px'}}));
// 2. Prof particulier
s=J.step(J.scene(t0(4),t0(6)),2,'Le prof','particulier');
['Leçon 1 · les allergènes, c\'est quoi','Leçon 2 · les repérer dans la carte','Leçon 3 · répondre au client'].forEach((x,i)=>s.add(`<div class="card" style="padding:22px 30px"><div style="font-size:34px;font-weight:700">${x}</div><div style="height:12px;border-radius:6px;background:#eee;margin-top:14px;overflow:hidden"><div class="pg" style="height:100%;width:${[100,60,0][i]}%;background:var(--accent)"></div></div></div>`,{x:540,w:900,y:320+i*190,at:w(5,'leçons')+i*.25}));
s.add(h.chip('Il reprend là où il s\'est arrêté','f'),{x:540,w:0,y:920,at:w(5,'reprend'),an:'pop',css:{transform:'translateX(-50%)'}});
s.add(`<div class="card" style="transform:rotate(4deg);padding:20px 26px"><div style="font-size:26px;font-weight:800;color:var(--accent)">FICHE</div><div style="font-size:30px;font-weight:700">Allergènes</div></div>`,{x:860,w:250,y:1010,at:w(5,'fiches'),an:'drop'});
// 3. Psychologue du menu
s=J.step(J.scene(t0(6),t0(8)),3,'Le psychologue','du menu');
s.img(J.kit('editorial-mentaliste-carte-menu.png'),{x:330,w:520,y:300,at:t0(6)+.2,an:'up'});
s.add(h.chip('Le plat star en haut','a'),{x:800,w:0,y:420,at:w(7,'haut'),an:'pop',css:{transform:'translateX(-50%)'}});
s.add(`<div class="card" style="text-align:center"><div style="font-size:30px;color:var(--mute);font-weight:700">AU LIEU DE</div><div style="font-size:60px;font-weight:800;text-decoration:line-through;color:#b9b2a4">14,00 €</div><div style="font-size:30px;color:var(--mute);font-weight:700;margin-top:8px">ÉCRIS</div><div style="font-size:76px;font-weight:900;color:var(--accent)">14</div></div>`,{x:800,w:380,y:560,at:w(7,'prix'),an:'zoom'});
s.text('<span class="mute" style="font-size:30px;font-weight:600">pour qu\'on ne compare pas les prix</span>',{y:1150,at:w(7,'compare'),an:'up'});
// 4. L'oreille des clients
s=J.step(J.scene(t0(8),t0(10)),4,'L\'oreille','des clients');
['« Accueil au top, les desserts aussi »','« Trop d\'attente samedi soir »','« On reviendra pour le tiramisu »'].forEach((x,i)=>s.add(`<div class="card" style="padding:20px 28px"><div style="color:#f5a623;font-size:34px">${'★'.repeat([5,3,5][i])}${'☆'.repeat(5-[5,3,5][i])}</div><div style="font-size:32px;font-weight:600">${x}</div></div>`,{x:540+(i%2?60:-60),w:820,y:290+i*175,at:w(9,'colle')+i*.3,an:i%2?'right':'left'}));
s.add(`<div class="card" style="border:3px solid var(--accent)"><div style="font-size:28px;font-weight:800;color:var(--accent);letter-spacing:2px">CE QUI REVIENT</div>${h.check('L\'accueil, les desserts')}${h.check('L\'attente le samedi',false)}</div>`,{x:540,w:860,y:830,at:w(9,'revient'),an:'zoom'});
s.text('<span class="mute" style="font-size:24px">avis d\'exemple</span>',{y:1230,at:w(9,'colle')});
// 5. Le tableau qui parle (curseurs qui bougent)
s=J.step(J.scene(t0(10),t0(12)),5,'Le tableau','qui parle');
let card=s.add(`<div class="card"><div style="font-size:30px;font-weight:800;color:var(--accent);letter-spacing:2px">COÛT D'UNE PIZZA · EXEMPLE</div>
 ${['Mozzarella','Sauce tomate','Pâte'].map((x,i)=>`<div style="margin-top:22px;font-size:32px;font-weight:700;display:flex;justify-content:space-between"><span>${x}</span><span class="q${i}"></span></div><div style="height:14px;background:#eee;border-radius:7px;position:relative"><div class="k${i}" style="position:absolute;top:-10px;width:34px;height:34px;border-radius:50%;background:var(--accent)"></div></div>`).join('')}
 <div style="margin-top:30px;font-size:40px;font-weight:900">Coût du plat : <span class="tot" style="color:var(--accent)"></span></div></div>`,{x:540,w:900,y:330,at:w(11,'tableau')-.6});
s.on(t=>{const q=J.ease((t-w(11,'bouge'))/1.4),g=[120+40*q,80,250];const c=g[0]*.012+g[1]*.004+g[2]*.0016;
  [0,1,2].forEach(i=>{card.querySelector('.q'+i).textContent=Math.round(g[i])+' g';card.querySelector('.k'+i).style.left=(g[i]/300*100-3)+'%';});
  card.querySelector('.tot').textContent=c.toFixed(2).replace('.',',')+' €';});
// Un consultant / une soirée
s=J.scene(t0(12),t0(13));
s.add(`<div class="card" style="text-align:center;opacity:.8"><div style="font-size:30px;color:var(--mute);font-weight:700">UN CONSULTANT</div><div style="font-size:72px;font-weight:900;font-family:var(--title)">des semaines</div></div>`,{x:540,w:820,y:330,at:t0(12)});
s.add(`<div class="card" style="text-align:center;border:4px solid var(--accent)"><div style="font-size:30px;color:var(--mute);font-weight:700">CLAUDE</div><div style="font-size:84px;font-weight:900;font-family:var(--title);color:var(--accent)">une soirée</div></div>`,{x:540,w:820,y:640,at:w(12,'soirée')-.3,an:'slam'});
J.logoArc(s,['claude'],{y:1100,at:w(12,'soirée'),h:70});
// Fin
J.cta(t0(13),{guideTitle:'Les 5 demandes',items:['Mon bras droit','Le prof particulier','Le psychologue du menu','L\'oreille des clients','Le tableau qui parle']});
J.cfg.thumbAt=w(7,'prix')+.8;
