#!/usr/bin/env python3
# FoodEatUp "Retrouver mes Plats sondés (historique)" tutorial (module HACCP, item 06).
# Same engine as the rest of the series: no avatar clip, full ElevenLabs VO,
# speed = setpts (never zoompan on real footage), xfade on every cut, forced
# back to yuv420p at the end of the chain. 48kHz stereo AAC, +faststart.
#
# Two linked actions in one rush (same principle as foodeatup-mouvement-stock-tuto):
# sonder ses plats (saisir/enregistrer les températures) puis retrouver l'historique
# de ces relevés filtré sur "Plats". No Claude-prompt sequence here: verified that
# mcp__FoodEatUp__add_temperature/list_haccp_temperatures are both scoped to
# equipment_id only (no plat/recette parameter) -- see SCRIPT.md.
import subprocess, os

ROOT = "/home/user/Video/videos/foodeatup-plats-sondes-tuto"
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

# Step banner -- two drawtext layers (plate + filet), NOT drawbox+drawtext.
# ffmpeg 6.1.1's drawbox does not evaluate `t` in x/y/w/h -- an animated-x
# drawbox is silently dropped. drawtext's own `box` is used as the plate
# instead. See videos/foodeatup-mouvement-stock-tuto/build.py for the full
# writeup of this bug (also documented in FOODEATUP-TUTORIELS-WORKFLOW.md).
BANNER_Y = H - 108

def banner(text, seg_dur):
    if not text: return None
    tin, sl = 0.15, 0.32
    tout = max(tin + sl + 0.3, seg_dur - 0.55)
    a = f"min(1\\,max(0\\,(t-{tin})/{sl}))"
    b = f"min(1\\,max(0\\,(t-{tout})/{sl}))"
    x = f"-640+700*({a})-700*({b})"
    label = f" {text} "
    return (f"drawtext=fontfile={FONT}:text='{label}':fontsize=31:fontcolor=white"
            f":box=1:boxcolor={ORANGE}@0.98:boxborderw=16:x='({x})-10':y={BANNER_Y},"
            f"drawtext=fontfile={FONT}:text='{label}':fontsize=31:fontcolor=white"
            f":box=1:boxcolor={BLUE}@0.92:boxborderw=16:x='({x})':y={BANNER_Y}")

# Coordinates measured on native 1920x828 frames (work/hi/, colour-thresholded
# where the button is a solid fill -- see analysis in SCRIPT.md) -- not eyeballed.
BTN_PLATS1    = (329, 147);  SZ_PLATS1    = (112, 64)   # onglet "Plats" (Production > Températures)
BTN_SAVE      = (1555, 742); SZ_SAVE      = (590, 80)   # "Enregistrer les relevés de température"
BTN_OUI       = (872, 608);  SZ_OUI       = (243, 53)   # "Oui, enregistrer !" (modale)
BTN_OK        = (960, 595);  SZ_OK        = (90, 55)    # "OK" (modale Enregistré !)
BTN_HIST_NAV  = (1390, 139); SZ_HIST_NAV  = (145, 63)   # "Historique" (nav du haut)
BTN_CARD_TEMP = (342, 375);  SZ_CARD_TEMP = (378, 290)  # carte "Températures" (historique haccp)
BTN_PLATS2    = (333, 310);  SZ_PLATS2    = (95, 60)    # onglet "Plats" (Historique > Températures)

