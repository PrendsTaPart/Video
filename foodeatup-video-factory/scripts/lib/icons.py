"""Les dix icônes « logiciels » du bloc C, dessinées en géométrie pure.

Le bloc C raconte « dix logiciels, mille euros par mois, et aucun ne se
parle ». Dix carrés gris identiques ne disaient pas ça : il faut dix vignettes
visiblement DIFFÉRENTES, comme dix applis qui n'ont rien à voir entre elles.

Ce sont des pictogrammes génériques de CATÉGORIE (caisse, livraison,
réservation…), pas des logos de marques réelles : on n'a pas à reproduire la
marque d'un tiers dans une pub comparative, et ça n'apporterait rien au gag.

Tout est tracé avec `lib.png` — aucune image générée par IA, aucune dépendance.
Les formes sont décrites dans un carré de 100 unités puis mises à l'échelle,
ce qui permet de changer la taille des tuiles sans retoucher un seul chiffre.
"""

from __future__ import annotations

from pathlib import Path

from . import png

BLANC = (255, 255, 255)

# Dix teintes franchement distinctes, toutes assez sombres pour qu'un
# pictogramme blanc reste lisible, et qui se détachent du fond crème.
LOGICIELS: list[tuple[str, str, tuple[int, int, int]]] = [
    ("caisse",      "Caisse",       (226,  87,  76)),
    ("livraison",   "Livraison",    (224, 123,  57)),
    ("reservation", "Réservation",  (184, 144,  31)),
    ("stock",       "Stock",        ( 92, 158,  74)),
    ("planning",    "Planning",     ( 46, 158, 143)),
    ("compta",      "Comptabilité", ( 60, 127, 177)),
    ("marketing",   "Marketing",    ( 79,  91, 168)),
    ("fidelite",    "Fidélité",     (129,  85, 168)),
    ("site",        "Site web",     (182,  82, 136)),
    ("kds",         "KDS",          (107, 114, 128)),
]


