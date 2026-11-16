#!/usr/bin/env bash
# Refait seulement le rendu et la miniature d'épisodes déjà tournés (captures/ecran.mp4 présent),
# après un rendu échoué (disque plein, navigateur de rendu planté…). Ne refilme rien, ne touche pas à la voix.
# Usage : bash _gabarit/rendu-seul.sh CRM69 [CRM..]
cd "$(dirname "$0")/.."
for EP in "$@"; do
  test -f "$EP/captures/ecran.mp4" || { echo "$EP : pas de tournage, utiliser file.sh"; continue; }
  test -f "$EP/index.html" || python3 _gabarit/build-tutoriel.py "$EP"
  (cd "$EP" && npx -y hyperframes render --output "../../videos/tutoriels-rapido/$EP.mp4" >/dev/null) || { echo "$EP : rendu en échec"; continue; }
  python3 - "$EP" <<'PY'
import json, subprocess, sys
ep = sys.argv[1]
c = json.load(open(f'{ep}/tuto.json'))
subprocess.run(['node', '_gabarit/miniature.cjs', '--product', c['product'], '--num', c['id'], '--title', c['title'], '--em', c.get('em', ''),
                '--tag', c.get('tag', ''), '--kicker', c['kicker'], '--shot', f'{ep}/captures/{c.get("thumb_shot", "fin.png")}', '--out', f'{ep}/miniature.png'], check=True)
PY
  echo "OK $EP $(ffprobe -v error -show_entries format=duration -of csv=p=0 ../videos/tutoriels-rapido/$EP.mp4)"
done
