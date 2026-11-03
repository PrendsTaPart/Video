const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const A=[0,8.19,18.497,27.72,38.595,48.354,58.143,70.24], P=[1.0,10.4,21.8,42.0,54.0,79.0,96.0];
const V=(i,w)=>P[i]+(w-A[i]);
const SC=[['s0',0,10.0],['s1',10.0,21.3],['s2',21.3,31.4],['s3',31.4,41.6],['s4',41.6,53.4],['s5',53.4,64.0],['s6',64.0,78.5],['s7',78.5,88.9],['s8',88.9,95.8],['s9',95.8,108.4],['s10',108.4,120.0]];
const DUR=120.0;
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
function lines(el,arr,t,a,lps){const n=Math.max(0,Math.floor((t-a)*lps)+(t>=a?1:0));el.innerHTML=arr.slice(0,n).join('\n');}
const CHN=[['FoodEatUp',60,560,'UC0Mc8pkW4t3uVjbI-ULptUA',87],['RapidoCRM',720,560,'UCXyptH13bJF7AVr2TZJWA-Q',71],['Plan-it',60,780,'UCj2P8FZ4YwygALBLITfOKNA',18],['RapidoCMS',720,780,'UCLQxmt2Wgsm-tX44CUOobPg',16]];
// s0 : 4 chaînes qui convergent
$('s0ch').innerHTML=CHN.map(([n,x,y],i)=>`<div class="ch" id="c${i}" style="left:${x}px;top:${y}px">${n}</div>`).join('');
$('s0l').innerHTML=CHN.map(([n,x,y],i)=>`<line id="l${i}" x1="${x+150}" y1="${y+48}" x2="540" y2="1040" stroke="#e11d2a" stroke-width="5" stroke-dasharray="12 9"/>`).join('');
// s1 : captures des chaînes + tâches
$('s1scr').innerHTML=CHN.map(c=>`<img src="a/img/chaine-${c[3]}.png" style="opacity:0">`).join('');const s1i=[...$('s1scr').children];
const T1=[['préparer les vidéos',12.14,70,1150],['écrire les titres',13.22,560,1150],['programmer les publications',14.16,70,1240],['suivre les résultats',15.48,620,1240]];
$('s1p').innerHTML=T1.map(([t,,x,y],i)=>`<div class="pill" id="p${i}" style="left:${x}px;top:${y}px">${t}</div>`).join('')+`<div class="badge" id="p4" style="left:250px;top:1360px;font-size:44px">Tout centraliser</div>`;
// s2 : l'application
const S2=[['accueil.png','Une seule interface · visuels d\'exemple du site',18.497],['videos.png','Organiser les vidéos',22.74],['videos2.png','Infos de chaque vidéo',24.34],['chaine-UC0Mc8pkW4t3uVjbI-ULptUA.png','Historique par chaîne',25.22],['autopilot.png','Espace connecté',26.96]];
$('s2scr').innerHTML=S2.map(s=>`<img src="a/img/${s[0]}" style="opacity:0">`).join('');const s2i=[...$('s2scr').children];
// s3 : galerie
$('s3g').innerHTML=CHN.map(([n,,,id,k],i)=>`<div class="gc" id="g${i}" style="left:${i%2?555:60}px;top:${390+Math.floor(i/2)*470}px"><img src="a/img/chaine-${id}.png"><b>${k}</b><span>vidéos partagées · ${n}</span></div>`).join('');
// s4 : flux + outils
const F4=[['Claude',60],['MCP YouTube',380],['Publisher Bot',700]];
$('s4f').innerHTML=F4.map(([t,x],i)=>`<div class="ch" id="f${i}" style="left:${x}px;top:410px;width:300px;font-size:30px;${i==1?'background:#e11d2a;border-color:#e11d2a':''}">${t}</div>`).join('')+`<div class="abs" id="f3" style="left:360px;top:440px;font-size:30px;color:var(--grey)">→</div><div class="abs" id="f4" style="left:680px;top:440px;font-size:30px;color:var(--grey)">→</div>`;
const L4=['<span class="m"># 86 outils déclarés (aussi préfixés yt_)</span>','<span class="g">list_channels</span>     <span class="m">consulter les chaînes</span>','<span class="g">list_videos</span>       <span class="m">récupérer les vidéos</span>','<span class="g">get_channel_analytics</span> <span class="m">analyser</span>','<span class="g">schedule_video</span>    <span class="m">préparer une action</span>','<span class="o">aucun appel d\'écriture pendant l\'audit</span>'];
// s6 : tableau des statuts
const R6=[['Galerie publique des vidéos','y','y','y','y','192 vidéos partagées'],['Serveur MCP (86 outils)','y','y','q','q','manifeste public lu'],['Programmation des Shorts','y','q','q','q','ton relevé : jusqu\'au 31/10'],['Autopilote','y','q','q','n','non activé à ma connaissance'],['Tests A/B des miniatures','y','q','q','q','seuil de 95 %'],['Paiement des crédits','n','n','n','n','par e-mail pour l\'instant']];
const SY={y:'✓',q:'?',n:'—'};
$('s6t').innerHTML=`<tr><th style="width:400px">Fonction</th><th>codée</th><th>configurée</th><th>testée</th><th>exécutée</th></tr>`+R6.map((r,i)=>`<tr id="t${i}"><td>${r[0]}<small>${r[5]}</small></td>${r.slice(1,5).map(s=>`<td class="${s}">${SY[s]}</td>`).join('')}</tr>`).join('');
// s8 : boucle
const LO=['contenu','programmation','publication','analyse','amélioration'];
const pos=LO.map((_,i)=>{const a=-Math.PI/2+i*2*Math.PI/5;return [540+330*Math.cos(a),900+330*Math.sin(a)];});
$('s8n').innerHTML=LO.map((t,i)=>`<div class="lo" id="o${i}" style="left:${pos[i][0]-150}px;top:${pos[i][1]-55}px">${t}</div>`).join('');
$('s8s').innerHTML=`<circle id="cir" cx="540" cy="900" r="330" fill="none" stroke="#e11d2a" stroke-width="6" stroke-dasharray="2074" stroke-dashoffset="2074"/>`;
// vignette
$('thch').innerHTML=CHN.map(([n],i)=>`<div class="pill c" style="left:${[40,760,40,760][i]}px;top:${[700,700,1120,1120][i]}px;font-size:28px">${n}</div>`).join('');

