#!/usr/bin/env python3
"""Abaisse musique et bruitages des neuf films « sans », sans re-rendre l'image.

Michael : « le bruitage et la musique sont trop fort, mets-les au minimum ».

**Pourquoi on ne re-rend pas.** Un rendu HyperFrames des neuf films prend des
heures et repasse par Chrome, la compression et le contrôle qualité — pour ne
changer que des gains audio. Or la composition déclare chaque son avec son
fichier, son instant, sa durée et son volume : tout ce qu'il faut pour
reconstruire la bande-son à l'identique, en dehors du navigateur. On refait donc
l'audio avec ffmpeg et on le remonte sur l'image existante en `-c:v copy`.
L'image n'est pas ré-encodée : elle est, au bit près, celle qui a été contrôlée.

**Ce qui change, et ce qui ne change pas.** La voix off reste à 1.0 : elle porte
le texte, et c'est justement pour qu'on l'entende mieux qu'on baisse le reste.
Tout le reste — lit musical, cadence finale, papier, frappes, clics, soupir —
est multiplié par `FACTEUR_AMBIANCE`. Un seul facteur plutôt que huit réglages :
la balance entre les bruitages avait été travaillée, il n'y a aucune raison de
la défaire, seulement de baisser l'ensemble sous la voix.

⚠️ `build-sans.py` doit porter le même facteur, sinon le prochain rendu
réintroduira les niveaux d'origine sans que personne le remarque.

Usage :
    python3 _serie/adoucir-ambiance.py            # les neuf
    python3 _serie/adoucir-ambiance.py c1s-…      # un seul
"""

from __future__ import annotations

import pathlib
import re
import shutil
import subprocess
import sys

ICI = pathlib.Path(__file__).resolve().parent
SERIE = ICI.parent
STUDIO = SERIE.parents[1] / "studio-video"
COMPOS = STUDIO / "compositions"

# Le facteur appliqué à tout ce qui n'est pas la voix. 0,25 vaut −12 dB : le
# lit reste perceptible — il porte le registre « sans » — mais il passe sous la
# voix au lieu de lutter avec elle.
FACTEUR_AMBIANCE = 0.25

# Compensation de la voix.
#
# Mesuré : reconstruire le mixage à partir des sources fait perdre 2 dB à la
# voix par rapport au rendu d'origine — le moteur de rendu applique un gain que
# la composition ne déclare pas. Sans cette correction, baisser l'ambiance
# baisserait aussi la voix, ce qui est exactement l'inverse du but.
# +2 dB, et les crêtes restent à −5,6 dB : aucun risque d'écrêtage.
GAIN_VOIX = 1.26

BALISE = re.compile(
    r'<audio\s+id="(?P<id>[^"]+)"\s+src="(?P<src>[^"]+)"\s+'
    r'data-start="(?P<start>[\d.]+)"\s+data-duration="(?P<dur>[\d.]+)"\s+'
    r'data-track-index="\d+"\s+data-volume="(?P<vol>[\d.]+)"',
)


# Posé par `build-sans.py` quand la composition porte déjà les niveaux abaissés.
# Ce script multiplie ce qu'il lit : sans ce garde-fou, l'enchaîner sur une
# composition régénérée donnerait −24 dB au lieu de −12, silencieusement.
MARQUEUR = "ambiance-adoucie="


def pistes(film: str) -> list[dict] | None:
    """Les pistes audio déclarées par la composition, dans l'ordre du fichier.

    Renvoie `None` si la composition porte déjà le facteur : le rendu qui en
    sort est au bon niveau, il n'y a rien à corriger après coup.
    """
    html = (COMPOS / f"{film}.html").read_text(encoding="utf-8")
    if MARQUEUR in html:
        return None
    out = []
    for m in BALISE.finditer(html):
        out.append(
            {
                "id": m.group("id"),
                "src": m.group("src"),
                "debut": float(m.group("start")),
                "duree": float(m.group("dur")),
                "volume": float(m.group("vol")),
            }
        )
    return out


