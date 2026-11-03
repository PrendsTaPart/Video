// node make.js 84 85 ... : couvertures 16:9 (1600×900) des lead magnets, à partir du guide, de la miniature et du logo officiel.
const {chromium}=require('playwright');const path=require('path');const fs=require('fs');
const V='/home/user/Video/videos',C=V+'/_journal-63-72/commun/',S=process.env.MINI;
const G=JSON.parse(fs.readFileSync(V+'/_journal-74-83/guides/guides.json'));
const LOGO={claude:'logo-claude.webp',foodeatup:'logo-foodeatup.webp',rapidocms:'logo-rapidocms.webp'};
const SITE={85:'mes-projets/_sites2/pwa/desktop.png',91:'mes-projets/_sites2/pwa/desktop.png',89:'mes-projets/_sites/tablette/desktop.png',90:'mes-projets/_sites/tablette/desktop.png'};
const DUO=JSON.parse(process.env.DUO||'{}');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1600,height:900}});
for(const n of process.argv.slice(2)){const g=G[n];
 const d={n,titre:g.titre,kw:g.kw,k:'Le guide de l\'épisode',me:'file://'+C+'michael-rond.png',logo:'file://'+C+LOGO[SITE[n]?'foodeatup':(DUO[n]||'claude')],
  phone:'file://'+(fs.existsSync(`${S}/episode${n}-miniature.png`)?`${S}/episode${n}-miniature.png`:fs.readdirSync(V).filter(x=>x.startsWith(`episode${n}-`)).map(x=>`${V}/${x}/episode${n}-miniature.png`)[0]),
  doc:'file://'+V+`/_journal-74-83/couvertures/guide-${n}.png`,site:SITE[n]?'file://'+V+'/'+SITE[n]:null};
 await p.goto('file://'+path.resolve(__dirname,'cover.html')+'?d='+encodeURIComponent(JSON.stringify(d)));
 await p.waitForSelector('body[data-ok]',{timeout:20000}).catch(()=>{});
 await p.screenshot({path:`${__dirname}/lead-magnet-episode${n}.jpg`,type:'jpeg',quality:90});console.log(n);}
await b.close();})();
