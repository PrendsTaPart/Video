// Captures du tutoriel 14 « Wi-Fi coupé : la cuisine continue », étape par étape.
// Serveur MCP simulé de l'application (données de démonstration), coupé puis rétabli.
// Copié dans test/widget/ d'une copie jetable de l'application.
import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:foodeatup_kds/core/mcp/simulated_mcp_client.dart';
import 'package:foodeatup_kds/core/providers.dart';
import 'package:foodeatup_kds/core/storage/prefs_store.dart';
import 'package:foodeatup_kds/features/station/station_screen.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../fixtures.dart';
import '../helpers.dart';

const Size taille = Size(1440, 900);
final String sortie = Platform.environment['SORTIE'] ?? '/tmp/kds-hl';
final List<List<Object?>> plans = [];
int n = 0;

Future<void> attendre(WidgetTester t, [int fois = 6]) async {
  for (var i = 0; i < fois; i++) {
    await t.pump(const Duration(milliseconds: 200));
  }
}

Future<void> shot(WidgetTester t, {Finder? tap}) async {
  final f = 'hors-ligne-${(n++).toString().padLeft(2, '0')}.png';
  autoUpdateGoldenFiles = true;
  await expectLater(find.byType(MaterialApp), matchesGoldenFile(Uri.file('$sortie/$f')));
  autoUpdateGoldenFiles = false;
  double? x, y;
  if (tap != null) {
    final p = t.getCenter(tap.first);
    x = double.parse((p.dx / taille.width).toStringAsFixed(3));
    y = double.parse((p.dy / taille.height).toStringAsFixed(3));
    await t.tap(tap.first);
    await attendre(t);
  }
  plans.add([f, x, y]);
}

void main() {
  tearDownAll(() => File('$sortie/manifeste.json').writeAsStringSync(jsonEncode({'app-kds-hors-ligne': plans})));

  testWidgets('hors ligne', (tester) async {
    Directory(sortie).createSync(recursive: true);
    SharedPreferences.setMockInitialValues({PrefsStore.onboardingDone(1): true});
    final prefs = await PrefsStore.open();
    final server = SimulatedMcpClient(now: () => fixedNow);
    tester.view
      ..physicalSize = taille
      ..devicePixelRatio = 1;
    addTearDown(tester.view.reset);
    await tester.pumpWidget(harness(const StationScreen(),
        overrides: [...screenOverrides(prefs: prefs), simulatedServerProvider.overrideWithValue(server)]));
    await attendre(tester);
    await shot(tester);
    server.offline = true;
    await shot(tester, tap: find.text('1× DOUBLE EXPRESSO'));
    await shot(tester, tap: find.text('BUMP'));
    server.offline = false;
    await shot(tester, tap: find.text('1× PISTACHIO LATTE'));
    await shot(tester);
    await tester.pumpWidget(const SizedBox());
    server.dispose();
  });
}
