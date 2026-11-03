// node make.js : compose les vignettes Mes projets (1080x1920 et 1280x720) au style des couvertures projet
const {chromium}=require('playwright'),path=require('path'),fs=require('fs');
const V=path.resolve(__dirname,'../..'),C=V+'/_journal-63-72/commun/';
(async()=>{const b=await chromium.launch(),data=JSON.parse(fs.readFileSync(__dirname+'/data.json'));
const only=process.argv.slice(2).map(Number);
for(const e of data){ if(only.length&&!only.includes(e.n)) continue;
 for(const [f,W,H] of [['v',1080,1920],['h',1280,720]]){
  const d={...e,f,ecran:'file://'+V+'/'+e.dir+'/og.png',me:'file://'+C+'michael-portrait.jpg',logo:e.logo?'file://'+C+e.logo:null};
  const p=await b.newPage({viewport:{width:W,height:H}});
  await p.goto('file://'+__dirname+'/vignette.html?d='+encodeURIComponent(JSON.stringify(d)));
  await p.waitForSelector('body[data-ok]',{timeout:30000});
  const out=f=='v'?`${V}/${e.dir}/episode${e.n}-miniature.png`:`${__dirname}/couverture-${e.slug}-1280x720.png`;
  await p.screenshot({path:out});await p.close();console.log(out);}}
await b.close();})();
