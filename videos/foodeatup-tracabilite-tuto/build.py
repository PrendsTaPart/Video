#!/usr/bin/env python3
# FoodEatUp "Historique de la production et traçabilité" tutorial.
# Full ElevenLabs VO (no avatar clip). Speed = setpts (never zoompan on real
# footage). xfade on every cut, forced back to yuv420p at the end of the
# chain. 48kHz stereo AAC, +faststart.
#
# The rush is a *consultation* flow, not a creation flow: the whole point is
# the three filters of the "Mes productions" page (statut, recherche par nom,
# période de dates) plus the "Voir la traçabilité" button that a realized
# production exposes. Nothing is created on screen, so the 3 zoom-punches sit
# on the filter controls rather than on a submit button.
import subprocess, os, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (
    render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png,
)

ROOT = "/home/user/Video/videos/foodeatup-tracabilite-tuto"
SRC  = f"{ROOT}/assets/screen.mp4"
W, H, FPS = 1920, 828, 25
SEG = f"{ROOT}/work/seg"
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
BLUE, ORANGE = "0x1B6DF3", "0xF7941D"
XF = 0.28
os.makedirs(SEG, exist_ok=True)

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("ERR:", " ".join(cmd)[:300]); print(r.stderr[-2000:]); raise SystemExit(1)

def dur(path):
    r = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                        "-of","csv=p=0",path], capture_output=True, text=True)
    return float(r.stdout.strip())

def clamp(v, lo, hi): return max(lo, min(hi, v))

ZOOM = 1.20
def crop_for(btn):
    bx, by = btn
    cw, ch = int(W/ZOOM), int(H/ZOOM); cw -= cw % 2; ch -= ch % 2
    x = int(clamp(bx - cw/2, 0, W - cw)); y = int(clamp(by - ch/2, 0, H - ch))
    return f"crop={cw}:{ch}:{x}:{y},scale={W}:{H}:flags=bicubic", (cw, ch, x, y)

def punch_highlight(btn, btn_wh, crop_box):
    """Static orange frame around the clicked control.

    Deliberately NOT animated: in drawbox the expression variable `t` is the
    box *thickness*, not the timestamp (unlike drawtext/overlay). Earlier
    builds in this series used `sin(...t...)` here believing it was time --
    it silently resolved to a constant. See the workflow doc."""
    cw, ch, cx, cy = crop_box
    sx, sy = W / cw, H / ch
    bw, bh = btn_wh[0] * sx, btn_wh[1] * sy
    ox, oy = (btn[0] - cx) * sx, (btn[1] - cy) * sy
    p = 14
    return (f"drawbox=x={ox-bw/2-p:.0f}:y={oy-bh/2-p:.0f}"
            f":w={bw+2*p:.0f}:h={bh+2*p:.0f}:color={ORANGE}@0.95:t=5")

BANNER_H, BANNER_FS, BANNER_BAR, BANNER_PAD = 62, 31, 10, 24
def banner_png(text, path):
    """Step banner rendered with PIL, then slid in with `overlay`.

    It cannot be drawn with drawbox: drawbox's `t` variable is the thickness,
    so the slide expression froze the box off-screen and only the drawtext
    caption (where `t` really is the timestamp) ever showed -- white text on a
    light UI, i.e. unreadable. overlay's x IS evaluated per frame against real
    time, so the animation belongs there."""
    font = ImageFont.truetype(FONT, BANNER_FS)
    probe = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    tw = probe.textbbox((0, 0), text, font=font)[2]
    w = BANNER_BAR + BANNER_PAD * 2 + tw
    img = Image.new("RGBA", (w, BANNER_H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, BANNER_BAR, BANNER_H], fill=(247, 148, 29, 250))          # #F7941D
    d.rectangle([BANNER_BAR, 0, w, BANNER_H], fill=(27, 109, 243, 235))          # #1B6DF3
    d.text((BANNER_BAR + BANNER_PAD, (BANNER_H - BANNER_FS) / 2 - 3), text,
           font=font, fill=(255, 255, 255, 255))
    img.save(path)
    return w

