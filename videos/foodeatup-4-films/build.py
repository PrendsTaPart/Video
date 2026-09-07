#!/usr/bin/env python3
"""Montage ffmpeg des 4 films FoodEatUp (clip, présentation, commercial, démo).

Pipeline sans dépendance externe : Pillow rend les cartons/logos en PNG (le ffmpeg
statique n'a pas drawtext), ffmpeg découpe, met à l'échelle, enchaîne, incruste, mixe.

    python3 build.py clip | presentation | commercial | demo | all
    REMIX=1 python3 build.py clip      # ne refait que le mixage audio (vidéo déjà rendue)

Sources :
- plans Higgsfield (bibliothèque existante, jamais régénérée) : assets/higgsfield/vNNN.mp4
- screencasts réels : ../foodeatup-*-tuto/assets/screen.mp4
- musiques originales ElevenLabs : assets/music/*.mp3
- voix off ElevenLabs : assets/vo/*.mp3
"""
import json
import os
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent.parent
WORK = ROOT / "work"
OUT = ROOT / "out"
HF = ROOT / "assets" / "higgsfield"
FONTS = REPO / "videos" / "stories-foodeatup-30j" / "assets" / "fonts"
LOGO_DIR = REPO / "studio-video" / "assets" / "brand" / "logo"

BLUE = (0, 123, 255)
ORANGE = (255, 165, 0)
CREAM = (252, 249, 230)
INK = (15, 26, 35)
WHITE = (255, 255, 255)

FPS = 30


def run(cmd, quiet=True):
    if not quiet:
        print(" ".join(str(c) for c in cmd))
    r = subprocess.run([str(c) for c in cmd], capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-3000:])
        raise SystemExit(f"ffmpeg failed: {cmd[:6]}")
    return r


def duration(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", str(path)],
                       capture_output=True, text=True)
    if r.returncode == 0:
        return float(json.loads(r.stdout)["format"]["duration"])
    r = subprocess.run(["ffmpeg", "-i", str(path)], capture_output=True, text=True).stderr
    import re
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r)
    return int(m[1]) * 3600 + int(m[2]) * 60 + float(m[3])


def font(weight=800, size=64):
    return ImageFont.truetype(str(FONTS / f"Poppins-{weight}.ttf"), size)


# ---------------------------------------------------------------- overlays (PNG)

