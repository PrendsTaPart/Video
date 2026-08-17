#!/usr/bin/env python3
"""Assemble la narration du film UpEatFood en une seule piste.

    python3 scripts/build-narration-film.py                (monte la piste)
    python3 scripts/build-narration-film.py --verifier      (dit où tombent les
                                                            répliques, ne monte rien)
    python3 scripts/build-narration-film.py --recalculer    (réécrit les minutages
                                                            depuis le film, puis monte)

Ce que fait ce script
---------------------
Il pose les soixante-six répliques d'`assets/vo/film/<clé>.mp3` sur un lit
silencieux de la durée du film et écrit `assets/voix/conteur-film.mp3`, que
`build-film.py --narration` mixe ensuite par-dessus l'ambiance et la musique.

Ce fichier de sortie est le même que celui qu'une session précédente avait
rempli par erreur avec l'échantillon de casting de la voix — une seule phrase
de six secondes posée sur six minutes de film. On l'écrase, on ne le contourne
pas : `build-habillage.py` lit ce chemin.

D'où viennent les minutages
---------------------------
**Pas des constantes de `build-film.py`.** C'est le piège dans lequel est
tombée la première version de `state/narration-film.json`, et il coûte cher :

  - le logo animé dure 3,333 s et non les 4,0 s de `T_LOGO` — `zoompan` rend
    100 images là où la constante en promet 120 ;
  - un chapitre dure 301 images, soit 10,033 s et non 10,0 s ;
  - EP524 n'a pas de réplique, mais occupe quand même ses dix secondes à
    l'écran — l'oublier décalait toute la cinquième saison d'un chapitre
    entier, soit une vingtaine de répliques posées sur le mauvais plan.

On lit donc la structure réelle du film : `build/film/liste.txt` donne les
morceaux dans l'ordre du montage, et on compte leurs **images**. La durée de
conteneur ne convient pas — elle inclut le rembourrage AAC de la piste son, et
le film dure 372,5 s d'image pour 375,1 s de conteneur.

Il faut donc que `build-film.py` ait tourné au moins une fois avant ce script.
C'est l'ordre naturel : on monte le film muet, on pose la narration dessus,
puis on remixe avec `--narration`.

Par sécurité, le script refuse de monter si les minutages notés dans
`state/narration-film.json` ne correspondent plus à la structure mesurée.
`--recalculer` les remet d'équerre.
"""
import argparse
import json
import pathlib
import subprocess
import sys

R = pathlib.Path(__file__).resolve().parent.parent
LISTE = R / "build" / "film" / "liste.txt"
FILM = R / "dist" / "film" / "upeatfood.mp4"
REPLIQUES = R / "state" / "narration-film.json"
VOIX = R / "assets" / "vo" / "film"
SORTIE = R / "assets" / "voix" / "conteur-film.mp3"

IPS = 30

# Où la réplique tombe dans son chapitre. Le conteur ouvre le plan, le
# personnage a le dernier mot — 7,6 s dans un chapitre qui en dure 10,033.
DANS_LE_PLAN = {"conteur": 0.5, "personnage": 7.6}

TOLERANCE = 0.05    # s — au-delà, les minutages notés sont considérés faux


def images(f):
    """Le nombre d'images de la piste vidéo — la seule mesure qui fasse foi."""
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=nb_frames", "-of", "csv=p=0", str(f)],
        capture_output=True, text=True).stdout.strip().rstrip(",")
    return int(out)


def duree(f):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(f)], capture_output=True, text=True).stdout
    return float(out.strip())


def debuts_de_chapitre():
    """{EPxxx: seconde où son plan commence}, mesuré sur le montage réel."""
    if not LISTE.exists():
        sys.exit(f"{LISTE} est absent — lancer d'abord `python3 scripts/build-film.py`.")
    morceaux = [l.strip()[6:-1] for l in LISTE.read_text(encoding="utf-8").splitlines()
                if l.strip()]
    debuts, n = {}, 0
    for m in morceaux:
        nom = pathlib.Path(m).stem
        if "-EP" in nom:
            debuts[nom.split("-")[1]] = n / IPS
        n += images(m)
    return debuts, n / IPS


