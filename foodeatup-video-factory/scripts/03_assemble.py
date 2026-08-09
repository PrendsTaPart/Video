#!/usr/bin/env python3
"""03 — Assemblage ffmpeg + contrôle qualité bloquant.

Chaîne complète, 100 % locale :

    segments normalisés → concat → logo permanent → piste VO → mixage
    → loudnorm 2 passes → QA (6 tests) → out/EPxx_<format>.mp4

Rien n'est publié si un test QA échoue : le script sort en erreur et laisse le
master dans `out/` marqué comme rejeté dans le journal de run.

Points d'implémentation qui méritent une note :

* **Durées exactes.** Chaque bloc est coupé à la durée de `episodes.json` après
  `fps=30`, donc sur un nombre entier d'images. 7,0 + 2,0 + 7,5 + 9,5 + 4,0 =
  30,000 s pile, et le démuxeur `concat` (copie sans réencodage) ne dérive pas.

* **Bloc B.** Le sting affiche déjà le logo en grand ; on ne superpose pas une
  seconde instance centrée par-dessus, on passe le filigrane du coin à 100 %
  d'opacité pendant B. Le logo reste visible sur 100 % de la durée.

* **Ducking.** `sidechaincompress` baisse la musique ET le son diégétique dès
  que la voix parle. Sans ça la VO est mangée sur un haut-parleur de téléphone.
  La musique est calée à −22 LUFS avant mixage, le master à −14 LUFS.

* **loudnorm en deux passes.** Le simple passage `loudnorm=I=-14` est un
  compresseur approximatif qui rate la cible de plusieurs LU ; on mesure puis
  on applique en linéaire, ce qui tient le ±1 LUFS exigé par la QA.

Usage :
    python scripts/03_assemble.py --episode EP01 --format tiktok_30
    python scripts/03_assemble.py --episode EP01 --skip-vo   # test de chaîne
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ff  # noqa: E402

ROOT = ff.ROOT
BUILD = ROOT / "build"
OUT = ROOT / "out"
FONTS = ROOT / "assets" / "fonts"

DEMO_ORDER = ["site_web", "caisse_pos", "kds", "marketing"]
WHITE_FADE = 0.25          # fondu au blanc entre D et E
MUSIC_LUFS = -22.0         # charte : musique à −22 LUFS
MASTER_LUFS = -14.0
# On vise −1,5 dBTP au mixage pour livrer sous la limite de charte (−1,0) : le
# limiteur de loudnorm dépasse légèrement sa consigne, viser pile −1,0 sortait
# à −0,85 et violait la charte.
MASTER_TP_TARGET = -1.5
MASTER_TP_LIMIT = -1.0

QA_TOLERANCE_S = 0.15
QA_LUFS_TOL = 1.0
QA_MIN_LUMA = 12.0
QA_MIN_RMS = -50.0
QA_LOGO_DELTA = 3.0        # écart moyen mini dans la zone du logo


# ---------------------------------------------------------------------------
# Sous-titres du hook (ASS — meilleur contour que drawtext, et éditable)
# ---------------------------------------------------------------------------

def wrap_hook(text: str) -> tuple[str, int]:
    """3 mots par ligne, 2 lignes max ; au-delà de 6 mots on réduit la taille.

    On ne rajoute jamais une 3e ligne : elle sortirait des safe zones.
    """
    words = text.split()
    size = 96 if len(words) <= 6 else 82
    half = (len(words) + 1) // 2
    half = min(max(half, 1), 3)
    lines = [" ".join(words[:half]), " ".join(words[half:])]
    # On échappe CHAQUE ligne avant de poser le `\N` : échapper après
    # transformerait le saut de ligne ASS en backslash littéral à l'écran.
    return "\\N".join(ff.ass_escape(l) for l in lines if l), size


def write_ass(path: Path, text: str, *, res_x: int, res_y: int, margin_v: int,
              t_in: float, t_out: float) -> Path:
    body, size = wrap_hook(text)

    def ts(v: float) -> str:
        h, rem = divmod(v, 3600)
        m, s = divmod(rem, 60)
        return f"{int(h)}:{int(m):02d}:{s:05.2f}"

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "[Script Info]\n"
        "ScriptType: v4.00+\n"
        f"PlayResX: {res_x}\nPlayResY: {res_y}\n"
        "WrapStyle: 2\nScaledBorderAndShadow: yes\n\n"
        "[V4+ Styles]\n"
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, "
        "OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, "
        "ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, "
        "Alignment, MarginL, MarginR, MarginV, Encoding\n"
        # Alignment 2 = bas-centre : combiné à MarginV c'est ce qui place le
        # texte « à N px du bas » comme demandé par la charte.
        f"Style: Hook,Anton,{size},&H00FFFFFF,&H00000000,&H00000000,"
        f"&H80000000,-1,0,0,0,100,100,0,0,1,6,3,2,80,80,{margin_v},1\n\n"
        "[Events]\n"
        "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, "
        "Effect, Text\n"
        f"Dialogue: 0,{ts(t_in)},{ts(t_out)},Hook,,0,0,0,,"
        f"{{\\fad(200,200)}}{body}\n",
        encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# Blocs
# ---------------------------------------------------------------------------

def block_seconds(block: dict) -> float:
    return round(block["end"] - block["start"], 4)


def build_hook(ep: dict, block: dict, fmt: dict, tag: str) -> Path:
    src = ROOT / "assets" / "hooks" / f"{ep['id']}.mp4"
    if not src.exists():
        raise SystemExit(f"MISSING_HOOK {ep['id']} — {src} absent. "
                         f"Clip à générer par l'humain dans l'UI Higgsfield ; "
                         f"aucune génération automatique.")
    want = block_seconds(block)
    total = ff.duration(src)
    if "cut_out" in ep and ep["cut_out"] is not None:
        ss = max(0.0, float(ep["cut_out"]) - want)
    else:
        ss = float(ep.get("cut_in", 0.0))
    if ss + want > total + 1e-3:
        raise SystemExit(f"HOOK_TOO_SHORT {ep['id']} — {total:.2f}s "
                         f"disponibles, {ss + want:.2f}s demandées")

    raw = ff.normalize(src, BUILD / f"norm_A_{tag}.mp4",
                       width=fmt["width"], height=fmt["height"],
                       fps=fmt["fps"], seconds=want, ss=ss)

    ass = write_ass(BUILD / f"hook_{tag}.ass", ep["hook"],
                    res_x=fmt["width"], res_y=fmt["height"],
                    margin_v=fmt.get("hook_margin_v",
                                     700 if fmt["height"] > fmt["width"]
                                     else 180),
                    t_in=fmt["hook_text_in_s"], t_out=fmt["hook_text_out_s"])

    dst = BUILD / f"blockA_{tag}.mp4"
    ff.ffmpeg([
        "-i", str(raw), "-vf",
        f"ass='{ff.filter_escape(ass)}':fontsdir='{ff.filter_escape(FONTS)}'",
        "-c:a", "copy", *ff.VCODEC, *ff.TIMESCALE,
        "-frames:v", str(round(want * fmt["fps"])), str(dst),
    ])
    return dst


def build_simple(src_rel: str, block: dict, fmt: dict, tag: str, name: str,
                 *, fade_in_white=False, fade_out_white=False) -> Path:
    src = ROOT / src_rel
    if not src.exists():
        raise SystemExit(f"MISSING_ASSET {src_rel} — lance "
                         f"scripts/00_build_brand_clips.py")
    want = block_seconds(block)
    extra = []
    if fade_in_white:
        extra.append(f"fade=t=in:st=0:d={WHITE_FADE}:color=white")
    if fade_out_white:
        extra.append(f"fade=t=out:st={want - WHITE_FADE:.3f}:"
                     f"d={WHITE_FADE}:color=white")
    dst = BUILD / f"block{name}_{tag}.mp4"
    return ff.freeze_pad(
        ff.normalize(src, BUILD / f"norm_{name}_{tag}.mp4",
                     width=fmt["width"], height=fmt["height"], fps=fmt["fps"],
                     seconds=want, extra_vf=",".join(extra)),
        dst, seconds=want, width=fmt["width"], height=fmt["height"],
        fps=fmt["fps"])


def build_demo(block: dict, fmt: dict, tag: str, fmt_name: str) -> Path:
    """4 sous-plans égaux + fondu au blanc sur la fin du bloc."""
    want = block_seconds(block)
    # Mêmes durées frame-exactes que celles produites par 01_fetch_assets.py.
    subs = ff.split_seconds(want, fmt["fps"], len(DEMO_ORDER))
    parts = []
    for name, sub in zip(DEMO_ORDER, subs):
        p = BUILD / f"demo_{name}_{fmt_name}.mp4"
        if not p.exists():
            raise SystemExit(
                f"MISSING_DEMO {p.name} — lance scripts/01_fetch_assets.py "
                f"--format {fmt_name} (les tutos bruts viennent du Drive)")
        parts.append(ff.normalize(p, BUILD / f"norm_D_{name}_{tag}.mp4",
                                  width=fmt["width"], height=fmt["height"],
                                  fps=fmt["fps"], seconds=sub))
    joined = ff.concat(parts, BUILD / f"demo_join_{tag}.mp4", BUILD)
    dst = BUILD / f"blockD_{tag}.mp4"
    ff.ffmpeg([
        "-i", str(joined), "-vf",
        f"fade=t=out:st={want - WHITE_FADE:.3f}:d={WHITE_FADE}:color=white",
        "-c:a", "copy", *ff.VCODEC, *ff.TIMESCALE,
        "-frames:v", str(round(want * fmt["fps"])), str(dst),
    ])
    return dst


# ---------------------------------------------------------------------------
# Logo permanent
# ---------------------------------------------------------------------------

def overlay_logo(src: Path, dst: Path, cfg: dict, fmt: dict) -> Path:
    brand = cfg["brand"]
    logo = ROOT / brand["logo_path"]
    h = brand["logo_height_px"]
    m = brand["logo_margin_px"]
    op = brand["logo_opacity"]
    b = next(x for x in fmt["blocks"] if x["id"] == "B")

    fc = (
        f"[1:v]scale=-1:{h}:flags=lanczos,format=rgba,"
        f"colorchannelmixer=aa={op}[lg];"
        f"[2:v]scale=-1:{h}:flags=lanczos,format=rgba[lgb];"
        # filigrane courant, désactivé pendant le sting…
        f"[0:v][lg]overlay=W-w-{m}:{m + 20}:format=auto:"
        f"enable='not(between(t\\,{b['start']}\\,{b['end']}))'[v1];"
        # …remplacé pendant B par la même incrustation à 100 % d'opacité.
        f"[v1][lgb]overlay=W-w-{m}:{m + 20}:format=auto:"
        f"enable='between(t\\,{b['start']}\\,{b['end']})'[v]"
    )
    # Le master est épinglé ici au nombre d'images exact : c'est le dernier
    # ré-encodage vidéo de la chaîne (le mixage final copie la vidéo).
    ff.ffmpeg([
        "-i", str(src), "-i", str(logo), "-i", str(logo),
        "-filter_complex", fc, "-map", "[v]", "-map", "0:a",
        *ff.VCODEC, *ff.ACODEC, *ff.TIMESCALE,
        *ff.exact_cut(fmt["total_s"], fmt["fps"]), str(dst),
    ])
    return dst


# ---------------------------------------------------------------------------
# Audio
# ---------------------------------------------------------------------------

VO_GAP = 0.12          # silence minimal entre deux prises de parole


def build_vo_track(ep: dict, fmt: dict, tag: str, total: float) -> Path | None:
    """Pose chaque VO à sa place sur une piste unique de `total` secondes.

    Deux VO ne doivent JAMAIS parler en même temps : la punchline de l'épisode
    (posée sur le beat comique du hook) débordait sur la VO « FoodEatUp » du
    sting, et sur le format 45 s la VO de démo chevauchait celle du closing.
    """
    segs: list[dict] = []
    for bid, rel in fmt["vo"].items():
        p = ROOT / rel
        blk = next(x for x in fmt["blocks"] if x["id"] == bid)
        if not p.exists():
            ff.log(f"  WARN MISSING_VO {rel}", err=True)
            continue
        d = ff.duration(p)
        at = blk["start"]
        over = (at + d) - blk["end"]
        if over > 0.01:
            # VO plus longue que son bloc : on l'avance pour qu'elle finisse
            # avec le bloc, plutôt que de la laisser tronquer en plein mot par
            # le `-t` final.
            at = max(0.0, at - over)
            ff.log(f"  INFO VO_AVANCEE {bid} : {d:.2f}s pour un bloc de "
                   f"{blk['end'] - blk['start']:.2f}s → départ à {at:.2f}s")
        segs.append({"path": p, "at": at, "dur": d, "nom": bid})

    punch = ROOT / "vo" / "punch" / f"{ep['id']}.mp3"
    if punch.exists():
        segs.append({"path": punch, "at": float(fmt["punch_at_s"]),
                     "dur": ff.duration(punch), "nom": "punchline"})
    else:
        ff.log(f"  WARN MISSING_VO vo/punch/{ep['id']}.mp3", err=True)

    if not segs:
        return None

    # Passe arrière : on remonte depuis la fin et on recule ce qui déborde sur
    # le suivant. On recule le PRÉCÉDENT plutôt que de repousser le suivant —
    # repousser ferait sortir la dernière VO du montage.
    segs.sort(key=lambda s: s["at"])
    for i in range(len(segs) - 1, 0, -1):
        prev, cur = segs[i - 1], segs[i]
        fin_max = cur["at"] - VO_GAP
        if prev["at"] + prev["dur"] > fin_max:
            nouveau = max(0.0, fin_max - prev["dur"])
            ff.log(f"  INFO VO_ANTI_CHEVAUCHEMENT {prev['nom']} recalée "
                   f"{prev['at']:.2f}s → {nouveau:.2f}s "
                   f"(parlait par-dessus {cur['nom']})")
            prev["at"] = nouveau

    placed = [(s["path"], s["at"]) for s in segs]

    args: list[str] = []
    chains: list[str] = []
    for i, (p, at) in enumerate(placed):
        args += ["-i", str(p)]
        chains.append(f"[{i}:a]aresample=48000,"
                      f"adelay=delays={int(at * 1000)}ms:all=1[a{i}]")
    mix = "".join(f"[a{i}]" for i in range(len(placed)))
    chains.append(f"{mix}amix=inputs={len(placed)}:duration=longest:"
                  f"dropout_transition=0:normalize=0,"
                  f"apad,atrim=0:{total},asetpts=N/SR/TB[vo]")
    dst = BUILD / f"votrack_{tag}.wav"
    ff.ffmpeg([*args, "-filter_complex", ";".join(chains), "-map", "[vo]",
               "-ar", "48000", "-ac", "2", str(dst)])
    return dst


def music_bed(total: float) -> Path:
    """Lit musical bouclé, calé à −22 LUFS (mis en cache par durée)."""
    src = ROOT / "assets" / "music" / "bed.mp3"
    dst = BUILD / f"bed_{total:g}s.wav"
    if dst.exists():
        return dst
    loop = BUILD / f"bed_loop_{total:g}s.wav"
    ff.ffmpeg(["-stream_loop", "-1", "-i", str(src), "-t", f"{total:.4f}",
               "-ar", "48000", "-ac", "2", str(loop)])
    m = ff.measure_loudness(loop, target_i=MUSIC_LUFS, target_tp=-2.0,
                            target_lra=11.0)
    ff.ffmpeg(["-i", str(loop), "-af",
               ff.loudnorm_filter(m, target_i=MUSIC_LUFS, target_tp=-2.0,
                                  target_lra=11.0),
               "-ar", "48000", "-ac", "2", str(dst)])
    return dst


def mix_audio(video: Path, vo: Path | None, bed: Path, dst: Path,
              total: float) -> Path:
    """Diégétique + VO + lit musical, avec ducking, puis loudnorm 2 passes."""
    if vo is not None:
        fc = (
            "[1:a]asplit=3[vo_mix][key1][key2];"
            "[2:a]afade=t=in:d=0.5,"
            f"afade=t=out:st={total - 0.8:.3f}:d=0.8[bed0];"
            "[bed0][key1]sidechaincompress=threshold=0.05:ratio=8:"
            "attack=20:release=300[bed];"
            "[0:a]volume=0.9[diag0];"
            "[diag0][key2]sidechaincompress=threshold=0.05:ratio=6:"
            "attack=20:release=300[diag];"
            "[diag][bed][vo_mix]amix=inputs=3:duration=first:"
            "dropout_transition=0:normalize=0[mixed]"
        )
        inputs = ["-i", str(video), "-i", str(vo), "-i", str(bed)]
    else:
        fc = (
            "[1:a]afade=t=in:d=0.5,"
            f"afade=t=out:st={total - 0.8:.3f}:d=0.8[bed];"
            "[0:a]volume=0.9[diag];"
            "[diag][bed]amix=inputs=2:duration=first:"
            "dropout_transition=0:normalize=0[mixed]"
        )
        inputs = ["-i", str(video), "-i", str(bed)]

    raw = BUILD / f"{dst.stem}_premix.wav"
    ff.ffmpeg([*inputs, "-filter_complex", fc, "-map", "[mixed]",
               "-ar", "48000", "-ac", "2", str(raw)])

    m = ff.measure_loudness(raw, target_i=MASTER_LUFS,
                            target_tp=MASTER_TP_TARGET)
    dst.parent.mkdir(parents=True, exist_ok=True)
    ff.ffmpeg(["-i", str(video), "-i", str(raw),
               "-af", ff.loudnorm_filter(m, target_i=MASTER_LUFS,
                                         target_tp=MASTER_TP_TARGET),
               "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy",
               *ff.ACODEC, "-t", f"{total:.4f}", str(dst)])
    return dst


# ---------------------------------------------------------------------------
# Contrôle qualité
# ---------------------------------------------------------------------------

def run_qa(final: Path, before_logo: Path, cfg: dict, fmt: dict) -> list[dict]:
    total = fmt["total_s"]
    tests: list[dict] = []

    def add(name, ok, got, expected):
        tests.append({"test": name, "ok": bool(ok), "mesure": got,
                      "attendu": expected})

    d = ff.duration(final)
    add("duree", abs(d - total) <= QA_TOLERANCE_S, round(d, 3),
        f"{total} ±{QA_TOLERANCE_S}s")

    vs = ff.video_stream(final)
    res_ok = vs["width"] == fmt["width"] and vs["height"] == fmt["height"]
    add("resolution", res_ok, f"{vs['width']}×{vs['height']}",
        f"{fmt['width']}×{fmt['height']}")

    lr = ff.loudness_report(final)
    add("loudness_I", abs(lr["input_i"] - MASTER_LUFS) <= QA_LUFS_TOL,
        lr["input_i"], f"{MASTER_LUFS} ±{QA_LUFS_TOL} LUFS")
    add("true_peak", lr["input_tp"] <= MASTER_TP_LIMIT, lr["input_tp"],
        f"≤ {MASTER_TP_LIMIT} dBTP")

    # Logo : on compare le master AVANT et APRÈS incrustation. Dans la zone du
    # logo l'écart doit être franc à chacun des 3 instants testés.
    brand = cfg["brand"]
    lh = brand["logo_height_px"]
    m = brand["logo_margin_px"]
    lw = min(fmt["width"] - 2 * m, int(lh * 3.2))
    crop = f"{lw}:{lh + 8}:{fmt['width'] - lw - m}:{m + 16}"
    hits, deltas = 0, []
    for t in (1.0, round(total / 2, 2), round(total - 1.0, 2)):
        delta = ff.region_delta(before_logo, final, t, crop)
        deltas.append(round(delta, 2))
        if delta >= QA_LOGO_DELTA:
            hits += 1
    add("logo_present", hits == 3, f"{hits}/3 (écarts {deltas})", "3/3")

    luma = ff.frame_luma(final, max(0.0, total - 0.1))
    add("pas_de_frame_noire", luma > QA_MIN_LUMA, round(luma, 2),
        f"> {QA_MIN_LUMA}")

    rms = ff.audio_rms(final)
    add("audio_non_muet", rms > QA_MIN_RMS,
        rms if rms != float("-inf") else "-inf", f"> {QA_MIN_RMS} dB")

    return tests


# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--episode", required=True)
    ap.add_argument("--format", default="tiktok_30")
    ap.add_argument("--skip-vo", action="store_true",
                    help="assemble sans voix off (test de chaîne uniquement — "
                         "le master est marqué non publiable)")
    args = ap.parse_args()

    cfg = ff.load_config()
    ep = ff.episode(cfg, args.episode)
    fmt = cfg["formats"][args.format]
    tag = f"{ep['id']}_{args.format}"
    total = fmt["total_s"]
    BUILD.mkdir(parents=True, exist_ok=True)

    blocks = {b["id"]: b for b in fmt["blocks"]}
    declared = sum(block_seconds(b) for b in fmt["blocks"])
    if abs(declared - total) > 1e-3:
        raise SystemExit(f"CONFIG_ERROR {args.format}: les blocs totalisent "
                         f"{declared}s, `total_s` annonce {total}s")

    ff.log(f"→ {ep['id']} « {ep['titre']} » · {args.format}")

    segments = [
        build_hook(ep, blocks["A"], fmt, tag),
        build_simple("assets/brand/sting-logo.mp4", blocks["B"], fmt, tag, "B"),
        build_simple("assets/brand/probleme.mp4", blocks["C"], fmt, tag, "C"),
        build_demo(blocks["D"], fmt, tag, args.format),
        build_simple("assets/brand/outro.mp4", blocks["E"], fmt, tag, "E",
                     fade_in_white=True),
    ]
    for s in segments:
        ff.log(f"  bloc {s.stem.split('_')[0][-1]}: {ff.duration(s):.3f}s "
               f"/ {ff.frames(s)} images")

    concat = ff.concat(segments, BUILD / f"concat_{tag}.mp4", BUILD)
    logo = overlay_logo(concat, BUILD / f"logo_{tag}.mp4", cfg, fmt)

    vo = None if args.skip_vo else build_vo_track(ep, fmt, tag, total)
    bed = music_bed(total)
    final = OUT / f"{ep['id']}_{args.format}.mp4"
    mix_audio(logo, vo, bed, final, total)

    ff.log("\nContrôle qualité :")
    tests = run_qa(final, concat, cfg, fmt)
    for t in tests:
        ff.log(f"  {'PASS' if t['ok'] else 'FAIL'}  {t['test']:<20} "
               f"{t['mesure']}  (attendu {t['attendu']})")

    passed = all(t["ok"] for t in tests)
    journal = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "episode": ep["id"], "titre": ep["titre"], "format": args.format,
        "publiable": bool(passed and not args.skip_vo),
        "vo_incluse": not args.skip_vo,
        "sources": {
            "hook": f"assets/hooks/{ep['id']}.mp4",
            "sting": "assets/brand/sting-logo.mp4",
            "probleme": "assets/brand/probleme.mp4",
            "demo": [f"build/demo_{n}_{args.format}.mp4" for n in DEMO_ORDER],
            "outro": "assets/brand/outro.mp4",
            "musique": "assets/music/bed.mp3",
            "vo": None if vo is None else str(vo.relative_to(ROOT)),
        },
        "durees_blocs": {b["id"]: block_seconds(b) for b in fmt["blocks"]},
        "qa": tests,
        "sortie": str(final.relative_to(ROOT)),
    }
    jp = BUILD / f"run_{time.strftime('%Y%m%d-%H%M%S')}_{tag}.json"
    jp.write_text(json.dumps(journal, indent=2, ensure_ascii=False) + "\n",
                  encoding="utf-8")

    if not passed:
        ff.log(f"\nQA_FAILED — {final.relative_to(ROOT)} NON publiable. "
               f"Journal : {jp.relative_to(ROOT)}", err=True)
        return 1
    if args.skip_vo:
        ff.log(f"\nOK (chaîne validée) mais SANS VO → non publiable. "
               f"Journal : {jp.relative_to(ROOT)}")
        return 0
    ff.log(f"\nOK → {final.relative_to(ROOT)} · journal {jp.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
