#!/usr/bin/env python3
"""Reconstitue la piste son d'un plan UpEatFood, quand la story n'existe pas.

    python3 scripts/build-plan-upeatfood.py EP523 EP528 EP533 EP534

Pourquoi ce script existe
-------------------------
Vingt-neuf des trente-cinq plans avaient déjà leur story déposée dans la
bibliothèque RapidoCMS : l'habillage y prenait sa piste son toute faite. Les
six derniers n'ont que le plan Higgsfield brut, récupéré depuis la veille et
commité dans `dist/hooks/`. Il n'y a pas de story à télécharger — il faut la
refaire.

Or la matière est là. Le film porte les soixante-six répliques, une par voix et
par chapitre, dans `assets/vo/film/EPxxx-conteur.mp3` et
`EPxxx-personnage.mp3`. La story d'un plan, c'est exactement ça : l'ambiance du
plan, le conteur à 0,0 s, le personnage à 8,0 s.

Le mixage
---------
Les voix sont à 1,0 et l'ambiance du plan à ZÉRO — voir le commentaire sur
`AMBIANCE` plus bas : elle n'apportait qu'un souffle inaudible et les artefacts
de la séparation de sources, c'est-à-dire le grésillement. La normalisation
finale vise −16 LUFS, le niveau mesuré sur le master du film.

Ces six-là sonneront donc plus propres que les vingt-neuf autres, dont la piste
vient d'une story déjà mixée où l'ambiance est cuite dans le fichier. C'est un
écart assumé, et dans le bon sens.

`loudnorm` tourne dans une passe SÉPARÉE, comme partout ailleurs dans ce
dépôt : sur une entrée de quelques secondes il ressort ses frames avec des PTS
décalés, et tout ce qui suit prend ce décalage pour du temps écoulé.
"""
import pathlib
import subprocess
import sys

R = pathlib.Path(__file__).resolve().parent.parent
HOOKS = R / "dist" / "hooks"
VOIX = R / "assets" / "vo" / "film"
SOURCES = R / "build" / "sources"

CONTEUR_A = 0.00      # le conteur ouvre le plan
PERSONNAGE_A = 8.00   # le personnage le ferme
DUREE = 10.00
# L'ambiance du plan est coupée, pas baissée.
#
# Seedance prononce les répliques écrites dans le prompt : chaque plan arrive
# avec une voix française incrustée. `enlever-voix.py` la retirait par
# séparation de sources — 24 dB de parole en moins, mais du bruit musical en
# plus, et c'est ce bruit qu'on entendait grésiller.
#
# Ce qu'on perd en coupant : rien d'audible. Mesuré sur quatre plans du film,
# l'ambiance restante après séparation est à −33 / −40 dB ; à 0,42 dans le
# mixage elle atterrit vers −40 dBFS, sous un lit musical à −28 et une voix à
# −14. Au-dessus de 9 kHz il ne reste plus que −50 à −53 dB, c'est-à-dire
# rien. On jetait donc un souffle inaudible tout en gardant ses artefacts.
AMBIANCE = 0.0


def duree_de(f):
    return float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(f)],
        capture_output=True, text=True, check=True).stdout.strip())


def mixer(ep):
    clip = HOOKS / f"{ep}.mp4"
    if not clip.exists():
        return f"{ep} : pas de plan dans dist/hooks/"
    prises = [(VOIX / f"{ep}-conteur.mp3", CONTEUR_A),
              (VOIX / f"{ep}-personnage.mp3", PERSONNAGE_A)]
    absentes = [p.name for p, _ in prises if not p.exists()]
    if absentes:
        return f"{ep} : prise(s) manquante(s) — {', '.join(absentes)}"

    SOURCES.mkdir(parents=True, exist_ok=True)
    brut = SOURCES / f"{ep}-son-brut.wav"

    entrees, graphe, pistes = ["-i", str(clip)], [], []
    graphe.append(
        f"[0:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,"
        f"atrim=duration={DUREE},asetpts=N/SR/TB,volume={AMBIANCE}[amb]")
    pistes.append("[amb]")
    for i, (p, t) in enumerate(prises, start=1):
        entrees += ["-i", str(p)]
        ms = int(t * 1000)
        graphe.append(
            f"[{i}:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,"
            f"adelay={ms}|{ms}[v{i}]")
        pistes.append(f"[v{i}]")
    graphe.append(
        f"{''.join(pistes)}amix=inputs={len(pistes)}:normalize=0:duration=first,"
        f"atrim=duration={DUREE},asetpts=N/SR/TB[mx]")

    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", *entrees,
         "-filter_complex", ";".join(graphe), "-map", "[mx]",
         "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", str(brut)],
        check=True)

    # Passe séparée : jamais `loudnorm` dans le graphe principal.
    dest = SOURCES / f"{ep}-son.mp4"
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-i", str(brut),
         "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
         "-ar", "48000", "-ac", "2", "-c:a", "aac", "-b:a", "192k", str(dest)],
        check=True)
    brut.unlink(missing_ok=True)

    # Le clip est déposé dans le cache sous le nom que `rapatrier` attend :
    # il n'ira donc rien télécharger.
    lien = SOURCES / f"{ep}-clip.mp4"
    if not lien.exists():
        lien.write_bytes(clip.read_bytes())

    return f"{ep} : piste son {duree_de(dest):.2f} s, plan {duree_de(lien):.2f} s"


def main(argv):
    if not argv:
        raise SystemExit("usage: build-plan-upeatfood.py EP523 [EP528 …]")
    for ep in argv:
        print(" ", mixer(ep), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
