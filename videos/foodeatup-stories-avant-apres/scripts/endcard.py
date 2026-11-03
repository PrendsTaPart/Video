#!/usr/bin/env python3
"""Conform the FoodEatUp brand end-card into a fixed 1080x1920 / 24fps /
ENDCARD_SECONDS clip with a silent stereo AAC track, cached in work/.
Never fabricates a card: if manifest.json's endcard.source is unset or the
file is missing, returns None and callers must stop and ask instead of
inventing one (see README.md #carton).
"""
import os
from common import ENDCARD_SOURCE, ENDCARD_SECONDS, WORK, W, H, FPS, PALETTE, run

CACHE = f"{WORK}/endcard_conformed.mp4"


def ensure_endcard():
    if not ENDCARD_SOURCE or not os.path.exists(ENDCARD_SOURCE):
        return None
    if os.path.exists(CACHE):
        return CACHE

    is_image = ENDCARD_SOURCE.lower().endswith((".png", ".jpg", ".jpeg"))
    if is_image:
        # Logo lockup is landscape (~2.6:1): contain it, don't crop-to-fill —
        # cropping a wide logo card to a 9:16 frame zooms into a few letters.
        # Pad on the brand blue so the card reads as floating on a blue field.
        vf = (f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
              f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color={PALETTE['avec_bleu']},"
              f"setsar=1,fps={FPS}")
    else:
        vf = (f"scale={W}:{H}:force_original_aspect_ratio=increase,"
              f"crop={W}:{H},setsar=1,fps={FPS}")

    if is_image:
        run(["ffmpeg", "-y", "-v", "error", "-loop", "1", "-t", str(ENDCARD_SECONDS),
             "-i", ENDCARD_SOURCE,
             "-f", "lavfi", "-t", str(ENDCARD_SECONDS), "-i", "anullsrc=r=48000:cl=stereo",
             "-vf", vf, "-r", str(FPS),
             "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
             "-c:a", "aac", "-b:a", "192k", "-shortest", CACHE])
    else:
        run(["ffmpeg", "-y", "-v", "error", "-i", ENDCARD_SOURCE,
             "-f", "lavfi", "-t", str(ENDCARD_SECONDS), "-i", "anullsrc=r=48000:cl=stereo",
             "-t", str(ENDCARD_SECONDS), "-vf", vf, "-r", str(FPS),
             "-map", "0:v", "-map", "1:a",
             "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
             "-c:a", "aac", "-b:a", "192k", CACHE])
    return CACHE
