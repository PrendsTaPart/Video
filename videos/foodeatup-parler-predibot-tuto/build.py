#!/usr/bin/env python3
# FoodEatUp "Parler a PrediBot, votre agent RH" tutorial (PrediBot module, 3rd
# and last video of that module).
#
# Rush (53.76s, 1526x1032, WhatsApp desktop window capture): conversation with
# "Predibot" -- Liste mes employes -> Liste les conges -> Approuve le conge 995
# -> Rejette le conge 1023 -> Verifie les pointages -> Classement des employes.
# No clicks to zoom-punch here (it's a scrolling chat, not the FoodEatUp app),
# so segments are plain setpts speed-ups with a step banner, no punch_highlight.
# Source aspect (1.48:1) is narrower than the 1920x828 canvas (2.32:1) -> same
# "blurred background + contained foreground" treatment as the HeyGen avatar
# clip in foodeatup-boutique-tuto, no zoompan on real video.
#
# Same engine as the rest of the series: xfade on every cut forced back to
# yuv420p, 48kHz stereo AAC, +faststart, VO loudnorm per line before mixing.
import subprocess, os, sys

ROOT = "/home/user/Video/videos/foodeatup-parler-predibot-tuto"
SRC  = f"{ROOT}/assets/screen.mp4"
W, H, FPS = 1920, 828, 25
SEG = f"{ROOT}/work/seg"
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
BLUE, ORANGE = "0x1B6DF3", "0xF7941D"
XF = 0.28
os.makedirs(SEG, exist_ok=True)

sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (render_claude_stage1_png, render_claude_stage2_png,
                                     render_claude_stage3_png, CLAUDE_STAGE_D)

CLAUDE_PROMPT = 'Approuve le congé n°[ID congé] de [nom employé], commentaire : "[motif]".'
CLAUDE_RESPONSE = ("Congé approuvé ! Je peux aussi lister vos employés, vos congés en "
                    "attente, ou refuser une demande avec le motif de votre choix.")

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("ERR:", " ".join(cmd)[:300]); print(r.stderr[-2000:]); raise SystemExit(1)

def dur(path):
    r = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                        "-of","csv=p=0",path], capture_output=True, text=True)
    return float(r.stdout.strip())

def banner(text, seg_dur):
    if not text: return ""
    tin, sl = 0.15, 0.32
    a = f"min(1\\,max(0\\,(t-{tin})/{sl}))"
    x = f"-640+700*({a})"
    y = H - 108
    return (f",drawbox=x='{x}':y={y}:w=10:h=62:color={ORANGE}@0.98:t=fill"
            f",drawbox=x='({x})+10':y={y}:w=560:h=62:color={BLUE}@0.90:t=fill"
            f",drawtext=fontfile={FONT}:text='{text}':fontsize=31:fontcolor=white"
            f":x='({x})+34':y={y+16}")

# (name, src_start, src_end, target_out_duration, caption)
segs = [
    ("A", 6.0,  17.0, 6.5, "Liste des employés"),
    ("B", 21.0, 29.0, 5.0, "Congés en attente"),
    ("C", 29.0, 33.5, 2.2, "Congé approuvé"),
    ("D", 33.5, 39.5, 3.5, "Congé refusé (motif)"),
    ("E", 39.5, 44.5, 3.0, "Pointages sur la période"),
    ("F", 44.5, 53.6, 3.3, "Classement RH"),
]
INTRO_D, OUTRO_D = 2.20, 5.00

def encode_seg(name, s, e, target, caption):
    out = f"{SEG}/{name}.mp4"
    factor = (e - s) / target
    fc = (f"[0:v]setpts=(PTS-STARTPTS)/{factor:.6f}[sp];"
          f"[sp]split=2[a][b];"
          f"[a]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
          f"boxblur=20:2,eq=brightness=-0.06[bg];"
          f"[b]scale={W}:{H}:force_original_aspect_ratio=decrease[fg];"
          f"[bg][fg]overlay=(W-w)/2:(H-h)/2{banner(caption, target)}"
          f",fps={FPS},format=yuv420p[vout]")
    run(["ffmpeg","-y","-v","error","-ss",str(s),"-to",str(e),"-i",SRC,"-an",
         "-filter_complex",fc,"-map","[vout]","-r",str(FPS),
         "-c:v","libx264","-preset","medium","-crf","18",out])
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

    render_claude_stage1_png(f"{SEG}/claude1.png", W, H, CLAUDE_PROMPT)
    render_claude_stage2_png(f"{SEG}/claude2.png", W, H, CLAUDE_PROMPT)
    render_claude_stage3_png(f"{SEG}/claude3.png", W, H, CLAUDE_PROMPT, response=CLAUDE_RESPONSE)
    for i, d in enumerate(CLAUDE_STAGE_D, start=1):
        card(f"{SEG}/claude{i}.png", f"{SEG}/claude{i}.mp4", d, zoom_in=True, fade=False)

    parts = [f"{SEG}/intro.mp4"]
    for name, s, e, target, cap in segs:
        parts.append(encode_seg(name, s, e, target, cap))
    parts += [f"{SEG}/claude1.mp4", f"{SEG}/claude2.mp4", f"{SEG}/claude3.mp4",
              f"{SEG}/outro.mp4"]

    trans = ["fade",       # intro -> A
             "slideleft",  # A -> B (liste employes -> liste conges)
             "slideleft",  # B -> C (time jump: approuve)
             "slideleft",  # C -> D (rejette)
             "slideleft",  # D -> E (pointages)
             "slideleft",  # E -> F (classement)
             "slideleft",  # F -> claude1 (cut to Claude mockup)
             "slideleft",  # claude1 -> claude2
             "slideleft",  # claude2 -> claude3
             "fade"]       # claude3 -> outro
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
labels_order = ["intro"] + [s[0] for s in segs] + ["claude1", "claude2", "claude3", "outro"]
S = dict(zip(labels_order, starts))
OUTRO_START = S["outro"]

GAP = 0.22
anchor = {
    "N1": S["A"] + 0.15,       # liste employes
    "N2": S["B"] + 0.15,       # liste conges
    "N3": S["C"] + 0.10,       # approuve 995
    "N4": S["D"] + 0.15,       # rejette 1023
    "N5": S["E"] + 0.15,       # pointages
    "N6": S["F"] + 0.15,       # classement
    "N7": S["claude1"] + 0.10, # benefice, sur la sequence Claude
    "N8": OUTRO_START + 0.35,  # CTA
}
keys = ["N1","N2","N3","N4","N5","N6","N7","N8"]
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
FINAL = f"{ROOT}/out/foodeatup-parler-predibot-tuto-v1.mp4"
os.makedirs(f"{ROOT}/out", exist_ok=True)
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
