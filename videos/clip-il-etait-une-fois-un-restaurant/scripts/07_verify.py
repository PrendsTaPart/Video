#!/usr/bin/env python3
"""Étape 7 — contrôle les exports (ffprobe) et écrit out/RAPPORT.md."""

from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path

import common

EXPECTED = {
    "clip-9x16.mp4": (1080, 1920, True),
    "clip-1x1.mp4": (1080, 1080, True),
    "clip-16x9.mp4": (1920, 1080, True),
    "clip-teaser-30s.mp4": (1080, 1920, True),
}


def check_exports(edl: dict) -> tuple[list[dict], bool]:
    rows: list[dict] = []
    ok = True
    for name, (width, height, needs_audio) in EXPECTED.items():
        path = common.OUT / name
        info = common.probe_media(path)
        problems = []
        if not info:
            problems.append("illisible ou absent")
        else:
            if (info["width"], info["height"]) != (width, height):
                problems.append(f"résolution {info['width']}x{info['height']} au lieu de {width}x{height}")
            if needs_audio and not info["has_audio"]:
                problems.append("pas de piste audio")
            if name == "clip-9x16.mp4" and abs(info["duration"] - edl["duration_sec"]) > 0.2:
                problems.append(f"durée {info['duration']:.2f}s ≠ chanson {edl['duration_sec']:.2f}s")
        rows.append({"name": name, "info": info, "problems": problems})
        ok = ok and not problems

    vignette = common.OUT / "vignette.jpg"
    rows.append({
        "name": "vignette.jpg",
        "info": {"size": vignette.stat().st_size} if vignette.exists() else None,
        "problems": [] if vignette.exists() else ["absente"],
    })
    ok = ok and vignette.exists()
    return rows, ok


def write_report(edl: dict, rows: list[dict]) -> Path:
    sections = {s["id"]: s for s in edl["sections"]}
    lines: list[str] = []
    add = lines.append

    add("# Clip « Il était une fois un restaurant » — rapport de montage")
    add("")
    add(f"- Chanson : `{edl['song']}` · {edl['duration_sec']:.2f} s "
        f"({common.timecode(edl['duration_sec'])})")
    add(f"- Tempo détecté : {edl['bpm']} BPM (moteur : {edl['beat_engine']})")
    add(f"- Format master : {edl['width']}×{edl['height']}, {edl['fps']} i/s")
    add(f"- Plans montés : {len(edl['segments'])} · fondus d'acte : "
        f"{sum(1 for s in edl['segments'] if s['transition_out'] == 'xfade')} × {edl['xfade_sec']} s")
    if edl.get("missing_rushes"):
        add(f"- ⚠ Rushes manquants (sautés) : {', '.join(edl['missing_rushes'])}")
    add(f"- Généré le {dt.date.today().isoformat()}")
    add("")

    add("## Structure")
    add("")
    add("| Section | Début | Fin | Durée | Plans |")
    add("|---|---|---|---|---|")
    for section in edl["sections"]:
        count = sum(1 for s in edl["segments"] if s["section"] == section["id"])
        add(f"| {section['label']} | {common.timecode(section['start'])} | "
            f"{common.timecode(section['end'])} | {section['duration']:.2f} s | {count} |")
    add("")

    add("## Ordre des plans")
    add("")
    add("| # | Timecode | Durée | Plan | Acte | Étalonnage | Entrée rush | Vitesse | Sortie | Titre |")
    add("|---|---|---|---|---|---|---|---|---|---|")
    for segment in edl["segments"]:
        speed = "—" if segment["speed"] == 1.0 else f"{segment['speed']}×"
        add(f"| {segment['index']} | {common.timecode(segment['start'])} | {segment['len']:.2f} s | "
            f"{segment['ep']} | {segment['acte']} | {segment['grade']} | {segment['in_point']:.2f} s | "
            f"{speed} | {segment['transition_out']} | {segment['titre']} |")
    add("")

    add("## Exports")
    add("")
    add("| Fichier | Résolution | Durée | Audio | Poids | État |")
    add("|---|---|---|---|---|---|")
    for row in rows:
        info = row["info"]
        if row["name"].endswith(".jpg"):
            weight = f"{info['size'] / 1024:.0f} ko" if info else "—"
            state = "✓" if not row["problems"] else "✗ " + " ; ".join(row["problems"])
            add(f"| `{row['name']}` | — | — | — | {weight} | {state} |")
            continue
        if not info:
            add(f"| `{row['name']}` | — | — | — | — | ✗ {' ; '.join(row['problems'])} |")
            continue
        state = "✓" if not row["problems"] else "✗ " + " ; ".join(row["problems"])
        add(f"| `{row['name']}` | {info['width']}×{info['height']} | {info['duration']:.2f} s | "
            f"{'oui' if info['has_audio'] else 'non'} | {info['size'] / 1_048_576:.1f} Mo | {state} |")
    add("")

    add("## Reproduire ce montage")
    add("")
    add("```bash")
    add("python3 scripts/run_all.py            # tout, de bout en bout")
    add("python3 scripts/03_build_edl.py       # rejouer seulement le montage")
    add("```")
    add("")

    report = common.OUT / "RAPPORT.md"
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--edl", default=str(common.WORK / "edl.json"))
    args = parser.parse_args()

    edl = common.read_json(Path(args.edl))
    rows, ok = check_exports(edl)

    print(f"{'fichier':24} {'résolution':>12} {'durée':>9} {'audio':>6}  état")
    print("-" * 72)
    for row in rows:
        info = row["info"] or {}
        resolution = f"{info.get('width')}x{info.get('height')}" if info.get("width") else "—"
        duration = f"{info['duration']:.2f}s" if info.get("duration") else "—"
        audio = ("oui" if info.get("has_audio") else "non") if info.get("duration") else "—"
        state = "✓" if not row["problems"] else "✗ " + " ; ".join(row["problems"])
        print(f"{row['name']:24} {resolution:>12} {duration:>9} {audio:>6}  {state}")

    report = write_report(edl, rows)
    print(f"\n→ {report.relative_to(common.PROJECT)}")
    if not ok:
        print("\n✗ au moins un export est incomplet.")
        return 1
    print("✓ tous les exports sont conformes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
