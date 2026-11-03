const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const A=[0,25.55,51.0,59.6], P=[0.6,30.15,57.0];
const V=(i,w)=>P[i]+(w-A[i]);
const DUR=70;
const SC=[['s0',0,V(0,4.36)],['s1',V(0,4.36),V(0,11.92)],['s2',V(0,11.92),V(0,14.06)],['s3',V(0,14.06),V(0,18.44)],['s4',V(0,18.44),26.15],['s5',26.15,V(1,28.4)],['s6',V(1,28.4),V(1,32.38)],['s7',V(1,32.38),V(1,40.84)],['s8',V(1,40.84),V(1,45.68)],['s9',V(1,45.68),57.0],['s10',57.0,V(2,56.42)],['s11',V(2,56.42),DUR]];
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
const PI=[['Idées ?',80,260,-4],['Décision ?',620,300,5],['Qui contacte ?',120,560,3],['Échéance ?',640,620,-3],['Campagne ?',150,880,-2],['Compte rendu…',600,940,4]];
$('s1p').innerHTML=PI.map(([t,x,y,r],i)=>`<div class="pi" id="pi${i}" style="left:${x}px;top:${y}px">${t}</div>`).join('');
const TL=[['A','On lance l\'extension FoodEatUp le mois prochain ?'],['B','Oui. Il nous faut une démo, puis une campagne.'],['A','Je m\'occupe de la démo pour vendredi.'],['B','Et on contacte les clients intéressés.']];
$('s3t').innerHTML=TL.map(([w,t],i)=>`<div class="tl" id="tl${i}" style="top:${860+i*130}px"><b>Participant ${w}</b><span>${t}</span></div>`).join('');
const FL=['RÉUNION','TRANSCRIPTION','ANALYSE IA','DÉCISIONS','TÂCHES','LOGICIELS MÉTIER'];
$('s5f').innerHTML=FL.map((f,i)=>`<div class="fl" id="fl${i}" style="top:${220+i*175}px;${i==5?'background:linear-gradient(90deg,#7C3AED,#E91E8C);border:0':''}">${f}</div>`).join('');
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=V(0,4.36)&&t<V(2,56.42))?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.2):cl((t-a)/.22),fo=id==='s11'?1:1-cl((t-(b-.18))/.18);el.style.opacity=Math.min(fi,fo);}}
  if(t<V(0,4.36)){slam($('s0a'),t,.15);pop($('s0m'),t,.4,.4,80);}
  else if(t<V(0,11.92)){PI.forEach((p,i)=>slam($('pi'+i),t,V(0,4.5)+i*.55,`rotate(${p[3]}deg)`));slam($('s1a'),t,V(0,9.78));}
  else if(t<V(0,14.06)){pop($('s2i'),t,V(0,11.95),.4,0,.5);slam($('s2t'),t,V(0,12.52));}
  else if(t<V(0,18.44)){pop($('s3c'),t,V(0,14.1),.4,40);TL.forEach((l,i)=>pop($('tl'+i),t,V(0,16.34)+i*.4,.3,20));pop($('s3d'),t,V(0,15.0),.3,10);}
  else if(t<26.15){pop($('e0'),t,V(0,19.84),.3,30);pop($('e1'),t,V(0,20.58),.3,30);pop($('e2'),t,V(0,21.46),.3,30);pop($('e3'),t,V(0,24.0),.3,10);}
  else if(t<V(1,28.4)){FL.forEach((f,i)=>pop($('fl'+i),t,26.2+i*.6,.3,30,.15));}
  else if(t<V(1,32.38)){pop($('s6l'),t,V(1,28.45),.35,20,.3);pop($('d0'),t,V(1,28.5),.3,30,.05);pop($('d1'),t,V(1,29.74),.3,30,.05);pop($('d2'),t,V(1,30.74),.3,30,.05);}
  else if(t<V(1,40.84)){pop($('s7k'),t,V(1,32.4),.4,40);pop($('t0'),t,V(1,33.7),.3,30,.03);pop($('t1'),t,V(1,35.26),.3,30,.03);pop($('t2'),t,V(1,37.12),.3,30,.03);slam($('t3'),t,V(1,38.68));}
  else if(t<V(1,45.68)){pop($('r0'),t,V(1,41.8),.3,30,.03);pop($('r1'),t,V(1,43.2),.3,30,.03);}
  else if(t<57.0){pop($('k0'),t,V(1,47.14),.3,30,.2);pop($('k1'),t,V(1,47.6),.3,30,.2);pop($('k2'),t,V(1,48.74),.3,30,.03);pop($('k3'),t,V(1,49.6),.3,30,.03);pop($('k4'),t,V(1,50.3),.3,10);}
  else if(t<V(2,56.42)){pop($('s10a'),t,57.05,.35,20);slam($('s10b'),t,V(2,54.14));}
  else {pop($('s11p'),t,V(2,56.45),.4,0,.3);pop($('s11q'),t,V(2,56.82),.4,30);pop($('s11l'),t,V(2,58.5),.4,20);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
