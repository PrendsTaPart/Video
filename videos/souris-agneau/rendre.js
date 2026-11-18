// node rendre.js : rend habillage.html en PNG transparents (30 i/s) et les incruste sur base.mp4 -> visuel.mp4
const {chromium}=require('playwright');const {spawn}=require('child_process');const path=require('path');
(async()=>{const d=__dirname;const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+path.join(d,'habillage.html'),{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
const dur=await p.evaluate(()=>window.CFG.dur);const fps=30,n=Math.round(dur*fps);
const ff=spawn('ffmpeg',['-y','-v','error','-i',path.join(d,'base.mp4'),'-f','image2pipe','-framerate',String(fps),'-c:v','png','-i','-',
 '-filter_complex','[0:v][1:v]overlay=0:0:shortest=1,format=yuv420p[v]','-map','[v]','-c:v','libx264','-preset','medium','-crf','19',path.join(d,'visuel.mp4')],{stdio:['pipe','inherit','inherit']});
for(let i=0;i<n;i++){await p.evaluate(t=>render(t),i/fps);const buf=await p.screenshot({type:'png',omitBackground:true});
 if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));if(i%300===0)console.log(i,'/',n);}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close();})();
