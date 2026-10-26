const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const A=[0,7.275,16.709,28.9,40.486,52.657,66.587,76.075,84.24], P=[1.0,9.3,19.6,32.6,45.6,76.2,91.0,101.6];
const V=(i,w)=>P[i]+(w-A[i]);
const SC=[['s0',0,9.0],['s1',9.0,19.2],['s2',19.2,32.2],['s3',32.2,45.1],['s4',45.1,58.3],['s5',58.3,75.9],['s6',75.9,90.6],['s7',90.6,101.1],['s8',101.1,110.0],['s9',110.0,120.0]];
const DUR=120.0;
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
function lines(el,arr,t,a,lps){const n=Math.max(0,Math.floor((t-a)*lps)+(t>=a?1:0));el.innerHTML=arr.slice(0,n).join('\n');}
const PROMPT="Claude, analyse mes dernières prospections dans les régions françaises, identifie les nouveaux établissements et prépare une campagne commerciale adaptée à FoodEatUp. ";
const RULE="Ne contacte personne sans ma validation.";
const S2=['<span class="m">→ 18 régions : Auvergne-Rhône-Alpes, Bretagne, Corse,</span>','<span class="m">  Île-de-France, Occitanie, La Réunion…</span>','<span class="m">→ 25 spécialités : Restaurant, </span><span class="o">Bar et brasserie</span><span class="m">,</span>','<span class="m">  Boulangerie-pâtisserie, Traiteur, Food truck…</span>'];
const TOOLS=['prospection_history','run_prospection','add_clients','list_clients','list_logs','list_email_templates'];
$('s2chips').innerHTML=TOOLS.map((t,i)=>`<div class="chipx" id="tc${i}" style="left:${60+(i%2)*490}px;top:${720+Math.floor(i/2)*64}px">${t}</div>`).join('');
const H=[["Provence-Alpes-Côte d'Azur",40],["Pays de la Loire",40],["Occitanie",40],["Nouvelle-Aquitaine",40],["Normandie",40]];
$('s3rows').innerHTML=H.map(([r,n],i)=>`<div class="r" id="h${i}"><span>${r}</span><span class="n">${n}</span></div>`).join('');
const FUN=[['720 résultats','18 recherches · aujourd\'hui','#7dd3fc',900],['90 enregistrés','5 par région','#86efac',800],['0 qualifié','statut « nouveau »','#fde68a',700],['0 contacté','campagne FoodEatUp','#fdba74',600],['Réponses','non mesurées','#e5e7eb',500],['Ventes','—','#e5e7eb',400]];
$('s4fun').innerHTML=FUN.map(([a,b,c,w],i)=>`<div class="fun" id="f${i}" style="top:${380+i*92}px;width:${w}px;height:80px;background:${c};left:${90+(900-w)/2}px">${a}<small>${b}</small></div>`).join('');
const PR=[["B•••••••••••","Provence-Alpes-Côte d'Azur","e-mail ✓ · site ✓"],["A•••••••••••","Pays de la Loire","e-mail ✓ · site ✓"],["S•••••••••••","Occitanie","e-mail ✓ · site ✓"],["B•••••••••••","Nouvelle-Aquitaine","e-mail ✓ · site ✓"],["B•••••••••••","Normandie","e-mail — · site ✓"]];
$('s4rows').innerHTML=PR.map(([n,r,c],i)=>`<div class="r" id="p${i}" style="font-size:21px"><span>${n} · ${r}</span><span style="flex:none;width:230px;color:#AEB8C2">${c}</span><span class="n" style="color:#fde68a">nouveau</span></div>`).join('');
const RT=[['Préparer les messages','modèle conforme + segment dédoublonné',54.48],['Suivre les campagnes','list_emails · statuts',55.54],['Proposer les relances','J+3 / J+7, envoi sur accord',56.54],['Analyser les résultats','entonnoir · journal',57.56]];
$('s6rows').innerHTML=RT.map(([t,s],i)=>`<div class="row" id="rt${i}" style="top:${380+i*145}px"><div class="n">${i+1}</div><div class="t">${t}<small>${s}</small></div></div>`).join('');

