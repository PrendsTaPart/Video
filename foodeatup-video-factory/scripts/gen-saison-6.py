#!/usr/bin/env python3
"""Injecte la saison 6 dans data/series.json, avec sa propre voix.

Pourquoi un script à part plutôt qu'une branche dans gen-publications.py.

Les cinq premières saisons parlent du logiciel : leurs légendes disent « ce que
ça change dans ton resto », leur CTA est « Découvrir FoodEatUp », leur titre
YouTube est une requête sur un module. La saison 6 fait exactement l'inverse —
elle publie ce qu'un restaurant publierait, et ne cite le logiciel qu'une fois,
à la fin. Brancher ça dans le générateur des 150 aurait demandé un `if saison ==
6` dans chacune des sept fonctions d'écriture ; deux voix, deux fichiers.

`gen-publications.py` saute donc la saison 6, et c'est écrit dans son code.

La règle qui commande tout le reste : **une seule phrase de logiciel par
épisode, après le contenu, jamais avant**. Elle vit dans le champ `logiciel` de
content/saison-6.py et n'apparaît qu'en fin de légende.
"""
import importlib.util, json, os, re, unicodedata

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOCIAL = os.path.join(os.path.dirname(R), "foodeatup-social")

sp = importlib.util.spec_from_file_location("s6", os.path.join(R, "content", "saison-6.py"))
s6 = importlib.util.module_from_spec(sp); sp.loader.exec_module(s6)

# Le restaurant, pas l'éditeur. Ces coordonnées sont celles de l'enseigne.
SITE_RESTO = "https://site.foodeatup.com/"
TEL = "06 14 18 92 25"

HEURES = {"facebook": "12:00", "instagram": "18:30", "tiktok": "19:00",
          "linkedin": "08:00", "youtube": "10:00"}
FORMATS = {"facebook": "Vidéo native 9:16", "instagram": "Reel 9:16",
           "tiktok": "Vidéo 9:16", "linkedin": "Vidéo native 9:16",
           "youtube": "Short 9:16"}
CLIQUABLE = {"facebook": True, "instagram": False, "tiktok": False,
             "linkedin": True, "youtube": True}

# Les mots-dièse d'un restaurant, pas d'un éditeur de logiciel.
TAGS_ARC = {
    "La carte à l'écran": ["restaurant", "faitmaison", "cuisine", "carte"],
    "Les événements":     ["restaurant", "soiree", "sortie", "reservation"],
    "Les coulisses":      ["restaurant", "coulisses", "metier", "equipe"],
    "Le client":          ["restaurant", "client", "accueil", "service"],
    "La maison":          ["restaurant", "commerce", "quartier", "maison"],
}
TAGS_SOCLE = ["foodeatup", "restaurateur", "rapidocms", "iarestaurant"]

# La saison 6 ne se filme pas dans le même monde que les cinq autres : le décor
# suit l'arc, pas la saison, parce que c'est le restaurant qu'on montre.
DECORS = {
    "La carte à l'écran": ("le plat en très gros plan sur le pass, vapeur et "
                           "reflets", "lumière rasante de studio culinaire"),
    "Les événements":     ("la salle préparée pour le soir, tables dressées, "
                           "lumières basses", "lumière chaude de début de service"),
    "Les coulisses":      ("la cuisine et les réserves avant l'ouverture, inox "
                           "nu, cagettes", "lumière crue du matin"),
    "Le client":          ("une table en salle vue à hauteur de convive, "
                           "verres et nappe", "lumière douce de fin de repas"),
    "La maison":          ("la devanture et le comptoir, ardoise et carte "
                           "affichée", "plein jour, lumière franche"),
}


def slug(t):
    t = unicodedata.normalize("NFD", t)
    t = "".join(c for c in t if unicodedata.category(c) != "Mn").lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def trois_mots(e):
    """Deux ou trois mots pris dans le titre — ce que la vidéo montre."""
    vides = {"le", "la", "les", "un", "une", "de", "des", "du", "qu", "qui",
             "que", "on", "ce", "en", "et", "a", "à", "au", "aux", "sans", "d"}
    mots = [m for m in re.findall(r"[\w'À-ÿ]+", e["titre"])
            if m.lower().strip("'") not in vides]
    return " ".join(mots[:3]).upper()


