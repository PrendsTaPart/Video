#!/usr/bin/env python3
"""Enchaîne les sept étapes. Chaque script reste jouable seul.

    python3 scripts/run_all.py                    # tout
    python3 scripts/run_all.py --from 03          # reprendre au montage
    python3 scripts/run_all.py --audio ma-chanson.mp3
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import common

STEPS = [
    ("00", "00_check_env.py", ()),
    ("01", "01_fetch_rushes.py", ()),
    ("02", "02_analyze_audio.py", ("audio",)),
    ("03", "03_build_edl.py", ()),
    ("04", "04_render_segments.py", ()),
    ("05", "05_assemble.py", ("audio",)),
    ("06", "06_exports.py", ()),
    ("07", "07_verify.py", ()),
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--from", dest="start", default="00", help="première étape à jouer (00→07)")
    parser.add_argument("--to", dest="stop", default="07", help="dernière étape à jouer")
    parser.add_argument("--audio", help="chemin de la chanson")
    parser.add_argument("--force", action="store_true", help="ignore les caches (rushes, segments)")
    args = parser.parse_args()

    here = Path(__file__).resolve().parent
    for number, script, accepts in STEPS:
        if not (args.start <= number <= args.stop):
            continue
        cmd = [sys.executable, str(here / script)]
        if "audio" in accepts and args.audio:
            cmd += ["--audio", args.audio]
        if args.force and script in ("01_fetch_rushes.py", "04_render_segments.py"):
            cmd.append("--force")
        print(f"\n{'═' * 70}\n▶ étape {number} — {script}\n{'═' * 70}")
        result = subprocess.run(cmd)
        if result.returncode != 0:
            print(f"\n✗ étape {number} en échec (code {result.returncode}) — chaîne interrompue.",
                  file=sys.stderr)
            return result.returncode
    print(f"\n✓ chaîne terminée. Résultats dans {common.OUT.relative_to(common.PROJECT.parent)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
