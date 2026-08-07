#!/usr/bin/env python3
# FoodEatUp "Pointer son service -- pauses & photo" tutorial (module Equipe,
# Planning & RH, item 15). Fills the Lovable placeholder slug
# `pointer-son-service-cote-employe`.
#
# v2 -- built on the real screen recording (assets/screen.mp4, 23.88s), sent
# by Michael to replace the first (mislabeled) rush -- see SCRIPT.md for the
# full timeline / click coordinates measured frame-by-frame. Same engine as
# the rest of the series: setpts for speed (never zoompan on real footage),
# fixed crop+scale zoom-punch on each click, xfade on every cut forced back
# to yuv420p, 48kHz stereo AAC, +faststart.
import subprocess, os, sys
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (render_claude_stage1_png, render_claude_stage2_png,
                                     render_claude_stage3_png, CLAUDE_STAGE_D)

ROOT = "/home/user/Video/videos/foodeatup-pointer-service-tuto"
SRC  = f"{ROOT}/assets/screen.mp4"
W, H, FPS = 1920, 828, 25
SEG = f"{ROOT}/work/seg"
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
BLUE, ORANGE = "0x1B6DF3", "0xF7941D"
XF = 0.28
os.makedirs(SEG, exist_ok=True)
os.makedirs(f"{ROOT}/out", exist_ok=True)

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
    return (f"drawbox=x={ox-bw/2-p:.0f}:y={oy-bh/2-p:.0f}"
            f":w={bw+2*p:.0f}:h={bh+2*p:.0f}:color={ORANGE}@0.95:t=5")

def banner(text, seg_dur):
    if not text: return None
    tin, sl = 0.15, 0.32
    a = f"min(1\\,max(0\\,(t-{tin})/{sl}))"
    x = f"-640+700*({a})"
    y = H - 108
    return (f"drawbox=x='{x}':y={y}:w=10:h=62:color={ORANGE}@0.98:t=fill,"
            f"drawbox=x='({x})+10':y={y}:w=560:h=62:color={BLUE}@0.90:t=fill,"
            f"drawtext=fontfile={FONT}:text='{text}':fontsize=31:fontcolor=white"
            f":x='({x})+34':y={y+16}")

# Coordinates measured on full-res frames (see SCRIPT.md timeline).
BTN_BADGE  = (1598, 601); SZ_BADGE  = (340, 52)   # "Pas encore pointe" badge
BTN_ENTREE = (688, 672);  SZ_BTN    = (275, 60)   # Entree
BTN_PAUSE  = (968, 672);  SZ_BTN2   = (275, 60)   # Pause / Fin pause (same slot)
BTN_SORTIE = (1248, 672); SZ_BTN3   = (275, 60)   # Sortie

# (name, src_start, src_end, target_out_duration, button, btn_size, caption)
segs = [
    ("A1", 0.00,  1.85, 2.20, None,       None,    None),
    ("A2", 1.85,  2.60, 1.30, BTN_BADGE,  SZ_BADGE, "Ouvrir Pointage"),
    ("B1", 2.60,  2.90, 1.60, None,       None,    None),
    ("B2", 2.90,  3.20, 1.30, BTN_ENTREE, SZ_BTN,  None),
    ("B3", 3.20,  5.40, 1.80, None,       None,    "Photo + pointage envoyes"),
    ("C1", 5.90,  6.80, 2.00, None,       None,    "Entree enregistree"),
    ("D1", 6.90,  7.90, 1.80, BTN_PAUSE,  SZ_BTN2, None),
    ("D2", 8.00,  9.90, 1.60, None,       None,    "Pause enregistree"),
    ("E1", 11.00, 11.90, 1.80, None,      None,    "En pause"),
    ("F1", 12.00, 13.00, 1.80, BTN_PAUSE, SZ_BTN2, None),
    ("F2", 14.00, 15.00, 1.40, None,      None,    "Fin de pause enregistree"),
    ("G1", 16.00, 16.90, 1.80, None,      None,    "Duree de pause calculee"),
    ("G2", 16.90, 18.00, 1.80, BTN_SORTIE, SZ_BTN3, None),
    ("G3", 18.00, 19.90, 1.60, None,      None,    "Sortie enregistree"),
    ("H1", 20.00, 20.90, 2.30, None,      None,    "Journee terminee"),
]
INTRO_D = 2.50

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

