// Captures des tutoriels de l'application Recettes, étape par étape (tablette).
// Jeu de données FICTIF « Bistrot de l'École » (bistrot_demo.py) à la place des
// fiches de démonstration, dans une copie jetable de l'application.
import 'dart:convert';
import 'dart:io';

import 'package:clock/clock.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:foodeatup_recettes/app/etat.dart';
import 'package:foodeatup_recettes/data/demo_api.dart';

import '../aide.dart';

const Size taille = Size(1440, 900);
final String sortie = const String.fromEnvironment('CAPTURE_TUTOS', defaultValue: '/tmp/tutos-rec');
final Map<String, List<List<Object?>>> manifeste = {};

class Tuto {
  Tuto(this.cle, this.tester, this.c);
  final String cle;
  final WidgetTester tester;
  final ProviderContainer c;
  int n = 0;

  Future<void> shot({Finder? tap}) async {
    if (tap != null) {
      await tester.ensureVisible(tap.first);
      await attendre(tester);
    }
    final fichier = '$cle-${(n++).toString().padLeft(2, '0')}.png';
    autoUpdateGoldenFiles = true;
    await expectLater(find.byType(MaterialApp), matchesGoldenFile(Uri.file('$sortie/$fichier')));
    autoUpdateGoldenFiles = false;
    double? x, y;
    if (tap != null) {
      final p = tester.getCenter(tap.first);
      x = double.parse((p.dx / taille.width).toStringAsFixed(3));
      y = double.parse((p.dy / taille.height).toStringAsFixed(3));
    }
    (manifeste[cle] ??= []).add([fichier, x, y]);
    if (tap != null) {
      await tester.tap(tap.first);
      await attendre(tester);
    }
  }

  Future<void> va(String chemin) => aller(tester, c, chemin);
}

Future<Tuto> ouvrir(WidgetTester tester, String cle, {bool connecte = true}) async {
  final c = await lancer(tester, taille: taille);
  if (connecte) {
    await tester.runAsync(() => c.read(appliProvider.notifier).connecter(101, DemoRecettesApi.codeDemoEmploye));
    await aller(tester, c, '/');
  }
  return Tuto(cle, tester, c);
}

Future<void> tuto(String nom, Future<void> Function(WidgetTester) corps) =>
    Future.sync(() => testWidgets(nom, (tester) async => withClock(Clock.fixed(DateTime(2026, 11, 5, 9, 30)), () => corps(tester))));

void main() {
  tearDownAll(() {
    Directory(sortie).createSync(recursive: true);
    File('$sortie/manifeste.json').writeAsStringSync(const JsonEncoder.withIndent(' ').convert(manifeste));
  });

  tuto('se connecter', (tester) async {
    final t = await ouvrir(tester, 'app-recettes-qui-es-tu', connecte: false);
    await t.shot(tap: find.text('Camille'));
    for (final d in DemoRecettesApi.codeDemoEmploye.split('').take(3)) {
      await tester.tap(find.text(d).last);
      await tester.pump();
    }
    await t.shot(tap: find.text('4').last);
    await t.va('/');
    await t.shot();
    await fermer(tester, t.c);
  });

  tuto('trouver', (tester) async {
    final t = await ouvrir(tester, 'app-recettes-trouver-une-recette');
    await t.shot(tap: find.text('Plats du midi'));
    await t.shot(tap: find.text('Croque-monsieur'));
    await t.shot();
    await fermer(tester, t.c);
  });

  tuto('etapes', (tester) async {
    final t = await ouvrir(tester, 'app-recettes-suivre-les-etapes');
    await t.va('/recette/9002/preparer');
    await t.shot();
    await t.va('/recette/9002/etapes');
    await t.shot(tap: find.text('Suivant'));
    await t.shot(tap: find.text('Suivant'));
    await t.va('/recette/9002/fini');
    await t.shot();
    await fermer(tester, t.c);
  });

  tuto('allergenes', (tester) async {
    final t = await ouvrir(tester, 'app-recettes-allergenes-et-recherche');
    await t.va('/allergenes');
    await t.shot();
    await t.va('/recherche');
    await tester.enterText(find.byType(TextField).first, 'citron');
    await attendre(tester);
    await t.shot();
    await fermer(tester, t.c);
  });

  tuto('etiquette', (tester) async {
    final t = await ouvrir(tester, 'app-recettes-etiquette-dlc');
    await t.va('/recette/9010');
    await t.shot();
    await t.va('/recette/9010/etiquette');
    await t.shot();
    await fermer(tester, t.c);
  });

  tuto('formation', (tester) async {
    final t = await ouvrir(tester, 'app-recettes-parcours-et-quiz');
    await t.va('/formation');
    await t.shot();
    await t.va('/quiz/9004');
    await t.shot();
    await fermer(tester, t.c);
  });

  tuto('ecole', (tester) async {
    final t = await ouvrir(tester, 'app-recettes-mode-ecole');
    await t.va('/ecole');
    await t.shot();
    await t.va('/ecole/mission/visite_accueil');
    await t.shot();
    await t.va('/ecole/badge');
    await t.shot();
    await fermer(tester, t.c);
  });

  tuto('responsable', (tester) async {
    final t = await ouvrir(tester, 'app-recettes-espace-responsable');
    await t.va('/responsable');
    await t.shot();
    await tester.runAsync(() => t.c.read(appliProvider.notifier).ouvrirResponsable(DemoRecettesApi.codeDemoResponsable));
    await t.va('/responsable');
    await t.shot();
    await t.va('/responsable/equipe');
    await t.shot();
    await fermer(tester, t.c);
  });

  tuto('couts', (tester) async {
    final t = await ouvrir(tester, 'app-recettes-couts-et-marges');
    await tester.runAsync(() => t.c.read(appliProvider.notifier).ouvrirResponsable(DemoRecettesApi.codeDemoResponsable));
    await t.va('/responsable/couts');
    await t.shot();
    await t.va('/responsable/cout/9008');
    await t.shot();
    await fermer(tester, t.c);
  });

  tuto('export', (tester) async {
    final t = await ouvrir(tester, 'app-recettes-fiches-pdf');
    await tester.runAsync(() => t.c.read(appliProvider.notifier).ouvrirResponsable(DemoRecettesApi.codeDemoResponsable));
    await t.va('/responsable/export?recettes=9008,9009,9010');
    await t.shot();
    await pousser(tester, t.c, '/responsable/modeles-pdf');
    await t.shot();
    await fermer(tester, t.c);
  });

  tuto('valider', (tester) async {
    final t = await ouvrir(tester, 'app-recettes-valider-un-employe');
    await tester.runAsync(() => t.c.read(appliProvider.notifier).ouvrirResponsable(DemoRecettesApi.codeDemoResponsable));
    await t.va('/responsable/valider?employe=101');
    await t.shot();
    await fermer(tester, t.c);
  });

  tuto('langue', (tester) async {
    final t = await ouvrir(tester, 'app-recettes-langue');
    await t.va('/langue');
    await t.shot();
    await fermer(tester, t.c);
  });
}
