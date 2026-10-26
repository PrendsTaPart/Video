const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const A=[0,8.714,18.652,29.42,45.628,59.18,74.536,88.96], P=[1.0,10.8,21.8,46.6,64.0,78.8,95.4];
const V=(i,w)=>P[i]+(w-A[i]);
const SC=[['s0',0,10.6],['s1',10.6,21.6],['s2',21.6,32.8],['s3',32.8,46.3],['s4',46.3,63.6],['s5',63.6,78.5],['s6',78.5,95.1],['s7',95.1,110.2],['s8',110.2,120.0]];
const DUR=120.0;
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
function lines(el,arr,t,a,lps){const n=Math.max(0,Math.floor((t-a)*lps)+(t>=a?1:0));el.innerHTML=arr.slice(0,n).join('\n');}
// écran de tablette à fondu enchaîné
function slides(box,list){box.innerHTML=list.map(([src])=>`<img src="a/app/${src}.png" style="opacity:0">`).join('');return [...box.children];}
function showSlides(imgs,list,t,zoom=0){let cur=-1;list.forEach(([,a],i)=>{if(t>=a)cur=i;});
  imgs.forEach((im,i)=>{const a=list[i][1];const nx=list[i+1]?list[i+1][1]:1e9;
    let o=0;if(i===cur)o=1;else if(i===cur+1&&t>nx-.25)o=cl((t-(nx-.25))/.25);
    if(i===cur&&i>0){o=Math.max(o,cl((t-a)/.25));}
    im.style.opacity=i<=cur?(i===cur?1:(t<a+.25?1:0)):0;
    if(i===cur){im.style.opacity=1;im.style.zIndex=2;const f=cl((t-a)/2.5);im.style.transform=`scale(${1+zoom*f})`;im.style.transformOrigin='30% 30%';im.style.clipPath=`inset(0 0 0 0)`;im.style.filter='none';im.style.opacity=cl((t-a)/.25)+ (i===0?1:0);}
    else{im.style.zIndex=1;}
  });}
const L2=[['01-accueil-categories',V(2,20.4)],['02-recherche-cold-foam',V(2,21.5)],['06-fiche-ingredients',V(2,22.76)],['16-allergenes-sans-lait',V(2,24.38)],['08-etape-1',V(2,25.24)],['14-academy',V(2,27.88)]];
const im2=slides($('s2scr'),L2);
const F2=[['Catégories',20.64,70,1120],['Recherche',21.5,330,1120],['Ingrédients & quantités',22.76,590,1120],['Allergènes',24.38,70,1200],['Pas à pas',25.24,300,1200],['Academy',27.88,530,1200]];
$('s2pills').innerHTML=F2.map(([t,,x,y],i)=>`<div class="pill${i==4?' b':''}" id="s2p${i}" style="left:${x}px;top:${y}px">${t}</div>`).join('');
const D=[['01-accueil-categories','① L\'accueil : 9 catégories'],['03-categorie-ube','② La catégorie Ube'],['04-categorie-ube-glace','③ Le filtre « Glacé »'],['05-fiche-haut','④ La fiche recette'],['06-fiche-ingredients','⑤ Ingrédients et quantités'],['08-etape-1','⑥ Pas à pas · étape 1 / 3'],['09-etape-2','⑦ Étape 2 / 3'],['10-etape-3','⑧ Étape 3 / 3'],['12-rush','⑨ Mode rush, au comptoir']];
const L3=D.map(([s],i)=>[s,32.9+i*1.48]);
const im3=slides($('s3scr'),L3);
const S4=['<span class="k">list_recipes</span>(établissement du client)',
 '<span class="m">→ </span><span class="o">101 recettes</span><span class="m"> · 15 catégories (Coffee, Smoothies, Ube, Matcha…)</span>',
 '<span class="m">→ noms, catégories, compositions et étapes</span>',
 '<span class="m">→ compositions lues, aucun prix ni coût affiché</span>'];
$('s7pills').innerHTML=[['recettes',78.46,560,960],['formation',79.14,770,960],['fiches techniques',80.0,560,1040],['reliée à FoodEatUp',81.16,60,1040]].map(([t,,x,y],i)=>`<div class="pill${i==3?' b':''}" id="s7p${i}" style="left:${x}px;top:${y}px">${t}</div>`).join('');
$('pages').innerHTML=Array.from({length:7},(_,i)=>`<div class="paper" id="pg${i}" style="left:${640+i*8}px;top:${400+i*10}px;width:360px;height:480px;transform:rotate(${(i%2?1:-1)*(2+i)}deg)"></div>`).join('');
const QU=[['03/10 · premier prompt','« Crée [nom du client] Recettes… pour que l\'équipe retrouve et apprenne chaque recette sans chercher dans le classeur papier. »',61.0],
 ['03/10 · FoodEatUp','« Connecte l\'application au MCP FoodEatUp pour mettre à jour les recettes depuis FoodEatUp. »',62.2],
 ['04/10 · décision','« Je ne veux pas d\'IA : tout doit être pré-enregistré. » (textes et voix de la formatrice figés)',63.64]];
