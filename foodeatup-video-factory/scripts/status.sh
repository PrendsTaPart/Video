#!/usr/bin/env bash
# Tableau de bord des 150 épisodes : qui travaille sur quoi, ce qui manque.
#   ./status.sh            vue d'ensemble
#   ./status.sh --manquants   liste ce qu'il reste à déposer, épisode par épisode
set -euo pipefail
R="$(cd "$(dirname "$0")/.." && pwd)"

python3 - "$R" "${1:-}" <<'PY'
import json, pathlib, sys
R, mode = pathlib.Path(sys.argv[1]), sys.argv[2]

eps = [json.loads(f.read_text(encoding="utf-8"))
       for f in sorted((R / "state" / "episodes").glob("EP*.json"))]
claims = {}
for p in (R / "state" / "claims").glob("EP*.json"):
    claims[p.stem] = json.loads(p.read_text(encoding="utf-8"))

def dispo(e, d):
    return (R / "assets" / d / f"{e['id']}.mp4").exists()

manquants = []
compte = {"hook": 0, "avatar": 0, "software": 0, "monte": 0}
for e in eps:
    trous = [d for d in ("hooks", "avatar", "software") if not dispo(e, d)]
    for d in ("hooks", "avatar", "software"):
        if dispo(e, d):
            compte["hook" if d == "hooks" else d] += 1
    if (R / "dist" / "tiktok" / f"{e['id']}.mp4").exists():
        compte["monte"] += 1
    if trous:
        manquants.append((e, trous))

n = len(eps)
print(f"=== FoodEatUp — {n} épisodes ===\n")
print(f"  hooks Higgsfield déposés : {compte['hook']:3d}/{n}")
print(f"  avatars HeyGen déposés   : {compte['avatar']:3d}/{n}")
print(f"  extraits logiciel        : {compte['software']:3d}/{n}")
print(f"  masters montés           : {compte['monte']:3d}/{n}")
print(f"  épisodes réservés        : {len(claims):3d}")

if claims:
    print("\n--- en cours ---")
    for eid in sorted(claims):
        c = claims[eid]
        print(f"  {eid}  {c['owner']:<32} depuis {c['reserve_le']}")

if mode == "--manquants":
    print("\n--- assets manquants ---")
    for e, trous in manquants:
        print(f"  {e['id']} {e['titre'][:38]:<40} {' '.join(trous)}")
elif manquants:
    print(f"\n  {len(manquants)} épisodes attendent encore un asset "
          f"(./status.sh --manquants pour le détail)")
PY
