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
}

# Mots-dièse toujours présents, par réseau. Sur TikTok on reste large : l'algo
# y travaille sur le son et le début de vidéo, pas sur des dièses de niche.
SOCLE = {
    "facebook":  ["restaurant", "restaurateur", "gestionrestaurant", "foodeatup"],
    "instagram": ["restaurant", "restaurateur", "gestionrestaurant", "foodeatup",
                  "logicielrestaurant", "vieDeResto", "cuisine", "hotellerierestauration"],
    "tiktok":    ["restaurant", "resto", "foodeatup"],
    "linkedin":  ["restauration", "foodeatup"],
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
    lien = ep.get("tutorielUrl")
    benef = MODULES.get(ep["module"], DEFAUT)["benefice"]

    if reseau == "facebook":
        bloc = [f"{a} {p}", "", r, ""]
        if lien:
            bloc.append(f"👉 Le tutoriel complet : {lien}")
        bloc.append(f"Une démo ? {TEL} — {SITE}")
        return "\n".join(bloc)

    if reseau == "instagram":
        # Pas d'URL : Instagram ne la rend pas cliquable, elle ne ferait
        # qu'encombrer la légende.
        return "\n".join([a, p, "", r, "",
                          "Le pas-à-pas complet est dans notre Academy — lien en bio.",
                          f"Une démo ? {TEL}"])

    if reseau == "tiktok":
        # Deux lignes et une promesse. Au-delà, personne ne déplie.
        return "\n".join([f"{a} 😅", p, "", premiere_phrase(r)])

    # LinkedIn : on parle à un exploitant, pas à un abonné. Le bénéfice
    # d'abord, l'anecdote ensuite.
    bloc = [f"{a}", "", r, "",
            f"Concrètement : {benef}.", ""]
    if lien:
        bloc.append(f"Le tutoriel pas-à-pas : {lien}")
    bloc.append(f"Une démo ? {TEL} — {SITE}")
    return "\n".join(bloc)


def cta(ep, reseau):
    if not ep.get("tutorielUrl"):
        return "Demander une démo"
    return {"facebook": "Voir le tutoriel complet",
            "instagram": "Le pas-à-pas est en bio",
            "tiktok": "Tuto complet en bio",
            "linkedin": "Voir le tutoriel pas-à-pas"}[reseau]


def main():
    src = os.path.join(SOCIAL, "data", "series.json")
    d = json.load(open(src))
    comptes = {r["slug"]: r["compte"] for r in d["reseaux"]}
    n = 0
    for s in d["series"]:
        for sa in s["saisons"]:
            for ep in sa["episodes"]:
                pub = {}
                for res, cfg in RESEAUX.items():
                    anc = ep["reseaux"][res]
                    pub[res] = {
                        "statut": anc["statut"],
                        "date": anc["date"],
                        "heure": cfg["heure"],
                        "compte": comptes[res],
                        "format": cfg["format"],
                        "legende": legende(ep, res),
                        "hashtags": tags(ep, res),
                        "cta": cta(ep, res),
                        "lienCta": ep.get("tutorielUrl") if cfg["lien_cliquable"] else None,
                        "motsCles": mots_cles(ep),
                    }
                    if anc.get("url"):
                        pub[res]["url"] = anc["url"]
                    n += 1
                ep["reseaux"] = pub
                ep["posterUrl"] = (
                    f"/posters/{ep['id']}.jpg"
                    if os.path.exists(os.path.join(SOCIAL, "public", "posters", ep["id"] + ".jpg"))
                    else None)
    json.dump(d, open(src, "w"), ensure_ascii=False, indent=2)
    print(f"{n} publications écrites")


if __name__ == "__main__":
    main()
