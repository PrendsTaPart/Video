const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const eio=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
const A=[0,8.54,16.7,30.98,40.42,47.2,57.56,66.54,76.24], P=[0.4,12.2,24.2,40.2,65.2,80.2,98.2,109.6];
const V=(i,w)=>P[i]+(w-A[i]);
const DUR=120;
const SC=[['s1',0,12],['s2',12,24],['s3',24,40],['s4',40,65],['s5',65,73],['s5b',73,80],['s6',80,98],['s7',98,109.6],['s8',109.6,DUR]];
// duos : noms exacts des calques Figma (page Halloween), dans l'ordre des exports d01…d20
const DUOS=[['Vampires gothiques','Comte Carmine','Comtesse Nocturna'],['Sorcière & sorcier','Sorcière des Potions','Sorcier des Ombres'],['Squelettes royaux','Roi Squelette','Reine Squelette'],['Royauté citrouille','Roi Citrouille','Reine Citrouille'],['Mariés fantômes','Marié Fantôme','Mariée Fantôme'],['Momies royales','Pharaon Momie','Reine Momie'],['Laboratoire hanté','Savant Fou','Créature Électrique'],['Loup & lune','Loup-Garou','Enchanteresse Lunaire'],['Zombies chez Jello','Chef Zombie','Serveuse Zombie'],['Araignées royales','Roi Araignée','Reine Araignée']];
const im=k=>`../figma-selection/d${String(k).padStart(2,'0')}.jpg`;
$('r2').innerHTML=Array.from({length:20},(_,k)=>`<div id="g${k}"><img src="${im(k+1)}"></div>`).join('');
$('r3').innerHTML=DUOS.map((d,i)=>`<div class="duo" id="du${i}"><div class="t">${i+1}. ${d[0]}</div><div class="dz" style="left:50px"><img src="${im(2*i+1)}"></div><div class="dz" style="left:550px"><img src="${im(2*i+2)}"></div><div class="n" style="left:50px">${d[1]}</div><div class="n" style="left:550px">${d[2]}</div></div>`).join('');
$('r4').innerHTML=DUOS.map((_,i)=>`<i id="dt${i}"></i>`).join('');
const LAYERS=['Comte Carmine','Comtesse Nocturna','Sorcière des Potions','Sorcier des Ombres','Roi Squelette','Reine Squelette','Roi Citrouille','Reine Citrouille','Marié Fantôme','Mariée Fantôme','Pharaon Momie','Reine Momie','Savant Fou','Créature Électrique','Loup-Garou','Enchanteresse Lunaire','Chef Zombie','Serveuse Zombie','Roi Araignée','Reine Araignée'];
$('f2').innerHTML=LAYERS.map((n,i)=>`<div class="lay" id="ly${i}" style="top:${300+i*52}px">${n}</div>`).join('');
function pop(el,t,a,d=.4,dy=40,sc=0){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`scale(${s})`;}
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=12&&t<109.6)?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s1'?cl(t/.2):cl((t-a)/.22),fo=id==='s8'?1:1-cl((t-(b-.18))/.18);el.style.opacity=Math.min(fi,fo);}}
  if(t<12){pop($('h0'),t,.1,.4,0,.3);pop($('h1'),t,.5,.35,20,.2);pop($('h2'),t,.7,.35,20,.2);slam($('h3'),t,.9);
    pop($('h4'),t,V(0,5.72),.45,80);pop($('h5'),t,V(0,6.6),.45,80);pop($('h6'),t,V(0,7.86),.35,20);
    const z=1+0.04*cl((t-8)/4);$('h4').style.transform+=` scale(${z})`;$('h5').style.transform+=` scale(${z})`;}
  else if(t<24){pop($('c0'),t,12.3,.35,20);pop($('c1'),t,V(1,9.48),.3,20);pop($('c2'),t,V(1,11.88),.3,20);pop($('c3'),t,V(1,13.42),.3,20);pop($('c4'),t,V(1,14.46),.3,20);
    pop($('c5'),t,12.6,.5,80,.05);
    const o=eio(cl((t-V(1,12.2))/1.4));$('c5l').style.transform=`rotateY(${o*180}deg)`;
    const flip=o>.5;$('c5k').style.display=flip?'none':'flex';$('c5d').style.display=flip?'block':'none';$('c5d').style.transform='scaleX(-1)';
    pop($('c6'),t,13.0,.3,10);}
  else if(t<40){pop($('f0'),t,24.3,.35,20);pop($('f1'),t,24.6,.5,80);
    $('f1i').style.transform=`translateY(${-(2400*560/698-1048)*eio(cl((t-V(2,19.86))/9))}px)`;
    LAYERS.forEach((n,i)=>pop($('ly'+i),t,V(2,19.86)+i*.18,.25,15));
    pop($('f3'),t,V(2,25.28),.35,20);pop($('f4'),t,V(2,27.78),.35,20);}
  else if(t<65){const g=t<V(3,40.2);$('r0').style.display=$('r1').style.display=g?'block':'none';$('r2').style.display=g?'grid':'none';
    slam($('r0'),t,V(3,32.34));pop($('r1'),t,V(3,33.16),.35,20);
    for(let k=0;k<20;k++)pop($('g'+k),t,40.4+k*.12,.3,30,.2);
    const t0=V(3,40.2),dd=(65-t0)/10;
    for(let i=0;i<10;i++){const el=$('du'+i);const a=t0+i*dd,on=!g&&t>=a&&t<a+dd;el.style.display=on?'block':'none';
      if(on){const p=eout(cl((t-a)/.35)),q=1-cl((t-(a+dd-.2))/.2);el.style.opacity=Math.min(p,q);el.style.transform=`translateX(${(1-p)*80}px)`;}
      $('dt'+i).className=(!g&&t>=a)?'on':'';}
    $('r4').style.display=g?'none':'flex';}
  else if(t<73){pop($('z0'),t,65.2,.45,60);
    // zooms : découpe (haut), bandeau (bas gauche), QR (bas droite) ; image 900 px
    let s=1,x=0,y=0;const steps=[[1,0,0],[1.9,-405,0],[2.6,0,-1440],[4,-2700,-2700]];const ts=[65.2,V(4,42.4),V(4,43.86),V(4,46.3)];
    for(let k=1;k<4;k++){const p=eio(cl((t-ts[k])/.6));if(t>=ts[k]){s=steps[k-1][0]+(steps[k][0]-steps[k-1][0])*p;x=steps[k-1][1]+(steps[k][1]-steps[k-1][1])*p;y=steps[k-1][2]+(steps[k][2]-steps[k-1][2])*p;}}
    $('z0i').style.transform=`translate(${x}px,${y}px) scale(${s})`;$('z1').style.opacity=0;
    pop($('z2'),t,V(4,42.4),.3,20);pop($('z3'),t,V(4,43.86),.3,20);pop($('z4'),t,V(4,46.3),.3,20);pop($('z5'),t,V(4,46.7),.3,10);}
  else if(t<80){pop($('k0'),t,73.1,.35,20);for(let k=1;k<=6;k++)pop($('k'+k),t,73.4+(k-1)*.8,.3,30,.03);}
  else if(t<98){pop($('x0'),t,80.3,.35,20);pop($('x1'),t,V(5,48.32),.3,30,.03);pop($('x2'),t,V(5,50.34),.3,30,.03);pop($('x3'),t,V(5,52.12),.3,30,.03);
    pop($('x4'),t,V(5,53.66),.3,30,.03);pop($('x5'),t,V(5,55.66),.3,30,.03);pop($('x6'),t,V(5,52.6),.4,60);pop($('x7'),t,V(5,53.0),.4,60);pop($('x8'),t,V(5,57.0),.3,10);}
  else if(t<109.6){pop($('t0'),t,98.3,.35,20);pop($('t1'),t,V(6,59.5),.3,30,.03);pop($('t2'),t,V(6,60.7),.3,30,.03);pop($('t3'),t,V(6,62.44),.3,30,.03);pop($('t4'),t,V(6,64.24),.4,30);}
  else {const B=V(7,72.6);$('e0g').style.display=t<B?'block':'none';$('e4g').style.display=t>=B?'block':'none';
    pop($('e0'),t,109.7,.35,20);pop($('e1'),t,V(7,67.38),.3,20);pop($('e2'),t,V(7,68.5),.3,20);pop($('e3'),t,V(7,69.78),.45,60);
    pop($('e4'),t,B+.05,.4,20);pop($('e5'),t,V(7,74.5),.4,20);slam($('e6'),t,V(7,75.0));pop($('e7'),t,V(7,75.4),.3,20);pop($('e8'),t,V(7,75.8),.3,20);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
