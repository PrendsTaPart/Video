const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const A=[0,26.7,43.0,62.4], P=[0.6,29.7,47.5];
const V=(i,w)=>P[i]+(w-A[i]);
const DUR=72;
const SC=[['s0',0,V(0,3.16)],['s1',V(0,3.16),V(0,9.88)],['s2',V(0,9.88),29.7],['s3',29.7,V(1,32.0)],['s4',V(1,32.0),V(1,36.92)],['s5',V(1,36.92),47.5],['s6',47.5,V(2,47.9)],['s7',V(2,47.9),V(2,57.9)],['s8',V(2,57.9),DUR]];
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
$('s1g').innerHTML=Array.from({length:19},(_,i)=>`<div class="th" id="th${i}" style="left:${20+(i%5)*210}px;top:${40+Math.floor(i/5)*320}px"><img src="a/thumbs/${String(i+1).padStart(2,'0')}.jpg"></div>`).join('');
const RL=[['claude.webp','Claude',20,9.88],['openai.webp','ChatGPT',20,10.96],['rapidocrm.png','RapidoCRM',49,12.46],['rapidocms.png','RapidoCMS',29,14.5],['rapidorh.png','RapidoRH',19,16.44],['','Figma',20,18.38],['lovable.png','Lovable',25,19.54],['','ElevenLabs',20,20.98],['planit.png','API IA Plan\'It',20,22.8]];
$('rl').innerHTML=RL.map(([f,n,p],i)=>`<div class="ln" id="rl${i}">${f?`<div class="lw"><img src="a/lg/${f}"></div>`:`<div class="lw t">${n}</div>`}<span style="font-family:P;font-weight:600">${n}</span><b>${n.startsWith('API')?'≈ ':''}${p} €</b></div>`).join('');
const ST=[['foodeatup.png','FoodEatUp','métier du restaurant',60,260],['rapidocrm.png','RapidoCRM','commercial',420,200],['rapidocms.png','RapidoCMS','communication',790,260],['rapidorh.png','RapidoRH','organisation',40,620],['foodeatup-infini.webp','FoodEatUp Formation','agents et méthodes',810,620],['braindcode.png','BraindCode Build','cahiers des charges',60,1150],['braindcode.webp','BraindCode Plugins','skills et prompts',420,1250],['startupforge.webp','StartupForge','stratégie',790,1150]];
$('s5s').innerHTML=ST.map(([f,n,r,x,y],i)=>`<div class="sat" id="sa${i}" style="left:${x}px;top:${y}px"><div class="lw"><img src="a/lg/${f}"></div><span>${n}<br><small style="color:var(--grey);font-weight:500">${r}</small></span></div>`).join('');
$('s5l').innerHTML=ST.map(([f,n,r,x,y],i)=>`<path id="ml${i}" d="M540 900 L${x+115} ${y+46}" stroke-dasharray="900" stroke-dashoffset="900"/>`).join('');
$('thl').innerHTML=[['claude.webp',40,800],['openai.webp',40,930],['lovable.png',40,1060],['rapidocrm.png',800,800],['rapidocms.png',800,930],['rapidorh.png',800,1060],['foodeatup.png',100,1260],['planit.png',420,1260],['braindcode.png',740,1260]].map(([f,x,y])=>`<div class="lw" style="left:${x}px;top:${y}px;width:${y>1200?260:240}px;height:100px"><img src="a/lg/${f}"></div>`).join('')+`<div class="lw t" style="left:180px;top:1400px;width:300px;height:90px">Figma</div><div class="lw t" style="left:600px;top:1400px;width:300px;height:90px">ElevenLabs</div>`;
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=V(0,3.16)&&t<V(2,57.9))?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.2):cl((t-a)/.22),fo=id==='s8'?1:1-cl((t-(b-.18))/.18);el.style.opacity=Math.min(fi,fo);}}
  if(t<V(0,3.16)){slam($('s0a'),t,.15);pop($('s0m'),t,.4,.4,80);}
  else if(t<V(0,9.88)){for(let i=0;i<19;i++)pop($('th'+i),t,V(0,3.2)+i*.13,.25,30,.3,`rotate(${i%2?2:-2}deg)`);slam($('s1a'),t,V(0,7.96));}
  else if(t<29.7){pop($('rc'),t,V(0,9.9),.3,60);let s=0;RL.forEach((r,i)=>{const p=pop($('rl'+i),t,V(0,r[3]),.25,20);if(t>=V(0,r[3]))s+=r[2];});
    $('tt').style.opacity=t>=V(0,24.52)?1:.25;const k=eout(cl((t-V(0,24.52))/.8));$('tv').textContent=(t>=V(0,24.52)?Math.round(178+(222-178)*k):s)+' €';if(t>=V(0,25.28))slam($('tv'),t,V(0,25.28));pop($('tf'),t,27.6,.4,10);}
  else if(t<V(1,32.0)){[0,1,2,3,4].forEach(i=>pop($('a'+i),t,V(1,[26.8,29.12,30.96,31.2,31.6][i]),.3,30,.03));}
  else if(t<V(1,36.92)){[0,1,2,3].forEach(i=>pop($('b'+i),t,V(1,[32.34,34.58,35.44,36.28][i])-.1,.3,30,.03));}
  else if(t<47.5){pop($('s5c'),t,V(1,36.95),.4,0,.5);ST.forEach((s,i)=>{const a=V(1,37.3)+i*.38;pop($('sa'+i),t,a,.3,20,.3);$('ml'+i).style.strokeDashoffset=900*(1-eout(cl((t-a)/.5)));$('ml'+i).style.stroke=t>V(1,39.2)+i*.2?'#FFA500':'#007BFF';});}
  else if(t<V(2,47.9)){[0,1,2].forEach(i=>pop($('c'+i),t,V(2,[44.2,45.74,46.56][i]),.3,30,.03));pop($('c3'),t,V(2,47.2),.3,10);}
  else if(t<V(2,57.9)){pop($('s7a'),t,V(2,47.95),.35,20);pop($('s7b'),t,V(2,50.86),.3,20);slam($('s7c'),t,V(2,51.14));pop($('s7d'),t,V(2,51.66),.3,20);[0,1,2].forEach(i=>pop($('o'+i),t,V(2,[52.84,53.82,54.98][i]),.3,20));pop($('o3'),t,V(2,56.3),.35,20,.3);}
  else {slam($('s8a'),t,V(2,57.9));pop($('s8b'),t,V(2,58.3),.35,20);pop($('s8p'),t,V(2,58.7),.4,0,.3);pop($('s8c'),t,V(2,60.16),.4,20);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
