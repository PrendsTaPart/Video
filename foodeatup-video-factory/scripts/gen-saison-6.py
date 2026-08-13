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
BRIGADE = {
    "fraise":         ("La Fraise", "MCP Higgsfield", "elle écrit le plan et le fait rendre en dix secondes"),
    "tomate":         ("Tomate Man", "Claude Code", "il assemble les cinq segments et contrôle avant de livrer"),
    "ail":            ("L'Ail", "MCP FoodEatUp", "il tient la carte à jour partout à la fois"),
    "pomme-de-terre": ("La Pomme de Terre", "MCP ElevenLabs", "elle donne la voix off de la série"),
    "citron":         ("Don Citrone", "MCP FoodEatUp", "il relie ce qui est publié à ce qui arrive en salle"),
    "oignon":         ("L'Oignon", "MCP FoodEatUp", "il ouvre les livres : ventes, stock, réservations"),
    "betterave":      ("La Betterave", "MCP RapidoCMS", "elle programme les cinq réseaux aux bons créneaux"),
    "brocoli":        ("Le Brocoli", "MCP RapidoCMS", "il tient le calendrier et propose quoi publier, quand"),
    "carotte":        ("La Carotte", "Claude Code", "elle relit tout avant que ça sorte"),
    "navet":          ("Le Navet", "MCP RapidoCMS", "il fait le compte de ce qui a marché"),
}

# La chaîne complète, dite en une phrase. Elle ne change pas d'un épisode à
# l'autre : c'est le refrain de la saison.
CHAINE = ("Claude, branché sur quatre outils — FoodEatUp pour les données du "
          "restaurant, Higgsfield pour l'image, ElevenLabs pour la voix, "
          "RapidoCMS pour la publication.")


def legende(e, reseau):
    """Le restaurant parle. La méthode n'a droit qu'à la fin — sauf sur LinkedIn."""
    a, p, corps = e["accroche"], e["punchline"], e["publie"]
    nom, mcp, fait = BRIGADE[e["agent"]]

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



# --- Ce qu'un restaurateur copie pour refaire l'épisode chez lui ---------------
#
# La saison 6 ne se contente pas de montrer le résultat : elle donne la recette.
# Chaque épisode porte donc trois prompts prêts à coller, dans l'ordre de la
# chaîne — Higgsfield, Claude Code, RapidoCMS.
#
# Les crochets sont le cœur du dispositif. `[TON PLAT]`, `[TON RESTAURANT]` :
# le restaurateur remplace, il n'écrit pas. Un prompt entièrement rédigé serait
# copié tel quel et publierait notre plat sur son compte ; un prompt vide le
# renverrait à la page blanche. Les crochets sont le seul entre-deux qui marche.
#
# Le plan Higgsfield de cette saison met DEUX personnages : le chef, photo
# réaliste, et son végé-fruité, en 3D, à côté de lui. C'est l'image de la saison
# — un restaurateur et son agent, dans la même pièce.

def prompt_higgsfield(e):
    nom, mcp, fait = BRIGADE[e["agent"]]
    decor, lumiere = DECORS[e["arc"]]
    return (
        "Vertical 9:16, 10 secondes, 4K. PAS de texte incrusté, PAS de "
        "sous-titres, PAS de filigrane, PAS de logo.\n\n"
        "DEUX personnages dans le même plan, et c'est voulu :\n"
        "— le chef, PHOTORÉALISTE, joue le rôle : " + e["role"].lower() + ". "
        "Veste blanche, tablier, il est chez lui dans son restaurant ;\n"
        "— " + nom + ", personnage 3D stylisé de la Brigade Végé-Fruitée, "
        "incrusté dans le même décor à côté de lui, à hauteur de comptoir. "
        "Il ne parle pas : il fait le geste de son métier — " + fait + ".\n\n"
        "Le mélange photo + 3D est assumé, comme un dessin animé posé dans une "
        "prise de vue réelle. Les ombres et la lumière du personnage 3D suivent "
        "celles du décor.\n\n"
        "Décor : " + decor + ". " + lumiere + ".\n"
        "Action : " + e["publie"].split(".")[0].strip() + ". "
        "À 5 secondes, le geste bascule et le personnage 3D réagit.\n"
        "Deux dernières secondes : les deux regardent l'objectif, immobiles.\n\n"
        "Audio : ambiance réelle du restaurant, aucun dialogue, pas de musique."
    )


def script_heygen(e):
    """La phrase que dit le chef à l'écran. 25 à 30 mots, jamais plus."""
    return e["publie"].split(".")[0].strip() + ". " + e["punchline"]


