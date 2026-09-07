"""Six shorts thématiques FoodEatUp — 9:16, ~25 s, 100 % plans Higgsfield.

Structure commune, calée sur la durée réelle des voix off :
  problème (2 plans, VO a) → solution (2 plans, VO b) → signature (tagline C3) → carton final (C4).

    python3 shorts.py            # les six
    python3 shorts.py haccp      # un seul
"""
import subprocess
import sys

from build import BLUE, INK, ORANGE, WHITE, build_film, card, end_card, hf, logo_corner, to_16x9, vo

MUSIC = "assets/music/musique-underscore-99bpm-alt.mp3"
TAGLINE = ["Une infinité de solutions", "pour gérer votre restaurant"]


def dur(path):
    err = subprocess.run(["ffmpeg", "-i", str(path)], capture_output=True, text=True).stderr
    import re
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", err)
    return int(m[2]) * 60 + float(m[3])


# nom : (code VO, plans du problème [(index, start)], plans de la solution, carton problème, cartons solution)
SHORTS = {
    "haccp": ("SH1", [(85, 0.0), (84, 7.6)], [(143, 2.5), (141, 5.5)],
              "Le contrôle", ["TEMPÉRATURES", "CLASSEUR HACCP"]),
    "stock": ("SH2", [(69, 5.5), (79, 2.5)], [(142, 2.5), (145, 5.0)],
              "L'inventaire", ["STOCK TEMPS RÉEL", "ALERTE AVANT RUPTURE"]),
    "equipe": ("SH3", [(34, 2.5), (33, 2.5)], [(144, 2.5), (66, 7.5)],
               "Le planning", ["PLANNING PAR POSTE", "POINTAGE QR"]),
    "compta": ("SH4", [(47, 2.5), (46, 7.5)], [(25, 2.0), (141, 2.5)],
               "L'addition", ["ADDITION PARTAGÉE", "FACTURES LUES PAR L'IA"]),
    "reservations": ("SH5", [(89, 2.0), (38, 5.5)], [(144, 2.5), (28, 0.5)],
                     "La double réservation", ["PLAN DE SALLE À JOUR", "CAROLINE DÉCROCHE"]),
    "avis": ("SH6", [(86, 2.5), (87, 0.0)], [(63, 5.0), (19, 0.0)],
             "L'avis du soir", ["AVIS CENTRALISÉS", "IRIS PUBLIE"]),
}


def short(name):
    code, probs, sols, titre, puces = SHORTS[name]
    W, H = 1080, 1920
    va, vb = dur(vo(f"{code}a")), dur(vo(f"{code}b"))
    dc3, dc4 = dur(vo("C3")), dur(vo("C4"))
    a = (va + 0.9) / 2          # deux plans pour la ligne « problème »
    b = (vb + 1.1) / 2          # deux plans pour la ligne « solution »
    sig = dc3 + 0.8
    end_d = dc4 + 1.6
    segs = ([dict(src=hf(i), start=s, dur=a) for i, s in probs]
            + [dict(src=hf(i), start=s, dur=b) for i, s in sols]
            + [dict(src=hf(28), start=3.6, dur=sig)])

    def overlays(W, H, times, total):
        ov = []
        p = card(f"{name}-t", W, 300, titre, size=104, color=WHITE, pill=(*INK, 205), y=40)
        ov.append(dict(png=p, t0=0.35, t1=times[2] - 0.15, fin=0.2, fout=0.25, y=H - 700, slide="up"))
        for k, txt in enumerate(puces):
            p = card(f"{name}-p{k}", W, 260, txt, size=74, color=WHITE, pill=(*BLUE, 235), y=50)
            ov.append(dict(png=p, t0=times[2 + k] + 0.15, t1=times[2 + k] + b - 0.1, fin=0.15, fout=0.2,
                           y=H - 660, slide="up"))
        ov.append(dict(png=logo_corner(f"{name}-logo", W, H, scale=0.28, margin=46),
                       t0=times[4], t1=total - end_d, fin=0.3, fout=0.2))
        ov.append(dict(png=end_card(f"{name}-end", W, H, TAGLINE), t0=total - end_d, t1=total + 1, fin=0.5, fout=0.0))
        return ov

    segs.append(dict(src=hf(19), start=8.0, dur=end_d))
    t, acc = [], 0.0
    for s in segs[:-1]:
        t.append(acc)
        acc += s["dur"]
    audio = dict(music=MUSIC, music_start=12.0, music_gain=-12.0, music_fade_out=1.8, src_gain=-17.0, duck=0.32,
                 vo=[(vo(f"{code}a"), 0.3), (vo(f"{code}b"), t[2] + 0.25), (vo("C3"), t[4] + 0.25),
                     (vo("C4"), acc + 0.5)])
    out = build_film(f"foodeatup-short-{name}", W, H, segs, overlays, audio)
    to_16x9(out, f"foodeatup-short-{name}")


if __name__ == "__main__":
    for n in (sys.argv[1:] or list(SHORTS)):
        short(n)