def banner_overlay(text, seg_dur, png_path):
    """Returns (overlay_filter, png_path) or (None, None)."""
    if not text: return None, None
    w = banner_png(text, png_path)
    tin, sl, rest = 0.15, 0.32, 60
    tout = max(tin + sl + 0.3, seg_dur - 0.55)
    a = f"min(1\\,max(0\\,(t-{tin})/{sl}))"
    b = f"min(1\\,max(0\\,(t-{tout})/{sl}))"
    travel = w + rest
    x = f"-{w}+{travel}*({a})-{travel}*({b})"
    return f"overlay=x='{x}':y={H - 108}:format=auto", png_path

# Button boxes measured by colour-thresholding the real frames (work/frames/),
# not eyeballed. Click instants located to 0.2s by tracking the "Total" counter
# (532 -> 81 at 7.60s, 204 -> 2 at 39.00s) and the date panel appearing (28.20s).
# No apostrophe in any caption below (drawtext quoting bug, see the workflow doc).
BTN_STATUS = (1139, 197); SZ_STATUS = (272, 66)  # sélecteur de statut
BTN_DATES  = (1675, 197); SZ_DATES  = (240, 46)  # filtre "Toutes les dates"
BTN_APPLY  = (1675, 421); SZ_APPLY  = (240, 44)  # bouton "Appliquer"

# (name, src_start, src_end, target_out_duration, button, btn_size, caption)
segs = [
    ("A", 0.30,  5.20,  6.50, None,       None,       "1 · Toutes vos productions"),
    ("B", 7.30,  7.65,  0.90, BTN_STATUS, SZ_STATUS,  None),
    ("C", 7.70,  10.50, 4.40, None,       None,       "2 · Filtrer par statut"),
    ("D", 10.60, 13.60, 5.40, None,       None,       "Prêt à produire"),
    ("E", 13.90, 21.40, 5.50, None,       None,       "3 · Les productions réalisées"),
    ("F", 21.60, 26.60, 4.00, None,       None,       "4 · Rechercher une recette"),
    ("G", 27.75, 28.10, 0.90, BTN_DATES,  SZ_DATES,   None),
    ("H", 28.20, 38.80, 4.80, None,       None,       "5 · Choisir une période"),
    ("I", 38.80, 39.15, 0.90, BTN_APPLY,  SZ_APPLY,   None),
    ("J", 39.20, 44.60, 4.90, None,       None,       "Historique de la période"),
    ("K", 44.60, 52.80, 5.30, None,       None,       "Traçabilité complète"),
]
INTRO_D, OUTRO_D = 4.60, 6.20

def encode_seg(name, s, e, target, btn, btn_sz, caption):
    out = f"{SEG}/{name}.mp4"
    factor = (e - s) / target
    vf = f"setpts=(PTS-STARTPTS)/{factor:.6f}"
    if btn:
        crop_vf, box = crop_for(btn)
        vf += f",{crop_vf},{punch_highlight(btn, btn_sz, box)}"
    else:
        vf += f",scale={W}:{H}"
    vf += f",fps={FPS}"
    ov, png = banner_overlay(caption, target, f"{SEG}/ban_{name}.png")
    cmd = ["ffmpeg","-y","-v","error","-ss",str(s),"-to",str(e),"-i",SRC,"-an"]
    if ov:
        cmd += ["-i", png, "-filter_complex",
                f"[0:v]{vf}[bg];[bg][1:v]{ov},format=yuv420p[vout]", "-map", "[vout]"]
    else:
        cmd += ["-vf", f"{vf},format=yuv420p"]
    cmd += ["-r",str(FPS),"-c:v","libx264","-preset","medium","-crf","18",out]
    run(cmd)
    return out

# ---------------------------------------------------------------------------
# "Use it with Claude" sequence -- shared 3-stage chatbot animation
# (videos/_shared/claude_prompt_sequence.py). The matching tool is
# mcp__FoodEatUp__list_production_plans(establishment_id, start_date,
# end_date, status) -- it covers exactly the two filters the rush demonstrates
# (statut + période), fields checked against the tool schema.
# ---------------------------------------------------------------------------
CLAUDE_PROMPT = ("Liste mes productions au statut [statut] entre le "
                 "[date de début] et le [date de fin] pour mon établissement "
                 "FoodEatUp (ID [ID établissement]).")
