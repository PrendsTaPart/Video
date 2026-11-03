const { chromium } = require('playwright');
async function ready(p){ for (let i=0;i<60;i++){ const t=await p.evaluate(()=>document.body.innerText); if(!/se prépare/.test(t)) return; await p.waitForTimeout(1500);} }
(async () => {
  const out=process.argv[2];
  const b = await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
  const ctx = await b.newContext({viewport:{width:960,height:540}, deviceScaleFactor:1, recordVideo:{dir:out, size:{width:960,height:540}}});
  const p = await ctx.newPage();
  await p.goto('https://formation.foodeatup.fr/jeux/restaurant-3d/index.html',{waitUntil:'load',timeout:60000}); await ready(p);
  await p.evaluate(()=>document.querySelector('[data-action=play]').click());
  await p.waitForTimeout(30000);
  for(let i=0;i<4;i++){ await p.evaluate(()=>{const b=[...document.querySelectorAll('button')].find(b=>/Passer/.test(b.innerText)&&b.offsetParent); if(b) b.click();}); await p.waitForTimeout(2500);} 
  console.log(await p.evaluate(()=>[...document.querySelectorAll('button')].filter(b=>b.offsetParent).map(b=>b.innerText.trim().slice(0,30)).join(' | ')));
  await p.mouse.click(480,300); await p.waitForTimeout(500);
  const seq=[['KeyW',2000],['KeyD',500],['KeyW',1500],['KeyE',300],['KeyA',600],['KeyW',1500],['KeyE',300],['KeyV',200],['KeyW',2000],['KeyD',700],['KeyE',300],['KeyS',1200],['KeyA',900],['KeyW',2000],['KeyV',200],['KeyW',1500],['KeyE',300]];
  for(const [k,d] of seq){ await p.keyboard.down(k); await p.waitForTimeout(d); await p.keyboard.up(k); await p.waitForTimeout(700);} 
  await p.screenshot({path:out+'/end.png'});
  await ctx.close(); await b.close();
})();
