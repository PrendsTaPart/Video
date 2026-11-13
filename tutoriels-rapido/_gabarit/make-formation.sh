#!/usr/bin/env bash
# Chaîne complète d'une formation métier (motion design), une fois la voix déposée dans <EP>/audio/voix.mp3.
# Usage : bash _gabarit/make-formation.sh F21
set -euo pipefail
cd "$(dirname "$0")/.."
EP="$1"
test -f "$EP/audio/voix.mp3" || { echo "voix manquante"; exit 1; }
[ -f "$EP/audio/transcript.json" ] || (cd "$EP/audio" && npx -y hyperframes transcribe voix.mp3 --model small --language fr >/dev/null)
python3 _gabarit/para-times.py "$EP"
python3 _gabarit/build-formation.py "$EP"
mkdir -p ../videos/tutoriels-rapido
(cd "$EP" && npx -y hyperframes render --output "../../videos/tutoriels-rapido/$EP.mp4" >/dev/null)
python3 - "$EP" <<'PY'
import json, subprocess, sys
ep = sys.argv[1]; c = json.load(open(f'{ep}/tuto.json'))
subprocess.run(['node', '_gabarit/miniature.cjs', '--product', c.get('product', 'suite'), '--num', c['id'], '--title', c['title'],
                '--em', c.get('em', ''), '--tag', c.get('tag', ''), '--kicker', c['kicker'], '--out', f'{ep}/miniature.png'], check=True)
PY
ffprobe -v error -show_entries format=duration -of csv=p=0 "../videos/tutoriels-rapido/$EP.mp4"
echo "OK $EP"