CLAUDE_PROMPT = ("Fais-moi un resume de mes heures et de mes pauses pointees cette "
                  "semaine pour [nom employe].")

def build_silent(outro_d):
    card(f"{ROOT}/assets/intro.jpg", f"{SEG}/intro.mp4", INTRO_D, zoom_in=True)
    card(f"{ROOT}/assets/photo-confirmation.png", f"{SEG}/photo.mp4", 6.00, zoom_in=True)

    render_claude_stage1_png(f"{SEG}/claude1.png", W, H, CLAUDE_PROMPT)
    render_claude_stage2_png(f"{SEG}/claude2.png", W, H, CLAUDE_PROMPT)
    render_claude_stage3_png(f"{SEG}/claude3.png", W, H, CLAUDE_PROMPT,
        response="Bien sur ! Voici le recap de la semaine, avec les pauses hors norme signalees.")
    for i, d in enumerate(CLAUDE_STAGE_D, start=1):
        card(f"{SEG}/claude{i}.png", f"{SEG}/claude{i}.mp4", d, zoom_in=True, fade=False)

    card(f"{ROOT}/assets/outro.jpg", f"{SEG}/outro.mp4", outro_d, zoom_in=False)

    parts = [f"{SEG}/intro.mp4"]
    for name, s, e, target, btn, sz, cap in segs:
        parts.append(encode_seg(name, s, e, target, btn, sz, cap))
    parts += [f"{SEG}/photo.mp4", f"{SEG}/claude1.mp4", f"{SEG}/claude2.mp4",
              f"{SEG}/claude3.mp4", f"{SEG}/outro.mp4"]

    trans = (["fade"] +                       # intro -> A1
             ["fade"] +                       # A1 -> A2 (continuous: click badge)
             ["fade"] +                       # A2 -> B1 (modal opens)
             ["fade"] +                       # B1 -> B2 (click Entree)
             ["fade"] +                       # B2 -> B3 (continuous: processing)
             ["slideleft"] +                  # B3 -> C1 (cut to dashboard)
             ["slideleft"] +                  # C1 -> D1 (cut to modal reopened)
             ["fade"] +                       # D1 -> D2 (continuous: processing)
             ["slideleft"] +                  # D2 -> E1 (cut to dashboard)
             ["slideleft"] +                  # E1 -> F1 (cut to modal reopened)
             ["fade"] +                       # F1 -> F2 (continuous: processing)
             ["slideleft"] +                  # F2 -> G1 (cut to dashboard)
             ["slideleft"] +                  # G1 -> G2 (cut to modal reopened)
             ["fade"] +                       # G2 -> G3 (continuous: processing)
             ["slideleft"] +                  # G3 -> H1 (cut to dashboard)
             ["slideleft"] +                  # H1 -> photo
             ["slideleft"] +                  # photo -> claude1
             ["slideleft"] +                  # claude1 -> claude2
             ["slideleft"] +                  # claude2 -> claude3
             ["fade"])                        # claude3 -> outro
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
    names = (["intro"] + [s[0] for s in segs] +
             ["photo","claude1","claude2","claude3","outro"])
    return silent, dict(zip(names, starts))

OUTRO_D = 6.00
silent, S = build_silent(OUTRO_D)
print(f"SILENT TOTAL: {dur(silent):.2f}s")
OUTRO_START = S["outro"]

GAP = 0.22
anchor = {
    "N0": S["intro"]  + 0.15,
    "N1": S["B2"]     + 0.15,   # click Entree
    "N2": S["D1"]     + 0.15,   # click Pause
    "N3": S["F1"]     + 0.15,   # click Fin pause
    "N4": S["G2"]     + 0.15,   # click Sortie
    "N5": S["photo"]  + 0.15,
    "N6": S["claude1"] + 0.15,
    "N7": OUTRO_START + 0.30,
}
keys = ["N0","N1","N2","N3","N4","N5","N6","N7"]
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
    silent, S = build_silent(needed)
    print(f"SILENT TOTAL (extended): {dur(silent):.2f}s")
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
FINAL = f"{ROOT}/out/foodeatup-pointer-service-tuto-v2.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
