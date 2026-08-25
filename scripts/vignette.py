#!/usr/bin/env python3
"""Compose les vignettes 9:16 du catalogue Le Quai / Plani't en pur Python + Pillow.

Réutilisable pour les 186 épisodes du catalogue. Aucun navigateur, aucune capture
d'écran, aucune requête réseau : ce script est un compositeur d'image pur — il prend
en entrée l'image source déjà téléchargée (image_vignette) et les données déjà
récupérées via obtenir_episode / obtenir_charte, et produit un PNG déterministe.

ENTRÉES
  --charte     JSON = sortie brute de l'outil obtenir_charte (couleur encre, etc.)
  --manifest   JSON = liste d'épisodes, un objet par épisode :
                 {
                   "id": "...",
                   "titre": "...",
                   "serie_nom": "Le Quai",
                   "saison_numero": 1,
                   "numero": 1,
                   "serie_couleur": "#7A31F0",
                   "image_vignette_local": "/chemin/vers/le/png/deja/telecharge.png"
                 }
               (tous ces champs, sauf image_vignette_local, viennent tels quels de
               obtenir_episode — jamais reconstruits ou devinés)
  --fonts-dir  dossier contenant les .ttf/.otf Alte Haas Grotesk (par défaut
               assets/fonts/ à la racine du dépôt). Si les fichiers attendus
               manquent, le script s'arrête AVANT de traiter le moindre épisode :
               il ne compose jamais avec une police de repli (Sora/Inter/système).
  --logo       pictogramme Plani't blanc (PNG RGBA). Par défaut le mark blanc déjà
               versionné dans ce dépôt pour Le Quai.
  --out-dir    dossier de sortie des PNG

SORTIE
  Un fichier <out-dir>/<id>.png par épisode, plus un rapport JSON sur stdout
  (dimensions, luminosité du tiers supérieur, poids, statut) pour chaque épisode.

DÉTERMINISME
  Aucun aléatoire, aucun horodatage, aucune métadonnée PNG variable. À données et
  polices identiques, le PNG produit est strictement identique d'une exécution à
  l'autre (mêmes octets).
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

try:
    import numpy as _np
except ImportError:  # repli pur Python, plus lent mais sans dépendance neuve
    _np = None

# ---------------------------------------------------------------------------
# Constantes de composition — reflètent exactement les règles de l'usine du site.
# ---------------------------------------------------------------------------

CANVAS_W = 1440
CANVAS_H = 2560

MARGIN = 128

DESATURATION = 0.15  # 15 % — jamais d'assombrissement global du fond

VOILE_TRANSPARENT_UNTIL = 0.45  # fraction de hauteur : 0 % d'opacité jusque-là
VOILE_MAX_OPACITY = 0.88        # opacité atteinte en bas du cadre

FILET_WIDTH = 5
FILET_X = 128

BANDEAU_SIZE = 44
BANDEAU_TRACKING_EM = 0.18
BANDEAU_GAP_ABOVE_TITLE = 20  # px entre le bas du bandeau et le haut du titre

TITLE_SIZE_PRIMARY = 112
TITLE_SIZE_FALLBACK = 96
TITLE_LINE_HEIGHT = 1.02
TITLE_BASELINE_FRAC = 0.88  # base de la dernière ligne à 88 % de la hauteur
TITLE_MAX_LINES = 2
TITLE_COLOR = (255, 255, 255, 255)

LOGO_SIZE = 128  # hauteur cible en px, largeur proportionnelle

TEXT_SAFE_BELOW_Y = 2300  # aucun pixel de texte sous cette ligne

TOP_THIRD_MIN_LUMINOSITY = 25.0  # % — contrôle avant dépôt
MAX_PNG_BYTES = 4 * 1024 * 1024

FONT_REGULAR_DEFAULT_NAMES = ["AlteHaasGrotesk-Regular.ttf", "AlteHaasGrotesk-Regular.otf"]
FONT_BLACK_DEFAULT_NAMES = [
    "AlteHaasGrotesk-ExtraBold.ttf",
    "AlteHaasGrotesk-Black.ttf",
    "AlteHaasGrotesk-800.ttf",
    "AlteHaasGrotesk-ExtraBold.otf",
]


class MissingFontError(RuntimeError):
    pass


class VignetteError(RuntimeError):
    """Erreur propre à un épisode : on l'annonce et on passe au suivant."""


