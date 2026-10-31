// Épisode 70 — Espèces ou carte : devine qui perd de l'argent (inspiré « Thomas : espèces ou carte »)
const {t0,t1,w,h}=J;
J.init({episode:70,keyword:'CAISSE',duoLogo:'foodeatup',
  theme:{vars:{bg:'#0b1446',bg2:'#060b2a',bgc:'#1a2a7a',surf:'#16236a',line:'#2b3d96',text:'#FFFFFF',mute:'#aab4e8',accent:'#FF3B5C',accent2:'#2EE59D',hlbg:'#FFFFFF',hlfg:'#0b1446'}},
  kw:['carte','espèces.','vingt','commission.','temps.','vraiment.','FoodEatUp,','reste.','CAISSE'],red:['perd','commission.']});
// ciel étoilé
document.getElementById('bg').insertAdjacentHTML('beforeend',[...Array(70)].map((_,i)=>`<i style="position:absolute;left:${J.rnd(i)*100}%;top:${J.rnd(i+50)*100}%;width:${2+J.rnd(i+9)*3}px;height:${2+J.rnd(i+9)*3}px;border-radius:50%;background:#fff;opacity:${.25+J.rnd(i+3)*.6}"></i>`).join(''));
document.head.insertAdjacentHTML('beforeend','<style>#cap{text-transform:uppercase}.money{display:inline-block;background:#fff;color:#0b1446;font-weight:900;font-size:64px;padding:10px 28px;border-radius:22px;box-shadow:0 0 40px rgba(255,255,255,.25)}.money.g{background:#2EE59D}.money.r{background:#FF3B5C;color:#fff}</style>');
const K=J.kit;
// Accroche : ESPÈCES vs CARTE
let s=J.scene(0,t0(1),{noCap:false});
s.add('<div class="money g">ESPÈCES</div>',{x:290,w:0,y:300,at:w(0,'espèces'),an:'pop',css:{transform:'translateX(-50%) rotate(-6deg)'}});
s.add('<div style="font-size:90px;font-weight:900;color:#aab4e8">VS</div>',{x:540,w:0,y:300,at:w(0,'ou'),an:'pop',css:{transform:'translateX(-50%)'}});
s.add('<div class="money">CARTE</div>',{x:800,w:0,y:300,at:w(0,'carte'),an:'pop',css:{transform:'translateX(-50%) rotate(6deg)'}});
s.img(K('caisse-pizzeria-pizzaiolo-surpris.png'),{x:540,w:440,y:470,at:w(0,'devine'),an:'up'});
s.text('Devine qui <span style="color:#FF3B5C">perd de l\'argent</span>',{y:1180,at:w(0,'devine'),css:{fontSize:'56px'},an:'up'});
// Marco
s=J.scene(t0(1),t0(2));
s.text('Pour le client : <span style="color:#2EE59D">pareil</span>',{y:240,at:t0(1),css:{fontSize:'54px'}});
s.text('Pour le resto : <span style="color:#FF3B5C">pas du tout</span>',{y:330,at:w(1,'resto'),css:{fontSize:'54px'}});
s.img(K('caisse-pizzeria-pizzaiolo-pointe.png'),{x:540,w:440,y:470,at:w(1,'marco'),an:'up'});
s.add('<div class="sticker" style="background:#fff;color:#0b1446">MARCO · PIZZAÏOLO (EXEMPLE)</div>',{x:540,w:0,y:1150,at:w(1,'marco'),an:'pop',css:{transform:'translateX(-50%)'}});
// Paiement par carte : 20 € → 19,80 €
s=J.scene(t0(2),t0(4));
s.img(K('editorial-mentaliste-carte-bancaire-joyeuse.png'),{x:300,w:380,y:300,at:t0(2),an:'left'});
s.add('<div class="money">20,00 €</div>',{x:770,w:0,y:380,at:w(2,'vingt'),an:'pop',css:{transform:'translateX(-50%)'}});
s.add(`<div class="card" style="text-align:center"><div style="font-size:60px">🏦</div><div style="font-size:36px;font-weight:800">La banque prend</div><div style="font-size:30px;color:#aab4e8">une petite commission</div></div>`,{x:300,w:420,y:700,at:w(3,'banque'),an:'up'});
s.add('<div class="money r">− 1 %</div>',{x:770,w:0,y:760,at:w(3,'pour'),an:'stamp',css:{transform:'translateX(-50%)'}});
s.add('<div style="font-size:26px;color:#aab4e8;font-weight:700">taux d\'exemple</div>',{x:770,w:0,y:860,at:w(3,'pour'),an:'up',css:{transform:'translateX(-50%)'}});
const ct=s.add('<div class="money g" style="font-size:90px">20,00 €</div>',{center:true,y:960,at:w(3,'touche'),an:'zoom'});
s.on(t=>{const q=J.ease((t-w(3,'touche'))/1);ct.firstChild.textContent=(20-.2*q).toFixed(2).replace('.',',')+' €';});
// Paiement en espèces : 20 €
s=J.scene(t0(4),t0(5));
s.img(K('caisse-pizzeria-enveloppe-billets.png'),{x:540,w:520,y:280,at:t0(4),an:'drop'});
s.add('<div class="money g" style="font-size:90px">20,00 €</div>',{center:true,y:860,at:w(4,'touche'),an:'slam'});
// Mais le soir… ça coûte du temps
s=J.scene(t0(5),t0(6));
s.add('<div class="sticker" style="background:#fff;color:#0b1446">LE SOIR</div>',{x:540,w:0,y:220,at:t0(5),an:'pop',css:{transform:'translateX(-50%)'}});
[['🧮','Compter la caisse','compter'],['🏦','Aller à la banque','banque'],['⚠️','L\'erreur ou le vol','erreur']].forEach(([i,x,k],j)=>s.add(`<div class="row">${i} ${x}<span style="margin-left:auto;color:#FF3B5C;font-size:32px">⏱</span></div>`,{x:540,w:820,y:340+j*140,at:w(5,k),an:'left'}));
s.add('<div class="money r">ÇA COÛTE DU TEMPS</div>',{center:true,y:820,at:w(5,'temps'),an:'slam'});
s.img(K('commun-horloge-digitale.png'),{x:540,w:340,y:960,at:w(5,'coûte'),an:'pop'});
// Le vrai piège
s=J.scene(t0(6),t0(7));
s.img(K('editorial-mentaliste-point-interrogation.png'),{x:540,w:300,y:250,at:t0(6),an:'pop'});
s.text('Le vrai piège :<br><span class="hl">ne pas savoir</span><br>ce qu\'on paie',{y:620,at:w(6,'savoir'),an:'slam',css:{fontSize:'78px'}});
// FoodEatUp : rapprochement
s=J.scene(t0(7),t0(8));
s.add(h.logo('foodeatup',70),{x:540,w:0,y:230,at:t0(7),an:'pop',css:{transform:'translateX(-50%)'}});
s.text('<span style="font-size:40px;color:#aab4e8">les paiements par carte, rapprochés automatiquement</span>',{y:360,at:w(7,'rapprochés')});
[['Ce qui est entré','entré','#2EE59D'],['Ce qui a été prélevé','prélevé','#FF3B5C'],['Ce qui reste','reste','#FFFFFF']].forEach(([x,k,c],i)=>s.add(`<div class="row" style="border-left:12px solid ${c}">${x}<span style="margin-left:auto;color:${c};font-size:44px">✓</span></div>`,{x:540,w:820,y:520+i*140,at:w(7,k),an:'right'}));
// Fin
J.cta(t0(8),{guideTitle:'Le calcul complet',items:['Ce que coûte la carte','Ce que coûtent les espèces','Le temps du soir','Comment tout suivre']});
J.cfg.thumbAt=w(3,'touche')+1.2;
