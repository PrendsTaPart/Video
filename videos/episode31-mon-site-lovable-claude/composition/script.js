const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const eio=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
const A=[0,8.15,18.55,28.55,39.4,52.4,62.0,74.1,80.35,86.05], P=[0.5,10.15,21.55,33.05,45.4,59.9,71.5,85.1,92.35];
const V=(i,w)=>P[i]+(w-A[i]);
const DUR=101;
const SC=[['s0',0,10.15],['s1',10.15,21.55],['s2',21.55,33.05],['s3',33.05,45.4],['s4',45.4,V(4,47.58)],['s5',V(4,47.58),59.9],['s6',59.9,71.5],['s7',71.5,85.1],['s8',85.1,92.35],['s9',92.35,DUR]];
function pop(el,t,a,d=.4,dy=40,sc=0){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`scale(${s})`;}
function scrollImg(img,t,a,b,max){img.style.transform=`translateY(${-max*eio(cl((t-a)/(b-a)))}px)`;}
// les 37 outils réels de src/lib/mcp/tools
const TOOLS='archiver-formation archiver-lead-magnet archiver-offre archiver-projet changer-statut-rendez-vous creer-formation creer-lead-magnet creer-offre creer-projet creer-publication-linkedin creer-video depublier-video lister-formations lister-lead-magnets lister-leads lister-offres lister-projets lister-publications-linkedin lister-rendez-vous lister-videos modifier-formation modifier-lead-magnet modifier-offre modifier-projet modifier-reglages modifier-video obtenir-formation obtenir-reglages obtenir-video publier-formation publier-lead-magnet publier-offre publier-projet publier-publication-linkedin publier-video reordonner-videos statistiques'.split(' ');
$('tools').innerHTML=TOOLS.map((n,i)=>`<div class="tool" id="tt${i}" style="left:${i<19?60:550}px;top:${450+(i%19)*35}px;font-size:18px;padding:3px 10px">${n}</div>`).join('');
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=10.15&&t<92.35)?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.2):cl((t-a)/.22),fo=id==='s9'?1:1-cl((t-(b-.18))/.18);el.style.opacity=Math.min(fi,fo);}}
  if(t<10.15){pop($('h0'),t,.1,.4,0,.3);pop($('h1'),t,2.2,.35,30,.2);pop($('h2'),t,2.95,.35,30,.2);
    const k=eout(cl((t-3.2)/.5));$('h3').style.transform=`scaleX(${k})`;$('h3').style.opacity=k>0?1:0;
    slam($('h4'),t,3.6);pop($('h5a'),t,3.55,.3,30,.3);pop($('h5b'),t,4.7,.3,30,.3);pop($('h5c'),t,5.9,.3,30,.3);pop($('h6'),t,8.4,.3,10);}
  else if(t<21.55){pop($('b0'),t,10.3,.35,20);pop($('b1'),t,10.6,.45,80);scrollImg($('b1i'),t,14.2,17.4,229);
    pop($('b2'),t,14.45,.3,20,.2);pop($('b3'),t,15.2,.3,20,.2);pop($('b4'),t,15.95,.3,20,.2);pop($('b5'),t,16.75,.3,20,.2);pop($('b6'),t,18.4,.35,20);}
  else if(t<33.05){pop($('m0'),t,21.7,.3,30,.03);pop($('m0a'),t,23.5,.2,-10);pop($('m1'),t,26.1,.3,30,.03);pop($('m1a'),t,26.5,.2,-10);
    pop($('m2'),t,26.8,.3,30,.03);pop($('m2a'),t,30.2,.2,-10);pop($('m3'),t,30.6,.3,30,.03);pop($('m4'),t,31.3,.4,40);}
  else if(t<45.4){pop($('f0'),t,33.2,.45,80);scrollImg($('f0i'),t,34.5,38.5,250);pop($('f1'),t,39.1,.45,80);
    pop($('f2a'),t,35.9,.3,30,.3);pop($('f2c'),t,41.7,.3,30,.3);pop($('f2b'),t,43.3,.3,30,.3);}
  else if(t<V(4,47.58)){pop($('p0'),t,45.5,.45,80);pop($('p1'),t,49.35,.45,80);scrollImg($('p1i'),t,50.6,53.2,180);pop($('p2'),t,51.9,.3,10);}
  else if(t<59.9){pop($('q0'),t,53.7,.35,20);[1,2,3,4].forEach((k,i)=>pop($('q'+k),t,54.0+i*.18,.3,30,.1));
    pop($('q5'),t,56.3,.4,60);pop($('q7'),t,56.5,.3,10);pop($('q6'),t,56.8,.4,60);pop($('q8'),t,57.0,.3,10);}
  else if(t<71.5){slam($('c0'),t,61.85);pop($('c1'),t,62.2,.3,20);TOOLS.forEach((n,i)=>pop($('tt'+i),t,62.4+i*.06,.2,15));
    pop($('c3'),t,65.4,.35,20);pop($('c4'),t,67.25,.35,30);}
  else if(t<85.1){pop($('l0'),t,72.6,.35,30,.03);pop($('l1'),t,73.9,.35,30,.03);pop($('l2'),t,75.55,.35,30,.03);pop($('l3'),t,78.9,.35,30,.03);slam($('l4'),t,80.55);}
  else if(t<92.35){pop($('z0'),t,85.2,.35,20);pop($('z1'),t,85.6,.45,60,.05);pop($('z2'),t,88.5,.3,20);pop($('z3'),t,90.3,.35,20);pop($('z4'),t,90.8,.3,10);}
  else {pop($('e0'),t,92.5,.4,0,.3);pop($('e1'),t,92.8,.4,30);slam($('e2'),t,97.5);slam($('e3'),t,98.2);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
