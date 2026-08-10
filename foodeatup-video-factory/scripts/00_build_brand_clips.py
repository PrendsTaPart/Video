#!/usr/bin/env python3
"""00 — Fabrique les clips de marque réutilisés par les 30 épisodes.

Trois masters, produits UNE fois puis recoupés à la durée exacte de chaque bloc
par `03_assemble.py` :

  assets/brand/sting-logo.mp4   5,0 s — bloc B
  assets/brand/probleme.mp4    12,0 s — bloc C
  assets/brand/outro.mp4        5,0 s — bloc E

Tout est fabriqué en ffmpeg local à partir des PNG de marque déjà présents dans
le dépôt (`assets/brand/*.png`) + la police Anton. AUCUNE génération IA : ni
Higgsfield, ni HeyGen, ni image générée. C'est du motion design maison.

Contrainte de composition : tout le contenu utile tient dans le carré central
1080×1080 (y ∈ [420, 1500]) du canevas 1080×1920, pour que le recadrage 1:1 de
la version LinkedIn ne coupe rien. Ça respecte aussi les safe zones TikTok
(rien sous 320 px du bas, rien au-dessus de 200 px du haut).

Les beats sont calés pour que la troncature à la durée du master 30 s reste
lisible : le dernier beat de chaque clip tombe avant la coupe la plus courte.

Usage :
    python scripts/00_build_brand_clips.py [--force] [--only sting|probleme|outro]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ff, icons  # noqa: E402

ROOT = ff.ROOT
BRAND = ROOT / "assets" / "brand"
WORK = ROOT / "build" / "brand"
FONT = ROOT / "assets" / "fonts" / "Anton-Regular.ttf"

W, H, FPS = 1080, 1920, 30
CREAM, NAVY, BLUE, ORANGE = "0xFCF9E6", "0x0F1A23", "0x007BFF", "0xFFA500"
TILE_W = 150                # côté d'une vignette « logiciel » du bloc C

# Carré central conservé par le recadrage 1:1
SQ_TOP, SQ_BOT = 420, 1500


def _txt(name: str, content: str) -> str:
    """Écrit le texte dans un fichier (évite tout échappement drawtext)."""
    WORK.mkdir(parents=True, exist_ok=True)
    p = WORK / f"txt_{name}.txt"
    p.write_text(content, encoding="utf-8")
    return ff.filter_escape(p)


def _fade_alpha(start: float, dur: float = 0.25) -> str:
    return f"if(lt(t\\,{start})\\,0\\,min(1\\,(t-{start})/{dur}))"


def drawtext(name: str, text: str, *, size: int, color: str, y: int,
             appear: float, x: str = "(w-text_w)/2") -> str:
    return (f"drawtext=fontfile='{ff.filter_escape(FONT)}'"
            f":textfile='{_txt(name, text)}'"
            f":fontsize={size}:fontcolor={color}:x={x}:y={y}"
            f":alpha='{_fade_alpha(appear)}'")


# ---------------------------------------------------------------------------
# B — sting logo (5,0 s ; beat terminé à 1,2 s → lisible même coupé à 2,0 s)
# ---------------------------------------------------------------------------

def build_sting(dst: Path) -> None:
    mark = BRAND / "mark-eight.png"
    word = BRAND / "logo-foodeatup.png"

    # Rebond du pictogramme : 0.55 → 1.10 → 1.00 en 0,45 s (pas de pow(), plus
    # lisible et strictement équivalent à un back.out en deux segments).
    s = ("if(lt(t\\,0.30)\\,0.55+1.8333*t\\,"
         "if(lt(t\\,0.45)\\,1.10-0.6667*(t-0.30)\\,1))")

    fc = (
        f"color=c={CREAM}:s={W}x{H}:r={FPS}:d=5[bg];"
        f"[1:v]format=rgba,scale=w=-1:h='max(4\\,360*({s}))':eval=frame:"
        f"flags=lanczos[mark];"
        f"[bg][mark]overlay=x='(W-w)/2':y='740-h/2':format=auto[s1];"
        f"[2:v]format=rgba,scale=w=680:h=-1:flags=lanczos,"
        f"fade=t=in:st=0.55:d=0.30:alpha=1[word];"
        f"[s1][word]overlay=x='(W-w)/2':y='1080+40*max(0\\,1-(t-0.55)/0.35)':"
        f"format=auto[v]"
    )
    ff.ffmpeg([
        "-f", "lavfi", "-i", f"anullsrc=r=48000:cl=stereo:d=5",
        # -loop 1 : sans ça un PNG ne fournit qu'UNE image, l'animation gèle à
        # t=0 et overlay répète cette première image jusqu'à la fin.
        "-loop", "1", "-framerate", str(FPS), "-t", "5", "-i", str(mark),
        "-loop", "1", "-framerate", str(FPS), "-t", "5", "-i", str(word),
        "-filter_complex", fc, "-map", "[v]", "-map", "0:a",
        "-t", "5.0", *ff.VCODEC, *ff.ACODEC, *ff.TIMESCALE, str(dst),
    ])


# ---------------------------------------------------------------------------
# C — problème (12,0 s ; 3 beats à 0,2 / 2,5 / 5,0 s → tout est passé à 7,5 s)
# ---------------------------------------------------------------------------

def build_probleme(dst: Path) -> None:
    # 10 vignettes « logiciels » qui ne se touchent jamais : 5 colonnes × 2
    # rangées. Elles arrivent une par une — c'est l'accumulation qui raconte
    # le problème, pas la grille finale.
    icones = icons.build(BRAND / "icons", size=TILE_W)
    tw, gap, cols = TILE_W, 24, 5
    x0 = (W - (cols * tw + (cols - 1) * gap)) // 2
    y0 = 720

    fc = [f"color=c={CREAM}:s={W}x{H}:r={FPS}:d=12[bg];"]
    src = "[bg]"
    for i in range(len(icones)):
        appear = 0.35 + i * 0.13
        # fade alpha plutôt que enable : l'apparition est franche mais pas
        # sèche, et l'alpha est nul avant `st` — donc rien ne fuit à t=0.
        fc.append(f"[{i + 1}:v]format=rgba,"
                  f"fade=t=in:st={appear:.2f}:d=0.12:alpha=1[ic{i}];")
        x = x0 + (i % cols) * (tw + gap)
        y = y0 + (i // cols) * (tw + gap)
        fc.append(f"{src}[ic{i}]overlay=x={x}:y={y}:format=auto[st{i}];")
        src = f"[st{i}]"

    chain = [
        drawtext("c_kicker", "LE PROBLÈME", size=44, color=BLUE, y=470,
                 appear=0.15),
        drawtext("c_head", "DIX LOGICIELS", size=104, color=NAVY, y=545,
                 appear=0.20),
        drawtext("c_money", "1 000 € PAR MOIS", size=88, color=ORANGE, y=1120,
                 appear=2.50),
        drawtext("c_none", "ET AUCUN NE SE PARLE", size=62, color=NAVY, y=1260,
                 appear=5.00),
    ]
    fc.append(src + ",".join(chain) + ",format=yuv420p[v]")

    entrees = []
    for p in icones:
        entrees += ["-loop", "1", "-framerate", str(FPS), "-t", "12",
                    "-i", str(p)]
    ff.ffmpeg([
        "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo:d=12", *entrees,
        "-filter_complex", "".join(fc), "-map", "[v]", "-map", "0:a",
        "-t", "12.0", *ff.VCODEC, *ff.ACODEC, *ff.TIMESCALE, str(dst),
    ])


# ---------------------------------------------------------------------------
# E — outro CTA (5,0 s ; beat terminé à 1,8 s → lisible même coupé à 4,0 s)
# ---------------------------------------------------------------------------

def build_outro(dst: Path, cta_url: str) -> None:
    word = BRAND / "logo-foodeatup.png"
    label = cta_url.replace("https://", "").replace("http://", "").rstrip("/")

    chain = [
        drawtext("e_tag", "Avant, pendant, après le service.",
                 size=54, color=NAVY, y=1130, appear=0.85),
        f"drawbox=x=(iw-620)/2:y=1250:w=620:h=116:color={ORANGE}@1:t=fill:"
        f"enable='gte(t\\,1.35)'",
        drawtext("e_cta", label, size=64, color=NAVY, y=1276, appear=1.45),
    ]
    fc = (
        f"color=c={CREAM}:s={W}x{H}:r={FPS}:d=5[bg];"
        f"[1:v]format=rgba,scale=w=760:h=-1:flags=lanczos,"
        f"fade=t=in:st=0.20:d=0.35:alpha=1[word];"
        f"[bg][word]overlay=x='(W-w)/2':y='840-h/2':format=auto[s1];"
        f"[s1]" + ",".join(chain) + ",format=yuv420p[v]"
    )
    ff.ffmpeg([
        "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo:d=5",
        "-loop", "1", "-framerate", str(FPS), "-t", "5", "-i", str(word),
        "-filter_complex", fc, "-map", "[v]", "-map", "0:a",
        "-t", "5.0", *ff.VCODEC, *ff.ACODEC, *ff.TIMESCALE, str(dst),
    ])


BUILDERS = {
    "sting": ("sting-logo.mp4", 5.0),
    "probleme": ("probleme.mp4", 12.0),
    "outro": ("outro.mp4", 5.0),
}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--force", action="store_true",
                    help="regénère même si le fichier existe déjà")
    ap.add_argument("--only", choices=sorted(BUILDERS))
    args = ap.parse_args()

    if not FONT.exists():
        ff.log(f"MISSING_FONT {FONT} — récupère Anton (Google Fonts) d'abord",
               err=True)
        return 2

    cfg = ff.load_config()
    cta = cfg["brand"].get("cta_url", "https://foodeatup.com")
    wanted = [args.only] if args.only else list(BUILDERS)
    rc = 0

    for key in wanted:
        name, expected = BUILDERS[key]
        dst = BRAND / name
        if dst.exists() and not args.force:
            ff.log(f"SKIP   {name} (déjà présent — --force pour regénérer)")
            continue
        ff.log(f"BUILD  {name} …")
        if key == "sting":
            build_sting(dst)
        elif key == "probleme":
            build_probleme(dst)
        else:
            build_outro(dst, cta)

        got = ff.duration(dst)
        n = ff.frames(dst)
        ok = abs(got - expected) <= 0.05
        ff.log(f"       {name}: {got:.3f}s / {n} images "
               f"{'OK' if ok else '⚠ hors cible'}")
        if not ok:
            rc = 1
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
