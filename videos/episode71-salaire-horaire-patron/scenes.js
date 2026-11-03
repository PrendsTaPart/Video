// Épisode 71 — Patron ou salarié : qui gagne le plus à l'heure ? (inspiré « Thomas SMIC vs Lucas RSA »)
const {t0,t1,w,h}=J;
const A='../_journal-63-72/commun/';
J.init({episode:71,keyword:'HEURE',duoLogo:'foodeatup',
  theme:{vars:{bg:'#1d1452',bg2:'#0c3b44',bgc:'#3a2a8a',surf:'#251a63',line:'#3f3196',text:'#FFFFFF',mute:'#b7b0e8',accent:'#2EE59D',accent2:'#FF4D8D',hlbg:'#FFFFFF',hlfg:'#1d1452'}},
  kw:['heure','Karim,','soixante-dix','SMIC.','heures.','reprendre.','Caroline','monte.','HEURE'],red:['moins','minuit.']});
document.getElementById('bg').style.background='linear-gradient(180deg,#1d1452 0%,#2a1c6e 45%,#0c3b44 100%)';
document.head.insertAdjacentHTML('beforeend','<style>#cap{text-transform:uppercase}.money{display:inline-block;background:#fff;color:#1d1452;font-weight:900;font-size:62px;padding:10px 26px;border-radius:20px}.money.g{background:#2EE59D}.money.r{background:#FF4D8D;color:#fff}.tag{display:inline-block;background:rgba(255,255,255,.12);border:2px solid rgba(255,255,255,.25);border-radius:14px;padding:8px 16px;font-size:30px;font-weight:800}</style>');
const K=J.kit;
// Accroche : le patron et le salarié
let s=J.scene(0,t0(1));
s.img(K('iso-duel-nuit-patron.png'),{x:290,w:380,y:420,at:w(0,'patron'),an:'left'});
s.img(K('iso-duel-nuit-serveur.png'),{x:790,w:380,y:420,at:w(0,'salarié'),an:'right'});
s.add('<div class="tag">PATRON</div>',{x:290,w:0,y:360,at:w(0,'patron'),an:'pop',css:{transform:'translateX(-50%)'}});
s.add('<div class="tag">SALARIÉ</div>',{x:790,w:0,y:360,at:w(0,'salarié'),an:'pop',css:{transform:'translateX(-50%)'}});
s.text('Qui gagne le plus<br><span class="hl">à l\'heure ?</span>',{y:150,at:w(0,'gagne'),css:{fontSize:'70px'}});
// Karim : 2 500 € par mois
s=J.scene(t0(1),t0(2));
s.add('<div class="tag">EXEMPLE · KARIM, PATRON DE RESTO</div>',{x:540,w:0,y:200,at:t0(1),an:'pop',css:{transform:'translateX(-50%)'}});
s.img(K('iso-duel-nuit-patron.png'),{x:540,w:440,y:300,at:w(1,'karim'),an:'up'});
const m=s.add('<div class="money g" style="font-size:90px">0 €</div>',{center:true,y:930,at:w(1,'deux'),an:'zoom'});
s.on(t=>{m.firstChild.textContent=Math.round(2500*J.ease((t-w(1,'deux'))/1.2)).toLocaleString('fr-FR')+' € / mois';});
// 70 heures par semaine
s=J.scene(t0(2),t0(3));
s.img(K('commun-horloge-digitale.png'),{x:540,w:420,y:300,at:t0(2),an:'pop'});
const hh=s.add('<div class="money r" style="font-size:96px">0 h</div>',{center:true,y:700,at:w(2,'soixante-dix'),an:'zoom'});
s.on(t=>{hh.firstChild.textContent=Math.round(70*J.ease((t-w(2,'soixante-dix'))/1.1))+' h / semaine';});
// Ramené à l'heure : les barres
s=J.scene(t0(3),t0(4));
s.add('<div class="tag">RAMENÉ À L\'HEURE (EXEMPLE)</div>',{x:540,w:0,y:200,at:t0(3),an:'pop',css:{transform:'translateX(-50%)'}});
J.bars(s,[{l:'Karim · 70 h',v:8.24,c:'#FF4D8D',at:w(3,'ramené')+.3,fmt:x=>x.toFixed(2).replace('.',',')+' €'},{l:'Employé · 35 h',v:9.4,c:'#2EE59D',at:w(3,'employé'),fmt:x=>(x>=9.35?'+ de 9 €':x.toFixed(2).replace('.',',')+' €')}],{y:360,h:520,bw:260,gap:120,max:11});
s.text('<span style="font-size:24px;color:#b7b0e8">2 500 € ÷ 303 h par mois · SMIC net horaire : plus de 9 €</span>',{y:1000,at:w(3,'smic')});
s.add('<div class="money" style="font-size:40px">et rentre chez lui 🏠</div>',{center:true,y:1150,at:w(3,'rentre'),an:'up'});
// Le problème : les heures
s=J.scene(t0(4),t0(5));
s.text('<span style="text-decoration:line-through;color:#8f88c8">son salaire</span>',{y:320,at:t0(4),css:{fontSize:'80px'}});
s.text('ses <span class="hl">heures</span>',{y:500,at:w(4,'heures'),an:'slam',css:{fontSize:'140px'}});
// Les heures perdues
s=J.scene(t0(5),t0(6));
[['📞','Les appels pendant le service','appels'],['🗓️','Le planning du dimanche soir','planning'],['📦','Les commandes à minuit','commandes']].forEach(([i,x,k],j)=>s.add(`<div class="row">${i} ${x}</div>`,{x:540,w:860,y:330+j*150,at:w(5,k),an:'left'}));
s.img(K('commun-patron-inquiet.png'),{x:540,w:300,y:780,at:w(5,'minuit'),an:'up'});
// On les reprend
s=J.scene(t0(6),t0(7));
s.text('Ces heures-là,<br><span class="hl">on les reprend</span>',{y:200,at:t0(6),css:{fontSize:'64px'}});
s.add(`<div class="row"><img src="${A}agent-caroline.jpg" style="width:84px;height:84px;border-radius:50%">Caroline décroche le téléphone<span style="margin-left:auto;color:#2EE59D">✓</span></div>`,{x:540,w:880,y:430,at:w(6,'caroline'),an:'right'});
s.add(`<div class="row">🗓️ Le planning se prépare avec l'IA<span style="margin-left:auto;color:#2EE59D">✓</span></div>`,{x:540,w:880,y:590,at:w(6,'planning'),an:'right'});
s.add(`<div class="row">📦 Le stock bas te prévient<span style="margin-left:auto;color:#2EE59D">✓</span></div>`,{x:540,w:880,y:730,at:w(6,'stock'),an:'right'});
s.add(h.logo('foodeatup',56),{x:540,w:0,y:900,at:w(6,'stock'),an:'pop',css:{transform:'translateX(-50%)'}});
// Le salaire à l'heure monte
s=J.scene(t0(7),t0(8));
J.bars(s,[{l:'Ton salaire à l\'heure',v:10,v0:4,c:'#2EE59D',at:w(7,'heure'),d:1.4,fmt:()=>'↑'}],{y:300,h:600,bw:320,max:10});
s.text('chaque heure récupérée',{y:1060,at:w(7,'récupérée'),css:{fontSize:'50px'}});
// Fin
J.cta(t0(8),{guideTitle:'Calcule ton salaire à l\'heure',items:['Ce que tu te verses','Tes vraies heures','Le calcul','Les heures à reprendre']});
J.cfg.thumbAt=w(3,'employé')+1;
