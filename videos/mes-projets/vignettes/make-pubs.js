// node make-pubs.js : vignettes des épisodes « Mes projets en pub » (même design que les couvertures projet)
const {chromium}=require('playwright'),path=require('path');
const V=path.resolve(__dirname,'../..'),C=V+'/_journal-63-72/commun/';
const data=[
 {n:93,dir:'episode93-mes-30-projets',ecran:'assets/claude-construit.jpg',logo:null,nom:'Michael Kebail-Ali',hook:'Mes projets passent en pub.',punchline:'Le problème, la solution, comment l\'essayer.'},
 {n:94,dir:'episode94-pub-caisse-mobile',ecran:'assets/ecran-desktop.jpg',logo:'logo-foodeatup.webp',nom:'FoodEatUp',hook:'La commande à table, l\'encaissement dans la poche.',punchline:'Gratuite avec ta caisse FoodEatUp.'}];
(async()=>{const b=await chromium.launch();
for(const e of data){const d={...e,f:'v',ecran:'file://'+V+'/'+e.dir+'/'+e.ecran,me:'file://'+C+'michael-portrait.jpg',logo:e.logo?'file://'+C+e.logo:null};
 const p=await b.newPage({viewport:{width:1080,height:1920}});
 await p.goto('file://'+__dirname+'/vignette.html?d='+encodeURIComponent(JSON.stringify(d)));
 await p.waitForSelector('body[data-ok]',{timeout:30000});
 const out=`${V}/${e.dir}/episode${e.n}-miniature.png`;await p.screenshot({path:out});await p.close();console.log(out);}
await b.close();})();
