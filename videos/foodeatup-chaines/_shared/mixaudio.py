#!/usr/bin/env python3
"""
Habillage sonore : colle la voix off, la nappe et les bruitages sur un master muet.

    python3 mixaudio.py <bloc>        # boulangerie | restauration | fin

Règles reprises de videos/FOODEATUP-TUTORIELS-WORKFLOW.md :
  - `loudnorm` appliqué à CHAQUE ligne de voix individuellement, AVANT `adelay` —
    jamais sur le mix composite : le mix est majoritairement silencieux entre les
    lignes, un loudnorm global sous-estimerait la loudness et sur-amplifierait tout.
  - `alimiter` en garde-fou avec **`level=disabled`** explicite : ce paramètre est
    actif par défaut et renormalise à 0 dBFS APRÈS limitation, ce qui annule
    purement et simplement le plafond demandé.
  - plafond visé ~0.6 (≈ -4,4 dB) et non 0.85 : l'encodage AAC peut réintroduire
    1-2 dB de dépassement par ringing près du plafond.

`amix` reçoit `normalize=0` : par défaut il divise chaque entrée par le nombre
d'entrées, ce qui écraserait la nappe dès qu'un bruitage se déclenche.
"""

import pathlib
import re
import subprocess
import sys

FF = "/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
HERE = pathlib.Path(__file__).resolve().parent
EL = HERE / "audio"
ROOT = HERE.parent

I_BED = -30      # LUFS de la nappe : à -26 elle crêtait à -15,8 dBFS, au niveau
                 # même des bruitages, et plus rien n'en émergeait.
I_VO = -17       # LUFS de la voix : elle domine la nappe sans l'écraser
CEIL = 0.6       # plafond du limiteur (~ -4,4 dB), marge pour l'AAC
AMORCE = 0.8     # la scène s'installe avant que la voix entre

# Crête visée par bruitage, en dBFS. Les bruitages sont normalisés à la CRÊTE et
# pas en LUFS : `loudnorm` mesure une loudness intégrée, et sur un son bref noyé
# de silence il ne corrige quasiment rien — au premier mix, le froissement des
# fiches et la pose des plateaux étaient purement inaudibles sous la nappe.
CRETE_SFX = {
    "sfx-data-lock.mp3": -9.0,
    "sfx-impact-ecart.mp3": -5.0,
    "sfx-carnet-close.mp3": -8.0,
    "sfx-fiches-paper.mp3": -6.0,
    "sfx-plateau-pose.mp3": -9.0,
}

# Certains fichiers commencent par du silence (mesuré : 0,63 s pour la pose de
# plateau, 0,21 s pour les fiches). Sans l'enlever, le bruitage tombe APRÈS le
# repère visuel qu'il est censé accompagner.
DESILENCE = "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0"

# Un bruitage : (fichier, instant) ou (fichier, instant, crête forcée).
BLOCS = {
    "boulangerie": {
        "duree": 55.0,
        "scenes": {"s1": 0.0, "s2": 15.0, "s4": 33.0, "s5": 45.0},
        "sfx": [("sfx-data-lock.mp3", 2.20),      # le CA consolidé se remplit
                ("sfx-impact-ecart.mp3", 27.60),  # culmine sur « L'écart » (28.0)
                ("sfx-carnet-close.mp3", 38.40),  # les douze carnets se referment
                ("sfx-plateau-pose.mp3", 47.20),  # les fournées s'empilent
                ("sfx-plateau-pose.mp3", 48.04),
                ("sfx-plateau-pose.mp3", 48.88),
                ("sfx-data-lock.mp3", 50.40)],    # « Vous l'apprenez maintenant. »
    },
    "restauration": {
        "duree": 55.0,
        "scenes": {"s1": 0.0, "s2": 15.0, "s4": 33.0, "s5": 45.0},
        "sfx": [("sfx-data-lock.mp3", 2.20),
                ("sfx-impact-ecart.mp3", 27.60),
                ("sfx-fiches-paper.mp3", 33.30),  # les douze fiches se posent
                ("sfx-data-lock.mp3", 50.40)],
    },
    # Masters = variante + bloc de fin, montés d'un seul tenant. Le mix est refait
    # sur les 77 s plutôt que de coller deux mix : sinon la nappe s'éteint en fin
    # de variante puis remonte, et le spectateur croit la vidéo finie juste avant
    # l'appel à l'action.
    "master-boulangerie": {
        "duree": 77.0, "bed": "nappe-longue.mp3",
        "vo": [("vo-boulangerie-s1.mp3", 0.8), ("vo-boulangerie-s2.mp3", 15.8),
               ("vo-boulangerie-s4.mp3", 33.8), ("vo-boulangerie-s5.mp3", 45.8),
               ("vo-fin-s1.mp3", 55.8), ("vo-fin-s2.mp3", 67.8)],
        "sfx": [("sfx-data-lock.mp3", 2.20), ("sfx-impact-ecart.mp3", 27.60),
                ("sfx-carnet-close.mp3", 38.40), ("sfx-plateau-pose.mp3", 47.20),
                ("sfx-plateau-pose.mp3", 48.04), ("sfx-plateau-pose.mp3", 48.88),
                ("sfx-data-lock.mp3", 50.40),
                ("sfx-impact-ecart.mp3", 59.10, -9.0), ("sfx-data-lock.mp3", 68.60)],
        "src": "boulangerie/out/foodeatup-chaines-boulangerie-master-muet-v1.mp4",
    },
    "master-restauration": {
        "duree": 77.0, "bed": "nappe-longue.mp3",
        "vo": [("vo-restauration-s1.mp3", 0.8), ("vo-restauration-s2.mp3", 15.8),
               ("vo-restauration-s4.mp3", 33.8), ("vo-restauration-s5.mp3", 45.8),
               ("vo-fin-s1.mp3", 55.8), ("vo-fin-s2.mp3", 67.8)],
        "sfx": [("sfx-data-lock.mp3", 2.20), ("sfx-impact-ecart.mp3", 27.60),
                ("sfx-fiches-paper.mp3", 33.30), ("sfx-data-lock.mp3", 50.40),
                ("sfx-impact-ecart.mp3", 59.10, -9.0), ("sfx-data-lock.mp3", 68.60)],
        "src": "restauration/out/foodeatup-chaines-restauration-master-muet-v1.mp4",
    },
    # Séquences 7 et 9. La séquence 2b n'existe pas ici, donc pas de règle de
    # silence : les deux scènes portent une ligne.
    "fin": {
        "duree": 22.0,
        "scenes": {"s1": 0.0, "s2": 12.0},
        # -9 et non -5 : ici l'orange signale un risque, il ne doit pas claquer
        # comme la révélation de l'écart.
        "sfx": [("sfx-impact-ecart.mp3", 4.10, -9.0),  # le point bascule
                ("sfx-data-lock.mp3", 13.60)],         # le bouton apparaît
    },
}


