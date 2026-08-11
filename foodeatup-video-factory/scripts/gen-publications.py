#!/usr/bin/env python3
"""Écrit les 4 publications de chaque épisode — une par réseau — dans le fichier
de données de FoodEatUp Social.

Le principe : la légende n'est pas la même d'un réseau à l'autre. Poster le même
bloc de texte partout, c'est passer à côté de trois des quatre réseaux.

  - Instagram et TikTok ne rendent pas les liens cliquables dans une légende.
    Y coller une URL, c'est afficher une chaîne morte : on renvoie vers la bio.
  - LinkedIn rend le lien cliquable mais pénalise les posts qui sortent du fil ;
    le lien passe donc en fin de texte, et le ton se tient à ce qui se mesure.
  - Facebook accepte le lien dans le corps et tolère un texte plus long.
  - TikTok se lit en une seconde : deux lignes, cinq mots-dièse, rien d'autre.

Les horaires sont décalés par réseau pour qu'un même épisode ne tombe pas
quatre fois au même moment sur quatre fils.
"""
import json, re, unicodedata, sys, os

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOCIAL = os.path.join(os.path.dirname(R), "foodeatup-social")

# --- Ce qui change d'un réseau à l'autre --------------------------------------
RESEAUX = {
    "facebook":  {"heure": "12:00", "format": "Vidéo native 9:16",
                  "lien_cliquable": True,  "nb_tags": 7},
    "instagram": {"heure": "18:30", "format": "Reel 9:16",
                  "lien_cliquable": False, "nb_tags": 14},
    "tiktok":    {"heure": "19:00", "format": "Vidéo 9:16",
                  "lien_cliquable": False, "nb_tags": 5},
    "linkedin":  {"heure": "08:00", "format": "Vidéo native 9:16",
                  "lien_cliquable": True,  "nb_tags": 4},
    # YouTube est le seul réseau où la vidéo se cherche. Les quatre autres la
    # poussent dans un fil ; ici quelqu'un tape une question. D'où un titre
    # porteur de la requête, une description longue, et des balises.
    "youtube":   {"heure": "10:00", "format": "Short 9:16",
                  "lien_cliquable": True,  "nb_tags": 12},
}

# Mots-dièse toujours présents, par réseau. Sur TikTok on reste large : l'algo
# y travaille sur le son et le début de vidéo, pas sur des dièses de niche.
SOCLE = {
    "facebook":  ["restaurant", "restaurateur", "gestionrestaurant", "foodeatup"],
    "instagram": ["restaurant", "restaurateur", "gestionrestaurant", "foodeatup",
                  "logicielrestaurant", "vieDeResto", "cuisine", "hotellerierestauration"],
    "tiktok":    ["restaurant", "resto", "foodeatup"],
    "linkedin":  ["restauration", "foodeatup"],
    "youtube":   ["Shorts", "restaurant", "restaurateur", "foodeatup",
                  "logicielrestaurant", "gestionrestaurant"],
}