$('s6q').innerHTML=QU.map(([h,q],i)=>`<div class="quote" id="q${i}" style="top:${370+i*200}px"><b>${h}</b>${q}</div>`).join('');

function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=10.6&&t<110.2)?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?1:cl((t-a)/.3),fo=id==='s8'?1:1-cl((t-(b-.25))/.25);el.style.opacity=Math.min(fi,fo);}}
  if(t<10.6){
    pop($('s0c'),t,.1,.4,20);pop($('s0t'),t,.25,.5,30);pop($('s0tab'),t,.4,.6,60,.04);pop($('s0r'),t,1.0,.4,10);
    const b=$('s0b');if(t>=V(0,3.36))slam(b,t,V(0,3.36),'rotate(-3deg)');else b.style.opacity=0;
    pop($('s0m'),t,V(0,2.0),.5,80);
    pop($('s0l1'),t,V(0,4.3),.4,20);pop($('s0l2'),t,V(0,6.62),.4,20,.2);
  }
  else if(t<21.6){
    pop($('s1p'),t,V(1,8.88),.5,40,.03);pop($('s1pr'),t,V(1,9.2),.4,10);
    for(let i=0;i<7;i++)pop($('pg'+i),t,V(1,11.5)+i*.12,.3,-80,0,`rotate(${(i%2?1:-1)*(2+i)}deg)`);
    const n=$('s1n');const k=cl((t-V(1,12.28))/1.0);n.style.opacity=k>0?1:0;n.firstChild.textContent=String(Math.round(161*eout(k)));
    slam($('s1k'),t,V(1,13.58));
    pop($('s1tab'),t,V(1,17.08),.6,200,.1,'rotate(-3deg)');
  }
  else if(t<32.8){
    showSlides(im2,L2,t,.06);
    F2.forEach(([,w],i)=>slam($('s2p'+i),t,V(2,w)-.05));pop($('s2m'),t,21.9,.5,60);
  }
  else if(t<46.3){
    showSlides(im3,L3,t,.08);
    let cur=0;L3.forEach(([,a],i)=>{if(t>=a)cur=i;});const st=$('s3step');st.textContent=D[cur][1];
    const a=L3[cur][1];st.style.opacity=cl((t-a)/.2);st.style.transform=`translateX(${(1-eout(cl((t-a)/.3)))*-40}px)`;
  }
  else if(t<63.6){
    pop($('s4t'),t,V(3,31.2),.4,30);lines($('s4pre'),S4,t,V(3,32.5),1.4);
    [33.94,37.0,41.56,44.4].forEach((w,i)=>pop($('r'+i),t,V(3,w)-.1,.4,30,.03));
    pop($('s4n'),t,V(3,44.9),.4,10);pop($('s4w'),t,V(3,45.3),.4,20);
  }
  else if(t<78.5){
    pop($('s5a'),t,V(4,47.6),.5,60,.04,'rotate(-2deg)');pop($('s5al'),t,V(4,48.2),.3,10);
    pop($('s5b'),t,V(4,51.06),.5,60,.04,'rotate(2.5deg)');
    pop($('s5s'),t,V(4,55.84),.4,30);
  }
  else if(t<95.1){
    [0,1,2].forEach(i=>pop($('q'+i),t,QU[i][2]-A[5]+P[5]-.1,.4,30));
    pop($('s6m'),t,V(5,60.94),.5,20);
    [63.74,65.96,67.26].forEach((w,i)=>pop($('st'+i),t,V(5,w),.4,30,.1));
    pop($('s6a'),t,V(5,70.8),.4,30);pop($('s6b'),t,V(5,72.4),.4,30);
  }
  else if(t<110.2){
    pop($('s7a'),t,V(6,75.62)-.2,.45,40,0,'');pop($('s7b'),t,V(6,77.8)-.2,.45,40,.05);
    [78.46,79.14,80.0,81.16].forEach((w,i)=>slam($('s7p'+i),t,V(6,w)-.05));
    pop($('s7m'),t,V(6,82.0),.5,80);
  }
  else {
    pop($('s8a'),t,110.4,.6,30);const b=$('s8b');if(t>=111.3)slam(b,t,111.3,'rotate(-2deg)');else b.style.opacity=0;
    pop($('s8c'),t,112.2,.5,20);pop($('s8l'),t,113.0,.5,20,.1);
  }
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
