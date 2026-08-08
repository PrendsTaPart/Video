#!/usr/bin/env python3
"""Voix off des neuf films « sans », et bornes de scène qui en découlent.

Les neuf films « avec » ont été montés dans l'autre sens : une voix générée
d'un bloc, transcrite par reconnaissance, et des bornes de scène relevées à la
main dans les timings de mots. Ça marche, mais chaque borne est une lecture, et
une lecture peut être fausse d'une demi-seconde sans que rien ne le signale.

Ici on inverse. **Chaque segment est généré séparément**, donc sa durée est
mesurée, pas estimée ; la scène qui le porte dure exactement ce segment plus sa
respiration ; et la voix complète est reconstruite en collant les segments avec
ces mêmes respirations. Les bornes ne sont plus déduites du montage, c'est le
montage qui est déduit des bornes. Il devient impossible qu'une scène s'arrête
avant sa phrase.

Sortie par film :
  <film>/assets/vo.mp3      la voix complète, prête pour l'orchestrateur
  <film>/assets/timing.json les bornes absolues de chaque scène

Usage : python3 _serie/vo-sans.py [film…]   (sans argument : les neuf)
"""

import json
import os
import pathlib
import subprocess
import sys
import urllib.request

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
from films_sans import FILMS, PUNCHLINE_VO  # noqa: E402

# `_serie/` est dans le dossier de la série : le parent immédiat, pas au-dessus.
RACINE = ICI.parent

# Adam · Instructor, la voix de toute la série. La changer pour le volet
# « sans » casserait le miroir : c'est la même personne qui raconte les deux
# journées, c'est ce qui rend la comparaison recevable.
VOIX = "TGAegA0zNRi8I6nUdq3i"
MODELE = "eleven_multilingual_v2"

# Respirations. Le refrain est encadré plus large que le reste : c'est le seul
# moment où le film s'arrête de raconter pour énoncer, et il ne tient que si le
# silence autour de lui est plus long qu'ailleurs.
SOUFFLE = 0.55
SOUFFLE_REFRAIN = 1.10
SOUFFLE_PUNCHLINE = 0.90

# L'ouverture et la clôture ne portent pas de voix : le hook est lu à l'écran,
# la punchline est dite mais sa scène commence avant elle.
HOOK = 4.20
PUNCHLINE_MIN = 7.00


def tts(texte, sortie, cle):
    """Un segment. On ne re-génère jamais un fichier déjà produit."""
    if sortie.exists() and sortie.stat().st_size > 4000:
        return
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOIX}",
        data=json.dumps({
            "text": texte,
            "model_id": MODELE,
            "language_code": "fr",
            # Stabilité haute : neuf films doivent sonner comme un seul
            # locuteur, y compris sur le refrain répété neuf fois.
            "voice_settings": {"stability": .55, "similarity_boost": .78,
                               "style": .12, "use_speaker_boost": True},
        }).encode(),
        headers={"xi-api-key": cle, "Content-Type": "application/json"},
        method="POST")
    with urllib.request.urlopen(req, timeout=180) as r:
        sortie.write_bytes(r.read())


def duree(f):
    return float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(f)], capture_output=True, text=True).stdout)


def main():
    cle = os.environ.get("ELEVENLABS_API_KEY")
    if not cle:
        sys.exit("ELEVENLABS_API_KEY absente de l'environnement")

    voulus = sys.argv[1:] or list(FILMS)
    for film in voulus:
        spec = FILMS[film]
        dossier = RACINE / film / "assets"
        seg_dir = dossier / "segments"
        seg_dir.mkdir(parents=True, exist_ok=True)

        segments = list(spec["vo"]) + [PUNCHLINE_VO]
        fichiers = []
        for i, texte in enumerate(segments):
            f = seg_dir / f"{i:02d}.mp3"
            tts(texte, f, cle)
            fichiers.append(f)

        # Les bornes. La scène i commence là où finit la précédente, et dure
        # exactement son segment plus sa respiration — d'où la garantie qu'une
        # scène ne peut pas se refermer sur sa propre phrase.
        # ⚠️ On arrondit les **débuts**, puis on déduit chaque durée de la
        # différence entre deux débuts. Arrondir les deux séparément fait que
        # `debut + duree` retombe un centième à côté du début suivant, et le
        # lint rejette alors deux clips qui se chevauchent de 10 ms sur la même
        # piste. Ici la chaîne se referme exactement, par construction.
        voix, souffles = [], []
        for i, f in enumerate(fichiers):
            voix.append(duree(f))
            if i == 2:                       # le refrain
                souffles.append(SOUFFLE_REFRAIN)
            elif i == len(fichiers) - 1:     # la punchline
                souffles.append(SOUFFLE_PUNCHLINE)
            else:
                souffles.append(SOUFFLE)

        debuts, t = [], HOOK
        for i, (d, s) in enumerate(zip(voix, souffles)):
            debuts.append(round(t, 2))
            scene = d + s
            if i == len(fichiers) - 1:
                scene = max(scene, PUNCHLINE_MIN)
            t += scene
        fin = round(t, 2)

        bornes = [{"index": i, "debut": debuts[i],
                   "duree": round((debuts[i + 1] if i + 1 < len(debuts) else fin)
                                  - debuts[i], 2),
                   "voix": round(voix[i], 2)}
                  for i in range(len(debuts))]

        # La voix complète : chaque segment posé à son instant, du silence
        # entre. On la construit par `adelay` plutôt que par concaténation de
        # silences — un décalage exprimé en millisecondes ne dérive pas, une
        # somme de silences encodés si.
        entrees, filtres = [], []
        for i, (f, b) in enumerate(zip(fichiers, bornes)):
            entrees += ["-i", str(f)]
            ms = int(round(b["debut"] * 1000))
            filtres.append(f"[{i}:a]aresample=48000,adelay={ms}|{ms}[a{i}]")
        mix = "".join(f"[a{i}]" for i in range(len(fichiers)))
        # `amix` diviserait le niveau par le nombre d'entrées ; les segments ne
        # se recouvrent jamais, donc `amix` avec normalisation coupée convient
        # et garde chaque phrase à son niveau d'origine.
        filtres.append(f"{mix}amix=inputs={len(fichiers)}:normalize=0[out]")
        subprocess.run(
            ["ffmpeg", "-nostdin", "-v", "error", *entrees,
             "-filter_complex", ";".join(filtres), "-map", "[out]",
             "-c:a", "libmp3lame", "-b:a", "192k",
             str(dossier / "vo.mp3"), "-y"], check=True)

        total = round(bornes[-1]["debut"] + bornes[-1]["duree"], 2)
        (dossier / "timing.json").write_text(json.dumps(
            {"hook": HOOK, "total": total, "scenes": bornes},
            ensure_ascii=False, indent=2), encoding="utf-8")

        pic = subprocess.run(
            ["ffmpeg", "-nostdin", "-v", "error", "-i", str(dossier / "vo.mp3"),
             "-af", "volumedetect", "-f", "null", "-"],
            capture_output=True, text=True).stderr
        crete = next((l.split(":")[1].strip() for l in pic.splitlines()
                      if "max_volume" in l), "?")
        print(f"  {film:28} {total:6.2f} s  crête {crete}")


if __name__ == "__main__":
    main()
