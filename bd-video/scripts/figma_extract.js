// Lecture seule — à passer à l'outil Figma use_figma (fichier izfLEauBeeBnTcTt9tOAMm), 11 pages par appel.
// Remplacer IDS par la liste des nœuds de page. Le résultat concaténé = figma/extraction.json.
const IDS = [/* '58:364', '98:348', … */];
const page = await figma.getNodeByIdAsync('0:1');
await figma.setCurrentPageAsync(page);
const byPos=(a,b)=>(a.y-b.y)||(a.x-b.x);
const kids=n=>('children' in n)?[...n.children].filter(k=>k.visible!==false).sort(byPos):[];
const imgOf=n=>{if(!('fills' in n)||!Array.isArray(n.fills))return null;const f=n.fills.find(f=>f.type==='IMAGE'&&f.visible!==false);return f?f.imageHash:null;};
const texts=n=>n.type==='TEXT'?[n.characters]:kids(n).flatMap(texts);
function walk(n,cs,out){
  const nm=n.name;
  if(n.type==='TEXT'){ if(nm==='folio'||/^\d+$/.test(n.characters.trim()))return; out.items.push([cs,'T',null,n.characters]);return;}
  const h=imgOf(n);
  if(h && /^img:|^portrait:|^Rectangle$|^Logo/.test(nm)){out.imgs.push([cs,n.id,nm,h,Math.round(n.width),Math.round(n.height)]);if(!('children' in n))return;}
  if(/^Case \d+/.test(nm)){const c=+nm.match(/\d+/)[0];for(const k of kids(n))walk(k,c,out);return;}
  if(nm==='Récitatif'){out.items.push([cs,'R',null,texts(n).join(' ')]);return;}
  if(/^Bulle/.test(nm)){
    const loc=kids(n).find(k=>k.name==='Locuteur');
    let sp=null,ph=null,pid=null;
    if(loc){const p=kids(loc).find(k=>/^Pastille/.test(k.name));if(p){ph=imgOf(p);pid=p.id;}const t=kids(loc).find(k=>k.type==='TEXT');sp=t?t.characters:null;}
    const rep=kids(n).filter(k=>k!==loc).flatMap(texts).join(' ');
    out.items.push([cs,'B',sp,rep,ph,pid,nm]);return;}
  if(/^Carte · /.test(nm)){const p=kids(n).find(k=>/^portrait:/.test(k.name));out.items.push([cs,'C',nm.replace('Carte · ',''),texts(n).join(' | '),p?imgOf(p):null,p?p.id:null]);for(const k of kids(n))if(k!==p&&imgOf(k))out.imgs.push([cs,k.id,k.name,imgOf(k),Math.round(k.width),Math.round(k.height)]);for(const k of kids(n))if(k.name==='Logos IA')for(const l of kids(k))out.imgs.push([cs,l.id,l.name,imgOf(l),Math.round(l.width),Math.round(l.height)]);return;}
  for(const k of kids(n))walk(k,cs,out);
}
const res=[];
for(const id of IDS){const f=await figma.getNodeByIdAsync(id);const out={id,n:f.name,imgs:[],items:[]};for(const k of kids(f))walk(k,0,out);res.push(out);}
return res;
