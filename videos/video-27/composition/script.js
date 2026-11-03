// Animation réutilisable « routes n8n → autoroutes MCP » : bâtiments (BD), routes (routes()), autoroute (hw()).
const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const V=w=>0.5+w;
const DUR=76;
const SC=[['s0',0,V(3.64)],['s1',V(3.64),V(12.38)],['s2',V(12.38),V(19.36)],['s3',V(19.36),V(24.26)],['s4',V(24.26),V(35.16)],['s5',V(35.16),V(42.56)],['s6',V(42.56),V(49.58)],['s7',V(49.58),V(60.1)],['s8',V(60.1),V(65.64)],['s9',V(65.64),V(71.06)],['s10',V(71.06),DUR]];
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
// Bâtiments : logos officiels ; RapidoATS et StartupForge sans logo officiel ici, nom en typographie neutre.
const BD=[['foodeatup','<img src="a/lg/foodeatup.png">',90,420],['rapidocrm','<img src="a/lg/rapidocrm.png">',740,420],['rapidocms','<img src="a/lg/rapidocms.png">',60,800],['rapidorh','<img src="a/lg/rapidorh.png">',770,800],['ats','RapidoATS',90,1180],['sf','StartupForge',740,1180]];
$('city').innerHTML=BD.map(([k,h,x,y],i)=>`<div class="bd" id="bd${i}" style="left:${x}px;top:${y}px">${h}</div>`).join('');
const C=BD.map(([k,h,x,y])=>[x+125,y+60]);
// Routes : chaque paire, plusieurs courbes (densification progressive)
const R=[];let seed=7;const rnd=()=>{seed=(seed*9301+49297)%233280;return seed/233280;};
for(let k=0;k<3;k++)for(let i=0;i<6;i++)for(let j=i+1;j<6;j++){const [x1,y1]=C[i],[x2,y2]=C[j];const mx=(x1+x2)/2+(rnd()-.5)*420,my=(y1+y2)/2+(rnd()-.5)*420;R.push(`M${x1} ${y1} Q${mx} ${my} ${x2} ${y2}`);}
$('roads').innerHTML=R.map((d,i)=>`<path id="rd${i}" d="${d}" stroke="#EA4B71" stroke-width="4" fill="none" stroke-linecap="round" opacity="0"/>`).join('');
const L=R.map((d,i)=>$('rd'+i).getTotalLength());
// Autoroute : axe vertical central + bretelles vers chaque bâtiment
$('hw').innerHTML=`<rect id="hwr" x="470" y="300" width="140" height="1160" rx="20" fill="#2b2210" stroke="#FFB300" stroke-width="6" opacity="0"/><line id="hwl" x1="540" y1="300" x2="540" y2="1460" stroke="#fff" stroke-width="6" stroke-dasharray="40 30" opacity="0"/>`+C.map(([x,y],i)=>`<line id="rp${i}" x1="${x}" y1="${y}" x2="${x<540?470:610}" y2="${y}" stroke="#FFB300" stroke-width="10" opacity="0"/><text id="rt${i}" x="${x<540?405:675}" y="${y-22}" fill="#ffe08a" font-size="20" font-weight="700" text-anchor="middle" font-family="Poppins" opacity="0">entrée MCP</text>`).join('');
function roads(t,t0,t1,n0,n1,op){const n=Math.floor(n0+(n1-n0)*cl((t-t0)/(t1-t0)));R.forEach((d,i)=>{const el=$('rd'+i);if(i<n){const p=cl((t-(t0+(i-n0)*(t1-t0)/Math.max(1,n1-n0)))/.5);el.setAttribute('opacity',op);el.setAttribute('stroke-dasharray',L[i]);el.setAttribute('stroke-dashoffset',i<n0?0:L[i]*(1-p));}else el.setAttribute('opacity',0);});}
function hw(t,t0,on){['hwr','hwl'].forEach(id=>$(id).setAttribute('opacity',on?cl((t-t0)/.6):0));C.forEach((c,i)=>{const p=on?cl((t-t0-.6-i*.25)/.3):0;$('rp'+i).setAttribute('opacity',p);$('rt'+i).setAttribute('opacity',p);});if(on){const off=-((t*120)%70);$('hwl').setAttribute('stroke-dashoffset',off);}}
const FL=['9 h · déclencheur','MCP · lire les tâches « Todo »','Filtre : tâches pour agents IA','Todo → Doing','Agent IA + outils MCP','Enregistrer le résultat','Doing → Done'];
$('s6f').innerHTML=FL.map((f,i)=>`<div class="st ${i==1||i==4?'m':''} ${i==4?'a':''}" id="fl${i}" style="top:${200+i*128}px">${f}</div>`).join('');
const FW=[43.28,44.02,44.8,46.68,46.8,48.24,48.94];
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=V(3.64)&&t<V(71.06))?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.2):cl((t-a)/.22),fo=id==='s10'?1:1-cl((t-(b-.18))/.18);el.style.opacity=Math.min(fi,fo);}}
  const cityOn=t>=V(3.64)&&t<V(24.26);$('city').style.display=cityOn?'block':'none';$('map').style.display=cityOn?'block':'none';
  if(cityOn)BD.forEach((b,i)=>pop($('bd'+i),t,V(3.7)+i*.15,.35,20,.3));
  if(t<V(3.64)){slam($('s0a'),t,.15);pop($('s0m'),t,.5,.4,80);}
  else if(t<V(12.38)){pop($('s1a'),t,V(3.7),.3,20);roads(t,V(4.86),V(11.0),0,15,0.9);pop($('s1b'),t,V(9.64),.35,20);hw(t,0,false);}
  else if(t<V(19.36)){pop($('s2a'),t,V(12.4),.3,20);roads(t,V(12.5),V(15.1),15,45,0.9);pop($('s2b'),t,V(16.68),.35,20);hw(t,0,false);}
  else if(t<V(24.26)){roads(t,0,1,45,45,0.25);hw(t,V(19.9),true);pop($('s3a'),t,V(19.4),.3,20);slam($('s3b'),t,V(22.96));}
  else if(t<V(35.16)){[28.22,29.88,31.52,33.08].forEach((w,i)=>pop($('r'+i),t,V(w),.3,30,.03));pop($('r4'),t,V(25.0),.3,10);}
  else if(t<V(42.56)){slam($('n0'),t,V(35.36));pop($('n1'),t,V(35.96),.3,20);pop($('n2'),t,V(38.28),.3,20,.2);pop($('n3'),t,V(39.5),.3,20,.2);pop($('n4'),t,V(40.96),.3,20,.2);pop($('n5'),t,V(36.0),.4,80);}
  else if(t<V(49.58)){FL.forEach((f,i)=>pop($('fl'+i),t,V(FW[i]),.3,20,.05));pop($('d9'),t,V(43.6),.3,10);}
  else if(t<V(60.1)){pop($('i0'),t,V(51.26),.35,20);slam($('i1'),t,V(53.76));pop($('i2'),t,V(49.7),.4,80);}
  else if(t<V(65.64)){pop($('l2'),t,V(60.2),.35,30);pop($('l1'),t,V(61.0),.35,30);pop($('l0'),t,V(62.0),.35,30);pop($('l3'),t,V(63.4),.3,10);}
  else if(t<V(71.06)){slam($('p0'),t,V(65.64));slam($('p1'),t,V(67.36));slam($('p2'),t,V(69.3));pop($('p3'),t,V(70.2),.3,10);pop($('p4'),t,V(65.8),.4,80);}
  else {pop($('s10p'),t,V(71.1),.4,0,.3);pop($('s10q'),t,V(71.4),.4,30);pop($('s10l'),t,V(72.4),.4,20);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('city').style.display='none';$('map').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
