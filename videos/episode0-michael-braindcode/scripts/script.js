const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const A=[0,9.576,20.85,31.032,43.983,54.633,63.022,70.64], P=[1.5,12.6,25.4,37.2,62.8,75.0,94.0];
const V=(i,w)=>P[i]+(w-A[i]);
const SC=[['s0',0,12.0],['s1',12.0,24.6],['s2',24.6,36.6],['s3',36.6,50.6],['s4',50.6,62.4],['s5',62.4,74.4],['s6',74.4,84.0],['s7',84.0,93.6],['s8',93.6,102.4],['s9',102.4,109.6],['s10',109.6,118.0]];
const DUR=118.0;
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
function lines(el,arr,t,a,lps){const n=Math.max(0,Math.floor((t-a)*lps)+(t>=a?1:0));el.innerHTML=arr.slice(0,n).join('\n');}
const CH=[['les équipes',14.02,70,1110],['les stocks',14.74,380,1110],['les fournisseurs',15.34,650,1110],['les clients',16.18,140,1200],['les imprévus',17.0,470,1200]];
$('s1chips').innerHTML=CH.map(([t,,x,y],i)=>`<div class="pill" id="c${i}" style="left:${x}px;top:${y}px">${t}</div>`).join('')+`<div class="badge" id="c5" style="left:150px;top:1310px;font-size:40px">Besoin de meilleurs outils</div>`;
const SL=[['web/foodeatup.png','FoodEatUp'],['img/foodeatup-hub.webp','FoodEatUp · le hub'],['img/rapidocrm-ecran-tableau-de-bord.webp','RapidoCRM'],['img/rapidocms-ecran.webp','RapidoCMS'],['web/rapidocms.png','RapidoCMS · le site'],['web/rapidosoftware.png','RapidoSoftware'],['web/startupforge.png','StartupForge'],['web/plugin.png','Marketplace de plugins'],['web/build.png','BraindCode Build'],['web/planit.png',"Plan'It"]];
$('s4scr').innerHTML=SL.map(([s])=>`<img src="a/${s}" style="opacity:0">`).join('');const s4i=[...$('s4scr').children];
const NET=[['FoodEatUp',90,560],['RapidoCRM',740,560],['RapidoCMS',90,820],['RapidoRH',740,820],["Plan'It",90,1080],['Academy',740,1080]];
$('s5net').innerHTML=`<svg class="abs" id="lnk" style="left:0;top:0" width="1080" height="1920">${NET.map(([t,x,y])=>`<line x1="${x+125}" y1="${y+55}" x2="540" y2="870" stroke="#2f6f9f" stroke-width="4" stroke-dasharray="10 8"/>`).join('')}</svg>`+`<div class="node" id="hub" style="flex-direction:column;left:415px;top:780px;width:250px;height:180px;background:var(--blue);border-color:var(--blue);font-size:32px">Agents IA<br><span style="font-size:20px;font-weight:500">via MCP</span></div>`+NET.map(([t,x,y],i)=>`<div class="node" id="n${i}" style="left:${x}px;top:${y}px">${t}</div>`).join('');
const W5=[['DES OUTILS CONNECTÉS',45.7],['DES AGENTS IA',48.82],['DES COMPÉTENCES',51.72],['DES OBJECTIFS',53.88]];
$('s5w').innerHTML=W5.map(([t],i)=>`<div class="word" id="w5${i}" style="top:${390+i*0}px;font-size:52px;color:${i==3?'var(--orange)':'#fff'}">${t}</div>`).join('');
const TH=['miniature-episode1-1080x1920.jpg','miniature-episode4-1080x1920.jpg','miniature-episode6-1080x1920.jpg','miniature-episode9-1080x1920.jpg'];
$('s6th').innerHTML=TH.map((f,i)=>`<div class="thumbc" id="t${i}" style="left:${60+i*240}px;top:${400+(i%2)*60}px;transform:rotate(${[-5,3,-2,4][i]}deg)"><img src="a/ep/${f}"></div>`).join('');
const T6=[['les idées',58.52],['les tests',59.22],['les développements',59.82],['les difficultés',60.62]];
$('s6tags').innerHTML=T6.map(([t],i)=>`<div class="pill${i==3?' b':''}" id="g${i}" style="left:${[70,330,70,520][i]}px;top:${[1100,1100,1190,1190][i]}px">${t}</div>`).join('');
const L7=['<span class="g">$</span> git log --oneline | wc -l   <span class="m"># dépôt Video</span>','<span class="o">443</span> commits','<span class="g">$</span> marketplace plugin.braindcode.com','<span class="o">33</span> plugins · <span class="o">544</span> skills · <span class="o">77</span> agents','<span class="g">$</span> MCP Formation FoodEatUp','<span class="o">191</span> outils','<span class="g">$</span> Lüks Coffee Recipes (Lovable + Claude)','<span class="o">409</span> commits · 36 pull requests'];
const NX=['miniature-episode5-1080x1920.jpg','miniature-episode9-1080x1920.jpg','miniature-episode6-1080x1920.jpg','miniature-episode4-1080x1920.jpg'];
$('s9th').innerHTML=NX.map((f,i)=>`<div class="thumbc" id="x${i}" style="left:${90+(i%2)*480}px;top:${380+Math.floor(i/2)*560}px;width:420px;height:520px"><img src="a/ep/${f}" style="object-position:top"></div>`).join('');