MODULES = {
    "Service":          {"tags": ["service", "salle", "commandes", "coupdefeu"],
                         "cles": ["prise de commande", "commandes multicanal", "service en salle"],
                         "benefice": "moins de tickets perdus entre la salle et le pass"},
    "StockVision":      {"tags": ["gestiondestock", "stockvision", "inventaire", "antigaspi", "coutmatiere"],
                         "cles": ["gestion de stock restaurant", "coût matière", "inventaire cuisine"],
                         "benefice": "un stock juste et une marge qu'on voit avant de fixer le prix"},
    "Caisse POS":       {"tags": ["caisse", "pos", "encaissement", "tpe"],
                         "cles": ["logiciel de caisse restaurant", "caisse enregistreuse", "encaissement"],
                         "benefice": "une caisse qui ferme juste, tous les soirs"},
    "Configuration":    {"tags": ["parametrage", "organisation", "demarrage"],
                         "cles": ["paramétrage restaurant", "configuration logiciel restaurant"],
                         "benefice": "une seule saisie qui alimente tout le reste"},
    "Marketing":        {"tags": ["marketingrestaurant", "avisgoogle", "ereputation", "fidelisation"],
                         "cles": ["marketing restaurant", "avis clients", "fidélisation restaurant"],
                         "benefice": "une salle qui se remplit avant l'ouverture"},
    "Comptabilité":     {"tags": ["comptabilite", "facturation", "rentabilite", "tva"],
                         "cles": ["comptabilité restaurant", "facturation restaurant", "rentabilité"],
                         "benefice": "des chiffres à jour sans ressaisir une ligne"},
    "PrediBot":         {"tags": ["predibot", "iarestaurant", "previsions", "datarestaurant"],
                         "cles": ["prévision de ventes restaurant", "IA restaurant", "pilotage"],
                         "benefice": "voir venir la journée au lieu de la subir"},
    "Réservation":      {"tags": ["reservation", "plandesalle", "noshow"],
                         "cles": ["logiciel de réservation restaurant", "plan de salle", "no-show"],
                         "benefice": "un plan de salle qui reflète la réalité, minute par minute"},
    "Mon Site":         {"tags": ["sitewebrestaurant", "commandeenligne", "clickandcollect"],
                         "cles": ["site web restaurant", "commande en ligne", "click and collect"],
                         "benefice": "un site qui prend des commandes, pas une carte de visite"},
    "KDS":              {"tags": ["kds", "cuisine", "brigade", "pass"],
                         "cles": ["écran cuisine", "KDS restaurant", "organisation cuisine"],
                         "benefice": "une cuisine qui sait quoi sortir, et quand"},
    "HubRise":          {"tags": ["hubrise", "livraison", "uberEats", "deliveroo"],
                         "cles": ["intégration livraison", "HubRise", "plateformes de livraison"],
                         "benefice": "plus de tablette à surveiller dans un coin"},
    "HACCP":            {"tags": ["haccp", "hygiene", "tracabilite", "normes"],
                         "cles": ["HACCP restaurant", "traçabilité", "contrôle hygiène"],
                         "benefice": "un contrôle qui se passe bien, parce que tout est déjà tracé"},
    "Équipe & Planning":{"tags": ["planning", "rh", "equipe", "pointage"],
                         "cles": ["planning restaurant", "gestion d'équipe", "pointage"],
                         "benefice": "des plannings faits en vingt minutes, pas en deux soirées"},
    "Caroline":         {"tags": ["agentvocal", "iarestaurant", "reservation"],
                         "cles": ["agent vocal restaurant", "répondeur intelligent"],
                         "benefice": "le téléphone qui répond même en plein coup de feu"},
}
DEFAUT = {"tags": ["logicielrestaurant"], "cles": ["logiciel restaurant"],
          "benefice": "du temps repris sur l'administratif"}

TEL = "06 14 18 92 25"
SITE = "foodeatup.com"

# Le lien public des publications. Il ne pointe JAMAIS sur le Drive : ces liens
# sont internes à la production, ils exposent l'arborescence de travail et ne
# survivraient pas à un partage large. Le Drive sert à découper le screencast,
# rien de plus — il ne sort pas de l'usine.
LIEN_PUBLIC = "https://site.foodeatup.com/"


def lien_public(ep):
    """Ce qu'on met dans un post. Toujours une adresse publique."""
    return LIEN_PUBLIC

# --- Le titre en trois mots de la vignette ------------------------------------
# Trois mots, pas quatre : au-delà, sur une vignette lue au pouce sur un
# téléphone, plus personne ne lit la troisième ligne.
VIDES = {"de", "des", "du", "la", "le", "les", "un", "une", "en", "et", "à",
         "au", "aux", "sur", "son", "sa", "ses", "ce", "cette", "d", "l", "pour"}
COURT = {"Équipe & Planning": "PLANNING", "Caisse POS": "CAISSE",
         "StockVision": "STOCK", "Mon Site": "SITE", "Comptabilité": "COMPTA",
         "Configuration": "RÉGLAGES", "Réservation": "RÉSA"}


def trois_mots(ep):
    """Le titre de la vignette, tiré du chapitre — c'est ce que la vidéo montre.

    Trois mots au plus, deux si le chapitre n'en dit pas davantage. Une première
    version complétait à trois en collant le nom du module, ce qui produisait des
    titres faux en français (« TON CONFIGURER CAISSE ») : deux mots justes valent
    mieux que trois mots cassés.

    Les chapitres énumèrent souvent trois actions (« Ajouter, Supprimer, Modifier
    un équipement »). On garde alors le segment qui tient en trois mots plutôt que
    les trois premiers mots de la phrase, qui donneraient « AJOUTER SUPPRIMER
    MODIFIER » — trois verbes et aucun objet.
    """
    chap = re.sub(r"^\d+\s*-\s*", "", ep["chapitre"]).strip()
    segments = [s.strip() for s in re.split(r"[,;&/]", chap) if s.strip()]
    # le segment le plus informatif qui tient en trois mots
    tenant = [s for s in segments if len(s.split()) <= 3]
    choix = max(tenant, key=lambda s: len(s.split())) if tenant else segments[0]
    mots = choix.split()
    if len(mots) > 3:
        mots = [m for m in mots if m.lower() not in VIDES][:3]
    return " ".join(m.upper() for m in mots)


