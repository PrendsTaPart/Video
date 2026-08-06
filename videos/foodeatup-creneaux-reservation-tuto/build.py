#!/usr/bin/env python3
# FoodEatUp "Ouvrir ses créneaux de réservation" tutorial.
#
# Rush (89s, 1920x828): on the Réservations page, a "Nouvelle réservation" is
# filled for samedi 15/08/2026 18:58 and rejected -- "Restaurant fermé à cette
# heure (horaires Storefront)." (15/08/2026 is indeed a Saturday). The fix
# lives in Configuration boutique > Ma Vitrine > Infos & Publication :
# "Horaires d'ouverture" lists each day with a checkbox + time range: Samedi
# is unchecked ("Fermé"). Checking it (11:30 AM - 10:00 PM) and clicking
# Enregistrer ("Vitrine enregistrée" toast) opens the slot. Back on
# Réservations, the same client/date/time now goes through: a table is
# assigned (T5, then T7 for a second booking) and the list ends at
# Total 13 with two "En attente" Saturday reservations.
#
# Same engine as the rest of the series: setpts for speed (never zoompan on
# real footage -- freezes the image), fixed crop+scale zoom-punch on clicks,
# PIL-rendered sliding banner (drawbox doesn't animate x on this ffmpeg
# build), xfade on every cut, yuv420p, 48 kHz stereo AAC, +faststart.
import subprocess, os, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (
    render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png,
)

ROOT = "/home/user/Video/videos/foodeatup-creneaux-reservation-tuto"
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
    """Static ring around the clicked button (drawbox x/y/w/h is evaluated
    once at t=0 on this ffmpeg build, so an animated pulse would freeze
    anyway -- a steady ring reads fine for a punch this short)."""
    cw, ch, cx, cy = crop_box
    sx, sy = W / cw, H / ch
    bw, bh = btn_wh[0] * sx, btn_wh[1] * sy
    ox, oy = (btn[0] - cx) * sx, (btn[1] - cy) * sy
    p = 14
    return (f"drawbox=x={ox-bw/2-p:.0f}:y={oy-bh/2-p:.0f}"
            f":w={bw+2*p:.0f}:h={bh+2*p:.0f}:color={ORANGE}@0.95:t=5")

BANNER_H = 62
def render_banner_png(text, path):
    """Step banner rendered once with PIL, then slid in with `overlay`
    (eval=frame) -- drawbox does NOT re-evaluate x per frame on ffmpeg 6.1,
    so the old three-drawbox/drawtext banner never actually drew its plate."""
    f = ImageFont.truetype(FONT, 31)
    probe = ImageDraw.Draw(Image.new("RGBA", (8, 8)))
    w = max(570, int(34 + probe.textlength(text, font=f) + 28))
    im = Image.new("RGBA", (w, BANNER_H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, 9, BANNER_H - 1], fill=(247, 148, 29, 250))
    d.rectangle([10, 0, w - 1, BANNER_H - 1], fill=(27, 109, 243, 230))
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
BTN_NOUVELLE = (1650, 310); SZ_NOUVELLE = (280, 55)   # "+ Nouvelle réservation"
ERR_BOX      = (948, 497);  SZ_ERR      = (655, 45)   # "Restaurant fermé à cette heure..."
NAV_VITRINE  = (150, 545);  SZ_VITRINE  = (220, 34)   # "Ma Vitrine" (menu déroulant)
BTN_SAMEDI   = (190, 290);  SZ_SAMEDI   = (34, 34)    # case à cocher "Samedi"
BTN_ENREG    = (1100, 699); SZ_ENREG    = (290, 62)   # "Enregistrer" (horaires)

