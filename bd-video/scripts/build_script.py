#!/usr/bin/env python3
"""Étape 2 — script, casting et manifeste de génération des voix.

    python3 bd-video/scripts/build_script.py

Écrit :
  voices.json            personnage → voix ElevenLabs (voice_id + lien d'écoute gratuit)
  script.md              le texte complet du film, par partie, avec personnage et intention
  audio/vo_manifest.json une entrée par réplique : id, voice_id, modèle, texte envoyé au TTS
Le texte affiché reste celui de la BD ; seul le texte envoyé au TTS est normalisé pour la
prononciation (unités, sigles) et reçoit des balises d'intention eleven_v3 entre crochets.
"""
import json
import os
import re
import subprocess

ROOT = os.path.join(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip(), "bd-video")
shots = json.load(open(os.path.join(ROOT, "storyboard.json")))
MODEL = "eleven_v3"

# Casting : voix existantes de la bibliothèque ElevenLabs (aucune voix clonée).
# preview = extrait d'écoute gratuit fourni par ElevenLabs.
CAST = {
    "mickael": ("Mickael (narrateur)", "APbYQosMxYlAnCCBzydW", "Remy – Warm French Narrator",
                "chaud, grave, léger accent du Sud : un chef qui raconte", "https://storage.googleapis.com/eleven-public-prod/database/workspace/2c8edd3f08c1440c8c3445c4f4c3895d/voices/APbYQosMxYlAnCCBzydW/I69rFI2y1jKQdRkVdJOx.mp3"),
    "bernard": ("Bernard", "GFj5Qf6cNQ3Lgp8VKBwc", "Olivier D – Old man for cartoon & animation",
                "voix âgée, bourrue, dessin animé", "https://storage.googleapis.com/eleven-public-prod/database/workspace/8c6176bbc2f44115a207793db7b74bc6/voices/GFj5Qf6cNQ3Lgp8VKBwc/NrTlsCPkDgukftt0UFoH.mp3"),
    "lea": ("Léa", "Cy2zXKmu2kQeAuze0rzV", "Chloé – French",
            "nette, énergique, précise", "https://storage.googleapis.com/eleven-public-prod/database/workspace/7244784043964d9f87fd5c522a06d1ea/voices/Cy2zXKmu2kQeAuze0rzV/1YjM8FjImipT8xTx5Ejq.mp3"),
    "karim": ("Karim", "7pDdnNI6PhXmAp0pXFZm", "Noé – Content Creator",
              "jeune, spontané", "https://storage.googleapis.com/eleven-public-prod/database/workspace/b91a8bb1f701403a82385b792a802e71/voices/7pDdnNI6PhXmAp0pXFZm/FdWEpiSMIrpAniEZvmIJ.mp3"),
    "sofiane": ("Sofiane", "NBjtCdChq5Ph56VnCM8Z", "Théo – UGC Creator",
                "souriant, commercial, naturel", "https://api.us.elevenlabs.io/v1/voices/NBjtCdChq5Ph56VnCM8Z/previews/audio?payload=eyJ2b2ljZV9zb3VyY2UiOiJjdXN0b20iLCJ3b3Jrc3BhY2VfaWQiOiJlYzBkNmI0MzQwODA0MGFmYTkxYjg1YzdjYWU1MTdkNyIsImZpbGVuYW1lIjoiRGEyemo2cVRSNUZ2T2pvc3FoTE4ubXAzIiwidGltZXN0YW1wIjoxNzkwOTU2ODAwMDAwMDAwfQ%3D%3D"),
    "nadia": ("Nadia", "UaGvaD7NWzU5mJNoUqoY", "Perle – Premium French Corporate",
              "posée, rassurante", "https://storage.googleapis.com/eleven-public-prod/database/workspace/9b575dced44a494191dd4a86259dca58/voices/UaGvaD7NWzU5mJNoUqoY/vDA7gLJMATfRgzejin2y.mp3"),
    "ines": ("Inès", "O31r762Gb3WFygrEOGh0", "Victoria – Content Creator",
             "jeune, vive, réseaux sociaux", "https://storage.googleapis.com/eleven-public-prod/database/workspace/8883bfc00193440ba374c3ecd71610b5/voices/O31r762Gb3WFygrEOGh0/x79aDNW4Q3qgJKq1svTL.mp3"),
    "thomas": ("Thomas", "c365oriviHmAhyLhpuN6", "Adrien Clairon – French Modern",
               "assuré, directeur", "https://storage.googleapis.com/eleven-public-prod/database/workspace/34e3b1de9d1847c991f7159a05bb5e81/voices/c365oriviHmAhyLhpuN6/wW2tVxsVnR24BGWGN4eR.mp3"),
    # Agents IA : voix d'assistant claires ; un léger traitement « synthétique » est ajouté au mixage.
    "predibot": ("PrédiBot (IA)", "odOFTFZU3DvAZ3EV3KHi", "Lucas – Premium French Corporate",
                 "neutre, précis + filtre synthétique", "https://storage.googleapis.com/eleven-public-prod/database/workspace/27ed767f766c44b0af61d239d867281d/voices/odOFTFZU3DvAZ3EV3KHi/t1nwOMycInvdG6yuJZHr.mp3"),
    "iris": ("Iris (IA)", "yatuMX0k4Dh41R64sbGj", "Cécile – Interactive Customer Support",
             "aimable, réactive + filtre synthétique", "https://storage.googleapis.com/eleven-public-prod/database/workspace/ed9b05e6324c457685490352e9a1ec90/voices/yatuMX0k4Dh41R64sbGj/bW2x4IuA89YQmVwGwPPV.mp3"),
    "caroline": ("Caroline (IA vocale)", "uOw88F5bjqRiVuZLhXEA", "Victoria Agent",
                 "agent téléphonique + filtre téléphone", "https://storage.googleapis.com/eleven-public-prod/database/workspace/18b8771d279e4e979b042a209618a697/voices/uOw88F5bjqRiVuZLhXEA/l2Jl5QB3CZJLkwhOBPr1.mp3"),
    "jarvis": ("Jarvis (IA drive)", "N84W2MAq7DASQyJC2ug4", "Jean Charles",
               "voix d'annonce + filtre haut-parleur", "https://api.us.elevenlabs.io/v1/voices/N84W2MAq7DASQyJC2ug4/previews/audio?payload=eyJ2b2ljZV9zb3VyY2UiOiJjdXN0b20iLCJ3b3Jrc3BhY2VfaWQiOiJlYjBlMDUxYWJjODY0NjE4YmMwNzMzMjY0MDYxOWMyZCIsImZpbGVuYW1lIjoiNDY3MDc5OTUtZDQxYS00ZmY1LWE0NWYtZmQyYjYyNTFiMDRiLm1wMyIsInRpbWVzdGFtcCI6MTc5MDk1NjgwMDAwMDAwMH0%3D"),
    "assistant-ia": ("L'assistant IA", "5OnMHwgTFgvPVwE8jP6B", "Anaïs – News, podcasting",
                     "claire, neutre + filtre synthétique léger", "https://storage.googleapis.com/eleven-public-prod/database/workspace/ba696ba376dc4922a911da94eff98f2a/voices/5OnMHwgTFgvPVwE8jP6B/hyOFlAxqmCLW3fVQQMAG.mp3"),
    # Clients et rôles secondaires : 3 voix génériques.
    "client-f": ("Clientes (voix générique 1)", "mNu8EQcIlFZdOJs7yfhe", "Julia – Warm French Narrator",
                 "jeune femme, chaleureuse", "https://storage.googleapis.com/eleven-public-prod/database/workspace/9ba829528b3242f79e18a8ca367e00d9/voices/mNu8EQcIlFZdOJs7yfhe/UuwaczHRXyEGgUT8wxSm.mp3"),
    "client-f2": ("Clientes (voix générique 2)", "gAx9hUOvSB0WdmtuJSBl", "Merisa – smooth and captivating",
                  "femme, dynamique", "https://storage.googleapis.com/eleven-public-prod/database/workspace/6dec3214a63b421fa5083f1747b31eb2/voices/gAx9hUOvSB0WdmtuJSBl/3ef8a5f0-5f76-4d25-8a88-c0d85e78c68d.mp3"),
    "client-h": ("Clients (voix générique 3)", "kKgyAHjGAbeWHCNd7qoC", "Augustin – Conversational French",
                 "homme, conversationnel", "https://storage.googleapis.com/eleven-public-prod/database/workspace/f453e6ece3844b538d2987595f62f0ce/voices/kKgyAHjGAbeWHCNd7qoC/JKUrofGQfxVO8svGxbtc.mp3"),
}
ROLES = {  # rôle de la BD → voix
    "la-cliente": "client-f", "une-passante": "client-f2", "la-franchisee": "client-f2", "la-nouvelle": "client-f",
    "la-pizzaiolo": "client-f2", "la-comptable": "client-f", "la-boulangere": "client-f2",
    "le-client": "client-h", "le-traiteur": "client-h", "le-food-truck": "client-h",
    "le-petit": "client-f",  # balise [childlike voice] ajoutée
}
SYNTHETIC = {"predibot", "iris", "caroline", "jarvis", "assistant-ia"}

