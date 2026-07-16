#!/usr/bin/env python3
"""VO par commande (26) — explique chaque écran WhatsApp -> résultat FoodEatUp. Style 'je demande X, et voilà'."""
import urllib.request, json, subprocess, time, os
os.chdir(os.path.dirname(os.path.abspath(__file__))); os.makedirs("audio",exist_ok=True)
KEY=[l.strip().split("=",1)[1] for l in open("/home/user/Video/studio-video/.env") if l.startswith("ELEVENLABS_API_KEY=")][0]
V="TGAegA0zNRi8I6nUdq3i"
CMD={
 0:"Regardez : je demande d'ajouter un employé. Aussitôt, il apparaît dans la fiche équipe de FoodEatUp.",
 1:"J'ajoute un fournisseur en un simple message. Et voilà : il est enregistré dans FoodEatUp.",
 2:"Un nouvel ingrédient, dicté à l'agent. Il arrive directement dans votre stock FoodEatUp.",
 3:"J'ajoute un produit à la carte. Confirmation immédiate : c'est en ligne.",
 4:"Je dicte une recette. Elle rejoint aussitôt vos recettes dans FoodEatUp.",
 5:"Je relève une température. Elle est vérifiée contre vos seuils : le frigo hors zone s'affiche en rouge.",
 6:"Je demande mes commandes en attente. Il me les liste toutes, d'un coup d'œil.",
 7:"Je valide une réception. Sur FoodEatUp, la commande passe en livrée.",
 8:"Je demande la liste de mon équipe. Il me la sort en une seconde.",
 9:"Mes congés en attente ? Les voici, prêts à traiter.",
 10:"J'approuve un congé. C'est validé, tout de suite.",
 11:"Je rejette un autre congé, en une phrase. C'est fait.",
 12:"Je demande le classement de mes employés. Il le calcule instantanément.",
 13:"Mes stocks critiques ? Il me remonte les derniers, avec les alertes.",
 14:"Je demande mes recettes. La liste arrive, complète.",
 15:"Je vérifie un fournisseur. Il me retrouve sa fiche en un instant.",
 16:"Je crée une commande fournisseur. Elle apparaît dans FoodEatUp, prête à envoyer.",
 17:"Et là, regardez : il génère un vrai tableau de bord des stocks, et m'envoie le lien.",
 18:"Je demande mes productions du jour. Il me les liste, avec les ingrédients manquants.",
 19:"Je vérifie les ingrédients d'une production. Tout est là, en détail.",
 20:"Je valide une production. Sur FoodEatUp, elle passe au vert.",
 21:"J'ajoute une production pour le week-end. Planifiée, en un message.",
 22:"Je lui demande de prédire les prochains jours. Il estime, sur votre historique.",
 23:"J'analyse la rentabilité de mes plats. La marge de chaque plat, calculée.",
 24:"Mes meilleures ventes ? Voici le top des trente derniers jours.",
 25:"Et pour finir : le tableau de bord production complet, généré en un message.",
}
for i,t in CMD.items():
    out=f"audio/vo_cmd{i:02d}.mp3"
    if os.path.exists(out) and os.path.getsize(out)>2000: print("skip",i); continue
    for attempt in range(6):
        try:
            body=json.dumps({"text":t,"model_id":"eleven_multilingual_v2","voice_settings":{"stability":0.45,"similarity_boost":0.8,"style":0.12}}).encode()
            req=urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{V}?output_format=mp3_44100_128",data=body,headers={"xi-api-key":KEY,"Content-Type":"application/json"})
            with urllib.request.urlopen(req,timeout=120) as r,open(out,"wb") as f: f.write(r.read())
            d=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",out]).strip())
            print("ok",i,round(d,1)); break
        except Exception as e:
            print("retry",i,attempt,str(e)[:40]); time.sleep(5)
    time.sleep(1.5)
print("VO CMDS DONE")
