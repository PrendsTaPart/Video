// Épisode 69 — Claude a tué le business des agences web (inspiré « les outils gratuits de Google », face caméra + écrans)
const {t0,t1,w,h}=J;
const A='../_journal-63-72/commun/';
J.init({episode:69,keyword:'OUTILS',duoLogo:'claude',
  theme:{vars:{bg:'#111114',bg2:'#09090b',bgc:'#1b1b22',surf:'#1b1b22',line:'#30303a',text:'#FFFFFF',mute:'#a3a3b0',accent:'#7C5CFF',accent2:'#FF5C8A',hlbg:'#FFFFFF',hlfg:'#111114'}},
  kw:['agences','Lovable.','Claude.','Canva.','ElevenLabs.','RapidoCMS.','orchestre,','toi.','OUTILS'],red:['tué']});
const big=(n)=>`<div style="font-family:Poppins;font-weight:900;font-size:260px;line-height:1;background:linear-gradient(180deg,#fff,#7C5CFF);-webkit-background-clip:text;color:transparent">${n}</div>`;
const name=(t)=>`<span style="display:inline-block;background:#fff;color:#111;font-weight:900;font-size:56px;padding:14px 30px;border-radius:18px">${t}</span>`;
const shot=(src)=>`<div style="border-radius:28px;overflow:hidden;border:3px solid #30303a;box-shadow:0 30px 80px rgba(0,0,0,.5)"><img src="${src}" style="width:100%;display:block"></div>`;
// Accroche sur la photo de Michael (comme la face caméra)
let s=J.scene(0,t0(2),{bg:A+'michael-portrait.jpg',kb:[1.15,1.3],filter:'brightness(.45)',noCap:false});
s.add(`<div class="hookt">Claude a <span style="color:#ff4d4d">tué</span> le business des <span class="hl">agences web</span>.</div>`,{x:540,w:960,y:260,at:.3,an:'slam',d:.4});
s.add(`<div class="card" style="text-align:center"><div style="font-size:30px;color:#a3a3b0;font-weight:700">AVANT</div><div style="font-size:46px;font-weight:900">Une agence · des semaines · 💸💸💸</div></div>`,{x:540,w:880,y:820,at:w(1,'avant'),an:'up'});
s.add(`<div class="sticker" style="background:#7C5CFF;color:#fff">AUJOURD'HUI : MES VRAIS OUTILS</div>`,{x:540,w:0,y:1080,at:w(1,'aujourd'),an:'pop',css:{transform:'translateX(-50%)'}});
// Les cinq outils
const T=[[2,3,'1',h.logo('lovable',170),A+'capture-site-michael.png','Mon site, fait avec Lovable'],
 [4,5,'2',h.logo('claude',80),null,'Mon chef de chantier'],
 [6,7,'3',h.logo('canva',120),null,'Affiches et menus à imprimer'],
 [8,9,'4',h.logo('elevenlabs',56),null,'La voix de mes vidéos'],
 [10,11,'5',h.logo('rapidocms',120),null,'Tous les réseaux en une fois']];
const ends=[t0(4),t0(6),t0(8),t0(10),t0(12)];
T.forEach(([a,b,n,logo,img,sub],k)=>{const s=J.scene(t0(a),ends[k]);
  s.add(big(n),{x:180,w:0,y:150,at:t0(a),an:'slam',css:{transform:'translateX(-50%)'}});
  s.add(`<div>${logo}</div>`,{x:620,w:0,y:230,at:t0(a)+.1,an:'pop',css:{transform:'translateX(-50%)'}});
  if(img)s.add(shot(img),{x:540,w:940,y:470,at:t0(b),an:'up'});
  if(k===1){['Il écrit les textes','Il vérifie tout','Il pilote les autres outils'].forEach((x,i)=>s.add(h.check(x),{x:540,w:820,y:500+i*130,at:w(b,['écrit','vérifie','pilote'][i]),an:'left'}));}
  if(k===2){['Affiche','Menu','Flyer'].forEach((x,i)=>s.add(`<div style="width:260px;height:360px;border-radius:20px;background:linear-gradient(160deg,#7C5CFF,#FF5C8A);display:flex;align-items:flex-end;justify-content:center;padding:20px;font-size:40px;font-weight:900;transform:rotate(${(i-1)*6}deg)">${x}</div>`,{x:220+i*320,w:260,y:520,at:w(b,'affiches')+i*.15,an:'drop'}));}
  if(k===3){s.add(`<div class="card" style="text-align:center"><div style="display:flex;gap:10px;justify-content:center;align-items:flex-end;height:180px" class="eq">${[...Array(16)].map(()=>'<i style="display:block;width:22px;border-radius:11px;background:#7C5CFF"></i>').join('')}</div><div style="font-size:40px;font-weight:900;margin-top:20px">« Celle que tu entends en ce moment »</div></div>`,{x:540,w:880,y:520,at:t0(b),an:'up'});
    s.on(t=>{document.querySelectorAll('.eq i').forEach((e,i)=>e.style.height=(30+140*Math.abs(Math.sin(t*9+i*.7)))+'px');});}
  if(k===4){['Instagram','Facebook','LinkedIn','TikTok','YouTube'].forEach((x,i)=>s.add(h.chip(x,i%2?'a':'b'),{x:540,w:0,y:520+i*95,at:w(b,'réseaux')+i*.12,an:'pop',css:{transform:'translateX(-50%)'}}));}
  s.add(`<div style="font-size:40px;font-weight:800;color:#a3a3b0;text-align:center">${sub}</div>`,{center:true,y:1150,at:t0(b),an:'up'});
});
// Ils se parlent tous : Claude au centre, les autres autour
s=J.scene(t0(12),t0(13));
s.add(h.logo('claude',90),{x:540,w:0,y:520,at:w(12,'claude')-.2,an:'pop',css:{transform:'translate(-50%,-50%)'}});
const around=[[h.logo('lovable',130),250,260],[h.logo('canva',100),830,260],[h.logo('elevenlabs',44),230,820],[h.logo('rapidocms',100),850,820]];
around.forEach(([html,x,y],i)=>s.add(`<div style="transform:scale(.8)">${html}</div>`,{x,w:0,y,at:w(12,'parlent')+i*.15,an:'pop',css:{transform:'translate(-50%,-50%)'}}));
s.add(`<svg width="1080" height="1100" style="position:absolute;left:0;top:0"><g stroke="#7C5CFF" stroke-width="6" stroke-dasharray="14 12" fill="none"><line x1="540" y1="520" x2="250" y2="260"/><line x1="540" y1="520" x2="830" y2="260"/><line x1="540" y1="520" x2="230" y2="820"/><line x1="540" y1="520" x2="850" y2="820"/></g></svg>`,{at:w(12,'parlent'),an:'fade',css:{left:'0',top:'0'}});
s.text('Je décris · Claude orchestre · <span class="hl">ça sort</span>',{y:1060,at:w(12,'décris'),css:{fontSize:'44px'}});
// L'agence, c'est toi
s=J.scene(t0(13),t0(14),{bg:A+'michael-portrait.jpg',kb:[1.2,1.28],filter:'brightness(.5)'});
s.text('L\'agence,<br>maintenant,<br><span class="hl">c\'est toi.</span>',{y:380,at:t0(13),an:'slam',css:{fontSize:'110px'}});
// Fin
J.cta(t0(14),{guideTitle:'Mes outils (avec les liens)',items:['Lovable · le site','Claude · le chef de chantier','Canva · affiches et menus','ElevenLabs · la voix','RapidoCMS · les réseaux']});
J.cfg.thumbAt=t0(3)+1.2;
