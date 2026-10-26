const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const A=[0,19.45,34.64], P=[0.6,28.05];
const V=(i,w)=>P[i]+(w-A[i]);
const SC=[['s0',0,9.8],['s1',9.8,13.9],['s2',13.9,20.1],['s3',20.1,28.05],['s4',28.05,V(1,24.0)],['s5',V(1,24.0),V(1,28.08)],['s6',V(1,28.08),V(1,32.6)],['s7',V(1,32.6),47.0]];
const DUR=47.0;
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
function lines(el,arr,t,a,lps){const n=Math.max(0,Math.floor((t-a)*lps)+(t>=a?1:0));el.innerHTML=arr.slice(0,n).join('\n');}
const L3=['<span class="g">get_stats_pipeline_global</span>()','  <span class="o">→ 70 prospects : 69 nouveaux, 1 en qualification</span>','<span class="g">list_devis</span>()','  <span class="o">→ 1 devis en attente : Client A · 1 200 € · depuis le 21/07</span>','  <span class="m">  (les devis expirés sont tous des tests)</span>','<span class="g">list_factures</span>()','  <span class="o">→ 2 en attente : Client B · 1 428 € (09/10)</span>','  <span class="o">                 Client A · 600 € (21/07)</span>','<span class="g">get_today_schedule</span>(week)','  <span class="o">→ aucun rendez-vous cette semaine</span>','<span class="m"># priorité 1 : relancer Client A (devis + facture)</span>'];
const S5=[['ecran-formulaire-prospect.webp',V(1,24.4)],['ecran-resultat-prospection.webp',V(1,25.18)],['ecran-liste-des-entreprises.webp',V(1,26.36)]];
$('s5scr').innerHTML=S5.map(s=>`<img src="a/img/${s[0]}" style="opacity:0">`).join('');const s5i=[...$('s5scr').children];
const SEG=['Restauration traditionnelle','Boulangerie-pâtisserie','Restauration rapide','Traiteur','Bar / brasserie','Chaînes et franchises','Clients FoodEatUp'];
$('s5seg').innerHTML=SEG.map((s,i)=>`<div class="pill" id="g${i}" style="left:${[60,450,60,400,620,60,460][i]}px;top:${[1150,1150,1230,1230,1230,1310,1310][i]-0}px;font-size:22px;padding:8px 18px">${s}</div>`).join('');
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=9.8&&t<V(1,32.6))?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.3):cl((t-a)/.22),fo=id==='s7'?1:1-cl((t-(b-.18))/.18);el.style.opacity=Math.min(fi,fo);}}
  if(t<9.8){[3.22,3.94,4.76,5.44,6.2].forEach((w,i)=>slam($('c'+i),t,V(0,w),`rotate(${[-4,3,2,-3,-1][i]}deg)`));
    const m=$('s0m');pop(m,t,V(0,2.6),.4,80);if(t>V(0,6.2))m.style.transform=`translateX(${Math.sin(t*28)*6}px)`;slam($('s0b'),t,V(0,8.18));}
  else if(t<13.9){pop($('s1tab'),t,9.85,.45,50,.03);pop($('s1l'),t,V(0,10.06),.35,10,.1);slam($('s1c'),t,V(0,11.64));}
  else if(t<20.1){[15.16,16.76,18.28].forEach((w,i)=>pop($('q'+i),t,V(0,w)-.1,.35,40,.05));pop($('s2m'),t,14.0,.45,80);}
  else if(t<28.05){pop($('s3t'),t,20.15,.35,30);lines($('s3pre'),L3,t,20.4,1.55);}
  else if(t<V(1,24.0)){pop($('s4m'),t,28.1,.4,40);pop($('s4f'),t,29.4,.4,40);slam($('s4b'),t,V(1,22.6),'rotate(-2deg)');}
  else if(t<V(1,28.08)){let k=0;S5.forEach((s,i)=>{if(t>=s[1])k=i;});s5i.forEach((im,i)=>{im.style.opacity=i===k?1:0;im.style.transform=i===k?`scale(${1+.06*cl((t-S5[k][1])/1.2)})`:'';});
    $('s5bar').style.clipPath=`inset(0 ${100-100*eout(cl((t-V(1,24.2))/.7))}% 0 0)`;SEG.forEach((s,i)=>pop($('g'+i),t,V(1,25.18)+i*.12,.3,20,.1));}
  else if(t<V(1,32.6)){pop($('s6a'),t,V(1,28.08),.35,20);slam($('s6b'),t,V(1,30.32));}
  else {pop($('s7p'),t,V(1,32.6),.4,0,.2);slam($('s7a'),t,V(1,32.66)+.05);const b=$('s7b');if(t>=V(1,34.5))slam(b,t,V(1,34.5),'rotate(-2deg)');else b.style.opacity=0;pop($('s7l'),t,44.0,.4,20);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