function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=12&&t<109.6&&!(t>=93.6&&t<102.4))?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.6):cl((t-a)/.3),fo=id==='s10'?1:1-cl((t-(b-.25))/.25);el.style.opacity=Math.min(fi,fo);}}
  if(t<12){const p=$('s0p');const k=eout(cl((t-.2)/.9));p.style.opacity=k;p.style.transform=`scale(${.8+.2*k})`;
    slam($('s0n'),t,V(0,1.1));pop($('s0s'),t,V(0,2.84),.4,20);pop($('s0l'),t,V(0,3.32),.4,20,.1);pop($('s0r'),t,V(0,4.5),.4,10);}
  else if(t<24.6){pop($('s1a'),t,12.2,.5,40,.03);const imgs=['1','3','7','2'];const k=Math.min(3,Math.floor((t-12.2)/3));$('s1img').src='a/img/'+imgs[k]+'.webp';
    CH.forEach(([,w],i)=>slam($('c'+i),t,V(1,w)-.05));const b=$('c5');if(t>=V(1,19.98))slam(b,t,V(1,19.98),'rotate(-2deg)');else b.style.opacity=0;}
  else if(t<36.6){pop($('s2l'),t,V(2,24.94),.4,20,.1);pop($('s2tab'),t,24.8,.5,60,.04);
    [26.3,27.14,28.12].forEach((w,i)=>slam($('w'+i),t,V(2,w)-.05));['d0','d1'].forEach((d,i)=>$(d).style.opacity=t>V(2,[27.0,28.0][i])?1:0);}
  else if(t<50.6){[34.3,35.96,38.3,40.6].forEach((w,i)=>pop($('e'+i),t,V(3,w)-.2,.45,40,.03));}
  else if(t<62.4){const k=Math.min(SL.length-1,Math.floor((t-50.6)/1.18));s4i.forEach((im,i)=>{im.style.opacity=i===k?1:0;im.style.transform=i===k?`scale(${1+.05*cl((t-50.6-k*1.18)/1.18)})`:'';});
    const l=$('s4l');l.textContent=SL[k][1];l.style.opacity=1;}
  else if(t<74.4){pop($('hub'),t,62.6,.5,0,.3);NET.forEach((x,i)=>pop($('n'+i),t,V(4,45.7)+i*.15,.35,20,.1));$('lnk').style.opacity=cl((t-V(4,46.2))/.5);
    let cur=-1;W5.forEach(([,w],i)=>{if(t>=V(4,w))cur=i;});W5.forEach((x,i)=>{const e=$('w5'+i);if(i===cur)slam(e,t,V(4,W5[i][1]));else e.style.opacity=0;});
    pop($('s5r'),t,V(4,53.0),.4,10);}
  else if(t<84){TH.forEach((f,i)=>pop($('t'+i),t,74.6+i*.25,.4,60,.05,`rotate(${[-5,3,-2,4][i]}deg)`));T6.forEach(([,w],i)=>slam($('g'+i),t,V(5,w)-.05));}
  else if(t<93.6){pop($('s7t'),t,84.2,.4,30);lines($('s7pre'),L7,t,84.6,1.3);pop($('s7m'),t,85.0,.5,80);}
  else if(t<102.4){pop($('s8p'),t,93.8,.5,0,.2);pop($('s8a'),t,V(6,64.38)-.2,.45,30);pop($('s8b'),t,V(6,67.24),.4,20);pop($('s8c'),t,V(6,68.7),.4,20);}
  else if(t<109.6){NX.forEach((f,i)=>pop($('x'+i),t,102.6+i*.3,.4,60,.05));}
  else {pop($('s10p'),t,109.8,.5,0,.2);pop($('s10a'),t,110.3,.5,30);pop($('s10b'),t,111.0,.5,20);const b=$('s10c');if(t>=111.8)slam(b,t,111.8,'rotate(-2deg)');else b.style.opacity=0;pop($('s10l'),t,112.6,.5,20,.1);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
