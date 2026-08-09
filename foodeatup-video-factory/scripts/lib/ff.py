"""Helpers ffmpeg/ffprobe partagés par les scripts 00 → 04.

Aucune dépendance externe : stdlib uniquement. Tous les appels média passent par
ffmpeg local — aucune API payante n'est utilisée pour le montage.
"""

from __future__ import annotations

import json
import os
import re
import shlex
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Profil de normalisation commun (SPEC §3.1) — indispensable pour que le
# démuxeur `concat` recolle les segments sans artefact.
VCODEC = ["-c:v", "libx264", "-profile:v", "high", "-level", "4.1",
          "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p"]
ACODEC = ["-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2"]
TIMESCALE = ["-video_track_timescale", "30000"]


class FFError(RuntimeError):
    pass


def run(cmd, *, capture=True, check=True):
    """Exécute une commande et renvoie (returncode, stdout+stderr)."""
    proc = subprocess.run(
        cmd,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.STDOUT if capture else None,
        text=True,
    )
    out = proc.stdout or ""
    if check and proc.returncode != 0:
        raise FFError(
            f"commande échouée ({proc.returncode}):\n  {shlex.join(cmd)}\n{out[-4000:]}"
        )
    return proc.returncode, out


def ffmpeg(args, **kw):
    return run(["ffmpeg", "-hide_banner", "-nostdin", "-y", *args], **kw)


def ffprobe_json(path: Path, *entries: str) -> dict:
    code, out = run([
        "ffprobe", "-v", "error", "-print_format", "json",
        "-show_format", "-show_streams", str(path),
    ])
    return json.loads(out)


def duration(path: Path) -> float:
    """Durée du conteneur, en secondes."""
    code, out = run([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=nw=1:nk=1", str(path),
    ])
    try:
        return float(out.strip().splitlines()[-1])
    except (ValueError, IndexError):
        raise FFError(f"durée illisible pour {path}: {out!r}")


def video_stream(path: Path) -> dict | None:
    for s in ffprobe_json(path).get("streams", []):
        if s.get("codec_type") == "video":
            return s
    return None


def has_audio(path: Path) -> bool:
    return any(s.get("codec_type") == "audio"
               for s in ffprobe_json(path).get("streams", []))


def frames(path: Path) -> int:
    """Nombre exact d'images de la piste vidéo (comptage réel, pas nb_frames)."""
    code, out = run([
        "ffprobe", "-v", "error", "-select_streams", "v:0",
        "-count_frames", "-show_entries", "stream=nb_read_frames",
        "-of", "default=nw=1:nk=1", str(path),
    ])
    return int(out.strip().splitlines()[-1])


# --------------------------------------------------------------------------
# Normalisation / découpe
# --------------------------------------------------------------------------

def exact_cut(seconds: float, fps: int) -> list[str]:
    """Options ffmpeg qui bornent la sortie à EXACTEMENT N images.

    `-t` seul ne suffit pas : il garde les images de pts < t, et les arrondis
    flottants font passer une image de trop une fois sur deux (constaté sur les
    sous-plans de 2,3667 s). `-frames:v` plafonne la vidéo au compte exact,
    `-t` borne l'audio sur la même durée.
    """
    n = round(seconds * fps)
    return ["-frames:v", str(n), "-t", f"{n / fps:.5f}"]


