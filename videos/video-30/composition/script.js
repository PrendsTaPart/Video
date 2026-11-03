const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const V=w=>0.5+w;
const DUR=76;
const SC=[['s0',0,V(4.66)],['s1',V(4.66),V(14.1)],['s2',V(14.1),V(21.14)],['s3',V(21.14),V(30.14)],['s4',V(30.14),V(36.74)],['s5',V(36.74),V(38.64)],['s6',V(38.64),V(51.56)],['s7',V(51.56),V(57.08)],['s8',V(57.08),V(62.0)],['s9',V(62.0),V(69.84)],['s10',V(69.84),DUR]];
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
const PR="Trouve-moi des restaurants susceptibles d'être intéressés par FoodEatUp, qualifie les prospects et prépare les prochaines actions commerciales. Présente-moi les actions qui demandent mon accord avant de les exécuter.";
const TL=[['rechercher_prospects','lecture','ok',25.0],['prospecter_entreprise','recherche','ok',25.56],['prospecter_maps','recherche','ok',26.38],['enregistrer_prospect','écriture','wt',27.86],['list_segments · get_contacts_segment','lecture','ok',28.86],['ajouter_prospect_pipeline','écriture','wt',29.54]];
$('s3t').innerHTML=TL.map(([n,k,c],i)=>`<div class="tl" id="tl${i}" style="top:${200+i*96}px">${n}<em class="${c}">${k}</em></div>`).join('');
const ST=[['Appeler',41.7],['Comprendre les besoins',42.7],['Présenter mes solutions',43.94],['Proposer un rendez-vous',45.2]];
$('v2').innerHTML=ST.map(([n],i)=>`<div class="ds" id="st${i}" style="top:${620+i*100}px;padding:10px 22px"><div><b style="font-size:27px">${i+1}. ${n}</b></div><em class="wt">objectif</em></div>`).join('');
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=V(4.66)&&t<V(69.84))?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.2):cl((t-a)/.22),fo=id==='s10'?1:1-cl((t-(b-.18))/.18);el.style.opacity=Math.min(fi,fo);}}
  if(t<V(4.66)){slam($('s0a'),t,.15);pop($('s0m'),t,.5,.4,80);}
  else if(t<V(14.1)){pop($('s1a'),t,V(4.7),.35,30);pop($('s1d'),t,V(7.86),.35,30,.2);slam($('s1e'),t,V(11.5));pop($('s1b'),t,V(12.6),.3,30,.2);pop($('s1c'),t,V(13.1),.3,30,.2);pop($('s1m'),t,V(8.64),.4,80);}
  else if(t<V(21.14)){pop($('s2c'),t,V(14.15),.35,30);const n=Math.floor(cl((t-V(14.6))/5.6)*PR.length);$('s2t').textContent=PR.slice(0,n)+(n<PR.length?'▌':'');pop($('s2d'),t,V(15.5),.3,10);}
  else if(t<V(30.14)){TL.forEach((l,i)=>pop($('tl'+i),t,V(l[3]),.3,20,.03));pop($('s3p'),t,V(26.86),.35,30);pop($('s3d'),t,V(27.6),.3,10);}
  else if(t<V(36.74)){[30.14,31.28,32.16,32.88,33.32,33.6].forEach((w,i)=>pop($('g'+i),t,V(w),.3,30,.3));slam($('g6'),t,V(34.66));}
  else if(t<V(38.64)){slam($('p0'),t,V(36.8));pop($('p1'),t,V(37.0),.3,20);['p2','p3','p4'].forEach((p,i)=>pop($(p),t,V(37.2)+i*.2,.3,30,.2));pop($('p5'),t,V(37.6),.3,10);}
  else if(t<V(51.56)){pop($('v0'),t,V(38.7),.3,30);pop($('v1'),t,V(39.8),.35,30);ST.forEach((s,i)=>pop($('st'+i),t,V(s[1]),.3,30,.03));slam($('v3'),t,V(48.06));}
  else if(t<V(57.08)){pop($('r0'),t,V(51.6),.4,40);pop($('r1'),t,V(52.0),.4,40);pop($('r2'),t,V(52.6),.3,10);pop($('r3'),t,V(53.96),.3,30,.03);pop($('r4'),t,V(54.96),.3,30,.03);pop($('r5'),t,V(56.06),.3,30,.03);}
  else if(t<V(62.0)){['o0','o1','o2','o3','o4'].forEach((o,i)=>pop($(o),t,V(57.1)+i*.5,.3,30,.1));['q0','q1','q2','q3'].forEach((q,i)=>pop($(q),t,V(57.4)+i*.5,.2,10));slam($('o5'),t,V(60.26));}
  else if(t<V(69.84)){pop($('w0'),t,V(63.84),.35,20);pop($('w1'),t,V(66.64),.35,20);slam($('w2'),t,V(68.16));pop($('w3'),t,V(62.2),.4,80);}
  else {pop($('s10p'),t,V(69.9),.4,0,.3);pop($('s10q'),t,V(70.2),.4,30);pop($('s10l'),t,V(71.3),.4,20);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
