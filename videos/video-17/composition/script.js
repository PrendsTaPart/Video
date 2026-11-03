const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const O=0.6, W=w=>O+w;
const SC=[['s0',0,4.8],['s1',4.8,9.9],['s2',9.9,14.5],['s3',14.5,19.0],['s4',19.0,25.7],['s5',25.7,28.7],['s6',28.7,35.7],['s7',35.7,44.2],['s8',44.2,51.0]];
const DUR=51.0;
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
$('h0').innerHTML=[[120,300],[860,360],[160,620],[880,700],[480,240],[60,480]].map(([x,y],i)=>`<div class="heart" id="h${i}x" style="left:${x}px;top:${y}px">♥ ${[12,48,7,23,31,5][i]}</div>`).join('');
const S3=[['cms-ecran-calendrier.webp',14.5],['cms-ecran-calendrier-generer-ia.webp',W(15.38)],['cms-ecran-reseaux-sociaux.webp',W(16.96)]];
$('s3scr').innerHTML=S3.map(s=>`<img src="a/img/${s[0]}" style="opacity:0">`).join('');const s3i=[...$('s3scr').children];
const C3=[['1/5','3 erreurs qui provoquent des ruptures de stock'],['2/5','Commander « au feeling »'],['5/5','Voir la démo FoodEatUp →']];
$('s3c').innerHTML=C3.map(([n,t],i)=>`<div class="card" id="cc${i}" style="left:${60+i*330}px;top:1000px;transform:rotate(${[-3,1,3][i]}deg)"><small>${n}</small>${t}</div>`).join('');
const LO=['Attirer','Engager','Convertir','Fidéliser','Mesurer','Améliorer'];
const lp=LO.map((_,i)=>{const a=-Math.PI/2+i*Math.PI/3;return [540+230*Math.cos(a),1160+230*Math.sin(a)];});
$('s6n').innerHTML=LO.map((t,i)=>`<div class="loopn" id="l${i}" style="left:${lp[i][0]-115}px;top:${lp[i][1]-42}px">${t}</div>`).join('');
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=9.9&&t<44.2)?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.3):cl((t-a)/.22),fo=id==='s8'?1:1-cl((t-(b-.18))/.18);el.style.opacity=Math.min(fi,fo);}}
  if(t<4.8){[0,1,2,3,4,5].forEach(i=>pop($('h'+i+'x'),t,0.3+i*.4,.3,30,.3));pop($('s0m'),t,.2,.4,80);slam($('s0q'),t,W(3.36));}
  else if(t<9.9){pop($('s1a'),t,W(4.22),.35,20);slam($('s1b'),t,W(6.68));}
  else if(t<14.5){pop($('n0'),t,W(10.26),.35,30,.1);pop($('n2'),t,W(11.28),.35,30,.1);slam($('n1'),t,W(12.28));$('s2l').style.opacity=cl((t-W(12.64))/.4);}
  else if(t<19.0){let k=0;S3.forEach((s,i)=>{if(t>=s[1])k=i;});s3i.forEach((im,i)=>{im.style.opacity=i===k?1:0;im.style.transform=i===k?`scale(${1+.05*cl((t-S3[k][1])/1.4)})`:'';});
    C3.forEach((c,i)=>pop($('cc'+i),t,W(15.54)+i*.35,.35,60,.05,`rotate(${[-3,1,3][i]}deg)`));}
  else if(t<25.7){pop($('k0'),t,19.1,.35,20);$('kx').style.transform=`scaleX(${eout(cl((t-W(19.5))/.35))})`;[21.16,21.62,22.5,23.56].forEach((w,i)=>pop($('k'+(i+1)),t,W(w)-.15,.35,30,.03));}
  else if(t<28.7){pop($('s5q'),t,W(26.14),.4,30);}
  else if(t<35.7){[0,1,2,3].forEach(i=>pop($('f'+i),t,28.8+i*.3,.35,20,.1));$('cir').style.strokeDashoffset=1445*(1-cl((t-W(29.82))/4));LO.forEach((x,i)=>pop($('l'+i),t,W(29.82)+i*.6,.3,0,.3));}
  else if(t<44.2){pop($('s7a'),t,W(35.16),.35,20);slam($('s7b'),t,W(37.28));pop($('s7t'),t,W(40.72),.45,40);}
  else {slam($('s8a'),t,44.3);pop($('s8b'),t,W(44.24),.3,20);slam($('s8c'),t,W(45.28),'rotate(-2deg)');pop($('s8l'),t,46.6,.4,20);pop($('s8p'),t,47.2,.4,0,.2);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
