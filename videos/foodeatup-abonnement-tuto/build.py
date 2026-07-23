#!/usr/bin/env python3
# Build the ~30s FoodEatUp subscription tutorial.
# Speed = setpts (NEVER zoompan -> freezes). Zoom-on-click = a constant crop+scale
# "punch" applied to the sub-clip AFTER the click moment (fixed crop, no per-frame eval).
import subprocess, os

ROOT = "/home/user/Video/videos/foodeatup-abonnement-tuto"
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

def clip(v, lo, hi): return max(lo, min(hi, v))

ZOOM = 1.20
def crop_for(btn):
    bx, by = btn
    cw, ch = int(W/ZOOM), int(H/ZOOM)
    cw -= cw % 2; ch -= ch % 2
    x = int(clip(bx - cw/2, 0, W - cw))
    y = int(clip(by - ch/2, 0, H - ch))
    return f"crop={cw}:{ch}:{x}:{y},scale={W}:{H}:flags=bicubic"

# Buttons (1920x828 source space)
BTN_PACK  = (600, 274)
BTN_CONT  = (410, 616)
BTN_START = (543, 740)

# (name, src_start, src_end, factor, click_src_time_or_None, button)
segs = [
    ("A", 0.0,  4.2,  0.90, 3.0,  BTN_PACK),
    ("B", 4.2,  9.0,  1.40, 8.0,  BTN_CONT),
    ("C", 9.0,  41.0, 6.00, None, None),
    ("D", 41.0, 43.5, 1.30, 42.6, BTN_START),
    ("P", 43.5, 53.0, 4.50, None, None),
    ("G", 53.0, 56.8, 1.30, None, None),
]

def encode(name, s, e, f, extra=""):
    out = f"{SEG}/{name}.mp4"
    vf = f"setpts=(PTS-STARTPTS)/{f}"
    if extra: vf += f",{extra}"
    else:     vf += f",scale={W}:{H}"
    vf += f",fps={FPS},format=yuv420p"
    run(["ffmpeg","-y","-ss",str(s),"-to",str(e),"-i",SRC,"-an",
         "-vf",vf,"-r",str(FPS),"-c:v","libx264","-preset","medium","-crf","18",out])
    return out

# Encode segments (splitting click segments into normal + zoomed sub-clips).
order = []          # list of clip paths in order
boundary = {}       # cumulative time at start of each logical segment
t = 0.0
INTRO_D, OUTRO_D = 3.0, 4.6
t = INTRO_D  # intro card occupies first slot; screen starts here
for name, s, e, f, ck, btn in segs:
    boundary[name] = t
    if ck is None:
        p = encode(name, s, e, f); order.append(p); t += dur(p)
    else:
        p1 = encode(name+"1", s, ck, f)               # pre-click (normal)
        p2 = encode(name+"2", ck, e, f, crop_for(btn))# post-click (zoom punch)
        order += [p1, p2]; t += dur(p1) + dur(p2)
    print(f"seg {name}: start={boundary[name]:.2f} -> {t:.2f}")
SCREEN_END = t

# Cards: blurred cover bg + fitted fg + fades.
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

# VO offsets: desired anchors, then pushed sequentially so lines NEVER overlap.
GAP = 0.18
anchor = {
    "N0": 0.30,
    "N1": INTRO_D + 2.10,          # near the pack click
    "N2": boundary["B"] + 1.90,    # modal recap -> payment
    "N3": boundary["D"] + 0.05,    # click demarrer
    "N4": boundary["G"] - 1.30,    # activation reveal
    "N5": SCREEN_END + 0.15,       # outro CTA
}
off = {}
prev_end = -GAP
for k in ["N0","N1","N2","N3","N4","N5"]:
    o = max(anchor[k], prev_end + GAP)
    off[k] = o
    prev_end = o + dur(f"{ROOT}/vo2/{k}.mp3")
print("offsets:", {k: round(v,2) for k,v in off.items()}, "voice_end:", round(prev_end,2))

inputs, filters, labels = [], [], []
for i,(k,o) in enumerate(off.items()):
    inputs += ["-i", f"{ROOT}/vo2/{k}.mp3"]
    ms = int(o*1000)
    filters.append(f"[{i+1}:a]adelay={ms}|{ms},apad[a{i}]")
    labels.append(f"[a{i}]")
n = len(off)
filters.append("".join(labels) + f"amix=inputs={n}:normalize=0:duration=first[mix]")
filters.append(f"[mix]atrim=0:{total:.3f},loudnorm=I=-16:TP=-1.5:LRA=11,alimiter=limit=0.89,asetpts=N/SR/TB[voa]")
run(["ffmpeg","-y","-i",f"{ROOT}/work/video_silent.mp4"] + inputs +
    ["-filter_complex", ";".join(filters), "-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-shortest",
     f"{ROOT}/out/foodeatup-abonnement-tuto-30s-v1.mp4"])
final = f"{ROOT}/out/foodeatup-abonnement-tuto-30s-v1.mp4"
print(f"DONE: {final}  {dur(final):.2f}s")
