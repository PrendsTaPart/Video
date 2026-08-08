#!/usr/bin/env python3
"""Insère l'ouverture et la clôture de série dans les films montés.

Michael, 2026-08-08 : chaque film porte le logo à l'ouverture et à la
clôture, une accroche qui annonce la phase et le métier, et se termine sur la
signature de la marque avec sa photo.

Ces deux scènes décalent toute la ligne de temps : chaque scène existante
recule de la durée de l'ouverture, et **tous les éléments audio avec elle** —
voix off, musique, ambiances, bruitages. Refaire cette arithmétique à la main
sur sept films, ce sont sept occasions de décaler une piste d'une demi-seconde
sans s'en apercevoir. Ce script la fait une fois, en relisant l'orchestrateur
plutôt qu'une table écrite à côté : c'est l'orchestrateur qui fait foi.

Le script est **idempotent** : relancé, il détecte l'habillage déjà posé et
ne double rien.

Usage : python3 _serie/ajouter-habillages.py
"""

import pathlib
import re
import sys

INTRO, OUTRO = 4.20, 6.50

# film -> (sous-dossier des scènes, phase, couleur métier)
FILMS = {
    "c1-cuisine-avant":   ("c1", "avant",   "#059669"),
    "c2-cuisine-pendant": ("c2", "pendant", "#059669"),
    "c3-cuisine-apres":   ("c3", "apres",   "#059669"),
    "s1-salle-avant":     ("s1", "avant",   "#F59E0B"),
    "s2-salle-pendant":   ("s2", "pendant", "#F59E0B"),
    "s3-salle-apres":     ("s3", "apres",   "#F59E0B"),
    "d1-direction-avant": ("d1", "avant",   "#475569"),
    "d2-direction-pendant": ("d2", "pendant", "#475569"),
    "d3-direction-apres":  ("d3", "apres",   "#475569"),
}

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
from serie import Serie  # noqa: E402

COMPO = ICI.parents[2] / "studio-video" / "compositions"

SLOT = '''      <div
        id="el-{cid}"
        data-composition-id="{cid}"
        data-composition-src="compositions/{sous}/{cid}.html"
        data-start="{debut:.2f}"
        data-duration="{duree:.2f}"
        data-track-index="1"
        data-width="1920"
        data-height="1080"
      ></div>'''


def decale(html, delta):
    """Recule chaque data-start du fichier de `delta` secondes.

    Les scènes comme les pistes audio : une voix off qui ne suivrait pas
    l'ouverture serait décalée de 4,2 s sur tout le film.
    """
    return re.sub(r'data-start="([\d.]+)"',
                  lambda m: f'data-start="{float(m.group(1)) + delta:.2f}"', html)


def main():
    total_traites = 0
    for film, (sous, phase, metier) in FILMS.items():
        orch = COMPO / f"{film}.html"
        if not orch.exists():
            print(f"  ! {film} : orchestrateur absent, ignoré")
            continue
        html = orch.read_text(encoding="utf-8")

        if f"{film}-intro" in html:
            print(f"  = {film} : habillage déjà posé")
            continue

        scenes = re.findall(r'data-start="([\d.]+)"\s*\n\s*data-duration="([\d.]+)"\s*\n\s*'
                            r'data-track-index="1"', html)
        if not scenes:
            print(f"  ! {film} : aucune scène relue, ignoré")
            continue
        fin_avant = round(float(scenes[-1][0]) + float(scenes[-1][1]), 2)

        s = Serie(metier=metier, sous=sous)
        cid_in, cid_out = f"{film}-intro", f"{film}-outro"
        (s.out / f"{cid_in}.html").write_text(
            s.intro(cid_in, "0.00", f"{INTRO:.2f}", phase), encoding="utf-8")
        (s.out / f"{cid_out}.html").write_text(
            s.outro(cid_out, f"{fin_avant + INTRO:.2f}", f"{OUTRO:.2f}"), encoding="utf-8")

        html = decale(html, INTRO)
        # data-start="0" de la racine a été décalé lui aussi : on le remet.
        html = html.replace(f'data-composition-id="{film}"\n      data-start="{INTRO:.2f}"',
                            f'data-composition-id="{film}"\n      data-start="0"')

        premier = re.search(r'      <div\n        id="el-', html)
        html = (html[:premier.start()]
                + SLOT.format(cid=cid_in, sous=sous, debut=0.0, duree=INTRO) + "\n\n"
                + html[premier.start():])

        ancre = "\n\n      <!-- Voix off continue"
        html = html.replace(
            ancre,
            "\n\n" + SLOT.format(cid=cid_out, sous=sous,
                                 debut=fin_avant + INTRO, duree=OUTRO) + ancre, 1)

        total = round(fin_avant + INTRO + OUTRO, 2)
        html = re.sub(r'(data-composition-id="' + re.escape(film) + r'"[\s\S]{0,200}?data-duration=")[\d.]+(")',
                      lambda m: f"{m.group(1)}{total}{m.group(2)}", html, count=1)

        orch.write_text(html, encoding="utf-8")
        print(f"  + {film:20} {fin_avant:6.2f} s -> {total:6.2f} s "
              f"({len(scenes)} scènes décalées de {INTRO} s)")
        total_traites += 1
    print(f"\n{total_traites} film(s) habillé(s)")


if __name__ == "__main__":
    main()
