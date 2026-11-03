const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const A=[0,6.6,15.42,34.15,48.5,64.0,76.4,87.55,95.75,102.4], P=[0.5,8.7,18.1,38.2,57.0,73.5,88.2,102.4,111.6];
const V=(i,w)=>P[i]+(w-A[i]);
const DUR=120;
const SC=[['s0',0,8.7],['s1',8.7,18.1],['s2',18.1,V(2,23.48)],['s3',V(2,23.48),38.2],['s4',38.2,V(3,44.52)],['s5',V(3,44.52),52.7],['s6',52.7,57.0],['s7',57.0,73.5],['s8',73.5,88.2],['s9',88.2,102.4],['s10',102.4,111.6],['s11',111.6,DUR]];
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
const TL=[['18/07','Corrigé outils MCP pour JSON',''],['19/07','Ajouté les 4 outils MCP','v0.6.0 → v0.7.0'],['31/07','Ajouté 6 outils MCP',''],['23/08','Ajouté 14 outils MCP lecture','+ registre MCP en base'],['24/08','Ajouté enregistrement MCP',''],['10/10','Implemented MCP widgets',''],['25/10','Récupéré les 4 routes MCP','']];
$('tls').innerHTML=TL.map((r,i)=>`<div class="tl" id="tl${i}" style="top:${320+i*136}px"><b>${r[0]}</b><span>${r[1]}</span><em>${r[2]}</em></div>`).join('');
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=8.7&&t<111.6)?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.2):cl((t-a)/.22),fo=id==='s11'?1:1-cl((t-(b-.18))/.18);el.style.opacity=Math.min(fi,fo);}}
  if(t<8.7){pop($('h0'),t,.1,.4,0,.3);pop($('h2'),t,1.6,.35,30,.2);pop($('h1'),t,2.3,.35,30,.2);
    const k=eout(cl((t-2.7)/.5));$('h3').style.transform=`scaleX(${k})`;$('h3').style.opacity=k>0?1:0;
    const d=cl((t-3.2)/1.2);$('h3d').style.left=(437+((d*3)%1)*180)+'px';$('h3d').style.opacity=t>3.2?1:0;
    pop($('h1c'),t,2.6,.3,10);pop($('h2c'),t,2.6,.3,10);slam($('h4'),t,3.3);pop($('h5'),t,6.7,.4,60,.1);pop($('h6'),t,7.0,.4,60,.1);}
  else if(t<18.1){pop($('b0'),t,9.9,.3,30,.03);pop($('b0a'),t,11.3,.2,-10);pop($('b1'),t,13.9,.3,30,.03);pop($('b1a'),t,14.6,.2,-10);pop($('b2'),t,14.95,.3,30,.03);pop($('b2a'),t,15.9,.2,-10);pop($('b3'),t,16.25,.3,30,.03);pop($('b4'),t,12.6,.3,20);pop($('b5'),t,16.8,.3,10);}
  else if(t<V(2,23.48)){pop($('c0'),t,18.2,.35,20);pop($('c1'),t,V(2,17.98),.3,30,.03);pop($('c2'),t,V(2,19.14),.3,30,.03);pop($('c3'),t,V(2,20.26),.3,30,.03);pop($('c4'),t,V(2,21.72),.3,30,.03);pop($('c5'),t,24.9,.3,10);}
  else if(t<38.2){pop($('d0'),t,V(2,23.5),.35,30);pop($('d1'),t,V(2,26.6),.4,40);pop($('d2a'),t,V(2,29.3),.3,30,.4);pop($('d2b'),t,V(2,30.3),.3,30,.4);pop($('d2c'),t,V(2,31.6),.3,30,.4);slam($('d3'),t,V(2,33.4));pop($('d4'),t,36.9,.3,10);}
  else if(t<V(3,44.52)){[38.4,V(3,39.3),V(3,40.4),V(3,41.3),V(3,42.2),V(3,43.0)].forEach((a,i)=>pop($('p'+i),t,a,.3,30,.03));}
  else if(t<52.7){pop($('k0'),t,V(3,44.55),.35,40);pop($('k1'),t,V(3,46.9),.35,40);}
  else if(t<57.0){pop($('t9'),t,52.75,.3,20);TL.forEach((r,i)=>pop($('tl'+i),t,53.0+i*.42,.25,30,.03));slam($('t8'),t,56.1);}
  else if(t<73.5){pop($('e0'),t,V(4,51.0),.3,40,.3);pop($('e1'),t,V(4,52.75),.3,40,.3);pop($('e2'),t,V(4,54.45),.3,40,.3);pop($('e3'),t,V(4,56.15),.3,40,.3);pop($('e4'),t,V(4,57.6),.3,20);
    pop($('e5'),t,V(4,59.24),.35,30);pop($('e6'),t,V(4,60.9),.35,30);pop($('e7'),t,V(4,62.6),.35,30);pop($('e8'),t,V(4,63.2),.3,10);}
  else if(t<88.2){pop($('f0'),t,V(5,67.2),.3,30,.03);pop($('f1'),t,V(5,67.9),.3,30,.03);pop($('f2'),t,V(5,68.8),.3,30,.03);pop($('f3'),t,V(5,71.7),.35,40);pop($('f4'),t,V(5,73.1),.3,30,.03);pop($('f5'),t,V(5,74.55),.35,40,.05);}
  else if(t<102.4){pop($('r0'),t,V(6,79.4),.4,40);pop($('r1'),t,V(6,82.7),.4,40);slam($('r2'),t,V(6,84.6));pop($('r3'),t,88.5,.4,80);}
  else if(t<111.6){pop($('q0'),t,V(7,87.78),.3,30);pop($('q1'),t,V(7,90.34),.3,30,.1);pop($('q2'),t,V(7,92.28),.3,30);pop($('q3'),t,V(7,94.85),.4,30,.3);}
  else {pop($('z0'),t,111.7,.4,0,.3);pop($('z1'),t,111.9,.4,30);slam($('z2'),t,115.4);slam($('z3'),t,116.1);slam($('z4'),t,116.9);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