MOOD = {
    "Prologue": ("nostalgique, posé", "[warmly]"),
    "Partie 1 · Une journée sans FoodEatUp": ("épuisé, tendu", "[tired]"),
    "Partie 2 · La même journée, avec FoodEatUp": ("soulagé, confiant", "[happy]"),
    "Partie 3 · La brigade passe à l'écran": ("enjoué", "[excited]"),
    "Partie 4 · Expansion & franchise": ("fier, ambitieux", "[warmly]"),
    "Partie 5 · Le laboratoire et les agents": ("serein, maîtrisé", "[warmly]"),
    "Partie 6 · Une infinité de solutions": ("inspiré, chaleureux", "[warmly]"),
    "Épilogue": ("ému", "[softly]"),
}


def intention(s):
    part, t, voice = s["part"], s["text"], s["voice"]
    base, tag = MOOD.get(part, ("neutre", ""))
    if voice in SYNTHETIC:
        return "synthétique, aimable", "[warmly]"
    if s["type"] == "recit":
        if part.startswith("Partie 1"):
            return "las, ironique" if "…" in t else "las", "[tired]"
        return base, tag
    p1 = part.startswith("Partie 1")
    if t.endswith("?!") or ("!" in t and p1):
        return "exaspéré, pressé", "[frustrated]"
    if "?" in t and p1:
        return "inquiet", "[nervous]"
    if t.rstrip().endswith("…") or "…" in t[:25]:
        return "hésitant" if p1 else "complice", "[hesitant]" if p1 else "[chuckles]"
    if "!" in t:
        return "enthousiaste", "[excited]"
    if "?" in t:
        return "curieux", "[curious]"
    return base, tag