def kit(e):
    """Les trois prompts à copier, avec leurs crochets."""
    nom, mcp, fait = BRIGADE[e["agent"]]
    hf = prompt_higgsfield(e)
    hf = (hf.replace("son restaurant", "[TON RESTAURANT]")
            .replace("Action : ", "Action : chez [TON RESTAURANT], "))
    return [
        {
            "etape": 1,
            "titre": "Le plan comique",
            "outil": "Higgsfield",
            "guide": e["agent"],
            "consigne": "Remplace ce qui est entre crochets par ce qui est chez toi, "
                        "colle le tout dans Higgsfield, et lance. Dix secondes plus "
                        "tard tu as ton plan.",
            "lien": "https://higgsfield.ai/",
            "prompt": hf + "\n\nÉléments à remplacer : [TON RESTAURANT], "
                           "[TON PLAT], [TON PRÉNOM].",
        },
        {
            "etape": 2,
            "titre": "Le montage",
            "outil": "Claude Code",
            "guide": "tomate",
            "consigne": "Dépose ton plan et ton avatar dans le dépôt, puis écris "
                        "cette phrase à Claude Code. Tu n'ouvres aucun logiciel de "
                        "montage.",
            "lien": "https://claude.com/claude-code",
            "prompt": (
                "Monte l'épisode [TON NUMÉRO] de ma série.\n\n"
                "— Plan comique : assets/hooks/[TON NUMÉRO].mp4\n"
                "— Avatar : assets/avatar/[TON NUMÉRO].mp4\n"
                "— Écran du logiciel : assets/software/[TON NUMÉRO].mp4\n"
                "— Accroche à incruster : « " + e["accroche"] + " »\n"
                "— Punchline en voix off à 5,0 s : « " + e["punchline"] + " »\n\n"
                "Anatomie : A 0→9,5 · sting 9,5→18,5 · avatar seul 18,5→28,5 · "
                "signature 28,5→32,5 · sting de marque 32,5→37,5.\n"
                "Contrôle le master avant de me le rendre : 37,5 s, 1080×1920, "
                "-14 LUFS, crête sous -1 dBTP."
            ),
        },
        {
            "etape": 3,
            "titre": "La publication",
            "outil": "RapidoCMS",
            "guide": "betterave",
            "consigne": "Une phrase, et les cinq réseaux sont programmés. Tu ne "
                        "téléverses rien nulle part.",
            "lien": "https://cms.rapidosoftware.com/register",
            "prompt": (
                "Verse le master dans ma bibliothèque RapidoCMS, puis programme "
                "les cinq réseaux de [TON RESTAURANT] :\n\n"
                "— LinkedIn à 8 h, Facebook à 12 h, YouTube à 10 h, "
                "Instagram à 18 h 30, TikTok à 19 h\n"
                "— Légende : « " + e["accroche"] + " " + e["punchline"] + " » "
                "puis le corps, puis « [TON APPEL À L'ACTION] : [TON SITE] »\n"
                "— Mots-dièse : #restaurant #[TA VILLE] #[TA SPÉCIALITÉ]\n\n"
                "Rends-moi le lien de chaque publication."
            ),
        },
    ]


def prompt_vignette(e):
    """La vignette de la saison 6 : c'est le végé-fruité la vedette.

    Les saisons 1 à 5 mettent le chef en avant — c'est lui qui explique le
    logiciel. La saison 6 raconte une brigade d'agents qui fabrique la
    communication d'un restaurant : la vedette de l'image, c'est donc le
    personnage qui a fait le travail sur cet épisode-là, pas le chef.
    """
    decor, lumiere = DECORS[e["arc"]]
    nom, mcp, fait = BRIGADE[e["agent"]]
    return (
        "Illustration 3D, cadrage vertical 9:16, même style que l'image de "
        f"référence jointe. Le personnage de l'image de référence — {nom} — "
        "gardé À L'IDENTIQUE : mêmes proportions, mêmes couleurs, même tenue, "
        "même accessoire. Ne le redessine pas, ne change pas son visage. "
        "Il est LA VEDETTE de l'image et occupe les deux tiers du cadre, en "
        "premier plan, tourné vers l'objectif. "
        f"Ce qu'il fait ici : {fait}. "
        f"Scène : {e['titre'].lower()}. {e['accroche']} "
        f"Décor derrière lui : {decor}. {lumiere}. "
        "Le décor reste flou et discret — c'est un fond, pas un sujet. "
        "Aucun humain photoréaliste dans l'image, aucun écran de logiciel "
        "lisible. "
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
            "higgsfield": {**anc.get("higgsfield",
                                     {"videoSourceUrl": None, "source": None,
                                      "duree": "10 s", "format": "vertical 9:16"}),
                           "prompt": prompt_higgsfield(e)},
            "scriptHeygen": script_heygen(e),
            "kit": kit(e),
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
