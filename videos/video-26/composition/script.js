const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eout=x=>1-Math.pow(1-x,3);
const A=[0,39.9,64.56], P=[0.5,49.9];
const V=(i,w)=>P[i]+(w-A[i]);
const DUR=77;
const SC=[['s0',0,V(0,1.7)],['s1',V(0,1.7),V(0,10.44)],['s2',V(0,10.44),V(0,12.36)],['s3',V(0,12.36),V(0,18.7)],['s4',V(0,18.7),V(0,23.5)],['s5',V(0,23.5),V(0,27.68)],['s6',V(0,27.68),40.4],['s7',40.4,49.9],['s8',49.9,V(1,46.22)],['s9',V(1,46.22),V(1,51.78)],['s10',V(1,51.78),V(1,56.96)],['s11',V(1,56.96),V(1,61.74)],['s12',V(1,61.74),DUR]];
function pop(el,t,a,d=.4,dy=40,sc=0,rot=''){const p=eout(cl((t-a)/d));el.style.opacity=p;el.style.transform=`${rot} translateY(${(1-p)*dy}px) scale(${1-sc*(1-p)})`;return p;}
function slam(el,t,a,rot=''){const x=cl((t-a)/.3);const s=x<1?1.5-0.5*eout(x):1;el.style.opacity=x>0?1:0;el.style.transform=`${rot} scale(${s})`;}
function flow(id,items,top,gap,cls=''){$(id).innerHTML=items.map((f,i)=>`<div class="nd ${cls}" id="${id}${i}" style="top:${top+i*gap}px">${f}</div>`).join('');}
flow('s3f',['Fixtures Webhook','Build Query','Fetch Fixtures For Date','Filter And Rank Fixtures','Return Fixture List'],200,125);
$('s4c').innerHTML=['H2H','Stats domicile','Stats extérieur','Effectifs'].map((c,i)=>`<div class="pill" id="pc${i}" style="left:${60+i*245}px;top:${i%2?330:230}px;font-size:23px">${c}</div>`).join('')+`<div class="pill" id="pc4" style="left:60px;top:440px;border-color:#fff;font-size:23px">API-Football · match</div>`;
flow('s5f',['Webhook + configuration','Agent de prompts · Gemini Flash','Image de début','Image de fin','→ déclenche WC2026_3'],200,140);
const MW=[[13.02,0],[13.7,1],[15.58,2],[16.72,3],[17.64,4]];
function render(t){
  $('thumb').style.display='none';$('logos').style.display=(t>=V(0,1.7)&&t<V(1,61.74)&&!(t>=40.4&&t<49.9))?'flex':'none';
  for(const [id,a,b] of SC){const el=$(id);const on=t>=a&&t<b;el.style.display=on?'block':'none';
    if(on){const fi=id==='s0'?cl(t/.2):cl((t-a)/.22),fo=id==='s12'?1:1-cl((t-(b-.18))/.18);el.style.opacity=Math.min(fi,fo);}}
  if(t<V(0,1.7)){slam($('s0a'),t,.1);pop($('s0m'),t,.3,.4,80);}
  else if(t<V(0,10.44)){pop($('s1t'),t,V(0,1.8),.4,30,.1);const bx=360+Math.sin(t*3)*250;$('s1b').style.left=bx+'px';$('s1b').style.transform=`rotate(${t*300}deg)`;pop($('b0'),t,V(0,5.18),.4,60,.5);pop($('b1'),t,V(0,8.82),.35,60,.5,'scale(.8)');pop($('b2'),t,V(0,9.2),.35,60,.5);pop($('s1a'),t,V(0,9.64),.3,20);}
  else if(t<V(0,12.36)){slam($('s2a'),t,V(0,11.6));pop($('s2b'),t,V(0,11.9),.3,20);}
  else if(t<V(0,18.7)){MW.forEach(([w,i])=>pop($('s3f'+i),t,V(0,w),.3,20,.05));pop($('s3p'),t,V(0,13.7),.3,20,.3);pop($('s3d'),t,V(0,14.4),.3,10);}
  else if(t<V(0,23.5)){[0,1,2,3,4].forEach(i=>pop($('pc'+i),t,V(0,18.8)+i*.3,.25,20,.3));pop($('s4g'),t,V(0,20.52),.35,20,.1);slam($('s4s'),t,V(0,22.4));pop($('s4d'),t,V(0,22.7),.3,10);}
  else if(t<V(0,27.68)){[23.6,24.6,26.06,26.74,27.2].forEach((w,i)=>pop($('s5f'+i),t,V(0,w),.25,20,.05));pop($('s5d'),t,V(0,26.5),.3,10);}
  else if(t<40.4){pop($('a0'),t,V(0,30.54),.3,30,.03);pop($('a1'),t,V(0,32.64),.3,30,.03);pop($('a2'),t,V(0,34.72),.3,30,.03);pop($('a3'),t,V(0,37.94),.3,30,.03);pop($('a4'),t,V(0,28.4),.3,10);}
  else if(t<49.9){const c=t-40.4;pop($('c0'),t,40.5,.4,-30);pop($('m0'),t,40.7,.4,200);pop($('m1'),t,40.9,.4,200);
    const sq=1+0.08*Math.sin(c*8);$('m0').style.transform+=` scaleY(${sq})`;$('m1').style.transform+=` scaleY(${2-sq})`;
    const bx=c<5?220+((c*400)%600):540, by=c<5?1100-Math.abs(Math.sin(c*4))*350:760;$('c2').style.left=(bx-55)+'px';$('c2').style.top=by+'px';$('c2').style.transform=`rotate(${c*400}deg)`;
    $('c1a').textContent=c<2.5?'0':c<5?'1':'2';$('c1b').textContent=c<3.8?'0':'1';pop($('c1'),t,40.6,.4,0,.5);slam($('c3'),t,46.0);}
  else if(t<V(1,46.22)){pop($('e0'),t,V(1,42.32),.3,30,.03);pop($('e1'),t,V(1,44.4),.3,30,.03);pop($('e2'),t,V(1,45.3),.3,30,.03);slam($('e3'),t,V(1,45.8));}
  else if(t<V(1,51.78)){slam($('f0'),t,V(1,48.78));pop($('f1'),t,V(1,50.6),.3,20);pop($('f2'),t,V(1,46.4),.4,80);}
  else if(t<V(1,56.96)){pop($('o0'),t,V(1,52.0),.4,30);pop($('o1'),t,V(1,52.6),.4,30);pop($('o2'),t,V(1,54.5),.3,20);}
  else if(t<V(1,61.74)){pop($('g0'),t,V(1,57.0),.35,20);slam($('g1'),t,V(1,59.18));pop($('g2'),t,V(1,57.3),.4,80);}
  else {pop($('s12p'),t,V(1,61.8),.4,0,.3);pop($('s12q'),t,V(1,62.1),.4,30);pop($('s12l'),t,V(1,63.2),.4,20);}
}
function thumb(){for(const [id] of SC)$(id).style.display='none';$('logos').style.display='none';$('thumb').style.display='block';}
window.render=render;window.thumb=thumb;window.DUR=DUR;
