
// ---------------------------------------------------------------------------
// Tutoriels vidéo (dépôt Video, foodeatup-tutos-haccp/outils) : une image par
// étape, rendue par les vrais écrans de l'app avec les données de démonstration.
// Lancement : --dart-define=CAPTURE_TUTOS=<dossier>. Ce bloc est ajouté à une
// copie jetable de store_screenshots_test.dart : le dépôt de l'app n'est jamais modifié.
const _tutosDir = String.fromEnvironment('CAPTURE_TUTOS');

Future<void> _tuto(
  WidgetTester tester,
  String name,
  Widget screen, {
  Future<void> Function()? act,
  AppLanguage language = AppLanguage.fr,
  HaccpThemeSpec? theme,
  StubRpc? rpc,
  SpeechInput? speech,
  bool connected = true,
  bool withEstablishment = true,
  bool withEmployee = true,
}) async {
  tester.view.physicalSize = const Size(1080, 1920);
  tester.view.devicePixelRatio = _pixelRatio;
  final key = GlobalKey();
  final store = await seededStore(
    connected: connected,
    establishmentId: withEstablishment ? 900 : null,
    establishmentName: withEstablishment ? 'Bistrot de l\'École' : null,
    employeeId: withEmployee ? 121 : null,
    employeeName: withEmployee ? 'Sami Ali' : null,
    employeeRole: withEmployee ? 'Chef de cuisine' : null,
  );
  final db = memoryDatabase();
  addTearDown(db.close);
  await tester.pumpWidget(
    RepaintBoundary(
      key: key,
      child: harness(
        child: screen,
        rpc: rpc ?? _DemoRpc(_demo()),
        store: store,
        db: db,
        language: language,
        theme: theme,
        speech: speech,
        tts: speech == null ? null : FakeSpeechOutput(),
      ),
    ),
  );
  await tester.pumpAndSettle();
  if (act != null) {
    try {
      await act();
      await tester.pumpAndSettle();
      final ex = tester.takeException();
      // ignore: avoid_print
      if (ex != null) print('EXCEPTION $name : $ex');
    } catch (e) {
      // ignore: avoid_print
      print('ECHEC-ACTION $name : $e');
    }
  }
  await tester.pump(const Duration(milliseconds: 500));
  await tester.runAsync(() async {
    final boundary = key.currentContext!.findRenderObject()! as RenderRepaintBoundary;
    final image = await boundary.toImage(pixelRatio: _pixelRatio);
    final bytes = await image.toByteData(format: ui.ImageByteFormat.png);
    Directory(_tutosDir).createSync(recursive: true);
    File('$_tutosDir/$name.png').writeAsBytesSync(bytes!.buffer.asUint8List());
  });
  // Fin de l'écran : on démonte pour repartir propre.
  await tester.pumpWidget(const SizedBox());
}

