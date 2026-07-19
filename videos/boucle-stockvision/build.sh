#!/usr/bin/env bash
# Build reproductible — Boucle StockVisionAI (1920x1080, 60s, voix off + BGM)
set -euo pipefail; cd "$(dirname "$0")"
echo "[1/3] Voix off ElevenLabs (Adam) — 6 blocs"
python3 - <<'PY'
import json,os,urllib.request
env={l.split('=',1)[0]:l.split('=',1)[1].strip().strip('"') for l in open('/home/user/Video/studio-video/.env') if '=' in l and not l.startswith('#')}
KEY=env['ELEVENLABS_API_KEY']; cfg=json.load(open('script/script.json')); vid=cfg['voice']['voice_id']; os.makedirs('work/vo',exist_ok=True)
for b in cfg['blocks']:
    body=json.dumps({"text":b['text'],"model_id":cfg['voice']['model'],"voice_settings":{"stability":0.55,"similarity_boost":0.75,"style":0.1,"use_speaker_boost":True}}).encode()
    r=urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{vid}",data=body,headers={"xi-api-key":KEY,"Content-Type":"application/json","Accept":"audio/mpeg"},method="POST")
    open(f"work/vo/{b['id']}.mp3",'wb').write(urllib.request.urlopen(r,timeout=120).read()); print("  vo",b['id'])
PY
echo "[2/3] Capture 1800 frames (Playwright/Chromium)"
GROOT=$(npm root -g) FRAMES=1800 node capture.cjs
echo "[3/3] Assemblage (frames + VO + BGM)"
python3 build_final.py
echo "OK -> output/boucle-stockvision.mp4"