def card(name, W, H, lines, size=96, color=WHITE, bg=None, pill=None, y=None, weight=800,
         align="center", shadow=True, pad=36, sub=None, sub_size=44, sub_color=None, logo=None,
         logo_w=None, box_alpha=0):
    """Rend un carton texte transparent (PNG RGBA) prêt pour overlay."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if bg is not None:
        d.rectangle([0, 0, W, H], fill=bg)
    if box_alpha:
        d.rectangle([0, 0, W, H], fill=(15, 26, 35, box_alpha))
    f = font(weight, size)
    lines = [lines] if isinstance(lines, str) else lines
    heights = [d.textbbox((0, 0), l, font=f)[3] - d.textbbox((0, 0), l, font=f)[1] for l in lines]
    gap = int(size * 0.28)
    total = sum(heights) + gap * (len(lines) - 1)
    if sub:
        fs = font(600, sub_size)
        sb = d.textbbox((0, 0), sub, font=fs)
        total += gap + (sb[3] - sb[1])
    ly = (H - total) // 2 if y is None else y
    logo_im = None
    if logo:
        logo_im = Image.open(logo).convert("RGBA")
        lw = logo_w or int(W * 0.55)
        logo_im = logo_im.resize((lw, int(logo_im.height * lw / logo_im.width)), Image.LANCZOS)
        ly_logo = ly - logo_im.height - gap * 2
        im.alpha_composite(logo_im, ((W - lw) // 2, max(0, ly_logo)))
    for l, h in zip(lines, heights):
        bb = d.textbbox((0, 0), l, font=f)
        tw = bb[2] - bb[0]
        x = (W - tw) // 2 if align == "center" else pad
        if pill:
            d.rounded_rectangle([x - pad, ly - pad // 2, x + tw + pad, ly + h + pad // 2 + 8], radius=(h + pad) // 2, fill=pill)
        if shadow and not pill:
            d.text((x + 4, ly + 6), l, font=f, fill=(0, 0, 0, 170))
        d.text((x, ly - bb[1]), l, font=f, fill=color)
        ly += h + gap
    if sub:
        fs = font(600, sub_size)
        bb = d.textbbox((0, 0), sub, font=fs)
        tw = bb[2] - bb[0]
        x = (W - tw) // 2 if align == "center" else pad
        if shadow:
            d.text((x + 3, ly + 4), sub, font=fs, fill=(0, 0, 0, 160))
        d.text((x, ly - bb[1]), sub, font=fs, fill=sub_color or color)
    p = WORK / f"ov-{name}.png"
    im.save(p)
    return p


def logo_corner(name, W, H, scale=0.28, margin=40, pos="tr"):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    lg = Image.open(LOGO_DIR / "foodeatup-logo-mascot.png").convert("RGBA")
    lw = int(W * scale)
    lg = lg.resize((lw, int(lg.height * lw / lg.width)), Image.LANCZOS)
    x = W - lw - margin if pos.endswith("r") else margin
    y = margin if pos.startswith("t") else H - lg.height - margin
    im.alpha_composite(lg, (x, y))
    p = WORK / f"ov-{name}.png"
    im.save(p)
    return p


def end_card(name, W, H, tagline_lines, url="foodeatup.fr", cta="Essai gratuit · sans carte bancaire"):
    im = Image.new("RGBA", (W, H), CREAM + (255,))
    d = ImageDraw.Draw(im)
    lg = Image.open(LOGO_DIR / "foodeatup-logo-horizontal.png").convert("RGBA")
    lw = int(W * (0.62 if W < H else 0.34))
    lg = lg.resize((lw, int(lg.height * lw / lg.width)), Image.LANCZOS)
    f1 = font(800, int(W * (0.062 if W < H else 0.036)))
    f2 = font(600, int(W * (0.040 if W < H else 0.024)))
    f3 = font(700, int(W * (0.046 if W < H else 0.028)))
    blocks = []
    tot = lg.height + int(W * 0.06)
    for l in tagline_lines:
        bb = d.textbbox((0, 0), l, font=f1); blocks.append((l, f1, bb)); tot += bb[3] - bb[1] + int(f1.size * 0.35)
    tot += int(W * 0.03)
    bb = d.textbbox((0, 0), cta, font=f2); blocks.append((cta, f2, bb)); tot += bb[3] - bb[1] + int(f2.size * 0.5)
    bb = d.textbbox((0, 0), url, font=f3); blocks.append((url, f3, bb)); tot += bb[3] - bb[1]
    y = (H - tot) // 2
    im.alpha_composite(lg, ((W - lw) // 2, y)); y += lg.height + int(W * 0.06)
    for i, (t, f, bb) in enumerate(blocks):
        tw = bb[2] - bb[0]
        col = INK if f is f1 else (INK if f is f2 else WHITE)
        x = (W - tw) // 2
        if f is f3:
            padx, pady = int(f.size * 0.7), int(f.size * 0.35)
            d.rounded_rectangle([x - padx, y - pady, x + tw + padx, y + bb[3] - bb[1] + pady], radius=int(f.size * 0.9), fill=BLUE)
        d.text((x, y - bb[1]), t, font=f, fill=col)
        y += bb[3] - bb[1] + int(f.size * (0.35 if f is f1 else 0.5)) + (int(W * 0.03) if f is f1 and t == tagline_lines[-1] else 0)
    p = WORK / f"ov-{name}.png"
    im.save(p)
    return p


# ---------------------------------------------------------------- segments

def seg_filter(W, H, fit, speed):
    vf = []
    if speed != 1.0:
        vf.append(f"setpts=PTS/{speed}")
    if fit == "cover":
        vf.append(f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}")
    elif fit == "contain":
        vf.append(f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=0x0F1A23")
    elif fit == "screen":  # screencast 16:9-ish posé sur fond crème avec ombre douce
        vf.append(f"scale={int(W*0.92)}:-2,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=0xFCF9E6")
    elif fit == "blur":  # 9:16 dans un 16:9 (ou inverse) avec fond flouté
        vf = [f"split[a][b];[a]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},gblur=sigma=40,eq=brightness=-0.08[bg];"
              f"[b]{'setpts=PTS/%s,' % speed if speed != 1.0 else ''}scale={W}:{H}:force_original_aspect_ratio=decrease[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2"]
        return ",".join(vf) + f",fps={FPS},format=yuv420p"
    vf.append(f"fps={FPS}")
    vf.append("format=yuv420p")
    return ",".join(vf)


_AUDIO_CACHE = {}


def has_audio(path):
    path = str(path)
    if path not in _AUDIO_CACHE:
        err = subprocess.run(["ffmpeg", "-i", path], capture_output=True, text=True).stderr
        _AUDIO_CACHE[path] = "Audio:" in err
    return _AUDIO_CACHE[path]


def render_segment(i, s, W, H):
    """s = dict(src, start, dur, speed=1, fit='cover', zoom=None, still=False)"""
    out = WORK / f"seg{i:02d}.mp4"
    src = Path(s["src"])
    speed = s.get("speed", 1.0)
    fit = s.get("fit", "cover")
    dur = s["dur"]
    cmd = ["ffmpeg", "-y", "-loglevel", "error"]
    if s.get("still"):
        cmd += ["-loop", "1", "-t", str(dur), "-i", src]
        vf = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},format=yuv420p"
        if s.get("zoom"):
            # lent zoom avant sur image fixe
            n = int(dur * FPS)
            vf = (f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
                  f"zoompan=z='1+0.08*on/{n}':d={n}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},format=yuv420p")
        cmd += ["-f", "lavfi", "-t", str(dur), "-i", "anullsrc=r=48000:cl=stereo",
                "-filter_complex", f"[0:v]{vf}[v]", "-map", "[v]", "-map", "1:a", "-shortest"]
    else:
        cmd += ["-ss", str(s.get("start", 0)), "-t", str(dur * speed + 0.2), "-i", src]
        vf = seg_filter(W, H, fit, speed)
        if has_audio(src):
            af = f"atempo={speed}," if speed != 1.0 else ""
            af += "aresample=48000,aformat=channel_layouts=stereo,apad"
            cmd += ["-filter_complex", f"[0:v]{vf}[v];[0:a]{af}[a]", "-map", "[v]", "-map", "[a]", "-t", str(dur)]
        else:
            cmd += ["-f", "lavfi", "-t", str(dur), "-i", "anullsrc=r=48000:cl=stereo",
                    "-filter_complex", f"[0:v]{vf}[v]", "-map", "[v]", "-map", "1:a", "-t", str(dur)]
    cmd += ["-c:v", "libx264", "-preset", "veryfast", "-crf", "17", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", out]
    run(cmd)
    return out


def concat(segs, name):
    lst = WORK / f"{name}-list.txt"
    lst.write_text("".join(f"file '{p}'\n" for p in segs))
    out = WORK / f"{name}-base.mp4"
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", out])
    return out


def apply_overlays(base, overlays, name, W, H):
    """overlays = list of dict(png, t0, t1, fin=0.25, fout=0.25, x=0, y=0, slide=None)"""
    if not overlays:
        return base
    out = WORK / f"{name}-video.mp4"
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", base]
    fc = []
    for k, o in enumerate(overlays):
        cmd += ["-loop", "1", "-t", str(o["t1"] - o["t0"] + 0.1), "-i", o["png"]]
        fin, fout = o.get("fin", 0.25), o.get("fout", 0.25)
        d = o["t1"] - o["t0"]
        f = f"[{k+1}:v]format=rgba,fade=t=in:st=0:d={fin}:alpha=1,fade=t=out:st={max(0, d-fout):.3f}:d={fout}:alpha=1,setpts=PTS-STARTPTS+{o['t0']}/TB[o{k}]"
        fc.append(f)
    prev = "[0:v]"
    for k, o in enumerate(overlays):
        x, y = o.get("x", 0), o.get("y", 0)
        if o.get("slide") == "up":
            y = f"{y}+(1-min(1\\,(t-{o['t0']})/0.5))*80"
        fc.append(f"{prev}[o{k}]overlay=x={x}:y={y}:enable='between(t,{o['t0']},{o['t1']})':eof_action=pass[v{k}]")
        prev = f"[v{k}]"
    cmd += ["-filter_complex", ";".join(fc), "-map", prev, "-map", "0:a", "-c:v", "libx264", "-preset", "medium", "-crf", "21",
            "-c:a", "copy", out]
    run(cmd)
    return out


def mix_audio(video, name, total, music=None, music_gain=-14.0, music_start=0.0, music_fade_out=3.0,
              vo=(), vo_gain=1.0, src_gain=-18.0, duck=0.22, src_ranges=None, final_out=None, music_end_at=None):
    """Mixe piste source (ducked), musique (ducked sous la voix) et voix off datées."""
    out = final_out or (OUT / f"{name}.mp4")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", video]
    fc = []
    idx = 1
    layers = []
    # voix off
    vo_labels = []
    for (f, t) in vo:
        cmd += ["-i", f]
        fc.append(f"[{idx}:a]aresample=48000,aformat=channel_layouts=stereo,volume={vo_gain},adelay={int(t*1000)}|{int(t*1000)},apad=whole_dur={total}[vo{idx}]")
        vo_labels.append(f"[vo{idx}]")
        idx += 1
    if vo_labels:
        fc.append("".join(vo_labels) + f"amix=inputs={len(vo_labels)}:normalize=0,atrim=0:{total}[vo]")
        fc.append("[vo]asplit=3[voA][voB][voC]")
    # musique
    if music:
        cmd += ["-ss", str(music_start), "-i", music]
        mend = music_end_at or total
        mf = (f"[{idx}:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{mend},volume={music_gain}dB,"
              f"afade=t=in:st=0:d=0.8,afade=t=out:st={max(0, mend-music_fade_out):.2f}:d={music_fade_out},apad=whole_dur={total}")
        if vo_labels:
            fc.append(mf + "[m0]")
            fc.append(f"[m0][voA]sidechaincompress=threshold=0.02:ratio=12:attack=40:release=500:makeup=1:level_sc={duck*6}[m]")
        else:
            fc.append(mf + "[m]")
        layers.append("[m]")
        idx += 1
    # piste source (ambiances / dialogues des plans)
    sf = f"[0:a]aresample=48000,aformat=channel_layouts=stereo,volume={src_gain}dB"
    if src_ranges:
        expr = "+".join(f"between(t,{a},{b})" for a, b in src_ranges)
        sf += f",volume='if({expr},1,0)':eval=frame"
    if vo_labels:
        fc.append(sf + "[s0]")
        fc.append(f"[s0][voB]sidechaincompress=threshold=0.02:ratio=10:attack=40:release=400:makeup=1[s]")
    else:
        fc.append(sf + "[s]")
    layers.append("[s]")
    if vo_labels:
        layers.append("[voC]")
    fc.append("".join(layers) + f"amix=inputs={len(layers)}:normalize=0:dropout_transition=0,atrim=0:{total},"
              f"loudnorm=I=-14:TP=-1.5:LRA=11,alimiter=limit=0.97[aout]")
    cmd += ["-filter_complex", ";".join(fc), "-map", "0:v", "-map", "[aout]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
            "-movflags", "+faststart", "-t", str(total), out]
    run(cmd)
    return out


def hf(i):
    return HF / f"v{i:03d}.mp4"


def tuto(name):
    return REPO / "videos" / f"foodeatup-{name}-tuto" / "assets" / "screen.mp4"


def vo(code):
    return ROOT / "assets" / "vo" / f"{code}.mp3"


def build_film(name, W, H, segments, overlays_fn, audio_kwargs):
    WORK.mkdir(exist_ok=True)
    OUT.mkdir(exist_ok=True)
    t = 0.0
    times = []
    for s in segments:
        times.append(t)
        t += s["dur"]
    total = round(t, 3)
    video = WORK / f"{name}-video.mp4"
    if os.environ.get("REMIX") and video.exists():
        print(f"{name}: remix audio seul sur {video.name}")
    else:
        segs = [render_segment(i, s, W, H) for i, s in enumerate(segments)]
        base = concat(segs, name)
        ovs = overlays_fn(W, H, times, total)
        video = apply_overlays(base, ovs, name, W, H)
    final = mix_audio(video, name, total, **audio_kwargs)
    print(f"{name}: {total:.1f}s -> {final}")
    return final


def to_16x9(src, name):
    """Version 16:9 : le 9:16 centré sur son propre fond flouté."""
    out = OUT / f"{name}-16x9.mp4"
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-filter_complex",
         "[0:v]split[a][b];[a]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,gblur=sigma=45,eq=brightness=-0.1[bg];"
         "[b]scale=-2:1080[fg];[bg][fg]overlay=(W-w)/2:0,format=yuv420p[v]",
         "-map", "[v]", "-map", "0:a", "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-c:a", "copy", "-movflags", "+faststart", out])
    return out


if __name__ == "__main__":
    import films
    which = sys.argv[1:] or ["all"]
    if "all" in which:
        which = ["clip", "presentation", "commercial", "demo"]
    for w in which:
        getattr(films, w)()