# --- La direction artistique, saison par saison -------------------------------
# Chaque saison a son décor et sa lumière. Sans ça, 150 vignettes du même chef
# sur le même fond deviennent une bouillie : on ne distingue plus une saison
# d'une autre dans une grille.
SAISONS_DA = {
    1: {"decor": "une salle de restaurant en plein service, tables dressées, "
                 "clients flous en arrière-plan",
        "lumiere": "lumière chaude de fin de journée, reflets dorés"},
    2: {"decor": "un bureau d'arrière-salle, classeurs, tickets de caisse, "
                 "calculatrice, cartons de livraison",
        "lumiere": "lumière rasante de néon adouci, ambiance fin de mois"},
    3: {"decor": "une cuisine professionnelle en pleine brigade, inox, "
                 "passe-plat, plannings punaisés au mur",
        "lumiere": "lumière blanche et nette de cuisine, vapeur légère"},
    4: {"decor": "la devanture et la terrasse du restaurant, ardoise, "
                 "téléphone à la main, avis clients affichés",
        "lumiere": "plein jour, lumière naturelle franche"},
    5: {"decor": "le restaurant vide au petit matin, chaises encore sur les "
                 "tables, tablette posée sur le comptoir",
        "lumiere": "lumière bleutée de l'aube qui entre par la vitrine"},
}

# L'arc de chaque épisode est le même : le chaos, puis le calme. Le chef n'est
# jamais paniqué — il a déjà vu ça cent fois. Quatre nuances suffisent, prises
# de façon déterministe pour qu'un même épisode garde toujours la sienne.
EXPRESSIONS = [
    "l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé",
    "un sourire en coin, parfaitement serein au milieu du désastre",
    "faussement dépité, la main sur le front, mais l'œil qui rit",
    "l'air satisfait de celui qui sait que le problème est déjà réglé",
]


def mots_cles(ep):
    m = MODULES.get(ep["module"], DEFAUT)
    chap = re.sub(r"^\d+\s*-\s*", "", ep["chapitre"]).strip().lower()
    return list(dict.fromkeys(m["cles"] + [chap, f"{ep['module'].lower()} restaurant"]))


def tags(ep, reseau):
    m = MODULES.get(ep["module"], DEFAUT)
    n = RESEAUX[reseau]["nb_tags"]
    return list(dict.fromkeys(SOCLE[reseau] + m["tags"]))[:n]


def premiere_phrase(t):
    p = re.split(r"(?<=[.!?])\s+", t.strip())
    return p[0] if p else t


def legende(ep, reseau):
    """Le texte prêt à coller, sans les mots-dièse (ils sont à part)."""
    a, p, r = ep["accroche"], ep["punchline"], ep["resume"]
    lien = lien_public(ep)
    benef = MODULES.get(ep["module"], DEFAUT)["benefice"]

    if reseau == "facebook":
        bloc = [f"{a} {p}", "", r, ""]
        if lien:
            bloc.append(f"👉 Tout FoodEatUp : {lien}")
        bloc.append(f"Une démo ? {TEL} — {SITE}")
        return "\n".join(bloc)

    if reseau == "instagram":
        # Pas d'URL : Instagram ne la rend pas cliquable, elle ne ferait
        # qu'encombrer la légende.
        return "\n".join([a, p, "", r, "",
                          "Tout est expliqué sur notre site — lien en bio.",
                          f"Une démo ? {TEL}"])

    if reseau == "tiktok":
        # Deux lignes et une promesse. Au-delà, personne ne déplie.
        return "\n".join([f"{a} 😅", p, "", premiere_phrase(r)])

    if reseau == "youtube":
        return description_youtube(ep)

    # LinkedIn : on parle à un exploitant, pas à un abonné. Le bénéfice
    # d'abord, l'anecdote ensuite.
    bloc = [f"{a}", "", r, "",
            f"Concrètement : {benef}.", ""]
    if lien:
        bloc.append(f"En savoir plus : {lien}")
    bloc.append(f"Une démo ? {TEL} — {SITE}")
    return "\n".join(bloc)


def titre_youtube(ep):
    """Une requête, pas un slogan. YouTube est un moteur de recherche."""
    chap = re.sub(r"^\d+\s*-\s*", "", ep["chapitre"]).strip()
    chap = chap[0].upper() + chap[1:] if chap else chap
    t = f"{chap} — {ep['module']} | FoodEatUp"
    if len(t) > 95:                      # au-delà, YouTube coupe dans le titre
        t = f"{chap} | FoodEatUp"[:95]
    return t


