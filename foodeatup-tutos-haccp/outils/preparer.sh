#!/bin/bash
# Copie jetable de l'app HACCP + test de capture des tutoriels, puis rendu des images.
# Usage : outils/preparer.sh <dossier de l'app> <dossier de sortie>
set -e
APP=$1; OUT=$2; ICI=$(cd "$(dirname "$0")" && pwd)
W=$(mktemp -d)/app; cp -r "$APP" "$W"
T=$W/test/screenshots/tutos_test.dart
cp "$W/test/screenshots/store_screenshots_test.dart" "$T"
cat >> "$T" <<'IMP'
IMP
python3 - "$T" "$ICI/tutos_part.dart" <<'PY'
import sys,re
t=open(sys.argv[1]).read(); part=open(sys.argv[2]).read()
extra="import 'package:foodeatup_haccp/features/establishment/presentation/establishment_screen.dart';\nimport 'package:foodeatup_haccp/features/cleaning/presentation/cleaning_plan_screen.dart';\nimport 'package:foodeatup_haccp/features/school/presentation/feature_lesson_screen.dart';\nimport 'package:foodeatup_haccp/features/school/presentation/quiz_screen.dart';\nimport 'package:foodeatup_haccp/features/theme/presentation/theme_picker_screen.dart';\nimport 'package:foodeatup_haccp/core/voice/voice_engine.dart';\n"
t=t.replace("import '../helpers/app_harness.dart';", extra+"import '../helpers/app_harness.dart';",1)
# appel de nos tutoriels à la fin de main()
t=t.replace("if (_capture || _whiteDir.isNotEmpty || _storeDir.isNotEmpty)","if (true)")
t=t.replace("void main() {\n","void main() {\n  tutosMain();\n",1)
open(sys.argv[1],'w').write(t+part)
PY
cd "$W" && PATH=/opt/flutter/bin:$PATH flutter test test/screenshots/tutos_test.dart --plain-name "tutoriels" --dart-define=CAPTURE_TUTOS="$OUT" 2>&1 | grep -E "EXCEPTION|ECHEC|Error|error:|passed|failed" | head -40
