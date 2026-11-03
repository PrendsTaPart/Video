const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const V=w=>0.5+w;
const DUR=67;
const SC=[['s0',0,V(5.2)],['s1',V(5.2),V(10.06)],['s2',V(10.06),V(27.94)],['s3',V(27.94),V(37.74)],['s4',V(37.74),V(45.78)],['s5',V(45.78),V(53.26)],['s6',V(53.26),V(60.48)],['s7',V(60.48),DUR]];
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
const PL=[['Food cost & marge',60,780],['HACCP & traçabilité',540,780],['Salle & réservations',60,860],['Équipe & RH',540,860],['Clients & fidélité',60,940],['IA & technologie',540,940],['Comparatifs',300,1020]];
$('s3p').innerHTML=PL.map(([n,x,y],i)=>`<div class="pl" id="pl${i}" style="left:${x}px;top:${y}px">${n}</div>`).join('');
const LP=[['Tendances',47.38],['Mots-clés',47.86],['Contenu',48.42],['Vérification',50.32],['Publication',49.88],['Mesure',51.74]];
const cx=540,cy=740,R=360;
$('s5l').innerHTML=LP.map(([n],i)=>{const a=-Math.PI/2+i*Math.PI/3;return `<div class="lp" id="lp${i}" style="left:${cx+R*Math.cos(a)-125}px;top:${cy+R*Math.sin(a)-55}px">${n}</div>`}).join('');
const Q='logiciel restaurant';
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=V(5.2)&&t<V(60.48))?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.2):cl((t-a)/.22),fo=id==='s7'?1:1-cl((t-(b-.18))/.18);el.style.opacity=Math.min(fi,fo);}}
  if(t<V(5.2)){slam($('s0a'),t,.15);pop($('s0m'),t,.5,.4,80);}
  else if(t<V(10.06)){pop($('s1a'),t,V(5.3),.35,30);$('s1t').textContent=Q.slice(0,Math.floor(cl((t-V(5.6))/1.5)*Q.length));slam($('s1b'),t,V(7.52));pop($('s1m'),t,V(6.0),.4,80);}
  else if(t<V(27.94)){[12.9,16.86,20.64,24.56].forEach((w,i)=>pop($('w'+i),t,V(w),.35,30,.03));[14.64,15.48,16.26].forEach((w,i)=>pop($('n'+i),t,V(w),.25,10,.3));pop($('w4'),t,V(13.6),.3,10);}
  else if(t<V(37.74)){pop($('m0'),t,V(28.0),.35,20,.2);[31.32,34.04,35.46,36.42].forEach((w,i)=>pop($('t'+i),t,V(w),.3,20,.03));PL.forEach((p,i)=>pop($('pl'+i),t,V(34.1)+i*.12,.25,20,.3));}
  else if(t<V(45.78)){pop($('k0'),t,V(38.64),.3,30,.2);pop($('k1'),t,V(39.6),.3,30,.2);pop($('k2'),t,V(41.22),.3,30,.2);pop($('k3'),t,V(42.52),.35,30);pop($('k4'),t,V(42.9),.35,30);slam($('k5'),t,V(43.92));}
  else if(t<V(53.26)){LP.forEach((l,i)=>pop($('lp'+i),t,V(l[1]),.3,0,.4));pop($('s5c'),t,V(46.6),.3,10);}
  else if(t<V(60.48)){pop($('g0'),t,V(53.3),.35,20);pop($('g1'),t,V(55.48),.35,20);slam($('g2'),t,V(57.76));pop($('g3'),t,V(53.6),.4,80);}
  else {pop($('s7p'),t,V(60.5),.4,0,.3);pop($('s7q'),t,V(60.8),.4,30);pop($('s7l'),t,V(62.0),.4,20);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
