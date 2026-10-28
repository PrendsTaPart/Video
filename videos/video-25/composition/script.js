const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const A=[0,28.2,55.85,66.88], P=[0.6,30.8,62.45];
const V=(i,w)=>P[i]+(w-A[i]);
const DUR=78;
const SC=[['s0',0,V(0,4.6)],['s1',V(0,4.6),V(0,13.0)],['s2',V(0,13.0),V(0,15.18)],['s3',V(0,15.18),V(0,22.78)],['s4',V(0,22.78),28.8],['s5',28.8,V(1,30.56)],['s6',V(1,30.56),V(1,38.94)],['s7',V(1,38.94),V(1,44.76)],['s8',V(1,44.76),V(1,51.2)],['s9',V(1,51.2),62.45],['s10',62.45,V(2,63.48)],['s11',V(2,63.48),DUR]];
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
function seq(img,t,t0,f0,n){const f=Math.max(0,Math.min(n-1,Math.floor((t-t0)*15)));img.src='a/pres/'+String(f0+f).padStart(4,'0')+'.jpg';}
const DM=['Démo client #1','Démo client #2','Démo client #3','Démo client #4','Démo client #5'];
$('s0d').innerHTML=DM.map((d,i)=>`<div class="pp" id="dm${i}" style="left:${[60,600,90,620,330][i]}px;top:${[560,600,700,740,500][i]}px">${d}</div>`).join('');
const CH=['LOGICIEL','CAPTURE','STORYBOARD','SCRIPT IA','AVATAR','PRÉSENTATION INTERACTIVE'];
$('s5s').innerHTML=CH.map((c,i)=>`<div class="st" id="ch${i}" style="top:${230+i*170}px;justify-content:center;${i==5?'background:var(--rb);color:#fff':''}">${c}</div>`).join('');
const MT=[['list_projects','lire'],['get_project','lire'],['create_project','crée un brouillon'],['list_brand_kits','lire'],['list_support_requests','lire'],['update_support_request','traitée / rouverte'],['list_unanswered_questions','lire'],['get_tutorial_stats','lire']];
$('s8r').innerHTML=MT.map(([n,r],i)=>`<div class="rt" id="m${i}" style="top:${370+i*130}px"><code style="font-size:26px">${n}</code><em style="background:${r==='lire'?'#E8F5E9;color:#2e7d32':'#FFF1D6;color:#9a5b00'}">${r}</em></div>`).join('');
const FS=[['Le hook','« Une rupture le samedi soir ? »'],['Les produits sous le seuil','list_low_stocks'],['La liste d\'achats','get_shopping_list'],['La commande préparée','l\'humain l\'envoie']];
$('s9s').innerHTML=FS.map(([a,b],i)=>`<div class="sb" id="fs${i}" style="top:${820+i*150}px"><i>${i+1}</i><div><b>${a}</b><small>${b}</small></div></div>`).join('');
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=V(0,4.6)&&t<V(2,63.48))?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.2):cl((t-a)/.22),fo=id==='s11'?1:1-cl((t-(b-.18))/.18);el.style.opacity=Math.min(fi,fo);}}
  if(t<V(0,4.6)){slam($('s0a'),t,.15);pop($('s0m'),t,.4,.4,80);DM.forEach((d,i)=>pop($('dm'+i),t,1.2+i*.5,.3,20,.3));}
  else if(t<V(0,13.0)){pop($('s1a'),t,V(0,4.65),.35,20);pop($('s1c'),t,V(0,4.8),.4,40);seq($('s1i'),t,V(0,4.8),1,112);}
  else if(t<V(0,15.18)){pop($('s2i'),t,V(0,13.05),.4,0,.5);slam($('s2t'),t,V(0,14.12));}
  else if(t<V(0,22.78)){pop($('s3a'),t,V(0,15.3),.4,40);pop($('s3b'),t,V(0,19.5),.4,40);}
  else if(t<28.8){pop($('s4a'),t,V(0,22.85),.5,60);pop($('l0'),t,V(0,26.62),.3,20,.3);pop($('l1'),t,V(0,27.2),.3,20,.3);pop($('l2'),t,V(0,27.82),.3,20,.3);}
  else if(t<V(1,30.56)){CH.forEach((c,i)=>pop($('ch'+i),t,28.85+i*.32,.25,30,.1));}
  else if(t<V(1,38.94)){pop($('s6c'),t,V(1,30.6),.4,40);seq($('s6i'),t,V(1,30.6),300,105);pop($('lv0'),t,V(1,33.04),.3,30,.03);pop($('lv1'),t,V(1,35.74),.3,30,.03);pop($('lv2'),t,V(1,37.62),.3,30,.03);pop($('lvd'),t,V(1,38.2),.3,10);}
  else if(t<V(1,44.76)){[0,1,2,3].forEach(i=>pop($('r'+i),t,V(1,39.14)+i*.35,.3,30,.03));pop($('r4'),t,V(1,41.92),.4,40);}
  else if(t<V(1,51.2)){MT.forEach((m,i)=>pop($('m'+i),t,V(1,45.0)+i*.32,.25,30,.03));}
  else if(t<62.45){[0,1,2].forEach(i=>pop($('k'+i),t,V(1,51.3)+i*.3,.3,30,.2));pop($('k3'),t,V(1,52.2),.3,10);pop($('k4'),t,V(1,54.16),.3,20);pop($('k5'),t,V(1,55.5),.35,20,.3);FS.forEach((f,i)=>pop($('fs'+i),t,58.6+i*.6,.3,30,.03));pop($('k6'),t,60.6,.3,10);}
  else if(t<V(2,63.48)){pop($('s10a'),t,62.5,.35,20);slam($('s10b'),t,V(2,58.5));}
  else {pop($('s11p'),t,V(2,63.5),.4,0,.3);pop($('s11v'),t,V(2,63.7),.5,40);slam($('s11b'),t,V(2,64.2));pop($('s11q'),t,V(2,64.7),.4,30);pop($('s11l'),t,V(2,66.6),.4,20);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
