#!/usr/bin/env bash
# Renvoie l'identifiant du prochain épisode à produire, ou rien s'il n'y en a plus.
#
# Ordre : les épisodes dont les trois assets sont déjà déposés d'abord (ils sont
# montables tout de suite), puis l'ordre naturel. EP150 passe toujours en dernier :
# c'est le final, il ne se monte qu'une fois les autres connus.
set -euo pipefail
R="$(cd "$(dirname "$0")/.." && pwd)"

python3 - "$R" <<'PY'
import json, pathlib, sys
R = pathlib.Path(sys.argv[1])
claims = {p.stem for p in (R / "state" / "claims").glob("EP*.json")}

pret, reste = [], []
for f in sorted((R / "state" / "episodes").glob("EP*.json")):
    if f.stem in claims:
        continue
    e = json.loads(f.read_text(encoding="utf-8"))
    if e["etat"]["build"] == "ok":
        continue
    if e["num"] == 150:
        continue
    ok = all((R / "assets" / d / f"{e['id']}.mp4").exists()
             for d in ("hooks", "avatar", "software"))
    (pret if ok else reste).append(e["id"])

ordre = pret + reste
if not ordre and "EP150" not in claims:
    ordre = ["EP150"]
print(ordre[0] if ordre else "")
PY
