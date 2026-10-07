#!/usr/bin/env python3
"""Construit bd-video/storyboard.json à partir de l'extraction Figma.

    python3 bd-video/scripts/build_storyboard.py

Un plan = une ligne de la BD, dans l'ordre de lecture (page, case, haut → bas, gauche → droite) :
  recit  : cartouche crème, voix off de Mickael (première personne)
  bulle  : réplique d'un personnage, avec sa pastille
  titre  : texte posé sur la page (couverture, titres de partie, cartes personnages, fermeture)
La durée estimée sert au budget ; c'est la durée réelle des voix (étape 2) qui fixera le montage.
"""
import json
import os
import re
import subprocess

ROOT = os.path.join(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip(), "bd-video")
pages = json.load(open(os.path.join(ROOT, "figma", "extraction.json")))
panels = {(p["page"], p["case"]): p["file"] for p in json.load(open(os.path.join(ROOT, "panels", "index.json")))}

PARTS = [  # (première page, dernière page, libellé, épisode)
    (1, 4, "Ouverture", "ep01"), (5, 7, "Prologue", "ep01"),
    (8, 31, "Partie 1 · Une journée sans FoodEatUp", "ep01"),
    (32, 53, "Partie 2 · La même journée, avec FoodEatUp", "ep02"),
    (54, 62, "Partie 3 · La brigade passe à l'écran", "ep03"),
    (63, 73, "Partie 4 · Expansion & franchise", "ep04"),
    (74, 81, "Partie 5 · Le laboratoire et les agents", "ep05"),
    (82, 86, "Partie 6 · Une infinité de solutions", "ep06"),
    (87, 87, "Épilogue", "ep06"), (88, 88, "Fermeture", "ep06"),
]

# Nom affiché → identifiant de personnage (voix + pastille).
SPEAKERS = {
    "MICKAEL": "mickael", "BERNARD": "bernard", "LÉA": "lea", "KARIM": "karim", "SOFIANE": "sofiane",
    "NADIA": "nadia", "INÈS": "ines", "THOMAS": "thomas",
    "PRÉDIBOT": "predibot", "IRIS": "iris", "CAROLINE": "caroline", "JARVIS": "jarvis",
    "L'ASSISTANT IA": "assistant-ia", "PLANI'T": None,
    "LA CLIENTE": "la-cliente", "LE CLIENT": "le-client", "UNE PASSANTE": "une-passante", "LE PETIT": "le-petit",
    "LA FRANCHISÉE": "la-franchisee", "LA NOUVELLE": "la-nouvelle", "LA PIZZAIOLO": "la-pizzaiolo",
    "LE TRAITEUR": "le-traiteur", "LA COMPTABLE": "la-comptable", "LA BOULANGÈRE": "la-boulangere",
    "LE FOOD-TRUCK": "le-food-truck",
}

# Cases fortes animées par IA (étape 3B) : (page, case) → ce qui doit bouger.
HERO = {
    (1, 1): "Couverture : la brigade pose devant le Bistrot du Marché",
    (5, 1): "« Je m'appelle Mickael » : portrait du chef derrière son passe",
    (15, 1): "Le coup de feu : la cuisine déborde, les tickets s'accumulent",
    (22, 1): "« On tient… mais à quel prix ? » : les assiettes tombent",
    (27, 1): "Le dîner manqué : Mickael seul, la tête dans les mains",
    (30, 1): "« FoodEatUp est né » : l'équipe IA apparaît en hologramme",
    (33, 2): "PrédiBot s'allume et présente le brief du matin",
    (37, 1): "Iris propose le post « tarte du jour »",
    (40, 1): "Caroline décroche pendant le coup de feu",
    (45, 1): "Jarvis accueille le client au drive",
    (51, 1): "« Ce soir, je dîne avec ma famille »",
    (53, 1): "« Bienvenue dans la brigade FoodEatUp » : humains et agents réunis",
    (57, 2): "« Diffuser maintenant » : toute la salle s'allume",
    (60, 1): "Le plat sort de l'écran du site",
    (63, 1): "Expansion & franchise : la carte de France s'illumine",
    (73, 2): "La brigade augmentée devient une famille",
    (74, 1): "Le laboratoire central et ses agents",
    (77, 2): "Les quatre agents s'animent autour de la table",
    (82, 1): "Une infinité de solutions : le symbole infini",
    (86, 1): "« Chef… tu sors de la BD ! »",
    (87, 2): "Épilogue : dîner en famille",
}

