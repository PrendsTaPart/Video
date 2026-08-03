#!/usr/bin/env python3
# FoodEatUp "Détails et impression de la liste des ingrédients de production".
#
# Rush: Mes productions -> Voir les ingrédients -> tableau (qté nécessaire /
# stock / statut / traçabilité) -> menu Action -> fiche traçabilité Saumon frais
# (photo DLC, quantité, DLC, n° de lot, remarques) -> PDF -> page "Liste
# d'ingrédients" -> Exporter PDF -> visionneuse PDF.
#
# Same engine as the rest of the series: setpts for speed (never zoompan on
# real footage -- freezes the image), fixed crop+scale zoom-punch on clicks,
# xfade on every cut, yuv420p, 48 kHz stereo AAC, +faststart.
#
# Two rush-specific points:
#  - The traçabilité form is *filled* then cancelled in the rush (the row stays
#    "À compléter"). The edit stops at the filled form: no VO line claims the
#    fiche was validated.
#  - A McAfee WebAdvisor browser toast pops in from ~48 s (bottom right, source
#    y >= 640). The "Exporter PDF" punch therefore uses a tighter zoom (1.45)
#    so its crop window stops above the toast; the following segment starts
#    once the PDF viewer covers the page.
import subprocess, os, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (
    render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png,
)

ROOT = "/home/user/Video/videos/foodeatup-production-ingredients-tuto"
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

def crop_for(btn, zoom=1.20):
    bx, by = btn
    cw, ch = int(W/zoom), int(H/zoom); cw -= cw % 2; ch -= ch % 2
    x = int(clamp(bx - cw/2, 0, W - cw)); y = int(clamp(by - ch/2, 0, H - ch))
    return f"crop={cw}:{ch}:{x}:{y},scale={W}:{H}:flags=bicubic", (cw, ch, x, y)

def punch_highlight(btn, btn_wh, crop_box):
    """Static ring around the clicked button. Deliberately NOT animated:
    `drawbox` in this ffmpeg (6.1) evaluates x/y/w/h once at config time, so a
    `sin(t)` pulse would silently freeze at its t=0 value anyway. A punch lasts
    0.9 s -- a steady ring reads better than a pulse nobody can perceive."""
    cw, ch, cx, cy = crop_box
    sx, sy = W / cw, H / ch
    bw, bh = btn_wh[0] * sx, btn_wh[1] * sy
    ox, oy = (btn[0] - cx) * sx, (btn[1] - cy) * sy
    p = 14
    return (f"drawbox=x={ox-bw/2-p:.0f}:y={oy-bh/2-p:.0f}"
            f":w={bw+2*p:.0f}:h={bh+2*p:.0f}:color={ORANGE}@0.95:t=5")