REPL = [
    (r"(\d+) h (\d\d)", r"\1 heures \2"), (r"(\d+) h\b", r"\1 heures"),
    (r"(\d+),(\d+) € HT", r"\1 euros \2 hors taxe"), (r"(\d+),(\d+) €", r"\1 euros \2"),
    (r"(\d+) %", r"\1 pour cent"), (r"(\d+) ml\b", r"\1 millilitres"), (r"(\d+) g\b", r"\1 grammes"),
    (r"\bHACCP\b", "H.A.C.C.P."), (r"\bMCP\b", "M.C.P."), (r"\bQR\b", "Q.R."),
    (r"Plani't", "Planit"), (r"«\s*|\s*»", ""), (r"1er\b", "premier"),
]


def tts_text(s, tag):
    t = s["text"]
    letters = [c for c in t if c.isalpha()]
    if letters and sum(c.isupper() for c in letters) > 0.8 * len(letters):  # « AVANT LE SERVICE · 7 h 05 »
        t = t.capitalize()
    t = t.replace(" · ", ", ")
    for a, b in REPL:
        t = re.sub(a, b, t)
    extra = "[childlike voice] " if s["voice"] == "le-petit" else ""
    return f"{extra}{tag} {t}".strip()


lines, manifest = [], []
for s in shots:
    if s["type"] == "titre":
        continue
    vkey = ROLES.get(s["voice"], s["voice"])
    label, vid = CAST[vkey][0], CAST[vkey][1]
    intent, tag = intention(s)
    s["intent"] = intent
    manifest.append({"id": s["id"], "speaker": s["speaker"], "cast": vkey, "voice_id": vid, "model_id": MODEL,
                     "text": s["text"], "tts_text": tts_text(s, tag), "intent": intent,
                     "synthetic": vkey in SYNTHETIC, "file": f"audio/vo/{s['id']}.mp3"})

os.makedirs(os.path.join(ROOT, "audio"), exist_ok=True)
json.dump(manifest, open(os.path.join(ROOT, "audio", "vo_manifest.json"), "w"), ensure_ascii=False, indent=1)
json.dump({k: {"role": v[0], "voice_id": v[1], "voice_name": v[2], "note": v[3], "preview_url": v[4],
               "synthetic_filter": k in SYNTHETIC} for k, v in CAST.items()} | {"_roles": ROLES, "_model": MODEL},
          open(os.path.join(ROOT, "voices.json"), "w"), ensure_ascii=False, indent=1)

# script.md
out = ["# Script — La Brigade augmentée", "",
       "Texte de la BD, dans l'ordre, sans ajout. Chaque ligne : identifiant du plan · personnage · intention.",
       "Les titres (couverture, cartes, titres de partie) sont à l'écran, sans voix.", ""]
cur = None
for s in shots:
    if s["part"] != cur:
        cur = s["part"]
        out += ["", f"## {cur}", ""]
    if s["type"] == "titre":
        out.append(f"- `{s['id']}` · *à l'écran* — {s['text']}")
    else:
        who = "MICKAEL (récit)" if s["type"] == "recit" else s["speaker"]
        out.append(f"- `{s['id']}` · **{who}** · _{s['intent']}_ — {s['text']}")
open(os.path.join(ROOT, "script.md"), "w").write("\n".join(out) + "\n")
print(f"{len(manifest)} répliques · {sum(len(m['tts_text']) for m in manifest)} caractères envoyés au TTS")
