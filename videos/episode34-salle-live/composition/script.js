const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);const eio=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
const A=[0,7.04,15.34,24.78,36.42,45.62,54.46,65.72,72.63],P=[0.4,12.2,27.2,45.2,63.2,80.2,96.2,110.2];
const V=(i,w)=>P[i]+(w-A[i]);const DUR=120;
const SC=[['s1',0,12],['s2',12,27],['s3',27,45],['s4',45,63],['s5',63,80],['s6',80,96],['s7',96,110],['s8',110,DUR]];
const RULES=[['🍽️','Pas encore de commande','no_order'],['🧾',"Attente de l'addition",'bill_wait'],['🧹','Table à débarrasser','to_clear'],['⏳',"Liste d'attente",'waitlist'],['🔥','Rush','rush'],['📡','Boîtier hors ligne','device_offline'],['📈','Affluence supérieure à la prévision','forecast_over']];
$('a2').innerHTML=RULES.map((r,i)=>`<div class="al" id="ar${i}" style="top:${980+i*84}px"><i>${r[0]}</i>${r[1]}<code>${r[2]}</code></div>`).join('');
function pop(el,t,a,d=.4,dy=40,sc=0){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a){const x=cl((t-a)/.3);el.style.opacity=x>0?1:0;el.style.transform=`scale(${x<1?1.5-.5*eout(x):1})`;}
function xf(ids,t,ts){ids.forEach((id,k)=>{const a=ts[k],b=ts[k+1]??1e9;$(id).style.opacity=k===0?1:cl((t-a)/.5);$(id).style.display=t>=a-.01||k===0?'block':'none';});}
function render(t){$('thumb').style.display='none';$('logos').style.display=(t>=12&&t<110)?'flex':'none';
 for(const [id,a,b] of SC){const el=$(id),on=t>=a&&t<b;el.style.display=on?'block':'none';if(on){const fi=id==='s1'?cl(t/.2):cl((t-a)/.22),fo=id==='s8'?1:1-cl((t-(b-.18))/.18);el.style.opacity=Math.min(fi,fo);}}
 if(t<12){pop($('h1'),t,.2,.4,0,.3);$('hm').style.transform=`rotate(${180+t*120}deg)`;$('hh').style.transform=`rotate(${180+t*10}deg)`;pop($('h2'),t,V(0,1.08),.45,40);slam($('h3'),t,V(0,4.86));}
 else if(t<27){pop($('i0'),t,12.3,.35,20);pop($('i1'),t,12.5,.5,60);const z=1+.06*cl((t-12)/15);$('i1').style.transform+=` scale(${z})`;
  xf(['i1a','i1b','i1c','i1d'],t,[0,V(1,11.38),V(1,12.74),V(1,13.7)]);
  pop($('lg1'),t,V(1,11.38),.3,20,.2);pop($('lg2'),t,V(1,12.74),.3,20,.2);pop($('lg3'),t,V(1,13.7),.3,20,.2);pop($('lg4'),t,21.5,.3,20,.2);pop($('i3'),t,22.5,.3,10);}
 else if(t<45){pop($('t0'),t,27.3,.35,20);pop($('t1'),t,27.5,.5,60);xf(['t1a','t1b','t1c'],t,[0,V(2,17.24),V(2,19.74)]);
  const z=1+.25*eio(cl((t-37)/1.2))-.25*eio(cl((t-41.5)/1.2));$('t1').style.transformOrigin='50% 95%';$('t1').style.transform=`scale(${z})`;
  pop($('t2'),t,V(2,22.9),.4,40);$('t2i').style.transform=`translateY(${-60*cl((t-38)/6)}px)`;pop($('t3'),t,39,.3,10);}
 else if(t<63){pop($('c0'),t,V(3,26.38),.3,30,.03);pop($('c1'),t,V(3,28.74),.3,30,.03);pop($('c2'),t,V(3,30.46),.3,30,.03);pop($('c3'),t,V(3,32.48),.3,-10);pop($('c4'),t,V(3,32.6),.35,20,.1);
  pop($('c5'),t,V(3,33.24),.4,40);pop($('c6'),t,V(3,34.6),.3,10);pop($('c7'),t,57.5,.3,10);}
 else if(t<80){pop($('a0'),t,63.3,.35,20);pop($('a1'),t,63.6,.5,60);RULES.forEach((r,i)=>pop($('ar'+i),t,V(4,40.5)+i*.45,.3,30,.03));pop($('a3'),t,74,.3,10);}
 else if(t<96){pop($('p0'),t,80.3,.35,20);pop($('p1'),t,V(5,46.82),.4,40);pop($('p2'),t,V(5,48.76),.4,40);pop($('p3'),t,V(5,50.06),.3,20);pop($('p4'),t,V(5,51.24),.3,20);pop($('p5'),t,V(5,53.0),.3,20);pop($('p6'),t,89.5,.3,10);}
 else if(t<110){pop($('d0'),t,V(6,57.06),.3,20,.2);pop($('d1'),t,V(6,57.78),.3,20,.2);pop($('d2'),t,V(6,58.5),.3,20,.2);pop($('d3'),t,V(6,59.88),.4,40);
  pop($('d4'),t,V(6,61.58),.3,20);pop($('d5'),t,V(6,62.24),.3,20);pop($('d6'),t,V(6,63.52),.3,20);pop($('d7'),t,V(6,64.36),.3,20);pop($('d8'),t,107,.3,10);}
 else{pop($('e0'),t,110.2,.4,0,.3);pop($('e1'),t,110.5,.4,30);pop($('e2'),t,V(7,67.78),.4,20);slam($('e3'),t,V(7,71.4));pop($('e4'),t,V(7,71.8),.3,20);pop($('e5'),t,V(7,72.2),.3,20);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;