def normalize(src: Path, dst: Path, *, width: int, height: int, fps: int,
              seconds: float | None = None, ss: float | None = None,
              extra_vf: str = "", loop_still: bool = False) -> Path:
    """Passe un média au profil commun (SPEC §3.1).

    - recadrage `increase` + `crop` centré → jamais de bandes noires,
    - `fps` forcé pour que les durées tombent sur un nombre entier d'images,
    - piste audio silencieuse ajoutée si la source n'en a pas.
    """
    dst.parent.mkdir(parents=True, exist_ok=True)
    chain = [f"scale={width}:{height}:force_original_aspect_ratio=increase",
             f"crop={width}:{height}", f"fps={fps}"]
    if extra_vf:
        chain.append(extra_vf)
    chain.append("format=yuv420p")
    vf = ",".join(chain)

    args: list[str] = []
    if loop_still:
        args += ["-loop", "1"]
    if ss is not None:
        args += ["-ss", f"{ss:.3f}"]
    args += ["-i", str(src)]

    silent = not has_audio(src) or loop_still
    if silent:
        args += ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo"]

    args += ["-vf", vf, "-map", "0:v:0"]
    args += ["-map", "1:a:0" if silent else "0:a:0"]
    if seconds is not None:
        args += exact_cut(seconds, fps)
    args += [*VCODEC, *ACODEC, *TIMESCALE, "-avoid_negative_ts", "make_zero",
             "-af", "aresample=async=1:first_pts=0", str(dst)]
    ffmpeg(args)
    return dst


def freeze_pad(src: Path, dst: Path, *, seconds: float, width: int, height: int,
               fps: int) -> Path:
    """Allonge un segment trop court en tenant sa dernière image (SPEC §2.3).

    On étire le plan vidéo plutôt que d'accélérer la voix.
    """
    d = duration(src)
    if d >= seconds - 1e-3:
        return normalize(src, dst, width=width, height=height, fps=fps,
                         seconds=seconds)
    pad = seconds - d
    ffmpeg([
        "-i", str(src),
        "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
        "-filter_complex",
        f"[0:v]tpad=stop_mode=clone:stop_duration={pad:.4f},fps={fps},"
        f"format=yuv420p[v]",
        "-map", "[v]", "-map", "1:a:0", *exact_cut(seconds, fps),
        *VCODEC, *ACODEC, *TIMESCALE, str(dst),
    ])
    return dst


def concat(segments: list[Path], dst: Path, workdir: Path) -> Path:
    """Concaténation sans réencodage (démuxeur concat)."""
    workdir.mkdir(parents=True, exist_ok=True)
    listfile = workdir / f"{dst.stem}_concat.txt"
    listfile.write_text(
        "".join(f"file '{s.resolve()}'\n" for s in segments), encoding="utf-8"
    )
    ffmpeg(["-f", "concat", "-safe", "0", "-i", str(listfile),
            "-c", "copy", str(dst)])
    return dst


# --------------------------------------------------------------------------
# Mesures / contrôle qualité
# --------------------------------------------------------------------------

_LOUDNORM_KEYS = ("input_i", "input_tp", "input_lra", "input_thresh",
                  "target_offset")


def measure_loudness(path: Path, *, target_i=-14.0, target_tp=-1.0,
                     target_lra=9.0) -> dict:
    """Passe 1 de loudnorm : renvoie les mesures JSON."""
    code, out = ffmpeg([
        "-i", str(path), "-af",
        f"loudnorm=I={target_i}:TP={target_tp}:LRA={target_lra}:"
        f"print_format=json",
        "-f", "null", "-",
    ])
    blocks = re.findall(r"\{[^{}]*\"input_i\"[^{}]*\}", out, re.S)
    if not blocks:
        raise FFError(f"loudnorm n'a rien mesuré sur {path}")
    return json.loads(blocks[-1])


def loudnorm_filter(measured: dict, *, target_i=-14.0, target_tp=-1.0,
                    target_lra=9.0) -> str:
    """Passe 2 : filtre loudnorm linéaire calé sur les mesures de la passe 1.

    Le loudnorm simple passe est un compresseur dynamique approximatif ; en deux
    passes on tombe à ±0,3 LUFS de la cible, ce qui fait passer le test QA.
    """
    m = {k: measured[k] for k in _LOUDNORM_KEYS}
    return (f"loudnorm=I={target_i}:TP={target_tp}:LRA={target_lra}:"
            f"measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
            f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:"
            f"offset={m['target_offset']}:linear=true:print_format=summary")


def loudness_report(path: Path) -> dict:
    """Mesure I / TP / LRA d'un fichier fini (contrôle QA)."""
    m = measure_loudness(path)
    return {
        "input_i": float(m["input_i"]),
        "input_tp": float(m["input_tp"]),
        "input_lra": float(m["input_lra"]),
    }


