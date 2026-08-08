#!/usr/bin/env python3
"""Contrôle un film rendu avant publication.

Trois vérifications, dans cet ordre d'importance :

1. **Aucun cadre écran éteint.** C'est le défaut qui est passé deux fois : un
   clip dont la fenêtre ne couvre pas sa scène laisse voir le fond marine du
   cadre. On mesure la luminance dans la zone du cadre tablette, et on ignore
   les scènes qui n'en ont pas — habillages, cartons pleins écran et schémas
   animés, dont les bornes sont lues dans l'orchestrateur.

   ⚠️ La luminance moyenne seule ne suffit pas. Le KDS de C2 est une
   interface sombre : elle mesure 52, à peine au-dessus d'un cadre vide, et
   le contrôle criait au défaut sur trente images parfaitement bonnes. Ce
   qui sépare vraiment les deux cas n'est pas la moyenne mais le **point le
   plus clair** : un cadre vide est un aplat marine uniforme, une interface
   porte toujours du texte blanc ou une pastille vive. On exige donc les
   deux — moyenne basse *et* aucun pixel clair (`YMAX`).

2. **La durée rendue correspond à la durée déclarée**, à une image près.

3. **Le fichier porte bien une piste audio.** Un film muet passerait le lint.

Usage : python3 _serie/qa-film.py <film>
        python3 _serie/qa-film.py c2-cuisine-pendant
"""

import pathlib
import re
import subprocess
import sys

RACINE = pathlib.Path(__file__).resolve().parents[3]
COMPO = RACINE / "studio-video" / "compositions"
# Zone du cadre tablette dans l'image (cf. serie.py).
CADRE = "1560:546:180:226"
# Un cadre éteint mesure ~43 de moyenne — mais le KDS de C2 en mesure 52, la
# marge est trop mince pour décider seule. Le second seuil tranche : l'aplat
# marine du cadre vide ne dépasse jamais 120, le KDS monte à 241.
SEUIL = 60
SEUIL_CLAIR = 120


def scenes_avec_ecran(film, sous):
    """Bornes des scènes qui portent un cadre écran, lues dans l'orchestrateur."""
    html = (COMPO / f"{film}.html").read_text(encoding="utf-8")
    out = []
    for nom, a, d in re.findall(
            rf'data-composition-src="compositions/{sous}/([a-z0-9-]+)\.html"\s*\n\s*'
            r'data-start="([\d.]+)"\s*\n\s*data-duration="([\d.]+)"', html):
        p = COMPO / sous / f"{nom}.html"
        if not p.exists():
            continue
        contenu = p.read_text(encoding="utf-8")
        # Un cadre écran, et pas un carton plein écran ni un schéma animé.
        if 'class="frame"' in contenu and "assets/screens/" in contenu:
            out.append((nom, float(a), float(a) + float(d)))
    return out


def main():
    film = sys.argv[1]
    sous = film.split("-")[0]
    mp4 = RACINE / "videos" / "foodeatup-9-films" / film / "out" / f"{film}.mp4"
    if not mp4.exists():
        sys.exit(f"{mp4} : absent")

    duree = float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(mp4)], capture_output=True, text=True).stdout)
    pistes = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "stream=codec_type",
         "-of", "csv=p=0", str(mp4)], capture_output=True, text=True).stdout.split()

    html = (COMPO / f"{film}.html").read_text(encoding="utf-8")
    declaree = float(re.search(
        rf'data-composition-id="{re.escape(film)}"[\s\S]{{0,200}}?data-duration="([\d.]+)"',
        html).group(1))

    txt = pathlib.Path(f"/tmp/qa-{film}.txt")
    subprocess.run(
        ["ffmpeg", "-nostdin", "-v", "error", "-i", str(mp4),
         "-vf", f"fps=2,crop={CADRE},signalstats,"
                f"metadata=print:file={txt}",
         "-f", "null", "-"], check=True)

    vals, t, moy = [], None, None
    for ligne in txt.read_text().splitlines():
        ligne = ligne.strip()
        if ligne.startswith("frame:"):
            t = float(ligne.split("pts_time:")[1])
        elif ligne.startswith("lavfi.signalstats.YAVG="):
            moy = float(ligne.split("=")[1])
        elif ligne.startswith("lavfi.signalstats.YMAX="):
            vals.append((t, moy, float(ligne.split("=")[1])))

    fenetres = scenes_avec_ecran(film, sous)
    eteints = [(t, y, ymax) for t, y, ymax in vals
               if y < SEUIL and ymax < SEUIL_CLAIR
               and any(a + 0.5 < t < b - 0.2 for _, a, b in fenetres)]

    print(f"  film              {film}")
    print(f"  durée             {duree:.2f} s "
          f"({'ok' if abs(duree - declaree) < 0.05 else f'≠ déclaré {declaree}'})")
    print(f"  pistes            {' + '.join(pistes)} "
          f"({'ok' if 'audio' in pistes else 'AUCUN SON'})")
    print(f"  scènes à écran    {len(fenetres)}")
    print(f"  cadres éteints    {len(eteints)} "
          f"({'ok' if not eteints else 'DÉFAUT'})")
    for t, y, ymax in eteints[:8]:
        print(f"                    t={t:6.2f} s  moyenne {y:.1f}  point clair {ymax:.0f}")
    sys.exit(1 if (eteints or "audio" not in pistes or abs(duree - declaree) > 0.05) else 0)


if __name__ == "__main__":
    main()