# ---------------------------------------------------------------------------
# Polices — jamais de repli. On s'arrête si Alte Haas Grotesk est absente.
# ---------------------------------------------------------------------------

def _find_font(fonts_dir: Path, candidate_names: list[str]) -> Path | None:
    for name in candidate_names:
        p = fonts_dir / name
        if p.is_file():
            return p
    return None


def require_fonts(fonts_dir: Path) -> tuple[Path, Path]:
    """Localise les deux graisses requises. Lève MissingFontError sinon.

    Ne cherche JAMAIS Sora/Inter/une police système : c'est le point explicite
    de cette fonction. Si Alte Haas Grotesk n'est pas dans fonts_dir, on arrête
    tout le run avant de composer quoi que ce soit.
    """
    regular = _find_font(fonts_dir, FONT_REGULAR_DEFAULT_NAMES)
    black = _find_font(fonts_dir, FONT_BLACK_DEFAULT_NAMES)
    missing = []
    if regular is None:
        missing.append(f"régulière (400) — un de : {', '.join(FONT_REGULAR_DEFAULT_NAMES)}")
    if black is None:
        missing.append(f"extra-bold (800) — un de : {', '.join(FONT_BLACK_DEFAULT_NAMES)}")
    if missing:
        raise MissingFontError(
            "Alte Haas Grotesk introuvable dans "
            f"{fonts_dir} :\n  - " + "\n  - ".join(missing) +
            "\nAucune police de repli ne sera utilisée. Dépose les fichiers "
            "manquants puis relance."
        )
    return regular, black


# ---------------------------------------------------------------------------
# Couleurs — uniquement celles rendues par obtenir_charte / obtenir_episode.
# ---------------------------------------------------------------------------

def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    h = hex_color.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


# ---------------------------------------------------------------------------
# a. FOND — recadrage 9:16 centré, cover, désaturation 15 %, sans assombrissement.
# ---------------------------------------------------------------------------

def cover_crop_resize(im: Image.Image, target_w: int, target_h: int) -> Image.Image:
    im = im.convert("RGB")
    src_w, src_h = im.size
    target_ratio = target_w / target_h
    src_ratio = src_w / src_h

    if src_ratio > target_ratio:
        # source plus large que la cible : on rogne les côtés
        new_w = round(src_h * target_ratio)
        x0 = (src_w - new_w) // 2
        box = (x0, 0, x0 + new_w, src_h)
    else:
        # source plus haute que la cible : on rogne haut/bas, centré
        new_h = round(src_w / target_ratio)
        y0 = (src_h - new_h) // 2
        box = (0, y0, src_w, y0 + new_h)

    cropped = im.crop(box)
    return cropped.resize((target_w, target_h), Image.LANCZOS)


def desaturate(im: Image.Image, amount: float) -> Image.Image:
    gray = im.convert("L").convert("RGB")
    return Image.blend(im, gray, amount)


# ---------------------------------------------------------------------------
# b. VOILE — dégradé vertical encre : transparent jusqu'à 45 % H, puis montée
#    progressive (ease-in quadratique) jusqu'à 88 % d'opacité en bas.
# ---------------------------------------------------------------------------

def _voile_alpha_column(h: int) -> list[int]:
    """Dégradé vertical : 0 jusqu'à 45 % H, puis montée en ease-in quadratique
    jusqu'à 88 % d'opacité en bas. Une seule colonne, valable pour toute
    largeur puisque le voile ne varie jamais horizontalement."""
    threshold_y = VOILE_TRANSPARENT_UNTIL * h
    span = h - threshold_y
    column = []
    for y in range(h):
        if y < threshold_y:
            alpha = 0.0
        else:
            t = (y - threshold_y) / span if span > 0 else 1.0
            alpha = (t * t) * VOILE_MAX_OPACITY  # ease-in quadratique, progressif
        column.append(round(alpha * 255))
    return column


