#!/usr/bin/env python3
"""Build foodeatup-configurateur-cas-usage-tuto.mp4 from the WhatsApp/Predibot rush.

Pitfalls avoided (see videos/FOODEATUP-TUTORIELS-WORKFLOW.md):
- setpts for speed changes, never zoompan on a video (zoompan is fine on a still image).
- drawtext via textfile (no apostrophe-in-shell-string crash).
- loudnorm per VO line before adelay/apad, alimiter with level=disabled on the final mix.
"""
import json
import subprocess
import os

import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
ROOT = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(ROOT, "assets")
VO = os.path.join(ROOT, "vo")
WORK = os.path.join(ROOT, "work")
OUT = os.path.join(ROOT, "out")
os.makedirs(WORK, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

RUSH = os.path.join(
    os.path.dirname(ROOT), "foodeatup-configurateur", "reference",
    "cas-usage-predibot-whatsapp.mp4",
)  # committed asset, avoids duplicating the 12MB rush in this project too
INTRO_IMG = os.path.join(ASSETS, "intro.jpg")
OUTRO_IMG = os.path.join(ASSETS, "outro.jpg")
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

W, H = 1280, 720
FPS = 25
# source is 1526x1032; crop to 16:9 centered (drops the window title bar and the
# "Activer Windows" watermark, both near the very top/bottom edges), then scale.
CROP = "crop=1526:858:0:68"

def run(cmd):
    print("+", " ".join(cmd))
    subprocess.run(cmd, check=True)

def ffprobe_duration(path):
    out = subprocess.run(
        [FFMPEG, "-i", path], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True
    ).stderr
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("Duration:"):
            hms = line.split(",")[0].split("Duration:")[1].strip()
            h, m, s = hms.split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    raise RuntimeError(f"no duration found for {path}")

VO_DUR = {}
for i in range(9):
    p = os.path.join(VO, f"N{i:02d}.mp3")
    VO_DUR[i] = ffprobe_duration(p)
    print(f"N{i:02d}: {VO_DUR[i]:.2f}s")

PAD = 0.4
LEAD = 0.15

# (index, kind, src_start, src_end, caption)
SCENES = [
    (1, "clip", 6.0, 18.0, "Ajouter un employé"),
    (2, "clip", 18.0, 31.0, "Ajouter un fournisseur"),
    (3, "clip", 31.0, 45.0, "Ajouter un ingrédient"),
    (4, "clip", 45.0, 57.0, "Ajouter un produit"),
    (5, "clip", 57.0, 70.0, "Ajouter une recette"),
    (6, "clip", 70.0, 80.4, "Résultat instantané dans FoodEatUp"),
    (7, "clip", 0.0, 4.0, "Vous écrivez. Le Configurateur configure."),
]

def make_intro():
    dur = VO_DUR[0] + 0.3
    out = os.path.join(WORK, "scene_00_intro.mp4")
    vf = (
        f"scale={W*2}:{H*2},"
        f"zoompan=z='min(zoom+0.0007,1.08)':d={int(dur*FPS)}:s={W}x{H}:fps={FPS},"
        f"fade=t=in:st=0:d=0.3,fade=t=out:st={dur-0.3:.2f}:d=0.3,format=yuv420p"
    )
    run([FFMPEG, "-y", "-loop", "1", "-i", INTRO_IMG, "-t", f"{dur:.3f}", "-vf", vf,
         "-r", str(FPS), "-an", out])
    return out, dur

def make_outro():
    dur = VO_DUR[8] + 0.6
    out = os.path.join(WORK, "scene_08_outro.mp4")
    vf = (
        f"scale={W*2}:{H*2},"
        f"zoompan=z='min(zoom+0.0007,1.08)':d={int(dur*FPS)}:s={W}x{H}:fps={FPS},"
        f"fade=t=in:st=0:d=0.3,fade=t=out:st={dur-0.3:.2f}:d=0.3,format=yuv420p"
    )
    run([FFMPEG, "-y", "-loop", "1", "-i", OUTRO_IMG, "-t", f"{dur:.3f}", "-vf", vf,
         "-r", str(FPS), "-an", out])
    return out, dur

def make_clip(idx, src_start, src_end, caption, vo_idx):
    target = VO_DUR[vo_idx] + PAD
    src_dur = src_end - src_start
    factor = src_dur / target
    out = os.path.join(WORK, f"scene_{idx:02d}_clip.mp4")
    vf = (
        f"{CROP},setpts=(PTS-STARTPTS)/{factor:.6f},"
        f"scale={W}:{H},fps={FPS},"
        f"fade=t=in:st=0:d=0.25,fade=t=out:st={target-0.25:.2f}:d=0.25,format=yuv420p"
    )
    run([FFMPEG, "-y", "-ss", f"{src_start:.3f}", "-t", f"{src_dur:.3f}", "-i", RUSH,
         "-vf", vf, "-an", out])
    return out, target

def main():
    clips = []
    intro_path, intro_dur = make_intro()
    clips.append((intro_path, intro_dur, 0))
    for idx, kind, s, e, cap in SCENES:
        path, dur = make_clip(idx, s, e, cap, idx)
        clips.append((path, dur, idx))
    outro_path, outro_dur = make_outro()
    clips.append((outro_path, outro_dur, 8))

    # concat (all same codec params -> demuxer concat, no re-encode needed for join step,
    # but we still re-encode below when muxing audio so mismatches are harmless)
    listfile = os.path.join(WORK, "concat.txt")
    with open(listfile, "w") as f:
        for path, _, _ in clips:
            f.write(f"file '{path}'\n")
    video_concat = os.path.join(WORK, "video_concat.mp4")
    run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", listfile,
         "-c", "copy", video_concat])

    # audio timeline
    starts = []
    t = 0.0
    for path, dur, vo_idx in clips:
        starts.append((vo_idx, t, dur))
        t += dur
    total_dur = t
    print(f"total duration: {total_dur:.2f}s")

    # burned-in captions (subtitles filter / libass — drawtext isn't compiled
    # into this static ffmpeg build)
    captions = {idx: cap for idx, _, _, _, cap in SCENES}

    def srt_ts(sec):
        h = int(sec // 3600)
        m = int((sec % 3600) // 60)
        s = int(sec % 60)
        ms = int(round((sec - int(sec)) * 1000))
        return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

    srt_path = os.path.join(WORK, "captions.srt")
    with open(srt_path, "w") as f:
        n = 1
        for vo_idx, start, dur in starts:
            if vo_idx not in captions:
                continue
            cue_start = start + 0.3
            cue_end = start + dur - 0.3
            f.write(f"{n}\n{srt_ts(cue_start)} --> {srt_ts(cue_end)}\n{captions[vo_idx]}\n\n")
            n += 1

    # normalize each VO line individually (loudnorm before adelay, per pitfalls doc)
    norm_paths = {}
    for i in range(9):
        src = os.path.join(VO, f"N{i:02d}.mp3")
        dst = os.path.join(WORK, f"vo_norm_{i:02d}.wav")
        run([FFMPEG, "-y", "-i", src, "-af",
             "loudnorm=I=-16:TP=-1.5:LRA=11", dst])
        norm_paths[i] = dst

    # build delayed VO inputs + amix
    inputs = []
    filter_parts = []
    for i, (vo_idx, start, _dur) in enumerate(starts):
        inputs += ["-i", norm_paths[vo_idx]]
        delay_ms = int((start + LEAD) * 1000)
        filter_parts.append(f"[{i}:a]adelay={delay_ms}|{delay_ms}[vo{i}]")
    vo_labels = "".join(f"[vo{i}]" for i in range(len(starts)))

    bgm_src = os.path.join(os.path.dirname(ROOT), "foodeatup-configurateur", "assets", "bgm", "track.mp3")
    inputs += ["-i", bgm_src]
    bgm_i = len(starts)
    filter_parts.append(
        f"[{bgm_i}:a]aloop=loop=-1:size=2147483647,atrim=0:{total_dur:.3f},"
        f"afade=t=in:st=0:d=1,afade=t=out:st={total_dur-1.5:.2f}:d=1.5,volume=0.10[bgm]"
    )
    filter_parts.append(
        f"{vo_labels}[bgm]amix=inputs={len(starts)+1}:duration=longest:normalize=0[mixraw]"
    )
    filter_parts.append("[mixraw]alimiter=limit=0.6:level=disabled[mix]")
    filter_complex = ";".join(filter_parts)

    audio_out = os.path.join(WORK, "audio_mix.wav")
    run([FFMPEG, "-y", *inputs, "-filter_complex", filter_complex,
         "-map", "[mix]", "-t", f"{total_dur:.3f}", audio_out])

    final_out = os.path.join(OUT, "foodeatup-configurateur-cas-usage-tuto.mp4")
    style = (
        "FontName=Liberation Sans,FontSize=15,Bold=1,PrimaryColour=&H00FFFFFF,"
        "OutlineColour=&H00412A1B,BorderStyle=1,Outline=3,Shadow=0,"
        "Alignment=2,MarginV=55"
    )
    sub_vf = f"subtitles={srt_path}:force_style='{style}'"
    run([FFMPEG, "-y", "-i", video_concat, "-i", audio_out,
         "-vf", sub_vf,
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", str(FPS),
         "-c:a", "aac", "-b:a", "192k", "-shortest", final_out])

    peak = subprocess.run([FFMPEG, "-i", final_out, "-af", "astats", "-f", "null", "-"],
                           stderr=subprocess.PIPE, text=True).stderr
    for line in peak.splitlines():
        if "Peak level" in line:
            print(line.strip())

    with open(os.path.join(OUT, "meta.json"), "w") as f:
        json.dump({"total_duration_s": round(total_dur, 2)}, f, indent=2)
    print("DONE:", final_out, f"{total_dur:.2f}s")

if __name__ == "__main__":
    main()
