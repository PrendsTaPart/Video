const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const W=w=>0.6+w;
const SC=[['s0',0,3.7],['s1',3.7,W(9.26)],['s2',W(9.26),W(15.44)],['s3',W(15.44),W(24.7)],['s4',W(24.7),W(28.68)],['s5',W(28.68),W(32.82)],['s6',W(32.82),W(38.28)],['s7',W(38.28),W(42.26)],['s8',W(42.26),W(49.02)],['s9',W(49.02),59.0]];
const DUR=59.0;
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
function lines(el,arr,t,a,lps){const n=Math.max(0,Math.floor((t-a)*lps)+(t>=a?1:0));el.innerHTML=arr.slice(0,n).join('\n');}
function seq(img,dir,t,t0,n,off=0){const f=Math.max(0,Math.min(n-1,Math.floor((t-t0)*15)+off));img.src=`a/${dir}/`+String(f+1).padStart(4,'0')+'.jpg';}
// s0 : agents qui sollicitent
const AG=[['nina','Nina : 3 devis à relancer ?',40,250,-3],['theo','Théo : je publie quoi ?',560,330,3],['leo','Léo : stock bas !',60,560,2],['sam','Sam : planning de lundi ?',540,640,-2]];
$('s0a').innerHTML=AG.map(([a,q,x,y,r],i)=>`<div id="ag${i}" class="abs" style="left:${x}px;top:${y}px"><div class="av" style="position:relative;width:120px;height:120px;display:inline-block;vertical-align:middle"><img src="a/img/agent-${a}.png"></div><div class="qb" style="position:relative;display:inline-block;vertical-align:middle;margin-left:10px;transform:rotate(${r}deg)">${q}</div></div>`).join('');
// s1 : fenêtres qui s'empilent
const CH=['Conversation 1','Conversation 2','Tâches','Prompts','Connecteurs','Conversation 3'];
$('s1c').innerHTML=CH.map((c,i)=>`<div class="pill" id="c${i}" style="left:${90+(i%3)*300}px;top:${720+Math.floor(i/3)*110}px;font-size:26px">${c}</div>`).join('');
// s3 : terminal
const L3=['<span class="g">route_orchestrator</span>(« Organise ma campagne commerciale','  FoodEatUp de la semaine… »)','  <span class="o">rapidocrm · list_campagnes</span>','  <span class="o">rapidocrm · list_newsletters</span>','  <span class="o">foodeatup · get_marketing_calendar</span>','  <span class="m">foodeatup · add_marketing_event</span>','  <span class="m">plugin_braindcode · ma_semaine</span>','  <span class="m">agents : []</span>'];
// s5 : connecteurs
const MC=[['foodeatup.png','FoodEatUp · 193',140,560],['rapidocrm-logo-officiel.png','RapidoCRM · 131',700,560],['rapidocms-logo-officiel.png','RapidoCMS · 45',60,910],['rapidorh.png','RapidoRH · 22',780,910],['braindcode.png','Plugins BraindCode · 53',140,1260],['planit.png','Plan\'It natif · 63',700,1260]];
$('s5n').innerHTML=MC.map(([l,t,x,y],i)=>`<div class="lg" id="mc${i}" style="left:${x}px;top:${y}px"><img src="a/logos/${l}">${t}<br>outils</div>`).join('');
$('s5l').innerHTML=MC.map(([l,t,x,y],i)=>`<path id="ml${i}" d="M540 970 L${x+120} ${y+59}" stroke-dasharray="900" stroke-dashoffset="900"/>`).join('');
// s6 : outils à confirmation
const DT=['run_routine_now','accept_routine_proposal','resume_routine','pause_routine','delete_task','remove_mcp_server'];
$('s6r').innerHTML=DT.map((d,i)=>`<div class="lock" id="dt${i}" style="top:${510+i*105}px"><code>${d}</code><span>confirmation</span></div>`).join('');
// s9 : rôles
const RO=[['marc','Stratégie','Marc · le Directeur',60,180],['theo','Communication','Théo · RapidoCMS',440,120],['nina','Commercial','Nina · RapidoCRM',820,180],['sam','Organisation','Sam · RapidoRH',60,870],['orchestrateur','Contrôle','L\'Orchestrateur',820,870]];
$('s9r').innerHTML=RO.map(([a,r,n,x,y],i)=>`<div class="role" id="ro${i}" style="left:${x}px;top:${y}px"><div class="av"><img src="a/img/agent-${a}.png"></div><b>${r}</b><span>${n}</span></div>`).join('');
$('thr').innerHTML=[['nina',60,560],['theo',860,560],['leo',60,900],['sam',860,900],['marc',120,1240],['iris',800,1240]].map(([a,x,y])=>`<div class="av" style="left:${x}px;top:${y}px;width:160px;height:160px"><img src="a/img/agent-${a}.png"></div>`).join('');
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=3.7&&t<W(49.02))?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.3):cl((t-a)/.22),fo=id==='s9'?1:1-cl((t-(b-.18))/.18);el.style.opacity=Math.min(fi,fo);}}
  if(t<3.7){AG.forEach((a,i)=>pop($('ag'+i),t,.2+i*.55,.3,30,.2));pop($('s0m'),t,.1,.4,80);pop($('s0i'),t,1.5,.4,10);}
  else if(t<W(9.26)){pop($('s1a'),t,W(3.12),.35,20);CH.forEach((c,i)=>pop($('c'+i),t,W(5.5)+i*.25,.3,30,.2,`rotate(${(i%2?3:-3)}deg)`));slam($('s1b'),t,W(7.3));}
  else if(t<W(15.44)){pop($('s2l'),t,W(9.4),.5,0,.5);slam($('s2t'),t,W(9.86));pop($('s2p0'),t,W(11.96),.35,30);pop($('s2p1'),t,W(13.04),.35,30);pop($('s2p2'),t,W(14.38),.35,30);}
  else if(t<W(24.7)){pop($('u0'),t,W(15.6),.4,40);pop($('s3t'),t,W(19.4),.3,30);lines($('s3pre'),L3,t,W(19.5),5);
    pop($('s3a'),t,W(21.34),.35,30,.2);pop($('s3b'),t,W(22.98),.35,30,.2);pop($('s3c'),t,W(23.6),.35,30,.2);pop($('s3r'),t,W(23.9),.35,10);}
  else if(t<W(28.68)){pop($('s4ph'),t,W(24.75),.4,60);seq($('s4i'),'taches',t,W(24.7),135,30);pop($('s4q'),t,W(26.6),.4,30);pop($('s4p'),t,W(27.6),.35,20);}
  else if(t<W(32.82)){pop($('s5c'),t,W(28.7),.4,0,.5);MC.forEach((m,i)=>{const a=W(29.0)+i*.4;pop($('mc'+i),t,a,.35,20,.3);$('ml'+i).style.strokeDashoffset=900*(1-eout(cl((t-a)/.5)));});}
  else if(t<W(38.28)){pop($('s6g0'),t,W(34.96),.3,20,.3);pop($('s6g1'),t,W(35.6),.3,20,.3);pop($('s6g2'),t,W(36.48),.3,20,.3);DT.forEach((d,i)=>pop($('dt'+i),t,W(33.0)+i*.25,.3,30,.03));}
  else if(t<W(42.26)){pop($('s7ph'),t,W(38.3),.4,60);seq($('s7i'),'dash',t,W(38.3),390,0);pop($('s7ph2'),t,W(39.6),.4,60);seq($('s7j'),'taches',t,W(39.6),135,40);}
  else if(t<W(49.02)){for(let i=0;i<3;i++)pop($('k'+i),t,W(42.3)+i*.3,.35,30,.2);pop($('k3'),t,W(43.4),.35,10);pop($('s8a'),t,W(44.52),.35,20);slam($('s8b'),t,W(47.06));}
  else {pop($('s9p'),t,W(49.02),.4,0,.2);RO.forEach((r,i)=>pop($('ro'+i),t,W(49.4)+i*.3,.35,30,.3));slam($('s9a'),t,W(49.84));pop($('s9i'),t,W(51.5),.4,10);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