CLAUDE_RESPONSE = "Bien sûr ! Voici vos productions sur cette période…"

def card(img, out, secs, zoom_in=True, fade=True):
    """fade=False for the claude stages: they sit mid-video and only meet the
    timeline through xfade -- adding card()'s own fade-to-black on top makes
    short stages read as a murky blur (bug hit on the tva build)."""
    z0, z1 = (1.0, 1.09) if zoom_in else (1.09, 1.0)
    frames = int(secs * FPS)
    zexpr = f"{z0}+({z1}-{z0})*on/{frames}"
    vf = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
          f"boxblur=20:2,eq=brightness=-0.06[bg];"
          f"[0:v]scale={W}:{H}:force_original_aspect_ratio=decrease[fg];"
          f"[bg][fg]overlay=(W-w)/2:(H-h)/2,scale={W*2}:{H*2},"
          f"zoompan=z='{zexpr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
          f":d=1:s={W}x{H}:fps={FPS}")
    if fade:
        vf += f",fade=t=in:st=0:d=0.4,fade=t=out:st={secs-0.4:.3f}:d=0.4"
    vf += ",format=yuv420p"
    run(["ffmpeg","-y","-v","error","-loop","1","-t",str(secs),"-i",img,
         "-filter_complex",vf,"-r",str(FPS),
         "-c:v","libx264","-preset","medium","-crf","18",out])

# N9 (4.41s) has to live inside reveal+copied, N10 (4.68s) inside the chatbot
# stage -- sized from the measured VO durations, per the workflow rule.
CLAUDE_STAGE_D = [5.50, 2.60, 5.80]  # reveal, copied, chatbot mockup

def build_silent(outro_d):
    card(f"{ROOT}/assets/intro.jpg", f"{SEG}/intro.mp4", INTRO_D, zoom_in=True)
    card(f"{ROOT}/assets/outro.jpg", f"{SEG}/outro.mp4", outro_d, zoom_in=False)
    c1, c2, c3 = f"{SEG}/claude1.png", f"{SEG}/claude2.png", f"{SEG}/claude3.png"
    if not os.path.exists(c1):
        render_claude_stage1_png(c1, W, H, CLAUDE_PROMPT)
    if not os.path.exists(c2):
        render_claude_stage2_png(c2, W, H, CLAUDE_PROMPT)
    if not os.path.exists(c3):
        render_claude_stage3_png(c3, W, H, CLAUDE_PROMPT, response=CLAUDE_RESPONSE)
    for i, png in enumerate([c1, c2, c3]):
        card(png, f"{SEG}/claude{i+1}.mp4", CLAUDE_STAGE_D[i], zoom_in=True, fade=False)
    parts = [f"{SEG}/intro.mp4"]
    for name, s, e, target, btn, sz, cap in segs:
        parts.append(encode_seg(name, s, e, target, btn, sz, cap))
    parts += [f"{SEG}/claude1.mp4", f"{SEG}/claude2.mp4", f"{SEG}/claude3.mp4",
              f"{SEG}/outro.mp4"]

    trans = ["fade",       # intro -> A
             "fade",       # A -> B (continuous: click on the visible toolbar)
             "fade",       # B -> C (the filter applies on the same page)
             "slideleft",  # C -> D (statut change: new list)
             "slideleft",  # D -> E (statut change: new list)
             "slideleft",  # E -> F (search field)
             "fade",       # F -> G (continuous: click on the date filter)
             "fade",       # G -> H (panel opens on the same page)
             "fade",       # H -> I (continuous: click Appliquer)
             "fade",       # I -> J (submit -> filtered list)
             "slideleft",  # J -> K (another period)
             "slideleft",  # K -> claude1
             "slideleft",  # claude1 -> claude2
             "slideleft",  # claude2 -> claude3
             "fade"]       # claude3 -> outro
    durs = [dur(p) for p in parts]
    starts, acc = [], 0.0
    for i, d in enumerate(durs):
        starts.append(acc); acc += d - (XF if i < len(durs) - 1 else 0)

    inputs, fc, cur = [], [], "[0:v]"
    for p in parts: inputs += ["-i", p]
    for k in range(len(parts) - 1):
        off = starts[k + 1]
        lbl = f"[x{k}]"
        fc.append(f"{cur}[{k+1}:v]xfade=transition={trans[k]}:duration={XF}"
                  f":offset={off:.4f}{lbl}")
        cur = lbl
    fc.append(f"{cur}format=yuv420p[vout]")
    silent = f"{ROOT}/work/video_silent.mp4"
    run(["ffmpeg","-y","-v","error"] + inputs +
        ["-filter_complex", ";".join(fc), "-map", "[vout]",
         "-r",str(FPS),"-c:v","libx264","-profile:v","high","-pix_fmt","yuv420p",
         "-preset","medium","-crf","18", silent])
    return silent, starts, acc