def apply_voile(im: Image.Image, encre_rgb: tuple[int, int, int]) -> Image.Image:
    w, h = im.size
    r, g, b = encre_rgb
    column_alpha = _voile_alpha_column(h)
    base = im.convert("RGBA")

    if _np is not None:
        alpha = _np.array(column_alpha, dtype=_np.uint8).reshape(h, 1)
        alpha = _np.repeat(alpha, w, axis=1)
        rgba = _np.empty((h, w, 4), dtype=_np.uint8)
        rgba[..., 0] = r
        rgba[..., 1] = g
        rgba[..., 2] = b
        rgba[..., 3] = alpha
        voile = Image.fromarray(rgba, mode="RGBA")
    else:
        voile = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        px = voile.load()
        for y in range(h):
            a = column_alpha[y]
            if a == 0:
                continue
            for x in range(w):
                px[x, y] = (r, g, b, a)

    return Image.alpha_composite(base, voile)


# ---------------------------------------------------------------------------
# Texte avec interlettrage manuel (Pillow ne gère pas le tracking nativement).
# ---------------------------------------------------------------------------

def draw_tracked_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int, int],
    tracking_em: float,
) -> int:
    """Dessine `text` avec un interlettrage de `tracking_em` * taille de police,
    ancré en haut-gauche. Retourne la largeur totale dessinée."""
    x, y = xy
    tracking_px = tracking_em * font.size
    cursor = float(x)
    for ch in text:
        draw.text((cursor, y), ch, font=font, fill=fill, anchor="la")
        advance = draw.textlength(ch, font=font)
        cursor += advance + tracking_px
    return round(cursor - tracking_px - x)


def tracked_text_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, tracking_em: float) -> float:
    tracking_px = tracking_em * font.size
    width = sum(draw.textlength(ch, font=font) for ch in text)
    if text:
        width += tracking_px * (len(text) - 1)
    return width


# ---------------------------------------------------------------------------
# e. TITRE — wrap à 2 lignes max ; 112px sinon 96px, jamais 3 lignes.
# ---------------------------------------------------------------------------

def wrap_title(draw: ImageDraw.ImageDraw, text: str, font_path: Path, max_width: float) -> tuple[list[str], int]:
    for size in (TITLE_SIZE_PRIMARY, TITLE_SIZE_FALLBACK):
        font = ImageFont.truetype(str(font_path), size)
        lines = _greedy_wrap(draw, text, font, max_width)
        if len(lines) <= TITLE_MAX_LINES:
            return lines, size
    # Dernier recours : on force 2 lignes à la taille de repli, quitte à
    # déborder légèrement en largeur (mieux qu'une 3e ligne, cf. consigne).
    font = ImageFont.truetype(str(font_path), TITLE_SIZE_FALLBACK)
    forced = _force_two_lines(draw, text, font)
    print(
        f"  ! titre trop long même à {TITLE_SIZE_FALLBACK}px, forcé sur 2 lignes "
        "(peut déborder légèrement)",
        file=sys.stderr,
    )
    return forced, TITLE_SIZE_FALLBACK


def _greedy_wrap(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_width: float) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current: list[str] = []
    for word in words:
        trial = " ".join(current + [word])
        if draw.textlength(trial, font=font) <= max_width or not current:
            current.append(word)
        else:
            lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return lines


