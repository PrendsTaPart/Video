const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const O=0.6, W=w=>O+w;
const SC=[['s0',0,5.2],['s1',5.2,9.6],['s2',9.6,19.2],['s3',19.2,28.3],['s4',28.3,35.9],['s5',35.9,41.9],['s6',41.9,44.8],['s7',44.8,49.0]];
const DUR=49.0;
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
function lines(el,arr,t,a,lps){const n=Math.max(0,Math.floor((t-a)*lps)+(t>=a?1:0));el.innerHTML=arr.slice(0,n).join('\n');}
const L0=['<span class="err">✗ get_kpis       attendu 200 · obtenu 500</span>','<span class="err">✗ list_bugs      valeur attendue absente</span>','<span class="g">✓ whoami         200</span>','<span class="err">✗ get_progress   délai dépassé</span>'];
const ST=[['TESTER','scénarios','fx',19.02],['DÉTECTER','attendu ≠ obtenu','fx',19.14],['TICKET','create_bug','fx',20.7],['PROMPT','de débogage','fq',22.14],['CORRIGER','Claude Code · branche','fq',23.9],['RETESTER','relancer les tests','fq',25.38],['VALIDER','humain','fh',27.16]];
const pos=ST.map((_,i)=>{const a=-Math.PI/2+i*2*Math.PI/7;return [540+360*Math.cos(a),900+360*Math.sin(a)];});
$('s3n').innerHTML=ST.map(([t,s,c],i)=>`<div class="st" id="n${i}" style="left:${pos[i][0]-125}px;top:${pos[i][1]-48}px"><span class="${c}">${t}</span><small>${s}</small></div>`).join('');
const CAP=[[19.02,'<span class="err">✗ attendu 200<br>obtenu 500</span>'],[20.7,'Ticket : preuves<br>requête + réponse'],[22.14,'Prompt de débogage<br>pour Claude Code'],[23.9,'Correction<br>sur une branche'],[25.38,'Les tests<br>repartent…'],[27.16,'<span class="g">✓ réussi</span><br>validation humaine']];
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=5.2&&t<44.8)?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.3):cl((t-a)/.25),fo=id==='s7'?1:1-cl((t-(b-.2))/.2);el.style.opacity=Math.min(fi,fo);}}
  if(t<5.2){pop($('s0t'),t,.05,.3,20);lines($('s0pre'),L0,t,.2,3);pop($('s0a'),t,W(2.46),.4,20);$('s0m').style.opacity=0;}
  else if(t<9.6){pop($('s1a'),t,W(4.82),.35,20);slam($('s1b'),t,W(7.34));}
  else if(t<19.2){pop($('s2tab'),t,9.65,.4,40,.03);[11.24,12.26,14.96,15.58,16.26].forEach((w,i)=>pop($('k'+i),t,W(w)-.2,.3,20));slam($('s2b'),t,W(16.88));}
  else if(t<28.3){let cur=-1;ST.forEach((s,i)=>{if(t>=W(s[3]))cur=i;pop($('n'+i),t,W(s[3])-.1,.3,0,.3);$('n'+i).classList.toggle('on',i===cur);});
    $('cir').style.strokeDashoffset=2262*(1-cl((t-W(19.02))/(W(27.4)-W(19.02))));
    let c='';CAP.forEach(([w,h])=>{if(t>=W(w))c=h;});$('s3c').innerHTML=c;}
  else if(t<35.9){[27.8,29.18,30.66,31.6].forEach((w,i)=>pop($('r'+i),t,W(w)-.3,.35,30,.03));pop($('s4a'),t,W(33.12),.35,20);slam($('s4b'),t,W(34.32));}
  else if(t<41.9){pop($('s5a'),t,W(35.44)-.1,.4,30);slam($('s5b'),t,W(37.0));pop($('s5m'),t,W(37.6),.5,80);}
  else if(t<44.8){pop($('s6p'),t,42.0,.4,0,.2);pop($('s6a'),t,W(41.6),.4,30);}
  else {[44.9,45.6,46.3].forEach((a,i)=>slam($('f'+i),t,a));slam($('f3'),t,47.0);pop($('f4'),t,47.4,.4,10);pop($('s7l'),t,47.6,.4,20);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
