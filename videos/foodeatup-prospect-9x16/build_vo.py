#!/usr/bin/env python3
"""Voix off ElevenLabs — une ligne = un fichier, normalisée individuellement.

Nécessite ELEVENLABS_API_KEY (jamais commitée ; le dépôt la range dans
studio-video/.env). Sans la clé, le script s'arrête proprement sans rien casser :
le montage retombe alors sur l'animatique muette.

    export ELEVENLABS_API_KEY=...   # ou: set -a; . ../../studio-video/.env; set +a
    python3 build_vo.py

Produit vo/L*.mp3 + vo/vo_meta.json (durée réelle de chaque ligne), que
build_final.py utilise pour caler les sous-titres au lieu du débit estimé.

Règle du dépôt (FOODEATUP-TUTORIELS-WORKFLOW.md) : loudnorm est appliqué ligne
par ligne AVANT tout mixage — sur le mix composite il sous-estimerait la
loudness à cause des silences et sur-amplifierait la parole.
"""
import os, sys, json, subprocess, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.abspath(__file__))
VO = f"{ROOT}/vo"
API = "https://api.elevenlabs.io/v1/text-to-speech"

def dur(f):
    return float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).strip())

def tts(text, voice_id, model_id, out_raw, key):
    req = urllib.request.Request(
        f"{API}/{voice_id}?output_format=mp3_44100_128",
        data=json.dumps({"text": text, "model_id": model_id,
                         "voice_settings": {"stability": 0.45, "similarity_boost": 0.75,
                                            "style": 0.15, "use_speaker_boost": True}}).encode(),
        headers={"xi-api-key": key, "Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=120) as r, open(out_raw, "wb") as fh:
        fh.write(r.read())

def normalize(src, dst):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src,
                    "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-c:a", "libmp3lame", "-b:a", "192k",
                    dst], check=True)

if __name__ == "__main__":
    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key:
        sys.exit("ELEVENLABS_API_KEY absente — voir l'en-tête de ce fichier.")
    os.makedirs(f"{VO}/raw", exist_ok=True)
    script = json.load(open(f"{ROOT}/script/script.json"))
    voice = script["voice"]
    meta = {"voice": voice, "lines": {}}
    for scene in script["scenes"]:
        for line in scene["vo"]:
            lid = line["id"]
            raw, fin = f"{VO}/raw/{lid}.mp3", f"{VO}/{lid}.mp3"
            if not os.path.exists(fin):
                print(f"[{lid}] {line['text'][:60]}…")
                tts(line["text"], voice["voice_id"], voice["model"], raw, key)
                normalize(raw, fin)
            meta["lines"][lid] = {"scene": scene["id"], "text": line["text"],
                                  "sub": line["sub"], "duration": round(dur(fin), 3)}
    json.dump(meta, open(f"{VO}/vo_meta.json", "w"), ensure_ascii=False, indent=1)
    total = sum(v["duration"] for v in meta["lines"].values())
    print(f"\n{len(meta['lines'])} lignes · {total:.1f}s de voix off -> vo/vo_meta.json")
