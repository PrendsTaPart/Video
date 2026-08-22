#!/usr/bin/env python3
"""Moteur de fabrication de l'Académie Plan'It — commun aux 43 tutoriels.

Chaque épisode se réduit à une fiche de configuration (`Episode`) : le reste —
ouverture, bulle de présentation, montage de la démonstration, mixage sonore,
vignette — est produit ici, à l'identique d'un épisode à l'autre.

Ce qui est **généré une seule fois puis réutilisé** (`assets/`) :

* `avatar-generique.mp4` — le plan de synchronisation labiale de la présentatrice.
  Un seul rendu `creatify-aurora` pour toute la série. Il est bouclé en
  aller-retour pour couvrir la durée de la voix de chaque épisode.
* `sting-intro.mp3`, `musique-produit.mp3`, `signature-outro.mp3` — l'identité
  sonore.
* Le portrait, les logos, les polices.

Ce qui change à chaque épisode : **les lignes de voix off**, et elles seules.

Règle de calage : chaque plan dure exactement la longueur de sa ligne de voix.
La vitesse du plan en découle — jamais l'inverse.
"""

from __future__ import annotations

import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

from habillage import (Fin, Ouverture, Presentatrice, rendre_fin,
                       rendre_ouverture, rendre_presentatrice)
from habillage.fin import BASELINE, PUNCHLINE_BAS, PUNCHLINE_HAUT
from habillage.fin import DUREE as OUTRO_SECONDS
from habillage.noyau import (ACCENT, ASSETS as SHARED, AUDIO as SHARED_AUDIO,
                             BACKGROUND_PAGE, BRAND_GRADIENT, FPS, H, PRIMARY,
                             PRIMARY_BUTTON, SAFE_MARGIN, TEXT_DARK, W, WHITE,
                             duration_of, ffmpeg_bin, fitted, font, glow,
                             hex_rgb, run, vertical_gradient)
from habillage.ouverture import DUREE as INTRO_SECONDS

MUSIC_DB = -21
STING_DB = -7
SIGNATURE_DB = -5

PUNCHLINE_TOP = PUNCHLINE_HAUT
PUNCHLINE_BOTTOM = PUNCHLINE_BAS


# ── Description d'un épisode ───────────────────────────────────────────────────
@dataclass
class Segment:
    """Un plan de la démonstration : une plage source, une ligne de voix off."""

    vo: str
    src_in: float
    src_out: float
    banner: str

    @property
    def source_span(self) -> float:
        return self.src_out - self.src_in


@dataclass
class Episode:
    numero: int
    slug: str
    titre: str              # fiche.titre
    titre_court: str        # fiche.titreVignette
    promesse: str
    presentation: str       # ce que dit l'avatar
    module_nom: str
    module_couleur: str
    variante: str           # « A » avatar dominant · « B » écran dominant
    suivant: str            # titre du tutoriel suivant
    crop: str               # recadrage du screencast
    segments: list[Segment]
    racine: Path
    ecran_vignette: float = 0.5   # instant du screencast utilisé pour la vignette
    chapitres: list = field(default_factory=list)

    @property
    def out(self) -> Path:
        return self.racine / "out"

    @property
    def vo(self) -> Path:
        return self.racine / "vo"

    @property
    def screencast(self) -> Path:
        return self.racine / "assets" / "screencast.mp4"

    @property
    def final(self) -> Path:
        return self.out / f"tuto-{self.numero:02d}-{self.slug}.mp4"


# ── Habillage — les trois gabarits partagés ────────────────────────────────────
# Ouverture, bulle de présentation et fin vivent dans `habillage/`, hors de ce
# fichier : ce sont des gabarits réutilisables, documentés dans
# `habillage/README.md` et rendables seuls (`python3 -m habillage …`). Ici, on
# se contente de les nourrir depuis la fiche de l'épisode.
def build_bumpers(ep: Episode) -> tuple[Path, Path]:
    intro = rendre_ouverture(Ouverture(titre=ep.titre_court, numero=ep.numero),
                             ep.out / "intro.mp4", ep.racine / ".frames")
    print(f"  intro — {INTRO_SECONDS:.2f} s")
    outro = rendre_fin(Fin(suivant=ep.suivant, couleur=ep.module_couleur),
                       ep.out / "outro.mp4", ep.racine / ".frames")
    print(f"  outro — {OUTRO_SECONDS:.2f} s")
    return intro, outro


def build_presenter(ep: Episode) -> Path:
    """Carte de présentation : plan générique réutilisé + voix propre à l'épisode."""
    cible = rendre_presentatrice(
        Presentatrice(titre=ep.titre_court, promesse=ep.promesse,
                      numero=ep.numero, voix=ep.vo / "N0.mp3"),
        ep.out / "presenter.mp4", ep.racine / ".presenter")
    print(f"  bulle — {duration_of(cible):.2f} s")
    return cible


