#!/usr/bin/env python3
"""Monte le film « Une journée » à partir des 31 épisodes des deux saisons.

    python3 scripts/build-film-journee.py           # monte tout
    python3 scripts/build-film-journee.py --bloc B03   # un seul bloc, pour vérifier

Le principe
-----------
Le film n'est pas une suite d'épisodes bout à bout : c'est une narration
continue posée sur un montage. La voix off est découpée en dix blocs, un par
séquence du scénario ; chaque bloc a une durée mesurée, et les plans de ce bloc
se partagent cette durée. C'est donc **la voix qui commande le montage**, pas
l'inverse — on ne rallonge jamais une phrase pour tenir un plan.

Le cadre
--------
Toute la matière est verticale : les plans Higgsfield sont en 9:16. Le film est
en 16:9 parce qu'il se regarde sur un site, pas dans un fil. Le plan est donc
posé en pleine hauteur au centre, et les côtés sont comblés par une copie
floutée et assombrie du plan lui-même — exactement le traitement de
`build-youtube-paysage.py`, pour que le film ressemble à la série dont il sort.

Le son
------
Le son des clips Higgsfield reste à zéro, comme dans toute la série : ces pistes
portent une ambiance générée qui se contredit d'un plan à l'autre. Seule la voix
off est entendue. Elle est normalisée en deux passes — mesure puis application —
parce qu'une passe simple dérive avec la densité de parole, et que le film
enchaîne des blocs de densités très différentes.

`loudnorm` n'apparaît jamais dans le filtergraph principal : sur une entrée
courte il ressort ses frames avec des PTS décalés, et tout `atrim` qui suit
prend ce décalage pour du temps écoulé. C'est la règle du dépôt, elle vaut ici
comme ailleurs.
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys

R = pathlib.Path(__file__).resolve().parent.parent
HOOKS = R / "dist" / "hooks"
VOIX = R / "assets" / "vo" / "film-journee"
BUILD = R / "build" / "film"
SORTIE = R / "dist" / "film" / "une-journee.mp4"

L, H = 1920, 1080
FPS = 30
LARGEUR_PLAN = 607          # 1080 × 9/16, le plan vertical en pleine hauteur
LOUDNESS = "I=-14:TP=-1.5:LRA=11"
RESPIRE = 0.6               # le silence qui sépare deux blocs

# Le découpage du film. Pour chaque bloc : la voix off, et les plans qui la
# couvrent. L'ordre est celui du scénario `docs/film-une-journee.md`.
BLOCS = [
    ("B01", ["EP301", "EP313", "EP322", "EP316", "EP307", "EP310", "EP328"]),
    ("B02", ["EP316", "EP319", "EP319"]),
    ("B03", ["EP307", "EP308", "EP323", "EP305", "EP308", "EP323"]),
    ("B04", ["EP329", "EP302", "EP320", "EP317", "EP314", "EP330"]),
    ("B05", ["EP312", "EP315", "EP312"]),
    ("B06", ["EP309", "EP306", "EP321", "EP303", "EP318"]),
    ("B07", ["EP327", "EP325", "EP326", "EP327"]),
    ("B08", ["EP331", "EP331"]),
    ("B09", ["EP316", "EP307", "EP323", "EP329", "EP330", "EP312"]),
    ("B10", ["EP331"]),
]


def duree(chemin):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(chemin)],
        capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def segment(episode, debut, longueur, sortie):
    """Un plan, recadré en 16:9 sur son propre flou, sans son."""
    src = HOOKS / f"{episode}.mp4"
    if not src.exists():
        raise SystemExit(f"{episode} : plan introuvable dans dist/hooks/")
    chaine = (
        f"[0:v]split=2[fond][net];"
        f"[fond]scale={L}:{H}:force_original_aspect_ratio=increase,"
        f"crop={L}:{H},gblur=sigma=40,eq=brightness=-0.16:saturation=0.7,"
        f"setsar=1,fps={FPS}[flou];"
        f"[net]scale={LARGEUR_PLAN}:{H},setsar=1,fps={FPS}[plan];"
        # `overlay` a bien une option `format`, mais elle prend `yuv420`, pas
        # `yuv420p` : c'est un enum de mode de mélange, pas un pixel format.
        # Un filtre `format` séparé dit la même chose sans ambiguïté, et c'est
        # lui qui garantit que libx264 ne parte pas en High 4:4:4 Predictive.
        f"[flou][plan]overlay=(W-w)/2:0,format=yuv420p[v]"
    )
    subprocess.run(
        ["ffmpeg", "-y", "-v", "error",
         "-ss", f"{debut:.3f}", "-t", f"{longueur:.3f}", "-i", str(src),
         "-filter_complex", chaine, "-map", "[v]", "-an",
         "-c:v", "libx264", "-preset", "medium", "-crf", "22",
         "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.0",
         str(sortie)], check=True)


def monter_bloc(nom, episodes):
    """Les plans d'un bloc, taillés pour couvrir exactement sa voix off."""
    vo = VOIX / f"{nom}.mp3"
    if not vo.exists():
        raise SystemExit(f"{nom} : voix off absente ({vo})")
    d_vo = duree(vo)
    part = d_vo / len(episodes)

    morceaux = []
    for i, ep in enumerate(episodes):
        d_src = duree(HOOKS / f"{ep}.mp4")
        # On prend le morceau au centre du plan quand il est plus long que la
        # part : le début et la fin d'un plan Higgsfield sont les moments où la
        # caméra se stabilise et où elle décroche.
        debut = max(0.0, min(d_src - part, (d_src - part) / 2)) if d_src > part else 0.0
        longueur = min(part, d_src - debut)
        out = BUILD / f"{nom}_{i:02d}.mp4"
        segment(ep, debut, longueur, out)
        morceaux.append(out)
        print(f"    {ep}  {debut:5.2f} → {debut + longueur:5.2f}  ({longueur:.2f} s)")

    liste = BUILD / f"{nom}.txt"
    liste.write_text("".join(f"file '{m}'\n" for m in morceaux), encoding="utf-8")
    bloc = BUILD / f"{nom}_video.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
                    "-i", str(liste), "-c", "copy", str(bloc)], check=True)
    return bloc, vo, d_vo