# (name, src_start, src_end, target_out_duration, button, btn_size, caption)
# Targets sized on the sequential VO timeline (GAP 0.22, laid out below) so each
# line starts on its anchor segment and ends before the next unrelated visual.
segs = [
    ("A", 0.00,  2.60,  3.90, None,          None,          "1 . Sondez vos plats"),
    ("B", 2.60,  2.90,  1.00, BTN_PLATS1,    SZ_PLATS1,     None),
    ("C", 2.90,  11.00, 6.00, None,          None,          None),
    ("D", 11.00, 11.30, 1.00, BTN_SAVE,      SZ_SAVE,       None),
    ("E", 11.30, 11.90, 1.80, None,          None,          None),
    ("F", 11.90, 12.20, 1.00, BTN_OUI,       SZ_OUI,        None),
    ("G", 12.20, 13.60, 2.20, None,          None,          None),
    ("H", 13.60, 13.90, 1.00, BTN_OK,        SZ_OK,         None),
    ("I", 13.90, 16.30, 5.00, None,          None,          "2 . Non conformes signales"),
    ("J", 16.30, 16.60, 1.00, BTN_HIST_NAV,  SZ_HIST_NAV,   None),
    ("K", 16.60, 17.00, 2.40, None,          None,          "3 . Historique HACCP"),
    ("L", 17.00, 17.30, 1.00, BTN_CARD_TEMP, SZ_CARD_TEMP,  None),
    ("M", 17.30, 19.30, 4.00, None,          None,          None),
    ("N", 19.30, 19.65, 1.00, BTN_PLATS2,    SZ_PLATS2,     None),
    ("O", 19.65, 25.80, 13.50, None,         None,          "4 . Historique de vos plats sondes"),
]
INTRO_D, OUTRO_D = 6.30, 6.20

def encode_seg(name, s, e, target, btn, btn_sz, caption):
    out = f"{SEG}/{name}.mp4"
    factor = (e - s) / target
    vf = f"setpts=(PTS-STARTPTS)/{factor:.6f}"
    if btn:
        crop_vf, box = crop_for(btn)
        vf += f",{crop_vf},{punch_highlight(btn, btn_sz, box)}"
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
    for name, s, e, target, btn, sz, cap in segs:
        parts.append(encode_seg(name, s, e, target, btn, sz, cap))
    parts.append(f"{SEG}/outro.mp4")

    trans = ["fade",       # intro -> A
             "fade",       # A -> B (continuous: click onglet Plats)
             "slideleft",  # B -> C (cut into the Plats grid)
             "fade",       # C -> D (continuous: click Enregistrer)
             "fade",       # D -> E (continuous: modale de confirmation)
             "fade",       # E -> F (continuous: click Oui, enregistrer)
             "fade",       # F -> G (continuous: modale Enregistre !)
             "fade",       # G -> H (continuous: click OK)
             "fade",       # H -> I (continuous: retour a la liste)
             "fade",       # I -> J (continuous: click nav Historique)
             "slideleft",  # J -> K (cut: page historique haccp)
             "fade",       # K -> L (continuous: click carte Temperatures)
             "slideleft",  # L -> M (cut: dashboard Historique > Temperatures)
             "fade",       # M -> N (continuous: click onglet Plats)
             "fade",       # N -> O (continuous: liste bascule sur Plats)
             "fade"]       # O -> outro
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
    "N0": 0.30,                   # intro hook
    "N1": S["A"] + 0.25,          # ouvrez Temperatures > onglet Plats
    "N2": S["C"] + 0.20,          # ajustez la temperature de chaque plat
    "N3": S["D"] + 0.15,          # Enregistrer -> confirmation -> Oui, enregistrer
    "N4": S["G"] + 0.20,          # Enregistre ! -> OK -> non-conformes signales
    "N5": S["J"] + 0.15,          # nav Historique -> page historique haccp
    "N6": S["L"] + 0.15,          # carte Temperatures -> onglet Plats
    "N7": S["O"] + 0.20,          # fiche complete de chaque plat sonde
    "N8": S["O"] + 4.20,          # benefice (meme ecran, fin du scroll)
    "N9": OUTRO_START + 0.35,     # CTA
}
keys = [f"N{i}" for i in range(10)]
off, prev_end = {}, -GAP
for k in keys:
    o = max(anchor[k], prev_end + GAP); off[k] = o
    prev_end = o + dur(f"{ROOT}/vo/{k}.mp3")
print("offsets:", {k: round(v, 2) for k, v in off.items()}, "voice_end:", round(prev_end, 2))
drift = {k: round(off[k] - anchor[k], 2) for k in keys if off[k] - anchor[k] > 0.05}
print("drift vs anchors:", drift if drift else "none -- all lines on their anchors")
print("stage starts:", {k: round(v, 2) for k, v in S.items()})

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
FINAL = f"{ROOT}/out/foodeatup-plats-sondes-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
