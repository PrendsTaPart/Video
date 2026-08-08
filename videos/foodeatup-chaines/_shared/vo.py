#!/usr/bin/env python3
"""
Génère la voix off des deux variantes et calcule le recalage des scènes.

    ELEVENLABS_API_KEY=... python3 vo.py            # génère + mesure

Règle C0 : « Génère la VO AVANT la composition : sa durée réelle fixe les
data-duration. » Les durées de scène du premier jet (15/13/5/12/10) étaient
provisoires ; ce script mesure chaque ligne et sort les durées à appliquer.

La clé API n'est JAMAIS écrite ici : elle vient de l'environnement.
"""

import json
import os
import pathlib
import re
import subprocess
import sys

FF = "/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "audio"

# Julien — voix masculine française, accent standard, « calme et posé,
# professionnel, clair, articulé ». Retenue contre Paul K (« French Ad &
# Trailer ») : la fiche de Paul K annonce « energetic, persuasive, punchy »,
# l'exact inverse du registre C0, et son débit de bande-annonce mettait 14,3 s
# là où Julien met 8,3 s — il ne tenait pas dans la fenêtre de la séquence 2.
VOICE_ID = "eOwAMwUJEGkP44SKOXIH"
VOICE_NAME = "Julien - Professional customer service"
MODEL = "eleven_multilingual_v2"
SETTINGS = {"stability": 0.55, "similarity_boost": 0.8, "style": 0.0, "use_speaker_boost": True}

AMORCE = 0.8   # la scène s'installe avant que la voix entre
QUEUE = 0.7    # silence en fin de scène avant la coupe
D_ECART = 5.0  # séquence 2b : SANS voix off, le plan qui doit rester en tête

# Version SANS CHIFFRES (SOURCES.md : aucun des 4 chiffres n'a été fourni).
# « plusieurs semaines » partout, jamais « six semaines » : le délai de remontée
# est un chiffre [À CONFIRMER], on pose la question au lieu de l'affirmer.
LIGNES = {
    "boulangerie": [
        ("s1", "Vous savez ce que vos douze magasins ont fait hier. Vous savez ce qu'ils ont "
               "encaissé. Vous ne savez pas ce qu'ils ont jeté."),
        ("s2", "Même production. Mêmes horaires. Même enseigne. Et pourtant, l'écart d'invendus "
               "entre votre meilleur magasin et le dernier, personne dans l'entreprise ne "
               "saurait le donner."),
        ("s4", "Ce n'est pas de la négligence. C'est que chaque responsable commande au labo "
               "selon ce qu'il sent. Douze habitudes, douze vérités, aucune comparable."),
        ("s5", "Et vous ne le découvrez pas ce soir. Vous le découvrez au consolidé, plusieurs "
               "semaines plus tard. Plusieurs semaines pendant lesquelles la même fournée de "
               "trop est repartie chaque matin."),
    ],
    "restauration": [
        ("s1", "Vos douze restaurants servent la même carte. Le même plat, au même prix, partout."),
        ("s2", "Ils ne le produisent pas au même coût. De combien ? Personne dans l'entreprise "
               "ne saurait le dire site par site."),
        ("s4", "Ce n'est pas une question de gestion. C'est que chaque site a sa fiche technique, "
               "son fournisseur, ses grammages. Douze versions du même plat."),
        ("s5", "Et l'écart ne se voit pas dans le chiffre d'affaires. Il se voit dans la marge, "
               "que vous lisez plusieurs semaines plus tard, agrégée, sur une seule ligne."),
    ],
    # Bloc de fin (séquences 7 et 9). La ligne C1 « Vous voyez les trous avant le
    # contrôleur » est VOLONTAIREMENT retirée : c'est une promesse de visibilité
    # conformité au niveau groupe, donc une affirmation sur un écran non vérifié.
    # Ne reste que l'argument de risque de marque, qui n'engage aucun produit.
    "fin": [
        ("s1", "La conformité suit la même logique. Un relevé manqué sur un site n'est pas un "
               "détail local : c'est votre enseigne qui est exposée."),
        ("s2", "Trois sites. Soixante jours. Vos chiffres, pas les nôtres."),
    ],
}


def duree(path: pathlib.Path) -> float:
    out = subprocess.run([FF, "-hide_banner", "-i", str(path)],
                         capture_output=True, text=True).stderr
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", out)
    h, mi, s = m.groups()
    return int(h) * 3600 + int(mi) * 60 + float(s)


def genere(variante: str, key: str) -> dict:
    OUT.mkdir(exist_ok=True)
    durees = {}
    for scene, texte in LIGNES[variante]:
        dest = OUT / f"vo-{variante}-{scene}.mp3"
        payload = OUT / "_payload.json"
        payload.write_text(json.dumps(
            {"text": texte, "model_id": MODEL, "voice_settings": SETTINGS}))
        r = subprocess.run(
            ["curl", "-sS", "-m", "180", "-X", "POST",
             f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}",
             "-H", f"xi-api-key: {key}", "-H", "Content-Type: application/json",
             "--data", f"@{payload}", "-o", str(dest), "-w", "%{http_code}"],
            capture_output=True, text=True)
        payload.unlink()
        if r.stdout.strip() != "200":
            sys.exit(f"échec TTS {variante}/{scene} : HTTP {r.stdout}")
        durees[scene] = duree(dest)
        print(f"  {variante:12s} {scene}  {durees[scene]:5.2f}s  {len(texte):3d} car.")
    return durees


def recalage(durees: dict) -> dict:
    """Durée de scène = amorce + voix + queue, jamais moins que le plan d'origine."""
    mini = {"s1": 15.0, "s2": 13.0, "s4": 12.0, "s5": 10.0}
    d = {s: max(mini[s], round(AMORCE + durees[s] + QUEUE, 1)) for s in mini}
    d["s3"] = D_ECART
    return d


if __name__ == "__main__":
    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key:
        sys.exit("ELEVENLABS_API_KEY absent de l'environnement")
    print(f"voix : {VOICE_NAME} ({VOICE_ID})  ·  {MODEL}\n")
    cibles = sys.argv[1:] or ["boulangerie", "restauration"]
    for v in cibles:
        d = genere(v, key)
        if v == "fin":
            print()
            continue
        r = recalage(d)
        total = r["s1"] + r["s2"] + r["s3"] + r["s4"] + r["s5"]
        print(f"  -> scènes {v}: s1={r['s1']} s2={r['s2']} s3={r['s3']} "
              f"s4={r['s4']} s5={r['s5']}  total={total:.1f}s\n")
