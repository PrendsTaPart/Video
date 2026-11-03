#!/bin/bash
# Monte l'atelier de montage du journal : moteur + images du site + dépendances.
# Usage : bash videos/_moteur/preparer-atelier.sh [dossier]   (défaut : ~/atelier-journal)
# Relancer après chaque nouveau thème Lovable : il ne télécharge que les images manquantes.
set -e
ICI="$(cd "$(dirname "$0")" && pwd)"
A="${1:-$HOME/atelier-journal}"
mkdir -p "$A/kit"
cp "$ICI"/kit.js "$ICI"/kit.css "$ICI"/mk.py "$ICI"/mkspec.py "$ICI"/trd.py "$ICI"/tr.py "$ICI"/render.js "$ICI"/stills.js "$ICI"/sheet.sh "$ICI"/fin.py "$A"/
cp "$ICI"/../planit-academy/assets/audio/musique-produit.mp3 "$A"/musique-produit.mp3
chmod +x "$A"/sheet.sh
# images du kit : la liste versionnée + toute image nouvelle repérée dans la médiathèque (voir PROMPT-REPRISE-JOURNAL.md §6)
LISTE="${LISTE:-$ICI/kit-liste.txt}"
n=0
while read -r f; do [ -s "$A/kit/$f" ] || { echo "$f"; }; done < "$LISTE" > "$A/.a-telecharger"
n=$(wc -l < "$A/.a-telecharger")
echo "images à télécharger : $n"
cat "$A/.a-telecharger" | xargs -P 8 -I{} sh -c 'curl -fsS --retry 3 -o "'"$A"'/kit/{}" "https://michael.foodeatup.fr/img/kit/{}" || echo "ÉCHEC {}"'
rm -f "$A/.a-telecharger"
# dépendances (une seule fois)
python3 -c "import faster_whisper" 2>/dev/null || pip install -q faster-whisper numpy
node -e "require('playwright')" 2>/dev/null || echo "playwright absent : voir le guide de l'environnement (il est préinstallé en session cloud)"
command -v ffmpeg >/dev/null || echo "ffmpeg absent"
echo "Atelier prêt : $A  (images : $(ls "$A/kit" | wc -l))"
