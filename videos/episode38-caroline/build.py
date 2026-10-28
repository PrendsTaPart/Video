"""Ép. 38 : place les répliques bout à bout, produit cfg.js (timeline + mots) et vo.wav."""
import json, subprocess
A = "v38/a/"
# (locuteur, fichier, début, fin, texte affiché, écart avant)
L = [
 ("chef","chef",0.00,1.40,"Qui a rempli mon resto ?",0.6),
 ("caro","caroline",0.00,0.55,"Moi !",0.25),
 ("chef","chef",1.62,3.92,"Pas maintenant, j'ai trois plats sur le feu !",0.3),
 ("caro","caroline",0.72,1.64,"Je décroche.",0.2),
 ("caro","caroline",1.80,4.52,"Restaurant FoodEatUp, Caroline à l'appareil, bonjour !",1.5),
 ("cli","client",0.00,2.05,"Bonjour, une table pour quatre ce soir ?",0.35),
 ("caro","caroline",4.68,6.15,"20 h, c'est réservé !",0.3),
 ("cli","client",2.22,3.32,"Deux pizzas à emporter !",0.7),
 ("caro","caroline",6.36,8.48,"Envoyé en cuisine, prêtes dans 20 minutes !",0.3),
 ("cli","client",3.48,5.52,"On sera dix, pour un anniversaire !",0.7),
 ("caro","caroline",8.60,12.84,"Complet à 20 h. 21 h 30, ça vous va ? Je préviens le chef pour le gâteau !",0.35),
 ("chef","chef",4.06,6.00,"Tout ça pendant que je cuisinais ?!",0.8),
 ("caro","caroline",13.00,15.55,"Toi, tu cuisines. Moi, je décroche.",0.35),
 ("caro","caroline",15.68,19.36,"Tu veux Caroline dans ton resto ? Commente CAROLINE, je t'envoie la démo.",0.9),
]
W = json.load(open("v38/words.json"))
t, lines, flt, ins = 0.0, [], [], []
for k,(sp,f,a,b,txt,gap) in enumerate(L):
    t += gap
    ww = [w for w in W[A+f+".mp3"] if a-0.05 <= w[1] < b]
    v0 = ww[0][1] if ww else a; v1 = min(b, ww[-1][2]) if ww else b
    words = txt.split()
    # mots répartis au prorata de leur longueur sur la durée réellement parlée
    tot = sum(len(x)+1 for x in words); acc = 0; wt = []
    for x in words:
        wt.append(round(t + (v0-a) + (v1-v0)*acc/tot, 2)); acc += len(x)+1
    lines.append({"sp":sp,"t0":round(t,2),"t1":round(t+b-a,2),"txt":txt,"w":list(zip(words,wt))})
    ins += ["-i", A+f+".mp3"]
    ms = int(t*1000)
    flt.append(f"[{k}:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={b-a-0.04:.2f}:d=0.04,aresample=48000,adelay={ms}|{ms}[l{k}]")
    t += b-a
dur = round(t + 3.2, 2)
flt.append("".join(f"[l{k}]" for k in range(len(L))) + f"amix=inputs={len(L)}:normalize=0,apad=whole_dur={dur}[o]")
subprocess.run(["ffmpeg","-y","-v","error",*ins,"-filter_complex",";".join(flt),"-map","[o]","-t",str(dur),"-ac","1","v38/vo.wav"],check=True)
cfg = {"dur":dur,"lines":lines}
open("v38/cfg.js","w").write("window.CFG="+json.dumps(cfg,ensure_ascii=False)+";")
json.dump(cfg,open("v38/cfg.json","w"),ensure_ascii=False,indent=0)
for l in lines: print(l["sp"],l["t0"],l["t1"],l["txt"])
print("dur",dur)
