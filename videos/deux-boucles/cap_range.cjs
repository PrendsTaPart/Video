const path=require('path');const {chromium}=require(path.join(process.env.GROOT,'playwright'));
(async()=>{
 const [start,end,dir]=[parseInt(process.argv[2]),parseInt(process.argv[3]),process.argv[4]];
 const b=await chromium.launch({args:['--no-sandbox','--force-color-profile=srgb']});
 const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
 await p.goto('file://'+path.resolve(__dirname,'InfinityLoop.html'));
 await p.evaluate(async()=>{await document.fonts.ready;});
 let idx=0;
 for(let fr=start;fr<end;fr++){ await p.evaluate(x=>window.render(x),fr);
   await p.screenshot({path:path.join(__dirname,'work',dir,`f${String(idx).padStart(4,'0')}.png`),clip:{x:0,y:0,width:1080,height:1920}}); idx++; }
 await b.close();console.log('DONE',dir,idx);
})().catch(e=>{console.error(e);process.exit(1);});
