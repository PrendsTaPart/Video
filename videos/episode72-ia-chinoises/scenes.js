// Épisode 72 — La Chine rattrape les géants américains de l'IA (inspiré « La Chine est en train d'écraser… »)
const {t0,t1,w,h}=J;
J.init({episode:72,keyword:'CHINE',duoLogo:'claude',stepLabel:'NUMÉRO',
  theme:{vars:{bg:'#0d0d0f',bg2:'#050506',bgc:'#1f1f24',surf:'#18181c',line:'#2d2d33',text:'#F5F5F5',mute:'#9a9aa3',accent:'#E53935',accent2:'#FFC107',hlbg:'#F5F5F5',hlfg:'#0d0d0f'}},
  kw:['Chine','gratuits.','DeepSeek.','Qwen,','Wan,','GLM,','Kimi.','Mistral,','données','Claude','CHINE'],red:['rattraper']});
J.progress(5);
const nm=(t,sz=56,bg='#E53935')=>`<span style="display:inline-block;background:${bg};color:#fff;font-weight:900;font-size:${sz}px;padding:12px 26px;border-radius:16px;white-space:nowrap">${t}</span>`;
const NAMES=['DeepSeek','Qwen','Wan','GLM','Kimi'];
const LG={DeepSeek:'deepseek',Qwen:'qwen',Wan:'wan',GLM:'zhipu',Kimi:'kimi'};
const lg=(n,hh)=>h.logo(LG[n],hh);
document.head.insertAdjacentHTML('beforeend','<style>.hook .hookt{font-size:86px}</style>');
// Accroche : les géants américains contre les outils chinois
let s=J.hook(0,t0(1),{line:0,hl:['Chine'],y:260,w:980});
s.add('<div style="display:flex;gap:20px;justify-content:center">'+h.logo('openai',50)+h.logo('claude',50)+'</div>',{center:true,y:1010,at:w(0,'géants'),an:'left'});
s.add('<div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap">'+NAMES.map(n=>lg(n,38)).join('')+'</div>',{center:true,y:1120,at:w(0,'rattraper'),an:'right'});
s.add('<div class="sticker" style="font-size:70px;background:#FFC107">GRATUIT</div>',{x:700,w:0,y:860,at:w(0,'gratuits'),an:'stamp'});
// Les cinq à connaître
s=J.scene(t0(1),t0(2));
s.text('Les <span class="acc">5</span> à connaître',{y:300,at:t0(1),css:{fontSize:'84px'}});
NAMES.forEach((n,i)=>s.add(`<div>${lg(n,62)}</div>`,{x:540,w:0,y:450+i*120,at:t0(1)+.15*i,an:'pop',css:{transform:'translateX(-50%)'}}));
// Les cinq outils
const S=[[2,3,'DeepSeek',''],[4,5,'Qwen','d\'Alibaba'],[6,7,'Wan','chez Alibaba'],[8,9,'GLM','de Zhipu'],[10,11,'Kimi','']];
const ends=[t0(4),t0(6),t0(8),t0(10),t0(12)];
S.forEach(([a,b,ti,hl],k)=>{const s=J.step(J.scene(t0(a),ends[k]),k+1,ti,hl);
  const win=s.add(`<div class="win" style="min-height:640px"><div class="wtop"><s style="background:#ff5f57"></s><s style="background:#febc2e"></s><s style="background:#28c840"></s><span class="wlab">${ti.toUpperCase()}</span><span style="margin-left:auto">${lg(ti,40)}</span></div><div class="wz" style="position:relative;height:560px"></div></div>`,{x:540,w:900,y:310,at:t0(a)+.1,an:'up'});
  const add=(html,o)=>s.add(html,Object.assign({an:'pop'},o));
  if(k===0){add(h.chip('GRATUIT','a'),{x:330,w:0,y:450,at:w(b,'gratuit'),css:{transform:'translateX(-50%)'}});add(h.chip('OUVERT À TOUS','b'),{x:740,w:0,y:450,at:w(b,'ouvert'),css:{transform:'translateX(-50%)'}});
    add(`<div class="tx" style="font-size:48px;text-align:center">a fait trembler<br><span class="hl">la Silicon Valley</span></div>`,{center:true,y:620,at:w(b,'trembler'),an:'up'});}
  if(k===1){[['💬','Discuter','discute'],['🖼️','Images','images'],['🌐','Sites','sites']].forEach(([i,x,kk],j)=>add(`<div class="tile" style="width:240px;height:240px;font-size:34px"><div style="font-size:90px">${i}</div>${x}</div>`,{x:250+j*290,w:240,y:480,at:w(b,kk)}));}
  if(k===2){add(`<div class="tile" style="width:260px;height:200px;font-size:40px">Une phrase</div>`,{x:300,w:260,y:520,at:w(b,'phrase')});
    add(`<div style="font-size:90px;font-weight:900;color:#E53935">→</div>`,{x:540,w:0,y:560,at:w(b,'phrase')+.3,css:{transform:'translateX(-50%)'}});
    add(`<div class="tile" style="width:260px;height:200px;font-size:40px;border-color:#E53935"><div style="font-size:70px">▶</div>Une vidéo</div>`,{x:780,w:260,y:520,at:w(b,'vidéo')});}
  if(k===3){J.bars(s,[{l:'Modèle A',v:7,c:'#3a3a42',at:t0(b),fmt:()=>''},{l:'Modèle B',v:8,c:'#3a3a42',at:t0(b)+.15,fmt:()=>''},{l:'GLM',v:8.6,c:'#E53935',at:w(b,'mesure'),fmt:()=>''}],{y:430,h:380,bw:180,gap:70,max:10});
    s.text('<span class="mute" style="font-size:24px">illustration, pas un vrai score</span>',{y:930,at:w(b,'tests')});}
  if(k===4){[...Array(10)].forEach((_,i)=>add(`<div style="font-size:70px">📄</div>`,{x:200+(i%5)*170,w:0,y:450+Math.floor(i/5)*130,at:w(b,'documents')+i*.05,css:{transform:'translateX(-50%)'}}));
    add(h.chip('d\'un seul coup','f'),{x:540,w:0,y:760,at:w(b,'coup'),css:{transform:'translateX(-50%)'}});}
});
// Et l'Europe ? Mistral
s=J.scene(t0(12),t0(13));
s.text('Et l\'Europe ?',{y:280,at:t0(12),css:{fontSize:'90px'}});
s.add(h.logo('mistral',260),{x:540,w:0,y:480,at:w(12,'mistral'),an:'pop',css:{transform:'translateX(-50%)'}});
s.add('<div class="sticker" style="font-size:44px;background:#1f5bd8;color:#fff">🇫🇷 EN FRANCE</div>',{x:540,w:0,y:840,at:w(12,'france'),an:'pop',css:{transform:'translateX(-50%)'}});
// Attention aux données des clients
s=J.scene(t0(13),t0(14));
s.add('<div style="font-size:150px;text-align:center">🔒</div>',{center:true,y:230,at:t0(13),an:'pop'});
s.add(`<div class="card" style="border:4px solid #FFC107;text-align:center"><div style="font-size:30px;font-weight:900;color:#FFC107;letter-spacing:2px">POUR TON RESTO</div><div style="font-size:44px;font-weight:800;margin-top:10px">Les données de tes clients :<br>vérifie où elles partent</div></div>`,{x:540,w:880,y:480,at:w(13,'données'),an:'zoom'});
// Je reste sur Claude, je teste tout
s=J.scene(t0(14),t0(15));
s.add(h.logo('claude',100),{x:540,w:0,y:300,at:w(14,'claude'),an:'pop',css:{transform:'translateX(-50%)'}});
s.text('pour ce qui compte',{y:470,at:w(14,'compte'),css:{fontSize:'54px'}});
s.add('<div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">'+NAMES.map(n=>lg(n,34)).join('')+'</div>',{center:true,y:700,at:w(14,'teste'),an:'up'});
s.text('<span class="mute" style="font-size:40px">je les teste tous</span>',{y:880,at:w(14,'teste'),an:'up'});
// Fin
J.cta(t0(15),{guideTitle:'La liste complète',items:['DeepSeek','Qwen (Alibaba)','Wan (Alibaba)','GLM (Zhipu)','Kimi','+ Mistral, en France']});
J.cfg.thumbAt=t0(1)+.9;
