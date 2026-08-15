#!/usr/bin/env python3
"""Écrit le script HeyGen des épisodes qui n'en ont pas.

    python3 scripts/gen-scripts-heygen.py

Le master de 37,5 s enchaîne cinq segments, dont neuf secondes où l'avatar 3D du
chef dit ce que le logiciel fait. Sans ce texte, l'épisode ne se monte pas : il
manque un cinquième du master.

Cent trente-quatre épisodes n'en avaient aucun. Ce n'est pas un oubli d'écriture
— le texte existe déjà, il est dans le `resume` de l'épisode, qui a toujours été
défini comme « ce que dit l'avatar : le contenu utile ». Il n'avait simplement
jamais été extrait sous la forme que HeyGen attend.

Neuf secondes, c'est trente mots. Au-delà, le montage accélère la parole et ça
s'entend : le script est donc coupé à la phrase, jamais au mot, et ce qui ne
tient pas est laissé de côté plutôt que compressé.

Le script ne touche jamais un épisode qui a déjà son texte — ceux des saisons 6,
7 et 8 sont écrits à la main, ils priment.
"""
import json
import pathlib
import re

R = pathlib.Path(__file__).resolve().parent.parent
INVENTAIRE = R.parent / "foodeatup-social" / "data" / "series.json"

MOTS_MAX = 30


def phrases(texte):
    return [p.strip() for p in re.split(r"(?<=[.!?…])\s+", texte.strip()) if p.strip()]


def script(e):
    """Ce que l'avatar dit — au plus trente mots, coupés à la phrase."""
    retenues, total = [], 0
    for p in phrases(e.get("resume") or ""):
        n = len(p.split())
        if retenues and total + n > MOTS_MAX:
            break
        retenues.append(p)
        total += n
        if total >= MOTS_MAX:
            break
    return " ".join(retenues)


def consigne(e, s, sa):
    """Le bloc à coller dans HeyGen, avec ses réglages."""
    return (
        f"AVATAR — le chef FoodEatUp, avatar 3D, plan poitrine, fond neutre "
        f"crème #FCF9E6. Regard caméra, posture ouverte, aucune gestuelle "
        f"appuyée.\n"
        f"VOIX — française, timbre grave, débit posé. Neuf secondes, pas une de "
        f"plus.\n"
        f"CADRE — vertical 9:16, 1080 × 1920. Aucun texte incrusté : les "
        f"sous-titres sont ajoutés au montage.\n"
        f"CONTEXTE — {s['nom']}, saison {sa['numero']} « {sa['titre']} », "
        f"épisode {e['id']} · {e['module']} · {e['chapitre']}.\n\n"
        f"TEXTE À DIRE, mot pour mot :\n"
        f"« {script(e)} »"
    )


def main():
    d = json.load(open(INVENTAIRE, encoding="utf-8"))
    ecrits, deja, vides = 0, 0, []
    for s in d["series"]:
        for sa in s["saisons"]:
            for e in sa["episodes"]:
                # Les textes écrits à la main priment : saisons 6, 7 et 8.
                if e.get("heygenPrompt") or e.get("scriptHeygen"):
                    deja += 1
                    continue
                if not script(e):
                    vides.append(e["id"])
                    continue
                e["heygenPrompt"] = consigne(e, s, sa)
                ecrits += 1

    open(INVENTAIRE, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2))
    print(f"{ecrits} script(s) HeyGen écrit(s), {deja} déjà présent(s)")
    if vides:
        print(f"⚠️ {len(vides)} épisode(s) sans résumé, donc sans script : "
              f"{', '.join(vides[:8])}")


if __name__ == "__main__":
    main()