function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=9&&t<110)?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?1:cl((t-a)/.3),fo=id==='s9'?1:1-cl((t-(b-.25))/.25);el.style.opacity=Math.min(fi,fo);}}
  if(t<9){pop($('s0c'),t,.1,.4,20);pop($('s0tab'),t,.3,.6,60,.04);pop($('s0r'),t,.9,.4,10);pop($('s0m'),t,V(0,1.8),.5,80);pop($('s0l'),t,V(0,0.9),.5,30);
    const tt=$('s0t');if(t>=V(0,5.9))slam(tt,t,V(0,5.9));else tt.style.opacity=0;}
  else if(t<19.2){pop($('s1p'),t,9.2,.4,40);const a=V(1,8.0),n=Math.floor(cl((t-a)/5.2)*PROMPT.length);
    const r=Math.floor(cl((t-V(1,14.5))/1.3)*RULE.length);$('s1txt').innerHTML=PROMPT.slice(0,n)+'<b>'+RULE.slice(0,r)+'</b>'+((t*2|0)%2?'▍':'');
    pop($('s1k'),t,V(1,16.0),.4,20);pop($('s1m'),t,9.6,.5,60);}
  else if(t<32.2){pop($('s2t'),t,V(2,16.85),.4,30);lines($('s2pre'),S2,t,V(2,19.9),2.2);
    TOOLS.forEach((x,i)=>pop($('tc'+i),t,V(2,21.88)+i*.18,.3,20,.1));pop($('s2n'),t,V(2,26.0),.4,30);pop($('s2n2'),t,V(2,27.0),.4,30);}
  else if(t<45.1){pop($('s3t'),t,V(3,29.0),.4,30);H.forEach((x,i)=>pop($('h'+i),t,V(3,29.6)+i*.35,.3,15));
    const k=cl((t-V(3,32.36))/.9);const tot=$('s3tot');tot.style.opacity=k>0?1:0;tot.textContent=Math.round(200*eout(k));
    const b=$('s3b');if(t>=V(3,37.82))slam(b,t,V(3,37.82),'rotate(-2deg)');else b.style.opacity=0;pop($('s3r'),t,V(3,34.4),.4,10);}
  else if(t<58.3){FUN.forEach((x,i)=>pop($('f'+i),t,V(4,40.7)+i*.8,.35,20,.05));pop($('s4t'),t,V(4,48.5),.4,30);PR.forEach((x,i)=>pop($('p'+i),t,V(4,48.9)+i*.3,.3,10));}
  else if(t<75.9){pop($('d1'),t,58.6,.5,50,.03);for(let i=0;i<5;i++)pop($('c'+i),t,60.0+i*1.1,.35,20);pop($('d2'),t,66.0,.45,40);
    const b=$('d3');if(t>=70.2)slam(b,t,70.2);else b.style.opacity=0;}
  else if(t<90.6){RT.forEach(([,,w],i)=>pop($('rt'+i),t,V(5,w)-.1,.35,30,.03));pop($('s6t'),t,V(5,58.54),.4,30);pop($('s6w'),t,V(5,61.4),.4,20);}
  else if(t<101.1){[68.48,69.02,69.72,70.28].forEach((w,i)=>pop($('ch'+i),t,V(6,w)-.1,.35,30,.05));const b=$('s7b');if(t>=V(6,72.14))slam(b,t,V(6,72.14),'rotate(-2deg)');else b.style.opacity=0;}
  else if(t<110){pop($('s8a'),t,V(7,77.3),.4,30);pop($('s8b'),t,V(7,80.3),.5,30);pop($('s8m'),t,V(7,78.4),.5,80);}
  else {pop($('s9a'),t,110.2,.6,30);pop($('s9b'),t,111.2,.5,20);pop($('s9l'),t,112.2,.5,20,.1);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
