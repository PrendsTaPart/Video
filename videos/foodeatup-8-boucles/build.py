#!/usr/bin/env python3
"""Assemble les frames capturées et la voix off en MP4.

Chaîne : `capture.cjs` produit les PNG → ce script les encode et y colle la VO,
une piste par plan, posée à l'instant exact du plan correspondant.

Règles audio reprises de `videos/FOODEATUP-TUTORIELS-WORKFLOW.md`, qui fait foi :

- `loudnorm` est appliqué **par ligne**, avant `adelay`, jamais sur le mix. Le
  mix contient beaucoup de silence entre les lignes ; un loudnorm global
  sous-estime la loudness et sur-amplifie la parole (pics relevés à +1,9 dB).
- Le limiteur de sortie passe `level=disabled` **explicitement**. Le paramètre
  est actif par défaut et renormalise à 0 dB APRÈS limitation, ce qui annule le
  plafond : sans lui, `limit=` n'a aucun effet réel.
- Plafond visé à 0,6 (~-4,4 dB) et non 0,85 : l'encodage AAC peut réintroduire
  1 à 2 dB de dépassement près du plafond.
"""
import argparse
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "tools"))
from build_html import (  # noqa: E402
    AMORCE, FORMATS, RESPIRATION, duree_mp3, ffmpeg,
)

FPS = 30


def run(cmd: list[str], quoi: str) -> None:
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-3000:], file=sys.stderr)
        sys.exit(f"ERREUR ffmpeg — {quoi}")


def pic_dbfs(mp4: pathlib.Path) -> float:
    """Pic réel du fichier FINAL encodé.

    `volumedetect` seul est insuffisant : il arrondit et peut afficher « 0.0 dB »
    sur un clip qui ne l'est pas. On lit donc `astats`.
    """
    out = subprocess.run(
        [ffmpeg(), "-i", str(mp4), "-af", "astats", "-f", "null", "-"],
        capture_output=True, text=True,
    ).stderr
    pics = [
        float(l.split(":")[1])
        for l in out.splitlines()
        if "Peak level dB" in l and "inf" not in l
    ]
    return max(pics) if pics else float("-inf")


def assembler(video: dict, fmt_nom: str, frames: pathlib.Path,
              sortie: pathlib.Path, types: dict) -> None:
    F = FORMATS[fmt_nom]
    dossier = HERE / video["dossier"]
    vo = dossier / "assets" / "vo"

    # Position de chaque ligne sur la timeline : même calcul que build_html.py,
    # sinon la voix décroche de l'image.
    curseur, pistes = 0.0, []
    for p in video["plans"]:
        mp3 = vo / f"p{p['n']:02d}.mp3"
        if not mp3.exists():
            sys.exit(f"ERREUR — VO manquante : {mp3}")
        parole = duree_mp3(mp3)
        pistes.append((mp3, curseur + AMORCE))
        curseur += parole + AMORCE + 0.75 + RESPIRATION.get(types[p["n"]], 0.0)
    duree = curseur

    # Garde-fou : aucune ligne ne doit démarrer avant la fin de la précédente.
    # Un chevauchement de voix a déjà été livré une fois sur cette série.
    for i in range(1, len(pistes)):
        fin_prec = pistes[i - 1][1] + duree_mp3(pistes[i - 1][0])
        if pistes[i][1] < fin_prec:
            sys.exit(
                f"ERREUR — chevauchement VO : la ligne {i + 1} démarre à "
                f"{pistes[i][1]:.2f}s, la précédente finit à {fin_prec:.2f}s."
            )

    entrees = ["-framerate", str(FPS), "-i", str(frames / "f%05d.png")]
    for mp3, _ in pistes:
        entrees += ["-i", str(mp3)]

    # Une chaîne par ligne : loudnorm d'abord, décalage ensuite.
    # `aformat` après loudnorm n'est pas cosmétique : loudnorm rééchantillonne en
    # interne et ressort en 192 kHz, ce qui donnait un MP4 à 96 kHz mono. On
    # ramène chaque ligne en 48 kHz stéréo avant de mixer.
    filtres = []
    for i, (_, t0) in enumerate(pistes):
        filtres.append(
            f"[{i + 1}:a]loudnorm=I=-16:TP=-1.5:LRA=11,"
            "aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,"
            f"adelay={int(t0 * 1000)}|{int(t0 * 1000)}[a{i}]"
        )
    filtres.append(
        "".join(f"[a{i}]" for i in range(len(pistes)))
        + f"amix=inputs={len(pistes)}:normalize=0:dropout_transition=0,"
        "alimiter=limit=0.6:level=disabled,"
        f"apad,atrim=0:{duree:.3f}[aout]"
    )

    sortie.parent.mkdir(parents=True, exist_ok=True)
    run(
        [ffmpeg(), "-y", *entrees,
         "-filter_complex", ";".join(filtres),
         "-map", "0:v", "-map", "[aout]",
         "-c:v", "libx264", "-preset", "medium", "-crf", "18",
         "-pix_fmt", "yuv420p", "-r", str(FPS),
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
         "-t", f"{duree:.3f}",
         "-movflags", "+faststart", str(sortie)],
        f"{video['slug']} / {fmt_nom}",
    )

    pic = pic_dbfs(sortie)
    marge = "OK" if pic <= -3.0 else "!! TROP FORT"
    print(f"  {sortie.name}  {duree:.2f}s  {F['W']}×{F['H']}  "
          f"pic {pic:+.1f} dBFS  {marge}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--format", default="master", choices=["master", "reel"])
    args = ap.parse_args()

    manifeste = json.loads((HERE / "boucles.json").read_text(encoding="utf-8"))
    video = next(v for v in manifeste["videos"] if v["slug"] == args.slug)

    types = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}
    if video["slug"] == "boucle-00-principe":
        types = {1: 1, 2: 2, 3: 5, 4: 2, 5: 7, 6: 6}

    suffixe = "" if args.format == "master" else "-reel"
    frames = HERE / "work" / f"{args.slug}{suffixe}"
    if not frames.exists():
        sys.exit(f"ERREUR — frames absentes : {frames}\n"
                 f"Lance d'abord : node capture.cjs --html {video['dossier']}"
                 f"/index{suffixe}.html --out work/{args.slug}{suffixe}")

    sortie = HERE / video["dossier"] / "out" / f"{args.slug}{suffixe}.mp4"
    assembler(video, args.format, frames, sortie, types)


if __name__ == "__main__":
    main()
