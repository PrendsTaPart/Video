/* Moteur de motion design du journal « Mon quotidien d'entrepreneur avec l'IA » (épisodes 63-72).
   Chaque épisode : index.html charge cfg.js (mots calés sur la voix), ce fichier, puis scenes.js.
   Tout est fonction du temps t : render(t) est appelé image par image par _moteur/render.js. */
(function(){
const $=s=>document.querySelector(s);
const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)), ease=x=>1-Math.pow(1-clamp(x),3), back=x=>{x=clamp(x);const c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2);};
const rnd=s=>{const x=Math.sin(s*12.9898)*43758.5453;return x-Math.floor(x);};
const C=window.CFG, L=C.lines, W=C.words;
const C0='../_journal-63-72/commun/';
const LOGOS={claude:'logo-claude.webp',openai:'logo-openai.webp',mistral:'logo-mistral.webp',lovable:'logo-lovable.webp',rapidocms:'logo-rapidocms.webp',rapidocrm:'logo-rapidocrm.webp',rapidorh:'logo-rapidorh.webp',planit:'logo-planit.webp',braindcode:'logo-braindcode.webp',foodeatup:'logo-foodeatup.webp',rapidosoftware:'logo-rapidosoftware.png'};
const J={clamp,ease,back,rnd,scenes:[],fx:[],kw:new Set(),red:new Set(),steps:[],cfg:{}};
J.t0=i=>L[i].t0; J.t1=i=>L[i].t1;
// temps du premier mot de la ligne qui commence par « mot » (insensible à la casse et à la ponctuation)
const nrm=s=>s.toLowerCase().replace(/[^a-z0-9àâäéèêëîïôöùûüç']/g,'');
J.w=(line,word,nth=0)=>{const ws=W.filter(w=>w[2]===line);const m=ws.filter(w=>nrm(w[0]).startsWith(nrm(word)));return (m[nth]||m[0]||ws[0])[1];};
J.logoSrc=n=>C0+(LOGOS[n]||n);
J.kit=n=>'../kit/'+n;            // images du kit (copiées dans videos/kit)
J.h={ // petits gabarits HTML
  chip:(t,c='')=>`<div class="chip ${c}">${t}</div>`,
  logo:(n,h=60)=>`<span class="lpill"><img src="${J.logoSrc(n)}" style="height:${h}px"></span>`,
  num:(n)=>`<div class="numb">${n}</div>`,
  check:(t,ok=true)=>`<div class="row"><span class="${ok?'ok':'ko'}">${ok?'✓':'✗'}</span>${t}</div>`,
};

J.init=function(o){
  J.cfg=o; const th=o.theme, R=document.documentElement.style;
  for(const k in th.vars)R.setProperty('--'+k,th.vars[k]);
  document.body.className=th.cls||'';
  const st=$('#stage');
  st.innerHTML=`<div id="bg"></div><div id="scenes"></div><div id="top"><div id="bar"></div><div id="head"><div class="lab"></div><div class="ttl"><div class="num"></div><div class="txt"></div></div></div></div>
  <div id="cap"></div><div id="duo"><img id="mic" src="${C0}michael-rond.png"><div class="nm">MICHAEL</div><span id="dlogo" class="lpill"><img src="${J.logoSrc(o.duoLogo||'claude')}"></span></div>
  <div id="epi">ÉPISODE ${o.episode}/365</div><div id="flash"></div><div id="grain"></div>`;
  if(th.bgImage)$('#bg').style.backgroundImage=`url(${th.bgImage})`;
  (o.kw||[]).forEach(k=>J.kw.add(nrm(k))); (o.red||[]).forEach(k=>J.red.add(nrm(k)));
};
// une scène = un plein écran entre a et b
J.scene=function(a,b,o={}){const d=document.createElement('div');d.className='sc '+(o.cls||'');
  if(o.bg){const bg=document.createElement('div');bg.className='scbg';bg.style.backgroundImage=`url(${o.bg})`;d.appendChild(bg);o._bg=bg;}
  $('#scenes').appendChild(d);const s={a,b,d,o,items:[],fn:[],head:o.head||null,noDuo:!!o.noDuo,noCap:!!o.noCap};
  s.add=(html,p={})=>{const w=document.createElement('div');w.innerHTML=p.center?'<div>'+html.trim()+'</div>':html.trim();const e=w.firstElementChild;e.classList.add('it');
    const css=Object.assign({},p.css||{});if(p.x!=null){css.left=(p.x-(p.w||0)/2)+'px';}if(p.y!=null)css.top=p.y+'px';if(p.w)css.width=p.w+'px';if(p.z)css.zIndex=p.z;
    if(p.center){css.left='0';css.right='0';css.textAlign='center';}
    Object.assign(e.style,css);d.appendChild(e);s.items.push({e,at:p.at??a,an:p.an||'up',until:p.until,d:p.d||.45,p});return e;};
  s.img=(src,p={})=>s.add(`<img src="${src}" class="${p.cls||''}" style="position:absolute;${p.style||''}">`,p);
  s.text=(html,p={})=>s.add(`<div class="tx ${p.cls||''}">${html}</div>`,Object.assign({center:true},p));
  s.on=f=>{s.fn.push(f);return s;};
  J.scenes.push(s);return s;};
// en-tête numéroté (étape k sur n)
J.step=(s,k,title,hl)=>{s.head={k,title,hl};return s;};
J.progress=n=>{J.cfg.steps=n;$('#bar').innerHTML=Array.from({length:n},()=>'<i><b></b></i>').join('');};
// fenêtre de conversation : la ligne de voix se tape mot à mot
J.window=(s,line,p={})=>{const e=s.add(`<div class="win"><div class="wtop"><s style="background:#ff5f57"></s><s style="background:#febc2e"></s><s style="background:#28c840"></s><span class="wlab">${p.label||'EXEMPLE DE DEMANDE'}</span>${J.h.logo(p.logo||'claude',30)}</div><div class="wask"><span class="wtxt"></span><span class="cur"></span><div class="send">↑</div></div><div class="wzone"></div></div>`,Object.assign({x:540,w:p.w||960,y:p.y||330,an:'up'},p));
  const tx=e.querySelector('.wtxt'),cur=e.querySelector('.cur');
  s.on(t=>{const ws=W.filter(w=>w[2]===line&&w[1]<=t+.05);tx.textContent=(p.prefix||'')+ws.slice(p.skip||0).map(w=>w[0]).join(' ');cur.style.opacity=(Math.floor(t*2.5)%2)?1:0;});
  return e.querySelector('.wzone');};
// éléments dans la fenêtre (zone relative)
J.inzone=(s,zone,html,p={})=>{const w=document.createElement('div');w.innerHTML=html.trim();const e=w.firstElementChild;e.classList.add('it');Object.assign(e.style,{position:'absolute'},p.css||{});zone.appendChild(e);s.items.push({e,at:p.at??s.a,an:p.an||'pop',d:p.d||.35,p});return e;};
// logos qui arrivent en arc (Claude, OpenAI, Mistral…)
J.logoArc=(s,names,p={})=>{const n=names.length,cy=p.y||900,r=p.r||330;names.forEach((nm,i)=>{const ang=Math.PI*(0.15+0.7*(n===1?.5:i/(n-1)));const x=540-Math.cos(ang)*r,y=cy-Math.sin(ang)*r*.55;
  s.add(J.h.logo(nm,p.h||56),{x,y,w:0,at:(p.at??s.a)+i*(p.step||.15),an:'pop',css:{transform:'translate(-50%,-50%)'}});});};
// portrait avec cartouche et crédit (photo Wikimedia, etc.)
J.photo=(s,src,p)=>s.add(`<div class="photo"><img src="${src}"><div class="pname">${p.name}<small>${p.role||''}</small></div>${p.credit?`<div class="pcred">${p.credit}</div>`:''}</div>`,Object.assign({x:540,w:p.w||560,y:p.y||330,an:'zoom'},p));
// barres animées
J.bars=(s,items,p={})=>{const max=p.max||Math.max(...items.map(i=>i.v));const H=p.h||520,bw=p.bw||220,gap=p.gap||80,x0=540-(items.length*bw+(items.length-1)*gap)/2;
  items.forEach((it,i)=>{const e=s.add(`<div class="bar" style="width:${bw}px;height:${H}px"><div class="bfill" style="background:${it.c||'var(--accent)'}"></div><div class="bval"></div><div class="blab">${it.l}</div></div>`,{x:x0+i*(bw+gap)+bw/2,w:bw,y:p.y||520,at:it.at,an:'fade'});
    const f=e.querySelector('.bfill'),v=e.querySelector('.bval');s.on(t=>{const q=ease((t-it.at)/(it.d||.8));const val=(it.v0??0)+(it.v-(it.v0??0))*q;f.style.height=(val/max*100)+'%';v.textContent=(it.fmt||(x=>Math.round(x)))(val);v.style.bottom=(val/max*100)+'%';});});};
J.counter=(s,p)=>{const e=s.add(`<div class="tx counter" style="font-size:${p.size||150}px">${p.fmt(p.from)}</div>`,Object.assign({center:true},p));s.on(t=>{const q=ease((t-p.at)/(p.d||1));e.textContent=p.fmt(p.from+(p.to-p.from)*q);});return e;};
// accroche (hook) : la punchline arrive mot à mot sur la voix
J.hook=(a,b,p)=>{const s=J.scene(a,b,Object.assign({cls:'hook',noCap:true},p.scene||{}));
  const ws=W.filter(w=>w[2]===(p.line??0));
  const html=ws.map((w,i)=>{const k=nrm(w[0]);return `<span class="hw ${J.red.has(k)?'red':''} ${(p.hl||[]).map(nrm).includes(k)?'hl':''}" data-t="${w[1]}">${w[0]}</span>`;}).join(' ');
  const e=s.add(`<div class="hookt">${html}</div>`,{x:540,w:p.w||960,y:p.y||420,an:'none'});
  const spans=[...e.querySelectorAll('.hw')];
  s.on(t=>spans.forEach(sp=>{const d=t-(+sp.dataset.t);sp.style.opacity=d>=0?1:0;sp.style.transform=`translateY(${(1-back(d/.3))*40}px) scale(${d>=0?1+.25*Math.max(0,1-d/.18):1})`;}));
  if(p.sticker)s.add(`<div class="sticker">${p.sticker}</div>`,{x:540,w:0,y:(p.y||420)-110,at:a+.1,an:'pop',css:{transform:'translateX(-50%) rotate(-4deg)'}});
  return s;};
// carte finale : mot-clé + guide + épisode
J.cta=(a,p)=>{const s=J.scene(a,C.dur+1,{cls:'cta',noCap:false});
  s.add(`<div class="guide"><div class="gt">${p.guideTitle||'LE GUIDE'}</div>${(p.items||[]).map((x,i)=>`<div class="gi"><b>${i+1}</b>${x}</div>`).join('')}</div>`,{x:540,w:640,y:250,at:a,an:'drop'});
  s.add(`<div class="kwbox">Écris <b>${J.cfg.keyword}</b><br>en commentaire</div>`,{center:true,y:p.y||880,at:p.kwAt??J.w(L.length-1,'écris'),an:'slam'});
  s.add(`<div class="kwsub">${p.sub||'je t\'envoie le lien de la ressource'}</div>`,{center:true,y:(p.y||880)+215,at:(p.kwAt??J.w(L.length-1,'écris'))+.4,an:'up'});
  return s;};

/* ---------- rendu ---------- */
function anim(it,t){const p=clamp((t-it.at)/it.d);let op=t>=it.at?1:0,tr='';const base=it.p&&it.p.css&&it.p.css.transform||'';
  switch(it.an){case'up':op=p;tr=`translateY(${(1-ease(p))*50}px)`;break;case'fade':op=p;break;case'none':op=1;break;
  case'pop':tr=`scale(${t<it.at?0:back(p)})`;break;case'slam':op=p;tr=`scale(${2.2-1.2*ease(p)})`;break;
  case'drop':op=p;tr=`translateY(${(1-back(p))*-120}px)`;break;case'zoom':op=p;tr=`scale(${.7+.3*back(p)})`;break;
  case'left':op=p;tr=`translateX(${(1-ease(p))*-300}px)`;break;case'right':op=p;tr=`translateX(${(1-ease(p))*300}px)`;break;
  case'stamp':op=p;tr=`scale(${2-ease(p)}) rotate(-8deg)`;break;case'float':op=p;tr=`translateY(${Math.sin(t*2)*12}px)`;break;}
  if(it.until!=null&&t>=it.until)op=0;it.e.style.opacity=op;it.e.style.transform=(base+' '+tr).trim();}
window.render=function(t){
  let cur=null;for(const s of J.scenes){const on=t>=s.a&&t<s.b;s.d.style.visibility=on?'visible':'hidden';if(!on)continue;cur=s;
    if(s.o._bg){const kb=s.o.kb||[1.04,1.12],q=clamp((t-s.a)/(s.b-s.a));s.o._bg.style.transform=`scale(${kb[0]+(kb[1]-kb[0])*q})`;s.o._bg.style.filter=s.o.filter||'';}
    for(const it of s.items)anim(it,t);for(const f of s.fn)f(t);}
  // en-tête d'étape + barre de progression
  const h=cur&&cur.head;$('#top').style.visibility=h?'visible':'hidden';
  if(h){$('#head .lab').textContent=(J.cfg.stepLabel||'NUMÉRO')+' '+h.k;$('#head .num').textContent=h.k;$('#head .txt').innerHTML=`${h.title} ${h.hl?`<span class="hl">${h.hl}</span>`:''}`;
    const p=ease((t-cur.a)/.4);$('#head').style.opacity=p;$('#head').style.transform=`translateX(${(1-p)*-50}px)`;
    [...document.querySelectorAll('#bar b')].forEach((b,i)=>{b.style.transform=`scaleX(${i<h.k-1?1:i>h.k-1?0:clamp((t-cur.a)/(cur.b-cur.a))})`;});}
  // sous-titres mot à mot
  let li=-1;for(let i=0;i<L.length;i++)if(t>=L[i].t0-.05&&t<=L[i].t1+.25)li=i;
  if(li>=0&&!(cur&&cur.noCap)){const ws=W.filter(w=>w[2]===li);let c=0;ws.forEach((w,i)=>{if(t>=w[1])c=i;});const g0=Math.floor(c/4)*4;
    $('#cap').innerHTML=ws.slice(g0,g0+4).map((w,i)=>{const k=nrm(w[0]);return `<span class="${t>=w[1]?'on':''} ${g0+i===c?'now':''} ${J.kw.has(k)?'k':''} ${J.red.has(k)?'r':''}">${w[0]}</span>`;}).join(' ');}
  else $('#cap').innerHTML='';
  // duo Michael + logo, flottement
  $('#duo').style.visibility=cur&&cur.noDuo?'hidden':'visible';
  $('#mic').style.transform=`translateY(${Math.sin(t*2)*6}px)`;$('#dlogo').style.transform=`translateY(${Math.sin(t*2+1.5)*6}px)`;
  $('#epi').style.opacity=t>C.dur-3?1:0;
  // éclair blanc léger à chaque changement de scène
  let f=0;for(const s of J.scenes){const d=t-s.a;if(s.a>0&&d>=0&&d<.18)f=Math.max(f,(J.cfg.flash??.22)*(1-d/.18));}$('#flash').style.opacity=f;
  $('#grain').style.backgroundPosition=`${(rnd(Math.floor(t*24))*200)|0}px ${(rnd(Math.floor(t*24)+3)*200)|0}px`;
  for(const f2 of J.fx)f2(t);
};
window.thumb=function(){render(J.cfg.thumbAt??(J.t0(2)+.8));};
window.J=J;
})();
