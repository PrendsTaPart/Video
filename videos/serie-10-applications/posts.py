"""Génère posts.json et POSTS.md : légendes TikTok et LinkedIn (Michael, 1re personne) + calendrier 1 épisode/jour."""
import json, datetime, os
ICI = os.path.dirname(os.path.abspath(__file__))
EPS = json.load(open(f"{ICI}/episodes.json"))
PAGE = "https://foodeatup-10-applications.lovable.app"
DEBUT = datetime.date(2026, 11, 17)
HEURE = "18:00"
TAGS = {
 "haccp": "#HACCP #hygiene #restaurant", "caisse": "#caisse #restaurant #serveur",
 "kds": "#cuisine #coupdefeu #restaurant", "menu": "#menudigital #restaurant #commande",
 "fidelite": "#fidelite #commerce #restaurant", "recettes": "#recette #formation #cuisine",
 "production": "#production #cuisine #laboratoire", "labo": "#laboratoire #boulangerie #franchise",
 "game": "#jeux #famille #restaurant", "cocuisinage": "#recettes #cuisinemaison #restaurant",
}
INTRO_LI = {
 "tofu": "Nouvelle série : je vous présente les 10 applications FoodEatUp, une par une. Trois épisodes chacune : le problème, comment ça marche, et comment s'y mettre.",
 "mofu": "Suite d'hier.",
 "bofu": "Dernier épisode sur cette application.",
}
def legende_tiktok(e):
    txt = " ".join(p[0] for p in e["phrases"][:2])
    return f"{e['titre']} 👇 {txt} Écris {e['cle']} en commentaire, je t'envoie le lien. Épisode {e['n']}/30 · les 10 applis FoodEatUp. {TAGS[e['app']]} #foodeatup #restaurateur"

def texte_linkedin(e):
    corps = "\n".join(p[0] for p in e["phrases"][:-1])
    intro = INTRO_LI[e["funnel"]] if not (e["funnel"] == "tofu" and e["n"] > 1) else f"Application {(e['n'] - 1)//3 + 1}/10 : {e['nom']}."
    cible = "Pour les restaurateurs." if e["cible"] == "restaurateurs" else "Celle-ci est pour les particuliers : vos clients, votre famille."
    return (f"{e['titre']}\n\n{intro}\n\n{corps}\n\n{cible}\n\n"
            f"Toutes les applications sont présentées ici : {PAGE}\n\n"
            f"Écrivez {e['cle']} en commentaire et je vous envoie le lien.\n\n"
            f"Épisode {e['n']}/30\n\n{TAGS[e['app']]} #FoodEatUp #Restauration #Entrepreneur")

out = []
for e in EPS:
    d = DEBUT + datetime.timedelta(days=e["n"] - 1)
    out.append(dict(n=e["n"], slug=e["slug"], app=e["app"], funnel=e["funnel"], date=d.isoformat(), heure=HEURE,
                    titre=e["titre"], tiktok=legende_tiktok(e), linkedin=texte_linkedin(e)))
json.dump(out, open(f"{ICI}/posts.json", "w"), ensure_ascii=False, indent=1)
with open(f"{ICI}/POSTS.md", "w") as f:
    f.write("# Série « Les 10 applis FoodEatUp » — calendrier et textes\n\nUn épisode par jour à 18 h, du 17/11/2026 au 16/12/2026. TikTok Michael + LinkedIn Michael. Page de vente : " + PAGE + "\n\n")
    f.write("| # | Date | Application | Étape | Titre |\n|---|---|---|---|---|\n")
    for p in out: f.write(f"| {p['n']} | {p['date']} | {p['app']} | {p['funnel'].upper()} | {p['titre']} |\n")
    for p in out:
        f.write(f"\n## Épisode {p['n']} · {p['date']} · {p['titre']}\n\n### TikTok\n\n{p['tiktok']}\n\n### LinkedIn (Michael)\n\n{p['linkedin']}\n")
print(len(out), "posts")