# --- La brigade d'agents ------------------------------------------------------
# Chaque épisode est porté par un des dix végé-fruités, qui tient un poste du
# restaurant ET pilote un outil réel via son MCP. Le rapprochement suit l'arc :
# un épisode de coulisses est porté par celui qui ouvre les livres, un épisode
# d'événement par celle qui publie.
#
# Ces cinq lignes doivent rester d'accord avec src/data/agents.ts du site. Deux
# tables, un seul sujet : si l'une bouge, l'autre suit.
AGENT_PAR_ARC = {
    "La carte à l'écran": ("La Fraise", "MCP Higgsfield",
                           "elle écrit le plan et le fait rendre en dix secondes"),
    "Les événements":     ("La Betterave", "MCP RapidoCMS",
                           "elle programme les cinq réseaux aux bons créneaux"),
    "Les coulisses":      ("L'Oignon", "MCP FoodEatUp",
                           "il ouvre les livres : ventes, stock, réservations"),
    "Le client":          ("Don Citrone", "MCP FoodEatUp",
                           "il relie ce qui est publié à ce qui arrive en salle"),
    "La maison":          ("Le Brocoli", "MCP RapidoCMS",
                           "il tient le calendrier et propose quoi publier, quand"),
}

# La chaîne complète, dite en une phrase. Elle ne change pas d'un épisode à
# l'autre : c'est le refrain de la saison.
CHAINE = ("Claude, branché sur quatre outils — FoodEatUp pour les données du "
          "restaurant, Higgsfield pour l'image, ElevenLabs pour la voix, "
          "RapidoCMS pour la publication.")


def legende(e, reseau):
    """Le restaurant parle. La méthode n'a droit qu'à la fin — sauf sur LinkedIn."""
    a, p, corps = e["accroche"], e["punchline"], e["publie"]
    nom, mcp, fait = AGENT_PAR_ARC[e["arc"]]

    if reseau == "facebook":
        b = [f"{a} {p}", "", corps, "",
             f"Cette vidéo, personne ne l'a montée à la main : {nom} s'en est "
             f"chargée — {fait} — puis toute la brigade a suivi.", "",
             f"👉 {e['cta']} : {SITE_RESTO}", f"Une table ? {TEL}"]
    elif reseau == "instagram":
        b = [a, p, "", corps, "",
             f"Fabriquée par {nom} et les neuf autres. Aucun logiciel de montage.",
             f"{e['cta']} — lien en bio.", f"Une table ? {TEL}"]
    elif reseau == "tiktok":
        b = [a, p, "", corps.split(".")[0].strip() + ".", "",
             f"Montée par une IA. Sérieusement. ({nom}, {mcp})"]
    elif reseau == "linkedin":
        # Sur LinkedIn on s'adresse à un confrère restaurateur : c'est le seul
        # réseau où la méthode intéresse autant que le plat. On la déplie.
        b = [a, "", corps, "",
             "Comment c'est fabriqué, sans agence et sans community manager :", "",
             f"• {nom} ({mcp}) — {fait}.",
             f"• Puis la brigade : la voix, le montage, la relecture, la mise en ligne.",
             f"• Le tout dirigé en écrivant, depuis {CHAINE}", "",
             f"Pour cet épisode : {e['logiciel']}", "",
             f"{e['cta']} : {SITE_RESTO}", f"Une table ? {TEL}"]
    else:
        b = [f"{a} {p}", "", corps, "", "— — —", "",
             "COMMENT CETTE VIDÉO A ÉTÉ FAITE", "",
             f"Une équipe d'agents IA — la Brigade Végé-Fruitée — dirigée en "
             f"écrivant. Sur cet épisode, c'est {nom} qui ouvre le bal ({mcp}) : "
             f"{fait}. Les autres suivent : la voix, le montage, la relecture "
             "avant publication, la mise en ligne, le bilan.", "",
             f"La chaîne : {CHAINE}", "",
             f"Pour cet épisode : {e['logiciel']}", "",
             "— — —", "",
             f"🔗 {SITE_RESTO}", f"📞 {TEL}", "",
             f"Saison 6 « L'orchestration du restaurant » — épisode {e['n'] - 150} "
             f"sur 30. Arc : {e['arc']}. Rôle à l'écran : {e['role']}.", ""]
    return "\n".join(b)


def titre_youtube(e):
    t = f"{e['titre']} — {e['arc']} | FoodEatUp"
    return t if len(t) <= 95 else f"{e['titre']} | FoodEatUp"[:95]


