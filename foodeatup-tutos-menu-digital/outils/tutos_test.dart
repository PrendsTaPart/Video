// Captures des tutoriels du Menu digital, étape par étape.
// Restaurant FICTIF « Bistrot de l'École » (établissement 900) : aucune donnée réelle.
// Copié dans test/tutos/ d'une copie jetable de l'application par preparer.sh.
// CAPTURE_TUTOS=<dossier> flutter test test/tutos/tutos_test.dart
import 'dart:async';
import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:foodeatup_menu_digital/app.dart';
import 'package:foodeatup_menu_digital/core/storage/secure_store.dart';
import 'package:foodeatup_menu_digital/features/cart/cart.dart';
import 'package:foodeatup_menu_digital/features/menu/menu_controller.dart';
import 'package:foodeatup_menu_digital/features/order/c06_suivi_screen.dart';
import 'package:foodeatup_menu_digital/features/staff/staff_mode.dart';
import 'package:foodeatup_menu_digital/features/staff/staff_pin.dart';

import '../helpers/fake_server.dart';
import '../helpers/fonts.dart';
import '../helpers/harness.dart';

const Size taille = Size(1440, 900);
final String sortie = const String.fromEnvironment('CAPTURE_TUTOS', defaultValue: '/tmp/tutos-md');
final Map<String, List<List<Object?>>> manifeste = {};

const String nom = "Bistrot de l'École";

Map<String, dynamic> plat(int id, String name, String price, int cat,
        {bool soldOut = false, List<int> ing = const [], String? description}) =>
    {
      'id': id, 'name': name, 'price': price, 'description': description, 'category_id': cat,
      'sold_out': soldOut, 'portions_vendables': null, 'tva_rate_sur_place': 10, 'tva_rate_emporter': 5.5,
      'has_image': false, 'image_url': null, 'active': true,
      'ingredients': [for (final i in ing) {'ingredient_id': i, 'name': 'ing $i', 'quantity': 1, 'unit': 'g'}],
    };

List<Map<String, dynamic>> plats({Set<int> epuises = const {104}}) => [
      plat(101, 'Café expresso', '1.80', 11, ing: [1], soldOut: epuises.contains(101)),
      plat(102, 'Cappuccino', '3.50', 11, ing: [1, 2], description: 'Expresso, lait mousseux.', soldOut: epuises.contains(102)),
      plat(103, 'Citronnade maison', '3.90', 12, description: 'Citron pressé, menthe fraîche.', soldOut: epuises.contains(103)),
      plat(104, 'Thé glacé pêche', '3.90', 12, soldOut: epuises.contains(104)),
      plat(105, 'Jus de pomme', '3.50', 12, soldOut: epuises.contains(105)),
      plat(201, 'Burger du Bistrot', '14.50', 20, ing: [3, 4, 5], description: 'Bœuf haché, cheddar, oignons confits.', soldOut: epuises.contains(201)),
      plat(202, 'Salade César', '12.00', 20, ing: [6, 7, 3, 8], soldOut: epuises.contains(202)),
      plat(203, 'Croque-monsieur', '9.50', 20, ing: [3, 5], soldOut: epuises.contains(203)),
      plat(301, 'Tarte au citron', '5.50', 30, ing: [3, 8, 2], soldOut: epuises.contains(301)),
      plat(302, 'Mousse au chocolat', '5.00', 30, ing: [8, 2], soldOut: epuises.contains(302)),
    ];

