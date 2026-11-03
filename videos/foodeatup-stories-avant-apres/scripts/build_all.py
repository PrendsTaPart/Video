#!/usr/bin/env python3
"""Build every story whose clips are already present, then print the
delivery report: duration/weight/resolution per file, and the exact reason
for each story not produced.
"""
import os
from common import MANIFEST, OUT, clip_path, duration, probe
from build_story import build as build_split
from build_signature import build as build_signature
from endcard import ensure_endcard, ENDCARD_SOURCE

results = {}
for s in MANIFEST["stories"]:
    if s["id"] == "story-10":
        results[s["id"]] = build_signature()
    else:
        results[s["id"]] = build_split(s["id"])

print("\n=== RAPPORT ===")
for s in MANIFEST["stories"]:
    sid = s["id"]
    path = results[sid]
    if path and os.path.exists(path):
        info = probe(path)
        size_mb = os.path.getsize(path) / 1024 / 1024
        print(f"{sid}.mp4 — {duration(path):.2f}s — {size_mb:.1f} Mo — "
              f"{info['width']}x{info['height']}")
    else:
        if "clip_full" in s:
            clips_ok = clip_path(s["clip_full"]) is not None
        else:
            clips_ok = clip_path(s["clip_sans"]) is not None and clip_path(s["clip_avec"]) is not None
        if not clips_ok:
            reason = "clip(s) source manquant(s) dans clips/"
        elif not ENDCARD_SOURCE or not os.path.exists(ENDCARD_SOURCE):
            reason = "carton final non confirmé (manifest.json endcard.source)"
        else:
            reason = "échec de montage — voir logs ffmpeg ci-dessus"
        print(f"{sid} — NON PRODUITE — {reason}")