def _draw(nom: str, c: png.Canvas, u, fond: tuple[int, int, int]) -> None:
    """Pictogramme blanc ; `u` convertit les unités (0-100) en pixels.
    Certaines formes sont retracées en couleur de fond : c'est ce qui creuse
    une roue ou un point sans avoir besoin d'un canal de découpe."""
    def W(shape, x0, y0, x1, y1):
        c.fill(shape, BLANC, (u(x0), u(y0), u(x1), u(y1)))

    def F(shape, x0, y0, x1, y1):
        c.fill(shape, fond, (u(x0), u(y0), u(x1), u(y1)))

    S = lambda *a: png.seg(*[u(v) for v in a[:4]], u(a[4]))       # noqa: E731
    R = lambda x, y, w, h, r=0: png.rrect(u(x), u(y), u(w), u(h), u(r))
    RG = lambda x, y, w, h, t, r=0: png.ring(                      # noqa: E731
        u(x), u(y), u(w), u(h), u(t), u(r))
    D = lambda cx, cy, r: png.disc(u(cx), u(cy), u(r))             # noqa: E731
    P = lambda pts: png.poly([(u(x), u(y)) for x, y in pts])       # noqa: E731

    if nom == "caisse":                     # ticket de caisse dentelé
        W(P([(32, 18), (68, 18), (68, 78), (62, 71), (56, 78), (50, 71),
             (44, 78), (38, 71), (32, 78)]), 30, 16, 70, 80)
        for y in (34, 46):
            F(S(40, y, 60, y, 4), 38, y - 3, 62, y + 3)
        F(S(40, 58, 53, 58, 4), 38, 55, 55, 61)

    elif nom == "livraison":                # camion de livraison
        W(R(16, 40, 38, 26, 4), 14, 38, 56, 68)
        W(P([(56, 48), (70, 48), (79, 58), (79, 66), (56, 66)]), 54, 46, 81, 68)
        W(D(31, 70, 9), 21, 60, 41, 80)
        W(D(69, 70, 9), 59, 60, 79, 80)
        F(D(31, 70, 4), 26, 65, 36, 75)
        F(D(69, 70, 4), 64, 65, 74, 75)

    elif nom == "reservation":              # calendrier
        W(S(36, 18, 36, 30, 6), 32, 14, 40, 33)
        W(S(64, 18, 64, 30, 6), 60, 14, 68, 33)
        W(RG(20, 24, 60, 56, 5, 6), 18, 22, 82, 82)
        W(R(20, 24, 60, 14), 18, 22, 82, 40)
        for cx in (34, 50, 66):
            W(D(cx, 54, 4.5), cx - 6, 48, cx + 6, 60)
        for cx in (34, 50):
            W(D(cx, 68, 4.5), cx - 6, 62, cx + 6, 74)

    elif nom == "stock":                    # trois cageots empilés
        W(RG(34, 22, 32, 24, 5, 3), 32, 20, 68, 48)
        W(RG(16, 52, 32, 26, 5, 3), 14, 50, 50, 80)
        W(RG(52, 52, 32, 26, 5, 3), 50, 50, 86, 80)

    elif nom == "planning":                 # horloge
        W(png.circle_ring(u(50), u(50), u(28), u(6)), 20, 20, 80, 80)
        W(S(50, 50, 50, 32, 6), 46, 28, 54, 54)
        W(S(50, 50, 64, 57, 6), 46, 46, 68, 61)

    elif nom == "compta":                   # document + lignes
        W(RG(28, 16, 44, 68, 5, 5), 26, 14, 74, 86)
        for y in (36, 50, 64):
            fin = 62 if y != 64 else 54
            W(S(38, y, fin, y, 5), 36, y - 4, 64, y + 4)

    elif nom == "marketing":                # mégaphone
        W(P([(22, 42), (52, 26), (52, 74), (22, 58)]), 20, 24, 54, 76)
        W(R(52, 42, 12, 16, 3), 50, 40, 66, 60)
        W(S(70, 38, 78, 33, 5), 66, 30, 80, 41)
        W(S(70, 50, 80, 50, 5), 66, 46, 82, 54)
        W(S(70, 62, 78, 67, 5), 66, 59, 80, 70)

    elif nom == "fidelite":                 # étoile
        W(png.star(u(50), u(52), u(30), u(13)), 18, 18, 82, 84)

    elif nom == "site":                     # fenêtre de navigateur
        W(RG(18, 24, 64, 52, 5, 6), 16, 22, 84, 78)
        W(R(18, 24, 64, 14), 16, 22, 84, 40)
        for cx in (27, 36, 45):
            F(D(cx, 31, 3), cx - 5, 26, cx + 5, 36)
        W(S(30, 52, 70, 52, 5), 28, 48, 72, 56)
        W(S(30, 64, 56, 64, 5), 28, 60, 58, 68)

    else:                                   # kds — écran + validation
        W(RG(18, 24, 64, 44, 5, 6), 16, 22, 84, 70)
        W(S(50, 68, 50, 78, 8), 44, 64, 56, 82)
        W(S(34, 82, 66, 82, 7), 30, 78, 70, 86)
        W(S(34, 46, 45, 56, 7), 29, 41, 50, 61)
        W(S(45, 56, 65, 37, 7), 40, 32, 70, 61)


def build(dst_dir: Path, size: int = 150, scale: int = 6) -> list[Path]:
    """Écrit les dix PNG et renvoie leurs chemins, dans l'ordre d'apparition."""
    u = lambda v: v * size / 100.0                                 # noqa: E731
    out: list[Path] = []
    for i, (nom, _label, teinte) in enumerate(LOGICIELS):
        c = png.Canvas(size, size, scale)
        c.fill(png.rrect(0, 0, size, size, u(24)), teinte)
        _draw(nom, c, u, teinte)
        p = dst_dir / f"{i:02d}-{nom}.png"
        c.save(p)
        out.append(p)
    return out