def crete_db(path: pathlib.Path) -> float:
    """Crête du fichier UNE FOIS le silence de tête retiré."""
    out = subprocess.run(
        [FF, "-hide_banner", "-i", str(path), "-af", f"{DESILENCE},astats=metadata=1",
         "-f", "null", "-"], capture_output=True, text=True).stderr
    m = re.search(r"Peak level dB: (-?[\d.]+)", out)
    return float(m.group(1)) if m else -20.0


def build(bloc: str) -> pathlib.Path:
    cfg = BLOCS[bloc]
    duree = cfg["duree"]
    if "src" in cfg:
        src = ROOT / cfg["src"]
    else:
        src = ROOT / bloc / "out" / f"foodeatup-chaines-{bloc}-muet-v1.mp4"
        if not src.exists():  # nommage historique des deux variantes
            src = ROOT / bloc / "out" / f"foodeatup-chaines-{bloc}-seq1-4-muet-v1.mp4"
    dst = src.with_name(src.name.replace("-muet", ""))
    if not src.exists():
        sys.exit(f"master muet introuvable : {src}")

    sfx = cfg["sfx"]
    vo = cfg.get("vo") or [(f"vo-{bloc}-{s}.mp3", t + AMORCE)
                           for s, t in sorted(cfg["scenes"].items())
                           if (EL / f"vo-{bloc}-{s}.mp3").exists()]

    cmd = [FF, "-v", "error", "-y", "-i", str(src), "-i", str(EL / cfg.get("bed", "nappe.mp3"))]
    for item in sfx:
        cmd += ["-i", str(EL / item[0])]
    for name, _ in vo:
        cmd += ["-i", str(EL / name)]

    parts = [
        f"[1:a]loudnorm=I={I_BED}:TP=-3:LRA=11,atrim=0:{duree},"
        f"afade=t=in:st=0:d=1.5,afade=t=out:st={duree - 2.5}:d=2.5[bed]"
    ]
    labels = ["[bed]"]
    for i, item in enumerate(sfx):
        name, at = item[0], item[1]
        cible = item[2] if len(item) > 2 else CRETE_SFX[name]
        parts.append(
            f"[{i + 2}:a]{DESILENCE},volume={cible - crete_db(EL / name):.2f}dB,"
            f"adelay={int(at * 1000)}|{int(at * 1000)}[s{i}]"
        )
        labels.append(f"[s{i}]")
    # La voix : loudnorm par ligne. Ici la loudness intégrée EST le bon critère
    # (contrairement aux bruitages) — une ligne parlée est un signal continu.
    n0 = 2 + len(sfx)
    for j, (_, at) in enumerate(vo):
        parts.append(
            f"[{n0 + j}:a]loudnorm=I={I_VO}:TP=-3:LRA=11,"
            f"adelay={int(at * 1000)}|{int(at * 1000)}[v{j}]"
        )
        labels.append(f"[v{j}]")

    # `aresample=48000` : sans lui la sortie sort en 96 kHz (amix suit le plus haut
    # taux des entrées). `apad` + trim 0,3 s PLUS LOIN que la vidéo, en laissant
    # `-shortest` trancher : sinon l'audio, plus court de ~90 ms après alignement
    # des trames AAC, rognait la fin de la vidéo.
    parts.append(
        "".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=longest,"
        f"alimiter=limit={CEIL}:level=disabled,"
        f"aresample=48000,apad,atrim=0:{duree + 0.3},asetpts=N/SR/TB[out]"
    )

    cmd += ["-filter_complex", ";".join(parts),
            "-map", "0:v", "-map", "[out]",
            "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
            "-movflags", "+faststart", "-shortest", str(dst)]
    subprocess.run(cmd, check=True)
    return dst


if __name__ == "__main__":
    b = sys.argv[1] if len(sys.argv) > 1 else "boulangerie"
    out = build(b)
    print(f"écrit {out}  —  {out.stat().st_size / 1024 / 1024:.1f} Mo")
