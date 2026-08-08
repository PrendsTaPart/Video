#!/usr/bin/env python3
"""Musique et bruitages du volet « sans ». Générés une fois, partagés par neuf.

NOTES §6.3 fixe le registre sonore : « même tonalité désaccordée d'un quart de
ton, sans résolution », puis, sur le carton final, « la musique "avec" reprend
sur sa tonique — la résolution musicale est l'argument ».

On ne désaccorde pas un lit existant par traitement : un `asetrate` change
aussi le tempo, et un ré-échantillonnage laisse des artefacts qui s'entendent
sur un plan tenu cinquante secondes. On demande directement un lit **non
résolu** — une boucle qui tourne sans jamais retomber sur sa fondamentale. Le
carton final, lui, reçoit la cadence : c'est le seul accord qui se referme de
tout le film, et c'est là toute la démonstration.

Trois lits, un par phase, partagés par les trois métiers : ce qui distingue
les films entre eux est le texte, pas la couleur sonore, et neuf lits
différents feraient neuf films au lieu d'une série.

⚠️ Les niveaux rendus par l'API sont très inégaux d'une génération à l'autre —
de −1 dB à −69 dB sur les campagnes précédentes. Ce script **mesure** chaque
fichier et refuse ceux qui sont inaudibles, plutôt que de les normaliser :
normaliser un fichier à −69 dB ne fait qu'amplifier son souffle.

Usage : python3 _serie/audio-sans.py
"""

import json
import os
import pathlib
import subprocess
import sys
import urllib.request

ICI = pathlib.Path(__file__).resolve().parent
OUT = ICI.parents[2] / "studio-video" / "assets" / "audio" / "sans"

# Un lit trop court se répète de façon audible ; 70 s couvrent le plus long
# des neuf films sans boucler une seule fois.
LITS = {
    "lit-avant": (
        "Sparse, unresolved ambient bed in D minor for a documentary about "
        "administrative fatigue. Muted electric piano and a low sustained "
        "drone. The phrase never returns to its tonic — it hangs on the "
        "subdominant and starts again. Slightly cold, patient, no percussion, "
        "no melody, no build, no resolution.", 70000),
    "lit-pendant": (
        "Restless unresolved ambient bed in D minor. Short repeating muted "
        "piano figure that keeps being interrupted before it lands, faint "
        "irregular ticking, low drone underneath. Tense but flat — busy "
        "without ever arriving. No drums, no melody, no climax, no resolution.",
        70000),
    "lit-apres": (
        "Very sparse, tired unresolved ambient bed in D minor. Long low "
        "sustained tones, a single muted piano note repeating at irregular "
        "intervals, faint room tone. Late-evening emptiness. The harmony never "
        "resolves. No drums, no melody, no build.", 70000),
    # Le seul accord qui se referme de tout le volet.
    "resolution": (
        "Warm resolving cadence in D minor moving home to its tonic, then held. "
        "Muted electric piano and soft strings, a single clear resolution that "
        "settles and opens up. Hopeful, calm, uncluttered. Eight seconds, no "
        "drums, no vocals.", 9000),
}

# Bruitages. Volontairement secs et sans matière : le monde « sans » n'a pas
# de confort sonore.
SFX = {
    "frappe": ("A single dry mechanical keyboard keystroke, close mic, no "
               "reverb, no room tone", 0.5),
    "papier": ("A single sheet of paper being turned over on a hard counter, "
               "dry, close, no music", 0.9),
    # 0,5 s est le plancher de l'API : en dessous, elle répond 400 sans le dire.
    "clic-mat": ("One dull flat mouse click, muffled, no reverb", 0.5),
    "soupir-machine": ("A short low electrical hum swelling and stopping "
                       "abruptly, like an old machine giving up", 1.6),
}

SEUIL_DB = -35.0  # en dessous, la génération est ratée, pas faible


def api(chemin, charge, sortie, cle):
    if sortie.exists() and sortie.stat().st_size > 8000:
        return False
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/{chemin}",
        data=json.dumps(charge).encode(),
        headers={"xi-api-key": cle, "Content-Type": "application/json"},
        method="POST")
    try:
        with urllib.request.urlopen(req, timeout=420) as r:
            sortie.write_bytes(r.read())
    except urllib.error.HTTPError as e:
        # Le corps de la réponse dit ce qui ne va pas ; l'exception seule ne
        # donne qu'un « 400 Bad Request » qui n'aide personne.
        raise SystemExit(f"{sortie.name} : {e.code} — {e.read().decode()[:400]}")
    return True


def crete(f):
    txt = subprocess.run(
        ["ffmpeg", "-nostdin", "-hide_banner", "-i", str(f),
         "-af", "volumedetect", "-f", "null", "-"],
        capture_output=True, text=True).stderr
    for l in txt.splitlines():
        if "max_volume" in l:
            return float(l.split(":")[1].strip().split()[0])
    return None


def main():
    cle = os.environ.get("ELEVENLABS_API_KEY")
    if not cle:
        sys.exit("ELEVENLABS_API_KEY absente de l'environnement")
    OUT.mkdir(parents=True, exist_ok=True)

    rates = []
    for nom, (prompt, ms) in LITS.items():
        f = OUT / f"{nom}.mp3"
        api("music", {"prompt": prompt, "music_length_ms": ms}, f, cle)
        rates.append((nom, f))
    for nom, (prompt, sec) in SFX.items():
        f = OUT / f"{nom}.mp3"
        api("sound-generation",
            {"text": prompt, "duration_seconds": sec, "prompt_influence": .55},
            f, cle)
        rates.append((nom, f))

    mauvais = []
    for nom, f in rates:
        db = crete(f)
        d = float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", str(f)], capture_output=True, text=True).stdout)
        etat = "ok" if db is not None and db > SEUIL_DB else "INAUDIBLE"
        if etat != "ok":
            mauvais.append(nom)
        print(f"  {nom:16} {d:6.2f} s  crête {db:6.1f} dB  {etat}")

    if mauvais:
        print("\nÀ régénérer (supprimer le fichier puis relancer) : "
              + ", ".join(mauvais))
        sys.exit(1)


if __name__ == "__main__":
    main()
