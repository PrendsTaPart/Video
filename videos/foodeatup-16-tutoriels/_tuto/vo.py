#!/usr/bin/env python3
"""Voix off des seize tutoriels, et bornes de scène qui en découlent.

**Le sens du montage est inversé, comme pour les films « sans ».** On ne génère
pas une voix d'un bloc pour y relever ensuite des bornes à la lecture : chaque
segment est généré séparément, donc sa durée est *mesurée*, la scène qui le
porte dure exactement ce segment plus sa respiration, et la voix complète est
reconstruite en collant les segments avec ces mêmes respirations.

Les bornes ne sont plus déduites du montage : c'est le montage qui est déduit
des bornes. Il devient impossible qu'une scène s'arrête avant sa phrase — le
défaut le plus courant d'un montage sur estimation, et celui qui ne se voit
qu'au visionnage complet.

Sortie par tutoriel :
    <sous>/assets/vo.mp3       la voix complète, prête pour l'orchestrateur
    <sous>/assets/timing.json  les bornes absolues de chaque scène

⚠️ La clé d'API vient de l'environnement, jamais d'un fichier versionné.

    set -a && . <scratchpad>/el.env && set +a
    python3 _tuto/vo.py [sous…]
"""

import json
import os
import pathlib
import subprocess
import sys
import urllib.error
import urllib.request

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
from scripts import CLAUDE, TUTORIELS, VOIX  # noqa: E402

RACINE = ICI.parent
MODELE = "eleven_multilingual_v2"

# Respirations. Le carton d'ouverture et le carton de fin sont encadrés plus
# large : ce sont les deux seuls moments où le film énonce au lieu d'expliquer,
# et ils ne tiennent que si le silence autour d'eux est plus long qu'ailleurs.
SOUFFLE = 0.50
SOUFFLE_CARTON = 0.90


def segments(t):
    """Les segments d'un tutoriel, dans l'ordre, avec leur type de scène.

    Le type décide de la respiration et de la scène à fabriquer plus tard ;
    c'est la seule table qui relie une phrase à son image, et elle vit ici pour
    que le monteur n'ait pas à la redeviner.
    """
    out = []
    lignes = list(t["vo"])
    cta = lignes.pop()  # la dernière est toujours la clôture
    tete = lignes.pop(0)  # la première est toujours l'ouverture

    out.append(("ouverture", tete[0], tete[1]))
    for i, (ident, texte) in enumerate(lignes):
        out.append((f"planche:{i}", ident, texte))
    if t["prompt"]:
        out.append(("prompt", "CLAUDE", CLAUDE))
    out.append(("cloture", cta[0], cta[1]))
    return out


def parler(texte, sortie, cle):
    """Un segment, généré et écrit. Rejette bruyamment : un segment manquant
    décalerait tout le film sans qu'aucune étape suivante ne s'en plaigne."""
    corps = json.dumps(
        {
            "text": texte,
            "model_id": MODELE,
            "language_code": "fr",
            "voice_settings": {"stability": 0.45, "similarity_boost": 0.80, "style": 0.10},
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOIX}?output_format=mp3_44100_128",
        data=corps,
        headers={"xi-api-key": cle, "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            sortie.write_bytes(r.read())
    except urllib.error.HTTPError as e:
        raise SystemExit(f"ElevenLabs {e.code} sur « {texte[:48]}… » : {e.read()[:200]!r}")


def duree(f):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(f)],
        capture_output=True, text=True, check=True,
    )
    return float(r.stdout.strip())


def monter(t, cle):
    sous = t["sous"]
    dossier = RACINE / sous / "assets"
    (dossier / "seg").mkdir(parents=True, exist_ok=True)

    plan, curseur, entrees, filtres = [], 0.0, [], []
    for i, (genre, ident, texte) in enumerate(segments(t)):
        f = dossier / "seg" / f"{i:02d}-{ident}.mp3"
        if not f.exists():
            parler(texte, f, cle)
        d = duree(f)
        souffle = SOUFFLE_CARTON if genre in ("ouverture", "cloture") else SOUFFLE

        # La scène commence avec sa respiration d'entrée et finit avec celle de
        # sortie : la voix ne démarre jamais sur la première image, et l'image
        # ne coupe jamais sur la dernière syllabe.
        debut_scene = curseur
        debut_voix = curseur + souffle / 2
        duree_scene = souffle + d

        ms = int(round(debut_voix * 1000))
        entrees += ["-i", str(f)]
        filtres.append(f"[{len(plan)}:a]adelay={ms}|{ms}[v{len(plan)}]")

        plan.append({
            "genre": genre, "ident": ident, "texte": texte,
            "debut": round(debut_scene, 3), "duree": round(duree_scene, 3),
            "voix_a": round(debut_voix, 3), "voix_duree": round(d, 3),
        })
        curseur += duree_scene

    total = round(curseur, 3)
    mix = "".join(f"[v{i}]" for i in range(len(plan)))
    filtres.append(f"{mix}amix=inputs={len(plan)}:normalize=0:dropout_transition=0[out]")

    subprocess.run(
        ["ffmpeg", "-nostdin", "-v", "error", "-y", *entrees,
         "-filter_complex", ";".join(filtres), "-map", "[out]",
         "-t", f"{total:.3f}", "-c:a", "libmp3lame", "-b:a", "192k",
         str(dossier / "vo.mp3")],
        check=True,
    )

    (dossier / "timing.json").write_text(
        json.dumps({"total": total, "scenes": plan}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"  ✓ {sous}  {len(plan)} scènes   {total:6.2f} s")
    return total


def main():
    cle = os.environ.get("ELEVENLABS_API_KEY")
    if not cle:
        sys.exit("ELEVENLABS_API_KEY absente de l'environnement.")

    voulus = sys.argv[1:]
    liste = [t for t in TUTORIELS if not voulus or t["sous"] in voulus]
    total = 0.0
    for t in liste:
        total += monter(t, cle)
    print(f"\n{len(liste)} tutoriels, {total / 60:.1f} min de voix au total.")


if __name__ == "__main__":
    main()
