#!/usr/bin/env python3
"""Étape 1 — télécharge les 35 rushes Higgsfield dans ./rushes/.

Idempotent : un rush déjà présent et lisible par ffprobe n'est pas retéléchargé.
Source principale = base + file ; repli = base_cms + cms (fichier sans extension,
c'est quand même un MP4). Un rush manquant est signalé, il ne bloque pas la suite.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import subprocess
from pathlib import Path

import common

TIMEOUT_SEC = 300


def download(url: str, target: Path) -> tuple[bool, str]:
    tmp = target.with_suffix(target.suffix + ".part")
    tmp.unlink(missing_ok=True)
    cmd = [
        "curl", "-sS", "-L", "--fail",
        "--connect-timeout", "20", "--max-time", str(TIMEOUT_SEC),
        "--retry", "3", "--retry-delay", "2",
        "-o", str(tmp), url,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    if proc.returncode != 0:
        tmp.unlink(missing_ok=True)
        lines = (proc.stderr or "").strip().splitlines()
        return False, lines[-1] if lines else f"curl a rendu {proc.returncode}"
    if common.probe_media(tmp) is None:
        tmp.unlink(missing_ok=True)
        return False, "fichier téléchargé illisible par ffprobe"
    tmp.replace(target)
    return True, "ok"


def fetch_one(clip: dict, base: str, base_cms: str, force: bool) -> dict:
    ep = clip["ep"]
    target = common.RUSHES / f"{ep}.mp4"
    row = {"ep": ep, "acte": clip["acte"], "titre": clip["titre"], "source": None}

    if not force:
        info = common.probe_media(target)
        if info:
            row.update(info, source="cache", status="ok")
            return row

    attempts: list[tuple[str, str]] = [("base", base + clip["file"])]
    if clip.get("cms"):
        attempts.append(("cms", base_cms + clip["cms"]))

    errors = []
    for label, url in attempts:
        okay, message = download(url, target)
        if okay:
            info = common.probe_media(target) or {}
            row.update(info, source=label, status="ok")
            return row
        errors.append(f"{label}: {message}")

    row.update(status="manquant", error=" | ".join(errors))
    return row


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="retélécharge même si le rush est déjà valide")
    parser.add_argument("--jobs", type=int, default=6, help="téléchargements en parallèle (défaut 6)")
    parser.add_argument("--only", nargs="*", help="limiter à certains EP (ex. --only EP501 EP535)")
    args = parser.parse_args()

    common.ensure_dirs()
    manifest = common.load_manifest()
    clips = manifest["clips"]
    if args.only:
        wanted = {ep.upper() for ep in args.only}
        clips = [c for c in clips if c["ep"].upper() in wanted]

    rows: list[dict] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        futures = [
            pool.submit(fetch_one, clip, manifest["base"], manifest["base_cms"], args.force)
            for clip in clips
        ]
        for future in concurrent.futures.as_completed(futures):
            rows.append(future.result())

    rows.sort(key=lambda r: r["ep"])
    print(f"\n{'EP':7} {'acte':14} {'src':6} {'taille':>10} {'durée':>7} {'résolution':>11} {'fps':>6}  titre")
    print("-" * 104)
    for row in rows:
        if row["status"] == "ok":
            size = f"{row.get('size', 0) / 1_048_576:.1f} Mo"
            resolution = f"{row.get('width')}x{row.get('height')}"
            print(
                f"{row['ep']:7} {row['acte']:14} {row['source']:6} {size:>10} "
                f"{row.get('duration', 0):6.2f}s {resolution:>11} {str(row.get('fps')):>6}  {row['titre']}"
            )
        else:
            print(f"{row['ep']:7} {row['acte']:14} {'—':6} {'MANQUANT':>10}  {row.get('error', '')}")

    missing = [r for r in rows if r["status"] != "ok"]
    common.write_json(common.WORK / "rushes.json", {"rushes": rows, "missing": [r["ep"] for r in missing]})
    print(f"\n{len(rows) - len(missing)}/{len(rows)} rushes disponibles.")
    if missing:
        print(f"⚠ manquants (ignorés au montage) : {', '.join(r['ep'] for r in missing)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
