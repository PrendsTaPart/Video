// Épisode 64 — Je t'apprends à réfléchir comme un pro, en cinq phrases (inspiré « Une idée de projet ? 5 phrases à Claude »)
const {t0,t1,w,h}=J;
J.init({episode:64,keyword:'PHRASES',duoLogo:'claude',stepLabel:'PHRASE',
  theme:{cls:'clair',vars:{bg:'#FFFFFF',bg2:'#F3F1EE',bgc:'#FFFFFF',surf:'#1B1B1B',line:'#2c2c2c',text:'#141414',mute:'#7c7c7c',accent:'#E07A4F',accent2:'#141414',hlbg:'#141414',hlfg:'#FFFFFF'}},
  kw:['pro,','cinq','simples.','dix','risques','opposé','pourquoi.','questions.','PHRASES'],red:['rate']});
J.progress(5);
// grande étoile orange de Claude dans le coin (décor)
J.fx.push(t=>{});
const star=(s,x,y,sz,at)=>s.add(`<div style="width:${sz}px;height:${sz}px;background:conic-gradient(from 0deg,#E07A4F 0 8%,transparent 8% 12.5%,#E07A4F 12.5% 20.5%,transparent 20.5% 25%,#E07A4F 25% 33%,transparent 33% 37.5%,#E07A4F 37.5% 45.5%,transparent 45.5% 50%,#E07A4F 50% 58%,transparent 58% 62.5%,#E07A4F 62.5% 70.5%,transparent 70.5% 75%,#E07A4F 75% 83%,transparent 83% 87.5%,#E07A4F 87.5% 95.5%,transparent 95.5%);border-radius:50%;-webkit-mask:radial-gradient(circle,transparent 18%,#000 19%)"></div>`,{x,w:sz,y,at,an:'pop',css:{}});
let s=J.hook(0,t0(1),{line:0,hl:['pro,'],y:420,sticker:'JE T\'APPRENDS'});
star(s,900,1180,360,.2);
s.on(t=>{s.items[s.items.length-1].e.style.transform+=` rotate(${t*20}deg)`;});
// Contexte : trois projets, avant de dépenser
s=J.scene(t0(1),t0(2));
['Un nouveau plat','La livraison','Un deuxième resto'].forEach((x,i)=>s.add(`<div class="card" style="background:#fff;border:3px solid #141414;color:#141414;text-align:center;font-size:44px;font-weight:800">${x}</div>`,{x:540+(i-1)*40,w:700,y:300+i*170,at:[w(1,'nouveau'),w(1,'livraison'),w(1,'deuxième')][i],an:i%2?'right':'left'}));
s.add(`<div class="kwbox" style="font-size:52px">Avant de dépenser 1 €</div>`,{center:true,y:860,at:w(1,'avant'),an:'slam'});
J.logoArc(s,['claude'],{y:1180,at:w(1,'claude'),h:64});
// Les cinq phrases
const P=[[2,3,'Comprendre',''],[4,5,'Explorer',''],[6,7,'Anticiper',''],[8,9,'Se faire','contredire'],[10,11,'Apprendre','d\'un échec']];
const ends=[t0(4),t0(6),t0(8),t0(10),t0(12)];
P.forEach(([q,r,ti,hl],k)=>{
  const s=J.step(J.scene(t0(q),ends[k]),k+1,ti,hl);
  const z=J.window(s,q,{y:300,skip:1,label:'MESSAGE'});
  const at=t0(r);
  if(k===0){['A','B','C'].forEach((c,i)=>J.inzone(s,z,`<div class="tile" style="width:150px;height:150px;font-size:80px;color:${i==1?'#fff':'#141414'};background:${i==1?'#E07A4F':'#fff'};border-color:#fff">${c}</div>`,{at:at+i*.15,css:{left:(i*175)+'px',top:'10px'}}));
    J.inzone(s,z,'<div style="font-size:34px;font-weight:700;color:#fff">Enfin clair.</div>',{at:at+.6,css:{left:'560px',top:'60px'}});}
  if(k===1){[...Array(10)].forEach((_,i)=>J.inzone(s,z,`<div class="tile" style="width:150px;height:120px;font-size:46px;background:${i==6?'#E07A4F':'#fff'};color:${i==6?'#fff':'#141414'};border-color:#fff">${i+1}</div>`,{at:w(5,'dix')+i*.07,css:{left:((i%5)*172)+'px',top:(i<5?0:140)+'px'}}));
    J.inzone(s,z,h.chip('C\'est toi qui choisis','f'),{at:w(5,'toi'),css:{left:'230px',top:'290px'}});}
  if(k===2){['Le loyer du local de livraison','La saison : moins de monde l\'été','Le temps de préparation au coup de feu'].forEach((x,i)=>J.inzone(s,z,`<div class="row" style="background:#fff;color:#141414;border-color:#fff;font-size:30px"><span style="color:#E07A4F;font-size:40px">⚠</span>${x}</div>`,{at:at+i*.35,an:'up',css:{left:'0',right:'0',top:(i*104)+'px'}}));}
  if(k===3){J.inzone(s,z,`<div class="tile" style="width:400px;height:260px;background:#fff;color:#141414;font-size:40px;border-color:#fff">Ton avis</div>`,{at:at,css:{left:'0',top:'0'}});
    J.inzone(s,z,`<div style="font-size:50px;font-weight:900;color:#fff">VS</div>`,{at:at+.2,css:{left:'418px',top:'100px'}});
    J.inzone(s,z,`<div class="tile" style="width:400px;height:260px;background:#E07A4F;color:#fff;font-size:40px;border-color:#E07A4F">L'inverse</div>`,{at:at+.4,css:{left:'504px',top:'0'}});}
  if(k===4){J.inzone(s,z,`<div class="tile" style="width:430px;height:220px;background:#fff;color:#141414;font-size:44px;border-color:#fff">Quoi ?</div>`,{at:w(10,'analyse'),css:{left:'0',top:'0'}});
    J.inzone(s,z,`<div class="tile" style="width:430px;height:220px;background:#E07A4F;color:#fff;font-size:44px;border-color:#E07A4F">Pourquoi ?</div>`,{at:w(10,'pourquoi'),css:{left:'474px',top:'0'}});
    J.inzone(s,z,h.chip('La prochaine fois, tu sais','f'),{at:at,css:{left:'190px',top:'250px'}});}
});
// Pas de formule magique
s=J.scene(t0(12),t0(13));
s.text('<span style="text-decoration:line-through;color:#bbb">Formules magiques</span>',{y:380,at:t0(12),css:{fontSize:'86px'}});
s.text('Juste les bonnes<br><span class="hl">questions</span>',{y:620,at:w(12,'juste'),an:'slam',css:{fontSize:'110px'}});
star(s,540,960,240,w(12,'questions'));
// Fin
J.cta(t0(13),{guideTitle:'Les 5 phrases',items:['Explique-moi avec des mots simples','Donne-moi dix versions','Quels risques cachés ?','Défends le point de vue opposé','Analyse ce qui n\'a pas marché']});
J.cfg.thumbAt=w(5,'toi');
