#!/usr/bin/env python3
"""Étape 6 — décline le master en 1:1, 16:9, teaser 30 s et vignette.

Le 16:9 ne recadre pas : le plan vertical reste entier au centre, sur un fond
flouté tiré de lui-même — un recadrage 16:9 dans du 9:16 couperait les visages.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import common

TEASER_SEC = 30.0


def encode(cmd_filters: str, source: Path, target: Path, *, extra: list[str] | None = None,
           seek: float | None = None, length: float | None = None) -> None:
    cmd = [common.need_tool("ffmpeg"), "-y", "-v", "error"]
    if seek is not None:
        cmd += ["-ss", f"{seek:.6f}"]
    cmd += ["-i", str(source)]
    if length is not None:
        cmd += ["-t", f"{length:.6f}"]
    cmd += [
        "-filter_complex", cmd_filters,
        "-map", "[vout]", "-map", "0:a:0",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-pix_fmt", "yuv420p", "-r", str(common.FPS),
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        "-movflags", "+faststart",
        *(extra or []),
        str(target),
    ]
    common.run(cmd)


def teaser_window(edl: dict) -> tuple[float, float]:
    """Les 30 s autour du refrain final : on démarre un peu avant son entrée."""
    sections = {s["id"]: s for s in edl["sections"]}
    final = sections.get("refrain_final")
    duration = edl["duration_sec"]
    if not final:
        return max(0.0, duration - TEASER_SEC), TEASER_SEC
    start = max(0.0, final["start"] - 2.0)
    if start + TEASER_SEC > duration:
        start = max(0.0, duration - TEASER_SEC)
    return start, min(TEASER_SEC, duration - start)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--edl", default=str(common.WORK / "edl.json"))
    parser.add_argument("--master", default=str(common.OUT / "clip-9x16.mp4"))
    args = parser.parse_args()

    master = Path(args.master)
    if not common.probe_media(master):
        common.die(f"master introuvable ou illisible : {master} — joue scripts/05_assemble.py")
    edl = common.read_json(Path(args.edl))
    common.OUT.mkdir(parents=True, exist_ok=True)

    # 1:1 — recadrage centré dans le vertical (le sujet est déjà au centre).
    print("· clip-1x1.mp4")
    encode("[0:v]crop=1080:1080:0:(ih-1080)/2,format=yuv420p[vout]",
           master, common.OUT / "clip-1x1.mp4")

    # 16:9 — fond flouté + plan vertical entier au centre.
    print("· clip-16x9.mp4")
    encode(
        "[0:v]split=2[bg][fg];"
        "[bg]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,"
        "gblur=sigma=40,eq=brightness=-0.10:saturation=0.75[blurred];"
        "[fg]scale=-2:1080[front];"
        "[blurred][front]overlay=(W-w)/2:0,format=yuv420p[vout]",
        master, common.OUT / "clip-16x9.mp4",
    )

    # Teaser 30 s autour du refrain final, avec ses propres fondus.
    start, length = teaser_window(edl)
    print(f"· clip-teaser-30s.mp4 (à partir de {common.timecode(start)})")
    encode(
        f"[0:v]fade=t=in:st=0:d=0.5,fade=t=out:st={max(0.0, length - 1.0):.6f}:d=1.0,format=yuv420p[vout]",
        master, common.OUT / "clip-teaser-30s.mp4",
        seek=start, length=length,
        extra=["-af", f"afade=t=in:st=0:d=0.5,afade=t=out:st={max(0.0, length - 1.0):.6f}:d=1.0"],
    )

    # Vignette — une image du plan EP535 (le titre du film).
    final_shot = next((s for s in reversed(edl["segments"]) if s["ep"] == "EP535"), edl["segments"][-1])
    stamp = min(final_shot["start"] + 1.5, edl["duration_sec"] - 2.0)
    print(f"· vignette.jpg ({final_shot['ep']} à {common.timecode(stamp)})")
    common.run([
        common.need_tool("ffmpeg"), "-y", "-v", "error",
        "-ss", f"{stamp:.6f}", "-i", str(master),
        "-frames:v", "1", "-q:v", "2",
        str(common.OUT / "vignette.jpg"),
    ])

    print("\n✓ déclinaisons écrites dans out/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
