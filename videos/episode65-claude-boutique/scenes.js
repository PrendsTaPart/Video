// Épisode 65 — Truc de ouf : Anthropic a confié une vraie boutique à Claude (inspiré « L'information IA »)
const {t0,t1,w,h}=J;
J.init({episode:65,keyword:'BOUTIQUE',duoLogo:'claude',
  theme:{cls:'clair',vars:{bg:'#E9E6E0',bg2:'#DCD8D0',bgc:'#F2F0EC',surf:'#FFFFFF',line:'#D6D1C6',text:'#141414',mute:'#7a756c',accent:'#F06A1D',accent2:'#141414',hlbg:'#141414',hlfg:'#fff',title:"'Montserrat'"}},
  kw:['boutique','Claude.','prix,','stock,','réductions','perte.','humain,','Amodei,','règles.','employé.','patron.','BOUTIQUE'],red:['ouf','perte.','débutant.']});
document.getElementById('stage').insertAdjacentHTML('beforeend','<div style="position:absolute;right:60px;top:60px;text-align:right;font-family:Montserrat;font-weight:900;line-height:.95;z-index:28"><div style="font-size:26px">L\'INFO</div><div style="font-size:64px">IA</div></div><div style="position:absolute;left:60px;top:1225px;font-size:20px;color:#7a756c;font-weight:600;z-index:28">Source : Anthropic, expérience « Project Vend », 2025</div>');
const pill=(t,c='#141414',bg='#fff')=>`<span style="display:inline-block;background:${bg};color:${c};font-weight:900;font-size:40px;padding:10px 22px;border-radius:12px;white-space:nowrap;box-shadow:0 10px 30px rgba(0,0,0,.12)">${t}</span>`;
// Accroche
let s=J.hook(0,t0(1),{line:0,hl:['boutique'],y:330,sticker:'TRUC DE OUF'});
s.img(J.kit('ville-pixel-boutique-vitrine.png'),{x:540,w:520,y:760,at:w(0,'boutique')-.2,an:'zoom'});
// L'expérience
s=J.scene(t0(1),t0(2));
s.add(pill('ANTHROPIC'),{x:540,w:0,y:300,at:t0(1),an:'pop',css:{transform:'translateX(-50%)'}});
s.text('<span class="mute" style="font-size:34px;font-weight:700">l\'entreprise qui fabrique</span>',{y:400,at:w(1,'entreprise')});
s.add(h.logo('claude',70),{x:540,w:0,y:460,at:w(1,'claude'),an:'pop',css:{transform:'translateX(-50%)'}});
s.img(J.kit('ville-pixel-boutique-vitrine.png'),{x:540,w:560,y:620,at:w(1,'magasin')-.3,an:'up'});
s.add(`<div class="sticker" style="background:#141414;color:#fff">LE MAGASIN DU BUREAU</div>`,{x:540,w:0,y:1150,at:w(1,'bureaux'),an:'pop',css:{transform:'translateX(-50%)'}});
// Il gère tout
s=J.scene(t0(2),t0(3));
s.img(J.kit('ville-pixel-boutique-vitrine.png'),{x:540,w:520,y:420,at:t0(2),an:'fade'});
[['Les prix',230,330,'prix'],['Le stock',850,330,'stock'],['Les commandes',230,980,'commandes'],['Les clients',850,980,'discussion']].forEach(([x,X,Y,k])=>s.add(pill(x,'#fff','#F06A1D'),{x:X,w:0,y:Y,at:w(2,k),an:'pop',css:{transform:'translateX(-50%)'}}));
s.add('<div class="sticker" style="font-size:90px;background:#141414;color:#fff">TOUT.</div>',{x:540,w:0,y:1080,at:w(2,'tout'),an:'stamp',css:{transform:'translateX(-50%)'}});
// Résultat : qualités puis erreurs
s=J.scene(t0(3),t0(4));
['Poli','Rapide','Toujours disponible'].forEach((x,i)=>s.add(h.check(x),{x:540,w:760,y:330+i*130,at:w(3,['poli','rapide','toujours'][i]),an:'left'}));
s.add(`<div class="kwbox" style="background:#d93025;color:#fff">Erreurs de débutant</div>`,{center:true,y:800,at:w(3,'erreurs'),an:'slam'});
// Réductions et ventes à perte
s=J.scene(t0(4),t0(5));
['-15 %','-25 %','-10 %','-30 %'].forEach((x,i)=>s.add(pill(x,'#fff','#d93025'),{x:220+i*215,w:0,y:330+(i%2)*90,at:w(4,'réductions')+i*.12,an:'pop',css:{transform:'translateX(-50%) rotate('+(i%2?6:-6)+'deg)'}}));
s.text('Des réductions<br>à presque tout le monde',{y:560,at:w(4,'réductions'),css:{fontSize:'64px'}});
s.add(`<div class="card" style="text-align:center;border:4px solid #d93025"><div style="font-size:40px;font-weight:900">Vendu à perte</div><div style="font-size:120px;color:#d93025;line-height:1">↘</div></div>`,{x:540,w:520,y:800,at:w(4,'perte'),an:'zoom'});
s.text('<span class="mute" style="font-size:24px">pourcentages pour illustrer</span>',{y:1190,at:w(4,'réductions')});
// Il se prend pour un humain
s=J.scene(t0(5),t0(6));
s.img(J.kit('holo-nuit-agents-assistant-orange-face.png'),{x:540,w:420,y:300,at:t0(5),an:'up'});
s.add(`<div class="card" style="font-size:40px;font-weight:800;line-height:1.3">« Je livrerai en personne,<br>en veste et cravate. »</div>`,{x:540,w:860,y:760,at:w(5,'persuadé'),an:'drop'});
s.text('<span class="mute" style="font-size:28px;font-weight:700">ce que l\'IA a affirmé · elle n\'a pas de corps</span>',{y:1060,at:w(5,'veste')});
// Dario Amodei
s=J.scene(t0(6),t0(7));
J.photo(s,'../_journal-63-72/wiki/dario.jpg',{name:'Dario Amodei',role:'patron d\'Anthropic',credit:'Photo : Kimberly White / Getty Images for TechCrunch · CC BY 2.0',w:560,y:250,at:w(6,'patron')});
s.add(`<div class="card" style="font-size:44px;font-weight:900;text-align:center">« Ces outils avancent<br><span class="acc">très vite.</span> »</div>`,{x:540,w:820,y:1000,at:w(6,'outils'),an:'up'});
// La leçon
s=J.scene(t0(7),t0(8));
s.text('Une IA <span class="hl">seule</span>',{y:300,at:w(7,'seule'),css:{fontSize:'96px'}});
['Sans règles','Sans outils'].forEach((x,i)=>s.add(h.check(x,false),{x:540,w:640,y:520+i*130,at:w(7,['règles','outils'][i]),an:'left'}));
s.add(`<div class="kwbox" style="background:#141414;color:#fff;font-size:54px">ne tient pas une boutique</div>`,{center:true,y:860,at:w(7,'tient'),an:'slam'});
// FoodEatUp : des agents avec des règles
s=J.scene(t0(8),t0(9));
s.add(h.logo('foodeatup',70),{x:540,w:0,y:270,at:t0(8),an:'pop',css:{transform:'translateX(-50%)'}});
s.img(J.kit('commun-caroline-souriante.png'),{x:300,w:420,y:420,at:w(8,'caroline')-.3,an:'up'});
s.add(`<div class="card" style="border:4px solid var(--accent)"><div style="font-size:26px;font-weight:900;color:var(--accent);letter-spacing:2px">LA RÈGLE DE CAROLINE</div><div style="font-size:36px;font-weight:800;margin-top:8px">Réserver seulement sur les créneaux vraiment libres</div></div>`,{x:760,w:520,y:520,at:w(8,'réserve'),an:'right'});
s.add(h.chip('Rien sans garde-fou','f'),{x:540,w:0,y:960,at:w(8,'règles'),an:'pop',css:{transform:'translateX(-50%)'}});
// Super employé, pas encore patron
s=J.scene(t0(9),t0(10));
s.add(h.check('Super employé'),{x:540,w:700,y:420,at:w(9,'employé'),an:'zoom',css:{fontSize:'52px'}});
s.add(h.check('Patron (pas encore)',false),{x:540,w:700,y:600,at:w(9,'patron'),an:'zoom',css:{fontSize:'52px'}});
// Fin
J.cta(t0(10),{guideTitle:'L\'histoire complète',items:['L\'expérience d\'Anthropic','Ce qui a marché','Les erreurs de Claude','Ce que ça change pour ton resto']});
J.cfg.thumbAt=w(2,'tout')+.3;
