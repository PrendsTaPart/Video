#!/bin/bash
# Captures des tutoriels Recettes dans une COPIE jetable de l'application, sur le jeu fictif.
# preparer.sh <dossier mobile/ de l'app> <dossier de sortie>
set -e
APP="$1"; OUT="$(realpath -m "$2")"; ICI="$(cd "$(dirname "$0")" && pwd)"
TMP=$(mktemp -d); cp -r "$APP"/. "$TMP"/
python3 "$ICI/bistrot_demo.py" "$TMP/assets/demo/mena.json" > /dev/null
# Nom affiché par la session responsable de démo : prénom fictif (copie jetable seulement).
sed -i "s/SessionResponsable('rsm_demo', 'Michael'/SessionResponsable('rsm_demo', 'Camille'/" "$TMP/lib/data/demo_api.dart"
mkdir -p "$TMP/test/tutos" "$OUT"; cp "$ICI/tutos_test.dart" "$TMP/test/tutos/"
cd "$TMP"; export PATH=/opt/flutter/bin:$PATH
flutter pub get > /dev/null 2>&1
flutter test test/tutos/tutos_test.dart --dart-define=CAPTURE_TUTOS="$OUT" 2>&1 | grep -E "^[0-9:]+ \+|Bad state|No element|Exception|tutos_test.dart:[0-9]+" | tail -40
rm -rf "$TMP"
