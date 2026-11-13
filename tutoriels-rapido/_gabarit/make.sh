#!/usr/bin/env bash
# Chaîne complète d'un épisode, une fois la voix déposée dans <EP>/audio/voix.mp3 :
#   transcription → débuts de paragraphe → tournage → montage → rendu → miniature.
# Usage : bash _gabarit/make.sh CRM03 http://127.0.0.1:8124 demo@rapido.test Demo-Rapido-2026
set -euo pipefail
cd "$(dirname "$0")/.."
EP="$1"; BASE="$2"; EMAIL="${3:-demo@rapido.test}"; PASS="${4:-Demo-Rapido-2026}"
G=_gabarit
test -f "$EP/audio/voix.mp3" || { echo "voix manquante : $EP/audio/voix.mp3"; exit 1; }

if [ ! -f "$EP/audio/transcript.json" ]; then
  (cd "$EP/audio" && npx -y hyperframes transcribe voix.mp3 --model small --language fr >/dev/null)
fi
python3 "$G/para-times.py" "$EP"
node "$G/record.cjs" "$EP" "$BASE" "$EMAIL" "$PASS"
START=$(python3 -c "import json;print(json.load(open('$EP/captures/timing.json'))['voiceStartInCapture'])")
DUR=$(python3 -c "import json;print(json.load(open('$EP/paragraphes.json'))['end']+1.5)")
ffmpeg -v error -y -ss "$START" -i "$EP/captures/ecran.webm" -t "$DUR" -an -c:v libx264 -preset veryfast -crf 18 -pix_fmt yuv420p -r 30 "$EP/captures/ecran.mp4"
python3 "$G/build-tutoriel.py" "$EP"
mkdir -p ../videos/tutoriels-rapido
(cd "$EP" && npx -y hyperframes lint >/dev/null 2>&1 || true; npx -y hyperframes render --output "../../videos/tutoriels-rapido/$EP.mp4" >/dev/null)
python3 - "$EP" <<'PY'
import json, subprocess, sys
ep = sys.argv[1]
c = json.load(open(f'{ep}/tuto.json'))
cmd = ['node', '_gabarit/miniature.cjs', '--product', c['product'], '--num', c['id'], '--title', c['title'],
       '--em', c.get('em', ''), '--tag', c.get('tag', ''), '--kicker', c['kicker'],
       '--shot', f'{ep}/captures/{c.get("thumb_shot", "fin.png")}', '--out', f'{ep}/miniature.png']
subprocess.run(cmd, check=True)
PY
ffprobe -v error -show_entries format=duration -of csv=p=0 "../videos/tutoriels-rapido/$EP.mp4"
echo "OK $EP"
