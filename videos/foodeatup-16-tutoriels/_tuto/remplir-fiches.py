#!/usr/bin/env python3
"""Remplit les seize fiches du site, qui sont encore des coquilles.

Une vidéo publiée sous une fiche qui dit « Cette vidéo est en cours de
tournage » serait pire que pas de vidéo : la page se contredirait elle-même,
sous les yeux du lecteur. Le film et le texte partent donc ensemble.

Le script réécrit `src/data/tutorials.ts` — la source versionnée — et produit
le SQL pour la base, qui est ce que le site lit désormais.

**Il ne touche que les seize.** Chaque bloc est repéré par son slug, et la
réécriture est bornée au bloc : le fichier fait cinq mille lignes et porte cent
soixante-treize fiches, dont aucune autre ne doit bouger. Le compte est vérifié
avant écriture.

Usage : python3 _tuto/remplir-fiches.py [--ecrire]
        (sans `--ecrire` : contrôle à blanc, n'écrit rien)
"""

import json
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
from scripts import TUTORIELS  # noqa: E402

RACINE = ICI.parent
SITE = pathlib.Path("/workspace/foodeatup-guide-star-0cc068d1")
FICHIER = SITE / "src" / "data" / "tutorials.ts"

MEDIA = "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque"


def nom_media(t):
    """Le nom du média en bibliothèque. `-v1` comme toute la série."""
    return f"tuto-{t['slug']}-v1"


# Le module Caisse POS est annoncé sur le site comme « en préparation par notre
# équipe de développeurs · arrive en v2 », et ses sept fiches sont en brouillon.
#
# Ses huit outils MCP existent pourtant, et sont détaillés : `open_pos_session`,
# `record_pos_payment`, `close_pos_session`… La fonction est donc là côté API.
# Mais **basculer un module en production n'est pas une décision de montage** :
# publier sept tutoriels sous un module que le site annonce comme non livré
# ferait dire au site deux choses contraires le même jour.
#
# Les sept fiches reçoivent donc leur contenu réel et restent en brouillon.
# Le jour où Michael retire l'indicateur du module, elles sont prêtes — il n'y
# a qu'un statut à changer, pas un texte à écrire.
MODULE_EN_PREPARATION = {"caisse-pos"}


def statut_sql(t):
    if t["module"] in MODULE_EN_PREPARATION:
        return "statut='brouillon'"
    return "statut='publie', publie_le=now()"


def ts(texte):
    """Une chaîne TypeScript, guillemets doubles échappés."""
    return '"' + texte.replace("\\", "\\\\").replace('"', '\\"') + '"'


def bloc_ts(t, duree):
    """Les champs à substituer dans le bloc d'une fiche."""
    etapes = "\n".join(f"      {ts(e)}," for e in t["etapes"])
    prompt = (
        "\n    claudePrompts: [\n"
        "      {\n"
        f"        title: {ts('Prompt Claude')},\n"
        f"        prompt: {ts(t['prompt'])},\n"
        "      },\n"
        "    ],"
        if t["prompt"]
        else ""
    )
    return (
        f'    videoUrl: {ts(f"{MEDIA}/{nom_media(t)}")},\n'
        f'    thumbnailUrl: {ts(f"{MEDIA}/{nom_media(t)}-poster")},\n'
        f"    durationSeconds: {int(round(duree))},\n"
        f"    howItWorks: [\n{etapes}\n    ],\n"
        f"    whatItsFor:\n      {ts(t['a_quoi'])},\n"
        f"    chefTip:\n      {ts(t['astuce'])},"
        f"{prompt}"
    )


def remplacer(source, t, duree):
    """Réécrit le bloc d'une fiche, de `videoUrl` à la fin du bloc.

    La borne de fin est la ligne `  },` qui ferme l'objet — repérée depuis le
    slug, jamais depuis un compte de lignes : deux fiches n'ont pas le même
    nombre d'étapes, et un décalage d'une ligne mangerait la fiche suivante.
    """
    ancre = f'    slug: "{t["slug"]}",'
    i = source.find(ancre)
    if i < 0:
        raise SystemExit(f"fiche introuvable : {t['slug']}")

    j = source.find("\n    videoUrl:", i)
    fin = source.find("\n  },", j)
    if j < 0 or fin < 0 or (fin < j):
        raise SystemExit(f"bloc illisible pour {t['slug']}")

    # Le titre change pour la seule fiche retitrée (doublon écarté).
    tete = source[i:j]
    if t["titre_fiche"] != t["titre"] or True:
        tete = re.sub(
            r'(\n    title: )"(?:[^"\\]|\\.)*"',
            lambda m: m.group(1) + ts(t["titre_fiche"]),
            tete,
            count=1,
        )

    return source[:i] + tete + "\n" + bloc_ts(t, duree) + source[fin:]


def main():
    ecrire = "--ecrire" in sys.argv
    source = FICHIER.read_text(encoding="utf-8")
    avant = source.count('    slug: "')

    sql = ["BEGIN;"]
    for t in TUTORIELS:
        timing = json.loads(
            (RACINE / t["sous"] / "assets" / "timing.json").read_text(encoding="utf-8")
        )
        duree = int(round(timing["total"]))
        source = remplacer(source, t, duree)

        prompts = (
            [{"title": "Prompt Claude", "prompt": t["prompt"]}] if t["prompt"] else []
        )
        q = lambda x: "'" + x.replace("'", "''") + "'"  # noqa: E731
        arr = "ARRAY[" + ",".join(q(e) for e in t["etapes"]) + "]::text[]"
        sql.append(
            f"UPDATE public.tutorials SET "
            f"titre={q(t['titre_fiche'])}, "
            f"video_url={q(f'{MEDIA}/{nom_media(t)}')}, "
            f"thumbnail_url={q(f'{MEDIA}/{nom_media(t)}-poster')}, "
            f"duree_secondes={duree}, "
            f"how_it_works={arr}, "
            f"what_its_for={q(t['a_quoi'])}, "
            f"astuce_du_chef={q(t['astuce'])}, "
            f"claude_prompts={q(json.dumps(prompts, ensure_ascii=False))}::jsonb, "
            + statut_sql(t)
            + f" WHERE slug={q(t['slug'])};"
        )
    sql.append("COMMIT;")

    apres = source.count('    slug: "')
    if avant != apres:
        raise SystemExit(f"⚠️ {avant} fiches avant, {apres} après — réécriture abandonnée")

    reste = source.count("Cette vidéo est en cours de tournage")
    print(f"fiches : {avant} avant, {apres} après")
    print(f"coquilles restantes : {reste}")

    if not ecrire:
        print("\ncontrôle à blanc — rien écrit. Relancer avec --ecrire.")
        return

    FICHIER.write_text(source, encoding="utf-8")
    (RACINE / "_tuto" / "fiches.sql").write_text("\n".join(sql), encoding="utf-8")
    print(f"\nécrit {FICHIER}")
    print(f"écrit {RACINE / '_tuto' / 'fiches.sql'}")


if __name__ == "__main__":
    main()
