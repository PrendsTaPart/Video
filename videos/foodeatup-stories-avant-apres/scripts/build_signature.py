#!/usr/bin/env python3
"""Assemble story-10 (signature): plein cadre 9:16, pas de split-screen.
Usage: build_signature.py
"""
from common import (
    MANIFEST, WORK, OUT, W, H, FPS, PALETTE, FONT_BOLD,
    clip_path, run, duration, has_audio,
)
from endcard import ensure_endcard

BODY_SECONDS = 10


def story_by_id(story_id):
    for s in MANIFEST["stories"]:
        if s["id"] == story_id:
            return s
    raise SystemExit(f"Story inconnue: {story_id}")


def timed_banner(text, start, end, y, box_color):
    text = text.replace("'", "\\'").replace(":", "\\:")
    return (
        f"drawtext=fontfile={FONT_BOLD}:text='{text}':fontsize=50:fontcolor=white"
        f":box=1:boxcolor={box_color}@0.7:boxborderw=26"
        f":x=(w-text_w)/2:y={y}:enable='between(t,{start},{end})'"
    )


def build():
    s = story_by_id("story-10")
    src = clip_path(s["clip_full"])
    if src is None:
        print(f"SKIP story-10: clip manquant — {s['clip_full']}")
        return None

    body = f"{WORK}/story-10-body.mp4"
    y = H - 320
    b1 = timed_banner(s["texte_1"], 1.2, 5.5, y, PALETTE["avec_marine"])
    b2 = timed_banner(s["texte_2"], 6.0, 8.8, y, PALETTE["avec_bleu"])

    vf = (f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
          f"setsar=1,fps={FPS},{b1},{b2}")

    src_has_a = has_audio(src)
    if src_has_a:
        run(["ffmpeg", "-y", "-v", "error", "-i", src,
             "-vf", vf, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
             "-t", str(BODY_SECONDS), "-r", str(FPS),
             "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
             "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", body])
    else:
        run(["ffmpeg", "-y", "-v", "error", "-i", src,
             "-f", "lavfi", "-t", str(BODY_SECONDS), "-i", "anullsrc=r=48000:cl=stereo",
             "-vf", vf, "-map", "0:v", "-map", "1:a",
             "-t", str(BODY_SECONDS), "-r", str(FPS),
             "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
             "-c:a", "aac", "-b:a", "192k", body])

    endcard = ensure_endcard()
    final = f"{OUT}/story-10.mp4"
    if endcard is None:
        print("SKIP concat carton pour story-10: pas de carton confirmé — "
              "corps seul écrit dans work/, PAS copié dans out/.")
        return None

    concat_list = f"{WORK}/story-10-concat.txt"
    with open(concat_list, "w") as f:
        f.write(f"file '{body}'\nfile '{endcard}'\n")
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
         "-i", concat_list,
         "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
         "-r", str(FPS), "-movflags", "+faststart", final])
    print(f"OK story-10: {final} ({duration(final):.2f}s)")
    return final


if __name__ == "__main__":
    build()
