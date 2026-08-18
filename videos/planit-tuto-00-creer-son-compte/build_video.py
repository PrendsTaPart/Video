#!/usr/bin/env python3
"""Monte le tutoriel 00 « Créer son compte Plan'It ».

Assemble : animation d'ouverture → (plan avatar HeyGen, si présent) →
démonstration écran commentée par la voix off ElevenLabs → animation de fin
portant la punchline.

Principe de calage : **chaque segment dure exactement la longueur de sa ligne
de voix off**. Le rythme de l'écran s'adapte à la parole (accéléré sur les
saisies au clavier, ralenti sur les écrans à lire), jamais l'inverse — c'est ce
qui évite l'effet « carte de fin qui s'étire » rencontré sur les tutoriels
FoodEatUp.

    python3 build_video.py
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent
FONTS = ROOT.parent / "_shared" / "fonts"
ASSETS = ROOT / "assets"
VO = ROOT / "vo"
OUT = ROOT / "out"
WORK = ROOT / ".work"

SOURCE = ASSETS / "screencast-inscription.mp4"
PRESENTER = OUT / "presenter.mp4"        # bulle avatar, produite par build_presenter.py
AVATAR = ASSETS / "avatar-heygen.mp4"    # optionnel — plan HeyGen plein cadre
FINAL = OUT / "tuto-00-creer-son-compte.mp4"

AUDIO = ROOT / "audio"
STING = AUDIO / "sting-intro.mp3"          # animation sonore d'ouverture
MUSIC = AUDIO / "musique-produit.mp3"      # lit musical du produit
SIGNATURE = AUDIO / "signature-outro.mp3"  # identité sonore de fin

OUTRO_SECONDS = 5.2
MUSIC_DB = -21          # niveau du lit musical sous la parole
STING_DB = -7
SIGNATURE_DB = -5

W, H = 1080, 1920
FPS = 30
# Bandes noires du screencast, mesurées avec cropdetect sur la source.
CROP = "crop=590:1234:0:23"
PHONE_H = 1860  # hauteur du téléphone dans le cadre final

BACKGROUND_PAGE = (0xED, 0xEA, 0xFE)
PRIMARY = (0x4F, 0x2D, 0xF9)
ACCENT = (0xFE, 0x64, 0xD5)


@dataclass
class Segment:
    """Un plan de la démonstration : une plage source, une ligne de voix off."""

    vo: str          # nom du fichier dans vo/
    src_in: float    # entrée dans le screencast (secondes)
    src_out: float   # sortie dans le screencast (secondes)
    banner: str      # libellé du bandeau d'étape

    @property
    def source_span(self) -> float:
        return self.src_out - self.src_in


# Découpage calé sur l'analyse image par image du screencast.
# Les coupes entre segments retirent les temps morts : navigation vers l'écran
# d'accueil du téléphone (39,2 → 42,0), bascule multitâche (47,0 → 50,5) et
# chargement du tableau de bord (71,5 → 74,8 : squelettes et clavier encore
# à l'écran, le tableau de bord n'est peuplé qu'à partir de 74,8).
SEGMENTS = [
    Segment("N1",  0.0,  4.2, "1 · L'écran de connexion"),
    Segment("N2",  4.2, 13.0, "2 · Le formulaire d'inscription"),
    Segment("N3", 13.0, 17.5, "3 · L'adresse professionnelle"),
    Segment("N4", 17.5, 35.0, "4 · Mot de passe et confirmation"),
    Segment("N5", 35.2, 39.2, "5 · Le code à 6 chiffres"),
    Segment("N6", 42.0, 47.0, "6 · Le code reçu par email"),
    Segment("N7", 50.5, 58.5, "7 · Vérification du code"),
    Segment("N8", 58.8, 71.5, "8 · Première connexion"),
    Segment("N9", 74.8, 78.0, "9 · Votre espace est ouvert"),
]

PUNCHLINE_VO = "N10"  # posée sur l'animation de fin


# ── Outils ──────────────────────────────────────────────────────────────────────
def ffmpeg_bin() -> str:
    return shutil.which("ffmpeg") or __import__("imageio_ffmpeg").get_ffmpeg_exe()


def ffprobe_duration(path: Path) -> float:
    """Durée d'un média, lue via ffmpeg (ffprobe n'est pas garanti présent)."""
    proc = subprocess.run([ffmpeg_bin(), "-hide_banner", "-i", str(path)],
                          capture_output=True, text=True)
    for token in proc.stderr.split():
        pass
    for line in proc.stderr.splitlines():
        if "Duration:" in line:
            clock = line.split("Duration:")[1].split(",")[0].strip()
            h, m, s = clock.split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    raise RuntimeError(f"durée introuvable pour {path}")


def run(args: list[str]) -> None:
    subprocess.run(args, check=True)


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS / name), size)


# ── Bandeau d'étape ─────────────────────────────────────────────────────────────
def make_banner(text: str, path: Path) -> None:
    """Chip arrondi violet posé en bas de cadre, façon design system Plan'It."""
    layer = Image.new("RGBA", (W, 220), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    fnt = font("Manrope-700.ttf", 44)

    size = 44
    while size > 20 and d.textlength(text, font=font("Manrope-700.ttf", size)) > W - 260:
        size -= 2
    fnt = font("Manrope-700.ttf", size)

    tw = d.textlength(text, font=fnt)
    box = fnt.getbbox("Hg")
    th = box[3] - box[1]
    cx, cy = W // 2, 110
    pad_x, pad_y = 52, 28
    rect = (cx - tw / 2 - pad_x, cy - th / 2 - pad_y,
            cx + tw / 2 + pad_x, cy + th / 2 + pad_y)

    shadow = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle(
        (rect[0], rect[1] + 10, rect[2], rect[3] + 10),
        radius=(rect[3] - rect[1]) / 2, fill=(30, 10, 70, 90))
    layer.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(18)))

    d = ImageDraw.Draw(layer)
    d.rounded_rectangle(rect, radius=(rect[3] - rect[1]) / 2, fill=PRIMARY + (240,))
    d.text((cx, cy), text, font=fnt, fill=(255, 255, 255, 255), anchor="mm")
    layer.save(path)


