#!/usr/bin/env python3
"""04 — Brouillons RapidoCMS planifiés (jamais de publication directe).

RapidoCMS et Google Drive sont exposés en MCP, donc côté agent : ce script ne
passe pas les appels lui-même. Il fait ce qu'un script peut faire de mieux —
vérifier qu'on a le droit de publier, et produire le plan d'appels exact :

  build/publish_plan_<EPxx>.json

L'agent exécute ce plan tel quel, dans l'ordre. Chaque entrée porte le nom de
l'outil MCP et ses arguments complets.

Garde-fous appliqués avant d'écrire le plan :
  * le master doit exister ET son dernier journal de run doit porter
    `publiable: true` (donc QA 7/7 et voix off incluse) ;
  * un master assemblé avec `--skip-vo` est refusé ;
  * `privacy_level` TikTok reste `SELF_ONLY` sauf `--tiktok-public` explicite ;
  * on ne produit que des BROUILLONS planifiés, jamais de publication immédiate.

Chaîne d'URL publique (SPEC §5.1) : `upload_file_tool` ne lit pas le disque, il
exige une URL publique. Le plan enchaîne donc Drive (create_file dans le dossier
partagé) → URL de téléchargement direct → upload_file_tool → create_draft_tool
→ schedule_draft_tool.

Usage :
    python scripts/04_publish_rapidocms.py --episode EP01
    python scripts/04_publish_rapidocms.py --episode EP01 --start 2026-08-18
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ff  # noqa: E402

ROOT = ff.ROOT
BUILD = ROOT / "build"
OUT = ROOT / "out"

# Réseau → (format du master, clé de hashtags)
NETWORKS = {
    "tiktok": ("tiktok_30", "tiktok"),
    "instagram": ("tiktok_30", "instagram"),
    "facebook": ("tiktok_30", "instagram"),
    "linkedin": ("linkedin_45", "linkedin"),
}
# 2 h d'écart entre réseaux : ne pas poster le même contenu partout à la seconde.
OFFSET_H = {"tiktok": 0, "instagram": 2, "linkedin": 4, "facebook": 6}
# 3 publications par semaine et par réseau.
WEEKDAYS = [0, 2, 4]                       # lundi, mercredi, vendredi
BASE_HOUR = 12
DRIVE_FOLDER = "FoodEatUp — Vidéos promo"


def latest_run(ep_id: str, fmt: str) -> dict | None:
    runs = sorted(BUILD.glob(f"run_*_{ep_id}_{fmt}.json"))
    if not runs:
        return None
    return json.loads(runs[-1].read_text(encoding="utf-8"))


def slot(index: int, start: dt.date) -> dt.date:
    """Date du `index`-ième créneau (3 par semaine) à partir de `start`."""
    week, pos = divmod(index, len(WEEKDAYS))
    monday = start - dt.timedelta(days=start.weekday()) + dt.timedelta(weeks=week)
    d = monday + dt.timedelta(days=WEEKDAYS[pos])
    return d if d >= start else d + dt.timedelta(weeks=1)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--episode", required=True)
    ap.add_argument("--start", help="date du 1er créneau (AAAA-MM-JJ), "
                                    "défaut : aujourd'hui")
    ap.add_argument("--tiktok-public", action="store_true",
                    help="passe privacy_level à PUBLIC_TO_EVERYONE "
                         "(uniquement si l'humain l'a validé)")
    ap.add_argument("--heure-separateur", choices=[":", "-"], default=":",
                    help="séparateur de post_heure ; la doc de l'outil annonce "
                         "H-i-s mais l'API a été vérifiée en H:i:s")
    args = ap.parse_args()

    cfg = ff.load_config()
    ep = ff.episode(cfg, args.episode)
    idx = [e["id"] for e in cfg["episodes"]].index(ep["id"])
    start = (dt.date.fromisoformat(args.start) if args.start
             else dt.date.today())

    # --- garde-fous ------------------------------------------------------
    blockers: list[str] = []
    masters: dict[str, Path] = {}
    for fmt in sorted({f for f, _ in NETWORKS.values()}):
        p = OUT / f"{ep['id']}_{fmt}.mp4"
        if not p.exists():
            blockers.append(f"MISSING_MASTER {p.relative_to(ROOT)} — lance "
                            f"03_assemble.py --episode {ep['id']} "
                            f"--format {fmt}")
            continue
        run = latest_run(ep["id"], fmt)
        if run is None:
            blockers.append(f"NO_RUN_JOURNAL {ep['id']}/{fmt} — master non "
                            f"tracé, réassemble-le")
        elif not run.get("publiable", False):
            failed = [t["test"] for t in run.get("qa", []) if not t["ok"]]
            reason = (", ".join(failed) if failed
                      else "voix off absente (--skip-vo)")
            blockers.append(f"NOT_PUBLISHABLE {ep['id']}/{fmt} — {reason}")
        else:
            masters[fmt] = p

    if blockers:
        for b in blockers:
            ff.log(f"  BLOQUÉ  {b}", err=True)
        ff.log("\nAucun plan écrit : on ne publie pas un master non validé.",
               err=True)
        return 1

    # --- plan d'appels MCP ------------------------------------------------
    steps: list[dict] = []
    steps.append({
        "step": "comptes",
        "tool": "RapidoCMS:list_connected_accounts",
        "args": {},
        "note": "récupère les account_id réels ; ne jamais les coder en dur",
    })

    for fmt, path in masters.items():
        steps.append({
            "step": f"drive_upload:{fmt}",
            "tool": "GoogleDrive:create_file",
            "args": {"name": f"{ep['id']}_{fmt}.mp4",
                     "folder": DRIVE_FOLDER,
                     "local_path": str(path.relative_to(ROOT))},
            "note": "dossier pré-partagé « tous les utilisateurs disposant du "
                    "lien » ; vérifier avec get_file_permissions",
        })
        steps.append({
            "step": f"biblio:{fmt}",
            "tool": "RapidoCMS:upload_file_tool",
            "args": {"file_url": "https://drive.google.com/uc?export=download"
                                 "&id=<FILE_ID de l'étape précédente>",
                     "name": f"{ep['id']}_{fmt}", "type": "video"},
            "note": "si RapidoCMS refuse l'URL Drive (antivirus sur les gros "
                    "fichiers), basculer sur un hébergement statique maîtrisé "
                    "et le documenter — ne PAS regénérer la vidéo ailleurs",
        })

    sep = args.heure_separateur
    for net, (fmt, tag) in NETWORKS.items():
        date = slot(idx, start)
        hour = BASE_HOUR + OFFSET_H[net]
        caption = f"{ep['caption']}\n\n{cfg['hashtags'][tag]}"
        draft = {
            "account_id": f"<accounts['{net}'] de l'étape comptes>",
            "social_type": net,
            "post_name": f"{ep['id']} — {ep['titre']}",
            "post_type": "mediatext",
            "media_type": "video",
            "media_source": "biblio",
            "media_url": f"<file_url renvoyé par biblio:{fmt}>",
            "media_caption": caption,
        }
        if net == "tiktok":
            draft["privacy_level"] = ("PUBLIC_TO_EVERYONE" if args.tiktok_public
                                      else "SELF_ONLY")
            draft["your_brand"] = True
        steps.append({"step": f"draft:{net}",
                      "tool": "RapidoCMS:create_draft_tool",
                      "args": draft, "format": fmt})
        steps.append({
            "step": f"schedule:{net}",
            "tool": "RapidoCMS:schedule_draft_tool",
            "args": {"draft_id": f"<id renvoyé par draft:{net}>",
                     "post_date": date.isoformat(),
                     "post_heure": f"{hour:02d}{sep}00{sep}00"},
            "note": "heure comparée à l'horloge Europe/Paris côté serveur",
        })

    plan = {
        "episode": ep["id"], "titre": ep["titre"],
        "genere_le": dt.datetime.now().isoformat(timespec="seconds"),
        "masters": {k: str(v.relative_to(ROOT)) for k, v in masters.items()},
        "tiktok_public": args.tiktok_public,
        "publication_directe": False,
        "steps": steps,
    }
    p = BUILD / f"publish_plan_{ep['id']}.json"
    p.write_text(json.dumps(plan, indent=2, ensure_ascii=False) + "\n",
                 encoding="utf-8")

    ff.log(f"Plan écrit : {p.relative_to(ROOT)}  ({len(steps)} appels MCP)")
    for net, (fmt, _) in NETWORKS.items():
        ff.log(f"  {net:<10} {fmt:<12} {slot(idx, start).isoformat()} "
               f"{BASE_HOUR + OFFSET_H[net]:02d}{sep}00{sep}00")
    ff.log("\nBrouillons planifiés uniquement — aucune publication immédiate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