def _force_two_lines(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> list[str]:
    words = text.split()
    if len(words) <= 1:
        return [text]
    best_split, best_diff = 1, float("inf")
    for i in range(1, len(words)):
        w1 = draw.textlength(" ".join(words[:i]), font=font)
        w2 = draw.textlength(" ".join(words[i:]), font=font)
        diff = abs(w1 - w2)
        if diff < best_diff:
            best_diff, best_split = diff, i
    return [" ".join(words[:best_split]), " ".join(words[best_split:])]


# ---------------------------------------------------------------------------
# Composition complète d'un épisode.
# ---------------------------------------------------------------------------

@dataclass
class ComposeResult:
    image: Image.Image
    text_bottom_y: int  # plus bas pixel de texte dessiné (hors logo)


def compose_vignette(
    episode: dict,
    encre_rgb: tuple[int, int, int],
    source_image_path: Path,
    font_regular_path: Path,
    font_black_path: Path,
    logo_path: Path,
) -> ComposeResult:
    if not source_image_path.is_file():
        raise VignetteError(f"image source introuvable : {source_image_path}")

    serie_couleur = episode.get("serie_couleur")
    if not serie_couleur:
        raise VignetteError("serie_couleur manquante (doit venir de obtenir_episode)")
    serie_rgb = hex_to_rgb(serie_couleur)

    titre = episode.get("titre") or ""
    serie_nom = (episode.get("serie_nom") or "").upper()
    saison_numero = episode.get("saison_numero")
    numero = episode.get("numero")
    if not titre or saison_numero is None or numero is None or not episode.get("serie_nom"):
        raise VignetteError("champs manquants (titre / serie_nom / saison_numero / numero)")

    # a. FOND
    with Image.open(source_image_path) as src:
        bg = cover_crop_resize(src, CANVAS_W, CANVAS_H)
    bg = desaturate(bg, DESATURATION)

    # b. VOILE
    canvas = apply_voile(bg, encre_rgb)
    draw = ImageDraw.Draw(canvas)

    # e. TITRE — wrap d'abord (nécessaire pour positionner bandeau + filet)
    max_text_width = CANVAS_W - 2 * MARGIN
    title_font_path = font_black_path
    lines, title_size = wrap_title(draw, titre, title_font_path, max_text_width)
    title_font = ImageFont.truetype(str(title_font_path), title_size)
    line_height = round(title_size * TITLE_LINE_HEIGHT)

    baseline_y = round(TITLE_BASELINE_FRAC * CANVAS_H)
    # ascenders du haut de la 1re ligne (approximé par la taille de police, via
    # la bbox réelle du texte pour rester exact quelle que soit la police).
    ascent, descent = title_font.getmetrics()
    n_lines = len(lines)
    first_line_top = baseline_y - (n_lines - 1) * line_height - ascent

    # d. BANDEAU — 20px au-dessus du haut du titre
    bandeau_font = ImageFont.truetype(str(font_regular_path), BANDEAU_SIZE)
    bandeau_ascent, bandeau_descent = bandeau_font.getmetrics()
    bandeau_baseline_y = first_line_top - BANDEAU_GAP_ABOVE_TITLE
    bandeau_top_y = bandeau_baseline_y - bandeau_ascent
    label = f"{serie_nom} · SAISON {saison_numero} · ÉPISODE {numero}"
    draw_tracked_text(
        draw,
        (MARGIN, bandeau_top_y),
        label,
        bandeau_font,
        (*serie_rgb, 255),
        BANDEAU_TRACKING_EM,
    )

    # c. FILET — 5px, couleur série, du haut du bandeau à la base du titre
    draw.rectangle(
        [FILET_X, bandeau_top_y, FILET_X + FILET_WIDTH, baseline_y],
        fill=(*serie_rgb, 255),
    )

    # Titre, ligne par ligne, ancré haut-gauche (anchor "la") pour un calcul exact.
    text_bottom_y = baseline_y + descent
    for i, line in enumerate(lines):
        line_top = baseline_y - (n_lines - 1 - i) * line_height - ascent
        draw.text((MARGIN, line_top), line, font=title_font, fill=TITLE_COLOR, anchor="la")
        line_bottom = line_top + ascent + descent
        text_bottom_y = max(text_bottom_y, line_bottom)

    # f. LOGO — pictogramme blanc, 128px, coin bas droite, marge 128px.
    with Image.open(logo_path) as logo_src:
        logo = logo_src.convert("RGBA")
        lw, lh = logo.size
        new_h = LOGO_SIZE
        new_w = round(lw * (new_h / lh))
        logo = logo.resize((new_w, new_h), Image.LANCZOS)
    logo_x = CANVAS_W - MARGIN - new_w
    logo_y = CANVAS_H - MARGIN - new_h
    canvas.alpha_composite(logo, (logo_x, logo_y))

    return ComposeResult(image=canvas.convert("RGB"), text_bottom_y=round(text_bottom_y))


# ---------------------------------------------------------------------------
# Contrôles avant dépôt.
# ---------------------------------------------------------------------------

@dataclass
class QCReport:
    ok: bool
    width: int
    height: int
    luminosity_top_third: float
    text_bottom_y: int
    issues: list[str]


def run_qc(image: Image.Image, text_bottom_y: int) -> QCReport:
    issues = []
    w, h = image.size
    if (w, h) != (CANVAS_W, CANVAS_H):
        issues.append(f"dimensions {w}x{h} ≠ {CANVAS_W}x{CANVAS_H}")

    top_third = image.crop((0, 0, w, h // 3)).convert("L")
    hist = top_third.histogram()
    total = sum(hist)
    mean = sum(i * c for i, c in enumerate(hist)) / total if total else 0
    luminosity_pct = (mean / 255) * 100

    if luminosity_pct <= TOP_THIRD_MIN_LUMINOSITY:
        issues.append(
            f"luminosité tiers supérieur {luminosity_pct:.1f}% ≤ {TOP_THIRD_MIN_LUMINOSITY}%"
        )

    if text_bottom_y >= TEXT_SAFE_BELOW_Y:
        issues.append(f"texte descend à y={text_bottom_y} ≥ {TEXT_SAFE_BELOW_Y}")

    return QCReport(
        ok=not issues,
        width=w,
        height=h,
        luminosity_top_third=round(luminosity_pct, 1),
        text_bottom_y=text_bottom_y,
        issues=issues,
    )


def save_within_size_limit(image: Image.Image, out_path: Path) -> int:
    """Sauvegarde en PNG déterministe. Si > MAX_PNG_BYTES, recompresse en
    réduisant la palette (l'équivalent PNG d'une repasse « qualité 90 » — le
    PNG n'a pas de facteur de qualité JPEG, donc on réduit la palette de
    couleurs plutôt que d'introduire un flou)."""
    image.save(out_path, format="PNG", optimize=True, compress_level=9)
    size = out_path.stat().st_size
    if size <= MAX_PNG_BYTES:
        return size

    quantized = image.quantize(colors=256, method=Image.MEDIANCUT, dither=Image.FLOYDSTEINBERG)
    quantized.save(out_path, format="PNG", optimize=True, compress_level=9)
    return out_path.stat().st_size


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def default_paths(repo_root: Path) -> dict:
    return {
        "fonts_dir": repo_root / "assets" / "fonts",
        "logo": repo_root / "videos" / "planit-b-s1p1-l-atelier" / "assets" / "brand" / "planit-mark-white.png",
    }


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    defaults = default_paths(repo_root)

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--charte", required=True, type=Path, help="JSON = sortie de obtenir_charte")
    parser.add_argument("--manifest", required=True, type=Path, help="JSON = liste d'épisodes à composer")
    parser.add_argument("--fonts-dir", type=Path, default=defaults["fonts_dir"])
    parser.add_argument("--logo", type=Path, default=defaults["logo"])
    parser.add_argument("--out-dir", required=True, type=Path)
    args = parser.parse_args()

    try:
        font_regular_path, font_black_path = require_fonts(args.fonts_dir)
    except MissingFontError as exc:
        print(f"ARRÊT — {exc}", file=sys.stderr)
        return 1

    if not args.logo.is_file():
        print(f"ARRÊT — logo introuvable : {args.logo}", file=sys.stderr)
        return 1

    charte = json.loads(args.charte.read_text())
    encre_hex = charte.get("couleurs", {}).get("encre", {}).get("hex")
    if not encre_hex:
        print("ARRÊT — couleur « encre » absente de la charte", file=sys.stderr)
        return 1
    encre_rgb = hex_to_rgb(encre_hex)

    manifest = json.loads(args.manifest.read_text())
    args.out_dir.mkdir(parents=True, exist_ok=True)

    results = []
    for episode in manifest:
        ep_id = episode.get("id", "?")
        image_vignette_local = episode.get("image_vignette_local")
        if not image_vignette_local:
            results.append({"id": ep_id, "statut": "echec", "raison": "image_vignette absente"})
            continue
        try:
            composed = compose_vignette(
                episode,
                encre_rgb,
                Path(image_vignette_local),
                font_regular_path,
                font_black_path,
                args.logo,
            )
            qc = run_qc(composed.image, composed.text_bottom_y)
            out_path = args.out_dir / f"{ep_id}.png"
            if qc.ok:
                size_bytes = save_within_size_limit(composed.image, out_path)
                results.append(
                    {
                        "id": ep_id,
                        "titre": episode.get("titre"),
                        "statut": "ok",
                        "dimensions": f"{qc.width}x{qc.height}",
                        "luminosite_tiers_sup_pct": qc.luminosity_top_third,
                        "poids_octets": size_bytes,
                        "fichier": str(out_path),
                    }
                )
            else:
                results.append(
                    {
                        "id": ep_id,
                        "titre": episode.get("titre"),
                        "statut": "echec_qc",
                        "raisons": qc.issues,
                    }
                )
        except VignetteError as exc:
            results.append({"id": ep_id, "statut": "echec", "raison": str(exc)})

    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 0 if all(r["statut"] == "ok" for r in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
