// Épisode 66 — Arrête de parler à Claude comme ça : la phrase EXPERT (inspiré « la phrase d'un ingénieur »)
const {t0,t1,w,h}=J;
J.init({episode:66,keyword:'EXPERT',duoLogo:'claude',
  theme:{vars:{bg:'#14254A',bg2:'#0c1833',bgc:'#1d3566',surf:'#1d3566',line:'#2c4a86',text:'#FFFFFF',mute:'#a9b8d8',accent:'#FFC52E',accent2:'#3FD0A0',hlbg:'#FFC52E',hlfg:'#14254A'}},
  kw:['phrase.','quatre','pro','infos','outils','vérifier','réécrire','gérant.','EXPERT'],red:['arrête']});
const robot=(s,file,x,y,wd,at,an='up')=>s.img(J.kit('ville-pixel-'+file),{x,w:wd,y,at,an});
const box=(t,c='#fff',bg='#1d3566',bd='#FFC52E')=>`<div style="background:${bg};border:4px solid ${bd};border-radius:18px;padding:16px 22px;font-size:34px;font-weight:800;color:${c};text-align:center">${t}</div>`;
// Accroche : texte jaune géant façon affiche
let s=J.hook(0,t0(1),{line:0,hl:['claude'],y:330});
robot(s,'robot-neutre.png',540,820,420,.4,'pop');
s.add('<div class="sticker" style="font-size:90px;background:#d93025;color:#fff">STOP</div>',{x:820,w:0,y:760,at:w(0,'arrête'),an:'stamp'});
// La phrase à coller
s=J.scene(t0(1),t0(2));
s.add(`<div class="card" style="background:#fff;color:#14254A;transform:rotate(-3deg)"><div style="font-size:26px;font-weight:900;color:#c48b00;letter-spacing:2px">TA DEMANDE…</div><div style="height:16px;background:#e5e9f2;border-radius:8px;margin:14px 0"></div><div style="height:16px;width:70%;background:#e5e9f2;border-radius:8px"></div><div style="margin-top:22px;background:#FFC52E;border-radius:12px;padding:14px 18px;font-size:32px;font-weight:900">+ LA PHRASE</div></div>`,{x:540,w:700,y:330,at:t0(1)+.2,an:'drop'});
s.add(h.chip('Tu la colles à la fin','a'),{x:540,w:0,y:820,at:w(1,'colles'),an:'pop',css:{transform:'translateX(-50%)'}});
robot(s,'robot-developpeur.png',540,920,300,w(1,'change'),'pop');
// Les quatre choses (schéma qui se construit)
s=J.scene(t0(2),t0(5));
s.text('<span class="acc">4 CHOSES</span> À TON IA',{y:200,at:t0(2),css:{fontSize:'72px'}});
const Q=[['1 · Ce qu\'un pro ferait de plus','pro'],['2 · Les infos de départ','infos'],['3 · Les outils à utiliser','outils'],['4 · Comment vérifier que c\'est juste','vérifier']];
Q.forEach(([x,k],i)=>s.add(box(x),{x:i%2?780:300,w:440,y:380+Math.floor(i/2)*230,at:w(3,k),an:'pop'}));
s.add(`<div class="kwbox" style="font-size:50px">Réécrire ta demande</div>`,{center:true,y:900,at:w(4,'réécrire'),an:'slam'});
robot(s,'robot-sorcier.png',880,960,220,w(4,'réécrire'),'pop');
// Exemple : le planning
s=J.scene(t0(5),t0(6));
s.text('EXEMPLE',{y:240,at:t0(5),css:{fontSize:'40px',letterSpacing:'10px',color:'#a9b8d8'}});
s.text('Un <span class="hl">planning</span><br>pour mon équipe',{y:320,at:w(5,'planning'),css:{fontSize:'90px'}});
s.img(J.kit('tuto-ecran-sombre-calendrier-semaine.png'),{x:540,w:620,y:640,at:w(5,'équipe'),an:'up'});
// Sans la phrase
s=J.scene(t0(6),t0(7));
s.add('<div class="sticker" style="background:#d93025;color:#fff">SANS LA PHRASE</div>',{x:540,w:0,y:230,at:t0(6),an:'pop',css:{transform:'translateX(-50%)'}});
s.add(`<div class="card" style="background:#fff;color:#14254A"><table style="width:100%;font-size:32px;font-weight:700;border-collapse:collapse">${['Nom','Karim','Léa','Yanis'].map((n,i)=>`<tr style="border-bottom:2px solid #e5e9f2"><td style="padding:12px">${n}</td><td>${i?'11h – 15h':'Horaires'}</td></tr>`).join('')}</table></div>`,{x:540,w:760,y:360,at:w(6,'tableau'),an:'up'});
s.text('<span class="mute" style="font-size:36px">juste des noms et des horaires</span>',{y:820,at:w(6,'horaires')});
// Avec la phrase : il pense comme un gérant
s=J.scene(t0(7),t0(8));
s.add('<div class="sticker" style="background:#3FD0A0;color:#0c1833">AVEC LA PHRASE</div>',{x:540,w:0,y:230,at:t0(7),an:'pop',css:{transform:'translateX(-50%)'}});
s.text('Il pense comme un <span class="hl">vrai gérant</span>',{y:320,at:w(7,'gérant'),css:{fontSize:'60px'}});
['Les heures de pointe','Les jours de repos','Les congés déjà posés','Un planning qui tient dans le budget'].forEach((x,i)=>s.add(h.check(x),{x:540,w:820,y:490+i*125,at:w(7,['heures','jours','congés','planning'][i]),an:'left'}));
// Il réécrit ma demande
s=J.scene(t0(8),t0(9));
s.add(`<div class="card" style="background:#fff;color:#14254A"><div style="font-size:24px;font-weight:900;color:#c48b00;letter-spacing:2px">MA DEMANDE, RÉÉCRITE</div><div style="font-size:32px;font-weight:600;margin-top:10px;line-height:1.4">« Prépare le planning de la semaine pour mon équipe de salle : couvre le coup de feu de midi et du soir, respecte les jours de repos et les congés posés, reste dans mon budget d'heures, et montre-moi comment tu as vérifié. »</div></div>`,{x:540,w:880,y:300,at:t0(8)+.2,an:'drop'});
s.add(h.chip('En mieux','f'),{x:540,w:0,y:900,at:w(8,'mieux'),an:'pop',css:{transform:'translateX(-50%)'}});
// Garde-la
s=J.scene(t0(9),t0(10));
s.text('GARDE<br><span class="hl">CETTE PHRASE</span>',{y:420,at:t0(9),an:'slam',css:{fontSize:'110px'}});
robot(s,'robot-court.png',540,860,300,w(9,'pro'),'pop');
// Fin
J.cta(t0(10),{guideTitle:'La phrase EXPERT',items:['Ce qu\'un pro ferait de plus','Les infos de départ','Les outils à utiliser','Comment vérifier','Réécris ma demande']});
J.cfg.thumbAt=w(4,'réécrire')+.6;
