const path=require('path');const {chromium}=require(path.join(process.env.GROOT,'playwright'));
(async()=>{
 const b=await chromium.launch({args:['--no-sandbox','--force-color-profile=srgb']});
 const p=await b.newPage({viewport:{width:1920,height:1080},deviceScaleFactor:1});
 await p.goto('file://'+path.resolve(__dirname,'youdy.html'));
 await p.evaluate(async()=>{await document.fonts.ready;});
 for(const fr of [75,250,410,610,850,1085,1350,1600,1850,2050]){
   await p.evaluate(x=>window.render(x),fr);
   await p.screenshot({path:`work/qa_${fr}.png`,clip:{x:0,y:0,width:1920,height:1080}});}
 await b.close();console.log('ok');
})().catch(e=>{console.error(e);process.exit(1);});
