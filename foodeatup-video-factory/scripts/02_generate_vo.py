#!/usr/bin/env python3
"""02 — Voix off ElevenLabs (7 blocs communs + 30 punchlines).

Règles de coût, non négociables :
  * un MP3 déjà présent sur le disque n'est JAMAIS regénéré sans `--force` ;
  * les blocs B/C/D/E sont communs aux 30 épisodes → générés une seule fois ;
  * seule la punchline change d'un épisode à l'autre.

Deux modes d'exécution, selon ce qui est disponible :
  * `ELEVENLABS_API_KEY` dans l'environnement ou `config/secrets.env`
    → appel HTTP direct (stdlib), tout se fait ici ;
  * sinon → le script écrit `build/vo_jobs.json` avec les textes manquants et
    s'arrête. L'agent passe les `ElevenLabs:text_to_speech` correspondants et
    relance le script pour la mesure et la normalisation.

Calage (SPEC §2.3) : après génération on mesure la durée réelle. Écart > 8 % de
la cible → nouvelle tentative avec `speed` +0,05 (2 essais, plafond 1,15).
Au-delà, on log un avertissement : c'est le plan vidéo qui sera étiré à
l'assemblage, pas la voix qui sera accélérée davantage.

Usage :
    python scripts/02_generate_vo.py                 # commun + les 30 punchlines
    python scripts/02_generate_vo.py --episode EP01  # commun + EP01
    python scripts/02_generate_vo.py --force         # regénère tout (coûteux)
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ff  # noqa: E402

ROOT = ff.ROOT
VOICES = ROOT / "config" / "voices.json"
SECRETS = ROOT / "config" / "secrets.env"
API = "https://api.elevenlabs.io/v1/text-to-speech"

TOLERANCE = 0.08          # 8 % — au-delà on retente
SPEED_STEP = 0.05
SPEED_MAX = 1.15
MAX_RETRY = 2

# Textes VERBATIM de 02-VOIX-ELEVENLABS.md. Ne pas réécrire : ce sont les
# sources de vérité, la cible est la durée visée dans la timeline.
COMMON: list[tuple[str, str, float]] = [
    ("B-sting", "Foude Ate Up.", 1.2),
    ("C-probleme-30",
     "Aujourd'hui, tu gères ton restaurant avec dix logiciels. "
     "Mille euros par mois. Et aucun ne se parle.", 7.0),
    ("C-probleme-45",
     "Aujourd'hui, tu gères ton restaurant avec dix logiciels différents. "
     "Mille euros par mois. Et aucun ne communique avec les autres. "
     "Ta caisse ignore ton stock. Ton site ignore ta cuisine. Oublie tout ça.",
     11.5),
    ("D-demo-30",
     "Regarde. En un clic, ton site est prêt à vendre. Et il parle à ta "
     "caisse, à ton KDS, et il fait entrer le client dans ta boucle "
     "marketing.", 9.0),
    ("D-demo-45",
     "Regarde. En un clic, ton site est prêt à vendre tes produits. Et le "
     "petit plus : il communique avec ton logiciel de caisse et ton KDS. "
     "Chaque commande fait entrer le client dans ta boucle marketing, "
     "automatiquement.", 12.5),
    ("E-closing-30",
     "Avant, pendant, après le service. Prêt à augmenter ton chiffre "
     "d'affaires ?", 3.8),
    ("E-closing-45",
     "FoodEatUp pilote ton restaurant avant, pendant et après le service. "
     "Alors, prêt à augmenter ton chiffre d'affaires ?", 4.8),
]


def load_secrets() -> None:
    if not SECRETS.exists():
        return
    for line in SECRETS.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def load_voice() -> dict:
    if not VOICES.exists():
        raise SystemExit(
            f"NO_VOICE_CONFIG {VOICES} absent.\n"
            "Renseigne-le à partir de config/voices.example.json : l'ID doit "
            "venir d'un appel réel à la liste des voix ElevenLabs — n'invente "
            "jamais un voice_id."
        )
    cfg = json.loads(VOICES.read_text(encoding="utf-8"))
    if not cfg.get("voice_id"):
        raise SystemExit(
            "NO_VOICE_ID config/voices.json — appelle la liste des voix "
            "ElevenLabs, propose 3 voix françaises à l'humain, écris son choix."
        )
    return cfg


def tts_http(text: str, dst: Path, voice: dict, speed: float) -> None:
    key = os.environ["ELEVENLABS_API_KEY"]
    settings = dict(voice.get("settings", {}))
    settings["speed"] = round(speed, 3)
    body = json.dumps({
        "text": text,
        "model_id": voice.get("model_id", "eleven_multilingual_v2"),
        "voice_settings": settings,
    }).encode("utf-8")
    req = urllib.request.Request(
        f"{API}/{voice['voice_id']}",
        data=body,
        headers={"xi-api-key": key, "Content-Type": "application/json",
                 "Accept": "audio/mpeg"},
    )
    dst.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(req, timeout=180) as resp:
        dst.write_bytes(resp.read())


def normalize_vo(path: Path) -> None:
    """loudnorm I=-16 TP=-1.5 LRA=11 (SPEC §2.4), en place."""
    tmp = path.with_suffix(".norm.mp3")
    ff.ffmpeg(["-i", str(path), "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
               "-c:a", "libmp3lame", "-b:a", "192k", str(tmp)])
    tmp.replace(path)


def produce(name: str, text: str, target: float, dst: Path, voice: dict,
            *, force: bool, jobs: list) -> dict:
    """Génère si nécessaire, mesure, recale. Renvoie l'entrée de journal."""
    entry = {"name": name, "path": str(dst.relative_to(ROOT)),
             "target_s": target, "chars": len(text)}

    if dst.exists() and not force:
        entry["status"] = "skip"
        entry["duration_s"] = round(ff.duration(dst), 3)
        entry["delta_pct"] = round(
            (entry["duration_s"] - target) / target * 100, 1)
        return entry

    if not os.environ.get("ELEVENLABS_API_KEY"):
        jobs.append({"name": name, "text": text, "target_s": target,
                     "out": str(dst.relative_to(ROOT)),
                     "voice_id": voice["voice_id"],
                     "model_id": voice.get("model_id",
                                           "eleven_multilingual_v2")})
        entry["status"] = "pending_mcp"
        return entry

    speed = float(voice.get("speed", 1.0))
    attempt = 0
    while True:
        tts_http(text, dst, voice, speed)
        normalize_vo(dst)
        got = ff.duration(dst)
        delta = (got - target) / target
        entry.update(duration_s=round(got, 3), speed=round(speed, 3),
                     delta_pct=round(delta * 100, 1))
        # Seul le dépassement pose problème : plus court, on laisse respirer.
        if delta <= TOLERANCE or attempt >= MAX_RETRY or speed >= SPEED_MAX:
            break
        speed = min(SPEED_MAX, speed + SPEED_STEP)
        attempt += 1
        ff.log(f"       {name}: {got:.2f}s vs {target:.2f}s "
               f"→ nouvelle passe à speed={speed:.2f}")

    if entry["delta_pct"] > TOLERANCE * 100:
        entry["status"] = "over_target"
        ff.log(f"  WARN VO_TOO_LONG {name} {entry['duration_s']}s vs "
               f"{target}s — le plan vidéo sera étiré à l'assemblage", err=True)
    else:
        entry["status"] = "generated"
    return entry


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--episode", action="append",
                    help="limite aux punchlines de ces épisodes (répétable)")
    ap.add_argument("--force", action="store_true",
                    help="regénère même les MP3 déjà présents (coûteux)")
    args = ap.parse_args()

    load_secrets()
    cfg = ff.load_config()
    voice = load_voice()
    jobs: list = []
    journal: list = []

    ff.log("VO communes (générées une seule fois) :")
    for name, text, target in COMMON:
        dst = ROOT / "vo" / "common" / f"{name}.mp3"
        e = produce(name, text, target, dst, voice, force=args.force, jobs=jobs)
        journal.append(e)
        ff.log(f"  {e['status']:<12} {name:<16} {e.get('duration_s', '—')}s "
               f"(cible {target}s)")

    wanted = {x.upper() for x in args.episode} if args.episode else None
    ff.log("\nPunchlines :")
    for ep in cfg["episodes"]:
        if wanted and ep["id"] not in wanted:
            continue
        dst = ROOT / "vo" / "punch" / f"{ep['id']}.mp3"
        # Cible : la punchline doit tenir sur le beat comique du hook.
        target = max(1.6, len(ep["punchline"]) / 15.0)
        e = produce(ep["id"], ep["punchline"], target, dst, voice,
                    force=args.force, jobs=jobs)
        journal.append(e)
        ff.log(f"  {e['status']:<12} {ep['id']:<16} "
               f"{e.get('duration_s', '—')}s")

    (ROOT / "build").mkdir(exist_ok=True)
    (ROOT / "build" / "vo_report.json").write_text(
        json.dumps(journal, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")

    if jobs:
        p = ROOT / "build" / "vo_jobs.json"
        p.write_text(json.dumps(jobs, indent=2, ensure_ascii=False) + "\n",
                     encoding="utf-8")
        ff.log(f"\nNEED_MCP_ELEVENLABS {len(jobs)} fichier(s) à générer — "
               f"voir {p.relative_to(ROOT)}")
        ff.log("Pas de clé ELEVENLABS_API_KEY : l'agent passe les appels "
               "text_to_speech, dépose les MP3 aux chemins indiqués, puis "
               "relance ce script pour la mesure et la normalisation.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
