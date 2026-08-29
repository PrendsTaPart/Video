#!/usr/bin/env python3
"""Étape 5 — assemble les plans en un master 9:16 et y colle la chanson.

Coupe franche par défaut ; fondu de 0,3 s à chaque bascule avant ↔ après (le plan
sortant a été rendu 0,3 s plus long à l'étape 4, le fondu mange ce rab et la
timeline musicale ne bouge pas). Fondu au noir de 1,5 s en sortie. L'audio des
rushes n'est jamais repris : la chanson est la seule source sonore.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import common

RUNS = common.WORK / "runs"
FADE_OUT = 1.5


def concat_run(index: int, files: list[Path]) -> Path:
    """Colle bout à bout les plans d'un même run (mêmes réglages d'encodage → copie)."""
    RUNS.mkdir(parents=True, exist_ok=True)
    listing = RUNS / f"run-{index:02d}.txt"
    listing.write_text(
        "".join(f"file '{path.resolve()}'\n" for path in files), encoding="utf-8"
    )
    target = RUNS / f"run-{index:02d}.mp4"
    common.run([
        common.need_tool("ffmpeg"), "-y", "-v", "error",
        "-f", "concat", "-safe", "0", "-i", str(listing),
        "-c", "copy", "-video_track_timescale", "30000",
        str(target),
    ])
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--edl", default=str(common.WORK / "edl.json"))
    parser.add_argument("--audio", help="chanson (défaut : le fichier analysé à l'étape 2)")
    parser.add_argument("--out", default=str(common.OUT / "clip-9x16.mp4"))
    args = parser.parse_args()

    common.ensure_dirs()
    edl = common.read_json(Path(args.edl))
    segments = edl["segments"]
    duration = edl["duration_sec"]
    xfade = edl["xfade_sec"]
    # Par défaut on reprend exactement le fichier analysé à l'étape 2 : monter sur une
    # grille de temps issue d'un autre fichier que celui collé au master serait invisible
    # au rendu et catastrophique à l'écoute.
    recorded = edl.get("song_path")
    if args.audio:
        song = common.find_song(args.audio)
    elif recorded and Path(recorded).exists():
        song = Path(recorded)
    else:
        song = common.find_song(None)

    missing = [s["id"] for s in segments if not (common.SEGMENTS / f"{s['id']}.mp4").exists()]
    if missing:
        common.die(f"{len(missing)} plans non rendus (ex. {missing[0]}) — joue scripts/04_render_segments.py")

    # 1. Un fichier par run (le run se termine à chaque fondu).
    runs: list[tuple[Path, float]] = []
    for run_index in sorted({s["run"] for s in segments}):
        members = [s for s in segments if s["run"] == run_index]
        files = [common.SEGMENTS / f"{s['id']}.mp4" for s in members]
        path = concat_run(run_index, files)
        info = common.probe_media(path)
        if not info:
            common.die(f"run {run_index} illisible après collage")
        runs.append((path, info["duration"]))
        print(f"  run {run_index:02d} · {len(files):3d} plans · {info['duration']:7.3f}s")

    # 2. Chaînage des runs : fondu croisé de 0,3 s à chaque jointure.
    inputs: list[str] = []
    for path, _ in runs:
        inputs += ["-i", str(path)]
    inputs += ["-i", str(song)]
    audio_index = len(runs)

    filters: list[str] = []
    label = "0:v"
    timeline = runs[0][1]
    for index in range(1, len(runs)):
        offset = timeline - xfade
        out_label = f"v{index}"
        filters.append(
            f"[{label}][{index}:v]xfade=transition=fade:duration={xfade}:offset={offset:.6f}[{out_label}]"
        )
        label = out_label
        timeline = timeline + runs[index][1] - xfade

    fade_start = max(0.0, duration - FADE_OUT)
    filters.append(
        f"[{label}]fade=t=out:st={fade_start:.6f}:d={FADE_OUT},format=yuv420p[vout]"
    )

    target = Path(args.out)
    target.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        common.need_tool("ffmpeg"), "-y", "-v", "error", "-stats",
        *inputs,
        "-filter_complex", ";".join(filters),
        "-map", "[vout]", "-map", f"{audio_index}:a:0",
        "-t", f"{duration:.6f}",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-pix_fmt", "yuv420p", "-r", str(common.FPS),
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        "-movflags", "+faststart",
        str(target),
    ]
    print(f"\nassemblage de {len(runs)} runs ({timeline:.3f}s) + {song.name}…")
    common.run(cmd, quiet=False)

    info = common.probe_media(target)
    if not info:
        common.die("le master rendu est illisible")
    print(f"\n→ {target.relative_to(common.PROJECT)} · {info['duration']:.3f}s · "
          f"{info['width']}x{info['height']} · {info['fps']} i/s · audio {'oui' if info['has_audio'] else 'NON'}")
    if abs(info["duration"] - duration) > 0.2:
        print(f"⚠ écart avec la chanson : {info['duration'] - duration:+.3f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