# ── Rendu d'un segment ──────────────────────────────────────────────────────────
def render_segment(index: int, seg: Segment) -> Path:
    """Rend un plan à la durée exacte de sa ligne de voix off."""
    vo_path = VO / f"{seg.vo}.mp3"
    target = ffprobe_duration(vo_path)
    speed = seg.source_span / target  # >1 : accéléré · <1 : ralenti

    banner_png = WORK / f"banner{index:02d}.png"
    make_banner(seg.banner, banner_png)

    out = WORK / f"seg{index:02d}.mp4"
    pad_x = (W - round(590 * PHONE_H / 1234)) // 2
    pad_y = (H - PHONE_H) // 2

    # Le bandeau apparaît en glissant puis se retire en fin de plan.
    fade_in, fade_out = 0.35, 0.35
    banner_y = H - 345  # au-dessus de la barre d'onglets de l'app

    filtergraph = (
        f"[0:v]{CROP},setpts=(PTS-STARTPTS)/{speed:.6f},"
        f"scale=-2:{PHONE_H}:flags=lanczos,fps={FPS},"
        f"pad={W}:{H}:{pad_x}:{pad_y}:color=0x{BACKGROUND_PAGE[0]:02X}"
        f"{BACKGROUND_PAGE[1]:02X}{BACKGROUND_PAGE[2]:02X}[phone];"
        f"[1:v]format=rgba,"
        f"fade=t=in:st=0:d={fade_in}:alpha=1,"
        f"fade=t=out:st={max(target - fade_out, 0.1):.3f}:d={fade_out}:alpha=1[chip];"
        f"[phone][chip]overlay=0:{banner_y}:format=auto[v]"
    )

    run([
        ffmpeg_bin(), "-y", "-loglevel", "error",
        "-ss", f"{seg.src_in:.3f}", "-t", f"{seg.source_span:.3f}", "-i", str(SOURCE),
        "-loop", "1", "-t", f"{target:.3f}", "-i", str(banner_png),
        "-i", str(vo_path),
        "-filter_complex", filtergraph,
        "-map", "[v]", "-map", "2:a",
        "-t", f"{target:.3f}",
        "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-crf", "19",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        str(out),
    ])
    print(f"  segment {index} · {seg.banner} — {target:.2f} s (vitesse ×{speed:.2f})")
    return out


