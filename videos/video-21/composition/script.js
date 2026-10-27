const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const A=[0,21.4,32.25,47.4,56.8], P=[0.6,24.0,38.35,55.0];
const V=(i,w)=>P[i]+(w-A[i]);
const DUR=70;
const SC=[['s0',0,V(0,4.16)],['s1',V(0,4.16),V(0,9.42)],['s2',V(0,9.42),V(0,14.4)],['s3',V(0,14.4),24.0],['s4',24.0,V(1,28.78)],['s5',V(1,28.78),34.85],['s6',34.85,V(2,38.48)],['s7',V(2,38.48),55.0],['s8',55.0,V(3,53.78)],['s9',V(3,53.78),DUR]];
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
function lines(el,arr,t,a,lps){const n=Math.max(0,Math.floor((t-a)*lps)+(t>=a?1:0));el.innerHTML=arr.slice(0,n).join('\n');}
const BP=[[80,180],[880,220],[140,420],[820,470],[60,1150],[900,1120],[240,1350],[740,1380],[480,1500]];
$('s0b').innerHTML=BP.map(([x,y],i)=>`<div class="bot" id="b0${i}" style="left:${x}px;top:${y}px">IA</div>`).join('');
const BAD=[['Commande envoyée seule','60px','560px',-3],['Prix inventé','520px','700px',3],['Mauvais logiciel','80px','840px',2],['Aucun contrôle','480px','980px',-2],['Outil non autorisé','140px','1120px',1]];
$('s2b').innerHTML=BAD.map(([t,x,y,r],i)=>`<div class="bad" id="bd${i}" style="left:${x};top:${y};transform:rotate(${r}deg)">✗ ${t}</div>`).join('');
const L4=['<span class="g">learn_task</span>(« Analyser les stocks et préparer','  les achats fournisseurs avant une rupture »)','  <span class="o">mission F3 · Stocks et commandes fournisseurs</span>','  <span class="o">« Du stock bas à la commande préparée,</span>','  <span class="o">   jamais envoyée seule. »</span>','  <span class="m">verdict : suis la mission, fais une première fois</span>','  <span class="m">en Aperçu, puis retiens la procédure (remember)</span>'];
$('thb').innerHTML=[[640,780],[860,900],[640,1040],[860,1180],[650,1330]].map(([x,y])=>`<div class="bot" style="left:${x}px;top:${y}px;width:150px;height:150px;border-radius:75px">IA</div>`).join('');
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=V(0,4.16)&&t<V(3,53.78))?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.2):cl((t-a)/.22),fo=id==='s9'?1:1-cl((t-(b-.18))/.18);el.style.opacity=Math.min(fi,fo);}}
  if(t<V(0,4.16)){BP.forEach((b,i)=>{const e=$('b0'+i);pop(e,t,.1+i*.12,.3,20,.5);e.style.transform+=` rotate(${Math.sin(t*3+i)*8}deg)`;});pop($('s0a'),t,.3,.35,20);slam($('s0q'),t,V(0,1.74));}
  else if(t<V(0,9.42)){slam($('s1a'),t,V(0,4.2));pop($('s1m'),t,V(0,4.3),.4,80);}
  else if(t<V(0,14.4)){pop($('s2a'),t,V(0,9.45),.35,20);BAD.forEach((b,i)=>slam($('bd'+i),t,V(0,10.6)+i*.5,`rotate(${b[3]}deg)`));pop($('s2d'),t,V(0,12.5),.35,10);}
  else if(t<24.0){pop($('s3t'),t,V(0,14.45),.4,60);$('s3i').src=t<V(0,16.4)?'a/img/accueil-0.png':'a/img/formations-0.png';['pl0','pl1','pl2','pl3'].forEach((p,i)=>pop($(p),t,V(0,[17.08,17.9,19.02,19.74][i]),.35,30,.1));}
  else if(t<V(1,28.78)){pop($('s4g'),t,V(1,21.66),.35,20);pop($('s4t'),t,V(1,24.1),.3,30);lines($('s4pre'),L4,t,V(1,24.2),6);[0,1,2,3].forEach(i=>pop($('st'+i),t,V(1,26.1)+i*.55,.3,30,.1));}
  else if(t<34.85){[0,1,2,3,4].forEach(i=>pop($('tl'+i),t,V(1,28.85)+i*.4,.3,30,.03));}
  else if(t<V(2,38.48)){[0,1,2].forEach(i=>pop($('qz'+i),t,34.95+i*.8,.3,30,.03));pop($('qzr'),t,37.0,.3,10);slam($('sc0'),t,V(2,35.24));slam($('sc1'),t,V(2,37.52));}
  else if(t<55.0){[0,1,2,3].forEach(i=>pop($('k'+i),t,V(2,[41.66,42.42,43.24,44.26][i]),.3,30,.2));slam($('k4'),t,V(2,45.68));pop($('k5'),t,V(2,46.6),.35,10);}
  else if(t<V(3,53.78)){pop($('s8a'),t,55.05,.35,20);slam($('s8b'),t,V(3,50.54));}
  else {pop($('s9p'),t,V(3,53.8),.4,0,.3);pop($('s9q'),t,V(3,54.34),.4,30);pop($('s9l'),t,V(3,56.2),.4,20);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