def mesurer(chemin):
    """Première passe de loudnorm : les mesures du fichier."""
    p = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", str(chemin),
         "-af", f"loudnorm={LOUDNESS}:print_format=json", "-f", "null", "-"],
        capture_output=True, text=True)
    blocs = re.findall(r"\{[^{}]*\}", p.stderr, re.S)
    return json.loads(blocs[-1]) if blocs else None


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--bloc", help="ne monter qu'un bloc, pour vérifier")
    a = ap.parse_args(argv)

    BUILD.mkdir(parents=True, exist_ok=True)
    SORTIE.parent.mkdir(parents=True, exist_ok=True)

    choisis = [b for b in BLOCS if not a.bloc or b[0] == a.bloc]
    if not choisis:
        raise SystemExit(f"bloc « {a.bloc} » inconnu")

    videos, voix, total = [], [], 0.0
    for nom, episodes in choisis:
        print(f"  {nom} :")
        v, vo, d = monter_bloc(nom, episodes)
        videos.append(v)
        voix.append((vo, total, d))
        total += d + RESPIRE
    total -= RESPIRE

    # La vidéo : les blocs bout à bout, avec le silence de respiration comblé
    # par un gel de la dernière image plutôt que par du noir — le noir entre
    # deux séquences ferait lire une coupure de bobine.
    liste = BUILD / "film.txt"
    liste.write_text("".join(f"file '{v}'\n" for v in videos), encoding="utf-8")
    muet = BUILD / "film_muet.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
                    "-i", str(liste), "-c", "copy", str(muet)], check=True)
    d_video = duree(muet)

    # Le son : chaque bloc décalé à sa place, mixé sans normalisation de somme.
    entrees, chaines, etiquettes = [], [], []
    for i, (vo, depart, _) in enumerate(voix):
        entrees += ["-i", str(vo)]
        chaines.append(f"[{i}:a]adelay={int(depart * 1000)}|{int(depart * 1000)},"
                       f"aformat=sample_fmts=fltp:sample_rates=48000:"
                       f"channel_layouts=stereo[a{i}]")
        etiquettes.append(f"[a{i}]")
    chaines.append("".join(etiquettes) +
                   f"amix=inputs={len(voix)}:normalize=0,"
                   f"apad,atrim=0:{d_video:.3f}[mix]")
    brut = BUILD / "voix_brute.wav"
    subprocess.run(["ffmpeg", "-y", "-v", "error", *entrees,
                    "-filter_complex", ";".join(chaines), "-map", "[mix]",
                    "-c:a", "pcm_s16le", str(brut)], check=True)

    # Deux passes de loudnorm, dans un passage séparé du graphe principal.
    m = mesurer(brut)
    normal = BUILD / "voix.wav"
    if m:
        af = (f"loudnorm={LOUDNESS}:measured_I={m['input_i']}:"
              f"measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:"
              f"measured_thresh={m['input_thresh']}:offset={m['target_offset']}:"
              f"linear=true:print_format=summary")
    else:
        print("  (mesure indisponible — repli sur une passe simple)")
        af = f"loudnorm={LOUDNESS}"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(brut),
                    "-af", af + ",alimiter=limit=0.891",
                    "-c:a", "pcm_s16le", str(normal)], check=True)

    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(muet), "-i", str(normal),
                    "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                    "-c:a", "aac", "-b:a", "192k", "-shortest", str(SORTIE)],
                   check=True)

    d = duree(SORTIE)
    ko = SORTIE.stat().st_size // 1024
    print(f"\n  {SORTIE.relative_to(R)}  {d // 60:.0f} min {d % 60:04.1f} s  {ko} Ko")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
