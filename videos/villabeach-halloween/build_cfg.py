"""Construit cfg.js : lignes calées sur les silences de la voix (prise B), mots répartis au prorata des syllabes."""
import json,re
O=0.8  # la voix démarre après 0,8 s de nappe
L=[("Ici… la soirée commence quand le soleil se couche.",1.15,3.57),
("Mais samedi 31 octobre… le soleil ne se relèvera pas.",6.22,9.60),
("Villa Beach devient… le plus grand château hanté.",10.21,13.52),
("Deux ambiances. Deux univers musicaux.",14.73,17.40),
("D'un côté : hits, R&B, hip-hop, afro, house.",17.85,21.14),
("De l'autre : zouk, kompa, shatta, dancehall, bouyon.",21.53,24.95),
("Tout est prêt… Il ne manquait que vous.",25.91,28.60),
("Samedi 31 octobre. 23, rue des Pyrénées, à Lisses.",29.73,33.28),
("Villa Beach… la peur, sinon rien.",33.71,36.75)]
syl=lambda w:max(1,len(re.findall(r"[aeiouyàâéèêëîïôùûü]+",w.lower())) or 1)
words=[];lines=[]
for i,(txt,a,b) in enumerate(L):
  toks=[t for t in txt.split(" ") if t!=":"]
  n=[syl(t) for t in toks];tot=sum(n);acc=0
  for t,k in zip(toks,n):
    words.append([t,round(a+O+(b-a)*acc/tot,2),i]);acc+=k
  lines.append({"t0":round(a+O,2),"t1":round(b+O,2),"txt":txt})
dur=round(38.11+O+1.6,2)
cfg={"dur":dur,"words":words,"lines":lines,
 "kw":["soleil","couche.","31","octobre…","château","hanté.","Deux","hits,","zouk,","vous.","Lisses.","Villa","Beach…"],
 "red":["peur,","rien.","pas."],
 "bolts":[lines[1]["t0"]-.15,lines[2]["t0"]+.05,lines[2]["t0"]+1.9,lines[7]["t0"]-.1,lines[8]["t0"]+1.2],
 "heart":[lines[6]["t0"]-.3],
 "cut":lines[1]["t1"]+.05,
 "batsAt":lines[2]["t0"]+.4,
 "marks":{}}
open("cfg.js","w").write("window.CFG="+json.dumps(cfg,ensure_ascii=False)+";\nCFG.showCap=t=>t<CFG.lines[8].t0;\n")
json.dump(cfg,open("cfg.json","w"),ensure_ascii=False,indent=0)
print(dur,cfg["bolts"],cfg["heart"],cfg["cut"])
