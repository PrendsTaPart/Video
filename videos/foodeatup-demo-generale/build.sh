#!/usr/bin/env bash
# Build reproductible — FoodEatUp « Démo générale » (1920x1080, ~1:51, H.264)
# Prérequis : ffmpeg, python3 + Pillow, police Poppins (videos/rapidocms-presentation-4min/assets/fonts),
#             clé ELEVENLABS_API_KEY dans studio-video/.env, assets/ présents.
set -euo pipefail
cd "$(dirname "$0")"

echo "[1/3] Voix off ElevenLabs (Adam) — 7 blocs"
python3 - <<'PY'
import json,os,urllib.request,subprocess
env={l.split('=',1)[0]:l.split('=',1)[1].strip().strip('"') for l in open('/home/user/Video/studio-video/.env') if '=' in l and not l.startswith('#')}
KEY=env['ELEVENLABS_API_KEY']; cfg=json.load(open('script/script.json')); vid=cfg['voice']['voice_id']
os.makedirs('work/vo',exist_ok=True)
for b in cfg['blocks']:
    body=json.dumps({"text":b['text'],"model_id":cfg['voice']['model'],
        "voice_settings":{"stability":0.5,"similarity_boost":0.75,"style":0.15,"use_speaker_boost":True}}).encode()
    r=urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{vid}",data=body,
        headers={"xi-api-key":KEY,"Content-Type":"application/json","Accept":"audio/mpeg"},method="POST")
    open(f"work/vo/{b['id']}.mp3",'wb').write(urllib.request.urlopen(r,timeout=120).read())
    print("  vo",b['id'])
PY

echo "[2/3] Séquences (cartes typo + Ken Burns + mascottes + Jarvis)"
python3 build_seqs.py

echo "[3/3] Assemblage final (xfade + sous-titres + VO + BGM + poster)"
python3 build_final.py

echo "OK -> output/demo-generale.mp4 + output/demo-generale-poster.jpg"
