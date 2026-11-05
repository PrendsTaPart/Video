#!/bin/bash
# Captures des tutoriels Menu digital dans une COPIE jetable de l'application.
# preparer.sh <dossier de l'app> <dossier de sortie>
set -e
APP="$1"; OUT="$(realpath -m "$2")"; ICI="$(cd "$(dirname "$0")" && pwd)"
TMP=$(mktemp -d); cp -r "$APP"/. "$TMP"/
mkdir -p "$TMP/test/tutos" "$OUT"; cp "$ICI/tutos_test.dart" "$TMP/test/tutos/"
cd "$TMP"; export PATH=/opt/flutter/bin:$PATH
flutter pub get > /dev/null
flutter test test/tutos/tutos_test.dart --dart-define=CAPTURE_TUTOS="$OUT" 2>&1 | grep -E "^[0-9:]+ \+|EXCEPTION|Error|Expected|Which|══|tuto " | tail -60
rm -rf "$TMP"