FakeFoodEatUpServer bistrot() {
  final s = FakeFoodEatUpServer(me: {'establishment': {'id': 900, 'name': nom}});
  s.tools['list_dish_categories'] = (_) => {
        'count': 5,
        'data': [
          {'id': 10, 'name': 'Boissons', 'parent_id': null, 'active': true, 'display_order': 1},
          {'id': 11, 'name': 'Boissons chaudes', 'parent_id': 10, 'active': true, 'display_order': 1},
          {'id': 12, 'name': 'Boissons fraîches', 'parent_id': 10, 'active': true, 'display_order': 2},
          {'id': 20, 'name': 'Plats', 'parent_id': null, 'active': true, 'display_order': 2},
          {'id': 30, 'name': 'Desserts', 'parent_id': null, 'active': true, 'display_order': 3},
        ],
      };
  s.tools['list_dishes'] = (_) => {'count': 10, 'data': plats()};
  s.tools['list_option_groups'] = (_) => {
        'groups': [
          {
            'id': 1, 'name': 'Cuisson', 'type': 'choix', 'min': 1, 'max': 1, 'sort': 1, 'is_active': true,
            'items': [
              {'id': 11, 'label': 'Saignant', 'price_delta': 0, 'is_active': true},
              {'id': 12, 'label': 'À point', 'price_delta': 0, 'is_active': true},
              {'id': 13, 'label': 'Bien cuit', 'price_delta': 0, 'is_active': true},
            ],
            'links': [{'id': 1, 'scope': 'plat', 'target_id': 201, 'mode': 'ajoute'}],
          },
          {
            'id': 2, 'name': 'Suppléments', 'type': 'supplement', 'min': 0, 'max': null, 'sort': 2, 'is_active': true,
            'items': [
              {'id': 21, 'label': 'Bacon', 'price_delta': 1.5, 'is_active': true},
              {'id': 22, 'label': 'Œuf au plat', 'price_delta': 1.0, 'is_active': true},
            ],
            'links': [{'id': 2, 'scope': 'plat', 'target_id': 201, 'mode': 'ajoute'}],
          },
          {
            'id': 3, 'name': 'Lait végétal', 'type': 'supplement', 'min': 0, 'max': 1, 'sort': 1, 'is_active': true,
            'items': [
              {'id': 31, 'label': "Lait d'avoine", 'price_delta': 0.4, 'is_active': true},
            ],
            'links': [{'id': 3, 'scope': 'plat', 'target_id': 102, 'mode': 'ajoute'}],
          },
        ],
        'types': {'choix': 'Choix', 'supplement': 'Supplément', 'retrait': 'Retrait'},
      };
  s.tools['list_formules'] = (_) => {
        'data': [
          {
            'id': 5, 'name': 'Menu du midi', 'price': '17.90', 'vendable': true,
            'steps': [
              {'name': 'Plat', 'min': 1, 'max': 1, 'choices': [
                {'dish_id': 201, 'name': 'Burger du Bistrot'}, {'dish_id': 202, 'name': 'Salade César'}, {'dish_id': 203, 'name': 'Croque-monsieur'},
              ]},
              {'name': 'Dessert', 'min': 1, 'max': 1, 'choices': [
                {'dish_id': 301, 'name': 'Tarte au citron'}, {'dish_id': 302, 'name': 'Mousse au chocolat'},
              ]},
            ],
          },
        ],
      };
  s.tools['list_ingredients'] = (_) => {
        'data': [
          {'id': 1, 'name': 'Café', 'allergens': []},
          {'id': 2, 'name': 'Lait entier', 'allergens': ['Lait']},
          {'id': 3, 'name': 'Pain', 'allergens': ['Gluten']},
          {'id': 4, 'name': 'Bœuf haché', 'allergens': []},
          {'id': 5, 'name': 'Cheddar', 'allergens': ['Lait']},
          {'id': 6, 'name': 'Poulet', 'allergens': []},
          {'id': 7, 'name': 'Parmesan', 'allergens': ['Lait']},
          {'id': 8, 'name': 'Œuf', 'allergens': ['Œufs']},
        ],
      };
  s.tools['list_tables'] = (_) => {
        'data': [
          for (var i = 1; i <= 12; i++)
            {'id': 100 + i, 'name': 'T$i', 'zone': 'Salle', 'status': [3, 6, 9].contains(i) ? 'occupied' : 'free'},
          {'id': 87, 'name': 'Borne 1', 'zone': 'Bornes de commande', 'status': 'free'},
        ],
      };
  s.tools['create_order'] = (args) => {'id': 783, 'order_number': 'CMD-DEMO-0001', 'status': 'confirmee'};
  s.tools['get_order'] = (args) => {
        'id': 783, 'order_number': 'CMD-DEMO-0001', 'status': 'en_preparation',
        'items': [
          {'item_id': 1, 'name': 'Burger du Bistrot', 'quantity': 1, 'kds_status': 'in_progress'},
          {'item_id': 2, 'name': 'Citronnade maison', 'quantity': 2, 'kds_status': 'ready'},
        ],
      };
  s.tools['create_notification'] = (args) => {'id': 1};
  s.tools['get_table_status'] = (args) => {
        'summary': 'T7 occupée depuis 12:15, 33,30 € restent dus.',
        'status': 'occupee',
        'tab': {
          'remaining_due': 33.3,
          'bill_requested': false,
          'lines': [
            {'name': 'Burger du Bistrot', 'quantity': 1, 'total': 16.0},
            {'name': 'Citronnade maison', 'quantity': 2, 'total': 7.8},
            {'name': 'Croque-monsieur', 'quantity': 1, 'total': 9.5},
          ],
        },
      };
  s.tools['get_qr_destinations'] = (args) => {
        'destinations': [
          if (args['famille'] == 'payer') {'famille': 'payer', 'label': 'Payer à table', 'url': 'https://bistrot-ecole.exemple/payer/t7', 'actif': true},
          if (args['famille'] == 'jouer') {'famille': 'jouer', 'label': 'Roue du Bistrot', 'url': 'https://bistrot-ecole.exemple/jouer', 'actif': true},
        ],
      };
  s.tools['get_loyalty_program'] = (args) => {'active': true, 'name': 'Club du Bistrot', 'description': '1 point par euro dépensé.'};
  s.tools['list_loyalty_rewards'] = (args) => {
        'data': [
          {'name': 'Café offert', 'points_cost': 50, 'active': true},
          {'name': 'Dessert offert', 'points_cost': 120, 'active': true},
        ],
      };
  final connus = [
    {'id': 77, 'nom': 'Exemple', 'prenom': 'Camille', 'num_tel': '0600000000', 'email': 'camille@exemple.fr'},
  ];
  s.tools['list_clients'] = (args) {
    final q = (args['search'] as String).toLowerCase().replaceAll(' ', '');
    return {'data': [for (final c in connus) if ('${c['num_tel']} ${c['email']}'.replaceAll(' ', '').contains(q)) c]};
  };
  s.tools['create_client'] = (args) => {'id': 5001, ...args};
  s.tools['get_loyalty_account'] = (args) => {'email': args['email'], 'points': 86, 'next_reward': {'name': 'Dessert offert'}};
  s.tools['list_wheel_games'] = (args) => {'data': [{'id': 3, 'name': 'Roue du Bistrot', 'status': 'active'}]};
  s.tools['get_site_status'] = (args) => {'public_url': 'https://bistrot-ecole.exemple'};
  return s;
}

