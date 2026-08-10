#!/usr/bin/env python3
"""Extrait les 150 prompts Higgsfield des briefs de saison vers content/prompts-higgsfield.json.

Les cinq briefs n'ont pas tout à fait le même balisage (## ou ###, avec ou sans
libellé **Prompt**). On repère l'en-tête d'épisode, puis la première citation qui
suit : c'est le prompt.
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
BRIEFS = ROOT / "content" / "briefs"

TITRE = re.compile(r"^#{2,3}\s+EP\s?(\d{1,3})\s*[—–-]\s*(.+?)\s*$")

prompts = {}
for f in sorted(BRIEFS.glob("0[23456]-HIGGSFIELD-S*.md")):
    lignes = f.read_text(encoding="utf-8").splitlines()
    courant = None
    attend_prompt = False
    for ligne in lignes:
        m = TITRE.match(ligne)
        if m:
            courant = f"EP{int(m.group(1)):03d}"
            attend_prompt = False
            continue
        if not courant or courant in prompts:
            continue
        # saisons 4-5 : le prompt est la ligne qui suit le libellé, sans citation
        if ligne.strip() == "**Prompt**":
            attend_prompt = True
            continue
        texte = ligne.lstrip("> ").strip()
        if (attend_prompt or ligne.startswith(">")) and len(texte) > 80:
            prompts[courant] = texte
            courant, attend_prompt = None, False

sortie = ROOT / "content" / "prompts-higgsfield.json"
sortie.write_text(
    json.dumps(prompts, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)

attendus = {f"EP{n:03d}" for n in range(1, 151)}
manquants = sorted(attendus - set(prompts))
print(f"prompts extraits : {len(prompts)}/150")
if manquants:
    print(f"manquants : {', '.join(manquants)}")
