#!/usr/bin/env python3
# FoodEatUp "Configurer ses fournisseurs" tutorial (~48s, target 45-90s).
# Speed = setpts (NEVER zoompan). Zoom-on-click = constant crop+scale punch on the
# sub-clip AFTER the click moment (fixed crop, no per-frame eval).
import subprocess, os

ROOT = "/home/user/Video/videos/foodeatup-fournisseurs-tuto"
SRC  = f"{ROOT}/assets/screen.mp4"
W, H, FPS = 1920, 828, 25
SEG = f"{ROOT}/work/seg"
os.makedirs(SEG, exist_ok=True)

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("ERR:", " ".join(cmd)[:200]); print(r.stderr[-1500:]); raise SystemExit(1)

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
    return f"crop={cw}:{ch}:{x}:{y},scale={W}:{H}:flags=bicubic"

BTN_ADD  = (1656, 344)   # "Ajouter un fournisseur"
BTN_SAVE = (1034, 734)   # "Enregistrer"

# (name, src_start, src_end, factor, click_src_time_or_None, button)
segs = [
    ("A", 0.0,  2.5,  1.00, 1.5,  BTN_ADD),   # list + click Ajouter
    ("B", 2.5,  33.0, 1.70, None, None),       # form fill 1 (nom/adresse/email/tel)
    ("C", 33.0, 51.0, 1.50, None, None),       # form fill 2 (statut/cat/livraison/etoiles)
    ("D", 51.0, 55.0, 1.30, 54.0, BTN_SAVE),   # click Enregistrer
    ("E", 55.0, 61.08, 1.30, None, None),      # saved supplier card
]

def encode(name, s, e, f, extra=""):
    out = f"{SEG}/{name}.mp4"
    vf = f"setpts=(PTS-STARTPTS)/{f}"
    vf += f",{extra}" if extra else f",scale={W}:{H}"
    vf += f",fps={FPS},format=yuv420p"
    run(["ffmpeg","-y","-ss",str(s),"-to",str(e),"-i",SRC,"-an",
         "-vf",vf,"-r",str(FPS),"-c:v","libx264","-preset","medium","-crf","18",out])
    return out

order = []; boundary = {}
INTRO_D, OUTRO_D = 3.5, 5.4
t = INTRO_D
for name, s, e, f, ck, btn in segs:
    boundary[name] = t
    if ck is None:
        p = encode(name, s, e, f); order.append(p); t += dur(p)
    else:
        p1 = encode(name+"1", s, ck, f)
        p2 = encode(name+"2", ck, e, f, crop_for(btn))
        order += [p1, p2]; t += dur(p1) + dur(p2)
    print(f"seg {name}: start={boundary[name]:.2f} -> {t:.2f}")
SCREEN_END = t

def card(img, out, secs, fin, fout):
    vf = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
          f"boxblur=20:2,eq=brightness=-0.06[bg];"
          f"[0:v]scale={W}:{H}:force_original_aspect_ratio=decrease[fg];"
          f"[bg][fg]overlay=(W-w)/2:(H-h)/2,"
          f"fade=t=in:st=0:d={fin},fade=t=out:st={secs-fout}:d={fout},"
          f"fps={FPS},format=yuv420p")
    run(["ffmpeg","-y","-loop","1","-t",str(secs),"-i",img,
         "-filter_complex",vf,"-r",str(FPS),
         "-c:v","libx264","-preset","medium","-crf","18",out])

card(f"{ROOT}/assets/intro.jpg", f"{SEG}/intro.mp4", INTRO_D, 0.4, 0.3)
card(f"{ROOT}/assets/outro.jpg", f"{SEG}/outro.mp4", OUTRO_D, 0.4, 0.6)

full = [f"{SEG}/intro.mp4"] + order + [f"{SEG}/outro.mp4"]
with open(f"{SEG}/list.txt","w") as fh:
    for p in full: fh.write(f"file '{p}'\n")
run(["ffmpeg","-y","-f","concat","-safe","0","-i",f"{SEG}/list.txt",
     "-c:v","libx264","-preset","medium","-crf","18","-r",str(FPS),
     f"{ROOT}/work/video_silent.mp4"])
total = dur(f"{ROOT}/work/video_silent.mp4")
print(f"SILENT TOTAL: {total:.2f}s")

# VO: anchors then sequential push (no overlap).
GAP = 0.18
anchor = {
    "N0": 0.30,
    "N1": boundary["A"] + 0.30,
    "N2": boundary["B"] + 0.50,
    "N3": boundary["C"] + 0.30,
    "N4": boundary["D"] + 1.30,   # aligns with Enregistrer click zoom
    "N5": boundary["E"] + 0.20,   # card appears
    "N6": SCREEN_END + 0.15,      # outro CTA
}
off = {}; prev_end = -GAP
for k in ["N0","N1","N2","N3","N4","N5","N6"]:
    o = max(anchor[k], prev_end + GAP); off[k] = o
    prev_end = o + dur(f"{ROOT}/vo/{k}.mp3")
print("offsets:", {k: round(v,2) for k,v in off.items()}, "voice_end:", round(prev_end,2))

inputs, filters, labels = [], [], []
for i,(k,o) in enumerate(off.items()):
    inputs += ["-i", f"{ROOT}/vo/{k}.mp3"]; ms = int(o*1000)
    filters.append(f"[{i+1}:a]adelay={ms}|{ms},apad[a{i}]"); labels.append(f"[a{i}]")
n = len(off)
filters.append("".join(labels) + f"amix=inputs={n}:normalize=0:duration=first[mix]")
filters.append(f"[mix]atrim=0:{total:.3f},loudnorm=I=-16:TP=-1.5:LRA=11,alimiter=limit=0.89,asetpts=N/SR/TB[voa]")
run(["ffmpeg","-y","-i",f"{ROOT}/work/video_silent.mp4"] + inputs +
    ["-filter_complex", ";".join(filters), "-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-shortest",
     f"{ROOT}/out/foodeatup-fournisseurs-tuto-v1.mp4"])
final = f"{ROOT}/out/foodeatup-fournisseurs-tuto-v1.mp4"
print(f"DONE: {final}  {dur(final):.2f}s")
