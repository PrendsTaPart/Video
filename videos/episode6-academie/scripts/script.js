const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const A=[0,6.955,16.915,24.857,33.954,48.38,57.664,70.335], P=[2.5,11.0,22.5,32.0,42.6,58.4,68.5,97.6];
const V=(i,w)=>P[i]+(w-A[i]);
const SC=[['s0',0,10.2],['s1',10.2,21.7],['s2',21.7,31.2],['s3',31.2,41.8],['s4',41.8,57.7],['s5',57.7,68.1],['s6',68.1,81.4],['s7',81.4,97.3],['s8',97.3,111.3],['s9',111.3,118.5]];
const DUR=118.5, FPS=30;
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)}) ${rot}`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.28);const s=x<1?1.6-0.6*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
function lines(el,arr,t,a,lps){const n=Math.max(0,Math.floor((t-a)*lps)+(t>=a?1:0));el.innerHTML=arr.slice(0,n).join('\n');}
const keepRot=el=>{el.dataset.r=el.style.transform||'';};
document.querySelectorAll('.panel,.tag,.stamp,.chip').forEach(keepRot);
const R=el=>el.dataset.r||'';

const MCPS=['<span class="g">✓</span> FoodEatUp       <span class="m">foodeatup.com/api/mcp</span>',
 '<span class="g">✓</span> RapidoCRM','<span class="g">✓</span> RapidoCMS','<span class="g">✓</span> RapidoRH',"<span class=\"g\">✓</span> Plan'It",
 '<span class="g">✓</span> Carte · Site · Laboratoire'];
const S3=['<span class="k">describe_server</span>()',
 '<span class="m">→ 191 outils · 122 en lecture · 69 en écriture</span>',
 '<span class="m">→ règle : écriture = </span><span class="o">confirm=true</span><span class="m">, sinon aperçu</span>',
 '<span class="k">list_formations</span>()',
 '<span class="m">→ parcours : FoodEatUp (12 missions), Marketing (7),</span>',
 '<span class="m">  Prospection (7), Piloter FoodEatUp par son MCP (4)…</span>',
 '<span class="k">get_mission</span>("F3")',
 '<span class="m">→ « Stocks et commandes fournisseurs »</span>',
 '<span class="m">→ 5 diapositives narrées · règle : </span><span class="c">préparer, montrer,</span>',
 '<span class="c">  attendre l\'accord</span>'];
const S4=['<span class="k">get_claude_brief</span>()  <span class="m">→ mémoire : </span><span class="o">vide</span><span class="m"> · savoir d\'équipe : 0</span>',
 '<span class="k">recall</span>()            <span class="m">→ notes : [] · propositions : []</span>',
 '<span class="k">list_decisions</span>()    <span class="m">→ « prescripteurs : 20 » (11/10/2026)</span>',
 '<span class="m">savoir « équipe » → validé par le responsable avant partage</span>'];
const FAM=['commercial','marketing','gestion','formation','pilotage'];
const AG=[['Accueil des demandes','Site Admin · Carte · RapidoCRM · 4 routines'],['Relance et devis','Site Admin · RapidoCRM · 2 routines'],['Prescripteurs','RapidoCRM · 5 routines'],['Contenus','RapidoCMS · Site Admin · Carte · 3 routines'],['Veille','aucun connecteur · 2 routines'],['Pilotage',"Plan'It · 4 routines"]];
$('s2tags').innerHTML=[['parcours',80,1180,-3],['missions',330,1240,2],['quiz',600,1180,-2],['exercices',780,1250,3],['suivi des compétences',200,1330,-1]].map(([t,x,y,r],i)=>`<div class="tag${i==4?' b':''}" id="s2g${i}" data-r="rotate(${r}deg)" style="left:${x}px;top:${y}px">${t}</div>`).join('');
$('s4tags').innerHTML=[['préférences',70,470,-3],['objectifs',360,520,2],['corrections',590,465,-2],['méthodes',800,530,3]].map(([t,x,y,r],i)=>`<div class="tag" id="s4g${i}" data-r="rotate(${r}deg)" style="left:${x}px;top:${y}px;font-size:28px">${t}</div>`).join('');
$('s5fam').innerHTML=FAM.map((t,i)=>`<div class="tag${i==4?' b':''}" id="s5f${i}" data-r="rotate(${[-3,2,-2,3,-1][i]}deg)" style="left:${[70,330,600,90,380][i]}px;top:${[400,420,400,480,480][i]}px;font-size:28px;padding:6px 20px">${t}</div>`).join('');
$('s5list').innerHTML=AG.map(([n,s],i)=>`<div class="agent" id="s5a${i}" style="top:${610+i*140}px"><div class="n">${i+1}</div><div class="t">${n}<small>${s}</small></div><div class="s">à configurer</div></div>`).join('');
const LOOP=[['V0','écrite, lancée à la main'],['V1','après 3 exécutions au journal'],['V2','un KPI + 14 jours de mesures']];
$('s6loop').innerHTML=LOOP.map(([v,s],i)=>`<div class="node${i==0?' hl':''}" id="s6n${i}" style="left:120px;width:840px;top:${430+i*170}px">${v}<small>${s}</small></div>`+(i<2?`<div class="arrow" id="s6r${i}" style="left:532px;top:${535+i*170}px;height:56px"></div>`:'')).join('');
const CH=[['Academy','formations, missions, quiz'],['MCP','191 outils'],['Claude','brief + mémoire'],['Agent','rôle, outils, objectifs'],['Routine','prompt en 6 blocs'],['KPI','mesures au journal'],['Amélioration','verdict du vendredi']];
$('chain').innerHTML=CH.map(([t,s],i)=>`<div class="node${i==2?' hl':''}" id="c${i}" style="left:300px;width:680px;top:${370+i*156}px;height:92px">${t}<small>${s}</small></div>`+(i<6?`<div class="arrow" id="ca${i}" style="left:632px;top:${466+i*156}px;height:56px"></div>`:'')).join('')+
 `<div class="abs" id="cl" style="left:985px;top:420px;width:40px;height:950px;border:6px solid var(--orange);border-left:none;border-radius:0 30px 30px 0"></div>`;
document.querySelectorAll('[data-r]').forEach(()=>{});

function render(t){
  $('thumb').style.display='none';$('logo').style.display=t>=111.3?'none':'flex';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?1:cl((t-a)/.3),fo=id==='s9'?1:1-cl((t-(b-.25))/.25);el.style.opacity=Math.min(fi,fo);}}
  if(t<10.2){
    const z=1.08-0.08*cl(t/10);$('s0p').style.transform=`rotate(-1.5deg) scale(${z})`;$('s0p').style.opacity=1;
    slam($('s0c'),t,.15,'rotate(-2deg)');
    const tt=$('s0t');if(t<2.4){slam(tt,t,.35);}else{tt.style.opacity=1-cl((t-2.4)/.3);}
    pop($('s0b1'),t,V(0,0.1),.35,30,.2);
    pop($('s0m'),t,V(0,2.7),.4,60);
    pop($('s0b2'),t,V(0,5.3),.35,30,.25);
    if(t<V(0,0.1)){$('s0b1').style.opacity=0;}
  }
  else if(t<21.7){
    pop($('s1t'),t,V(1,7.1),.4,40);lines($('s1pre'),MCPS,t,V(1,7.4),2.2);
    pop($('s1m'),t,V(1,10.74),.4,60);
    pop($('s1a'),t,V(1,14.6),.3,30,.3,R($('s1a')));pop($('s1b'),t,V(1,15.38),.3,30,.3,R($('s1b')));pop($('s1c'),t,V(1,16.0),.3,30,.3,R($('s1c')));
    pop($('s1k'),t,V(1,12.78),.4,30);
  }
  else if(t<31.2){
    pop($('s2l'),t,21.8,.4,20);
    pop($('s2a'),t,V(2,17.7),.45,60,.05,R($('s2a')));pop($('s2b'),t,V(2,19.14),.45,60,.05,R($('s2b')));
    [20.62,21.38,22.12,22.76,23.74].forEach((w,i)=>{const e=$('s2g'+i);slam(e,t,V(2,w)-.05,e.dataset.r);});
  }
  else if(t<41.8){
    pop($('s3l1'),t,V(3,24.9),.35,30);pop($('s3l2'),t,V(3,26.84),.35,30);
    const w=cl((t-V(3,27.6))/.6);$('s3w').style.clipPath=`inset(0 ${100-w*100}% 0 0)`;$('s3wl').style.opacity=w;
    pop($('s3t'),t,V(3,28.9),.4,40);lines($('s3pre'),S3,t,V(3,29.2),1.6);
  }
  else if(t<57.7){
    [36.4,37.22,38.06,38.94].forEach((w,i)=>{const e=$('s4g'+i);slam(e,t,V(4,w)-.05,e.dataset.r);});
    pop($('s4d'),t,V(4,40.0),.45,40,0,'rotate(-.6deg)');
    $('s4ar').style.width=(cl((t-V(4,40.6))/.8)*95)+'px';
    const s=$('s4s');if(t>=V(4,42.6))slam(s,t,V(4,42.6),'rotate(-8deg)');else s.style.opacity=0;
    pop($('s4t'),t,V(4,44.2),.4,30);lines($('s4pre'),S4,t,V(4,44.4),1.0);
  }
  else if(t<68.1){
    [50.8,51.54,52.26,52.84,53.54].forEach((w,i)=>{const e=$('s5f'+i);slam(e,t,V(5,w)-.05,e.dataset.r);});
    pop($('s5r'),t,V(5,54.1),.3,10);
    for(let i=0;i<6;i++)pop($('s5a'+i),t,V(5,54.28)+i*.35,.35,30,.05);
  }
  else if(t<81.4){
    for(let i=0;i<3;i++){pop($('s6n'+i),t,V(6,59.86)+i*.5,.35,30,.05);if(i<2)pop($('s6r'+i),t,V(6,59.86)+i*.5+.3,.25,10);}
    [['s6v1',64.74,-6],['s6v2',65.62,3],['s6v3',66.38,-4]].forEach(([id,w,r])=>{const e=$(id);if(t>=V(6,w))slam(e,t,V(6,w),`rotate(${r}deg)`);else e.style.opacity=0;});
    pop($('s6t'),t,V(6,62.22),.4,30);
    pop($('s6k'),t,V(6,66.98),.4,30);
  }
  else if(t<97.3){
    pop($('d1'),t,81.8,.4,40);pop($('d2'),t,85.4,.4,40);pop($('d3'),t,89.0,.4,40);pop($('d4'),t,92.6,.4,40);
    const s=$('d4s');if(t>=93.6)slam(s,t,93.6,'rotate(-8deg)');else s.style.opacity=0;
  }
  else if(t<111.3){
    const cw=[70.32,71.9,73.0,74.56,75.58,77.8,78.88];
    cw.forEach((w,i)=>{pop($('c'+i),t,V(7,w)-.1,.35,30,.05);if(i<6)pop($('ca'+i),t,V(7,cw[i+1])-.25,.2,10);});
    const l=cl((t-V(7,79.6))/.8);$('cl').style.opacity=l>0?1:0;$('cl').style.clipPath=`inset(${100-l*100}% 0 0 0)`;
    pop($('s8m'),t,V(7,74.56),.45,80);
    pop($('s8r'),t,V(7,80.84),.3,10);
  }
  else {
    $('s9p').style.opacity=1;$('s9p').style.transform=`rotate(1.5deg) scale(${1.04-0.04*cl((t-111.3)/7)})`;
    slam($('s9t'),t,111.6);pop($('s9b'),t,112.6,.35,20,.2);pop($('s9u'),t,113.4,.4,10);
  }
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logo').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
