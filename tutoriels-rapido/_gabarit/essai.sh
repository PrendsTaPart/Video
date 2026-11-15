#!/bin/bash
# Tournage d'essai d'un épisode RH (sans montage ni rendu) : base remise à zéro, liens, hook, capture, images clés.
# Usage : bash _gabarit/essai.sh RH07   → <EP>/captures/ecran.webm + /tmp/claude-0/essai/<EP>-<paragraphe>.png
set -e
cd "$(dirname "$0")/.."
EP="$1"; G=_gabarit
bash $G/demo-rh.sh 2>&1 | grep -E "^ok|ERROR" || true
bash $G/liens-rh.sh "$EP"
[ -f "$G/avant-$EP.sh" ] && bash "$G/avant-$EP.sh"
LOGIN=$(python3 -c "import json;print(json.load(open('$EP/tuto.json')).get('login_as','camille@studio-demo.test'))")
rm -rf "$EP/captures"
python3 $G/para-times.py "$EP" >/dev/null
node $G/record.cjs "$EP" http://127.0.0.1:8000 "$LOGIN" 'Demo-Tuto-2026!'
mkdir -p /tmp/claude-0/essai
python3 - "$EP" <<'PY'
import json, subprocess, sys
ep = sys.argv[1]
t = json.load(open(f'{ep}/captures/timing.json')); s = t['voiceStartInCapture']; P = t['paragraphs']
keys = [k for k in P if k not in ('end',)]
for i, k in enumerate(keys):
    nxt = P[keys[i + 1]] if i + 1 < len(keys) else P.get('end', P[k] + 4)
    at = s + (P[k] + nxt) / 2 + 0.6
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{at:.2f}', '-i', f'{ep}/captures/ecran.webm', '-frames:v', '1', '-vf', 'scale=960:-1', f'/tmp/claude-0/essai/{ep}-{i}-{k}.png'])
print('zones', list(t['zones']))
PY
