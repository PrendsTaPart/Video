// Épisode 73 — J'ai choqué mon développeur en lui présentant ma méthode (RapidoCRM Terrain, avec Sadok)
// Format du Journal : « L'escalier du logiciel » (escalier sombre + cartes claires avec les vrais écrans de l'appli).
const {t0,t1,w,h}=J;
const E=n=>`ecrans/e${String(n).padStart(2,'0')}.png`, K=J.kit;
J.init({episode:73,keyword:'TERRAIN',duoLogo:'lovable',stepLabel:'MARCHE',
  theme:{vars:{bg:'#0c0c0e',bg2:'#060607',bgc:'#1a1412',surf:'#17171a',line:'#2b2b30',text:'#FFFFFF',mute:'#a3a3ab',accent:'#FF5A1F',accent2:'#3FB66B',hlbg:'#FF5A1F',hlfg:'#0c0c0e'}},
  kw:['choqué','Sadok,','idée','méthode,','plan.','construit','secondes','téléphone','cadeau.','RapidoCRM','ressaisie','ligne.','méthode.','TERRAIN'],red:['semaines']});
J.progress(8);
document.head.insertAdjacentHTML('beforeend',`<style>
.ph{border-radius:56px;overflow:hidden;box-shadow:0 40px 90px rgba(0,0,0,.55);border:6px solid #1f1f24;background:#f3f4f8}
.ph img{display:block;width:100%}
.pastel{position:absolute;inset:0}
.stair{position:absolute;left:0;top:0}
.chipw{display:inline-block;background:#fff;color:#1b2340;font-weight:800;font-size:34px;padding:14px 24px;border-radius:18px;box-shadow:0 12px 30px rgba(0,0,0,.25)}
.chipw.g{background:#3FB66B;color:#fff}.chipw.o{background:#FF5A1F;color:#fff}
.url{display:inline-block;background:#1f6b3a;color:#fff;font-weight:800;font-size:40px;padding:16px 34px;border-radius:999px}
.avatar{width:230px;height:230px;border-radius:50%;object-fit:cover;border:7px solid #FF5A1F;box-shadow:0 20px 50px rgba(0,0,0,.5)}
.react{font-size:110px;line-height:1}
.ep37{border-radius:30px;overflow:hidden;border:5px solid #FF5A1F;box-shadow:0 30px 70px rgba(0,0,0,.6)}
.ep37 img{display:block;width:100%}
</style>`);
const ph=(n,wd=470)=>`<div class="ph" style="width:${wd}px"><img src="${E(n)}"></div>`;
const pastel=(c)=>`<div class="pastel" style="background:radial-gradient(900px 900px at 50% 40%,${c},#0c0c0e 75%)"></div>`;
// escalier : 8 marches, la marche k s'allume
const stair=(lit,y=620)=>{let s='';for(let i=0;i<8;i++){const x=90+i*112,yy=y+(7-i)*80;s+=`<div style="position:absolute;left:${x}px;top:${yy}px;width:${1080-x-90}px;height:80px;background:#17171a;border-top:6px solid ${i<lit?'#FF5A1F':'#2b2b30'};${i<lit?'box-shadow:0 -6px 30px rgba(255,90,31,.45)':''}"></div>`;}return `<div class="stair" style="width:1080px;height:1300px">${s}</div>`;};
const spark=(i,y=620)=>({x:90+i*112+56,y:y+(7-i)*80-150});

// ── Accroche : le développeur choqué
let s=J.hook(0,t0(1),{line:0,hl:['choqué'],y:300,sticker:'MA MÉTHODE'});
s.add(`<img class="avatar" src="a/sadok.jpg">`,{x:540,w:230,y:880,at:w(0,'développeur'),an:'pop',css:{transform:'translateX(0)'}});
s.add('<div class="react">😳</div>',{x:700,w:0,y:850,at:w(0,'présentant'),an:'stamp'});
s.add(`<div style="transform:rotate(6deg)">${ph(2,330)}</div>`,{x:880,w:330,y:1080,at:w(0,'méthode'),an:'right'});

// ── Rappel : épisode 37
s=J.scene(t0(1),t0(2));
s.add('<div class="sticker" style="background:#FF5A1F;color:#fff">ÉPISODE 37</div>',{x:540,w:0,y:230,at:t0(1),an:'pop',css:{transform:'translateX(-50%)'}});
s.add(`<div class="ep37" style="width:400px"><img src="a/ep37.png"></div>`,{x:540,w:400,y:320,at:t0(1)+.1,an:'up'});
s.text('« Bravo Sadok ! »',{y:1065,at:w(1,'souviens'),css:{fontSize:'64px'}});
s.text('<span class="mute" style="font-size:40px">il a branché RapidoCRM à l\'IA</span>',{y:1160,at:w(1,'branché')});

