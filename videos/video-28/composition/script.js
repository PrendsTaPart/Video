const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const V=w=>0.5+w;
const DUR=73;
const SC=[['s0',0,V(8.18)],['s1',V(8.18),V(20.92)],['s2',V(20.92),V(30.44)],['s3',V(30.44),V(34.94)],['s4',V(34.94),V(47.12)],['s5',V(47.12),V(59.34)],['s6',V(59.34),V(67.02)],['s7',V(67.02),DUR]];
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
const PI=[['Prospecter',90,300,-4,1.94],['Rechercher',600,340,5,2.94],['Récupérer les infos',100,520,3,4.32],['Préparer les e-mails',560,600,-3,5.84],['Gérer les relances',280,780,2,6.9]];
$('s0p').innerHTML=PI.map(([t,x,y,r],i)=>`<div class="pi" id="pi${i}" style="left:${x}px;top:${y}px">${t}</div>`).join('');
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=V(8.18)&&t<V(67.02))?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.2):cl((t-a)/.22),fo=id==='s7'?1:1-cl((t-(b-.18))/.18);el.style.opacity=Math.min(fi,fo);}}
  if(t<V(8.18)){pop($('s0a'),t,.1,.3,20);PI.forEach((p,i)=>slam($('pi'+i),t,V(p[4]),`rotate(${p[3]}deg)`));pop($('s0m'),t,V(7.0),.4,80);}
  else if(t<V(20.92)){slam($('s1a'),t,V(8.3));[13.12,14.34,15.58,16.4].forEach((w,i)=>pop($('c'+i),t,V(w),.3,20,.2));pop($('s1b'),t,V(17.32),.3,20);pop($('s1c'),t,V(19.12),.35,20,.2);pop($('s1d'),t,V(20.22),.35,20,.2);pop($('s1m'),t,V(8.6),.4,80);}
  else if(t<V(30.44)){[23.3,24.86,26.36,27.86,28.88].forEach((w,i)=>pop($('w'+i),t,V(w),.3,30,.03));pop($('w5'),t,V(21.6),.3,10);}
  else if(t<V(34.94)){[30.6,31.2,31.8,32.4].forEach((w,i)=>pop($('t'+i),t,V(w),.25,20,.03));slam($('t4'),t,V(33.74));}
  else if(t<V(47.12)){pop($('d0'),t,V(40.48),.35,30,.1);pop($('d1'),t,V(42.84),.35,30,.1);pop($('d2'),t,V(45.06),.35,30,.1);pop($('d3'),t,V(35.2),.4,80);}
  else if(t<V(59.34)){slam($('k0'),t,V(47.82));pop($('k1'),t,V(51.68),.35,30,.2);slam($('k2'),t,V(53.22));pop($('k3'),t,V(54.0),.3,10);pop($('k4'),t,V(55.12),.3,20);pop($('m0'),t,V(57.2),.25,20,.2);pop($('m1'),t,V(58.0),.25,20,.2);pop($('m2'),t,V(58.84),.25,20,.2);pop($('k5'),t,V(48.0),.4,80);}
  else if(t<V(67.02)){pop($('n0'),t,V(61.2),.3,30,.05);pop($('n1'),t,V(63.1),.3,30,.05);pop($('n2'),t,V(64.32),.3,30,.05);slam($('n3'),t,V(65.56));}
  else {pop($('s7p'),t,V(67.05),.4,0,.3);pop($('s7q'),t,V(67.4),.4,30);pop($('s7l'),t,V(68.6),.4,20);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