SKIP = re.compile(r"^(★|✓|p\. \d+|WhatsApp)$")


def part_of(n):
    for a, b, label, ep in PARTS:
        if a <= n <= b:
            return label, ep
    raise ValueError(n)


def norm_speaker(s):
    s = (s or "").replace("’", "'").replace(" · IA", "").strip()
    return s


def estimate(kind, text):
    # Débit voix FR ~ 14 caractères/s + respiration ; un titre muet reste ~2,5 s mini.
    if kind == "titre":
        return round(max(2.5, 1.5 + len(text) / 20), 1)
    return round(max(2.0, 0.6 + len(text) / 14), 1)


shots = []
for p in pages:
    n = int(re.match(r"Page (\d+)", p["n"]).group(1))
    part, ep = part_of(n)
    counter = {}
    pending_titles = []  # titres consécutifs fusionnés en un plan

    def image_for(case):
        return panels.get((n, case or 1)) or f"pages/p{n:02d}.png"

    def add(case, kind, speaker, text, extra=None):
        c = case or 1
        counter[c] = counter.get(c, 0) + 1
        sid = SPEAKERS.get(speaker) if speaker else None
        shot = {
            "id": f"p{n:02d}-c{c}-{counter[c]:02d}",
            "page": n, "case": c, "part": part, "episode": ep,
            "image": image_for(case),
            "page_image": f"pages/p{n:02d}.png",
            "type": kind,
            "speaker": speaker,
            "voice": sid,
            "text": text,
            "avatar": f"cast/{sid}.png" if sid else None,
            "hero": (n, c) in HERO,
            "duration_est": estimate(kind, text),
        }
        if extra:
            shot.update(extra)
        shots.append(shot)

    def flush():
        while pending_titles:
            case, text = pending_titles.pop(0)
            # On fusionne les titres courts consécutifs de la même case.
            while pending_titles and pending_titles[0][0] == case and len(text) < 120 and len(pending_titles[0][1]) < 120:
                text += " · " + pending_titles.pop(0)[1]
            add(case, "titre", None, text)

    # Ordre des bulles dans une case : l'ordre de création Figma (id de la pastille) suit le récit,
    # alors que la position ne le fait pas toujours (deux bulles à la même hauteur, p. 57 et 59).
    items = list(p["items"])
    for c in {it[0] for it in items}:
        slots = [i for i, it in enumerate(items) if it[0] == c and it[1] == "B"]
        ordered = sorted((items[i] for i in slots), key=lambda it: tuple(int(x) for x in it[5].split(":")))
        for i, it in zip(slots, ordered):
            items[i] = it

    for it in items:
        case, kind = it[0], it[1]
        if kind == "T":
            if SKIP.match(it[3].strip()):
                continue
            pending_titles.append((case, it[3].strip()))
            continue
        flush()
        if kind == "R":
            add(case, "recit", "MICKAEL", it[3].strip(), {"voice_role": "narrateur"})
        elif kind == "B":
            add(case, "bulle", norm_speaker(it[2]), it[3].strip(), {"figma_pastille": it[5]})
        elif kind == "C":  # cartes personnages (pages 3 et 4)
            fields = [f.strip() for f in it[3].split("|")]
            name = norm_speaker(it[2])
            add(case, "titre", name, " — ".join(fields), {"card": {"name": fields[0], "role": fields[1], "bio": fields[2]}})
    flush()

for s in shots:
    if s["hero"]:
        s["hero_action"] = HERO[(s["page"], s["case"])]

json.dump(shots, open(os.path.join(ROOT, "storyboard.json"), "w"), ensure_ascii=False, indent=1)

# Contrôles : chaque case dessinée a au moins un plan, chaque page est couverte.
covered = {(s["page"], s["case"]) for s in shots}
orphans = [k for k in panels if k not in covered]
pages_cov = sorted({s["page"] for s in shots})
print(f"{len(shots)} plans · pages couvertes {len(pages_cov)}/88 · cases sans plan : {orphans or 'aucune'}")