def normalise(path: Path, name: str, audio: Path | None = None) -> Path:
    """Ré-encode un plan aux mêmes caractéristiques que les segments.

    Indispensable avant le concat : les bumpers sont muets et les formats de
    pixel/cadence doivent correspondre exactement.
    """
    out = WORK / name
    duration = ffprobe_duration(path)
    args = [ffmpeg_bin(), "-y", "-loglevel", "error", "-i", str(path)]
    if audio is not None:
        args += ["-i", str(audio)]
    else:
        args += ["-f", "lavfi", "-t", f"{duration:.3f}",
                 "-i", "anullsrc=channel_layout=stereo:sample_rate=48000"]
    args += [
        "-filter_complex",
        f"[0:v]scale={W}:{H},fps={FPS},format=yuv420p[v];"
        f"[1:a]apad,atrim=0:{duration:.3f},asetpts=PTS-STARTPTS[a]",
        "-map", "[v]", "-map", "[a]", "-t", f"{duration:.3f}",
        "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-crf", "19",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        str(out),
    ]
    run(args)
    return out


def mix_audio(source: Path, target: Path) -> None:
    """Pose l'habillage sonore sur le master parole.

    Trois couches par-dessus la voix : le sting d'ouverture, le lit musical du
    produit et l'identité sonore de fin. La musique passe par un
    `sidechaincompress` piloté par la voix — elle se retire d'elle-même dès que
    la narratrice parle, et remonte dans les silences.
    """
    total = ffprobe_duration(source)
    outro_at = max(total - OUTRO_SECONDS, 0.0)
    sting_at = 0.9                      # le sting tombe sur l'arrivée du logo
    fade_out_at = max(total - 3.2, 0.1)

    graph = (
        f"[0:a]asplit=2[dial][key];"
        f"[1:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,"
        f"volume={MUSIC_DB}dB,"
        f"afade=t=in:st=0:d=1.4,afade=t=out:st={fade_out_at:.3f}:d=3.2[music];"
        f"[music][key]sidechaincompress="
        f"threshold=0.03:ratio=9:attack=12:release=420:makeup=1[ducked];"
        f"[2:a]adelay={int(sting_at * 1000)}|{int(sting_at * 1000)},"
        f"volume={STING_DB}dB[sting];"
        f"[3:a]adelay={int(outro_at * 1000)}|{int(outro_at * 1000)},"
        f"volume={SIGNATURE_DB}dB[sig];"
        f"[dial][ducked][sting][sig]amix=inputs=4:duration=first:"
        f"dropout_transition=0:normalize=0[mixed];"
        # Normalisation de diffusion : -16 LUFS, crête vraie -1,5 dBFS.
        f"[mixed]loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000[aout]"
    )

    run([
        ffmpeg_bin(), "-y", "-loglevel", "error",
        "-i", str(source), "-i", str(MUSIC), "-i", str(STING), "-i", str(SIGNATURE),
        "-filter_complex", graph,
        "-map", "0:v", "-map", "[aout]",
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        "-movflags", "+faststart", str(target),
    ])


def main() -> int:
    if not SOURCE.exists():
        print(f"screencast introuvable : {SOURCE}", file=sys.stderr)
        return 1
    if WORK.exists():
        shutil.rmtree(WORK)
    WORK.mkdir(parents=True)
    OUT.mkdir(exist_ok=True)

    print("Ouverture…")
    parts = [normalise(OUT / "intro.mp4", "00_intro.mp4")]

    if PRESENTER.exists():
        print("Bulle avatar de présentation…")
        parts.append(normalise(PRESENTER, "01_presenter.mp4"))
    else:
        print("Pas de bulle avatar — lancez d'abord build_presenter.py.")

    if AVATAR.exists():
        print("Plan avatar HeyGen plein cadre détecté.")
        parts.append(normalise(AVATAR, "02_avatar.mp4"))

    print("Démonstration…")
    for i, seg in enumerate(SEGMENTS, start=1):
        parts.append(render_segment(i, seg))

    print("Fin…")
    parts.append(normalise(OUT / "outro.mp4", "99_outro.mp4", audio=VO / f"{PUNCHLINE_VO}.mp3"))

    listing = WORK / "concat.txt"
    listing.write_text("".join(f"file '{p.resolve()}'\n" for p in parts))

    speech_only = WORK / "speech_only.mp4"
    run([
        ffmpeg_bin(), "-y", "-loglevel", "error",
        "-f", "concat", "-safe", "0", "-i", str(listing),
        "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-crf", "19",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        str(speech_only),
    ])

    print("Mixage sonore…")
    mix_audio(speech_only, FINAL)

    shutil.rmtree(WORK)
    print(f"\n✓ {FINAL} — {ffprobe_duration(FINAL):.2f} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
