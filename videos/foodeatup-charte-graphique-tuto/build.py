#!/usr/bin/env python3
# FoodEatUp "Synchroniser la Charte graphique Iris" tutorial.
# Module marketing-fidelite, item #22 du catalogue 157 tutoriels.
#
# No avatar, and no "use it with Claude" 3-stage sequence at the end --
# aucun outil mcp__Foodeatup__* n'expose le pairage marque/Iris, donc pas
# de prompt Claude fabrique (regle du repo : si aucun outil ne correspond,
# ne pas inventer de prompt).
#
# Rush (49.26s): page Intégrations FoodEatUp, carte "Iris — Marque & Charte".
# Bouton "Appairer la marque" clique vers t=33-34s -> "Synchronisation..."
# (loading, t=37-40s) -> resultat "Braindcode" (couleurs, police, comptes
# sociaux, 728 assets) revele et scrolle jusqu'a t=49s.
#
# Meme moteur que le reste de la serie : setpts pour la vitesse (jamais
# zoompan sur du vrai footage), crop+scale fixe pour le zoom-punch sur le
# clic, un crop "colonne de droite" fixe pour rester cadre sur la carte Iris
# et masquer la colonne RapidoCMS/Reseaux sociaux (hors sujet ici), xfade
# sur chaque coupe force en yuv420p, AAC stereo 48kHz, +faststart.
import subprocess, os, sys

ROOT = "/home/user/Video/videos/foodeatup-charte-graphique-tuto"
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
    cw, ch, cx, cy = crop_box
    sx, sy = W / cw, H / ch
    bw, bh = btn_wh[0] * sx, btn_wh[1] * sy
    ox, oy = (btn[0] - cx) * sx, (btn[1] - cy) * sy
    p = 14
    br = "6*sin(2*PI*t*2.2)"
    return (f"drawbox=x='{ox-bw/2-p}-{br}':y='{oy-bh/2-p}-{br}'"
            f":w='{bw+2*p}+2*({br})':h='{bh+2*p}+2*({br})'"
            f":color={ORANGE}@0.95:t=5")

# Colonne de droite (carte "Iris — Marque & Charte") isolee de la colonne
# RapidoCMS/Reseaux sociaux, qui n'est pas le sujet de ce tutoriel.
RIGHT_CROP = f"crop=956:828:964:0,scale={W}:{H}:flags=bicubic"

def banner(text, seg_dur):
    if not text: return None
    # drawbox n'evalue x qu'une fois dans cet ffmpeg (6.1.1) -- voir
    # FOODEATUP-TUTORIELS-WORKFLOW.md. Un seul clamp de glissement (slide-in),
    # pas de slide-out anime.
    tin, sl = 0.15, 0.32
    a = f"min(1\\,max(0\\,(t-{tin})/{sl}))"
    x = f"-640+700*({a})"
    y = H - 108
    return (f"drawbox=x='{x}':y={y}:w=10:h=62:color={ORANGE}@0.98:t=fill,"
            f"drawbox=x='({x})+10':y={y}:w=560:h=62:color={BLUE}@0.90:t=fill,"
            f"drawtext=fontfile={FONT}:text='{text}':fontsize=31:fontcolor=white"
            f":x='({x})+34':y={y+16}")

# Coordonnee mesuree en extrayant des frames plein-format autour du clic
# (voir scratchpad -- bbox blue 994,309 -> 1273,370 en 1920x828).
BTN_PAIR = (1133, 339); SZ_PAIR = (279, 61)  # "Appairer la marque"

# (name, src_start, src_end, target_out_duration, button, btn_size, caption, use_right_crop)
segs = [
    ("A", 0.00,  2.50, 4.30, None,     None,    "Intégrations > Iris - Marque & Charte", True),
    ("B", 32.00, 33.50, 3.20, BTN_PAIR, SZ_PAIR, None,                                    False),
    ("C", 37.00, 39.00, 1.30, None,     None,    "Synchronisation en cours",               True),
    ("D", 41.00, 42.50, 5.26, None,     None,    "Couleurs, police & logo",                True),
    ("E", 44.00, 45.50, 6.60, None,     None,    "Comptes sociaux connectés",              True),
    ("F", 46.00, 49.20, 6.46, None,     None,    "728 assets de marque",                   True),
]
INTRO_D, OUTRO_D = 5.33, 6.20

def encode_seg(name, s, e, target, btn, btn_sz, caption, right_crop):
    out = f"{SEG}/{name}.mp4"
    factor = (e - s) / target
    vf = f"setpts=(PTS-STARTPTS)/{factor:.6f}"
    if btn:
        crop_vf, box = crop_for(btn)
        vf += f",{crop_vf},{punch_highlight(btn, btn_sz, box)}"
    elif right_crop:
        vf += f",{RIGHT_CROP}"
    else:
        vf += f",scale={W}:{H}"
    b = banner(caption, target)
    if b: vf += f",{b}"
    vf += f",fps={FPS},format=yuv420p"
    run(["ffmpeg","-y","-v","error","-ss",str(s),"-to",str(e),"-i",SRC,"-an",
         "-vf",vf,"-r",str(FPS),"-c:v","libx264","-preset","medium","-crf","18",out])
    return out

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

def build_silent(outro_d):
    card(f"{ROOT}/assets/intro.jpg", f"{SEG}/intro.mp4", INTRO_D, zoom_in=True)
    card(f"{ROOT}/assets/outro.jpg", f"{SEG}/outro.mp4", outro_d, zoom_in=False)

    parts = [f"{SEG}/intro.mp4"]
    for name, s, e, target, btn, sz, cap, rc in segs:
        parts.append(encode_seg(name, s, e, target, btn, sz, cap, rc))
    parts.append(f"{SEG}/outro.mp4")

    trans = ["fade",       # intro -> A
             "slideleft",  # A -> B (cut to the button, zoom-punch)
             "fade",       # B -> C (continuous: click -> loading)
             "slideleft",  # C -> D (loading -> result reveal)
             "fade",       # D -> E (same card, comptes sociaux)
             "fade",       # E -> F (same card, asset count)
             "fade"]       # F -> outro
    durs = [dur(p) for p in parts]
    starts, acc = [], 0.0
    for i, d in enumerate(durs):
        starts.append(acc); acc += d - (XF if i < len(durs) - 1 else 0)
    total = acc

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
    return silent, starts, total

silent, starts, total = build_silent(OUTRO_D)
print(f"SILENT TOTAL: {dur(silent):.2f}s")
labels_order = ["intro"] + [s[0] for s in segs] + ["outro"]
S = dict(zip(labels_order, starts))
OUTRO_START = S["outro"]

GAP = 0.22
anchor = {
    "N0": 0.20,
    "N1": S["A"] + 0.15,
    "N2": S["B"] + 0.10,
    "N3": S["D"] + 0.15,
    "N4": S["E"] + 0.15,
    "N5": S["F"] + 0.15,
    "N6": OUTRO_START + 0.30,
}
keys = ["N0","N1","N2","N3","N4","N5","N6"]
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
    S = dict(zip(labels_order, starts))
    OUTRO_START = S["outro"]

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
FINAL = f"{ROOT}/out/foodeatup-charte-graphique-tuto-v1.mp4"
os.makedirs(f"{ROOT}/out", exist_ok=True)
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