# ── Démonstration ──────────────────────────────────────────────────────────────
def make_banner(text: str, path: Path) -> None:
    layer = Image.new("RGBA", (W, 220), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    fnt = fitted("Manrope-700.ttf", 44, text, W - 260)
    tw = d.textlength(text, font=fnt)
    box = fnt.getbbox("Hg")
    th = box[3] - box[1]
    cx, cy = W // 2, 110
    rect = (cx - tw / 2 - 52, cy - th / 2 - 28, cx + tw / 2 + 52, cy + th / 2 + 28)

    sh = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((rect[0], rect[1] + 10, rect[2], rect[3] + 10),
                                         radius=(rect[3] - rect[1]) / 2, fill=(30, 10, 70, 90))
    layer.alpha_composite(sh.filter(ImageFilter.GaussianBlur(18)))
    d = ImageDraw.Draw(layer)
    d.rounded_rectangle(rect, radius=(rect[3] - rect[1]) / 2, fill=PRIMARY + (240,))
    d.text((cx, cy), text, font=fnt, fill=(255, 255, 255, 255), anchor="mm")
    layer.save(path)


def crop_dimensions(crop: str) -> tuple[int, int]:
    parts = crop.split("=")[1].split(":")
    return int(parts[0]), int(parts[1])


def render_segment(ep: Episode, index: int, seg: Segment, work: Path) -> Path:
    target_dur = duration_of(ep.vo / f"{seg.vo}.mp3")
    speed = seg.source_span / target_dur

    banner_png = work / f"banner{index:02d}.png"
    make_banner(seg.banner, banner_png)

    src_w, src_h = crop_dimensions(ep.crop)
    phone_h = 1860
    pad_x = (W - round(src_w * phone_h / src_h)) // 2
    pad_y = (H - phone_h) // 2
    fade = 0.35
    bg_hex = "".join(f"{c:02X}" for c in BACKGROUND_PAGE)

    graph = (
        f"[0:v]{ep.crop},setpts=(PTS-STARTPTS)/{speed:.6f},"
        f"scale=-2:{phone_h}:flags=lanczos,fps={FPS},"
        f"pad={W}:{H}:{pad_x}:{pad_y}:color=0x{bg_hex}[phone];"
        f"[1:v]format=rgba,fade=t=in:st=0:d={fade}:alpha=1,"
        f"fade=t=out:st={max(target_dur - fade, 0.1):.3f}:d={fade}:alpha=1[chip];"
        f"[phone][chip]overlay=0:{H - 345}:format=auto[v]"
    )
    out = work / f"seg{index:02d}.mp4"
    run([ffmpeg_bin(), "-y", "-loglevel", "error",
         "-ss", f"{seg.src_in:.3f}", "-t", f"{seg.source_span:.3f}", "-i", str(ep.screencast),
         "-loop", "1", "-t", f"{target_dur:.3f}", "-i", str(banner_png),
         "-i", str(ep.vo / f"{seg.vo}.mp3"),
         "-filter_complex", graph, "-map", "[v]", "-map", "2:a",
         "-t", f"{target_dur:.3f}",
         "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-crf", "19",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", str(out)])
    print(f"  plan {index} · {seg.banner} — {target_dur:.2f} s (vitesse ×{speed:.2f})")
    return out


def normalise(path: Path, name: str, work: Path) -> Path:
    """Aligne un plan sur le format des segments, en **conservant son audio**.

    Un plan muet (les bumpers) reçoit une piste de silence ; un plan qui parle —
    la bulle de présentation — garde la sienne. C'est la correction du défaut qui
    faisait disparaître la voix de la présentatrice du montage final.
    """
    out = work / name
    dur = duration_of(path)
    probe = subprocess.run([ffmpeg_bin(), "-hide_banner", "-i", str(path)],
                           capture_output=True, text=True).stderr
    has_audio = "Audio:" in probe

    args = [ffmpeg_bin(), "-y", "-loglevel", "error", "-i", str(path)]
    if has_audio:
        audio_in = "[0:a]"
    else:
        args += ["-f", "lavfi", "-t", f"{dur:.3f}",
                 "-i", "anullsrc=channel_layout=stereo:sample_rate=48000"]
        audio_in = "[1:a]"
    args += ["-filter_complex",
             f"[0:v]scale={W}:{H},fps={FPS},format=yuv420p[v];"
             f"{audio_in}aresample=48000,aformat=channel_layouts=stereo,"
             f"apad,atrim=0:{dur:.3f},asetpts=PTS-STARTPTS[a]",
             "-map", "[v]", "-map", "[a]", "-t", f"{dur:.3f}",
             "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-crf", "19",
             "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", str(out)]
    run(args)
    return out


# ── Mixage ─────────────────────────────────────────────────────────────────────
def mix_audio(source: Path, target: Path) -> None:
    """Pose l'habillage sonore sur le master parole.

    La musique passe par un `sidechaincompress` piloté par la voix : elle se
    retire dès qu'on parle et remonte dans les silences.
    """
    total = duration_of(source)
    outro_at = max(total - OUTRO_SECONDS, 0.0)
    fade_out_at = max(total - 3.2, 0.1)

    graph = (
        f"[0:a]asplit=2[dial][key];"
        f"[1:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,volume={MUSIC_DB}dB,"
        f"afade=t=in:st=0:d=1.4,afade=t=out:st={fade_out_at:.3f}:d=3.2[music];"
        f"[music][key]sidechaincompress=threshold=0.03:ratio=9:attack=12:"
        f"release=420:makeup=1[ducked];"
        f"[2:a]adelay=900|900,volume={STING_DB}dB[sting];"
        f"[3:a]adelay={int(outro_at * 1000)}|{int(outro_at * 1000)},"
        f"volume={SIGNATURE_DB}dB[sig];"
        f"[dial][ducked][sting][sig]amix=inputs=4:duration=first:"
        f"dropout_transition=0:normalize=0[mixed];"
        f"[mixed]loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000[aout]"
    )
    run([ffmpeg_bin(), "-y", "-loglevel", "error", "-i", str(source),
         "-i", str(SHARED_AUDIO / "musique-produit.mp3"),
         "-i", str(SHARED_AUDIO / "sting-intro.mp3"),
         "-i", str(SHARED_AUDIO / "signature-outro.mp3"),
         "-filter_complex", graph, "-map", "0:v", "-map", "[aout]", "-c:v", "copy",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
         "-movflags", "+faststart", str(target)])


# ── Vignette ───────────────────────────────────────────────────────────────────
def build_thumbnail(ep: Episode) -> Path:
    """Vignette 1080 × 1920 exportée en 2160 × 3840, au gabarit du MCP."""
    scale = 2
    tw, th = W * scale, H * scale
    module = hex_rgb(ep.module_couleur)
    lighter = tuple(min(255, round(c + (255 - c) * 0.34)) for c in module)

    canvas = vertical_gradient(tw, th, [lighter, module]).convert("RGBA")
    canvas.alpha_composite(glow(int(tw * 0.18), int(th * 0.12), 900, WHITE, 0.16, (tw, th)))
    canvas.alpha_composite(glow(int(tw * 0.84), int(th * 0.70), 1000, ACCENT, 0.28, (tw, th)))

    def f(name, size, text, max_w):
        probe = ImageDraw.Draw(Image.new("L", (1, 1)))
        while size > 20 and probe.textlength(text, font=font(name, size)) > max_w:
            size -= 4
        return font(name, size)

    d = ImageDraw.Draw(canvas)
    margin = 130

    logo = Image.open(SHARED / "white_logo.png").convert("RGBA").resize((150, 150), Image.LANCZOS)
    canvas.alpha_composite(logo, (margin, 170))
    d.text((margin + 200, 248), "ACADÉMIE PLAN'IT", font=font("Manrope-700.ttf", 62),
           fill=WHITE + (235,), anchor="lm")

    title_font = f("Sora-800.ttf", 210, ep.titre_court, tw - 2 * margin)
    sh = Image.new("RGBA", (tw, th), (0, 0, 0, 0))
    ImageDraw.Draw(sh).text((margin, 640), ep.titre_court, font=title_font,
                            fill=(25, 5, 70, 130), anchor="lm")
    canvas.alpha_composite(sh.filter(ImageFilter.GaussianBlur(22)))
    d = ImageDraw.Draw(canvas)
    d.text((margin, 630), ep.titre_court, font=title_font, fill=WHITE + (255,), anchor="lm")

    sub_font = f("Manrope-600.ttf", 84, ep.titre, tw - 2 * margin)
    d.text((margin, 810), ep.titre, font=sub_font, fill=(255, 255, 255, 225), anchor="lm")

    chip = f"TUTORIEL {ep.numero:02d} · {ep.module_nom.upper()}"
    chip_font = f("Manrope-700.ttf", 62, chip, tw - 2 * margin - 140)
    cw = d.textlength(chip, font=chip_font)
    d.rounded_rectangle((margin, 940, margin + cw + 130, 1080), radius=70,
                        fill=(255, 255, 255, 240))
    d.text((margin + 65 + cw / 2, 1010), chip, font=chip_font, fill=module + (255,), anchor="mm")

    # Bas de vignette : l'écran de l'app et la présentatrice.
    screen = _screen_still(ep)
    avatar = _cutout(SHARED / "avatar-presentatrice.png")

    if ep.variante.upper() == "A":
        av_h, av_cx = int(th * 0.56), int(tw * 0.66)
        ph_h, ph_cx = int(th * 0.44), int(tw * 0.26)
    else:
        av_h, av_cx = int(th * 0.44), int(tw * 0.80)
        ph_h, ph_cx = int(th * 0.55), int(tw * 0.38)

    if screen is not None:
        ph_w = int(ph_h * screen.width / screen.height)
        phone = _rounded(screen.resize((ph_w, ph_h), Image.LANCZOS), 54)
        sh = Image.new("RGBA", (ph_w + 160, ph_h + 160), (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle((80, 90, ph_w + 80, ph_h + 90),
                                             radius=54, fill=(20, 5, 60, 150))
        sh = sh.filter(ImageFilter.GaussianBlur(46))
        tilted = phone.rotate(-7, expand=True, resample=Image.BICUBIC)
        tsh = sh.rotate(-7, expand=True, resample=Image.BICUBIC)
        py = th - ph_h - 120
        canvas.alpha_composite(tsh, (ph_cx - tsh.width // 2, py - 80))
        canvas.alpha_composite(tilted, (ph_cx - tilted.width // 2, py))

    avatar = avatar.resize((int(avatar.width * av_h / avatar.height), av_h), Image.LANCZOS)
    canvas.alpha_composite(glow(av_cx, int(th * 0.76), 560, WHITE, 0.20, (tw, th)))
    canvas.alpha_composite(avatar, (av_cx - avatar.width // 2, th - av_h))

    ep.out.mkdir(parents=True, exist_ok=True)
    target = ep.out / f"vignette-tuto-{ep.numero:02d}.png"
    canvas.convert("RGB").save(target, "PNG")
    print(f"  vignette — {tw} × {th}")
    return target


def _screen_still(ep: Episode) -> Image.Image | None:
    if not ep.screencast.exists():
        return None
    tmp = ep.out / ".still.png"
    ep.out.mkdir(parents=True, exist_ok=True)
    run([ffmpeg_bin(), "-y", "-loglevel", "error", "-ss", str(ep.ecran_vignette),
         "-i", str(ep.screencast), "-frames:v", "1", "-vf", ep.crop, str(tmp)])
    img = Image.open(tmp).convert("RGBA")
    tmp.unlink()
    return img


def _rounded(image: Image.Image, radius: int) -> Image.Image:
    mask = Image.new("L", image.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, image.width - 1, image.height - 1),
                                           radius=radius, fill=255)
    out = image.copy()
    out.putalpha(mask)
    return out


def _cutout(path: Path) -> Image.Image:
    """Détoure le portrait, fourni sur fond gris studio uni."""
    src = Image.open(path).convert("RGBA")
    px = src.load()
    for y in range(src.height):
        for x in range(src.width):
            r, g, b, _ = px[x, y]
            if abs(r - g) < 9 and abs(g - b) < 9 and 92 < r < 125:
                px[x, y] = (r, g, b, 0)
    return src


# ── Chaîne complète ────────────────────────────────────────────────────────────
def build_episode(ep: Episode) -> Path:
    print(f"\n=== Tutoriel {ep.numero:02d} — {ep.titre} ===")
    work = ep.racine / ".work"
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)
    ep.out.mkdir(parents=True, exist_ok=True)

    print("Ouverture et fin…")
    intro, outro = build_bumpers(ep)

    print("Présentation…")
    presenter = build_presenter(ep)

    print("Démonstration…")
    parts = [normalise(intro, "00_intro.mp4", work),
             normalise(presenter, "01_presenter.mp4", work)]
    for i, seg in enumerate(ep.segments, start=1):
        parts.append(render_segment(ep, i, seg, work))
    parts.append(normalise(outro, "99_outro.mp4", work))

    listing = work / "concat.txt"
    listing.write_text("".join(f"file '{p.resolve()}'\n" for p in parts))
    speech = work / "speech.mp4"
    run([ffmpeg_bin(), "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
         "-i", str(listing), "-c:v", "libx264", "-profile:v", "high",
         "-pix_fmt", "yuv420p", "-crf", "19",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", str(speech)])

    print("Mixage sonore…")
    mix_audio(speech, ep.final)

    print("Vignette…")
    build_thumbnail(ep)

    shutil.rmtree(work)
    print(f"\n✓ {ep.final} — {duration_of(ep.final):.2f} s")
    return ep.final
