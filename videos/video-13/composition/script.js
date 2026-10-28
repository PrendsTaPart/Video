const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const O=0.6, W=w=>O+w;
const SC=[['s0',0,3.1],['s1',3.1,11.0],['s2',11.0,13.9],['s3',13.9,17.9],['s4',17.9,22.9],['s5',22.9,26.8],['s6',26.8,34.9],['s7',34.9,41.5]];
const DUR=41.5;
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
function lines(el,arr,t,a,lps){const n=Math.max(0,Math.floor((t-a)*lps)+(t>=a?1:0));el.innerHTML=arr.slice(0,n).join('\n');}
const TH=['miniature-episode0-1080x1920.jpg','miniature-episode1-1080x1920.jpg','miniature-episode4-1080x1920.jpg','miniature-episode5-1080x1920.jpg','miniature-episode6-1080x1920.jpg','miniature-episode9-1080x1920.jpg','miniature-episode10-1080x1920.jpg','miniature-video11.jpg'];
$('s1th').innerHTML=TH.map((f,i)=>`<div class="th" id="t${i}" style="left:${60+(i%4)*250}px;top:${400+Math.floor(i/4)*450}px;transform:rotate(${[-3,2,-2,3,2,-3,3,-2][i]}deg)"><img src="a/ep/${f}"></div>`).join('');
const P1=[['des applications',6.96,70,1330],['des agents IA',7.94,430,1330],['des vidéos',8.86,740,1330],['des bandes dessinées',9.6,300,1420]];
$('s1p').innerHTML=P1.map(([t,,x,y],i)=>`<div class="pill${i==3?' b':''}" id="p${i}" style="left:${x}px;top:${y}px">${t}</div>`).join('');
const S4=[['extensions-1.png','Le catalogue d\'idées',17.9],['extensions-2.png','Chaque idée : produit, difficulté, potentiel',19.2],['daily.png','Daily Brief · FoodEatUp',W(18.36)],['daily-1.png','Le cahier des charges et le prompt Lovable',W(19.32)],['daily-3.png','Prompts de routine et de plugin',W(19.98)]];
$('s4scr').innerHTML=S4.map(s=>`<img src="a/img/${s[0]}" style="opacity:0">`).join('');const s4i=[...$('s4scr').children];
const L5=['<span class="g">list_projects</span>()        <span class="m">→ catalogue de 100 idées</span>','<span class="g">get_project_context</span>(daily-brief)','<span class="m">  → besoin, charte, prompts Lovable · Figma · Claude Code</span>','<span class="g">get_project_roadmap</span>   <span class="m">→ du socle à la publication</span>','<span class="g">get_project_agents</span>    <span class="m">→ 6 agents</span>','<span class="o">aucun projet enregistré pour cette vidéo</span>'];
const AG=[['agent-leo.jpg','Léo','référent'],['agent-orchestrateur.jpg','Orchestrateur','routine'],['agent-marc.jpg','Marc','verdict'],['ali-pass.jpg','Ali','salle'],['lena-ux.jpg','Léna','produit'],['paul-veilleur.jpg','Paul','veille']];
$('s5ag').innerHTML=AG.map(([f,n,r],i)=>`<div class="ag" id="a${i}" style="left:${70+(i%3)*330+80}px;top:${760+Math.floor(i/3)*270}px"><img src="a/ag/${f}">${n}<small>${r}</small></div>`).join('');
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=3.1&&t<34.9)?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.3):cl((t-a)/.25),fo=id==='s7'?1:1-cl((t-(b-.2))/.2);el.style.opacity=Math.min(fi,fo);}}
  if(t<3.1){pop($('s0p'),t,.05,.4,0,.2);pop($('s0a'),t,W(.66),.35,20);slam($('s0b'),t,W(1.38));}
  else if(t<11.0){TH.forEach((f,i)=>pop($('t'+i),t,3.2+i*.32,.35,60,.05,`rotate(${[-3,2,-2,3,2,-3,3,-2][i]}deg)`));P1.forEach(([,w],i)=>slam($('p'+i),t,W(w)-.05));}
  else if(t<13.9){slam($('s2a'),t,W(11.42)-.3);pop($('s2m'),t,11.3,.45,80);}
  else if(t<17.9){pop($('s3tab'),t,13.95,.45,50,.03);const k=cl((t-W(14.92))/1.0);$('s3n').textContent=Math.round(100*eout(k));pop($('s3n'),t,W(14.8),.3,20);pop($('s3l'),t,W(15.2),.35,20);}
  else if(t<22.9){let k=0;S4.forEach((s,i)=>{if(t>=s[2])k=i;});s4i.forEach((im,i)=>{im.style.opacity=i===k?1:0;im.style.transform=i===k?`scale(${1+.05*cl((t-S4[k][2])/1.5)})`:'';});$('s4l').textContent=S4[k][1];pop($('s4s'),t,W(18.36),.4,20);}
  else if(t<26.8){pop($('s5t'),t,22.95,.35,30);lines($('s5pre'),L5,t,23.1,2.2);AG.forEach((a,i)=>pop($('a'+i),t,24.4+i*.2,.35,30,.1));pop($('s5r'),t,25.4,.35,10);}
  else if(t<34.9){pop($('s6a'),t,W(26.42),.35,20);slam($('s6b'),t,W(28.44));pop($('s6c'),t,W(30.68),.4,30);slam($('s6d'),t,W(32.34));}
  else {slam($('s7a'),t,35.0);pop($('s7b'),t,W(34.98),.35,20);slam($('s7c'),t,W(36.24),'rotate(-2deg)');pop($('s7l'),t,38.4,.4,20);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
