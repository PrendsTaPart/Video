#!/usr/bin/env python3
"""Écrit un SCRIPT.md par tutoriel, depuis `scripts.py`.

Le fichier Python est la source ; les Markdown en sont la vue lisible. Les
écrire à la main tous les deux, ce serait seize occasions de les laisser
diverger — et c'est le Markdown qu'on relit, donc c'est lui qui mentirait.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from scripts import TUTORIELS, VOIX  # noqa: E402

RACINE = pathlib.Path(__file__).resolve().parents[1]

GABARIT = """# {titre}

**Fiche** `{slug}` · module `{module}` · identifiant de série `{sous}`

> {intention}

⚠️ **Film sans rush.** Ce tutoriel n'a pas de capture d'écran : il est en motion
design assumé. Aucun plan ne prétend montrer le produit — une planche
schématique dit « voici l'étape et ce qui compte », là où une fausse interface
prétendrait « voici l'écran ». Le jour où le rush existe, le film est remplacé ;
ce script, lui, reste.

## À quoi ça sert (texte de la fiche)

{a_quoi}

## Marche à suivre (texte de la fiche)

{etapes}

## Astuce du chef

{astuce}

## Voix off

Adam - Instructor (`{voix}`), `eleven_multilingual_v2`, français.

| # | Texte |
|---|---|
{vo}

## Frise des jalons

{jalons}

## Outils MCP correspondants

{outils}

## Prompt Claude

{prompt}
"""


def puces(liste):
    return "\n".join(f"{i + 1}. {e}" for i, e in enumerate(liste))


def main():
    for t in TUTORIELS:
        dossier = RACINE / t["sous"]
        dossier.mkdir(parents=True, exist_ok=True)

        vo = "\n".join(f"| {i} | {texte} |" for i, texte in t["vo"])
        jalons = " → ".join(f"**{j}**" for j in t["boards"])
        outils = (
            "\n".join(f"- `{o}`" for o in t["outils"])
            if t["outils"]
            else "_Aucun outil MCP ne couvre ce geste. Pas de prompt inventé pour combler le vide._"
        )
        prompt = f"> {t['prompt']}" if t["prompt"] else (
            "_Aucun._ Le geste n'a pas d'outil MCP correspondant ; proposer un prompt "
            "qui ne marche pas serait pire que ne rien proposer."
        )

        (dossier / "SCRIPT.md").write_text(
            GABARIT.format(
                titre=t["titre"], slug=t["slug"], module=t["module"], sous=t["sous"],
                intention=t["intention"], a_quoi=t["a_quoi"],
                etapes=puces(t["etapes"]), astuce=t["astuce"], voix=VOIX,
                vo=vo, jalons=jalons, outils=outils, prompt=prompt,
            ),
            encoding="utf-8",
        )
        print(f"  {t['sous']}/SCRIPT.md  {t['titre']}")

    print(f"\n{len(TUTORIELS)} scripts écrits.")


if __name__ == "__main__":
    main()
