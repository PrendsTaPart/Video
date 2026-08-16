#!/usr/bin/env python3
"""Retire la voix incrustée d'un plan Higgsfield, en gardant l'ambiance.

    python3 scripts/enlever-voix.py bandes-annonces le-coup-de-feu-S1 …
    python3 scripts/enlever-voix.py hooks EP506 EP507 …
    python3 scripts/enlever-voix.py hooks            (tous ceux qui manquent)

Le problème
-----------
Seedance prononce les répliques écrites dans le prompt : chaque plan arrive
avec une voix française incrustée dans sa piste. Quand le montage pose
par-dessus une voix ElevenLabs — la même phrase sur une bande-annonce, une
punchline sur un chapitre du film — on entend deux voix. Baisser le plan ne
règle rien : ça baisse l'ambiance autant que la voix, et la voix reste
audible dessous.

Pourquoi une séparation de sources
----------------------------------
Les deux canaux du plan sont quasi identiques — la différence L−R est
mesurée 24 dB sous le signal — donc l'opposition de phase, le vieux truc
« karaoké », n'a rien à annuler. Il faut séparer voix et fond, ce que fait
Demucs.

Mesuré sur la bande-annonce de la saison 1 du Coup de Feu :

    pendant la parole   -25,2 dB  ->  -49,5 dB   (24 dB de voix en moins)
    hors parole         -36,8 dB  ->  -40,7 dB   (3,9 dB d'ambiance perdus)

La voix disparaît, le lieu reste. C'est le compromis qu'on cherchait.

Ce que le script écrit
----------------------
`assets/<famille>-sans-voix/<nom>.m4a` — la piste d'ambiance seule. Les
scripts de montage la préfèrent au son du plan quand elle existe, et
retombent sur le plan d'origine sinon : un montage ne casse jamais faute de
séparation.

Le fichier vidéo n'est pas réécrit. Séparer coûte une vingtaine de secondes
par plan, on ne le refait donc pas si la sortie est déjà là.
"""
import pathlib
import shutil
import subprocess
import sys
import tempfile

R = pathlib.Path(__file__).resolve().parent.parent


def separe(source: pathlib.Path, dest: pathlib.Path) -> str:
    """Écrit l'ambiance seule de `source` dans `dest`. Renvoie un mot d'état."""
    if dest.exists() and dest.stat().st_size > 0:
        return "déjà fait"
    dest.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        wav = tmp / "entree.wav"
        subprocess.run(
            ["ffmpeg", "-v", "error", "-y", "-i", str(source),
             "-vn", "-ac", "2", "-ar", "44100", str(wav)], check=True)

        # --two-stems=vocals ne sort que deux pistes au lieu de quatre : c'est
        # trois fois plus rapide, et « no_vocals » est exactement ce qu'on veut.
        subprocess.run(
            [sys.executable, "-m", "demucs", "--two-stems=vocals", "-n", "htdemucs",
             "-o", str(tmp / "out"), "--filename", "{stem}.{ext}", str(wav)],
            check=True, capture_output=True, text=True)

        fond = tmp / "out" / "htdemucs" / "no_vocals.wav"
        if not fond.exists():
            raise FileNotFoundError(f"séparation sans sortie pour {source.name}")
        subprocess.run(
            ["ffmpeg", "-v", "error", "-y", "-i", str(fond),
             "-c:a", "aac", "-b:a", "192k", "-ar", "48000", str(dest)], check=True)
    return "séparé"


def main(args):
    if not args:
        sys.exit("usage: enlever-voix.py <famille> [nom …]\n"
                 "  famille : « hooks » ou « bandes-annonces »")
    famille, noms = args[0], args[1:]
    src_dir = R / "assets" / famille
    dst_dir = R / "assets" / f"{famille}-sans-voix"
    if not src_dir.is_dir():
        sys.exit(f"{src_dir} n'existe pas")

    if not noms:
        noms = sorted(p.stem for p in src_dir.glob("*.mp4"))

    faits = sautes = rates = 0
    for n in noms:
        src = src_dir / f"{n}.mp4"
        if not src.exists():
            print(f"  {n:38s} pas de plan")
            rates += 1
            continue
        try:
            etat = separe(src, dst_dir / f"{n}.m4a")
            print(f"  {n:38s} {etat}")
            faits += etat == "séparé"
            sautes += etat == "déjà fait"
        except (subprocess.CalledProcessError, FileNotFoundError) as err:
            detail = getattr(err, "stderr", "") or str(err)
            print(f"  {n:38s} ÉCHEC — {detail[:160]}")
            rates += 1

    print(f"\nséparés : {faits} | déjà faits : {sautes} | en échec : {rates}")
    if rates:
        print("Les plans en échec gardent leur son d'origine au montage.")


if __name__ == "__main__":
    main(sys.argv[1:])
