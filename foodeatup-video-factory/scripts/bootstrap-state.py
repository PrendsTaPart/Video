#!/usr/bin/env python3
"""Génère un fichier d'état par épisode depuis content/episodes.json.

Un fichier par épisode, jamais un fichier partagé : c'est ce qui permet à
plusieurs sessions Claude Code de travailler en parallèle sans conflit git.
Idempotent — un état existant n'est jamais écrasé.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "content" / "episodes.json").read_text(encoding="utf-8"))
modules = data["modules"]

out = ROOT / "state" / "episodes"
out.mkdir(parents=True, exist_ok=True)

cree = garde = 0
for ep in data["episodes"]:
    n = ep["n"]
    eid = f"EP{n:03d}"
    f = out / f"{eid}.json"
    if f.exists():
        garde += 1
        continue
    saison = (n - 1) // 30 + 1
    f.write_text(json.dumps({
        "id": eid,
        "num": n,
        "saison": saison,
        "titre": ep["t"],
        "module": ep["mod"],
        "chapitre": ep["ch"],
        "module_drive_id": modules[ep["mod"]],
        "hook": ep["hook"],
        "vo_punchline": ep["punch"],
        "heygen_script": ep["heygen"],
        "etat": {
            "hook": "manquant",
            "avatar": "manquant",
            "software": "manquant",
            "vo": "manquant",
            "build": "manquant",
            "publie": "manquant",
        },
        "notes": "",
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    cree += 1

print(f"états créés : {cree} | déjà présents : {garde}")
