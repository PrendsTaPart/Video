#!/usr/bin/env python3
# FoodEatUp "Reecouter ses appels et reservations" tutorial (module Agent IA
# Caroline). First tutorial produced for this module. Same engine as the rest
# of the series (see videos/FOODEATUP-TUTORIELS-WORKFLOW.md): setpts speed
# change (never zoompan on real footage), zoom-punch crop on clicks, xfade on
# every cut, step banners drawn with two drawtext(box=1) layers (NOT drawbox --
# drawbox does not evaluate a t-dependent x in this ffmpeg 6.1.1, see
# foodeatup-mouvement-stock-tuto/build.py). 48kHz stereo AAC, +faststart.
#
# Rush (43.0s, 1920x828, silent): "Appels" tab (voice agent Caroline) ->
# counters (Total appels 47, Aujourd'hui 0, Commandes generees 2, Duree
# moyenne 0:53) -> click "Voir" on the first row -> detail modal (Resume +
# full Transcription, scrolled) -> close -> back to the list -> click the
# Statut filter -> cycle through Manque/Transfere/En cours (empty results,
# all demo calls are "Reussi") -> back to "Tous les statuts", full list.
#
# No mcp__FoodEatUp__* tool matches "listen back to a call" (no list_calls/
# get_call tool -- only reservation tools exist, which is a different
# action). No claudePrompt / Claude sequence for this video, per the
# documented rule in FOODEATUP-TUTORIELS-WORKFLOW.md paragraph 3.
import subprocess, os

ROOT = "/home/user/Video/videos/foodeatup-appels-reservations-tuto"
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

# Step banner -- two drawtext(box=1) layers sharing one animated x, NOT
# drawbox+drawtext. drawbox does not evaluate a t-dependent x on this ffmpeg
# (6.1.1): it silently draws nothing, leaving only bare white drawtext text on
# a light UI screenshot. drawtext's own `box` plate does not have that bug
# (it re-evaluates every frame). See foodeatup-mouvement-stock-tuto/build.py.
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

# Coordinates measured on extracted frames (native 1920x828), color-thresholded
# for the Voir button and the filter box, cropped+zoomed by eye for the close
# icon. No apostrophe in any caption below (bug hit on foodeatup-ingredients-tuto
# -- see FOODEATUP-TUTORIELS-WORKFLOW.md).
BTN_VOIR   = (1639, 303); SZ_VOIR   = (58, 35)    # pilule "Voir", 1re ligne
BTN_CLOSE  = (1278, 95);  SZ_CLOSE  = (30, 30)     # "x" de fermeture de la modale
BTN_FILTER = (1238, 147); SZ_FILTER = (197, 49)    # selecteur "Statut"

# (name, src_start, src_end, target_out_duration, button, btn_size, caption)
segs = [
    ("A", 2.00,  6.60,  5.80, None,       None,       "1 - Suivez tous vos appels"),
    ("B", 6.60,  6.95,  0.75, BTN_VOIR,   SZ_VOIR,    None),
    ("C", 7.00,  17.20, 7.20, None,       None,       "2 - Resume et transcription"),
    ("D", 17.20, 17.55, 0.75, BTN_CLOSE,  SZ_CLOSE,   None),
    ("E", 19.00, 22.30, 1.80, None,       None,       None),
    ("F", 22.30, 22.65, 0.75, BTN_FILTER, SZ_FILTER,  None),
    ("G", 24.00, 33.00, 5.20, None,       None,       "3 - Filtrez par statut"),
    ("H", 34.00, 42.50, 4.80, None,       None,       "Historique complet et accessible"),
]
INTRO_D, OUTRO_D = 5.30, 6.20

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
             "fade",       # A -> B (continuous: click on Voir)
             "fade",       # B -> C (continuous: modal opens)
             "fade",       # C -> D (continuous: click on close)
             "fade",       # D -> E (continuous: modal closes, list restored)
             "fade",       # E -> F (continuous: click on the Statut filter)
             "fade",       # F -> G (continuous: filter values cycle)
             "fade",       # G -> H (continuous: back to Tous les statuts)
             "fade"]       # H -> outro
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
    "N0": 0.30,                  # intro hook
    "N1": S["A"] + 0.25,         # compteurs / liste
    "N2": S["B"] + 0.10,         # cliquez sur Voir -> punch
    "N3": S["C"] + 0.30,         # resume + transcription
    "N4": S["F"] + 0.10,         # filtre statut -> punch + cycle
    "N5": S["H"] + 0.20,         # benefice / liste finale
    "N6": OUTRO_START + 0.35,    # CTA
}
keys = [f"N{i}" for i in range(7)]
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
FINAL = f"{ROOT}/out/foodeatup-appels-reservations-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