silent, starts, total = build_silent(OUTRO_D)
print(f"SILENT TOTAL: {dur(silent):.2f}s")
labels_order = ["intro"] + [s[0] for s in segs] + ["claude1", "claude2", "claude3", "outro"]
S = dict(zip(labels_order, starts))
OUTRO_START = S["outro"]

GAP = 0.22
anchor = {
    "N0":  0.35,                  # intro hook
    "N1":  S["A"] + 0.20,         # les 4 compteurs
    "N2":  S["B"] + 0.10,         # clic sur le filtre de statut
    "N3":  S["D"] + 0.20,         # prêt à produire
    "N4":  S["E"] + 0.20,         # réalisée -> Voir la traçabilité
    "N5":  S["F"] + 0.20,         # recherche par nom
    "N6":  S["G"] + 0.10,         # clic filtre de dates + panneau
    "N7":  S["I"] + 0.10,         # clic Appliquer -> résultat
    "N8":  S["K"] + 0.20,         # bénéfice (contrôle sanitaire)
    "N9":  S["claude1"] + 0.20,   # explique le prompt (reveal + copié)
    "N10": S["claude3"] + 0.20,   # collé dans Claude -> résultat
    "N11": OUTRO_START + 0.35,    # CTA
}
keys = [f"N{i}" for i in range(12)]
off, prev_end = {}, -GAP
for k in keys:
    o = max(anchor[k], prev_end + GAP); off[k] = o
    prev_end = o + dur(f"{ROOT}/vo/{k}.mp3")
print("offsets:", {k: round(v, 2) for k, v in off.items()}, "voice_end:", round(prev_end, 2))
print("anchors:", {k: round(v, 2) for k, v in anchor.items()})
drift = {k: round(off[k] - anchor[k], 2) for k in keys if off[k] - anchor[k] > 0.05}
print("drift vs anchors:", drift if drift else "none -- all lines on their anchors")

needed = prev_end - OUTRO_START + 0.80
if needed > OUTRO_D:
    print(f"extending outro {OUTRO_D:.2f} -> {needed:.2f}")
    silent, starts, total = build_silent(needed)
    print(f"SILENT TOTAL (extended): {dur(silent):.2f}s")

total = dur(silent)
inputs, filters, labels = [], [], []
for i, k in enumerate(keys):
    inputs += ["-i", f"{ROOT}/vo/{k}.mp3"]; ms = int(off[k] * 1000)
    filters.append(f"[{i+1}:a]loudnorm=I=-16:TP=-1.5:LRA=11,adelay={ms}|{ms},apad[a{i}]")
    labels.append(f"[a{i}]")
filters.append("".join(labels) + f"amix=inputs={len(keys)}:normalize=0:duration=first[mix]")
filters.append(f"[mix]atrim=0:{total:.3f},alimiter=limit=0.6:level=disabled,"
               f"aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,"
               f"asetpts=N/SR/TB[voa]")
FINAL = f"{ROOT}/out/foodeatup-tracabilite-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
