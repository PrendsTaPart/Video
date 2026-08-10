"""Encodeur PNG + rasteriseur minimal, stdlib uniquement.

Le dépôt n'a pas de dépendance Python et n'a pas le droit de générer d'image
par IA (CLAUDE.md §1 et §3). Pour dessiner les icônes des dix logiciels il
faut donc savoir écrire un PNG soi-même. C'est court : un PNG, c'est trois
chunks (IHDR, IDAT, IEND), des scanlines préfixées d'un octet de filtre, le
tout compressé en zlib.

L'anticrénelage se fait par suréchantillonnage : on dessine sur une grille
`scale` fois plus fine, puis on moyenne chaque bloc. Pas de calcul de
couverture analytique — inutile ici, les formes sont géométriques et les
icônes font 150 px.

Une forme est une simple fonction `(x, y) -> bool` en coordonnées finales.
Ça rend les combinaisons triviales : un contour, c'est `sub(exterieur,
interieur)`.
"""

from __future__ import annotations

import struct
import zlib
from pathlib import Path
from typing import Callable

Shape = Callable[[float, float], bool]
RGB = tuple[int, int, int]


# --------------------------------------------------------------------------
# Écriture PNG
# --------------------------------------------------------------------------

def _chunk(tag: bytes, data: bytes) -> bytes:
    return (struct.pack(">I", len(data)) + tag + data
            + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF))


def write_rgba(path: Path, w: int, h: int, buf: bytearray) -> None:
    """`buf` = w*h*4 octets RGBA non prémultipliés."""
    raw = bytearray()
    for y in range(h):
        raw.append(0)                      # filtre 0 (None) : suffisant ici
        raw += buf[y * w * 4:(y + 1) * w * 4]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(
        b"\x89PNG\r\n\x1a\n"
        + _chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0))
        + _chunk(b"IDAT", zlib.compress(bytes(raw), 9))
        + _chunk(b"IEND", b"")
    )


# --------------------------------------------------------------------------
# Formes
# --------------------------------------------------------------------------

def rrect(x: float, y: float, w: float, h: float, r: float = 0.0) -> Shape:
    """Rectangle à coins arrondis."""
    x1, y1 = x + w, y + h
    r = min(r, w / 2, h / 2)

    def f(px: float, py: float) -> bool:
        if not (x <= px <= x1 and y <= py <= y1):
            return False
        if r <= 0:
            return True
        # Hors des quatre carrés d'angle, c'est forcément dedans.
        cx = x + r if px < x + r else (x1 - r if px > x1 - r else px)
        cy = y + r if py < y + r else (y1 - r if py > y1 - r else py)
        return (px - cx) ** 2 + (py - cy) ** 2 <= r * r
    return f


def disc(cx: float, cy: float, r: float) -> Shape:
    def f(px: float, py: float) -> bool:
        return (px - cx) ** 2 + (py - cy) ** 2 <= r * r
    return f


def seg(x0: float, y0: float, x1: float, y1: float, t: float) -> Shape:
    """Segment d'épaisseur `t`, extrémités arrondies."""
    dx, dy = x1 - x0, y1 - y0
    ll = dx * dx + dy * dy
    half = t / 2

    def f(px: float, py: float) -> bool:
        if ll == 0:
            u = 0.0
        else:
            u = ((px - x0) * dx + (py - y0) * dy) / ll
            u = 0.0 if u < 0 else (1.0 if u > 1 else u)
        qx, qy = x0 + u * dx, y0 + u * dy
        return (px - qx) ** 2 + (py - qy) ** 2 <= half * half
    return f


def poly(points: list[tuple[float, float]]) -> Shape:
    """Polygone plein (lancer de rayon, pair-impair)."""
    n = len(points)

    def f(px: float, py: float) -> bool:
        inside = False
        j = n - 1
        for i in range(n):
            xi, yi = points[i]
            xj, yj = points[j]
            if (yi > py) != (yj > py):
                if px < (xj - xi) * (py - yi) / (yj - yi) + xi:
                    inside = not inside
            j = i
        return inside
    return f


def star(cx: float, cy: float, ro: float, ri: float, n: int = 5) -> Shape:
    import math
    pts = []
    for i in range(n * 2):
        a = -math.pi / 2 + i * math.pi / n
        r = ro if i % 2 == 0 else ri
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return poly(pts)


def sub(a: Shape, b: Shape) -> Shape:
    return lambda px, py: a(px, py) and not b(px, py)


def union(*shapes: Shape) -> Shape:
    return lambda px, py: any(s(px, py) for s in shapes)


def ring(x: float, y: float, w: float, h: float, t: float,
         r: float = 0.0) -> Shape:
    """Contour de rectangle arrondi, épaisseur `t` vers l'intérieur."""
    return sub(rrect(x, y, w, h, r),
               rrect(x + t, y + t, w - 2 * t, h - 2 * t, max(0.0, r - t)))


def circle_ring(cx: float, cy: float, r: float, t: float) -> Shape:
    return sub(disc(cx, cy, r), disc(cx, cy, r - t))


# --------------------------------------------------------------------------
# Canevas
# --------------------------------------------------------------------------

class Canvas:
    """Dessin suréchantillonné, aplati en RGBA à l'écriture."""

    def __init__(self, w: int, h: int, scale: int = 6):
        self.w, self.h, self.s = w, h, scale
        self.W, self.H = w * scale, h * scale
        # index de couleur par sous-pixel ; 0 = transparent
        self.idx = bytearray(self.W * self.H)
        self.palette: list[RGB] = [(0, 0, 0)]

    def fill(self, shape: Shape, color: RGB,
             bbox: tuple[float, float, float, float] | None = None) -> None:
        self.palette.append(color)
        ci = len(self.palette) - 1
        s = self.s
        if bbox is None:
            x0, y0, x1, y1 = 0, 0, self.w, self.h
        else:
            x0, y0, x1, y1 = bbox
        px0 = max(0, int(x0 * s)); px1 = min(self.W, int(x1 * s) + 1)
        py0 = max(0, int(y0 * s)); py1 = min(self.H, int(y1 * s) + 1)
        inv = 1.0 / s
        for yy in range(py0, py1):
            fy = (yy + 0.5) * inv
            row = yy * self.W
            for xx in range(px0, px1):
                if shape((xx + 0.5) * inv, fy):
                    self.idx[row + xx] = ci

    def to_rgba(self) -> bytearray:
        """Moyenne chaque bloc scale×scale. Un sous-pixel transparent
        contribue à l'alpha, pas à la couleur — sinon les bords bavent en
        noir."""
        s, W = self.s, self.W
        n = s * s
        out = bytearray(self.w * self.h * 4)
        pal = self.palette
        for y in range(self.h):
            base = y * s * W
            orow = y * self.w * 4
            for x in range(self.w):
                r = g = b = a = 0
                bx = base + x * s
                for dy in range(s):
                    row = bx + dy * W
                    for dx in range(s):
                        ci = self.idx[row + dx]
                        if ci:
                            cr, cg, cb = pal[ci]
                            r += cr; g += cg; b += cb; a += 255
                o = orow + x * 4
                if a:
                    cnt = a // 255
                    out[o] = r // cnt
                    out[o + 1] = g // cnt
                    out[o + 2] = b // cnt
                    out[o + 3] = a // n
        return out

    def save(self, path: Path) -> None:
        write_rgba(path, self.w, self.h, self.to_rgba())
