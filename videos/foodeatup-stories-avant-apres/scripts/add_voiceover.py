#!/usr/bin/env python3
"""Mix a pre-generated ElevenLabs voiceover into an already-built story.
The VO mp3 must already exist at work/vo/<story-id>.mp3 (fetched via the
ElevenLabs MCP tool — this script only does the ffmpeg mixing).
Ducks the existing ambience track under the VO, then re-normalizes to
-16 LUFS. Overwrites out/<story-id>.mp4 in place.

Usage: add_voiceover.py story-01 [story-02 ...]
"""
import os, sys
from common import MANIFEST, WORK, OUT, FPS, run, duration

VO_START = 0.4
AMBIENCE_DUCK = 0.3  # ambience kept at 30% under the voiceover


def add_voiceover(story_id):
    video = f"{OUT}/{story_id}.mp4"
    vo = f"{WORK}/vo/{story_id}.mp3"
    if not os.path.exists(video):
        print(f"SKIP {story_id}: {video} n'existe pas — monte d'abord la story.")
        return
    if not os.path.exists(vo):
        print(f"SKIP {story_id}: pas de voix off à {vo}.")
        return

    total = duration(video)
    delay_ms = int(VO_START * 1000)
    fc = (
        f"[0:a]volume={AMBIENCE_DUCK}[amb];"
        f"[1:a]adelay={delay_ms}|{delay_ms},apad[vo];"
        f"[amb][vo]amix=inputs=2:duration=first:dropout_transition=0,"
        f"loudnorm=I=-16:TP=-1.5:LRA=11,"
        f"aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo[aout]"
    )
    out_tmp = f"{WORK}/{story_id}-with-vo.mp4"
    run(["ffmpeg", "-y", "-v", "error", "-i", video, "-i", vo,
         "-filter_complex", fc, "-map", "0:v", "-map", "[aout]",
         "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
         "-t", f"{total:.3f}", "-movflags", "+faststart", out_tmp])
    os.replace(out_tmp, video)
    print(f"OK {story_id}: voix off mixée dans {video} ({duration(video):.2f}s)")


if __name__ == "__main__":
    ids = sys.argv[1:] or [s["id"] for s in MANIFEST["stories"]]
    for sid in ids:
        add_voiceover(sid)