const String tableInstallee =
    '{"authMode":"apiKey","establishmentId":900,"establishmentName":"Bistrot de l\'École","usage":"table","tableId":107,"tableName":"T7","themeChosen":true,"completed":true}';

class Tuto {
  Tuto(this.cle, this.tester);
  final String cle;
  final WidgetTester tester;
  int n = 0;

  /// Capture l'écran ; si [tap] est donné, note le point touché puis touche.
  Future<void> shot({Finder? tap, bool settle = true}) async {
    if (settle) await tester.pumpAndSettle();
    if (tap != null) {
      await tester.ensureVisible(tap.first);
      await tester.pumpAndSettle();
    }
    final fichier = '$cle-${(n++).toString().padLeft(2, '0')}.png';
    autoUpdateGoldenFiles = true;
    await expectLater(find.byType(MaterialApp), matchesGoldenFile(Uri.file('$sortie/$fichier')));
    autoUpdateGoldenFiles = false;
    double? x, y;
    if (tap != null) {
      final c = tester.getCenter(tap.first);
      x = double.parse((c.dx / taille.width).toStringAsFixed(3));
      y = double.parse((c.dy / taille.height).toStringAsFixed(3));
    }
    (manifeste[cle] ??= []).add([fichier, x, y]);
    if (tap != null) {
      await tester.tap(tap.first);
      await tester.pumpAndSettle();
    }
  }
}

Future<(ProviderContainer, FakeFoodEatUpServer, MemorySecureStore)> ouvrir(WidgetTester tester,
    {String? setup = tableInstallee, List overrides = const [], FakeFoodEatUpServer? server, bool connecte = true}) async {
  tester.view.physicalSize = taille;
  tester.view.devicePixelRatio = 1;
  addTearDown(tester.view.reset);
  final s = server ?? bistrot();
  final store = MemorySecureStore();
  if (connecte) {
    store.values[SecureKeys.clientId] = 'demo-id';
    store.values[SecureKeys.clientSecret] = 'demo-secret';
  }
  final c = await testContainer(
    server: s,
    store: store,
    prefs: {if (setup != null) 'menu.setup': setup, if (setup != null) 'menu.theme': '{"mode":"foodeatup"}'},
    overrides: [orderPollingProvider.overrideWithValue(null), ...overrides],
  );
  addTearDown(c.dispose);
  await tester.pumpWidget(UncontrolledProviderScope(container: c, child: const MenuDigitalApp()));
  await tester.pumpAndSettle();
  return (c, s, store);
}

Finder sem(String s) => find.bySemanticsLabel(RegExp('^${RegExp.escape(s)}'));

