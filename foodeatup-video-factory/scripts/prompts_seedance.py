"""Lecture et réécriture des prompts Higgsfield, en forme Seedance 2.5.

Ce module ne fait rien tout seul : il porte la grammaire des prompts, que
`refaire-prompts-higgsfield.py` applique à l'inventaire.

La forme d'un prompt
--------------------
Les trois cent trente-sept prompts du dépôt suivent tous le même squelette,
blocs séparés par une ligne vide :

    <en-tête technique et négatifs> <style>
    <blocs libres : identité visuelle, références @Image, décor…>
    <découpage : une ligne par tranche « 0-5s: », « 5-8s: », « 8-10s: »>
    Sound design: …

Le découpage est la seule partie qui compte pour la fabrique : chaque tranche
porte un seul changement, un « End state at Ns » explicite, et jusqu'à deux
répliques entre accolades.

Les accolades sont sacrées
--------------------------
`veille-higgsfield.py` apparie un job Higgsfield à un épisode en comparant les
répliques entre accolades — c'est le seul lien fiable entre les deux. Toute
réécriture doit donc les rendre à l'octet près. `parties()` les extrait,
`recompose()` les remet, et l'appelant vérifie l'égalité avant d'écrire.
"""
import re

# Une tranche : « 0-5s: … End state at 5s: … »
TRANCHE = re.compile(r"^(\d+)-(\d+)s:\s*(.*)$", re.S)
REPLIQUE = re.compile(r"\{([^}]*)\}")
FIN_DE_TRANCHE = re.compile(r"\s*End state at \d+s\s*:\s*(.*)$", re.S)


def repliques(texte):
    """Les répliques d'un texte, dans l'ordre, sans les accolades."""
    return REPLIQUE.findall(texte or "")


def parties(prompt):
    """Découpe un prompt en (blocs d'ouverture, tranches, ligne de son).

    Une tranche est un dict : début, fin, corps (la mise en scène), etat
    (le « End state at »), et les répliques telles quelles.
    """
    blocs = [b.strip() for b in (prompt or "").split("\n\n") if b.strip()]
    ouverture, tranches, son = [], [], None

    for bloc in blocs:
        if bloc.startswith("Sound design:") or bloc.startswith("AUDIO"):
            son = bloc
            continue
        lignes = [l for l in bloc.split("\n") if l.strip()]
        if lignes and all(TRANCHE.match(l) for l in lignes):
            for l in lignes:
                d, f, reste = TRANCHE.match(l).groups()
                m = FIN_DE_TRANCHE.search(reste)
                corps = reste[: m.start()] if m else reste
                tranches.append({
                    "debut": int(d), "fin": int(f),
                    "corps": corps.strip(),
                    "etat": (m.group(1).strip() if m else ""),
                    "repliques": repliques(reste),
                })
        else:
            ouverture.append(bloc)

    return ouverture, tranches, son


# ─────────────────────────────────────────────────────────────────────────────
# La forme Seedance 2.5
#
# Deux changements de fond par rapport à la forme précédente.
#
# 1. Le plan ne parle plus. Seedance prononçait les répliques du prompt, et
#    le montage posait par-dessus la même phrase dite par ElevenLabs : on
#    entendait deux voix. On les retirait ensuite par séparation de sources,
#    vingt secondes de calcul par plan pour défaire ce que le prompt avait
#    demandé. Il est plus simple de ne pas le demander.
#
# 2. La direction de jeu disparaît. « le débit d'un conteur qui connaît déjà
#    la fin » ne sert plus à rien quand la voix vient d'ailleurs : ce qui reste
#    utile au modèle, c'est que le personnage articule cette phrase-là, à ce
#    moment-là, pour que les lèvres et la respiration soient justes.
# ─────────────────────────────────────────────────────────────────────────────
EN_TETE = (
    "Seedance 2.5. Vertical 9:16, 10 secondes, 1080p, 24 im/s. "
    "PAS de texte incrusté, PAS de sous-titres, PAS de filigrane, PAS de logo, "
    "AUCUNE légende gravée dans l'image."
)

# Une seule façon d'annoncer une réplique, quelle que soit la série : le
# personnage la dit, et on ne l'entend pas.
def dit(qui, texte):
    """La ligne qui pose une réplique : jouée à l'image, muette à l'oreille."""
    return f"{qui} dit cette phrase, sans qu'aucun son ne sorte : {{{texte}}}"


BLOC_AUDIO = (
    "AUDIO — ambiance seule.\n"
    "La piste ne porte que le son réel du lieu : {ambiance}.\n"
    "AUCUNE voix, AUCUN dialogue audible, AUCUN narrateur, AUCUNE musique, "
    "AUCUN bruitage ajouté.\n"
    "Les répliques ci-dessus sont jouées à l'image — lèvres, souffle, regard — "
    "et ne doivent produire aucun son. La voix est enregistrée séparément et "
    "posée au montage."
)


def bloc_audio(ambiance):
    """Le bloc de son, avec l'ambiance propre au plan."""
    return BLOC_AUDIO.format(ambiance=ambiance.strip().rstrip("."))
