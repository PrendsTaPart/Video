#!/usr/bin/env python3
"""VO PrediBot (ElevenLabs, Adam, FR) — intro + 6 agents + outro."""
import os, urllib.request, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("audio", exist_ok=True)
# load key
KEY=None
for ln in open("/home/user/Video/studio-video/.env"):
    if ln.startswith("ELEVENLABS_API_KEY="): KEY=ln.strip().split("=",1)[1]
VOICE="TGAegA0zNRi8I6nUdq3i"  # Adam
VO={
 "intro":"PrediBot. Votre restaurant, dans une conversation. Un orchestrateur, et six agents spécialisés. Vous donnez un ordre en langage naturel, et chaque commande vous montre son résultat. Regardez.",
 "gen":"Le configurateur. Employés, fournisseurs, ingrédients, produits, recettes : vous dictez, il enregistre. Et chaque ajout apparaît aussitôt dans FoodEatUp.",
 "haccp":"La conformité. Une température relevée, vérifiée contre vos seuils critiques. Un frigo hors zone ? Il le voit.",
 "gf":"Les fournisseurs. Vos commandes, vos réceptions. Vous validez la livraison depuis le quai, sans remonter au bureau.",
 "rh":"Les ressources humaines. La liste de votre équipe, les congés à approuver ou refuser, le classement de vos employés. Entre deux services.",
 "stock":"Les stocks. Vos niveaux, vos recettes, une commande fournisseur en un message. Et un vrai tableau de bord qui se génère tout seul.",
 "prod":"La production. Vos plats, votre rentabilité, vos meilleures ventes, et une estimation de ce que vous devrez produire demain. Jusqu'au tableau de bord complet.",
 "outro":"Six agents. Une conversation. Zéro ordinateur. Vous pilotez, l'IA exécute.",
}
def gen(name, text):
    out=f"audio/vo_{name}.mp3"
    body=json.dumps({"text":text,"model_id":"eleven_multilingual_v2",
        "voice_settings":{"stability":0.45,"similarity_boost":0.8,"style":0.15}}).encode()
    req=urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}?output_format=mp3_44100_128",
        data=body, headers={"xi-api-key":KEY,"Content-Type":"application/json"})
    with urllib.request.urlopen(req,timeout=120) as r, open(out,"wb") as f:
        f.write(r.read())
    import subprocess
    d=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",out]).strip())
    print("ok",name,round(d,2),"s")
for n,t in VO.items(): gen(n,t)
print("VO DONE")