void tutosMain() {
  testWidgets('tutoriels vidéo : une image par étape', (tester) async {
    Future<void> tap(String text) async {
      await tester.tap(find.text(text).first);
      await tester.pumpAndSettle();
    }

    Future<void> scroll([double dy = -700]) async {
      await tester.drag(find.byType(Scrollable).first, Offset(0, dy));
      await tester.pumpAndSettle();
    }

    Future<void> keys(List<String> ks) async {
      for (final k in ks) {
        await tester.tap(find.widgetWithText(InkWell, k));
      }
      await tester.pumpAndSettle();
    }

    Future<void> s(String name, Widget screen, {Future<void> Function()? act, AppLanguage language = AppLanguage.fr,
        HaccpThemeSpec? theme, SpeechInput? speech, bool connected = true, bool est = true, bool emp = true}) =>
        _tuto(tester, name, screen, act: act, language: language, theme: theme, speech: speech,
            connected: connected, withEstablishment: est, withEmployee: emp);

    // 1. Installer et se connecter
    await s('01-installer-a', const ConnectScreen(), connected: false, est: false, emp: false);
    await s('01-installer-b', const EstablishmentScreen(), est: false, emp: false);
    await s('01-installer-c', const IdentifyScreen(), emp: false);
    await s('01-installer-d', const HomeScreen());
    // 2. Température
    await s('02-temperature-a', const TemperatureEquipmentsScreen());
    await s('02-temperature-b', const TemperatureEntryScreen(equipmentId: 12));
    await s('02-temperature-c', const TemperatureEntryScreen(equipmentId: 12), act: () => keys(['3', ',', '2']));
    await s('02-temperature-d', const TemperatureEntryScreen(equipmentId: 12), act: () => keys(['7', ',', '5']));
    // 3. Jarvis
    await s('03-jarvis-a', const JarvisScreen(autoStart: false));
    await s('03-jarvis-b', const JarvisScreen(autoStart: false),
        speech: _WaitingSpeech(['frigo deux, trois degrés']),
        act: () async => tester.tap(find.bySemanticsLabel('Micro Jarvis')));
    await s('03-jarvis-c', const JarvisScreen(autoStart: false),
        speech: _WaitingSpeech(['frigo deux, trois degrés', 'oui']),
        act: () async => tester.tap(find.bySemanticsLabel('Micro Jarvis')));
    // 4. Étiquette DLC
    await s('04-etiquette-a', const LabelScreen());
    await s('04-etiquette-b', const LabelScreen(), act: () async {
      await tester.enterText(find.byType(TextField).first, 'Crème pâtissière');
      tester.binding.focusManager.primaryFocus?.unfocus();
    });
    await s('04-etiquette-c', const LabelScreen(), act: () async {
      await tester.enterText(find.byType(TextField).first, 'Crème pâtissière');
      tester.binding.focusManager.primaryFocus?.unfocus();
      await tester.pumpAndSettle();
      await tap('Lait');
      await tap('Œufs');
    });
    await s('04-etiquette-d', const LabelScreen(), act: () async {
      await tester.enterText(find.byType(TextField).first, 'Crème pâtissière');
      tester.binding.focusManager.primaryFocus?.unfocus();
      await tester.pumpAndSettle();
      await tap('Lait');
      await tap('Œufs');
      await scroll(-1400);
    });
    // 5. Produits ouverts
    await s('05-produits-a', const OpenProductsScreen());
    await s('05-produits-b', const OpenProductsScreen(), act: () => scroll(-600));
    // 6. Réception
    await s('06-reception-a', const ReceptionScreen());
    await s('06-reception-b', const ReceptionScreen(), act: () => tap('Conforme'));
    await s('06-reception-c', const ReceptionScreen(), act: () => tap('Non conforme'));
    await s('06-reception-d', const ReceptionScreen(), act: () async {
      await tap('Non conforme');
      await scroll(-900);
    });
    // 7. Traçabilité
    await s('07-tracabilite-a', const TraceScreen());
    await s('07-tracabilite-b', const TraceFormScreen());
    await s('07-tracabilite-b2', const TraceFormScreen(), act: () async {
      await tester.enterText(find.byType(TextField).first, 'Filet de saumon');
      tester.binding.focusManager.primaryFocus?.unfocus();
    });
    await s('07-tracabilite-c', const TraceScreen(), act: () => tap('Compléter'));
    await s('07-tracabilite-d', const TraceScreen(), act: () => tap('Complétées'));
    // 8. Plan de nettoyage
    await s('08-nettoyage-a', const CleaningScreen());
    await s('08-nettoyage-b', const CleaningScreen(), act: () => tap('Plans de travail'));
    await s('08-nettoyage-c', const CleaningPlanScreen());
    // 9. Hygiène
    await s('09-hygiene-a', const HygieneScreen());
    final lists = await tester.runAsync(() => SandboxRpc().call('list_hygiene_checklists', {'establishment_id': 900}));
    final items = (lists!['items'] ?? lists['data'] ?? const []) as List;
    final tenue = items.cast<Map>().firstWhere((m) => m['nom_point_controle'] == 'Tenue et hygiène du personnel')['id'] as int;
    await s('09-hygiene-b', HygieneCheckScreen(templateId: tenue));
    await s('09-hygiene-b2', HygieneCheckScreen(templateId: tenue), act: () async {
      for (var i = 0; i < 4; i++) {
        await tester.tap(find.text('Oui').at(i));
        await tester.pumpAndSettle();
      }
    });
    await s('09-hygiene-b3', HygieneCheckScreen(templateId: tenue), act: () async {
      for (var i = 0; i < 4; i++) {
        await tester.tap(find.text('Oui').at(i));
        await tester.pumpAndSettle();
      }
      await scroll(-900);
    });
    await s('09-hygiene-c', const HygieneScreen(), act: () => tap('Locaux'));
    // 10. Huiles
    await s('10-huiles-a', const OilScreen());
    await s('10-huiles-b', const OilScreen(), act: () => tap('Test polaires'));
    await s('10-huiles-c', const OilScreen(), act: () => tap('Remplacement'));
    // 11. Refroidissement
    await s('11-refroidissement-a', const ThermalScreen());
    await s('11-refroidissement-b', const ThermalScreen(), act: () async {
      final fields = find.byType(TextField);
      await tester.enterText(fields.at(0), 'Blanquette de veau');
      await tester.enterText(fields.at(1), '12');
      await tester.enterText(fields.at(2), '63');
      tester.binding.focusManager.primaryFocus?.unfocus();
      await tester.pumpAndSettle();
    });
    await s('11-refroidissement-c', const ThermalScreen(), act: () async {
      final fields = find.byType(TextField);
      await tester.enterText(fields.at(0), 'Blanquette de veau');
      await tester.enterText(fields.at(1), '12');
      await tester.enterText(fields.at(2), '63');
      tester.binding.focusManager.primaryFocus?.unfocus();
      await tester.pumpAndSettle();
      await tap('Lancer le cycle');
    });
    // 12. Production
    await s('12-production-a', const ProductionScreen());
    await s('12-production-b', const ProductionScreen(), act: () => tap('Valider'));
    // 13. Historique
    await s('13-historique-a', const HistoryScreen());
    await s('13-historique-b', const HistoryScreen(), act: () => tap('7 jours'));
    await s('13-historique-c', const HistoryScreen(), act: () => scroll(-900));
    // 14. Alertes et automatisations
    await s('14-alertes-a', const SettingsScreen(), act: () => scroll(-1800));
    await s('14-alertes-b', const AutomationsScreen());
    await s('14-alertes-c', const AutomationsScreen(), act: () => scroll(-900));
    // 15. Mode école
    await s('15-ecole-a', const SchoolHomeScreen());
    await s('15-ecole-b', const SchoolHomeScreen(), act: () => scroll(-900));
    await s('15-ecole-c', const FeatureLessonScreen(featureId: 'temperature'));
    await s('15-ecole-d', const QuizScreen(featureId: 'temperature'));
    // 16. Langue et thème
    await s('16-langue-a', const SettingsScreen(), act: () => scroll(-500));
    await s('16-langue-b', const HomeScreen(), language: AppLanguage.ta);
    await s('16-langue-c', const HomeScreen(), language: AppLanguage.ar);
    await s('16-langue-d', const ThemePickerScreen());
    await s('16-langue-e', const HomeScreen(),
        theme: const HaccpThemeSpec(id: 'blanc', name: 'Blanc', description: '', palette: HaccpPalette.blanc));
  }, skip: _tutosDir.isEmpty);
}
