#!/usr/bin/env python3
"""01 — Inventaire des assets + découpe des sous-plans du bloc D.

Ce script ne télécharge rien lui-même : Google Drive et RapidoCMS sont exposés
en MCP, donc côté agent. Il fait deux choses :

  1. INVENTAIRE — vérifie tout ce dont l'assemblage a besoin et écrit
     `build/assets_report.json`. Chaque manque est loggé avec un code
     (`MISSING_HOOK EP07`, `NEED_MCP_DRIVE kds`, …) que l'agent lit pour savoir
     quel appel MCP passer. Un hook absent EXCLUT l'épisode du lot — il n'est
     jamais remplacé par une génération.

  2. DÉCOUPE DU BLOC D — extrait 4 sous-plans (`site_web`, `caisse_pos`, `kds`,
     `marketing`) depuis les tutos bruts déposés dans `assets/demo/*_raw.mp4`.
     Le point d'entrée est choisi automatiquement (fenêtre la plus animée, sans
     coupe franche) et la zone d'action est détectée sur une grille 3×3 pour
     zoomer dessus plutôt que de recadrer au centre en aveugle.
     Les choix retenus sont écrits dans `config/demo_cuts.json` : au run
     suivant ils sont relus tels quels, donc le montage est reproductible.

Usage :
    python scripts/01_fetch_assets.py                   # inventaire + découpe
    python scripts/01_fetch_assets.py --format linkedin_45
    python scripts/01_fetch_assets.py --redetect        # ignore demo_cuts.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ff  # noqa: E402

ROOT = ff.ROOT
DEMO_ORDER = ["site_web", "caisse_pos", "kds", "marketing"]
CUTS_PATH = ROOT / "config" / "demo_cuts.json"

# Une coupe franche (changement de plan) a un score de scène élevé ; on refuse
# toute fenêtre qui en contient une, sinon le sous-plan est illisible.
HARD_CUT = 0.35
BAND_BG = "0xFCF9E6"       # crème de la charte, fond des bandes de démo


# ---------------------------------------------------------------------------
# Choix automatique du point d'entrée
# ---------------------------------------------------------------------------

def scene_scores(src: Path, rate: int = 5) -> list[tuple[float, float]]:
    """(temps, score de changement) échantillonné à `rate` images/s."""
    code, out = ff.ffmpeg([
        "-i", str(src), "-vf",
        f"fps={rate},select='gte(scene\\,0)',metadata=print:file=-",
        "-an", "-f", "null", "-",
    ])
    scores = [float(m) for m in
              re.findall(r"lavfi\.scene_score=([0-9.]+)", out)]
    return [(i / rate, s) for i, s in enumerate(scores)]


def pick_window(src: Path, want: float) -> float:
    """Instant de départ du segment le plus lisible de `want` secondes."""
    total = ff.duration(src)
    if total <= want + 2.0:
        return max(0.0, (total - want) / 2)

    samples = scene_scores(src)
    if not samples:
        return max(0.0, (total - want) / 2)

    # Les tutos commencent par un carton titre et finissent par une page de fin :
    # on ne cherche que dans le corps du tuto, là où l'action se passe.
    lo = max(1.5, total * 0.10)
    hi = min(total - want - 1.0, total * 0.85)
    if hi <= lo:
        lo, hi = 1.5, max(1.5, total - want - 1.0)
    best_t, best_score = lo, -1.0
    step = 0.5
    t = lo
    while t <= hi:
        win = [s for ts, s in samples if t <= ts < t + want]
        t += step
        if not win or max(win) > HARD_CUT:
            continue                      # coupe franche dans la fenêtre
        mean = sum(win) / len(win)
        if mean > best_score:
            best_score, best_t = mean, t - step
    return round(best_t if best_score >= 0 else lo, 2)


def find_focus(src: Path, start: float, want: float) -> tuple[float, float]:
    """Centre de la zone d'action, en fractions de largeur/hauteur.

    On découpe l'image en 3×3, on mesure l'énergie de différence temporelle de
    chaque case sur la fenêtre retenue, et on garde la case qui bouge le plus :
    c'est là que se trouve le bouton cliqué ou la carte qui se génère.
    """
    vs = ff.video_stream(src)
    w, h = int(vs["width"]), int(vs["height"])
    cw, ch = w // 3, h // 3

    best, best_e = (0.5, 0.5), -1.0
    for row in range(3):
        for col in range(3):
            cx, cy = col * cw, row * ch
            code, out = ff.ffmpeg([
                "-ss", f"{start:.2f}", "-t", f"{want:.2f}", "-i", str(src),
                "-vf", f"crop={cw}:{ch}:{cx}:{cy},fps=10,"
                       f"tblend=all_mode=difference,signalstats,"
                       f"metadata=print:file=-",
                "-an", "-f", "null", "-",
            ])
            vals = [float(m) for m in
                    re.findall(r"lavfi\.signalstats\.YAVG=([0-9.]+)", out)]
            energy = sum(vals) / len(vals) if vals else 0.0
            if energy > best_e:
                best_e = energy
                best = ((cx + cw / 2) / w, (cy + ch / 2) / h)
    return round(best[0], 3), round(best[1], 3)


def cut_demo(src: Path, dst: Path, cut: dict, *, width: int, height: int,
             fps: int, seconds: float) -> None:
    """Extrait le sous-plan en PLEIN CADRE, sans jamais couper la capture.

    Les tutos sont des captures très larges (1920×828, soit 2,3:1). Les recadrer
    en 9:16 n'en garderait que ~24 % de la largeur : on perdrait le bouton
    cliqué comme son résultat.

    La capture est donc affichée **entière**, à la largeur du cadre, par-dessus
    un fond qui remplit tout l'écran : la même image agrandie pour couvrir et
    floutée. Rien n'est coupé, et il ne reste aucune zone vide.

    `zoom` > 1 est possible mais rogne la capture — laisser à 1,0 par défaut.
    """
    fx, fy = cut["focus_x"], cut["focus_y"]
    zoom = float(cut.get("zoom", 1.0))
    sw = round(width * zoom)
    if sw % 2:
        sw += 1

    fg = f"[fg]scale={sw}:-2:flags=lanczos"
    if zoom > 1.0:
        # rognage optionnel, recentré sur la zone d'action détectée
        fg += (f",crop='min(iw\\,{width})':'min(ih\\,{height})':"
               f"'clip(iw*{fx}-{width}/2\\,0\\,max(0\\,iw-{width}))':"
               f"'clip(ih*{fy}-{height}/2\\,0\\,max(0\\,ih-{height}))'")
    fg += "[fgs]"

    vf = (
        "[0:v]split=2[bgsrc][fg];"
        # fond : la capture agrandie pour couvrir le cadre, floutée et assombrie
        f"[bgsrc]scale={width}:{height}:force_original_aspect_ratio=increase,"
        f"crop={width}:{height},gblur=sigma=42,eq=brightness=-0.07[bgb];"
        f"{fg};"
        # capture entière, centrée, par-dessus le fond
        f"[bgb][fgs]overlay=(W-w)/2:(H-h)/2:format=auto,"
        f"fps={fps},format=yuv420p[out]"
    )
    dst.parent.mkdir(parents=True, exist_ok=True)
    ff.ffmpeg([
        "-ss", f"{cut['start']:.3f}", "-i", str(src),
        *ff.exact_cut(seconds, fps),
        "-filter_complex", vf, "-map", "[out]", "-an",
        *ff.VCODEC, *ff.TIMESCALE, str(dst),
    ])


# ---------------------------------------------------------------------------
# Inventaire
# ---------------------------------------------------------------------------

def check_logo(path: Path, report: dict) -> None:
    if not path.exists():
        report["missing"].append(f"NEED_MCP_RAPIDOCMS logo → {path}")
        return
    vs = ff.video_stream(path)
    pix = (vs or {}).get("pix_fmt", "")
    if "a" not in pix:
        report["warnings"].append(
            f"LOGO_OPAQUE {path.name} (pix_fmt={pix}) — applique un colorkey "
            f"ffmpeg avant incrustation, ne le regénère pas"
        )
    report["ok"].append(f"logo {path.name} ({vs['width']}×{vs['height']}, {pix})")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--format", default="tiktok_30")
    ap.add_argument("--redetect", action="store_true",
                    help="recalcule les points d'entrée même s'ils sont figés")
    args = ap.parse_args()

    cfg = ff.load_config()
    fmt = cfg["formats"][args.format]
    W, H, FPS = fmt["width"], fmt["height"], fmt["fps"]

    # Le bloc D contient 4 sous-plans de durée égale.
    d_block = next(b for b in fmt["blocks"] if b["id"] == "D")
    subs = ff.split_seconds(d_block["end"] - d_block["start"], FPS,
                            len(DEMO_ORDER))
    sub_s = subs[0]

    report: dict = {"format": args.format, "sub_shot_s": subs,
                    "ok": [], "missing": [], "warnings": [],
                    "episodes_ready": [], "episodes_excluded": []}

    # --- assets de marque -------------------------------------------------
    check_logo(ROOT / cfg["brand"]["logo_path"], report)
    for rel in ("assets/brand/sting-logo.mp4", "assets/brand/probleme.mp4",
                "assets/brand/outro.mp4", "assets/music/bed.mp3",
                "assets/fonts/Anton-Regular.ttf"):
        p = ROOT / rel
        if p.exists():
            report["ok"].append(rel)
        else:
            hint = ("lance scripts/00_build_brand_clips.py"
                    if rel.endswith(".mp4") else "dépose le fichier")
            report["missing"].append(f"MISSING_ASSET {rel} — {hint}")

    # --- sous-plans du bloc D --------------------------------------------
    cuts = json.loads(CUTS_PATH.read_text(encoding="utf-8")) \
        if CUTS_PATH.exists() else {}
    changed = False

    for idx, name in enumerate(DEMO_ORDER):
        want = subs[idx]
        raw = ROOT / "assets" / "demo" / f"{name}_raw.mp4"
        if not raw.exists():
            fid = cfg["drive"]["demo_clips"].get(name, {})
            report["missing"].append(
                f"NEED_MCP_DRIVE {name} — search_files(parentId="
                f"{fid.get('folder_id')}) puis download_file_content "
                f"→ assets/demo/{name}_raw.mp4"
            )
            continue

        cut = cuts.get(name)
        if cut is None or args.redetect:
            ff.log(f"DETECT {name} — recherche du meilleur segment …")
            start = pick_window(raw, want)
            fx, fy = find_focus(raw, start, want)
            cut = {"src": f"assets/demo/{name}_raw.mp4", "start": start,
                   "focus_x": fx, "focus_y": fy, "zoom": 1.35,
                   "detected": True}
            cuts[name] = cut
            changed = True
            ff.log(f"       start={start}s focus=({fx}, {fy})")

        dst = ROOT / "build" / f"demo_{name}_{args.format}.mp4"
        cut_demo(raw, dst, cut, width=W, height=H, fps=FPS, seconds=want)
        got = ff.duration(dst)
        report["ok"].append(
            f"demo {name}: {dst.name} {got:.3f}s / {ff.frames(dst)} images "
            f"@ start={cut['start']}s"
        )

    if changed:
        CUTS_PATH.write_text(
            json.dumps(cuts, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8")
        report["ok"].append(f"points d'entrée figés dans {CUTS_PATH.name}")

    # --- hooks ------------------------------------------------------------
    hook_s = next(b for b in fmt["blocks"] if b["id"] == "A")
    hook_len = hook_s["end"] - hook_s["start"]
    for ep in cfg["episodes"]:
        p = ROOT / "assets" / "hooks" / f"{ep['id']}.mp4"
        if not p.exists():
            ff.log(f"MISSING_HOOK {ep['id']}", err=True)
            report["episodes_excluded"].append(ep["id"])
            continue
        d = ff.duration(p)
        if d < hook_len - 0.05:
            report["warnings"].append(
                f"HOOK_TOO_SHORT {ep['id']} — {d:.2f}s < {hook_len:.2f}s "
                f"requis pour {args.format}"
            )
            report["episodes_excluded"].append(ep["id"])
        else:
            report["episodes_ready"].append(ep["id"])

    if report["episodes_excluded"]:
        report["missing"].append(
            f"MISSING_HOOK ×{len(report['episodes_excluded'])} — clips à "
            f"générer par l'humain dans l'UI Higgsfield puis à déposer dans "
            f"assets/hooks/ (aucune génération automatique)"
        )

    out = ROOT / "build" / "assets_report.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")

    ff.log("")
    for line in report["ok"]:
        ff.log(f"  OK      {line}")
    for line in report["warnings"]:
        ff.log(f"  WARN    {line}")
    for line in report["missing"]:
        ff.log(f"  MANQUE  {line}")
    ff.log(f"\n  épisodes prêts : {len(report['episodes_ready'])}/30 "
           f"→ {out.relative_to(ROOT)}")
    return 1 if report["missing"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