def minutages(repliques, debuts):
    """Le minutage que chaque réplique devrait avoir, d'après le film monté."""
    vrais = {}
    for r in repliques:
        ep, role = r["cle"].split("-")
        if ep not in debuts:
            sys.exit(f"{r['cle']} : le chapitre {ep} n'est pas dans le film monté.")
        vrais[r["cle"]] = round(debuts[ep] + DANS_LE_PLAN[role], 3)
    return vrais


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--verifier", action="store_true",
                    help="compare les minutages notés au film, ne monte rien")
    ap.add_argument("--recalculer", action="store_true",
                    help="réécrit les minutages depuis le film monté")
    args = ap.parse_args(argv)

    repliques = json.loads(REPLIQUES.read_text(encoding="utf-8"))
    debuts, duree_image = debuts_de_chapitre()
    vrais = minutages(repliques, debuts)

    ecarts = [(r["cle"], r["t"], vrais[r["cle"]]) for r in repliques
              if abs(r["t"] - vrais[r["cle"]]) > TOLERANCE]

    if args.verifier or ecarts:
        print(f"film : {duree_image:.3f} s d'image, {len(debuts)} chapitres")
        print(f"répliques : {len(repliques)}, hors tolérance : {len(ecarts)}\n")
        for cle, note, vrai in ecarts[:80]:
            print(f"  {cle:22s} noté {note:8.3f}  →  réel {vrai:8.3f}"
                  f"   ({vrai - note:+.3f})")
    if args.verifier:
        return 0

    if ecarts:
        if not args.recalculer:
            sys.exit("\nLes minutages notés ne correspondent pas au film monté. "
                     "Relancer avec --recalculer pour les remettre d'équerre.")
        for r in repliques:
            r["t"] = vrais[r["cle"]]
        REPLIQUES.write_text(
            json.dumps(repliques, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8")
        print(f"\n{REPLIQUES.name} remis d'équerre.\n")

    manquants = [r["cle"] for r in repliques if not (VOIX / f"{r['cle']}.mp3").exists()]
    if manquants:
        sys.exit(f"voix manquantes dans {VOIX} : {', '.join(manquants)}")

    # Le lit fait la durée du film — conteneur, pas image : c'est la piste son
    # qu'on double, et `amix` la coupera de toute façon sur l'ambiance.
    lit = duree(FILM)

    entrees, filtres, etiquettes = [], [], []
    for i, r in enumerate(repliques, start=1):
        f = VOIX / f"{r['cle']}.mp3"
        entrees += ["-i", str(f)]
        ms = int(round(r["t"] * 1000))
        filtres.append(
            f"[{i}:a]aresample=48000,"
            f"aformat=sample_fmts=fltp:channel_layouts=stereo,"
            f"adelay={ms}|{ms}[v{i}]")
        etiquettes.append(f"[v{i}]")

        fin = r["t"] + duree(f)
        ep = r["cle"].split("-")[0]
        fin_plan = debuts[ep] + 301 / IPS
        if fin > fin_plan:
            print(f"  ⚠ {r['cle']} déborde de {fin - fin_plan:.2f} s sur le plan suivant")

    filtres.append(
        "".join(["[0:a]"] + etiquettes)
        + f"amix=inputs={len(repliques) + 1}:duration=first:normalize=0[out]")

    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    cmd = (["ffmpeg", "-v", "error", "-y",
            "-f", "lavfi", "-t", f"{lit:.3f}", "-i", "anullsrc=r=48000:cl=stereo"]
           + entrees
           + ["-filter_complex", ";".join(filtres), "-map", "[out]",
              "-c:a", "libmp3lame", "-b:a", "192k", "-ar", "48000", "-ac", "2",
              str(SORTIE)])
    subprocess.run(cmd, check=True, capture_output=True, text=True)

    print(f"\n{SORTIE}  {duree(SORTIE):.3f} s  {len(repliques)} répliques")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
