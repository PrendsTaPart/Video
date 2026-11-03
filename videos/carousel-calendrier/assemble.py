#!/usr/bin/env python3
"""Assemble the RapidoCMS Carousel presentation video.
8 still frames -> per-segment clips (VO+pads) -> slide-left xfade chain
-> delayed VO amix + looped BGM -> final 1080x1920 MP4."""
import subprocess, os, json

os.chdir(os.path.dirname(os.path.abspath(__file__)))
FRAMES = os.environ.get("FRAMES_DIR", "frames")
OUTNAME = os.environ.get("OUTNAME", "carousel-rapidocms.mp4")
FPS = 30
T = 0.45           # xfade duration (swipe)
HEAD = 0.35        # silence before VO in each clip
TAIL = 0.55        # silence after VO
import glob
N = len(glob.glob("audio/s*.mp3"))

def dur(f):
    return float(subprocess.check_output(
        ["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())

vo = [f"audio/s{i}.mp3" for i in range(N)]
vodur = [dur(v) for v in vo]
clip = [vodur[i] + HEAD + TAIL + (0.55 if i == N-1 else 0) for i in range(N)]  # extra tail on CTA
print("clip durations:", [round(c,2) for c in clip])

# 1) build per-segment silent video clips (static frame)
os.makedirs("work", exist_ok=True)
for i in range(N):
    out = f"work/clip{i}.mp4"
    subprocess.run(["ffmpeg","-y","-loop","1","-t",f"{clip[i]:.3f}","-i",f"{FRAMES}/f{i}.png",
        "-r",str(FPS),"-vf","scale=1080:1920:flags=lanczos,format=yuv420p,setsar=1",
        "-c:v","libx264","-preset","medium","-crf","18","-pix_fmt","yuv420p", out],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("built", out)

# 2) xfade chain (slide left) + compute segment start offsets on final timeline
inputs = []
for i in range(N):
    inputs += ["-i", f"work/clip{i}.mp4"]

fc = []
prev = "[0:v]"
cum = clip[0]               # running length of chained video
offsets = [0.0]             # timeline start of each clip's content
for i in range(1, N):
    off = cum - T
    lbl = f"[v{i}]"
    fc.append(f"{prev}[{i}:v]xfade=transition=slideleft:duration={T}:offset={off:.3f}{lbl}")
    prev = lbl
    offsets.append(off)     # clip i begins its full-opacity around off (start of xfade)
    cum = cum + clip[i] - T
total = cum
video_last = prev
print("total video:", round(total,2), "offsets:", [round(o,2) for o in offsets])

# VO plays at offset_i + HEAD
vo_delays = [offsets[i] + HEAD for i in range(N)]

# 3) audio graph: delay each VO, mix, add looped BGM
# add VO inputs
for i in range(N):
    inputs += ["-i", vo[i]]
# bgm looped
inputs += ["-stream_loop","-1","-i","audio/bgm.mp3"]
vo_base = N            # first VO input index
bgm_idx = N + N        # bgm input index

afc = []
vo_labels = []
for i in range(N):
    d_ms = int(vo_delays[i]*1000)
    lbl = f"[a{i}]"
    afc.append(f"[{vo_base+i}:a]adelay={d_ms}|{d_ms},apad=whole_dur={total:.3f}{lbl}")
    vo_labels.append(lbl)
afc.append("".join(vo_labels)+f"amix=inputs={N}:normalize=0:dropout_transition=0[vomix]")
# bgm: trim to total, volume, fades
afc.append(f"[{bgm_idx}:a]atrim=0:{total:.3f},asetpts=N/SR/TB,volume=0.10,"
           f"afade=t=in:st=0:d=1.2,afade=t=out:st={total-1.5:.3f}:d=1.5[bgm]")
afc.append(f"[vomix][bgm]amix=inputs=2:normalize=0:dropout_transition=0,"
           f"loudnorm=I=-14:TP=-1.5:LRA=11[aout]")

filtergraph = ";".join(fc + afc)
cmd = ["ffmpeg","-y"] + inputs + [
    "-filter_complex", filtergraph,
    "-map", video_last, "-map", "[aout]",
    "-c:v","libx264","-preset","medium","-crf","19","-pix_fmt","yuv420p",
    "-c:a","aac","-b:a","192k","-r",str(FPS),"-t",f"{total:.3f}",
    f"deliverable/{OUTNAME}"]
with open("work/filtergraph.txt","w") as f:
    f.write(filtergraph)
print("running final ffmpeg...")
r = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
if r.returncode != 0:
    print("FFMPEG ERROR:\n", r.stderr.decode()[-3000:])
    raise SystemExit(1)
print(f"OK -> deliverable/{OUTNAME}")
print(json.dumps({"total_s": round(total,2), "vo_delays":[round(x,2) for x in vo_delays]}, indent=2))
