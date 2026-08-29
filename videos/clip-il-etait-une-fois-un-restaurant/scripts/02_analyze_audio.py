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


def structure_librosa(wav: Path, parts: int) -> dict | None:
    """Repère les vraies frontières d'arrangement (entrée de la batterie, chute au pont…).

    Sans ça, les sections ne seraient que des proportions calculées sur la durée : sur un
    morceau réel, un refrain arrive rarement pile au prorata des mesures.
    """
    try:
        import librosa
        import numpy as np
    except ImportError:
        return None

    y, sr = librosa.load(str(wav), sr=22050, mono=True)
    if y.size < sr:
        return None

    # Timbre (MFCC) + harmonie (chroma) + énergie : une frontière d'arrangement bouge
    # au moins l'un des trois.
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
    rms = librosa.feature.rms(y=y)
    features = np.vstack([
        librosa.util.normalize(mfcc, axis=1),
        librosa.util.normalize(chroma, axis=1),
        librosa.util.normalize(rms, axis=1),
    ])
    frames = librosa.segment.agglomerative(features, max(2, parts))
    times = librosa.frames_to_time(frames, sr=sr)

    envelope = librosa.feature.rms(y=y, frame_length=2048, hop_length=512)[0]
    envelope_times = librosa.frames_to_time(np.arange(envelope.size), sr=sr, hop_length=512)
    step = max(1, int(envelope.size / 600))
    return {
        "structure_sec": [round(float(t), 3) for t in times if t > 0.5],
        "energy_curve": [
            [round(float(t), 2), round(float(v), 5)]
            for t, v in zip(envelope_times[::step], envelope[::step])
        ],
    }


def quiet_zones(energy_curve: list[list[float]], duration: float) -> dict:
    """Repère les passages calmes : l'intro, le pont piano/voix, l'outro.

    Ce sont les seules frontières que la chanson donne sans ambiguïté — l'arrangement
    décrit dans le prompt Suno les rend audibles (« intro : piano seul », « pont : tout
    retombe sur le piano et une voix », « outro : retour au piano seul »). Les repérer
    évite de poser le pont au prorata des mesures, à dix secondes du vrai.
    """
    if len(energy_curve) < 20:
        return {}

    times = [row[0] for row in energy_curve]
    values = [row[1] for row in energy_curve]

    # Lissage sur ~3 s : une respiration entre deux phrases n'est pas un changement de section.
    step = max(1e-6, (times[-1] - times[0]) / max(1, len(times) - 1))
    window = max(1, int(3.0 / step))
    smooth = [
        sum(values[max(0, i - window):i + window + 1]) / len(values[max(0, i - window):i + window + 1])
        for i in range(len(values))
    ]

    loud = sorted(smooth)[int(len(smooth) * 0.9)]
    threshold = loud * 0.5

    runs: list[tuple[float, float]] = []
    start = None
    for time, level in zip(times, smooth):
        if level < threshold and start is None:
            start = time
        elif level >= threshold and start is not None:
            runs.append((start, time))
            start = None
    if start is not None:
        runs.append((start, duration))

    runs = [(a, b) for a, b in runs if b - a >= 6.0]
    if not runs:
        return {}

    zones: dict = {"quiet_runs_sec": [[round(a, 3), round(b, 3)] for a, b in runs]}
    head = [run for run in runs if run[0] <= 3.0]
    if head:
        zones["intro_end_sec"] = round(head[0][1], 3)
    tail = [run for run in runs if run[1] >= duration - 3.0]
    if tail:
        zones["outro_start_sec"] = round(tail[-1][0], 3)

    # Le pont : le plus long calme qui n'est ni la tête ni la queue du morceau.
    middle = [run for run in runs if run not in head and run not in tail
              and run[0] > duration * 0.35]
    if middle:
        bridge = max(middle, key=lambda run: run[1] - run[0])
        zones["bridge_sec"] = [round(bridge[0], 3), round(bridge[1], 3)]
    return zones


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
    parser.add_argument("--parts", type=int, default=14,
                        help="nombre de frontières d'arrangement cherchées (défaut 14)")
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

    structure = structure_librosa(wav, args.parts) or {"structure_sec": [], "energy_curve": []}
    structure.update(quiet_zones(structure.get("energy_curve", []), duration))

    payload = {
        "source": song.name,
        "source_path": str(song.resolve()),
        "duration_sec": round(duration, 4),
        "sample_rate": 48000,
        **result,
        **structure,
        "beat_count": len(result["beats_sec"]),
        "downbeat_count": len(result["downbeats_sec"]),
    }
    common.write_json(common.WORK / "beats.json", payload)
    print(
        f"✓ {payload['engine']} · {payload['bpm']} BPM · {payload['beat_count']} temps · "
        f"{payload['downbeat_count']} temps forts · durée {common.timecode(duration)}"
    )
    if payload["structure_sec"]:
        marks = " ".join(common.timecode(t) for t in payload["structure_sec"])
        print(f"✓ {len(payload['structure_sec'])} frontières d'arrangement : {marks}")
    else:
        print("○ pas de détection de structure — les sections resteront proportionnelles")
    if payload.get("bridge_sec"):
        print(f"✓ pont (passage calme) : {common.timecode(payload['bridge_sec'][0])} → "
              f"{common.timecode(payload['bridge_sec'][1])}")
    if payload.get("intro_end_sec"):
        print(f"✓ fin d'intro : {common.timecode(payload['intro_end_sec'])}")
    if payload.get("outro_start_sec"):
        print(f"✓ début d'outro : {common.timecode(payload['outro_start_sec'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