def description_youtube(ep):
    lien = lien_public(ep)
    benef = MODULES.get(ep["module"], DEFAUT)["benefice"]
    bloc = [f"{ep['accroche']} {ep['punchline']}", "",
            ep["resume"], "",
            f"Concrètement : {benef}.", "",
            "— — —", ""]
    if lien:
        bloc += [f"🔗 {lien}", ""]
    bloc += [f"📞 Une démo ? {TEL}",
             f"🌐 {SITE}", "",
             f"Série « Le Coup de Feu » — saison {ep['saison']}, épisode {ep['numero']}.",
             f"Module {ep['module']} · Chapitre : {ep['chapitre']}", "",
             "FoodEatUp est le logiciel qui réunit la caisse, le stock, les "
             "plannings, l'HACCP et le marketing d'un restaurant au même endroit.",
             ""]
    return "\n".join(bloc)


def prompt_vignette(ep):
    """Le prompt d'image, prêt à coller. Un par épisode, jamais générique."""
    da = SAISONS_DA[ep["saison"]]
    expr = EXPRESSIONS[sum(ord(c) for c in ep["id"]) % len(EXPRESSIONS)]
    return (
        "Photo réaliste, cadrage vertical 9:16. "
        "Le chef de l'image de référence — MÊME visage, même barbe, même toque "
        "blanche, même veste de cuisine blanche, même tablier blanc au logo "
        "FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. "
        f"Son expression : {expr}. "
        f"Scène : {ep['titre'].lower()}. {ep['accroche']} "
        f"Décor : {da['decor']}. {da['lumiere']}. "
        "Le chef occupe les deux tiers droits du cadre, en plan poitrine, "
        "l'élément comique est visible à gauche. "
        "Bande crème #FCF9E6 en haut du cadre sur un cinquième de la hauteur, "
        f"portant UNIQUEMENT le texte « {trois_mots(ep)} » en typographie "
        "arrondie très grasse, bleu marine #0F1A23, centré. "
        "Aucun autre texte, aucun logo ajouté, pas de filigrane, "
        "pas de bordure décorative."
    )


def cta(ep, reseau):
    if not lien_public(ep):
        return "Demander une démo"
    return {"facebook": "Découvrir FoodEatUp",
            "instagram": "Tout est en bio",
            "tiktok": "Lien en bio",
            "linkedin": "Découvrir FoodEatUp",
            "youtube": "Découvrir FoodEatUp"}[reseau]


def main():
    src = os.path.join(SOCIAL, "data", "series.json")
    d = json.load(open(src))
    comptes = {r["slug"]: r["compte"] for r in d["reseaux"]}
    if "youtube" not in comptes:
        d["reseaux"].append({"slug": "youtube", "nom": "YouTube",
                             "compte": "@FoodEatUp",
                             "url": "https://www.youtube.com/@FoodEatUp",
                             "couleur": "#FF0000"})
        comptes["youtube"] = "@FoodEatUp"
    n = 0
    for s in d["series"]:
        for sa in s["saisons"]:
            for ep in sa["episodes"]:
                pub = {}
                for res, cfg in RESEAUX.items():
                    anc = ep["reseaux"].get(
                        res, {"statut": "a_venir", "date": ep.get("datePrevue")})
                    pub[res] = {
                        "statut": anc["statut"],
                        "date": anc["date"],
                        "heure": cfg["heure"],
                        "compte": comptes[res],
                        "format": cfg["format"],
                        "legende": legende(ep, res),
                        "hashtags": tags(ep, res),
                        "cta": cta(ep, res),
                        "lienCta": lien_public(ep) if cfg["lien_cliquable"] else None,
                        "motsCles": mots_cles(ep),
                    }
                    if res == "youtube":
                        pub[res]["titre"] = titre_youtube(ep)
                    if anc.get("url"):
                        pub[res]["url"] = anc["url"]
                    n += 1
                ep["reseaux"] = pub
                ep["troisMots"] = trois_mots(ep)
                ep["promptVignette"] = prompt_vignette(ep)
                ep["posterUrl"] = (
                    f"/posters/{ep['id']}.jpg"
                    if os.path.exists(os.path.join(SOCIAL, "public", "posters", ep["id"] + ".jpg"))
                    else None)
    json.dump(d, open(src, "w"), ensure_ascii=False, indent=2)
    print(f"{n} publications écrites")


if __name__ == "__main__":
    main()
