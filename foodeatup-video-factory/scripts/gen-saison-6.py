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

def au_fil(nom):
    """Le nom du végé-fruité au milieu d'une phrase.

    La table donne les noms tels qu'on les écrit seuls — « La Fraise »,
    « L'Oignon ». Au fil d'une phrase parlée, cette majuscule sur l'article se
    voit et se lit comme une faute. On l'abaisse ; les noms sans article
    (« Tomate Man », « Don Citrone ») restent intacts.
    """
    for a in ("La ", "Le ", "L'"):
        if nom.startswith(a):
            return a.lower() + nom[len(a):]
    return nom


# Ce que chacun dit quand c'est LUI qui parle. La table BRIGADE décrit les
# agents à la troisième personne — c'est la bonne voix pour un plan Higgsfield
# ou une fiche. Dans un script HeyGen, le personnage se présente lui-même :
# « Moi c'est la Fraise, j'écris le plan » et non « elle écrit le plan ».
JE = {
    "fraise":         "j'écris le plan et je le fais rendre en dix secondes",
    "tomate":         "j'assemble les cinq segments et je contrôle avant de livrer",
    "ail":            "je tiens la carte à jour partout à la fois",
    "pomme-de-terre": "je donne la voix off de la série",
    "citron":         "je relie ce qui est publié à ce qui arrive en salle",
    "oignon":         "j'ouvre les livres : ventes, stock, réservations",
    "betterave":      "je programme les cinq réseaux aux bons créneaux",
    "brocoli":        "je tiens le calendrier et je propose quoi publier, quand",
    "carotte":        "je relis tout avant que ça sorte",
    "navet":          "je fais le compte de ce qui a marché",
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
    """Le plan d'ouverture. Marque RapidoCMS, végé-fruité en vedette.

    L'anatomie de la saison 6 n'est pas celle des cinq autres. Là-bas, le hook
    est un gag Higgsfield sous marque FoodEatUp et l'avatar explique un module.
    Ici, c'est RapidoCMS qui présente sa méthode : le hook, la signature de fin
    et les logos sont donc à sa charte, et c'est un végé-fruité qui porte le
    plan. Le chef reste présent — c'est son restaurant — mais il n'est plus le
    sujet : il est celui à qui on montre.
    """
    nom, mcp, fait = BRIGADE[e["agent"]]
    decor, lumiere = DECORS[e["arc"]]
    return (
        "Vertical 9:16, 10 secondes, 4K. PAS de texte incrusté, PAS de "
        "sous-titres, PAS de filigrane, PAS de logo dans l'image.\n\n"
        "IDENTITÉ VISUELLE : RapidoCMS. Bleu #03A9F5 présent dans le décor — "
        "un écran, une lumière, un objet — sans jamais former de logo. Tons "
        "clairs, blancs, gris #383838. Pas de crème, pas d'orange.\n\n"
        "DEUX personnages dans le même plan :\n"
        "— " + nom + ", personnage 3D stylisé de la Brigade Végé-Fruitée, EN "
        "VEDETTE, au premier plan, deux tiers du cadre. C'est le personnage "
        "qui agit : "
        "" + fait + " ;\n"
        "— le chef, PHOTORÉALISTE, veste blanche et tablier, en retrait dans "
        "son restaurant. Il regarde faire, il ne fait pas.\n\n"
        "Le mélange photo + 3D est assumé, comme un dessin animé posé dans une "
        "prise de vue réelle. Les ombres du personnage 3D suivent celles du "
        "décor.\n\n"
        "Décor : " + decor + ". " + lumiere + ".\n"
        "Action : " + e["publie"].split(".")[0].strip() + ".\n"
        "À 5 secondes, le geste aboutit et le chef réagit — surpris, puis "
        "convaincu.\n"
        "Deux dernières secondes : les deux regardent l'objectif côte à côte, "
        "immobiles.\n\n"
        "Audio : ambiance réelle du restaurant, un bip d'interface discret à "
        "5 secondes, aucun dialogue, pas de musique."
    )


def script_heygen(e):
    """Ce que dit le personnage HeyGen — et ce n'est plus le chef.

    Dans les cinq premières saisons, l'avatar est le chef et il explique une
    fonction du logiciel. Ici, l'avatar est LE VÉGÉ-FRUITÉ, monté en personnage
    HeyGen, et il explique comment fabriquer cet épisode-là. Le restaurateur
    n'apprend pas ce que fait un bouton : il apprend à produire sa vidéo.

    Vingt-cinq à trente mots. Au-delà, le montage accélère la parole et ça
    s'entend — mesuré dès la première saison.
    """
    nom, mcp, fait = BRIGADE[e["agent"]]
    return (
        f"Moi c'est {au_fil(nom)}. Sur cet épisode, {JE[e['agent']]}. Vous "
        f"me le demandez, ça part sur vos cinq réseaux ce soir."
    )


def kit(e):
    """Les quatre prompts à copier, avec leurs crochets.

    L'ordre est celui de la chaîne, et la répartition dit la saison : les deux
    premières étapes se passent CHEZ LE RESTAURATEUR — il filme, il fournit ses
    photos — les deux dernières sont RapidoCMS qui monte et publie.
    """
    nom, mcp, fait = BRIGADE[e["agent"]]
    hf = (prompt_higgsfield(e)
          .replace("son restaurant", "[TON RESTAURANT]")
          .replace("Action : ", "Action : chez [TON RESTAURANT], "))
    return [
        {
            "etape": 1,
            "titre": "Vos images",
            "outil": "Chez vous",
            "cote": "restaurant",
            "guide": e["agent"],
            "consigne": "Commencez par ce que vous avez déjà : dix secondes de "
                        "votre plat, de votre salle, de votre équipe. Filmé au "
                        "téléphone, à la verticale. Si vous n'avez rien, l'étape "
                        "suivante fabrique l'image à votre place.",
            "lien": "https://site.foodeatup.com/",
            "prompt": (
                "Ce que je fournis pour l'épisode [TON NUMÉRO] :\n\n"
                "— une vidéo verticale de 10 s de [TON PLAT], filmée au "
                "téléphone\n"
                "— une photo de [TON RESTAURANT] : la salle, la devanture ou le "
                "pass\n"
                "— mon logo, si j'en ai un\n\n"
                "Ce que je n'ai pas et que vous complétez avec vos gabarits : "
                "[CE QUI ME MANQUE]."
            ),
        },
        {
            "etape": 2,
            "titre": "Le plan d'ouverture",
            "outil": "Higgsfield",
            "cote": "restaurant",
            "guide": e["agent"],
            "consigne": "Si vous n'avez pas d'images, ce prompt les fabrique. "
                        "Remplacez ce qui est entre crochets, collez dans "
                        "Higgsfield, lancez. Dix secondes plus tard, vous avez "
                        "votre plan.",
            "lien": "https://higgsfield.ai/",
            "prompt": hf + "\n\nÀ remplacer : [TON RESTAURANT], [TON PLAT], "
                           "[TON PRÉNOM].",
        },
        {
            "etape": 3,
            "titre": "Le montage",
            "outil": "Claude Code",
            "cote": "rapidocms",
            "guide": "tomate",
            "consigne": "Le hook, la signature de fin et les logos sont ceux de "
                        "RapidoCMS — vous ne les fournissez pas, ils sont dans "
                        "le gabarit. Vos images occupent le centre. Vous "
                        "n'ouvrez aucun logiciel de montage.",
            "lien": "https://claude.com/claude-code",
            "prompt": (
                "Monte l'épisode [TON NUMÉRO] de ma série, gabarit RapidoCMS.\n\n"
                "— Plan d'ouverture : assets/hooks/[TON NUMÉRO].mp4\n"
                "— Personnage qui explique : assets/avatar/[TON NUMÉRO].mp4 "
                "(" + nom + ", avatar HeyGen)\n"
                "— Mes images de restaurant : assets/software/[TON NUMÉRO].mp4\n"
                "— Accroche à incruster : « " + e["accroche"] + " »\n"
                "— Punchline en voix off à 5,0 s : « " + e["punchline"] + " »\n\n"
                "Habillage : hook, signature de fin et logos en charte "
                "RapidoCMS — bleu #03A9F5, gris #383838, fond blanc. Pas de "
                "crème, pas d'orange.\n"
                "Anatomie : A 0→9,5 · sting RapidoCMS 9,5→18,5 · le personnage "
                "seul 18,5→28,5 · signature RapidoCMS 28,5→32,5 · sting de "
                "marque 32,5→37,5.\n"
                "Contrôle avant de me le rendre : 37,5 s, 1080×1920, -14 LUFS, "
                "crête sous -1 dBTP."
            ),
        },
        {
            "etape": 4,
            "titre": "La publication",
            "outil": "RapidoCMS",
            "cote": "rapidocms",
            "guide": "betterave",
            "consigne": "Une phrase, et les cinq réseaux sont programmés. Le "
                        "master part d'abord dans votre bibliothèque, puis en "
                        "ligne. Vous ne téléversez rien nulle part.",
            "lien": "https://cms.rapidosoftware.com/register",
            "prompt": (
                "Verse le master dans ma bibliothèque RapidoCMS, puis programme "
                "les cinq réseaux de [TON RESTAURANT] :\n\n"
                "— LinkedIn à 8 h, YouTube à 10 h, Facebook à 12 h, "
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
