const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const A=[0,24.85,32.95,41.6,49.68], P=[0.6,26.65,43.75,56.4];
const V=(i,w)=>P[i]+(w-A[i]);
const DUR=68;
const SC=[['s0',0,V(0,4.56)],['s1',V(0,4.56),V(0,8.66)],['s2',V(0,8.66),V(0,13.0)],['s3',V(0,13.0),V(0,21.48)],['s4',V(0,21.48),26.65],['s5',26.65,34.75],['s6',34.75,43.75],['s7',43.75,V(2,39.32)],['s8',V(2,39.32),V(3,41.76)],['s9',V(3,41.76),V(3,46.7)],['s10',V(3,46.7),DUR]];
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
function lines(el,arr,t,a,lps){const n=Math.max(0,Math.floor((t-a)*lps)+(t>=a?1:0));el.innerHTML=arr.slice(0,n).join('\n');}
const FAM=['Pages','Charte graphique','Navbar','Diaporamas','Agenda','Semaine','Formulaires','Réservations','Demandes','Contacts','Avis','Photos','Mur social','Commandes','Réglages','Connecteurs','Connexions MCP','Projets'];
$('s4f').innerHTML=FAM.map((f,i)=>`<div class="gp" id="fm${i}" style="left:${60+(i%3)*330}px;top:${880+Math.floor(i/3)*95}px;width:310px;text-align:center;font-size:25px">${f}</div>`).join('');
const RQ=[['« Change le titre de ma page d\'accueil »','modifier_page_site',V(1,29.14)],['« Ajoute un événement à mon agenda »','ajouter_evenement',V(1,30.12)],['« Ajoute une question au formulaire mariage »','configurer_champs_formulaire',V(1,31.12)],['« Prépare une page pour les séminaires »','ajouter_page_site',V(1,31.5)],['« Montre-moi les demandes de la semaine »','voir_demandes',V(1,32.48)],['« Change la couleur de mes boutons »','modifier_charte_graphique',V(1,32.9)],['« Prépare un article sur la soirée »','pas de blog → page éditoriale',V(1,33.3)]];
$('s5r').innerHTML=RQ.map(([q,c],i)=>`<div class="rq" id="rq${i}" style="top:${260+i*150}px"><div class="q">${q}</div><code class="${c.startsWith('pas')?'no':''}">${c}</code></div>`).join('');
const L6=['<span class="g">voir_evenements</span>(depuis: "2026-10-30")','<span class="g">ajouter_evenement</span>(titre: "Soirée du vendredi",','    starts_at: "2026-10-30T20:00+01:00")  <span class="o">→ désactivé par défaut</span>','<span class="g">ajouter_formulaire</span>(nom: "Réservation soirée")  <span class="o">→ désactivé</span>','<span class="g">configurer_champs_formulaire</span>(ajouter: couverts, heure)','<span class="g">configurer_enregistrement_formulaire</span>(couverts, heure)','<span class="g">modifier_evenement</span>(cta_url: lien du formulaire)','<span class="m">modifier_evenement(is_published: true) → après accord</span>'];
const FL=['VISITEUR','FORMULAIRE','DEMANDE','QUALIFICATION','SUIVI','RÉSERVATION OU DEVIS'];
$('s8f').innerHTML=FL.map((f,i)=>`<div class="flow" id="fl${i}" style="top:${240+i*125}px;${i==5?'background:var(--gold);color:#15130F;border-color:var(--gold)':''}">${f}</div>`).join('');
const PG=['Anniversaire','Mariage','Entreprises','Formations & salles','Restaurant','Soirées'];
$('s8p').innerHTML=PG.map((p,i)=>`<div class="gp" id="pg${i}" style="left:${60+(i%3)*330}px;top:${1020+Math.floor(i/3)*90}px;width:310px;text-align:center;font-size:24px">${p}</div>`).join('');
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=V(0,8.66)&&t<V(3,46.7))?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.2):cl((t-a)/.22),fo=id==='s10'?1:1-cl((t-(b-.18))/.18);el.style.opacity=Math.min(fi,fo);}}
  if(t<V(0,4.56)){slam($('s0t'),t,.2);pop($('s0p'),t,.6,.5,120);pop($('s0c'),t,2.0,.35,20,.3);pop($('s0o'),t,2.4,.35,20,.3);}
  else if(t<V(0,8.66)){const t0=V(0,4.56);$('s1f').src='a/ter/'+String(Math.min(152,1+Math.floor((t-t0)*15)+20)).padStart(4,'0')+'.jpg';pop($('s1l'),t,t0+.2,.5,0,.4);slam($('s1t'),t,V(0,4.9));pop($('s1s'),t,V(0,5.9),.4,20);pop($('s1r'),t,t0+1,.4,10);}
  else if(t<V(0,13.0)){pop($('s2t'),t,V(0,8.7),.4,60);pop($('s2l'),t,V(0,9.6),.35,20,.3);pop($('s2s'),t,V(0,10.4),.35,20);}
  else if(t<V(0,21.48)){pop($('c0'),t,V(0,14.24),.35,30,.03);pop($('s3p'),t,V(0,14.4),.4,80);pop($('c1'),t,V(0,16.12),.35,30,.03);pop($('c2'),t,V(0,17.32),.35,30,.03);}
  else if(t<26.65){pop($('s4l'),t,V(0,21.6),.4,0,.5);slam($('s4a'),t,V(0,22.82));FAM.forEach((f,i)=>pop($('fm'+i),t,V(0,23.3)+i*.07,.25,20,.3));}
  else if(t<34.75){RQ.forEach((r,i)=>pop($('rq'+i),t,26.8+i*.95,.3,30,.03));}
  else if(t<43.75){pop($('s6a'),t,34.8,.4,30);pop($('s6t'),t,36.0,.3,30);lines($('s6pre'),L6,t,36.1,2.2);pop($('s6e'),t,39.1,.4,30,.2);pop($('s6p'),t,40.0,.4,40);pop($('s6d'),t,40.6,.3,10);pop($('s6o'),t,41.8,.4,30);}
  else if(t<V(2,39.32)){pop($('p0'),t,V(2,34.6),.35,30,.03);pop($('p1'),t,V(2,35.92),.35,30,.03);pop($('p2'),t,V(2,37.32),.35,30,.03);pop($('p3'),t,V(2,38.6),.35,30,.03);}
  else if(t<V(3,41.76)){const a=V(2,39.32);FL.forEach((f,i)=>pop($('fl'+i),t,a+.1+i*.45,.3,30,.05));PG.forEach((p,i)=>pop($('pg'+i),t,a+3+i*.2,.3,20,.3));}
  else if(t<V(3,46.7)){pop($('s9a'),t,V(3,41.8),.35,20);slam($('s9b'),t,V(3,44.44));}
  else {pop($('s10p'),t,V(3,46.7),.4,0,.3);slam($('s10a'),t,V(3,47.9));pop($('s10l'),t,V(3,49.2),.4,20);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
