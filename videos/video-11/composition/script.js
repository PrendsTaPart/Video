const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const O=0.6, W=w=>O+w;
const SC=[['s0',0,3.9],['s1',3.9,7.2],['s2',7.2,11.9],['s3',11.9,14.5],['s4',14.5,23.6],['s5',23.6,27.5],['s6',27.5,31.7],['s7',31.7,36.0]];
const DUR=36.0;
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
const S4=[['s-cdf1.png','Le Coup de Feu · saison 1',14.5],['s-journee.png','Une journée · saison 1',16.6],['s-upeat.png','UpEatFood · saison 1',18.6],['s-cdf8.png','Le Coup de Feu · saison 8',20.6],['clips.png','Les clips musicaux',22.2]];
$('s4scr').innerHTML=S4.map(s=>`<img src="a/img/${s[0]}" style="opacity:0">`).join('');const s4i=[...$('s4scr').children];
const P4=[['Scénarios',20.0,70,1200],['Images',20.7,330,1200],['Voix',21.34,560,1200],['Montage',21.64,740,1200]];
$('s4p').innerHTML=P4.map(([t,,x,y],i)=>`<div class="pill${i==3?' b':''}" id="p${i}" style="left:${x}px;top:${y}px">${t}</div>`).join('')+`<div class="badge" id="p4" style="left:250px;top:1310px;font-size:40px">Tout s'enchaîne</div>`;
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=7.2&&t<31.7)?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?1:cl((t-a)/.25),fo=id==='s7'?1:1-cl((t-(b-.2))/.2);el.style.opacity=Math.min(fi,fo);}}
  if(t<3.9){slam($('s0a'),t,0.05);pop($('s0b'),t,W(1.64),.35,20);slam($('s0c'),t,W(2.64));}
  else if(t<7.2){pop($('s1p'),t,3.9,.4,0,.2);pop($('s1a'),t,W(3.8),.35,20);slam($('s1b'),t,W(5.48),'rotate(-2deg)');}
  else if(t<11.9){pop($('s2tab'),t,7.25,.45,50,.03);const k=cl((t-W(6.68))/1.2);$('s2n').textContent=Math.round(367*eout(k));pop($('s2n'),t,W(6.5),.3,20);pop($('s2l'),t,W(8.28),.35,20);}
  else if(t<14.5){pop($('s3a'),t,11.95,.35,20);slam($('s3b'),t,W(12.9));$('s3s').style.transform=`scaleX(${eout(cl((t-W(13.5))/.35))})`;pop($('s3m'),t,W(13.18),.4,80);}
  else if(t<23.6){let k=0;S4.forEach((s,i)=>{if(t>=s[2])k=i;});s4i.forEach((im,i)=>{im.style.opacity=i===k?1:0;im.style.transform=i===k?`scale(${1+.06*cl((t-S4[k][2])/2.2)})`:'';});$('s4l').textContent=S4[k][1];
    P4.forEach(([,w],i)=>slam($('p'+i),t,W(w)-.05));const b=$('p4');if(t>=W(22.38))slam(b,t,W(22.38),'rotate(-2deg)');else b.style.opacity=0;}
  else if(t<27.5){const b=$('s5bar');b.style.clipPath=`inset(0 ${100-100*eout(cl((t-23.7)/.8))}% 0 0)`;[W(23.74),W(25.92),W(26.32)].forEach((a,i)=>pop($('l'+i),t,a-.3,.35,20));pop($('s5tab'),t,24.2,.45,50,.03);}
  else if(t<31.7){pop($('s6a'),t,W(26.98)-.1,.4,20);slam($('s6b'),t,W(29.2));}
  else {pop($('s7p'),t,31.8,.45,0,.2);slam($('s7a'),t,W(31.18)+.05);const b=$('s7b');if(t>=33.6)slam(b,t,33.6,'rotate(-2deg)');else b.style.opacity=0;pop($('s7l'),t,34.2,.4,20);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
