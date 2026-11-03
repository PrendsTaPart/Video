#!/usr/bin/env python3
"""VO complète (13 lignes) — texte validé, espacé pour éviter les 401."""
import urllib.request, json, subprocess, time, os
os.chdir(os.path.dirname(os.path.abspath(__file__))); os.makedirs("audio",exist_ok=True)
KEY=[l.strip().split("=",1)[1] for l in open("/home/user/Video/studio-video/.env") if l.startswith("ELEVENLABS_API_KEY=")][0]
V="TGAegA0zNRi8I6nUdq3i"
VO={
 "hook":"Il est onze heures. Vous êtes chez votre poissonnier. Votre chambre froide vient de monter à huit degrés. Vous l'apprendrez ce soir. Peut-être.",
 "intro":"Un patron de restaurant n'est jamais assis devant un ordinateur. Il est en cuisine, en salle, chez un fournisseur. Alors on a arrêté de lui demander d'ouvrir un logiciel. Voici PrediBot : votre restaurant, dans une conversation WhatsApp.",
 "orch":"Derrière votre message, un orchestrateur. Il comprend ce que vous voulez, et le confie à l'un de ses six spécialistes. Comme une brigade : chacun son poste.",
 "socle":"Et sous ces six agents, un seul et même squelette : il reçoit, il analyse, il s'authentifie, il agit. Chaque restaurant a sa propre clé. Vos données restent les vôtres.",
 "gen":"Le configurateur. Vous dictez, il enregistre. Un employé. Un fournisseur. Un ingrédient. Un produit. Une recette. Chaque commande, et le résultat s'affiche aussitôt dans FoodEatUp. Ce qui vous prenait un après-midi de saisie prend le temps d'un message.",
 "haccp":"La conformité. Température relevée : c'est enregistré, et vérifié contre vos seuils critiques. Le frigo hors zone ? Il le voit, et il l'affiche en rouge. Le jour de l'inspection, vous n'avez rien à préparer.",
 "gf":"Les fournisseurs. Vos commandes en attente, d'un coup d'œil. Vous validez la réception, conforme, depuis le quai, sans jamais remonter au bureau.",
 "rh":"Les ressources humaines. La liste de votre équipe. Les congés à approuver, ou à refuser, en une phrase. Et le classement de vos employés. Votre RH, entre deux services.",
 "stock":"Les stocks. Vos niveaux critiques. Une commande fournisseur créée en un message. Et là, regardez : il ne répond pas par du texte, il fabrique un vrai tableau de bord, interactif, et vous envoie le lien. Un outil de pilotage, depuis une conversation.",
 "prod":"La production. Vos productions du jour, vos ingrédients manquants, la rentabilité de vos plats, vos meilleures ventes. Et une estimation de ce que vous devrez produire demain, entraînée sur votre historique. Jusqu'au tableau de bord complet.",
 "alertes":"Mais le plus important, PrediBot ne l'attend pas : il vous le dit. Température anormale. Réception non contrôlée. Stock au plus bas. Une notification, sur le téléphone que vous avez déjà dans la main.",
 "retour":"Il est onze heures. Vous êtes chez votre poissonnier. Votre chambre froide monte à huit degrés. Vous le savez, maintenant.",
 "outro":"Six agents. Une conversation. Zéro ordinateur. Vous pilotez, l'IA exécute.",
}
for n,t in VO.items():
    for attempt in range(6):
        try:
            body=json.dumps({"text":t,"model_id":"eleven_multilingual_v2","voice_settings":{"stability":0.45,"similarity_boost":0.8,"style":0.15}}).encode()
            req=urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{V}?output_format=mp3_44100_128",data=body,headers={"xi-api-key":KEY,"Content-Type":"application/json"})
            with urllib.request.urlopen(req,timeout=120) as r,open(f"audio/vo_{n}.mp3","wb") as f: f.write(r.read())
            d=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f"audio/vo_{n}.mp3"]).strip())
            print("ok",n,round(d,1)); break
        except Exception as e:
            print("retry",n,attempt,str(e)[:40]); time.sleep(5)
    time.sleep(2)
print("VO FULL DONE")
