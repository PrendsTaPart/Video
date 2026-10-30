// node make2.js : couvertures 16:9 des lead magnets plus anciens (épisodes 54, 62 à 73), même gabarit que make.js.
const {chromium}=require('playwright');const path=require('path');
const V='/home/user/Video/videos',C='file://'+V+'/_journal-63-72/commun/',H='file://'+__dirname+'/';
const mini=(n)=>{const d=require('fs').readdirSync(V).find(x=>x.startsWith(`episode${n}-`));return 'file://'+`${V}/${d}/episode${n}-miniature.png`;};
const L=[
 [62,'OUVRIR','7 questions à poser à Claude pour ouvrir son restaurant','claude'],
 [63,'CONSULTANT','Les 5 demandes qui remplacent un consultant','claude'],
 [64,'PHRASES','Les 5 phrases à dire à Claude avant de te lancer','claude'],
 [65,'BOUTIQUE','Anthropic a confié une boutique à Claude','claude'],
 [66,'EXPERT','La phrase EXPERT','claude'],
 [67,'WEEKEND','5 projets à construire avec Claude en un week-end','claude'],
 [68,'CONFIG','Les 5 réglages de Claude, pas à pas','claude'],
 [69,'OUTILS',"Mes outils, ceux qui remplacent l'agence web",'claude'],
 [70,'CAISSE','Espèces ou carte : le calcul complet','foodeatup'],
 [71,'HEURE',"Calcule ton vrai salaire à l'heure",'foodeatup'],
 [72,'CHINE','Les IA chinoises à connaître (et Mistral)','claude'],
 [73,'TERRAIN','La méthode : une appli en une journée','rapidocrm'],
];
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1600,height:900}});
const go=async(d,out)=>{await p.goto('file://'+path.resolve(__dirname,'cover.html')+'?d='+encodeURIComponent(JSON.stringify(d)));
 await p.waitForSelector('body[data-ok]',{timeout:20000}).catch(()=>{});await p.screenshot({path:`${__dirname}/${out}`,type:'jpeg',quality:90});console.log(out);};
for(const [n,kw,titre,logo] of L) await go({n,kw,titre,k:"Le guide de l'épisode",me:C+'michael-rond.png',logo:C+`logo-${logo}.webp`,phone:mini(n),doc:H+`guide-${n}.png`},`lead-magnet-episode${n}.jpg`);
await go({n:54,kw:'BD',titre:'La BD : Découvrir FoodEatUp',k:"La BD de l'épisode",g:'BD gratuite',me:C+'michael-rond.png',logo:C+'logo-foodeatup.webp',phone:H+'ep54-mini.png',doc:'file://'+V+'/bande-dessinee/decouvrir-foodeatup/planches/planche-01.jpg'},'lead-magnet-episode54.jpg');
await b.close();})();
