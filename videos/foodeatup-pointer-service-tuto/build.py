#!/usr/bin/env python3
# FoodEatUp "Pointer son service -- pauses & photo" tutorial (module Equipe,
# Planning & RH, item 15). Fills the Lovable placeholder slug
# `pointer-son-service-cote-employe`.
#
# NO USABLE SCREEN RECORDING for this one -- see SCRIPT.md. The rush sent
# under this title is the same mislabeled Google Drive file already
# documented in videos/LOVABLE-FOODEATUP-DOCS.md (row 17,
# creer-ses-roles-et-permissions): it shows Accueil/QR code/Roles, not the
# employee clock-in/pause/photo screen. Rather than reuse that same footage
# a second time (near-duplicate of an already-published tutorial) or invent
# a fake app screen, this build is card-based: real product screenshot
# (studio-video/assets/brand/product-screenshots/pointage.png, cropped into
# 3 close-ups) + one clearly-illustrative custom graphic for the photo/
# anti-fraud beat (not dressed up as a fabricated app screen) + the shared
# "use it with Claude" 3-stage sequence. Same engine (card() Ken Burns,
# xfade, loudnorm-per-line then alimiter) as the rest of the series.
import subprocess, os, sys
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (render_claude_stage1_png, render_claude_stage2_png,
                                     render_claude_stage3_png, CLAUDE_STAGE_D)

ROOT = "/home/user/Video/videos/foodeatup-pointer-service-tuto"
W, H, FPS = 1920, 828, 25
SEG = f"{ROOT}/work/seg"
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
    card(f"{ROOT}/assets/intro.jpg", f"{SEG}/intro.mp4", 3.00, zoom_in=True)
    card(f"{ROOT}/assets/pointage-popup.png", f"{SEG}/overview.mp4", 5.50, zoom_in=True)
    card(f"{ROOT}/assets/crop_entree.png", f"{SEG}/entree.mp4", 5.00, zoom_in=True)
    card(f"{ROOT}/assets/crop_pause.png", f"{SEG}/pause.mp4", 5.00, zoom_in=True)
    card(f"{ROOT}/assets/crop_boutons.png", f"{SEG}/sortie.mp4", 4.60, zoom_in=True)
    card(f"{ROOT}/assets/photo-confirmation.png", f"{SEG}/photo.mp4", 6.00, zoom_in=True)

    render_claude_stage1_png(f"{SEG}/claude1.png", W, H, CLAUDE_PROMPT)
    render_claude_stage2_png(f"{SEG}/claude2.png", W, H, CLAUDE_PROMPT)
    render_claude_stage3_png(f"{SEG}/claude3.png", W, H, CLAUDE_PROMPT,
        response="Bien sur ! Voici le recap de la semaine, avec les pauses hors norme signalees.")
    for i, d in enumerate(CLAUDE_STAGE_D, start=1):
        card(f"{SEG}/claude{i}.png", f"{SEG}/claude{i}.mp4", d, zoom_in=True, fade=False)

    card(f"{ROOT}/assets/outro.jpg", f"{SEG}/outro.mp4", outro_d, zoom_in=False)

    names = ["intro","overview","entree","pause","sortie","photo",
             "claude1","claude2","claude3","outro"]
    parts = [f"{SEG}/{n}.mp4" for n in names]

    trans = ["fade",       # intro -> overview (continuous reveal)
             "slideleft",  # overview -> entree
             "slideleft",  # entree -> pause
             "slideleft",  # pause -> sortie
             "slideleft",  # sortie -> photo
             "slideleft",  # photo -> claude1
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
    return silent, dict(zip(names, starts))

OUTRO_D = 6.00
silent, S = build_silent(OUTRO_D)
print(f"SILENT TOTAL: {dur(silent):.2f}s")
OUTRO_START = S["outro"]

GAP = 0.22
anchor = {
    "N0": S["intro"]    + 0.15,
    "N1": S["entree"]   + 0.15,
    "N2": S["pause"]    + 0.15,
    "N3": S["sortie"]   + 0.15,
    "N4": S["photo"]    + 0.15,
    "N5": S["claude1"]  + 0.15,
    "N6": OUTRO_START   + 0.30,
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
FINAL = f"{ROOT}/out/foodeatup-pointer-service-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
