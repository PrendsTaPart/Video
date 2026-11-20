// node rendre.js <slug> : habillage.html?s=<slug> en PNG transparents (30 i/s) incrustés sur work/<slug>/base.mp4 -> work/<slug>/visuel.mp4, plus la miniature
const {chromium}=require('playwright');const {spawn}=require('child_process');const path=require('path');
(async()=>{const d=__dirname,s=process.argv[2],w=path.join(d,'work',s);const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+path.join(d,'habillage.html')+'?s='+s,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
const dur=await p.evaluate(()=>window.CFG.dur);const fps=30,n=Math.round(dur*fps);
await p.evaluate(()=>thumb());await p.screenshot({path:path.join(w,'titre.png'),omitBackground:true});
const ff=spawn('ffmpeg',['-y','-v','error','-i',path.join(w,'base.mp4'),'-f','image2pipe','-framerate',String(fps),'-c:v','png','-i','-',
 '-filter_complex','[0:v][1:v]overlay=0:0:shortest=1,format=yuv420p[v]','-map','[v]','-c:v','libx264','-preset','medium','-crf','19',path.join(w,'visuel.mp4')],{stdio:['pipe','inherit','inherit']});
for(let i=0;i<n;i++){await p.evaluate(t=>render(t),i/fps);const buf=await p.screenshot({type:'png',omitBackground:true});
 if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close();})();
