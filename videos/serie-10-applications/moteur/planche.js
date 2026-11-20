// node planche.js <dossier épisode> t1 t2 ... -> <dossier>/planche.jpg (via ffmpeg)
const {chromium}=require('playwright');const {execFileSync}=require('child_process');const path=require('path');
(async()=>{const d=path.resolve(process.argv[2]);const ts=process.argv.slice(3).map(Number);
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+d+'/index.html',{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
const f=[];for(let i=0;i<ts.length;i++){await p.evaluate(t=>render(t),ts[i]);const o=`/tmp/claude-0/st-${i}.jpg`;await p.screenshot({path:o,type:'jpeg',quality:80});f.push(o);}
await p.evaluate(()=>thumb());await p.screenshot({path:'/tmp/claude-0/st-th.jpg',type:'jpeg'});f.push('/tmp/claude-0/st-th.jpg');
await b.close();
const args=[];f.forEach(x=>args.push('-i',x));const n=f.length;
execFileSync('ffmpeg',['-y','-v','error',...args,'-filter_complex',f.map((_,i)=>`[${i}]scale=270:480[s${i}]`).join(';')+';'+f.map((_,i)=>`[s${i}]`).join('')+`hstack=${n}`,d+'/planche.jpg']);})();
