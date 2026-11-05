// Captures du tutoriel « Espace gérant » de la tablette fidélité, étape par étape.
// Copié dans test/captures/ d'une copie jetable de l'application (données de démonstration).
import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import '../widget/tutoriels_test.dart' show ouvrirGerant;

final String sortie = Platform.environment['SORTIE'] ?? '/tmp/fid-gerant';
final List<List<Object?>> plans = [];
int n = 0;

Future<void> shot(WidgetTester tester, {Finder? tap, bool hold = false}) async {
  final fichier = 'gerant-${(n++).toString().padLeft(2, '0')}.png';
  autoUpdateGoldenFiles = true;
  await expectLater(find.byType(MaterialApp), matchesGoldenFile(Uri.file('$sortie/$fichier')));
  autoUpdateGoldenFiles = false;
  double? x, y;
  if (tap != null) {
    final taille = tester.view.physicalSize / tester.view.devicePixelRatio;
    final p = tester.getCenter(tap.first);
    x = double.parse((p.dx / taille.width).toStringAsFixed(3));
    y = double.parse((p.dy / taille.height).toStringAsFixed(3));
    await tester.tap(tap.first);
    for (var i = 0; i < 10; i++) {
      await tester.pump(const Duration(milliseconds: 100));
    }
  }
  plans.add([fichier, x, y]);
}

void main() {
  tearDownAll(() => File('$sortie/manifeste.json').writeAsStringSync(jsonEncode({'app-fidelite-espace-gerant': plans})));

  testWidgets('espace gérant', (tester) async {
    Directory(sortie).createSync(recursive: true);
    await ouvrirGerant(tester);
    for (final s in ['etablissement', 'apparence', 'programme', 'roue', 'tablettes', 'import']) {
      await shot(tester, tap: find.byKey(ValueKey('nav-$s')));
    }
    await shot(tester);
  });
}
