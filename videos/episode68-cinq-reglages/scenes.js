// Épisode 68 — Tu utilises Claude à moitié : les cinq réglages (inspiré « 5 réglages de Claude »)
const {t0,t1,w,h}=J;
J.init({episode:68,keyword:'CONFIG',duoLogo:'claude',stepLabel:'RÉGLAGE',
  theme:{cls:'typo',vars:{bg:'#0e0f12',bg2:'#08090b',bgc:'#1a1c22',surf:'#17191e',line:'#2a2d35',text:'#F4F4F4',mute:'#9aa0ab',accent:'#FFB020',accent2:'#3FD07A',hlbg:'#FFB020',hlfg:'#111',capfont:"'Anton'"}},
  kw:['moitié.','cinq','projets.','compétences.','artefacts.','connecteurs.','navigateur.','employé','maison.','CONFIG'],red:['sautent']});
document.head.insertAdjacentHTML('beforeend','<style>#cap{font-family:Anton;font-weight:400;text-transform:uppercase;letter-spacing:1px}.tg{display:inline-block;width:86px;height:46px;border-radius:23px;background:#2a2d35;position:relative;vertical-align:middle}.tg i{position:absolute;top:5px;left:5px;width:36px;height:36px;border-radius:50%;background:#9aa0ab;transition:none}.tg.on{background:#3FD07A}.tg.on i{left:45px;background:#fff}.pan{background:#17191e;border:2px solid #2a2d35;border-radius:24px;padding:24px 30px}.pr{display:flex;justify-content:space-between;align-items:center;font-family:Anton;font-size:42px;text-transform:uppercase;padding:12px 0;border-bottom:2px solid #2a2d35}</style>');
J.progress(5);
const R=['Projets','Compétences','Artefacts','Connecteurs','Navigateur'];
// Accroche + jauge à moitié
let s=J.hook(0,t0(1),{line:0,hl:['moitié.'],y:330});
s.add('<div class="pan"><div style="font-family:Anton;font-size:34px;color:#9aa0ab">CLAUDE UTILISÉ</div><div style="height:40px;background:#2a2d35;border-radius:20px;margin-top:14px;overflow:hidden"><div class="gg" style="height:100%;width:0;background:#FFB020"></div></div></div>',{x:540,w:820,y:720,at:.5,an:'up'});
s.on(t=>{const g=document.querySelector('.gg');if(g)g.style.width=(50*J.ease((t-.6)/1))+'%';});
// Le panneau des cinq réglages, un sauté
s=J.scene(t0(1),t0(2));
s.text('IL Y A <span class="acc">5 RÉGLAGES</span>',{y:230,at:t0(1),css:{fontSize:'84px'}});
const pan=s.add(`<div class="pan">${R.map((r,i)=>`<div class="pr"><span>${r}</span>${i===3?'<span style="background:#d93025;color:#fff;font-size:28px;padding:4px 12px;border-radius:8px">SAUTÉ</span>':`<span class="tg t${i}"><i></i></span>`}</div>`).join('')}</div>`,{x:540,w:820,y:400,at:w(1,'cinq'),an:'up'});
s.on(t=>R.forEach((_,i)=>{const e=pan.querySelector('.t'+i);if(e)e.classList.toggle('on',t>w(1,'cinq')+.4+i*.2);}));
// Les cinq réglages
const C=[[2,3,'Les','projets'],[4,5,'Les','compétences'],[6,7,'Les','artefacts'],[8,9,'Les','connecteurs'],[10,11,'Claude dans','ton navigateur']];
const ends=[t0(4),t0(6),t0(8),t0(10),t0(12)];
C.forEach(([a,b,ti,hl],k)=>{const s=J.step(J.scene(t0(a),ends[k]),k+1,ti,hl);
  if(k===0){s.add(`<div class="pan"><div style="font-family:Anton;font-size:40px">PROJET · MON RESTO</div>${['Ta carte','Tes horaires','Ta façon de parler'].map((x,i)=>`<div class="row" style="background:#0e0f12;margin-top:14px">📌 ${x}</div>`).join('')}</div>`,{x:540,w:820,y:330,at:w(b,'carte')-.3,an:'up'});
    s.add(`<div class="kwbox" style="font-family:Anton;font-weight:400;font-size:52px">IL S'EN SOUVIENT</div>`,{center:true,y:930,at:w(b,'souvient'),an:'slam'});}
  if(k===1){[0,1,2].forEach(i=>s.add(`<div class="pan" style="width:280px"><div style="font-family:Anton;font-size:30px;color:#FFB020">FICHE RECETTE</div><div style="height:12px;background:#2a2d35;border-radius:6px;margin-top:14px"></div><div style="height:12px;width:70%;background:#2a2d35;border-radius:6px;margin-top:10px"></div><div style="height:12px;width:85%;background:#2a2d35;border-radius:6px;margin-top:10px"></div></div>`,{x:220+i*320,w:280,y:400,at:w(b,'refait')+i*.2,an:'pop'}));
    s.add(`<div class="kwbox" style="font-family:Anton;font-weight:400;font-size:52px">PAREIL À CHAQUE FOIS</div>`,{center:true,y:780,at:w(b,'pareil'),an:'slam'});}
  if(k===2){s.add(`<div class="pan" style="text-align:center;opacity:.6"><div style="font-family:Anton;font-size:40px;text-decoration:line-through">DU TEXTE</div></div>`,{x:290,w:420,y:330,at:w(b,'texte'),an:'left'});
    s.add(`<div class="pan" style="text-align:center;border-color:#3FD07A"><div style="font-family:Anton;font-size:40px;color:#3FD07A">UN VRAI OUTIL</div></div>`,{x:790,w:420,y:330,at:w(b,'outil'),an:'right'});
    [['🧮','Calculateur de prix','calculateur'],['🗓️','Planning','planning'],['🖼️','Affiche','affiche']].forEach(([i,x,kk],j)=>s.add(`<div class="row" style="font-family:Anton;font-weight:400;text-transform:uppercase;font-size:40px">${i} ${x}</div>`,{x:540,w:760,y:540+j*130,at:w(b,kk),an:'up'}));}
  if(k===3){s.add(`<div class="pan"><div style="display:flex;justify-content:space-between;font-family:Anton;font-size:32px;color:#9aa0ab"><span>CONNECTEURS</span><span class="cc" style="color:#3FD07A"></span></div>${['Messagerie','Agenda','FoodEatUp'].map((x,i)=>`<div class="pr"><span>${x}</span><span class="tg c${i}"><i></i></span></div>`).join('')}</div>`,{x:540,w:820,y:330,at:t0(b)-.2,an:'up'});
    s.on(t=>{let n=0;['messagerie','agenda','foodeatup'].forEach((kk,i)=>{const on=t>w(b,kk);if(on)n++;const e=document.querySelector('.c'+i);if(e)e.classList.toggle('on',on);});const c=document.querySelector('.cc');if(c)c.textContent=n+'/3 BRANCHÉS';});
    s.add(h.logo('foodeatup',56),{x:540,w:0,y:830,at:w(b,'foodeatup'),an:'pop',css:{transform:'translateX(-50%)'}});
    s.add(`<div class="row" style="justify-content:center">📅 Il lit tes réservations</div>`,{x:540,w:760,y:960,at:w(b,'lit'),an:'up'});}
  if(k===4){s.add(`<div class="win" style="min-height:560px"><div class="wtop"><s style="background:#ff5f57"></s><s style="background:#febc2e"></s><s style="background:#28c840"></s><span class="wlab">CLAUDE · DANS LE NAVIGATEUR</span></div><div style="padding:30px">${['Nom du fournisseur','Quantité','Date de livraison'].map((x,i)=>`<div style="font-size:26px;color:#9aa0ab;margin-top:${i?18:0}px">${x}</div><div style="height:64px;border:2px solid #2a2d35;border-radius:14px;margin-top:8px;font-size:32px;padding:12px 16px" class="f${i}"></div>`).join('')}</div></div>`,{x:540,w:880,y:320,at:t0(b)-.3,an:'up'});
    const vals=['Les Halles de Rungis','12 caisses','Jeudi 8 h'];
    s.on(t=>vals.forEach((v,i)=>{const e=document.querySelector('.f'+i);if(!e)return;const q=J.clamp((t-w(b,'remplit')-i*.5)/.6);e.textContent=v.slice(0,Math.round(v.length*q));e.style.borderColor=q>0&&q<1?'#FFB020':'#2a2d35';}));
    s.text('<span class="mute" style="font-size:24px;font-family:Poppins">exemple de formulaire</span>',{y:930,at:w(b,'clique')});}
});
// Un employé qui connaît ta maison (badge)
s=J.scene(t0(12),t0(13));
s.text('<span style="text-decoration:line-through;color:#6b7180">UNE SIMPLE DISCUSSION</span>',{y:240,at:w(12,'discussion'),css:{fontSize:'64px'}});
s.add(`<div class="pan" style="text-align:left;border-color:#FFB020"><div style="font-family:Anton;font-size:28px;color:#9aa0ab">BADGE · NOUVEL EMPLOYÉ</div><div style="display:flex;gap:26px;align-items:center;margin-top:16px"><div style="width:150px;height:150px;border-radius:20px;background:#fff;display:flex;align-items:center;justify-content:center"><img src="../_journal-63-72/commun/logo-claude.webp" style="width:130px"></div><div><div style="font-family:Anton;font-size:64px">CLAUDE</div><div style="font-size:30px;color:#9aa0ab">Connaît ta maison</div></div></div></div>`,{x:540,w:800,y:420,at:w(12,'employé')-.2,an:'zoom'});
// Fin
J.cta(t0(13),{guideTitle:'Le pas à pas',items:['Créer ton projet','Apprendre une compétence','Demander un artefact','Brancher tes connecteurs','Claude dans ton navigateur']});
J.cfg.thumbAt=w(1,'cinq')+1.6;
