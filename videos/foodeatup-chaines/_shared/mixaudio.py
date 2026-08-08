#!/usr/bin/env python3
"""
Habillage sonore : colle la nappe + les bruitages sur un master muet.

    python3 mixaudio.py <variante>        # boulangerie | restauration

Règles reprises de videos/FOODEATUP-TUTORIELS-WORKFLOW.md :
  - `loudnorm` appliqué à CHAQUE élément individuellement, AVANT `adelay` —
    jamais sur le mix composite : le mix est majoritairement silencieux entre
    les bruitages, un loudnorm global sous-estimerait la loudness et
    sur-amplifierait tout.
  - `alimiter` en garde-fou avec **`level=disabled`** explicite : ce paramètre
    est actif par défaut et renormalise à 0 dBFS APRÈS limitation, ce qui
    annule purement et simplement le plafond demandé.
  - plafond visé ~0.6 (≈ -4,4 dB) et non 0.85 : l'encodage AAC peut
    réintroduire 1-2 dB de dépassement par ringing près du plafond.

`amix` reçoit `normalize=0` : par défaut il divise chaque entrée par le nombre
d'entrées, ce qui écraserait la nappe dès qu'un bruitage se déclenche.
"""

import pathlib
import re
import subprocess
import sys

FF = "/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
EL = pathlib.Path(__file__).resolve().parent / "audio"
ROOT = pathlib.Path(__file__).resolve().parent.parent

DUREE = 55.0
I_BED = -30      # LUFS de la nappe : elle doit rester sous une future voix off.
                 # -26 laissait la nappe cretes a -15,8 dBFS, au meme niveau que
                 # les bruitages : plus rien n'en emergeait.
CEIL = 0.6       # plafond du limiteur (~ -4,4 dB), marge pour l'AAC

# Crête visée par bruitage, en dBFS.
# Les bruitages sont normalisés à la CRÊTE, pas en LUFS : `loudnorm` mesure une
# loudness intégrée, et sur un son bref noyé dans du silence il ne corrige
# quasiment rien — au premier mix, le froissement des fiches et la pose des
# plateaux étaient purement inaudibles sous la nappe (mesuré : +0,0 dB).
CRETE_SFX = {
    "sfx-data-lock.mp3": -9.0,
    "sfx-impact-ecart.mp3": -5.0,    # le seul vrai temps fort de la vidéo
    "sfx-carnet-close.mp3": -8.0,
    "sfx-fiches-paper.mp3": -6.0,    # froissement très diffus : demande plus de gain
    "sfx-plateau-pose.mp3": -9.0,
}

# Certains fichiers commencent par du silence (mesuré : 0,63 s pour la pose de
# plateau, 0,21 s pour les fiches). Sans l'enlever, le bruitage tombe APRÈS le
# repère visuel qu'il est censé accompagner.
DESILENCE = "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0"

# Chaque bruitage est calé sur l'instant exact de l'animation qu'il accompagne.
PLACEMENTS = {
    "boulangerie": [
        ("sfx-data-lock.mp3", 2.20),      # le CA consolidé se remplit
        ("sfx-impact-ecart.mp3", 27.60),  # le gonflement culmine sur « L'écart » (28.0)
        ("sfx-carnet-close.mp3", 38.40),  # les douze carnets se referment
        ("sfx-plateau-pose.mp3", 47.20),  # les fournées s'empilent
        ("sfx-plateau-pose.mp3", 48.04),
        ("sfx-plateau-pose.mp3", 48.88),
        ("sfx-data-lock.mp3", 50.40),     # « Vous l'apprenez maintenant. »
    ],
    "restauration": [
        ("sfx-data-lock.mp3", 2.20),
        ("sfx-impact-ecart.mp3", 27.60),
        ("sfx-fiches-paper.mp3", 33.30),  # les douze fiches se posent
        ("sfx-data-lock.mp3", 50.40),     # « Le chiffre d'affaires n'a rien dit. »
    ],
}


def crete_db(path: pathlib.Path) -> float:
    """Crête du fichier UNE FOIS le silence de tête retiré."""
    out = subprocess.run(
        [FF, "-hide_banner", "-i", str(path), "-af", f"{DESILENCE},astats=metadata=1",
         "-f", "null", "-"], capture_output=True, text=True).stderr
    m = re.search(r"Peak level dB: (-?[\d.]+)", out)
    return float(m.group(1)) if m else -20.0


def build(variante: str) -> pathlib.Path:
    src = ROOT / variante / "out" / f"foodeatup-chaines-{variante}-seq1-4-muet-v1.mp4"
    dst = ROOT / variante / "out" / f"foodeatup-chaines-{variante}-seq1-4-v1.mp4"
    if not src.exists():
        sys.exit(f"master muet introuvable : {src}")

    placements = PLACEMENTS[variante]
    cmd = [FF, "-v", "error", "-y", "-i", str(src), "-i", str(EL / "nappe.mp3")]
    for name, _ in placements:
        cmd += ["-i", str(EL / name)]

    parts = [
        f"[1:a]loudnorm=I={I_BED}:TP=-3:LRA=11,"
        f"afade=t=in:st=0:d=1.5,afade=t=out:st={DUREE - 2.5}:d=2.5[bed]"
    ]
    labels = ["[bed]"]
    for i, (name, at) in enumerate(placements):
        lbl = f"[s{i}]"
        gain = CRETE_SFX[name] - crete_db(EL / name)
        parts.append(
            f"[{i + 2}:a]{DESILENCE},volume={gain:.2f}dB,"
            f"adelay={int(at * 1000)}|{int(at * 1000)}{lbl}"
        )
        labels.append(lbl)
    # `aresample=48000` : sans lui la sortie sort en 96 kHz (amix suit le plus
    # haut taux des entrées) — inutile pour de la vidéo, et deux fois plus lourd.
    # `apad` avant `atrim` : sans padding, le mix s'arrête au dernier échantillon
    # audio utile. On trime 0,3 s PLUS LOIN que la vidéo et on laisse `-shortest`
    # trancher : sinon l'audio, plus court de ~90 ms après alignement des trames
    # AAC, rognait la fin de la vidéo (master à 54,91 s au lieu de 55,00 s).
    parts.append(
        "".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=longest,"
        f"alimiter=limit={CEIL}:level=disabled,"
        f"aresample=48000,apad,atrim=0:{DUREE + 0.3},asetpts=N/SR/TB[out]"
    )

    cmd += ["-filter_complex", ";".join(parts),
            "-map", "0:v", "-map", "[out]",
            "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
            "-movflags", "+faststart", "-shortest", str(dst)]
    subprocess.run(cmd, check=True)
    return dst


if __name__ == "__main__":
    v = sys.argv[1] if len(sys.argv) > 1 else "boulangerie"
    out = build(v)
    print(f"écrit {out}  —  {out.stat().st_size / 1024 / 1024:.1f} Mo")
