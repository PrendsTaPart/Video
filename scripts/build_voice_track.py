#!/usr/bin/env python3
"""/ep-voix / /ep-montage — Cale les répliques ElevenLabs sur leur timecode et produit une
piste audio VO unique (silence entre répliques) prête à être mixée sur le master.

Usage :
    python3 scripts/build_voice_track.py episodes/ep01-la-rentree

Entrée attendue : episodes/<ep>/voix/ep01.voix.json (timecodes + chemins des fichiers audio
générés par /ep-voix, un WAV/MP3 par réplique).
Sortie : episodes/<ep>/build/vo_mix.wav
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def parse_tc(tc: str) -> float:
    """'MM:SS.s' ou 'SS.s' -> secondes."""
    parts = tc.split(":")
    if len(parts) == 2:
        minutes, seconds = parts
        return int(minutes) * 60 + float(seconds)
    return float(parts[0])


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: build_voice_track.py <episode-dir>", file=sys.stderr)
        sys.exit(1)

    ep_dir = Path(sys.argv[1])
    voix_dir = ep_dir / "voix"
    build_dir = ep_dir / "build"
    build_dir.mkdir(parents=True, exist_ok=True)

    manifest_path = voix_dir / "ep01.voix.json"
    if not manifest_path.exists():
        print(f"❌ Introuvable : {manifest_path}", file=sys.stderr)
        sys.exit(1)

    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    repliques = data["repliques"]

    missing = [r for r in repliques if "audio_path" not in r]
    if missing:
        print(
            f"❌ {len(missing)} réplique(s) sans audio_path — lance /ep-voix (text_to_speech) "
            "avant ce script.",
            file=sys.stderr,
        )
        for r in missing:
            print(f"   - [{r['tc']}] {r['voix']}: {r['texte'][:50]}...", file=sys.stderr)
        sys.exit(1)

    total_duration = data.get("duree_totale_s", 40)

    # Construit un filtre ffmpeg adelay + amix pour positionner chaque réplique à son timecode
    filter_parts = []
    inputs = []
    for i, r in enumerate(repliques):
        audio_path = Path(r["audio_path"])
        if not audio_path.is_absolute():
            audio_path = voix_dir / audio_path
        inputs.extend(["-i", str(audio_path)])
        delay_ms = int(parse_tc(r["tc"]) * 1000)
        filter_parts.append(f"[{i}:a]adelay={delay_ms}|{delay_ms}[a{i}]")

    mix_inputs = "".join(f"[a{i}]" for i in range(len(repliques)))
    filter_complex = ";".join(filter_parts) + f";{mix_inputs}amix=inputs={len(repliques)}:normalize=0[out]"

    output = build_dir / "vo_mix.wav"
    cmd = [
        "ffmpeg", "-y",
        *inputs,
        "-filter_complex", filter_complex,
        "-map", "[out]",
        "-t", str(total_duration),
        str(output),
    ]
    print("→ " + " ".join(cmd))
    subprocess.run(cmd, check=True)
    print(f"✅ Piste VO calée : {output}")


if __name__ == "__main__":
    main()
