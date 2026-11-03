const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const A=[0,13.5,28.75,48.2,62.04], P=[0.6,16.1,34.35,55.8];
const V=(i,w)=>P[i]+(w-A[i]);
const DUR=76;
const SC=[['s0',0,V(0,4.52)],['s1',V(0,4.52),V(0,10.7)],['s2',V(0,10.7),16.1],['s3',16.1,V(1,18.5)],['s4',V(1,18.5),34.35],['s5',34.35,V(2,33.08)],['s6',V(2,33.08),V(2,39.66)],['s7',V(2,39.66),V(2,43.18)],['s8',V(2,43.18),V(2,48.2)],['s9',V(2,48.2),V(3,48.36)],['s10',V(3,48.36),V(3,54.42)],['s11',V(3,54.42),DUR]];
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
// s0 : mosaïque des épisodes
$('s0g').innerHTML=Array.from({length:16},(_,i)=>`<div class="th" id="th${i}" style="left:${30+(i%4)*262}px;top:${40+Math.floor(i/4)*290}px;width:236px;height:270px"><img src="a/thumbs/${String(i+1).padStart(2,'0')}.jpg" style="object-position:top"></div>`).join('');
// s1 : logos en arc
const LG=[['foodeatup.png',60,420,300,110],['rapidocrm.png',380,380,160,150],['rapidocms.png',560,380,160,150],['rapidorh.png',740,380,160,150],['planit.png',90,600,300,100],['braindcode.png',420,610,300,90],['startupforge.webp',760,590,240,110]];
$('s1l').innerHTML=LG.map(([f,x,y,w,h],i)=>`<div class="lw" id="lg${i}" style="left:${x}px;top:${y}px;width:${w}px;height:${h}px"><img src="a/lg/${f}"></div>`).join('');
// s2 : équipe
$('s2d').innerHTML=Array.from({length:6},(_,i)=>`<div class="dot" id="d2${i}" style="left:${210+i*120}px;top:950px;width:90px;height:90px;border-radius:45px"></div>`).join('');
// s4 : orchestration
const ST=[['rapidocms.png','Agent Contenus','publications, webinaire',40,300,V(1,20.12),'#03A9F5','Calendrier éditorial'],['rapidocrm.png','Prescripteurs · Relance et devis','prospects, devis',740,300,V(1,22.24),'#4CAF50','Liste de prescripteurs'],['foodeatup.png','Agent Accueil des demandes','démo, carte, site',40,1220,V(1,24.88),'#007BFF','Créneaux de démo'],['foodeatup-infini.webp','Formation : pas d\'agent dédié','connecteur Tutoriel FoodEatUp',740,1220,V(1,27.04),'#FFA500','Parcours de formation']];
$('s4s').innerHTML=ST.map(([f,a,s,x,y],i)=>`<div class="sat" id="sa${i}" style="left:${x}px;top:${y}px"><div class="lw"><img src="a/lg/${f}"></div><div class="ag">${a}<small>${s}</small></div></div>`).join('');
$('s4l').innerHTML=ST.map(([f,a,s,x,y,t,c],i)=>`<path id="ln${i}" d="M540 900 L${x+150} ${y+(y<900?150:0)}" stroke="${c}" stroke-dasharray="1000" stroke-dashoffset="1000"/>`).join('');
$('s4k').innerHTML=ST.map((s,i)=>`<div class="tk" id="tk${i}">${s[7]}</div>`).join('');
// s5 : MCP
const MC=[['foodeatup.png','foodeatup.com/api/mcp'],['rapidocrm.png','crm.rapidosoftware.com/mcp'],['rapidocms.png','cms.rapidosoftware.com/mcp'],['rapidorh.png','rh.rapidosoftware.com/mcp'],['planit.png','planit.braindcode.com/mcp']];
$('s5r').innerHTML=MC.map(([f,u],i)=>`<div class="row" id="mc${i}" style="top:${400+i*160}px"><div class="lw" style="position:relative;width:200px;height:110px;flex:none"><img src="a/lg/${f}"></div><div class="t" style="font-family:'DejaVu Sans Mono',monospace;font-size:28px">${u}</div><div class="s" style="background:#14532d;color:#86efac">MCP</div></div>`).join('');
// s6 : agents réels
const AG=[['Accueil des demandes','Site Admin · Carte · RapidoCRM',4],['Relance et devis','Site Admin · RapidoCRM',2],['Prescripteurs','RapidoCRM',5],['Contenus','RapidoCMS · Site Admin · Carte',3],['Veille','aucun connecteur imposé',2],['Pilotage','Plan\'It',4]];
$('s6r').innerHTML=AG.map(([n,c,r],i)=>`<div class="agr" id="ag${i}" style="top:${330+i*140}px"><div class="ic">${n[0]}</div><div><b>${n}</b><span>${c}</span></div><div class="st"><i>à configurer</i><em>${r} routines · V0</em></div></div>`).join('');
// s7 : boucle
const LP=['Objectif','Planification','Attribution','Exécution','Contrôle','Résultats','Amélioration'];
$('s7c').innerHTML=LP.map((l,i)=>{const a=-Math.PI/2+i*2*Math.PI/7;return `<div class="lp7" id="lp${i}" style="left:${540+300*Math.cos(a)-125}px;top:${1100+300*Math.sin(a)-42}px">${l}</div>`}).join('');
// s9 : tableau
const KP=[['0','tâches planifiées'],['0','tâches exécutées'],['0','tâches en échec'],['0','livrables produits'],['0','en attente de validation'],['0','KPI mesurés']];
$('s9k').innerHTML=KP.map(([v,l],i)=>`<div class="kp" id="kp${i}" style="left:${60+(i%3)*330}px;top:${260+Math.floor(i/3)*250}px"><b>${v}</b><span>${l}</span></div>`).join('');
// s11 : 100 agents
$('s11d').innerHTML=Array.from({length:100},(_,i)=>`<div class="dot" id="dd${i}" style="left:${45+(i%10)*100}px;top:${470+Math.floor(i/10)*62}px;width:44px;height:44px;opacity:0"></div>`).join('');
$('thl').innerHTML=[['foodeatup.png',40,1380,300,110],['rapidocrm.png',380,1370,150,130],['rapidocms.png',550,1370,150,130],['rapidorh.png',720,1370,150,130],['braindcode.png',40,1530,320,100],['claude.webp',400,1530,300,100],['planit.png',740,1530,300,100]].map(([f,x,y,w,h])=>`<div class="lw" style="left:${x}px;top:${y}px;width:${w}px;height:${h}px"><img src="a/lg/${f}"></div>`).join('');
$('thd').innerHTML=[['Contenus',40,1010],['Prescripteurs',40,1130],['Relance et devis',760,1010],['Pilotage',760,1130]].map(([n,x,y])=>`<div class="pill" style="left:${x}px;top:${y}px;font-size:26px;background:linear-gradient(90deg,#4F2DF9,#FE64D5);border:0">${n}</div>`).join('');
$('thk').innerHTML=[['6','agents préparés'],['20','routines écrites'],['Aperçu','autonomie']].map(([v,l])=>`<div style="display:inline-block;width:240px;text-align:center;color:#fff"><b style="display:block;font-size:${v.length>3?44:64}px;line-height:1.1">${v}</b><span style="font-size:22px;color:#c9b8ff">${l}</span></div>`).join('');
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=V(0,4.52)&&t<V(3,54.42))?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.2):cl((t-a)/.22),fo=id==='s11'?1:1-cl((t-(b-.18))/.18);el.style.opacity=Math.min(fi,fo);}}
  if(t<V(0,4.52)){for(let i=0;i<16;i++)pop($('th'+i),t,.05+i*.17,.25,30,.3,`rotate(${(i%2?2:-2)}deg)`);const p=eout(cl((t-.6)/2.4));$('s0n').textContent=Math.max(1,Math.round(19*p));pop($('s0n'),t,.5,.3,20);pop($('s0l'),t,1.4,.3,20);}
  else if(t<V(0,10.7)){pop($('s1t'),t,V(0,4.6),.4,20);LG.forEach((l,i)=>pop($('lg'+i),t,V(0,5.6)+i*.35,.35,30,.4));pop($('s1m'),t,V(0,4.7),.4,80);}
  else if(t<16.1){pop($('s2a'),t,V(0,10.75),.3,20);slam($('s2b'),t,V(0,10.92));for(let i=0;i<6;i++)pop($('d2'+i),t,13.2+i*.25,.35,30,.5);}
  else if(t<V(1,18.5)){pop($('u0'),t,V(1,15.9),.4,40);pop($('s3d'),t,V(1,17.0),.35,10);pop($('s3m'),t,V(1,13.7),.4,80);}
  else if(t<34.35){pop($('s4c'),t,V(1,18.55),.4,0,.5);pop($('s4p'),t,V(1,19.0),.35,20);
    ST.forEach((s,i)=>{pop($('sa'+i),t,s[5],.35,20,.3);$('ln'+i).style.strokeDashoffset=1000*(1-eout(cl((t-s[5])/.6)));
      const k=$('tk'+i);const tk0=31.4+i*.35;const p=.62*eout(cl((t-tk0)/1.2));const x1=s[3]+150,y1=s[4]+(s[4]<900?150:0);k.style.opacity=t>=tk0?1:0;k.style.left=(540+(x1-540)*p-90)+'px';k.style.top=(900+(y1-900)*p-20)+'px';});
    pop($('s4i'),t,31.4,.4,10);}
  else if(t<V(2,33.08)){MC.forEach((m,i)=>pop($('mc'+i),t,34.45+i*.4,.35,30,.03));}
  else if(t<V(2,39.66)){AG.forEach((a,i)=>pop($('ag'+i),t,V(2,33.2)+i*.3,.35,30,.03));[0,1,2].forEach(i=>pop($('lv'+i),t,V(2,37.8)+i*.25,.3,20));}
  else if(t<V(2,43.18)){[0,1,2,3].forEach(i=>pop($('b'+i),t,V(2,[40.54,41.4,42.34,42.9][i]),.3,20));LP.forEach((l,i)=>pop($('lp'+i),t,V(2,39.8)+i*.22,.3,20,.3));}
  else if(t<V(2,48.2)){pop($('v0'),t,V(2,43.2),.3,30);pop($('v1'),t,V(2,43.66),.3,30);pop($('v2'),t,V(2,44.42),.3,30);slam($('vg'),t,V(2,46.18));slam($('va'),t,V(2,46.96));slam($('vs'),t,V(2,47.86));}
  else if(t<V(3,48.36)){for(let i=0;i<6;i++)pop($('kp'+i),t,V(2,48.2)+.05+i*.1,.25,30,.2);pop($('s9t'),t,V(2,48.2)+.8,.4,20);}
  else if(t<V(3,54.42)){pop($('s10a'),t,V(3,48.4),.35,20);slam($('s10b'),t,V(3,51.02));}
  else {const t0=V(3,54.42);for(let i=0;i<100;i++){const d=$('dd'+i);const a=t0+.9+i*.018;d.style.opacity=cl((t-a)/.2)*.85;}
    slam($('s11a'),t,t0+.1);pop($('s11p'),t,t0+.6,.4,0,.3);pop($('s11i'),t,t0+2.5,.4,10);pop($('s11q'),t,V(3,58.14),.4,30);pop($('s11c'),t,V(3,61.5),.4,20);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
