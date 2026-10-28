const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const A=[0,8.92,16.41,23.77,38.21,60.53,69.32,73.44], P=[1.0,12.0,22.0,41.0,72.0,96.0,106.0];
const V=(i,w)=>P[i]+(w-A[i]);
const SC=[['s0',0,11.0],['s1',11.0,21.0],['s2',21.0,30.0],['s3',30.0,40.8],['s4',40.8,V(3,28.68)],['s5',V(3,28.68),56.0],['s6',56.0,71.6],['s7',71.6,V(4,49.6)],['s8',V(4,49.6),95.6],['s9',95.6,105.6],['s10',105.6,120.0]];
const DUR=120.0;
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
function lines(el,arr,t,a,lps){const n=Math.max(0,Math.floor((t-a)*lps)+(t>=a?1:0));el.innerHTML=arr.slice(0,n).join('\n');}
function slides(box,list){box.innerHTML=list.map(s=>`<img src="a/img/${s[0]}" style="opacity:0">`).join('');return [...box.children];}
function show(imgs,list,t,lbl){let k=0;list.forEach((s,i)=>{if(t>=s[2])k=i;});imgs.forEach((im,i)=>{im.style.opacity=i===k?1:0;if(i===k){const z=list[k][3]||[1,1.15,0,0];const f=cl((t-list[k][2])/3);im.style.transformOrigin=`${z[2]}% ${z[3]}%`;im.style.transform=`scale(${z[0]+(z[1]-z[0])*f})`;}});if(lbl)lbl.textContent=list[k][1];}
const P1=[['projets',12.76,70,1170],['équipes',13.5,300,1170],['responsabilités',14.2,520,1170],['travail à réaliser',15.38,240,1260]];
$('s1p').innerHTML=P1.map(([t,,x,y],i)=>`<div class="pill${i==3?' b':''}" id="p1${i}" style="left:${x}px;top:${y}px">${t}</div>`).join('');
const P2=[['responsable',17.22,70,1110],['collaborateurs',18.14,360,1110],['dates',19.16,700,1110],['tâches',19.78,70,1200],['priorités',20.52,280,1200]];
$('s2p').innerHTML=P2.map(([t,,x,y],i)=>`<div class="pill${i==4?' b':''}" id="p2${i}" style="left:${x}px;top:${y}px">${t}</div>`).join('');
const L3=[['hd-k1.png','FoodEatUp · Daily Brief',30.0,[1,1.6,0,15]],['hd-k1.png','Priorité « Urgent » et échéances',33.4,[1.6,1.6,35,15]],['hd-k3.png','Série vidéo IA',36.4,[1,1.5,10,20]]];const i3=slides($('s3scr'),L3);
const L4=[['hd-users.png','Utilisateurs',40.8,[1,1.12,0,0]],['hd-roles.png','Rôles',V(3,25.18),[1,1.12,0,0]],['hd-departements.png','Départements',V(3,25.86),[1,1.12,0,0]]];const i4=slides($('s4scr'),L4);
const L5=['<span class="g">tools/list</span>   <span class="m">→ 24 outils exposés</span>','  <span class="k">get-projects-list-tool</span> · <span class="k">get-project-tasks-tool</span>','  <span class="k">get-users-list-tool</span> · <span class="k">get-dailies-tool</span> · …','<span class="g">get-projects-list-tool</span>()','  <span class="o">→ 3 projets en cours</span>','<span class="g">get-project-tasks-tool</span>(project_id: 1, 2, 3)','  <span class="o">→ 14 tâches · 7 urgentes · 1 en retard</span>','<span class="m"># lecture seule, aucune écriture</span>'];
const R7=[['Lire les projets en cours','get-projects-list-tool'],['Récupérer les tâches ouvertes','get-project-tasks-tool'],['Identifier les échéances proches','calcul de Claude'],['Signaler les blocages','retards, tâches urgentes'],['Préparer un plan d\'action','3 priorités par projet'],['Demander validation','avant toute modification']];
const W7=[40.16,40.16,43.04,41.46,43.72,43.72];
$('s7r').innerHTML=R7.map(([t,s],i)=>`<div class="row" id="q${i}" style="top:${330+i*118}px;padding:12px 20px"><div class="n">${i+1}</div><div class="t" style="font-size:27px">${t}<small>${s}</small></div></div>`).join('');
$('s7o').innerHTML=['Claude Code',"Plan'It",'n8n'].map((t,i)=>`<div class="pill b" id="o${i}" style="left:${60+i*300}px;top:1060px">${t}</div>`).join('')+`<div class="real" id="o3" style="left:70px;top:1160px">Il faut un orchestrateur pour lancer une routine : RapidoRH n'a ni tâche planifiée ni file d'attente</div>`;
const T8=[['Sarah','Brancher le MCP FoodEatUp','Routine du matin : signale le retard','25/10','En cours'],['Yanis','Écran « priorités du jour »','Claude prépare la maquette','27/10','À faire'],['Inès','Tests de bout en bout','Agent QA (vidéo 14)','01/11','À faire'],['Michael','Valider le plan du jour','—','26/10','Décision']];
$('s8t').innerHTML=`<tr><th>Responsable</th><th>Tâche</th><th>Agent ou routine</th><th>Échéance</th><th>Statut</th></tr>`+T8.map((r,i)=>`<tr id="u${i}"><td>${r[0]}</td><td>${r[1]}</td><td class="ag">${r[2]}</td><td>${r[3]}</td><td>${r[4]}</td></tr>`).join('');
// schéma d'architecture
const N=[['Michael (humain)','décide, valide',60,380,'#FFA500'],['Orchestrateur','Claude Code · Plan\'It · n8n',560,380,'#007BFF'],['Claude','analyse, propose, rédige',310,620,'#c4b5fd'],['MCP RapidoRH','/mcp/rapidorh · auth:api',310,860,'#86efac'],['RapidoRH','projets · tâches · équipes · dailies',310,1100,'#fff']];
$('sch').innerHTML=`<svg class="abs" style="left:0;top:0" width="1080" height="1920"><g stroke="#4b5d70" stroke-width="5" fill="none"><path d="M270 480 L470 620"/><path d="M770 480 L610 620"/><path d="M540 720 L540 860"/><path d="M540 960 L540 1100"/><path d="M250 380 C250 300 780 300 780 380" stroke-dasharray="10 8"/></g></svg>`+N.map(([t,s,x,y,c])=>`<div class="fc" style="left:${x}px;top:${y}px;width:460px;height:100px;border-color:${c};text-align:center"><div style="color:${c};font-size:30px">${t}</div><div style="font-size:19px;color:var(--grey);font-weight:500">${s}</div></div>`).join('')+`<div class="real" style="left:70px;top:1260px">Pointillé : validation humaine avant toute écriture (create-task-tool, move-task-tool…)</div>`;
function render(t){
  for(const id of ['thumb','schema'])$(id).style.display='none';$('logos').style.display=(t>=11&&t<95.6)?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.4):cl((t-a)/.25),fo=id==='s10'?1:1-cl((t-(b-.2))/.2);el.style.opacity=Math.min(fi,fo);}}
  if(t<11){[[0,1.46],[1,1.8],[2,2.1],[3,3.0],[4,4.1],[5,4.66],[6,4.9]].forEach(([i,w])=>pop($('f'+i),t,V(0,w),.35,30,.1));pop($('s0m'),t,V(0,5.5),.5,80);slam($('s0q'),t,V(0,7.42));}
  else if(t<21){pop($('s1tab'),t,11.1,.5,50,.03);pop($('s1l'),t,V(1,10.04),.4,10,.1);P1.forEach(([,w],i)=>slam($('p1'+i),t,V(1,w)-.05));}
  else if(t<30){pop($('s2tab'),t,21.1,.5,50,.03);P2.forEach(([,w],i)=>slam($('p2'+i),t,V(2,w)-.05));}
  else if(t<40.8){show(i3,L3,t,$('s3l'));}
  else if(t<V(3,28.68)){show(i4,L4,t,$('s4l'));}
  else if(t<56){pop($('s5q'),t,V(3,28.8),.4,30);pop($('s5t'),t,V(3,32.46)-.2,.4,30);lines($('s5pre'),L5,t,V(3,32.6),1.1);}
  else if(t<71.6){[56.3,58.0,59.6,61.2].forEach((a,i)=>pop($('r'+i),t,a,.4,40,.03));pop($('s6t'),t,64.0,.4,30);slam($('s6b'),t,67.0,'rotate(-2deg)');}
  else if(t<V(4,49.6)){W7.forEach((w,i)=>pop($('q'+i),t,V(4,w)-.3+i*.15,.35,30,.03));[0,1,2].forEach(i=>slam($('o'+i),t,V(4,46.24)+i*.5));pop($('o3'),t,V(4,47.6),.4,10);pop($('s7d'),t,V(4,48.6),.4,10);}
  else if(t<95.6){T8.forEach((r,i)=>pop($('u'+i),t,V(4,51.46)-.5+i*1.0,.4,30));pop($('s8q'),t,V(4,56.38),.4,30);}
  else if(t<105.6){pop($('s9p'),t,95.8,.5,0,.2);pop($('s9a'),t,V(5,61.16)-.2,.4,20);[65.02,66.42,67.98].forEach((w,i)=>slam($('w'+i),t,V(5,w)));}
  else {pop($('s10p'),t,105.8,.5,0,.2);pop($('s10a'),t,V(6,70.1),.5,30);pop($('s10b'),t,111.5,.5,20);pop($('s10l'),t,112.6,.5,20,.1);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('schema').style.display='none';$('thumb').style.display='block';}
function schema(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='none';$('schema').style.display='block';}
window.render=render;window.thumb=thumb;window.schema=schema;window.DUR=DUR;
