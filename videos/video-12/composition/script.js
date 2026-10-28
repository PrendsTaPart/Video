const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3), eio=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
const O=0.6, W=w=>O+w;
const SC=[['s0',0,4.0],['s1',4.0,6.0],['s2',6.0,11.6],['s3',11.6,15.2],['s4',15.2,22.0],['s5',22.0,27.8],['s6',27.8,35.5]];
const DUR=35.5;
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
// caméra : liste de clés [t, x, y, échelle] en pixels de l'image source
function cam(img,vw,vh,keys,t){let k=0;while(k<keys.length-1&&t>keys[k+1][0])k++;const a=keys[k],b=keys[Math.min(k+1,keys.length-1)];const f=b===a?1:eio(cl((t-a[0])/(b[0]-a[0])));
  const x=a[1]+(b[1]-a[1])*f,y=a[2]+(b[2]-a[2])*f,s=a[3]+(b[3]-a[3])*f;img.style.transform=`translate(${-x*s}px,${-y*s}px) scale(${s})`;}
// planche 10 (1588×2246) : quatre cases
const K2=[[6.0,0,0,1100/2246],[6.8,0,0,1100/2246],[7.5,60,120,0.95],[8.4,578,120,0.95],[9.3,40,1088,0.95],[10.2,578,1088,0.95],[11.6,0,0,1100/2246]];
const S4=[['fg/doc109-commande.png','Chapitre 7 · Prendre une commande',W(14.74)],['fg/doc111-encaisser.png','Chapitre 8 · Encaisser',W(15.76)],['cms/1522.jpg','Clôturer la caisse · tutoriel (RapidoCMS)',W(16.48)],['fg/doc194-atlas.png','Atlas des écrans',W(17.28)],['fg/doc174-claude.png','Chapitre 37 · Connecter FoodEatUp à Claude',W(17.96)],['fg/bd53-brigade.png','Les illustrations de la BD',W(18.82)]];
$('s4box').innerHTML=S4.map(s=>`<img src="a/${s[0]}" style="position:absolute;left:0;top:0;width:960px;opacity:0">`).join('');const s4i=[...$('s4box').children];
const M5=['fg/bd16-telephone.png','fg/doc111-encaisser.png','fg/bd40-planche.png','fg/doc194-atlas.png','fg/bd53-brigade.png','fg/doc174-claude.png'];
$('s5m').innerHTML=M5.map((f,i)=>`<div class="page" id="m${i}" style="width:300px;height:424px;left:${60+(i%3)*330}px;top:${880+Math.floor(i/3)*450}px"><img src="a/${f}"></div>`).join('');
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=4&&t<27.8)?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?1:cl((t-a)/.2),fo=id==='s6'?1:1-cl((t-(b-.15))/.15);el.style.opacity=Math.min(fi,fo);}}
  if(t<4){const s=1.9-0.9*eout(cl(t/3.6));$('s0i').style.transform=`translate(${-(s-1)*450}px,${-(s-1)*300}px) scale(${s})`;
    [1.22,1.88,2.9].forEach((w,i)=>slam($('t'+i),t,W(w)-.1));}
  else if(t<6){$('s1a').style.transform=`rotate(-4deg) translate(${(t-4)*-25}px,0)`;$('s1b').style.transform=`rotate(3deg) translate(${(t-4)*25}px,0)`;slam($('s1c'),t,W(4.26),'rotate(-3deg)');}
  else if(t<11.6){cam($('s2i'),960,1100,K2,t);const p=t<8.4?'a/fg/hd-bd10.png':(t<10.2?'a/fg/hd-bd40.png':'a/fg/hd-bd10.png');if(!$('s2i').src.endsWith(p.slice(2)))$('s2i').src=p;slam($('s2n'),t,W(9.98));}
  else if(t<15.2){slam($('s3a'),t,11.65,'rotate(-4deg)');pop($('s3c'),t,W(12.88),.4,50,.05);pop($('s3d'),t,W(13.58),.45,60,.05,'rotate(3deg)');}
  else if(t<22.0){let k=0;S4.forEach((s,i)=>{if(t>=s[2])k=i;});s4i.forEach((im,i)=>{const on=i===k;im.style.opacity=on?1:0;
      if(on){const d=t-S4[k][2];const h=im.naturalHeight*960/Math.max(1,im.naturalWidth);const z=1.0+0.18*cl(d/1.2);const dy=Math.max(0,(h*z-1100))*cl(d/1.2);im.style.transform=`translateY(${-dy}px) scale(${z})`;im.style.transformOrigin='50% 0';}});
    $('s4l').textContent=S4[k][1];}
  else if(t<27.8){pop($('s5a'),t,W(21.62),.35,20);[22.64,22.98,23.36].forEach((w,i)=>slam($('j'+i),t,W(w)));
    if(t>W(24.2)){[0,1,2].forEach(i=>{$('j'+i).style.opacity=1-cl((t-W(24.2))/.3)*.7;});}
    pop($('s5b'),t,W(24.2),.4,30);M5.forEach((f,i)=>pop($('m'+i),t,W(24.8)+i*.18,.3,60,.1));}
  else {slam($('s6a'),t,27.9);pop($('s6b'),t,W(28.36)-.1,.35,20);slam($('s6c'),t,W(28.58),'rotate(-3deg)');pop($('s6l'),t,31.5,.4,20);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