def frame_luma(path: Path, t: float) -> float:
    """Luminance moyenne (YAVG) de l'image à l'instant t."""
    code, out = ffmpeg([
        "-ss", f"{t:.3f}", "-i", str(path), "-frames:v", "1",
        "-vf", "signalstats,metadata=print:file=-", "-f", "null", "-",
    ])
    vals = re.findall(r"lavfi\.signalstats\.YAVG=([0-9.]+)", out)
    if not vals:
        raise FFError(f"signalstats muet sur {path} @ {t}s")
    return float(vals[-1])


def region_delta(a: Path, b: Path, t: float, crop: str) -> float:
    """Écart moyen entre deux vidéos sur une région, à l'instant t.

    Sert au test « logo présent » : on compare le master AVANT et APRÈS
    incrustation. Dans la zone du logo l'écart doit être franc, ailleurs nul.
    C'est déterministe et ça n'exige aucune bibliothèque d'image.
    """
    code, out = ffmpeg([
        "-ss", f"{t:.3f}", "-i", str(a),
        "-ss", f"{t:.3f}", "-i", str(b),
        "-filter_complex",
        f"[0:v]crop={crop},format=gray[x];[1:v]crop={crop},format=gray[y];"
        f"[x][y]blend=all_mode=difference,signalstats,metadata=print:file=-",
        "-frames:v", "1", "-f", "null", "-",
    ])
    vals = re.findall(r"lavfi\.signalstats\.YAVG=([0-9.]+)", out)
    if not vals:
        raise FFError(f"comparaison de zone impossible ({a} / {b} @ {t}s)")
    return float(vals[-1])


def audio_rms(path: Path) -> float:
    """Niveau RMS global en dBFS (test « audio non muet »)."""
    code, out = ffmpeg([
        "-i", str(path), "-af", "astats=metadata=1:reset=0", "-f", "null", "-",
    ])
    vals = re.findall(r"Overall[\s\S]*?RMS level dB:\s*(-?[0-9.]+|-inf)", out)
    if not vals:
        vals = re.findall(r"RMS level dB:\s*(-?[0-9.]+|-inf)", out)
    if not vals:
        raise FFError(f"astats muet sur {path}")
    v = vals[-1]
    return float("-inf") if v == "-inf" else float(v)


# --------------------------------------------------------------------------
# Divers
# --------------------------------------------------------------------------

def split_seconds(total: float, fps: int, n: int) -> list[float]:
    """Découpe `total` en `n` durées qui tombent sur un nombre entier d'images.

    9,5 s ÷ 4 = 2,375 s = 71,25 images : arrondir chaque part indépendamment
    fait dériver la somme. On répartit le reste sur les premières parts, ce qui
    garantit que le bloc rendu fait exactement `total`.
    """
    total_f = round(total * fps)
    base, rem = divmod(total_f, n)
    return [(base + (1 if i < rem else 0)) / fps for i in range(n)]


def ass_escape(text: str) -> str:
    """Échappe un texte pour un champ Dialogue ASS."""
    return (text.replace("\\", "\\\\")
                .replace("{", "\\{")
                .replace("}", "\\}")
                .replace("\n", "\\N"))


def filter_escape(path: str | Path) -> str:
    """Échappe un chemin utilisé DANS un filtre ffmpeg (ass=…, subtitles=…)."""
    s = str(path)
    return s.replace("\\", "/").replace(":", "\\:").replace("'", "\\'")


def load_config(path: Path | None = None) -> dict:
    cfg = path or (ROOT / "config" / "episodes.json")
    with open(cfg, encoding="utf-8") as fh:
        return json.load(fh)


def episode(cfg: dict, ep_id: str) -> dict:
    for ep in cfg["episodes"]:
        if ep["id"].upper() == ep_id.upper():
            return ep
    raise KeyError(f"épisode inconnu: {ep_id}")


def log(msg: str, *, err: bool = False) -> None:
    print(msg, file=sys.stderr if err else sys.stdout, flush=True)