// ── L'idée du matin
s=J.scene(t0(2),t0(3),{bg:null});
s.add(stair(0),{x:540,w:1080,y:0,at:t0(2),an:'fade'});
s.img(K('tuto-ecran-sombre-etincelle-orange.png'),{x:spark(0).x,w:150,y:spark(0).y,at:t0(2)+.2,an:'pop'});
s.text('<span class="acc">L\'IDÉE</span> DU MATIN',{y:230,at:t0(2),css:{fontSize:'84px'}});
s.add(`<div class="card" style="text-align:center"><div style="font-size:44px;font-weight:900">Une appli pour les commerciaux</div><div style="font-size:40px;color:#FF5A1F;font-weight:800;margin-top:8px">qui prospectent sur le terrain</div></div>`,{x:540,w:900,y:400,at:w(2,'appli'),an:'up'});
s.text('<span style="font-size:40px;color:#a3a3ab">en haut de l\'escalier : l\'appli en ligne</span>',{y:620,at:w(2,'terrain')});

// ── Des semaines… ou ma méthode
s=J.scene(t0(3),t0(4));
s.add(stair(1),{x:540,w:1080,y:0,at:t0(3),an:'none'});
s.add(`<div class="card" style="text-align:center;opacity:.9"><div style="font-size:30px;color:#a3a3ab;font-weight:800">LUI</div><div style="font-size:56px;font-weight:900">📆📆📆 <span style="color:#ff4d4d">des semaines</span></div></div>`,{x:540,w:860,y:250,at:w(3,'semaines')-.3,an:'left'});
s.add(`<div class="card" style="text-align:center;border:4px solid #FF5A1F"><div style="font-size:30px;color:#FF5A1F;font-weight:800">MOI</div><div style="font-size:60px;font-weight:900">ma méthode, <span class="hl">marche par marche</span></div></div>`,{x:540,w:860,y:470,at:w(3,'montré'),an:'right'});
s.img(K('tuto-ecran-sombre-etincelle-orange.png'),{x:spark(1).x,w:150,y:spark(1).y,at:w(3,'marche'),an:'pop'});

// ── Marches 2-3 : Claude écrit le plan, Lovable construit
s=J.scene(t0(4),t0(5));
s.add(stair(3),{x:540,w:1080,y:0,at:t0(4),an:'none'});
s.add(h.logo('claude',80),{x:330,w:0,y:260,at:w(4,'claude'),an:'pop',css:{transform:'translateX(-50%)'}});
s.add('<div class="chipw">écrit le plan</div>',{x:330,w:0,y:380,at:w(4,'plan'),an:'up',css:{transform:'translateX(-50%)'}});
s.add(h.logo('lovable',130),{x:770,w:0,y:260,at:w(4,'lovable'),an:'pop',css:{transform:'translateX(-50%)'}});
s.add('<div class="chipw o">construit</div>',{x:770,w:0,y:380,at:w(4,'construit'),an:'up',css:{transform:'translateX(-50%)'}});
['L\'appli','Son site','Sa démo'].forEach((x,i)=>s.add(`<div class="chipw g">✓ ${x}</div>`,{x:540,w:0,y:520+i*100,at:[w(4,'construit')+.5,w(4,'site'),w(4,'démo')][i],an:'pop',css:{transform:'translateX(-50%)'}}));
s.img(K('tuto-ecran-sombre-etincelle-orange.png'),{x:spark(3).x,w:150,y:spark(3).y,at:w(4,'construit'),an:'pop'});

// ── Marche 4 : ajouter un prospect (vrais écrans)
s=J.step(J.scene(t0(5),t0(6),{bg:null}),4,'Un prospect en','quelques secondes');
s.add(pastel('#1d3b2a'),{x:540,w:1080,y:0,at:t0(5),an:'fade',css:{left:0,top:0,width:'1080px',height:'1920px'}});
s.add(ph(3,400),{x:290,w:400,y:330,at:t0(5)+.1,an:'left'});
s.add(ph(4,400),{x:790,w:400,y:380,at:w(5,'carte')-.6,an:'right'});
[['🔎 Par son nom','nom,'],['📍 Autour de lui','autour'],['🪪 Carte de visite','carte']].forEach(([x,k],i)=>s.add(`<div class="chipw">${x}</div>`,{x:540,w:0,y:960+i*100,at:w(5,k),an:'left',css:{transform:'translateX(-50%)',zIndex:5}}));

