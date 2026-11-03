#!/usr/bin/env python3
"""Assemble one split-screen story (1-9) from its two already-generated
Higgsfield clips. Does not generate anything — clips must already sit in
clips/<name>.mp4. Usage: build_story.py story-01 [... story-09]
"""
import os, sys
from common import (
    MANIFEST, WORK, OUT, W, H, HALF_W, HALF_H, SEAM_PX, SEAM_COLOR, FPS,
    PALETTE, clip_path, check_square, banner_filter, run, duration, has_audio,
)
from endcard import ensure_endcard

BODY_SECONDS = 10


def story_by_id(story_id):
    for s in MANIFEST["stories"]:
        if s["id"] == story_id:
            return s
    raise SystemExit(f"Story inconnue: {story_id}")


def half_chain(label_in, label_out):
    return (
        f"[{label_in}]scale={HALF_W}:{HALF_H}:force_original_aspect_ratio=increase,"
        f"crop={HALF_W}:{HALF_H},setsar=1,fps={FPS}[{label_out}]"
    )


def build(story_id):
    s = story_by_id(story_id)
    sans = clip_path(s["clip_sans"])
    avec = clip_path(s["clip_avec"])
    missing = [n for n, p in [(s["clip_sans"], sans), (s["clip_avec"], avec)] if p is None]
    if missing:
        print(f"SKIP {story_id}: clip(s) manquant(s) — {', '.join(missing)}")
        return None

    check_square(s["clip_sans"], sans)
    check_square(s["clip_avec"], avec)

    body = f"{WORK}/{story_id}-body.mp4"
    banner_haut = banner_filter(s["texte_haut"], 90, PALETTE["avec_marine"])
    banner_bas = banner_filter(s["texte_bas"], H - 220, PALETTE["avec_bleu"])

    fc = [
        half_chain("0:v", "top"),
        half_chain("1:v", "bot"),
        f"color=c={SEAM_COLOR}:s={HALF_W}x{SEAM_PX}:d={BODY_SECONDS}:r={FPS}[seam]",
        "[top][seam][bot]vstack=inputs=3[stacked]",
        f"[stacked]{banner_haut},{banner_bas}[vout]",
    ]

    sans_has_a, avec_has_a = has_audio(sans), has_audio(avec)
    inputs = ["-i", sans, "-i", avec]
    if sans_has_a or avec_has_a:
        amix_inputs = []
        if sans_has_a:
            amix_inputs.append("[0:a]")
        if avec_has_a:
            amix_inputs.append("[1:a]")
        if len(amix_inputs) == 2:
            fc.append(f"{''.join(amix_inputs)}amix=inputs=2:duration=longest,"
                       f"loudnorm=I=-16:TP=-1.5:LRA=11[aout]")
        else:
            fc.append(f"{amix_inputs[0]}loudnorm=I=-16:TP=-1.5:LRA=11[aout]")
    else:
        # Pas de son exploitable dans les sources : piste muette (silence,
        # pas d'absence de piste) pour rester compatible avec le carton final.
        inputs += ["-f", "lavfi", "-t", str(BODY_SECONDS), "-i", "anullsrc=r=48000:cl=stereo"]
        fc.append("[2:a]anull[aout]")
    maps = ["-map", "[vout]", "-map", "[aout]"]
    acodec = ["-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2"]

    run(["ffmpeg", "-y", "-v", "error"] + inputs +
        ["-filter_complex", ";".join(fc)] + maps +
        ["-t", str(BODY_SECONDS), "-r", str(FPS),
         "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p"] +
        acodec + [body])

    endcard = ensure_endcard()
    final = f"{OUT}/{story_id}.mp4"
    if endcard is None:
        print(f"SKIP concat carton pour {story_id}: pas de carton confirmé — "
              f"corps seul écrit dans work/, PAS copié dans out/.")
        return None

    concat_list = f"{WORK}/{story_id}-concat.txt"
    with open(concat_list, "w") as f:
        f.write(f"file '{body}'\nfile '{endcard}'\n")
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
         "-i", concat_list,
         "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
         "-r", str(FPS), "-movflags", "+faststart", final])
    print(f"OK {story_id}: {final} ({duration(final):.2f}s)")
    return final


if __name__ == "__main__":
    ids = sys.argv[1:] or [s["id"] for s in MANIFEST["stories"] if s["id"] != "story-10"]
    for sid in ids:
        build(sid)
