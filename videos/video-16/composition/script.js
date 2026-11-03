const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const A=[0,25.55,49.04], P=[0.6,28.55];
const V=(i,w)=>P[i]+(w-A[i]);
const SC=[['s0',0,5.4],['s1',5.4,11.4],['s2',11.4,17.2],['s3',17.2,21.9],['s4',21.9,28.55],['s5',28.55,33.5],['s6',33.5,36.2],['s7',36.2,42.6],['s8',42.6,V(1,46.4)],['s9',V(1,46.4),56.0]];
const DUR=56.0;
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
function lines(el,arr,t,a,lps){const n=Math.max(0,Math.floor((t-a)*lps)+(t>=a?1:0));el.innerHTML=arr.slice(0,n).join('\n');}
const Q0=[['Comment je clôture la caisse ?',60,300,-3],['Où sont mes relevés HACCP ?',520,380,3],['Comment j\'imprime une étiquette ?',80,520,2],['Je déclare un frigo comment ?',480,640,-2],['Et le planning ?',200,760,1]];
$('s0q').innerHTML=Q0.map(([t,x,y,r],i)=>`<div class="qb" id="q${i}" style="left:${x}px;top:${y}px;transform:rotate(${r}deg)">${t}</div>`).join('');
const S2=[['accueil.png',11.4],['module-haccp.png',V(0,15.64)]];
$('s2scr').innerHTML=S2.map(s=>`<img src="a/img/${s[0]}" style="opacity:0">`).join('');const s2i=[...$('s2scr').children];
const L4=['<span class="g">rechercher_tutoriels</span>(« relevé de température »)','  <span class="o">1. Relever une température d\'équipement · 0:38</span>','  <span class="m">2. Retrouver l\'historique des relevés · 0:33</span>','  <span class="m">3. Agent HACCP : relevés depuis WhatsApp · 0:48</span>','  <span class="m">4. Ajouter une température de production · 0:38</span>','<span class="g">carte_tutoriel</span>(relever-une-temperature-equipement)','  <span class="o">→ vignette, vidéo, étapes, lien de la fiche</span>'];
const ST=['Ouvrir Hygiène & HACCP → « Températures »','Lire la plage cible (Frigo 5 : 0 à 4 °C)','Ajuster la valeur avec − et +','« Enregistrer les relevés de température »','Confirmer, puis message « Enregistré ! »','Hors plage (9 °C) → non conforme d\'office'];
$('s6s').innerHTML=ST.map((s,i)=>`<div class="row" id="st${i}" style="top:${380+i*100}px;padding:10px 18px"><div class="n" style="width:44px;height:44px">${i+1}</div><div class="t" style="font-size:25px">${s}</div></div>`).join('');
const LS=[['ouvrir-son-classeur-haccp','Ouvrir son classeur HACCP','0:48'],['declarer-ses-equipements','Déclarer ses équipements','0:51'],['relever-une-temperature-equipement','Relever une température d\'équipement','0:38'],['parametrer-son-plan-de-nettoyage','Paramétrer son plan de nettoyage','0:40'],['imprimer-ses-etiquettes','Imprimer ses étiquettes','1:02']];
$('s7l').innerHTML=LS.map(([s,t,d],i)=>`<div class="les" id="ls${i}" style="top:${370+i*145}px;${i==2?'border-color:var(--orange)':''}"><div style="width:60px;height:60px;border-radius:30px;background:${i==2?'var(--orange)':'var(--blue)'};display:flex;align-items:center;justify-content:center;font-weight:700;font-size:28px;flex:none;color:#fff">${i+1}</div><div><b>${t}</b><span>${d} · leçon ${i+1}/5</span></div></div>`).join('');
const TF0=V(1,27.64)-.6, TFN=565;
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=11.4&&t<V(1,46.4))?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.3):cl((t-a)/.22),fo=id==='s9'?1:1-cl((t-(b-.18))/.18);el.style.opacity=Math.min(fi,fo);}}
  if(t<5.4){Q0.forEach((q,i)=>slam($('q'+i),t,.3+i*.7,`rotate(${q[3]}deg)`));pop($('s0m'),t,.2,.4,80);}
  else if(t<11.4){pop($('s1a'),t,V(0,5.0),.35,20);slam($('s1b'),t,V(0,7.36));}
  else if(t<17.2){let k=0;S2.forEach((s,i)=>{if(t>=s[1])k=i;});s2i.forEach((im,i)=>{im.style.opacity=i===k?1:0;im.style.transform=i===k?`scale(${1+.05*cl((t-S2[k][1])/2)})`:'';});
    const p=eout(cl((t-V(0,13.6))/1.0));$('s2n').textContent=Math.round(173*p);pop($('s2n'),t,V(0,13.4),.3,20);pop($('s2l'),t,V(0,15.32),.35,20);}
  else if(t<21.9){pop($('m0'),t,17.3,.35,30,.1);slam($('m1'),t,V(0,17.54));$('s3l').style.opacity=cl((t-V(0,17.9))/.4);pop($('m2'),t,V(0,19.2),.35,30,.1);pop($('m3'),t,V(0,19.7),.35,30,.1);pop($('m4'),t,V(0,20.6),.35,20);}
  else if(t<28.55){pop($('u0'),t,V(0,22.0),.4,40);pop($('s4t'),t,V(0,25.38)+.1,.3,30);lines($('s4pre'),L4,t,V(0,25.38)+.3,3.2);}
  else if(t<33.5){const c=$('s5c');const p=eout(cl((t-28.6)/.5));c.style.opacity=p;c.style.transform=`translateY(${(1-p)*120}px) scale(${.85+.15*p})`;
    const f=Math.max(0,Math.min(TFN-1,Math.floor((t-TF0)*15)));$('tfi').src='a/tf/'+String(Math.min(TFN,f+12)).padStart(4,'0')+'.jpg';$('tfp').style.width=(100*f/TFN)+'%';
    pop($('s5r'),t,29.4,.35,10);pop($('s5a'),t,V(1,28.68),.35,20);pop($('s5b'),t,V(1,29.2),.35,20);}
  else if(t<36.2){ST.forEach((s,i)=>pop($('st'+i),t,33.55+i*.22,.3,20,.03));pop($('s6q'),t,V(1,32.28),.4,30);}
  else if(t<42.6){LS.forEach((s,i)=>pop($('ls'+i),t,36.3+i*.35,.35,30,.03));slam($('s7b'),t,V(1,37.04),'rotate(-1deg)');}
  else if(t<V(1,46.4)){pop($('s8a'),t,V(1,39.96),.35,20);slam($('s8b'),t,V(1,42.22));}
  else {pop($('s9p'),t,V(1,46.4),.4,0,.2);slam($('s9a'),t,V(1,46.5));pop($('s9b'),t,V(1,48.6),.4,20);pop($('s9l'),t,53.0,.4,20);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
