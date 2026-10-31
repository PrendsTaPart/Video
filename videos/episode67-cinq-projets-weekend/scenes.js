// Épisode 67 — Je t'apprends à construire ça en un week-end : 5 projets (inspiré « Cinq projets utiles avec Claude »)
const {t0,t1,w,h}=J;
const A='../_journal-63-72/commun/';
J.init({episode:67,keyword:'WEEKEND',duoLogo:'claude',stepLabel:'PROJET',
  theme:{cls:'mono',vars:{bg:'#120c08',bg2:'#080504',bgc:'#2a160a',surf:'#1d130d',line:'#4a2a16',text:'#FFF4EA',mute:'#c2a48e',accent:'#FF6B1A',accent2:'#FFB36B',hlbg:'#FF6B1A',hlfg:'#120c08'}},
  kw:['week-end.','cinq','tableau','cerveau.','bilan','contenu.','équipe','Caroline','PrediBot.','WEEKEND'],red:[]});
J.progress(5);
// lueur orange qui respire
J.fx.push(t=>{document.getElementById('bg').style.filter=`brightness(${1+.08*Math.sin(t*1.5)})`;});
const mini=(t)=>`<div style="position:absolute;inset:0;border:2px solid #4a2a16;border-radius:20px;background:#1d130d"></div>`;
// Accroche
let s=J.hook(0,t0(1),{line:0,hl:['week-end.'],y:380,sticker:'JE T\'APPRENDS'});
J.logoArc(s,['claude','lovable'],{y:1000,at:.8,h:56,r:260});
// Cinq projets, ils travaillent pour toi
s=J.scene(t0(1),t0(2));
s.text('CINQ PROJETS<br><span class="acc">UTILES</span>',{y:260,at:t0(1),css:{fontSize:'110px',letterSpacing:'-2px'}});
s.text('<span style="font-size:46px">en un <span class="hl">week-end</span></span>',{y:540,at:w(1,'week-end')});
s.text('<span class="mute" style="font-size:38px;font-weight:700">puis ils travaillent pour toi<br>tous les jours</span>',{y:680,at:w(1,'travaillent')});
// 1. Tableau du matin
s=J.step(J.scene(t0(2),t0(4)),1,'Tableau','du matin');
s.add(`<div class="card"><div style="font-size:42px;font-weight:900">Ta journée</div>
 <div style="display:flex;gap:18px;margin-top:20px">${[['📅','Réservations','ce soir'],['📦','Stocks bas','à commander'],['⭐','Avis du jour','à lire']].map(([i,a,b])=>`<div style="flex:1;background:#120c08;border:2px solid #4a2a16;border-radius:20px;padding:20px;text-align:center"><div style="font-size:60px">${i}</div><div style="font-size:30px;font-weight:800">${a}</div><div style="font-size:24px;color:#c2a48e">${b}</div></div>`).join('')}</div></div>`,{x:540,w:920,y:320,at:w(3,'réservations'),an:'up'});
s.add(h.chip('Tout sur une seule page','f'),{x:540,w:0,y:800,at:w(3,'seule'),an:'pop',css:{transform:'translateX(-50%)'}});
// 2. Deuxième cerveau
s=J.step(J.scene(t0(4),t0(6)),2,'Deuxième','cerveau');
s.add(`<div class="card"><div style="font-size:34px;font-weight:900">📁 Un dossier</div>${['Bail du local.pdf','Facture fournisseur.pdf','Contrat assurance.pdf'].map(x=>`<div style="font-size:28px;margin-top:12px;background:#120c08;border-radius:12px;padding:10px 16px;font-family:JetBrains Mono">📄 ${x}</div>`).join('')}</div>`,{x:540,w:820,y:300,at:w(5,'dossier')-.4,an:'up'});
s.add(`<div class="kwbox" style="font-size:40px">Quand finit mon bail ?</div>`,{center:true,y:760,at:w(5,'quand'),an:'pop'});
s.add(`<div class="kwbox" style="font-size:36px;background:#FFB36B">Combien j'ai payé la mozzarella ?</div>`,{center:true,y:880,at:w(5,'combien'),an:'pop'});
// 3. Bilan du soir
s=J.step(J.scene(t0(6),t0(8)),3,'Bilan','du soir');
s.add(`<div class="card"><div style="font-size:26px;font-weight:800;color:#FF6B1A">CHAQUE SOIR</div><div style="font-size:36px;font-weight:700;margin-top:10px">Qu'est-ce qui a marché ?<br>Qu'est-ce qui a coincé ?</div></div>`,{x:540,w:820,y:320,at:w(7,'soir'),an:'up'});
s.add(`<div style="background:#FF6B1A;color:#120c08;border-radius:26px;padding:24px 30px;font-size:34px;font-weight:800">« Demain : un deuxième commis au coup de feu de 20 h. »</div>`,{x:600,w:720,y:640,at:w(7,'demain'),an:'right'});
s.text('<span class="mute" style="font-size:24px">réponse d\'exemple</span>',{y:900,at:w(7,'demain')});
// 4. Agent de contenu
s=J.step(J.scene(t0(8),t0(10)),4,'Agent de','contenu');
s.add(`<div class="card"><div style="font-size:30px;font-weight:900">Ta fiche de style</div><div style="display:flex;gap:14px;margin-top:16px">${['#FF6B1A','#FFB36B','#FFF4EA','#3a2416'].map(c=>`<div style="width:90px;height:90px;border-radius:16px;background:${c};border:2px solid #4a2a16"></div>`).join('')}</div><div style="font-size:28px;margin-top:14px;color:#c2a48e">Tes photos · ton logo · tes couleurs</div></div>`,{x:540,w:760,y:300,at:w(9,'photos'),an:'up'});
['LUN','MER','VEN'].forEach((d,i)=>s.add(`<div style="background:#1d130d;border:2px solid #FF6B1A;border-radius:20px;padding:16px;text-align:center;width:240px"><div style="height:150px;border-radius:12px;background:linear-gradient(135deg,#FF6B1A,#3a2416)"></div><div style="font-size:26px;font-weight:800;margin-top:10px">Post · ${d}</div></div>`,{x:220+i*320,w:240,y:720,at:w(9,'posts')+i*.15,an:'pop'}));
// 5. Équipe d'IA
s=J.step(J.scene(t0(10),t0(12)),5,'Équipe','d\'IA');
[['agent-caroline.jpg','Caroline','répond au téléphone','répond'],['agent-predibot.jpg','PrediBot','suit les chiffres','chiffres']].forEach(([f,n,r,k],i)=>s.add(`<div class="card" style="text-align:center;padding:24px"><img src="${A}${f}" style="width:300px;height:300px;border-radius:50%;object-fit:cover;border:5px solid #FF6B1A"><div style="font-size:44px;font-weight:900;margin-top:14px">${n}</div><div style="font-size:28px;color:#c2a48e">${r}</div></div>`,{x:i?790:290,w:440,y:320,at:w(11,k),an:'pop'}));
s.add(h.chip('Chez moi','f'),{x:540,w:0,y:900,at:w(11,'chez'),an:'pop',css:{transform:'translateX(-50%)'}});
// Fin
J.cta(t0(12),{guideTitle:'Le guide des 5 projets',items:['Ton tableau du matin','Ton deuxième cerveau','Le bilan du soir','Ton agent de contenu','Ton équipe d\'IA']});
J.cfg.thumbAt=w(11,'chiffres')+.4;
document.head.insertAdjacentHTML('beforeend','<style>.guide .gi b{color:#120c08}</style>');