def prompt_vignette(e):
    decor, lumiere = DECORS[e["arc"]]
    return (
        "Photo réaliste, cadrage vertical 9:16. "
        "Le chef de l'image de référence — MÊME visage, même barbe, même toque "
        "blanche, même veste de cuisine blanche, même tablier blanc au logo "
        "FoodEatUp bleu. Ne change ni ses traits ni sa morphologie. "
        f"Il joue ici le rôle : {e['role'].lower()}. "
        f"Scène : {e['titre'].lower()}. {e['accroche']} "
        f"Décor : {decor}. {lumiere}. "
        "C'est le RESTAURANT qui est le sujet : le plat, la salle ou l'équipe "
        "occupent les deux tiers du cadre, le chef est présent mais pas au "
        "centre. Aucun écran de logiciel visible. "
        "Bande bleu RapidoCMS #03A9F5 en haut du cadre sur un cinquième de la "
        f"hauteur, portant UNIQUEMENT le texte « {trois_mots(e)} » en "
        "typographie arrondie très grasse, blanc, centré. "
        "Aucun autre texte, aucun logo ajouté, pas de filigrane, pas de "
        "bordure décorative."
    )


def main():
    src = os.path.join(SOCIAL, "data", "series.json")
    d = json.load(open(src))
    serie = d["series"][0]
    saison = next((s for s in serie["saisons"] if s["numero"] == 6), None)
    if saison is None:
        saison = {"numero": 6, "titre": "L'orchestration du restaurant",
                  "pitch": "Le restaurant devient le sujet et le logiciel passe "
                           "derrière : trente contenus qu'un restaurateur peut "
                           "publier tel quel. RapidoCMS mène, FoodEatUp est "
                           "l'enseigne.",
                  "episodes": []}
        serie["saisons"].append(saison)

    anciens = {e["id"]: e for e in saison["episodes"]}
    episodes = []
    for e in s6.EPISODES:
        eid = f"EP{e['n']}"
        anc = anciens.get(eid, {})
        reseaux = {}
        for res in HEURES:
            a = (anc.get("reseaux") or {}).get(res, {})
            reseaux[res] = {
                "statut": a.get("statut", "a_venir"),
                "date": a.get("date"),
                "heure": HEURES[res],
                "compte": {"facebook": "FoodEatUp", "instagram": "foodeatup.cocuisinage",
                           "tiktok": "foodeatup", "linkedin": "FoodEatUp",
                           "youtube": "@FoodEatUp"}[res],
                "format": FORMATS[res],
                "legende": legende(e, res),
                "hashtags": TAGS_SOCLE + TAGS_ARC[e["arc"]],
                "cta": e["cta"],
                "lienCta": SITE_RESTO if CLIQUABLE[res] else None,
                "motsCles": [e["arc"].lower(), e["format"].lower(),
                             "communication restaurant", "agent ia restaurant",
                             "rapidocms", "mcp claude restaurant"],
            }
            if res == "youtube":
                reseaux[res]["titre"] = titre_youtube(e)
        episodes.append({
            "id": eid, "numero": e["n"], "saison": 6,
            "slug": f"ep{e['n']}-{slug(e['titre'])}",
            "titre": e["titre"], "module": e["arc"], "chapitre": e["format"],
            "role": e["role"], "arc": e["arc"],
            "accroche": e["accroche"], "punchline": e["punchline"],
            "resume": e["publie"], "ressort": e["ressort"], "logiciel": e["logiciel"],
            "statut": anc.get("statut", "a_produire"),
            "dureeSecondes": anc.get("dureeSecondes"),
            "videoUrl": anc.get("videoUrl"),
            "tutoriel": None, "tutorielModuleUrl": None,
            "higgsfield": anc.get("higgsfield",
                                  {"videoSourceUrl": None, "source": None,
                                   "duree": "10 s", "format": "vertical 9:16"}),
            "masterRapidoUrl": anc.get("masterRapidoUrl"),
            "posterUrl": anc.get("posterUrl"),
            "troisMots": trois_mots(e),
            "promptVignette": prompt_vignette(e),
            "datePrevue": anc.get("datePrevue"),
            "reseaux": reseaux,
        })
    saison["episodes"] = episodes
    json.dump(d, open(src, "w"), ensure_ascii=False, indent=2)
    print(f"saison 6 : {len(episodes)} épisodes, {len(episodes) * 5} publications")


if __name__ == "__main__":
    main()
