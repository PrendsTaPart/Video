#!/usr/bin/env python3
"""Étape 4 — rend chaque plan de l'EDL en 1080×1920, 30 i/s, étalonné.

Découpe précise avec ré-encodage (jamais -c copy : les rushes sont en 24 i/s et
les points d'entrée ne tombent pas sur des images clés). Les rushes sont déjà en
9:16, le recadrage est donc centré et ne coupe aucun visage.

Idempotent : un segment déjà rendu avec les mêmes paramètres n'est pas refait.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path

import common

# Étalonnage : froid et désaturé sur les actes « avant », chaud et contrasté
# sur « apres » et « final » — c'est le montage qui raconte la bascule.
GRADES = {
    "froid": "eq=saturation=0.70:contrast=1.05:brightness=-0.015:gamma=0.98,"
             "colorbalance=rs=-0.05:gs=-0.012:bs=0.090",
    "chaud": "eq=saturation=1.14:contrast=1.10:brightness=0.012:gamma=1.02,"
             "colorbalance=rs=0.080:gs=0.020:bs=-0.055",
}


def fingerprint(segment: dict) -> str:
    payload = json.dumps(
        {k: segment[k] for k in ("ep", "in_point", "render_len", "speed", "grade", "source_len")},
        sort_keys=True,
    )
    return hashlib.sha1(payload.encode()).hexdigest()[:12]


def filter_chain(segment: dict) -> str:
    steps = []
    speed = segment.get("speed", 1.0)
    if abs(speed - 1.0) > 0.001:
        steps.append(f"setpts=PTS/{speed}")
    steps += [
        f"scale={common.W}:{common.H}:force_original_aspect_ratio=increase:flags=lanczos",
        f"crop={common.W}:{common.H}",
        f"fps={common.FPS}",
        GRADES[segment["grade"]],
        "format=yuv420p",
    ]
    return ",".join(steps)


def render(segment: dict, force: bool) -> dict:
    target = common.SEGMENTS / f"{segment['id']}.mp4"
    stamp = common.SEGMENTS / f"{segment['id']}.json"
    digest = fingerprint(segment)

    if not force and target.exists() and stamp.exists():
        try:
            if json.loads(stamp.read_text())["fingerprint"] == digest and common.probe_media(target):
                return {**segment, "status": "cache", "file": str(target)}
        except (json.JSONDecodeError, KeyError):
            pass

    source = common.PROJECT / segment["src"]
    if not source.exists():
        return {**segment, "status": "rush-manquant", "file": None}

    cmd = [
        common.need_tool("ffmpeg"), "-y", "-v", "error",
        "-ss", f"{segment['in_point']:.6f}",
        "-t", f"{segment['source_len']:.6f}",
        "-i", str(source),
        "-an",
        "-vf", filter_chain(segment),
        "-t", f"{segment['render_len']:.6f}",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-pix_fmt", "yuv420p", "-r", str(common.FPS),
        "-video_track_timescale", "30000",
        "-movflags", "+faststart",
        str(target),
    ]
    try:
        common.run(cmd)
    except common.StepError as error:
        return {**segment, "status": f"échec: {error}", "file": None}

    info = common.probe_media(target)
    if not info:
        return {**segment, "status": "rendu illisible", "file": None}

    stamp.write_text(json.dumps({"fingerprint": digest, "duration": info["duration"]}), encoding="utf-8")
    drift = info["duration"] - segment["render_len"]
    return {**segment, "status": "ok", "file": str(target), "rendered": round(info["duration"], 4),
            "drift": round(drift, 4)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--edl", default=str(common.WORK / "edl.json"))
    parser.add_argument("--force", action="store_true", help="refait tous les segments")
    parser.add_argument("--jobs", type=int, default=min(8, (os.cpu_count() or 2)))
    parser.add_argument("--limit", type=int, help="ne rendre que les N premiers plans (test)")
    args = parser.parse_args()

    common.ensure_dirs()
    edl = common.read_json(Path(args.edl))
    segments = edl["segments"][: args.limit] if args.limit else edl["segments"]

    print(f"rendu de {len(segments)} plans sur {args.jobs} fils…")
    results: list[dict] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = {pool.submit(render, segment, args.force): segment for segment in segments}
        for done, future in enumerate(concurrent.futures.as_completed(futures), start=1):
            result = future.result()
            results.append(result)
            if done % 10 == 0 or done == len(segments):
                print(f"  {done}/{len(segments)}")

    results.sort(key=lambda r: r["index"])
    failures = [r for r in results if r["status"] not in ("ok", "cache")]
    drifts = [r for r in results if abs(r.get("drift", 0)) > 1.0 / common.FPS]

    common.write_json(common.WORK / "segments.json", {"segments": results})
    print(f"\n✓ {len(results) - len(failures)}/{len(results)} plans rendus "
          f"({sum(1 for r in results if r['status'] == 'cache')} repris du cache)")
    if drifts:
        print("⚠ écart de durée > 1 image :")
        for row in drifts[:10]:
            print(f"   {row['id']} visé {row['render_len']:.3f}s rendu {row.get('rendered')}s")
    if failures:
        for row in failures:
            print(f"✗ {row['id']} — {row['status']}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
