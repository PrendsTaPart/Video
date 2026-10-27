const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const A=[0,56.5,82.05], P=[0.5,57.5];
const V=(i,w)=>P[i]+(w-A[i]);
const DUR=85;
const SC=[['s0',0,V(0,5.22)],['s1',V(0,5.22),V(0,14.0)],['s2',V(0,14.0),V(0,16.52)],['s3',V(0,16.52),V(0,24.8)],['s4',V(0,24.8),V(0,31.12)],['s5',V(0,31.12),V(0,40.24)],['s6',V(0,40.24),V(0,48.4)],['s7',V(0,48.4),57.5],['s8',57.5,V(1,65.34)],['s9',V(1,65.34),V(1,73.0)],['s10',V(1,73.0),V(1,79.18)],['s11',V(1,79.18),DUR]];
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
const CV=[[60,560,-10],[800,520,8],[40,1150,6],[820,1130,-7],[420,1500,3]];
$('s0c').innerHTML=CV.map(([x,y,r],i)=>`<div class="cv" id="cv${i}" style="left:${x}px;top:${y}px"><b>CV</b><i></i><i style="width:70%"></i><i></i><i style="width:50%"></i></div>`).join('');
const PI=[['Offres',90,520,-4,9.36],['CV',640,560,5,10.06],['Entretiens',120,820,3,10.78],['Relances',600,900,-3,11.62],['Entreprise 1',160,1120,-2,6.44],['Entreprise 2',610,1180,4,6.6]];
$('s1p').innerHTML=PI.map(([t,x,y,r],i)=>`<div class="pi" id="pi${i}" style="left:${x}px;top:${y}px">${t}</div>`).join('');
const VF=['CV','PARSING','SCORING','TRIAGE','CANDIDATURE STRUCTURÉE'];
$('v3').innerHTML=VF.map((f,i)=>`<div class="st" id="vf${i}" style="top:${660+i*76}px;height:64px;font-size:26px;${i==4?'background:linear-gradient(90deg,#0b4f7a,#3b2a6b);border:0':''}">${f}</div>`).join('');
const KB=[['Nouveau',42.38,[['Candidate D','FoodEatUp · commercial']]],['En analyse',43.1,[['Candidat A','BraindCode · dév.']]],['Entretien',43.84,[['Candidate B','FoodEatUp · commercial']]],['En attente',44.74,[['Candidat E','BraindCode · dév.']]],['Retenu',45.38,[['Candidat C','BraindCode · dév.']]],['Refusé',45.98,[['Candidat F','FoodEatUp · commercial']]]];
$('s6k').innerHTML=KB.map(([h,w,c],i)=>`<div class="col" id="kb${i}" style="left:${60+(i%3)*330}px;top:${220+Math.floor(i/3)*430}px;height:390px"><h4>${h}</h4>${c.map(([n,s])=>`<div class="kc">${n}<span>${s}</span></div>`).join('')}</div>`).join('');
const TL=[['get_report','lecture','ok'],['rank_candidates','lecture','ok'],['get_subscription','lecture','ok'],['generate_job','écriture','wt'],['score_cvs','écriture','wt'],['schedule_interview','écriture','wt'],['start_avatar_interview','écriture','wt'],['create_video','écriture','wt'],['publish_job','externe','no'],['trigger_onboarding','externe','no']];
$('s9t').innerHTML=TL.map(([n,k,c],i)=>`<div class="tl" id="tl${i}" style="top:${200+i*98}px">${n}<em class="${c}">${k}</em></div>`).join('');
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=V(0,5.22)&&t<V(1,79.18))?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.2):cl((t-a)/.22),fo=id==='s11'?1:1-cl((t-(b-.18))/.18);el.style.opacity=Math.min(fi,fo);}}
  if(t<V(0,5.22)){slam($('s0a'),t,.15);pop($('s0m'),t,.4,.4,80);CV.forEach((c,i)=>pop($('cv'+i),t,.9+i*.35,.35,60,.3,`rotate(${c[2]}deg)`));}
  else if(t<V(0,14.0)){pop($('s1a'),t,V(0,5.3),.35,30);PI.forEach((p,i)=>slam($('pi'+i),t,V(0,p[4]),`rotate(${p[3]}deg)`));slam($('s1b'),t,V(0,12.46));}
  else if(t<V(0,16.52)){pop($('s2i'),t,V(0,14.6),.4,0,.5);pop($('s2t'),t,V(0,15.3),.3,20);pop($('s2r'),t,V(0,15.5),.3,10);}
  else if(t<V(0,24.8)){pop($('c0'),t,V(0,17.86),.35,40,.1);pop($('c1'),t,V(0,19.34),.35,40,.1);pop($('c2'),t,V(0,22.52),.3,0,.6);slam($('c3'),t,V(0,23.08));pop($('c4'),t,V(0,23.6),.3,10);pop($('pz3'),t,V(0,16.7),.4,80);}
  else if(t<V(0,31.12)){['f0','f1','f2','f3'].forEach((f,i)=>pop($(f),t,V(0,[24.8,25.46,26.12,26.92][i]),.3,30,.03));pop($('f4'),t,V(0,27.58),.4,30,.05);pop($('f5'),t,V(0,28.9),.3,10);pop($('pz4'),t,V(0,25.0),.4,80);}
  else if(t<V(0,40.24)){pop($('v0'),t,V(0,31.2),.4,40,.1);pop($('v1'),t,V(0,33.86),.35,30);pop($('v2'),t,V(0,35.02),.35,30,.2);VF.forEach((f,i)=>pop($('vf'+i),t,V(0,32.3)+i*.5,.3,20,.1));slam($('v4'),t,V(0,37.04));}
  else if(t<V(0,48.4)){KB.forEach((k,i)=>pop($('kb'+i),t,V(0,k[1]),.3,30,.1));slam($('k9'),t,V(0,46.62));pop($('k8'),t,V(0,40.4),.3,10);pop($('pz6'),t,V(0,46.8),.4,80);}
  else if(t<57.5){pop($('i0'),t,V(0,50.04),.3,30,.03);pop($('i1'),t,V(0,51.1),.3,30,.03);pop($('i2'),t,V(0,52.06),.3,30,.03);pop($('i3'),t,V(0,53.16),.3,30,.03);pop($('i4'),t,V(0,54.44),.3,30,.03);pop($('pz7'),t,V(0,48.6),.4,80);}
  else if(t<V(1,65.34)){pop($('a0'),t,57.6,.3,30);pop($('b0'),t,58.3,.2,10);pop($('a1'),t,V(1,59.04),.3,30,.1);pop($('b1'),t,V(1,61.2),.2,10);pop($('a2'),t,V(1,61.66),.3,30,.1);pop($('b2'),t,V(1,63.3),.2,10);pop($('a3'),t,V(1,63.72),.3,30,.1);pop($('b3'),t,V(1,64.6),.2,10);pop($('a4'),t,V(1,64.9),.3,30,.1);}
  else if(t<V(1,73.0)){TL.forEach((l,i)=>pop($('tl'+i),t,V(1,65.4)+i*.18,.25,20));slam($('m9'),t,V(1,68.7));const g=t>=V(1,69.48)?1:0;[8,9].forEach(i=>{$('tl'+i).style.borderColor=g?'#f87171':'';$('tl'+i).style.boxShadow=g?'0 0 30px rgba(248,113,113,.45)':'';});}
  else if(t<V(1,79.18)){pop($('s10a'),t,V(1,73.05),.35,20);slam($('s10b'),t,V(1,75.56));}
  else {pop($('s11p'),t,V(1,79.2),.4,0,.3);pop($('s11q'),t,V(1,79.5),.4,30);pop($('s11l'),t,V(1,80.6),.4,20);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