BANNER_H = 62
def render_banner_png(text, path):
    """Step banner rendered once with PIL, then slid in with `overlay`.

    It used to be three chained `drawbox`/`drawtext` filters with a time-based
    x expression. `drawtext` does re-evaluate x per frame, but `drawbox` does
    NOT (ffmpeg 6.1 evaluates it once at config time, i.e. at t=0, where the
    slide-in expression is still off-screen at x=-640). Result: the orange rule
    and the blue plate were never drawn at all and the caption showed up as
    bare white text over the page -- illegible on light UI. `overlay` honours
    eval=frame, so the whole banner is now one RGBA image that really slides.
    Text must still avoid apostrophes/% only where drawtext is used elsewhere;
    here PIL draws the text, so it is not a constraint anymore -- kept anyway
    for consistency with the rest of the series."""
    f = ImageFont.truetype(FONT, 31)
    probe = ImageDraw.Draw(Image.new("RGBA", (8, 8)))
    w = max(570, int(34 + probe.textlength(text, font=f) + 28))
    im = Image.new("RGBA", (w, BANNER_H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, 9, BANNER_H - 1], fill=(247, 148, 29, 250))    # rule (orange)
    d.rectangle([10, 0, w - 1, BANNER_H - 1], fill=(27, 109, 243, 230))  # plate (blue)
    d.text((34, BANNER_H // 2), text, font=f, fill=(255, 255, 255, 255), anchor="lm")
    im.save(path)
    return w

def banner_x_expr(bw, seg_dur):
    tin, sl = 0.15, 0.32
    tout = max(tin + sl + 0.3, seg_dur - 0.55)
    a = f"min(1\\,max(0\\,(t-{tin})/{sl}))"
    b = f"min(1\\,max(0\\,(t-{tout})/{sl}))"
    return f"-{bw}+{bw + 60}*({a})-{bw + 60}*({b})"

# Button centres + sizes measured on the real 1920x828 frames.
BTN_ING    = (301, 449);  SZ_ING    = (355, 40)   # "Voir les ingrédients" (1re carte)
BTN_PDF    = (1265, 139); SZ_PDF    = (92, 40)    # "PDF" (en-tête du modal)
BTN_EXPORT = (1800, 72);  SZ_EXPORT = (270, 62)   # "Exporter PDF" (page imprimable)

# (name, src_start, src_end, target_out_duration, button, btn_size, zoom, caption)
segs = [
    ("A",  0.60,  6.30, 6.30, None,       None,       None, "1 · Vos productions planifiees"),
    ("B",  6.60,  7.05, 0.90, BTN_ING,    SZ_ING,     1.20, None),
    ("C",  7.20,  8.70, 4.00, None,       None,       None, "2 · Quantite, stock et statut"),
    ("D",  8.70, 10.60, 3.60, None,       None,       None, "3 · Completez la tracabilite"),
    ("E", 10.60, 17.50, 5.15, None,       None,       None, "4 · Photo de la DLC"),
    ("F", 17.50, 32.50, 4.80, None,       None,       None, "5 · Quantite, DLC et lot"),
    ("G", 37.20, 43.20, 3.28, None,       None,       None, "6 · Imprimez votre liste"),
    ("H", 43.20, 43.60, 0.90, BTN_PDF,    SZ_PDF,     1.20, None),
    ("I", 44.70, 48.00, 3.30, None,       None,       None, "7 · La liste generee"),
    ("J", 50.30, 50.70, 0.90, BTN_EXPORT, SZ_EXPORT,  1.45, None),
    ("K", 51.40, 56.10, 3.20, None,       None,       None, None),
]
INTRO_D, OUTRO_D = 3.20, 6.20

def encode_seg(name, s, e, target, btn, btn_sz, zoom, caption):
    out = f"{SEG}/{name}.mp4"
    factor = (e - s) / target
    vf = f"setpts=(PTS-STARTPTS)/{factor:.6f}"
    if btn:
        crop_vf, box = crop_for(btn, zoom)
        vf += f",{crop_vf},{punch_highlight(btn, btn_sz, box)}"
    else:
        vf += f",scale={W}:{H}"
    cmd = ["ffmpeg","-y","-v","error","-ss",str(s),"-to",str(e),"-i",SRC,"-an"]
    if caption:
        png = f"{SEG}/{name}_banner.png"
        bw = render_banner_png(caption, png)
        # shortest=1 is mandatory: the banner is an infinite -loop 1 still, so
        # without it overlay keeps emitting frames forever once the segment ends.
        fc = (f"[0:v]{vf}[base];"
              f"[base][1:v]overlay=x='{banner_x_expr(bw, target)}':y={H - 108}"
              f":eval=frame:shortest=1,fps={FPS},format=yuv420p[v]")
        cmd += ["-loop","1","-i",png,"-filter_complex",fc,"-map","[v]"]
    else:
        cmd += ["-vf", f"{vf},fps={FPS},format=yuv420p"]
    cmd += ["-r",str(FPS),"-c:v","libx264","-preset","medium","-crf","18",out]
    run(cmd)
    return out

# ---------------------------------------------------------------------------
# "Use it with Claude" sequence -- shared 3-stage chatbot animation.
# Matching tool: get_production_ingredients(establishment_id, production_id),
# which is exactly what the video shows (the ingredient list of a production
# with its required quantity and its stock status).
# ---------------------------------------------------------------------------
# Accents are fine here: the 3 stages are drawn with PIL, not with drawtext.
# (Only banner()/drawtext texts ever had escaping constraints.)
CLAUDE_PROMPT = ("Donne-moi la liste des ingrédients de ma production [nom de la "
                 "production] du [date], avec les quantités nécessaires et le stock "
                 "disponible, pour mon établissement FoodEatUp (ID [ID établissement]).")
CLAUDE_RESPONSE = "Bien sûr ! Voici la liste des ingrédients de votre production…"

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

CLAUDE_STAGE_D = [3.00, 2.30, 5.30]

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
    for name, s, e, target, btn, sz, zoom, cap in segs:
        parts.append(encode_seg(name, s, e, target, btn, sz, zoom, cap))
    parts += [f"{SEG}/claude1.mp4", f"{SEG}/claude2.mp4", f"{SEG}/claude3.mp4",
              f"{SEG}/outro.mp4"]

    trans = ["fade",       # intro -> A
             "fade",       # A -> B   (continu : clic sur le bouton visible)
             "fade",       # B -> C   (le modal s'ouvre)
             "fade",       # C -> D   (continu : menu Action)
             "fade",       # D -> E   (continu : fiche traçabilité)
             "fade",       # E -> F   (continu : champs de la fiche)
             "slideleft",  # F -> G   (coupe : retour au tableau + en-tête)
             "fade",       # G -> H   (continu : clic PDF)
             "fade",       # H -> I   (la page imprimable s'ouvre)
             "slideleft",  # I -> J   (coupe : clic Exporter PDF)
             "fade",       # J -> K   (la visionneuse PDF s'ouvre)
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
    "N0": 0.30,                  # accroche sur la carte intro (déborde sur A)
    "N1": S["A"] + 0.20,         # la liste des productions -> Voir les ingrédients
    "N2": S["C"] + 0.20,         # tableau : qté nécessaire / stock / statut (C + D)
    "N3": S["E"] + 0.20,         # photo de la DLC
    "N4": S["F"] + 0.20,         # quantité, DLC, n° de lot, remarques
    "N5": S["G"] + 0.20,         # clic PDF
    "N6": S["I"] + 0.20,         # exporter / imprimer (I + J + K)
    "N7": S["claude1"] + 0.20,   # explique le prompt (reveal + copié)
    "N8": S["claude3"] + 0.20,   # collé dans Claude -> résultat
    "N9": OUTRO_START + 0.35,    # CTA
}
keys = [f"N{i}" for i in range(10)]
off, prev_end = {}, -GAP
for k in keys:
    o = max(anchor[k], prev_end + GAP); off[k] = o
    prev_end = o + dur(f"{ROOT}/vo/{k}.mp3")
print("offsets:", {k: round(v, 2) for k, v in off.items()}, "voice_end:", round(prev_end, 2))
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
FINAL = f"{ROOT}/out/foodeatup-production-ingredients-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
