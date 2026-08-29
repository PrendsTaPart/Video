"""Socle commun aux étapes du clip « Il était une fois un restaurant ».

Chemins, appels ffmpeg/ffprobe, lecture du manifeste. Aucun effet de bord à
l'import : chaque script d'étape reste exécutable seul.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
RUSHES = PROJECT / "rushes"
WORK = PROJECT / "work"
OUT = PROJECT / "out"
SEGMENTS = WORK / "segments"
MANIFEST = PROJECT / "manifest.json"
STRUCTURE = PROJECT / "song-structure.json"

# Format de sortie — vertical, imposé par la destination (TikTok / Reels / Shorts).
W, H, FPS = 1080, 1920, 30

ACTES_FROIDS = {"avant-cuisine", "avant-salle", "avant-bureau", "avant-client"}


class StepError(RuntimeError):
    """Erreur bloquante d'une étape : message lisible, pas de traceback."""


def die(message: str) -> "None":
    print(f"✗ {message}", file=sys.stderr)
    raise SystemExit(1)


def need_tool(name: str) -> str:
    path = shutil.which(name)
    if not path:
        die(f"{name} est introuvable. Sur Debian/Ubuntu : apt-get install -y ffmpeg")
    return path


def run(cmd: list[str], *, check: bool = True, quiet: bool = True) -> subprocess.CompletedProcess:
    """Lance une commande et renvoie le CompletedProcess (stderr capturé)."""
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        errors="replace",
    )
    if check and proc.returncode != 0:
        tail = "\n".join((proc.stderr or "").strip().splitlines()[-12:])
        raise StepError(f"échec de {cmd[0]} (code {proc.returncode})\n{tail}")
    if not quiet and proc.stderr:
        print(proc.stderr, file=sys.stderr)
    return proc


def ffprobe_json(path: Path, *streams: str) -> dict:
    args = [
        need_tool("ffprobe"), "-v", "error",
        "-print_format", "json",
        "-show_format", "-show_streams",
        str(path),
    ]
    proc = run(args)
    return json.loads(proc.stdout)


def probe_media(path: Path) -> dict | None:
    """Renvoie {duration, width, height, fps, has_video, has_audio, size} ou None si illisible."""
    if not path.exists() or path.stat().st_size == 0:
        return None
    try:
        data = ffprobe_json(path)
    except (StepError, json.JSONDecodeError):
        return None
    video = next((s for s in data.get("streams", []) if s.get("codec_type") == "video"), None)
    audio = next((s for s in data.get("streams", []) if s.get("codec_type") == "audio"), None)
    duration = None
    for candidate in (data.get("format", {}).get("duration"), (video or {}).get("duration")):
        try:
            duration = float(candidate)
            break
        except (TypeError, ValueError):
            continue
    if duration is None or duration <= 0:
        return None
    fps = None
    if video:
        rate = video.get("avg_frame_rate") or video.get("r_frame_rate") or "0/0"
        try:
            num, _, den = rate.partition("/")
            fps = round(float(num) / float(den), 3) if float(den) else None
        except (ValueError, ZeroDivisionError):
            fps = None
    return {
        "duration": duration,
        "width": (video or {}).get("width"),
        "height": (video or {}).get("height"),
        "fps": fps,
        "has_video": video is not None,
        "has_audio": audio is not None,
        "size": path.stat().st_size,
    }


def load_manifest() -> dict:
    if not MANIFEST.exists():
        die(f"manifeste introuvable : {MANIFEST}")
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def load_structure() -> dict:
    if not STRUCTURE.exists():
        die(f"structure de chanson introuvable : {STRUCTURE}")
    return json.loads(STRUCTURE.read_text(encoding="utf-8"))


def read_json(path: Path) -> dict:
    if not path.exists():
        die(f"fichier attendu manquant : {path} (étape précédente non jouée ?)")
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"→ {path.relative_to(PROJECT)}")


def find_song(explicit: str | None = None) -> Path:
    """Localise la chanson : --audio, puis ./chanson.{mp4,mp3,wav,m4a,aac,flac}."""
    if explicit:
        path = Path(explicit)
        if not path.is_absolute():
            path = (PROJECT / path).resolve()
        if not path.exists():
            die(f"chanson introuvable : {path}")
        return path
    for name in ("chanson.mp4", "chanson.mp3", "chanson.wav", "chanson.m4a", "chanson.aac", "chanson.flac"):
        candidate = PROJECT / name
        if candidate.exists():
            return candidate
    die(
        "aucune chanson trouvée. Dépose le fichier Suno dans "
        f"{PROJECT.name}/ sous le nom chanson.mp4 (ou chanson.mp3), ou passe --audio <chemin>."
    )


def timecode(seconds: float) -> str:
    seconds = max(0.0, float(seconds))
    minutes, sec = divmod(seconds, 60)
    return f"{int(minutes):02d}:{sec:06.3f}"


def ensure_dirs() -> None:
    for directory in (RUSHES, WORK, OUT, SEGMENTS):
        directory.mkdir(parents=True, exist_ok=True)