def mesurer(fichier: pathlib.Path) -> str:
    """Sonie intégrée, en LUFS. C'est la mesure qui correspond au ressenti."""
    r = subprocess.run(
        ["ffmpeg", "-nostdin", "-v", "info", "-i", str(fichier),
         "-af", "loudnorm=print_format=summary", "-f", "null", "-"],
        capture_output=True, text=True,
    )
    m = re.search(r"Input Integrated:\s*(-?[\d.]+)\s*LUFS", r.stderr)
    return m.group(1) if m else "?"


def refaire(film: str) -> bool:
    mp4 = SERIE / film / "out" / f"{film}.mp4"
    if not mp4.exists():
        print(f"  ! {film} : pas de rendu")
        return False

    liste = pistes(film)
    if liste is None:
        print(f"  = {film} : composition déjà au bon niveau, re-rendre plutôt "
              f"que corriger après coup")
        return True
    if not liste:
        print(f"  ! {film} : aucune piste audio trouvée dans la composition")
        return False

    entrees: list[str] = []
    filtres: list[str] = []
    etiquettes: list[str] = []

    for i, p in enumerate(liste):
        chemin = STUDIO / p["src"]
        if not chemin.exists():
            print(f"  ! {film} : {p['src']} introuvable")
            return False
        entrees += ["-i", str(chemin)]

        # La voix garde son niveau ; tout le reste passe sous elle.
        gain = (
            p["volume"] * GAIN_VOIX
            if p["id"] == "el-vo"
            else p["volume"] * FACTEUR_AMBIANCE
        )
        # `adelay` place le son à son instant, `apad` évite qu'un mixage
        # s'arrête sur la piste la plus courte.
        ms = int(round(p["debut"] * 1000))
        # ⚠️ `i + 1` et non `i` : l'entrée 0 est le MP4 lui-même. La première
        # version numérotait à partir de zéro, si bien que `[0:a]` désignait le
        # mixage d'origine du film — lequel se retrouvait ajouté à plein niveau
        # au nouveau mixage. Le fichier changeait de taille et la mesure ne
        # bougeait pas d'un décibel : c'est elle qui a trahi l'erreur, pas la
        # relecture.
        filtres.append(
            f"[{i + 1}:a]volume={gain:.4f},aresample=48000,"
            f"adelay={ms}|{ms}[a{i}]"
        )
        etiquettes.append(f"[a{i}]")

    filtres.append(
        f"{''.join(etiquettes)}amix=inputs={len(liste)}:normalize=0:dropout_transition=0[mix]"
    )

    sortie = mp4.with_suffix(".adouci.mp4")
    cmd = [
        "ffmpeg", "-nostdin", "-v", "error", "-y",
        "-i", str(mp4), *entrees,
        "-filter_complex", ";".join(filtres),
        "-map", "0:v", "-map", "[mix]",
        # L'image n'est pas ré-encodée : c'est exactement celle qui a été
        # contrôlée plan par plan.
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-shortest", "-movflags", "+faststart",
        str(sortie),
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  ✗ {film} : {r.stderr.strip()[:300]}")
        sortie.unlink(missing_ok=True)
        return False

    avant = mesurer(mp4)
    apres = mesurer(sortie)
    shutil.move(str(sortie), str(mp4))
    print(f"  ✓ {film:<28} {len(liste):>2} pistes   {avant} → {apres} LUFS")
    return True


def main() -> int:
    films = sys.argv[1:] or sorted(
        d.name for d in SERIE.iterdir() if d.is_dir() and d.name.endswith("-sans")
    )
    print(f"Facteur appliqué à l'ambiance : {FACTEUR_AMBIANCE} "
          f"({20 * __import__('math').log10(FACTEUR_AMBIANCE):.1f} dB)")
    print("La voix off garde son niveau.\n")
    ok = sum(refaire(f) for f in films)
    print(f"\n{ok} / {len(films)} films remixés.")
    return 0 if ok == len(films) else 1


if __name__ == "__main__":
    sys.exit(main())