# (name, src_start, src_end, target_out_duration, button, btn_size, zoom, caption)
segs = [
    ("A", 0.20,  0.80,  2.60, None,        None,       None, "1 - Vos reservations"),
    ("B", 0.80,  1.10,  0.90, BTN_NOUVELLE, SZ_NOUVELLE, 1.20, None),
    ("C", 3.00,  9.00,  4.60, None,        None,       None, "2 - Coordonnees du client"),
    ("D", 20.00, 29.40, 5.60, None,        None,       None, "3 - Creneau hors horaires"),
    ("E", 29.20, 29.50, 1.00, ERR_BOX,     SZ_ERR,     1.35, None),
    ("F", 36.50, 39.20, 3.40, None,        None,       None, "4 - Configuration boutique > Ma Vitrine"),
    ("G", 39.20, 39.50, 0.90, NAV_VITRINE, SZ_VITRINE, 1.30, None),
    ("H", 44.80, 47.90, 3.60, None,        None,       None, "5 - Horaires d'ouverture"),
    ("I", 47.90, 48.20, 0.90, BTN_SAMEDI,  SZ_SAMEDI,  1.70, None),
    ("J", 49.80, 50.10, 0.90, BTN_ENREG,   SZ_ENREG,   1.25, None),
    ("K", 53.80, 55.30, 2.60, None,        None,       None, "6 - Enregistrez vos horaires"),
    ("L", 59.50, 80.00, 5.60, None,        None,       None, "7 - Recreez la reservation"),
    ("M", 85.00, 89.00, 3.80, None,        None,       None, "8 - Vos creneaux sont ouverts"),
]
INTRO_D, OUTRO_D = 3.00, 6.20

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
# Matching tool: reservation_availability(establishment_id, date, time,
# party_size) checks exactly what this video is about (open + tables free
# for a given slot) before a reservation is even attempted.
# ---------------------------------------------------------------------------
CLAUDE_PROMPT = ("Vérifie la disponibilité d'un créneau le [date] à [heure] pour "
                  "[nombre de couverts] couverts, pour mon établissement FoodEatUp "
                  "(ID [ID établissement]).")
CLAUDE_RESPONSE = "Bien sûr ! Je vérifie la disponibilité de ce créneau…"

def card(img, out, secs, zoom_in=True, fade=True):
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

CLAUDE_STAGE_D = [3.00, 2.30, 6.00]

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
             "fade",       # A -> B     (continu : clic sur le bouton)
             "fade",       # B -> C     (le modal s'ouvre)
             "fade",       # C -> D     (continu : creneau saisi)
             "fade",       # D -> E     (l'erreur apparait)
             "slideleft",  # E -> F     (coupe : ouverture du menu)
             "fade",       # F -> G     (continu : clic Ma Vitrine)
             "fade",       # G -> H     (la page horaires s'ouvre)
             "fade",       # H -> I     (continu : coche Samedi)
             "fade",       # I -> J     (continu : clic Enregistrer)
             "fade",       # J -> K     (confirmation)
             "slideleft",  # K -> L     (coupe : retour Reservations)
             "fade",       # L -> M     (la liste se met a jour)
             "slideleft",  # M -> claude1
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
    "N0": 0.30,                  # accroche sur la carte intro
    "N1": S["A"] + 0.20,         # coordonnees client (A+B+C)
    "N2": S["D"] + 0.20,         # creneau refuse (D+E)
    "N3": S["F"] + 0.20,         # nav configuration boutique -> ma vitrine (F+G)
    "N4": S["H"] + 0.20,         # cochez le jour + enregistrez (H+I+J+K)
    "N5": S["L"] + 0.20,         # recreez la reservation (L+M)
    "N6": S["claude1"] + 0.20,   # explique le prompt (reveal + copie)
    "N7": S["claude3"] + 0.20,   # colle dans Claude -> resultat
    "N8": OUTRO_START + 0.35,    # CTA
}
keys = ["N0","N1","N2","N3","N4","N5","N6","N7","N8"]
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
FINAL = f"{ROOT}/out/foodeatup-creneaux-reservation-tuto-v1.mp4"
os.makedirs(f"{ROOT}/out", exist_ok=True)
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
