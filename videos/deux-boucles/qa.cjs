const path=require('path');const {chromium}=require(path.join(process.env.GROOT,'playwright'));
(async()=>{
 const b=await chromium.launch({args:['--no-sandbox','--force-color-profile=srgb']});
 const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
 await p.goto('file://'+path.resolve(__dirname,'InfinityLoop.html'));
 await p.evaluate(async()=>{await document.fonts.ready;});
 for(const fr of [60,200,520,690,900,1330,1560,1850]){
   await p.evaluate(x=>window.render(x),fr);
   await p.screenshot({path:`work/qa_${fr}.png`,clip:{x:0,y:0,width:1080,height:1920}});
 }
 await b.close();console.log('ok');
})().catch(e=>{console.error(e);process.exit(1);});
