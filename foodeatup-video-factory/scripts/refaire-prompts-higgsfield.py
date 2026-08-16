#!/usr/bin/env python3
"""Réécrit les prompts Higgsfield de l'inventaire en forme Seedance 2.5.

    python3 scripts/refaire-prompts-higgsfield.py --controle   (n'écrit rien)
    python3 scripts/refaire-prompts-higgsfield.py

Ce qui change
------------
**Le plan ne parle plus.** Seedance prononçait les répliques écrites entre
accolades, et le montage posait par-dessus la même phrase dite par ElevenLabs :
on entendait deux voix. On les retirait après coup par séparation de sources,
vingt secondes de calcul par plan pour défaire ce que le prompt avait demandé.
Il est plus simple de ne pas le demander. Les répliques restent dans le prompt
— le personnage les articule, lèvres et souffle justes — mais la piste ne porte
que l'ambiance du lieu.

**La direction de jeu disparaît.** « le débit d'un conteur qui connaît déjà la
fin » ne pilote plus rien quand la voix vient d'ailleurs. Ce qui reste utile au
modèle tient en une ligne : qui dit quoi, quand, et sans un son.

**Tout est en français.** Cent dix-huit prompts mélangeaient un en-tête anglais
et des répliques françaises. Les textes traduits sont dans
`content/prompts-scenes-fr.json`, un fichier relu à la main plutôt qu'une
traduction faite à la volée.

Les épisodes sans réplique gardent leur son
-------------------------------------------
Cent vingt-deux plans de la série comique ne parlent pas : leur story n'a pas
de voix off, le hook et la punchline y sont incrustés en texte. Le son du plan
est donc leur seule bande-son, et il est conservé tel quel — il n'y a aucun
doublon à régler chez eux.

Les accolades sont vérifiées
----------------------------
`veille-higgsfield.py` apparie un job Higgsfield à un épisode en comparant les
répliques entre accolades : c'est le seul lien fiable entre les deux. Le script
refuse d'écrire si une seule réplique a bougé d'un octet.
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from prompts_seedance import parties, repliques  # noqa: E402

R = pathlib.Path(__file__).resolve().parent.parent
SERIES = R.parent / "foodeatup-social" / "data" / "series.json"
LEXIQUE = R / "content" / "prompts-scenes-fr.json"

EN_TETE = (
    "Seedance 2.5. Vertical 9:16, 10 secondes, 1080p, 24 im/s. "
    "PAS de texte incrusté, PAS de sous-titres, PAS de filigrane, PAS de logo, "
    "AUCUNE légende gravée dans l'image."
)

# La direction de voix, réduite à ce qui pilote encore l'image. Le premier
# groupe capture tout ce qui précède l'accolade depuis la fin de phrase.
DIRECTION = re.compile(
    r"(?:(?<=[.!?])|(?<=\n)|^)\s*([^.!?{}\n]{5,160}?)\s*:\s*\{([^}]*)\}")

BRIGADE = ("La Fraise", "Tomate Man", "L'Ail", "Don Citrone", "La Betterave",
           "Le Brocoli", "La Pomme de Terre", "L'Oignon", "Le Navet", "La Carotte")


def locuteur(direction):
    """Qui dit la réplique, et d'où : hors champ, face caméra, ou dans le plan.

    Les cinquante et une directions du dépôt finissent toutes par nommer leur
    locuteur ; c'est ce nom qu'on garde, le reste étant du jeu d'acteur qui ne
    sert plus à rien une fois la voix enregistrée ailleurs.
    """
    b = direction.lower()

    # Les formes que ce script produit lui-même : il est relancé après chaque
    # lot de traduction, il doit donc savoir relire sa propre sortie.
    deja = re.search(r"^À cet instant, (.+?) sera posé au montage", direction)
    if deja:
        return deja.group(1)[0].upper() + deja.group(1)[1:], "hors"
    deja = re.search(r"^(.+?) articule cette phrase (face caméra|sans regarder)",
                     direction)
    if deja:
        return deja.group(1), "camera" if "face" in deja.group(2) else "plan"

    if "off-screen narrator" in b or "conteur" in b:
        return "Le conteur", "hors"
    if "celle du chef" in b:
        return "Le chef", "hors"
    if "accent neutre, voix grave et posée, hors champ" in b:
        return "La voix off", "hors"
    for p in BRIGADE:
        if p.lower() in b:
            return p, "camera"
    if b.endswith("le chef, face caméra"):
        return "Le chef", "camera"
    for fin, nom in (("les quatre", "Le personnage"), ("le serveur", "Le serveur"),
                     ("le patron", "Le patron"), ("le client", "Le client"),
                     ("one of the characters", "Le personnage")):
        if b.endswith(fin):
            return nom, "plan"
    if b.endswith("the chef") or b.endswith("le chef"):
        return "Le chef", "plan"
    raise ValueError(f"direction de voix non reconnue : {direction!r}")


def pose_replique(qui, ou, texte):
    """La ligne qui pose une réplique. Jouée à l'image, muette à l'oreille.

    Hors champ il n'y a pas de bouche à animer : la réplique n'est plus qu'un
    repère de minutage pour la voix qu'on posera au montage. On le dit ainsi,
    plutôt que de demander au modèle de jouer une chose qu'il ne filme pas.
    """
    if ou == "hors":
        return (f"À cet instant, {qui.lower()} sera posé au montage — "
                f"ne produire aucun son ici : {{{texte}}}")
    place = "face caméra" if ou == "camera" else "sans regarder l'objectif"
    return (f"{qui} articule cette phrase {place}, sans qu'aucun son n'en "
            f"sorte : {{{texte}}}")


def sans_direction(corps):
    """Remplace chaque « <direction> : {réplique} » par la forme neutre."""
    def remplace(m):
        qui, ou = locuteur(m.group(1).strip())
        return " " + pose_replique(qui, ou, m.group(2))
    texte = re.sub(r"\s+", " ", DIRECTION.sub(remplace, corps)).strip()
    # Quelques mises en scène d'origine finissent par « immobiles.. » : le
    # générateur y ajoutait un point sans vérifier qu'il y en avait déjà un.
    return re.sub(r"\.{2,}(?!\.)", ".", texte)


def ambiances(ligne_son):
    """Les ambiances d'un bloc de son, ancienne forme ou nouvelle.

    L'ancienne les listait entre chevrons — « Sound design: <a> <b> » — la
    nouvelle les énumère en clair. Le script étant relancé à chaque lot de
    traduction, il doit savoir relire les deux, sinon la seconde passe perd
    l'ambiance du plan et la remplace par une valeur par défaut.
    """
    ligne_son = ligne_son or ""
    m = re.search(r"son réel du lieu\s*:\s*(.+?)\.\n", ligne_son)
    if m:
        return [x.strip() for x in m.group(1).split(",") if x.strip()]
    return [x.strip() for x in re.findall(r"<([^>]*)>", ligne_son)]


# Une ambiance qui contient une voix contredit le bloc AUDIO : huit plans
# demandaient « a calm continuous French voice listing things ». Ces éléments
# sont retirés, la voix venant désormais d'ElevenLabs.
VOIX_DANS_AMBIANCE = re.compile(r"\b(voix|voice|speaking|listing|chatter|"
                                r"conversation|talking)\b", re.I)


def bloc_audio(ligne_son, lex):
    """Le bloc de son : l'ambiance du lieu, et rien d'autre."""
    items = [i for i in (lex.get("ambiance") or ambiances(ligne_son))
             if not VOIX_DANS_AMBIANCE.search(i)]
    lieu = ", ".join(i.rstrip(".") for i in items) or "l'ambiance réelle du lieu"
    return (
        "AUDIO — ambiance seule.\n"
        f"La piste ne porte que le son réel du lieu : {lieu}.\n"
        "AUCUNE voix, AUCUN dialogue audible, AUCUN narrateur, AUCUNE musique.\n"
        "Les répliques ci-dessus sont jouées à l'image — lèvres, souffle, "
        "regard — et ne produisent aucun son. Les voix sont enregistrées "
        "séparément et posées au montage."
    )


def traduis(texte, lexique):
    """Applique le lexique de phrases, les plus longues d'abord.

    Traduire par phrases plutôt que par prompt tient à la nature du corpus :
    trente-cinq tournures de gabarit couvrent près de mille occurrences, et
    seules trois cent cinquante-cinq phrases sont réellement distinctes sur
    quatre-vingt-huit prompts. Le lexique est un fichier relu à la main ; il
    garantit qu'une même phrase est traduite pareil partout.
    """
    gardees = []

    def range(motif):
        """Met un fragment de côté, remplacé par un jeton neutre."""
        def prends(m):
            gardees.append(m.group(0))
            return f"\x00{len(gardees) - 1}\x00"
        return prends

    # Deux choses sont mises à l'abri avant de remplacer quoi que ce soit.
    #
    # Les répliques d'abord : une clé courte les mordait — « tickets » traduit
    # en « des tickets » transformait « Onze tickets. » en « Onze des
    # tickets. », et une réplique modifiée, c'est l'appariement perdu.
    texte = re.sub(r"\{[^}]*\}", range(None), texte)

    # Les traductions qui contiennent leur propre clé ensuite : « silence »
    # devient « le silence », que la passe suivante relirait comme un
    # « silence » à traduire, d'où « le le silence ». Le script étant relancé
    # à chaque lot, il doit pouvoir repasser sur sa propre sortie sans rien
    # empiler.
    deja = [fr for en, fr in lexique.items() if en in fr]
    if deja:
        texte = re.sub("|".join(re.escape(f) for f in sorted(deja, key=len, reverse=True)),
                       range(None), texte)

    for en in sorted(lexique, key=len, reverse=True):
        texte = texte.replace(en, lexique[en])
    return re.sub(r"\x00(\d+)\x00", lambda m: gardees[int(m.group(1))], texte)


def refais(prompt, lex):
    """Le prompt en forme Seedance 2.5. Renvoie None si rien à faire."""
    ouverture, tranches, son = parties(prompt)

    if not tranches:
        # Un plan sans réplique : sa bande-son est sa seule bande-son, on n'y
        # touche pas. Seul l'en-tête est refait, et le corps traduit s'il l'est.
        corps = lex.get("corps") or [ouverture[0] if ouverture else ""]
        texte = corps[0]
        # L'en-tête est réécrit, pas complété : il faut donc retirer celui
        # d'origine ET celui d'une passe précédente, sans quoi ils s'empilent.
        texte = re.sub(r"^Seedance 2\.5\.\s*", "", texte)
        texte = re.sub(r"^Vertical 9:16[^.]*\.\s*", "", texte)
        texte = re.sub(r"^(?:PAS de texte incrusté|NO text overlay)[^.]*\.\s*", "", texte)
        return f"{EN_TETE} {texte}".strip()

    blocs = []
    style = lex.get("style")
    tete = ouverture[0] if ouverture else ""
    if style is None:
        # L'en-tête d'origine porte le format ET le style ; on ne garde que le
        # style, le format étant redit en tête de la nouvelle version.
        style = re.sub(r"^.*?(?:image\.|l'image\.)\s*", "", tete, flags=re.S).strip()
    blocs.append(f"{EN_TETE} {style}".strip())

    autres = lex.get("ouverture")
    blocs += (autres if autres is not None else ouverture[1:])

    lignes = []
    corps_lex = lex.get("corps")
    etats_lex = lex.get("etat")
    for i, t in enumerate(tranches):
        corps = corps_lex[i] if corps_lex else t["corps"]
        etat = etats_lex[i] if etats_lex else t["etat"]
        lignes.append(f"{t['debut']}-{t['fin']}s: {sans_direction(corps)} "
                      f"End state at {t['fin']}s: {etat}")
    blocs.append("\n".join(lignes))
    blocs.append(bloc_audio(son, lex))
    return "\n\n".join(blocs)


def main(argv):
    controle = "--controle" in argv
    d = json.loads(SERIES.read_text(encoding="utf-8"))
    lexique = json.loads(LEXIQUE.read_text(encoding="utf-8")) if LEXIQUE.exists() else {}
    lexique = {k: v for k, v in lexique.items() if not k.startswith("_")}

    eps = [e for s in d["series"] for sa in s["saisons"] for e in sa["episodes"]]
    refaits = intacts = 0
    casses, anglais = [], []
    for e in eps:
        avant = e["higgsfield"]["prompt"]
        apres = traduis(refais(traduis(avant, lexique), {}), lexique)
        if repliques(apres) != repliques(avant):
            casses.append(e["id"])
            continue
        if re.search(r"\b(the|and|with|from|his|shot|frame|camera)\b", apres, re.I):
            anglais.append(e["id"])
        if apres == avant:
            intacts += 1
        else:
            refaits += 1
            e["higgsfield"]["prompt"] = apres

    if casses:
        sys.exit(f"ARRÊT — répliques modifiées sur {len(casses)} épisode(s) : "
                 f"{' '.join(casses[:10])}. Rien n'a été écrit.")

    print(f"refaits : {refaits} | déjà en forme : {intacts}")
    print(f"reste de l'anglais dans : {len(anglais)} prompt(s)")
    if anglais:
        print(f"  {' '.join(anglais[:20])}{' …' if len(anglais) > 20 else ''}")
        print(f"  → compléter {LEXIQUE.relative_to(R)}")

    if controle:
        print("\n--controle : rien n'a été écrit.")
        return
    SERIES.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n",
                      encoding="utf-8")
    print(f"\nécrit : {SERIES}")


if __name__ == "__main__":
    main(sys.argv[1:])
