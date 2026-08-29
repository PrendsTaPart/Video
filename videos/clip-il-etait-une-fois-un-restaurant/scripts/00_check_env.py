#!/usr/bin/env python3
"""Étape 0 — vérifie l'outillage et crée l'arborescence de travail."""

from __future__ import annotations

import importlib.util
import shutil
import sys

import common


def main() -> int:
    ok = True
    for tool in ("ffmpeg", "ffprobe", "curl"):
        path = shutil.which(tool)
        print(f"{'✓' if path else '✗'} {tool:8s} {path or 'INTROUVABLE'}")
        ok = ok and bool(path)

    for module, role in (("librosa", "détection BPM/temps forts"), ("soundfile", "lecture WAV")):
        found = importlib.util.find_spec(module) is not None
        mark = "✓" if found else "○"
        note = "" if found else " (optionnel — repli aubio puis grille fixe 92 BPM)"
        print(f"{mark} {module:8s} {role}{note}")

    common.ensure_dirs()
    print(f"✓ dossiers   rushes/ work/ work/segments/ out/ prêts dans {common.PROJECT.name}/")

    if not ok:
        print("\n✗ ffmpeg/ffprobe sont obligatoires : apt-get install -y ffmpeg", file=sys.stderr)
        return 1
    print("\n✓ environnement prêt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
