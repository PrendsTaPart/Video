const path=require('path');const {chromium}=require(path.join(process.env.GROOT,'playwright'));
(async()=>{
 const N=parseInt(process.env.FRAMES||'1800',10),FPS=30;
 const b=await chromium.launch({args:['--no-sandbox','--force-color-profile=srgb']});
 const p=await b.newPage({viewport:{width:1920,height:1080},deviceScaleFactor:1});
 await p.goto('file://'+path.resolve(__dirname,'boucle.html'));
 await p.evaluate(async()=>{await document.fonts.ready;});
 for(let i=0;i<N;i++){await p.evaluate(t=>window.render(t),i/FPS);
   await p.screenshot({path:path.join(__dirname,'work/frames',`f${String(i).padStart(4,'0')}.png`),clip:{x:0,y:0,width:1920,height:1080}});
   if(i%180===0)console.log('frame',i);}
 await b.close();console.log('DONE',N);
})().catch(e=>{console.error(e);process.exit(1);});