// ── Marche 5 : il tend son téléphone (mode client)
s=J.step(J.scene(t0(6),t0(7)),5,'Il tend son','téléphone');
s.add(pastel('#3b2140'),{at:t0(6),an:'fade',css:{left:0,top:0,width:'1080px',height:'1920px'}});
s.add(`<div style="transform:rotate(-5deg)">${ph(6,400)}</div>`,{x:300,w:400,y:300,at:w(6,'sondage'),an:'left'});
s.add(`<div style="transform:rotate(5deg)">${ph(7,400)}</div>`,{x:790,w:400,y:360,at:w(6,'roue'),an:'right'});
s.add('<div class="chipw o">MODE CLIENT</div>',{x:540,w:0,y:1150,at:w(6,'tend'),an:'stamp',css:{transform:'translateX(-50%)'}});

// ── Marche 6 : consentement + cadeau
s=J.step(J.scene(t0(7),t0(8)),6,'D\'accord','et un cadeau');
s.add(pastel('#2a2f48'),{at:t0(7),an:'fade',css:{left:0,top:0,width:'1080px',height:'1920px'}});
s.add(ph(8,400),{x:290,w:400,y:330,at:t0(7)+.1,an:'left'});
s.add('<div class="chipw g">☐ Case jamais pré-cochée</div>',{x:540,w:0,y:1160,at:w(7,'accord'),an:'pop',css:{transform:'translateX(-50%)'}});
s.add(ph(9,400),{x:790,w:400,y:360,at:w(7,'cadeau'),an:'right'});

// ── Marche 7 : tout arrive dans RapidoCRM
s=J.step(J.scene(t0(8),t0(9)),7,'Tout arrive dans','RapidoCRM');
s.add(pastel('#14324a'),{at:t0(8),an:'fade',css:{left:0,top:0,width:'1080px',height:'1920px'}});
s.add(ph(10,420),{x:290,w:420,y:330,at:t0(8)+.1,an:'up'});
[['👤 Le contact','contact,'],['📊 L\'étape','étape,'],['🔔 La relance','relance.']].forEach(([x,k],i)=>s.add(`<div class="chipw">${x}</div>`,{x:800,w:0,y:420+i*120,at:w(8,k),an:'right',css:{transform:'translateX(-50%)'}}));
s.add(h.logo('rapidocrm',90),{x:800,w:0,y:820,at:w(8,'rapidocrm'),an:'pop',css:{transform:'translateX(-50%)'}});
s.add(`<div class="kwbox" style="font-size:58px;background:#FF5A1F;color:#fff">ZÉRO RESSAISIE</div>`,{center:true,y:1130,at:w(8,'zéro'),an:'slam'});

// ── Marche 8 : en ligne le soir même
s=J.scene(t0(9),t0(10));
s.add(stair(8),{x:540,w:1080,y:0,at:t0(9),an:'none'});
s.img(K('tuto-ecran-sombre-etincelle-orange.png'),{x:spark(7).x,w:150,y:spark(7).y,at:t0(9)+.2,an:'drop'});
s.add(`<div style="transform:rotate(-4deg)">${`<div class="ph" style="width:380px"><img src="a/site-mobile.png"></div>`}</div>`,{x:300,w:380,y:200,at:w(9,'ligne'),an:'up'});
s.add('<div class="url">terrain.rapido-crm.com</div>',{x:540,w:0,y:1110,at:w(9,'ligne'),an:'pop',css:{transform:'translateX(-50%)'}});
s.add('<div class="chipw g" style="font-size:44px">EN LIGNE ✓</div>',{x:780,w:0,y:300,at:w(9,'ligne')+.3,an:'stamp',css:{transform:'translateX(-50%)'}});
s.add(`<img class="avatar" src="a/sadok.jpg" style="width:200px;height:200px">`,{x:780,w:200,y:480,at:w(9,'sadok'),an:'pop'});
s.add('<div class="react" style="font-size:90px">😳</div>',{x:880,w:0,y:470,at:w(9,'revenait'),an:'stamp'});

// ── La morale
s=J.scene(t0(10),t0(11));
s.text('<span style="text-decoration:line-through;color:#6b6b73">Ce n\'est pas l\'outil</span>',{y:500,at:t0(10),css:{fontSize:'78px'}});
s.text('C\'est la <span class="hl">méthode.</span>',{y:700,at:w(10,'méthode'),an:'slam',css:{fontSize:'120px'}});

// ── Fin
J.cta(t0(11),{guideTitle:'La méthode + la démo',items:['L\'idée en une phrase','Claude écrit le plan','Lovable construit l\'appli','Le site et la démo','Le lien de la démo']});
J.cfg.thumbAt=t0(5)+1.5;
