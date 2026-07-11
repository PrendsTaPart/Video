#!/usr/bin/env python3
import os, subprocess, json, time
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("audio", exist_ok=True)
KEY=""
for line in open("/home/user/Video/studio-video/.env"):
    if line.startswith("ELEVENLABS_API_KEY="):
        KEY=line.split("=",1)[1].strip().strip('"').strip("'")
VOICE="TGAegA0zNRi8I6nUdq3i"

SEG = [
("s00","Bienvenue dans FoodEatUp Academy. En cinq minutes, on configure votre restaurant de A à Z, de la création de votre boutique jusqu'au pilotage par l'intelligence artificielle. Dix-huit étapes, sept phases. C'est parti."),
("s10","Phase un : votre compte et votre boutique. On pose les fondations."),
("s11","Étape un : créez votre compte. Sur la page d'inscription, saisissez votre email, un mot de passe et votre nom, puis connectez-vous. Depuis votre avatar en haut à droite, vous retrouvez votre profil et votre abonnement."),
("s12","Étape deux : créez votre établissement. Depuis l'accueil admin, cliquez sur Créer un établissement, renseignez le nom et l'adresse. C'est la seule étape qui se fait uniquement sur le web. Tout le reste pourra être piloté par l'IA."),
("s20","Phase deux : les fondations. Deux réglages avant de brancher l'IA."),
("s21","Étape trois : configurez votre TVA. Ajoutez vos taux, vingt, dix, cinq et demi pour cent, avec un libellé. Ils serviront à vos produits, devis et factures."),
("s22","Étape quatre : créez vos catégories. Entrées, plats, desserts, boissons. Donnez un nom, un ordre, une couleur ou une icône pour structurer votre carte."),
("s30","Phase trois : connectez votre IA. C'est ici que la magie commence."),
("s31","Étape cinq : reliez FoodEatUp à Claude, Mistral ou ChatGPT via le protocole MCP StockVisionAI, et même à WhatsApp. Astuce du chef : donnez d'abord le contexte à votre IA en lui indiquant l'identifiant de votre établissement. Une fois connectée, elle agit directement dans votre restaurant."),
("s40","Phase quatre : remplissez votre contenu avec l'IA. Fini la saisie manuelle."),
("s41","Étape six : importez votre carte. Donnez votre menu en PDF ou en photo à votre IA, et laissez-la créer tous vos produits : nom, prix, catégorie. C'est le vrai gain de temps de FoodEatUp."),
("s42","Étape sept : créez vos ingrédients. Vos matières premières, avec unité, prix, stock et seuil d'alerte. Votre IA peut les déduire de votre carte."),
("s43","Étape huit : créez vos recettes. Associez ingrédients et quantités : FoodEatUp calcule votre coût matière et propose un prix de vente selon votre marge cible."),
("s44","Étape neuf : composez Ma carte. Ordonnez catégories et plats, activez ou masquez chaque élément par simple glisser-déposer."),
("s45","Étape dix : ajoutez vos fournisseurs, avec leurs coordonnées et conditions, pour vos ingrédients, commandes et livraisons."),
("s50","Phase cinq : votre équipe. Ajoutez vos collaborateurs, leurs rôles et leurs plannings."),
("s51","Étape onze : créez vos employés. Nom, rôle, permissions par module, et un QR code par personne pour le pointage et l'accès rapide."),
("s52","Étape douze : gérez plannings, pointages et congés. Définissez les horaires, suivez les arrivées et départs, validez ou refusez les absences."),
("s60","Phase six : hygiène et conformité HACCP. À régler une fois, puis ça devient un réflexe."),
("s61","Étape treize : configurez vos équipements et vos relevés de température, chambres froides, congélateurs, avec des alertes en cas de dépassement de seuil."),
("s62","Étape quatorze : gérez vos étiquettes DLC, la traçabilité de vos lots et le contrôle à réception à chaque livraison, photo et scan à l'appui."),
("s63","Étape quinze : définissez votre plan de nettoyage et vos checklists d'hygiène, exportables en PDF pour prouver votre conformité."),
("s70","Phase sept : l'exploitation. Votre restaurant est configuré. Pilotez-le au quotidien."),
("s71","Étape seize : gérez vos stocks, générez votre liste de courses, enregistrez vos livraisons et planifiez vos productions. FoodEatUp déduit automatiquement les ingrédients."),
("s72","Étape dix-sept : gérez vos clients, vos devis et vos factures conformes, TVA, remises, acompte, transformables en un clic."),
("s73","Étape dix-huit : PrediBot, votre assistant intégré. Posez-lui vos questions, anticipez vos ventes et vos besoins pour limiter le gaspillage, et faites votre premier bilan financier."),
("s99","Et voilà : votre restaurant est configuré, et piloté par l'IA. Pour aller plus loin, réservez une démo ou un coaching avec l'équipe BraindCode Academy. FoodEatUp, une infinité de solutions pour gérer votre restaurant."),
]

def gen(sid, text):
    out=f"audio/{sid}.mp3"
    if os.path.exists(out) and os.path.getsize(out)>2000:
        return True
    payload=json.dumps({"text":text,"model_id":"eleven_multilingual_v2",
        "voice_settings":{"stability":0.45,"similarity_boost":0.8,"style":0.15}})
    for t in range(1,6):
        r=subprocess.run(["curl","-s","-o",out,"-w","%{http_code}","-X","POST",
            f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}?output_format=mp3_44100_128",
            "-H",f"xi-api-key: {KEY}","-H","Content-Type: application/json","-d",payload],
            capture_output=True,text=True)
        if r.stdout.strip()=="200" and os.path.exists(out) and os.path.getsize(out)>2000:
            return True
        time.sleep(t*2)
    print("FAIL",sid,r.stdout.strip()); return False

total=0.0
for sid,text in SEG:
    ok=gen(sid,text)
    d=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f"audio/{sid}.mp3"]).strip()) if ok else 0
    total+=d
    print(f"{sid} {'ok' if ok else 'FAIL'} {d:.2f}s")
print(f"TOTAL VO {total:.1f}s")