void main() {
  setUpAll(loadAppFonts);
  tearDownAll(() {
    Directory(sortie).createSync(recursive: true);
    File('$sortie/manifeste.json').writeAsStringSync(const JsonEncoder.withIndent(' ').convert(manifeste));
  });

  testWidgets('tuto installer', (tester) async {
    final t = Tuto('app-menu-digital-installer-et-connecter', tester);
    await ouvrir(tester, setup: null, connecte: false);
    await t.shot(tap: find.text('Clé API (client_id / secret)'));
    await tester.enterText(find.byKey(const Key('client-id-input')), 'demo-id');
    await tester.enterText(find.byKey(const Key('client-secret-input')), 'demo-secret');
    await t.shot(tap: find.text('Connecter la tablette'));
    await t.shot(tap: find.text('Continuer'));
    await t.shot(tap: find.textContaining(nom));
    await t.shot(tap: find.text('Continuer'));
  });

  testWidgets('tuto table et code', (tester) async {
    final t = Tuto('app-menu-digital-table-et-code-personnel', tester);
    await ouvrir(tester, setup: '{"authMode":"apiKey","establishmentId":900,"establishmentName":"Bistrot de l\'École","themeChosen":true}');
    await t.shot(tap: find.text('T7'));
    for (final pass in [0, 1]) {
      for (final d in ['2', '4', '6']) {
        await tester.tap(find.text(d).last);
      }
      await tester.pumpAndSettle();
      await t.shot(tap: find.text('8').last);
      await t.shot(tap: find.bySemanticsLabel('Valider'));
      if (pass == 1) break;
    }
    await t.shot(tap: find.text("Terminer l'installation"));
    await t.shot();
  });

  testWidgets('tuto theme', (tester) async {
    final t = Tuto('app-menu-digital-choisir-son-theme', tester);
    await ouvrir(tester, setup: '{"authMode":"apiKey","establishmentId":900,"establishmentName":"Bistrot de l\'École"}');
    await t.shot(tap: find.text('Brasserie'));
    await t.shot(tap: find.text('Charte libre'));
    await t.shot();
  });

  testWidgets('tuto carte', (tester) async {
    final t = Tuto('app-menu-digital-parcourir-la-carte', tester);
    await ouvrir(tester);
    await t.shot(tap: find.byKey(const Key('see-menu')));
    await t.shot(tap: find.textContaining('Boissons fraîches').first);
    await t.shot(tap: find.text('Plats').first);
    await tester.enterText(find.byType(TextField).first, 'sans gluten');
    await t.shot();
  });

  testWidgets('tuto fiche', (tester) async {
    final t = Tuto('app-menu-digital-fiche-plat-et-options', tester);
    await ouvrir(tester);
    await tester.tap(find.byKey(const Key('see-menu')));
    await tester.pumpAndSettle();
    await t.shot(tap: find.text('Plats').first);
    await t.shot(tap: find.text('Burger du Bistrot'));
    await t.shot(tap: sem('À point'));
    await t.shot(tap: sem('Bacon'));
    await t.shot(tap: find.byKey(const Key('add-to-cart')));
    await t.shot();
  });

  testWidgets('tuto formule', (tester) async {
    final t = Tuto('app-menu-digital-composer-une-formule', tester);
    await ouvrir(tester);
    await tester.tap(find.byKey(const Key('see-menu')));
    await tester.pumpAndSettle();
    await t.shot(tap: find.text('Formules').first);
    await t.shot(tap: find.text('Menu du midi').last);
    await t.shot(tap: sem('Salade César'));
    await t.shot(tap: sem('Tarte au citron'));
    await t.shot(tap: find.byKey(const Key('add-formule')));
    await t.shot();
  });

  Future<void> remplirPanier(WidgetTester tester) async {
    await tester.tap(find.byKey(const Key('see-menu')));
    await tester.pumpAndSettle();
    await tester.tap(find.text('Plats').first);
    await tester.pumpAndSettle();
    await tester.tap(find.text('Burger du Bistrot'));
    await tester.pumpAndSettle();
    await tester.tap(sem('À point').first);
    await tester.enterText(find.byKey(const Key('dish-note')), 'sans oignons');
    await tester.pumpAndSettle();
    await tester.tap(find.byKey(const Key('add-to-cart')));
    await tester.pumpAndSettle();
    await tester.tap(find.text('Boissons').first);
    await tester.pumpAndSettle();
    await tester.tap(find.textContaining('Boissons fraîches').first);
    await tester.pumpAndSettle();
  }

  testWidgets('tuto panier', (tester) async {
    final t = Tuto('app-menu-digital-panier-et-envoi-en-cuisine', tester);
    await ouvrir(tester);
    await remplirPanier(tester);
    final plus = find.bySemanticsLabel('Ajouter au panier');
    await t.shot(tap: plus);
    await t.shot(tap: plus);
    await t.shot(tap: find.byKey(const Key('cart-button')));
    await tester.enterText(find.byKey(const Key('kitchen-note')), 'Servir ensemble');
    await t.shot(tap: find.byKey(const Key('send-order')));
    await t.shot();
  });

  testWidgets('tuto addition', (tester) async {
    final t = Tuto('app-menu-digital-addition-et-paiement', tester);
    await ouvrir(tester);
    await tester.tap(find.byKey(const Key('see-menu')));
    await tester.pumpAndSettle();
    await t.shot(tap: find.byKey(const Key('nav-addition')));
    await t.shot(tap: find.byKey(const Key('request-bill')));
    await t.shot();
  });

  testWidgets('tuto appel serveur', (tester) async {
    final t = Tuto('app-menu-digital-appeler-un-serveur', tester);
    await ouvrir(tester);
    await tester.tap(find.byKey(const Key('see-menu')));
    await tester.pumpAndSettle();
    await t.shot(tap: find.text('Appeler un serveur'));
    await t.shot(tap: find.byKey(const Key('call-water')));
    await t.shot(tap: find.byKey(const Key('call-send')));
    await t.shot();
  });

  testWidgets('tuto fidelite', (tester) async {
    final t = Tuto('app-menu-digital-fidelite-et-jeux', tester);
    await ouvrir(tester);
    await tester.tap(find.byKey(const Key('see-menu')));
    await tester.pumpAndSettle();
    await t.shot(tap: find.byKey(const Key('nav-fidelite')));
    await tester.enterText(find.byKey(const Key('loyalty-first')), 'Camille');
    await tester.enterText(find.byKey(const Key('loyalty-last')), 'Exemple');
    await tester.enterText(find.byKey(const Key('loyalty-phone')), '06 00 00 00 00');
    await tester.pump(const Duration(seconds: 6));
    await t.shot(tap: find.byKey(const Key('tab-check')));
    await tester.enterText(find.byKey(const Key('loyalty-lookup-phone')), '06 00 00 00 00');
    await t.shot(tap: find.byKey(const Key('loyalty-lookup')));
    await t.shot(tap: find.byKey(const Key('nav-jeux')));
    await t.shot();
  });

  testWidgets('tuto langues', (tester) async {
    final t = Tuto('app-menu-digital-langues-et-accessibilite', tester);
    await ouvrir(tester);
    await t.shot(tap: find.text('English'));
    await t.shot(tap: find.text('Français'));
    await t.shot(tap: find.byKey(const Key('a11y-button')).first);
    await t.shot(tap: find.byKey(const Key('a11y-lowVision')));
    await t.shot();
  });

  testWidgets('tuto rupture', (tester) async {
    final t = Tuto('app-menu-digital-plat-epuise-en-direct', tester);
    final (c, s, _) = await ouvrir(tester);
    await tester.tap(find.byKey(const Key('see-menu')));
    await tester.pumpAndSettle();
    await tester.tap(find.textContaining('Boissons fraîches').first);
    await tester.pumpAndSettle();
    await t.shot(tap: find.bySemanticsLabel('Ajouter au panier'));
    s.tools['list_dishes'] = (_) => {'count': 11, 'data': [...plats(epuises: {103, 104}), plat(106, 'Limonade artisanale', '3.90', 12)]};
    unawaited(c.read(menuControllerProvider.notifier).poll());
    await tester.pumpAndSettle();
    await t.shot(tap: find.byKey(const Key('soldout-replace')));
    await t.shot();
  });

  testWidgets('tuto personnel', (tester) async {
    final t = Tuto('app-menu-digital-mode-personnel', tester);
    final (c, _, store) = await ouvrir(tester, overrides: [staffAutoCloseProvider.overrideWithValue(const Duration(seconds: 60))]);
    await StaffPin(store).set('2468');
    await t.shot();
    final g = await tester.startGesture(tester.getCenter(find.byKey(const Key('logo-accueil'))));
    await tester.pump(const Duration(seconds: 5, milliseconds: 100));
    await g.up();
    await tester.pumpAndSettle();
    for (final d in ['2', '4', '6']) {
      await tester.tap(find.descendant(of: find.byType(Dialog), matching: find.text(d)));
      await tester.pump();
    }
    await t.shot(tap: find.descendant(of: find.byType(Dialog), matching: find.text('8')));
    await t.shot(tap: find.descendant(of: find.byType(Dialog), matching: find.text('OK')));
    await t.shot(tap: find.byKey(const Key('s01-table')));
    await t.shot();
    expect(c.read(staffModeProvider), isTrue);
    await tester.pump(const Duration(seconds: 61));
    await tester.pumpAndSettle();
  });
}
