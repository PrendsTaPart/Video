#!/usr/bin/env python3
"""Découpe un bloc de voix off groupées aux silences longs.

ElevenLabs limite le nombre de générations simultanées ; générer les répliques par blocs de
cinq, séparées par de longues pauses, puis découper ici, divise le nombre d'appels par cinq.

    python3 split_vo.py assets/vo/blocA.mp3 S04 S05 S06 S07 S08
"""
import re
import subprocess
import sys
from pathlib import Path

FF = "ffmpeg"


def silences(path, noise="-40dB", mindur=0.9):
    out = subprocess.run([FF, "-i", str(path), "-af", f"silencedetect=noise={noise}:d={mindur}", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    starts = [float(m) for m in re.findall(r"silence_start: ([\d.]+)", out)]
    ends = [float(m) for m in re.findall(r"silence_end: ([\d.]+)", out)]
    return list(zip(starts, ends))


def dur(path):
    out = subprocess.run([FF, "-i", str(path)], capture_output=True, text=True).stderr
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", out)
    return int(m[2]) * 60 + float(m[3])


def split(src, names, noise="-40dB", mindur=0.9, pad=0.25):
    src = Path(src)
    gaps = silences(src, noise, mindur)
    total = dur(src)
    if len(gaps) != len(names) - 1:
        raise SystemExit(f"{src.name} : {len(gaps)} silence(s) pour {len(names)} répliques attendues — "
                         f"ajuster noise/mindur ou régénérer le bloc")
    bounds, prev = [], 0.0
    for (s, e) in gaps:
        bounds.append((prev, s + pad))
        prev = e - pad
    bounds.append((prev, total))
    for (a, b), n in zip(bounds, names):
        out = src.parent / f"{n}.mp3"
        subprocess.run([FF, "-y", "-loglevel", "error", "-ss", f"{max(0, a):.3f}", "-to", f"{b:.3f}",
                        "-i", str(src), "-c", "copy", str(out)], check=True)
        print(f"{n}.mp3  {b - a:5.2f}s")


if __name__ == "__main__":
    split(sys.argv[1], sys.argv[2:])
