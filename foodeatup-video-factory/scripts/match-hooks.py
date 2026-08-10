#!/usr/bin/env python3
"""Apparie l'historique Higgsfield aux 150 épisodes, par comparaison de prompts.

RÉCUPÉRATION SEULE. Ce script ne génère rien : il lit des pages d'historique
déjà obtenues via le MCP Higgsfield (show_generations) et retrouve, pour chaque
épisode, les rendus déjà payés.

  1. Dans une session Claude Code, appelle show_generations(type="video",
     size=40), puis rappelle-le avec le next_cursor jusqu'à ce qu'il soit null.
     Chaque réponse trop grosse est écrite dans un fichier par le harnais.
  2. python3 scripts/match-hooks.py <fichier1.json> <fichier2.json> ...
  3. ./scripts/fetch-hooks.sh

L'appariement se fait sur le prompt, pas sur la date : c'est le seul lien fiable
entre un job Higgsfield et un épisode. Les prompts de l'historique sont
retournés à la ligne, d'où la normalisation des blancs avant comparaison.
"""
import difflib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SEUIL = 0.90  # en dessous, on considère que ce n'est pas le même plan


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip().lower()


def main(fichiers):
    ref = {k: norm(v) for k, v in json.loads(
        (ROOT / "content" / "prompts-higgsfield.json").read_text(encoding="utf-8")
    ).items()}

    items = []
    for f in fichiers:
        d = json.loads(pathlib.Path(f).read_text(encoding="utf-8"))
        items += d.get("items", [])

    trouve = {}
    for it in items:
        if it.get("status") != "completed":
            continue
        url = (it.get("results") or {}).get("rawUrl")
        p = norm((it.get("params") or {}).get("prompt"))
        if not url or len(p) < 80:
            continue
        best, score = None, 0.0
        for eid, rp in ref.items():
            r = difflib.SequenceMatcher(None, p[:400], rp[:400]).ratio()
            if r > score:
                best, score = eid, r
        if score >= SEUIL:
            trouve.setdefault(best, []).append({
                "job": it["id"],
                "url": url,
                "at": it["createdAt"],
                "score": round(score, 3),
            })

    # la prise la plus récente d'abord : c'est elle que fetch-hooks.sh prendra
    for v in trouve.values():
        v.sort(key=lambda x: -x["at"])

    sortie = ROOT / "content" / "hooks-higgsfield.json"
    sortie.write_text(
        json.dumps(trouve, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    manquants = [f"EP{n:03d}" for n in range(1, 151) if f"EP{n:03d}" not in trouve]
    reprises = {k: len(v) for k, v in trouve.items() if len(v) > 1}
    print(f"générations lues   : {len(items)}")
    print(f"épisodes appariés  : {len(trouve)}/150")
    print(f"plusieurs prises   : {len(reprises)} ({', '.join(sorted(reprises))})")
    print(f"sans rendu         : {len(manquants)}")
    if manquants:
        print("  " + ", ".join(manquants[:40]) + (" …" if len(manquants) > 40 else ""))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: match-hooks.py <page1.json> [page2.json ...]")
    main(sys.argv[1:])