function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=10&&t<108.4&&!(t>=95.8))?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.5):cl((t-a)/.3),fo=id==='s10'?1:1-cl((t-(b-.25))/.25);el.style.opacity=Math.min(fi,fo);}}
  if(t<10){const p=$('s0p');const k=eout(cl((t-.1)/.8));p.style.opacity=k;p.style.transform=`scale(${.8+.2*k})`;
    CHN.forEach((c,i)=>{pop($('c'+i),t,V(0,2.56)+i*.12,.35,20,.1);$('l'+i).style.opacity=cl((t-V(0,2.86)-i*.1)/.4);});
    pop($('s0y'),t,V(0,3.18),.4,20,.1);slam($('s0a'),t,V(0,4.6));pop($('s0b'),t,V(0,7.46)-.2,.4,20);}
  else if(t<21.3){pop($('s1tab'),t,10.1,.5,50,.03);const k=Math.max(0,Math.min(3,Math.floor((t-10.1)/2.6)));s1i.forEach((im,i)=>im.style.opacity=i===k?1:0);
    $('s1r').textContent='Chaîne '+CHN[k][0]+' · galerie Publisher Bot';
    T1.forEach(([,w],i)=>slam($('p'+i),t,V(1,w)-.05));const b=$('p4');if(t>=V(1,17.42))slam(b,t,V(1,17.42),'rotate(-2deg)');else b.style.opacity=0;}
  else if(t<31.4){pop($('s2tab'),t,21.4,.5,50,.03);pop($('s2lv'),t,V(2,20.12),.4,10,.1);let k=0;S2.forEach((s,i)=>{if(t>=V(2,s[2]))k=i;});
    s2i.forEach((im,i)=>{im.style.opacity=i===k?1:0;});const l=$('s2lb');l.textContent=S2[k][1];pop($('s2c'),t,V(2,26.96),.4,10);}
  else if(t<41.6){CHN.forEach((c,i)=>pop($('g'+i),t,31.6+i*.6,.45,50,.04));pop($('s3r'),t,34.4,.4,10);}
  else if(t<53.4){F4.forEach((f,i)=>pop($('f'+i),t,41.7+i*.35,.35,20,.1));['f3','f4'].forEach((f,i)=>$(f).style.opacity=cl((t-42.1-i*.35)/.3));
    pop($('s4t'),t,V(3,32.2)-.2,.4,30);lines($('s4pre'),L4,t,V(3,32.2),1.6);pop($('s4q'),t,V(3,36.3),.45,30);pop($('s4n'),t,V(3,37.82),.4,20);}
  else if(t<64){[38.64,42.88,45.2,46.84,47.94].forEach((w,i)=>pop($('r'+i),t,V(4,w)-.25,.4,40,.03));pop($('s5m'),t,V(4,43.98),.5,80);}
  else if(t<78.5){R6.forEach((r,i)=>pop($('t'+i),t,64.4+i*1.1,.4,30));}
  else if(t<88.9){[52.4,52.94,53.86].forEach((w,i)=>slam($('k'+i),t,V(5,w)-.1));pop($('s7q'),t,79.2,.45,30);pop($('s7b'),t,V(5,55.42),.4,20,.05);pop($('s7m'),t,V(5,49.86),.5,80);}
  else if(t<95.8){const c=$('cir');c.style.strokeDashoffset=2074*(1-cl((t-89.2)/4.5));LO.forEach((x,i)=>pop($('o'+i),t,89.2+i*.9,.35,0,.3));}
  else if(t<108.4){pop($('s9p'),t,96.0,.5,0,.2);pop($('s9a'),t,V(6,61.04)-.2,.5,30);slam($('s9b'),t,V(6,65.96));slam($('s9c'),t,V(6,66.64));
    const d=$('s9d');if(t>=V(6,68.36))slam(d,t,V(6,68.36),'rotate(-2deg)');else d.style.opacity=0;}
  else {pop($('s10p'),t,108.6,.5,0,.2);pop($('s10a'),t,109.1,.5,30);pop($('s10b'),t,110.0,.5,20);pop($('s10l'),t,110.8,.5,20,.1);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
