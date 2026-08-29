#!/usr/bin/env python3
"""Étape 2 — analyse la chanson : durée exacte, BPM, grille de temps forts.

Écrit work/beats.json. Trois moteurs, dans l'ordre : librosa, aubio, puis repli
sur une grille régulière à 92 BPM (le tempo nominal du prompt Suno).
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path

import common

FALLBACK_BPM = 92.0
WAV = common.WORK / "chanson.wav"


def extract_wav(song: Path, force: bool) -> Path:
    if WAV.exists() and not force:
        print(f"= {WAV.relative_to(common.PROJECT)} déjà extrait")
        return WAV
    common.WORK.mkdir(parents=True, exist_ok=True)
    common.run([
        common.need_tool("ffmpeg"), "-y", "-v", "error",
        "-i", str(song),
        "-vn", "-ac", "1", "-ar", "48000", "-c:a", "pcm_s16le",
        str(WAV),
    ])
    print(f"→ {WAV.relative_to(common.PROJECT)} (48 kHz mono)")
    return WAV


def beats_librosa(wav: Path) -> dict | None:
    try:
        import librosa
        import numpy as np
    except ImportError:
        return None

    y, sr = librosa.load(str(wav), sr=None, mono=True)
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    tempo, frames = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr, units="frames")
    times = librosa.frames_to_time(frames, sr=sr)
    if times.size < 4:
        return None

    strength = onset_env[np.clip(frames, 0, onset_env.size - 1)]
    peak = float(strength.max()) or 1.0
    strength = (strength / peak).astype(float)

    # Temps fort de mesure : on suppose du 4/4 et on ancre la phase sur celle des
    # quatre premières positions qui porte le plus d'énergie cumulée.
    phases = [float(strength[phase::4].sum()) for phase in range(4)]
    downbeat_phase = max(range(4), key=lambda p: phases[p])
    downbeats = [float(t) for t in times[downbeat_phase::4]]

    bpm = float(np.atleast_1d(tempo)[0])
    return {
        "engine": "librosa",
        "bpm": round(bpm, 3),
        "beats_sec": [round(float(t), 4) for t in times],
        "beat_strength": [round(float(s), 4) for s in strength],
        "downbeats_sec": [round(t, 4) for t in downbeats],
    }


def beats_aubio(wav: Path) -> dict | None:
    if not shutil.which("aubio"):
        return None
    proc = subprocess.run(["aubio", "beat", str(wav)], capture_output=True, text=True)
    if proc.returncode != 0:
        return None
    times = []
    for line in proc.stdout.split():
        try:
            times.append(round(float(line), 4))
        except ValueError:
            continue
    if len(times) < 4:
        return None
    spans = [b - a for a, b in zip(times, times[1:]) if b > a]
    median = sorted(spans)[len(spans) // 2] if spans else 60.0 / FALLBACK_BPM
    return {
        "engine": "aubio",
        "bpm": round(60.0 / median, 3) if median else FALLBACK_BPM,
        "beats_sec": times,
        "beat_strength": [1.0] * len(times),
        "downbeats_sec": times[::4],
    }


def beats_fixed(duration: float) -> dict:
    step = 60.0 / FALLBACK_BPM
    count = int(duration / step) + 1
    times = [round(i * step, 4) for i in range(count)]
    return {
        "engine": "grille-fixe",
        "bpm": FALLBACK_BPM,
        "beats_sec": times,
        "beat_strength": [1.0 if i % 4 == 0 else 0.6 for i in range(count)],
        "downbeats_sec": times[::4],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audio", help="chemin de la chanson (défaut : ./chanson.mp4 ou .mp3)")
    parser.add_argument("--force", action="store_true", help="ré-extrait le WAV même s'il existe")
    parser.add_argument("--engine", choices=("auto", "librosa", "aubio", "fixe"), default="auto")
    args = parser.parse_args()

    common.ensure_dirs()
    song = common.find_song(args.audio)
    print(f"chanson : {song.name}")
    wav = extract_wav(song, args.force)

    info = common.probe_media(wav)
    if not info:
        common.die("le WAV extrait est illisible — la chanson contient-elle bien une piste audio ?")
    duration = info["duration"]

    order = {
        "auto": (beats_librosa, beats_aubio),
        "librosa": (beats_librosa,),
        "aubio": (beats_aubio,),
        "fixe": (),
    }[args.engine]

    result = None
    for engine in order:
        result = engine(wav)
        if result:
            break
    if result is None:
        result = beats_fixed(duration)
        print("⚠ ni librosa ni aubio exploitables — repli sur une grille régulière à 92 BPM")

    # La grille ne doit jamais dépasser la fin du morceau.
    result["beats_sec"] = [t for t in result["beats_sec"] if t <= duration]
    result["beat_strength"] = result["beat_strength"][: len(result["beats_sec"])]
    result["downbeats_sec"] = [t for t in result["downbeats_sec"] if t <= duration]

    payload = {
        "source": song.name,
        "duration_sec": round(duration, 4),
        "sample_rate": 48000,
        **result,
        "beat_count": len(result["beats_sec"]),
        "downbeat_count": len(result["downbeats_sec"]),
    }
    common.write_json(common.WORK / "beats.json", payload)
    print(
        f"✓ {payload['engine']} · {payload['bpm']} BPM · {payload['beat_count']} temps · "
        f"{payload['downbeat_count']} temps forts · durée {common.timecode(duration)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
