#!/usr/bin/env python3
"""Écrit src/data/fiches-app-menu-digital.ts dans le dépôt de l'Académie : python3 academie.py <dépôt>."""
import os, sys
ICI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(ICI, "..", "outils-tutos"))
from fiches_academie import fiches, titres_academie
from tutos import T
D = sys.argv[1]
X = {
 "installer-et-connecter": ("Relier une tablette de table à son compte FoodEatUp avec une clé API, puis choisir l'établissement : la carte, les prix et les formules arrivent tout seuls.", "La clé API se crée dans FoodEatUp, Mon profil, API Clients. Le code d'appairage à 6 caractères arrivera bientôt.", "bornes-tablettes"),
 "table-et-code-personnel": ("Indiquer sur quelle table la tablette est posée et créer le code du personnel qui protège les réglages.", "Choisissez un code que les clients ne devinent pas, et ne le notez pas sur la tablette.", "menu-digital-qr-table"),
 "choisir-son-theme": ("Habiller le menu digital aux couleurs du restaurant : modèle de départ ou charte libre, police et forme des boutons.", "Si une couleur rend le texte peu lisible, l'appli la corrige toute seule et vous le dit.", None),
 "parcourir-la-carte": ("Montrer comment le client parcourt la carte sur la tablette : catégories, sous-catégories, plats épuisés et recherche.", "La recherche « sans gluten » s'appuie sur les fiches ingrédients : plus elles sont complètes, mieux elle répond.", "menu-digital-qr-table"),
 "fiche-plat-et-options": ("Ouvrir un plat, lire ses allergènes, choisir la cuisson et les suppléments, et ajouter une précision pour la cuisine.", "Les cuissons et suppléments viennent de FoodEatUp : réglez-les une fois, ils servent à la caisse, au QR et à la tablette.", "configurer-supplements-et-cuissons"),
 "composer-une-formule": ("Composer une formule étape par étape depuis la tablette ; elle est transmise au serveur, qui la valide en caisse.", "Une formule se choisit sur la tablette mais se valide toujours en caisse par le serveur.", None),
 "panier-et-envoi-en-cuisine": ("Relire le panier, ajouter une note pour la cuisine et envoyer la commande, puis suivre sa préparation.", "La tablette n'envoie jamais un prix : les montants viennent toujours de FoodEatUp.", "commander-qr-code"),
 "addition-et-paiement": ("Afficher l'addition de la table, payer avec son téléphone par le QR code, ou demander l'addition au serveur.", "Le reste à payer vient de la caisse : la tablette ne calcule rien.", "separer-une-addition"),
 "appeler-un-serveur": ("Prévenir un serveur depuis la table en choisissant le motif de l'appel.", "Un même appel n'est pas renvoyé deux fois dans la minute : l'équipe n'est pas noyée sous les alertes.", None),
 "fidelite-et-jeux": ("Rejoindre le programme de fidélité depuis la table, consulter ses points et ouvrir le jeu concours par QR code.", "Aucun point n'est crédité par la tablette : les points arrivent avec le paiement de la commande.", "booster-la-fidelite-programme"),
 "langues-et-accessibilite": ("Changer la langue du menu (français, anglais, espagnol, chinois) et activer une aide d'accessibilité.", "Après une période sans geste, la tablette revient à l'accueil et repasse en français pour le client suivant.", None),
 "plat-epuise-en-direct": ("Voir comment la tablette prévient le client quand un plat de son panier s'épuise, et propose un remplaçant au même prix.", "Un plat marqué épuisé en cuisine disparaît des tablettes en direct.", "portions-rupture-automatique"),
 "mode-personnel": ("Ouvrir le mode personnel avec un appui long et le code du personnel pour changer de table, recharger la carte ou régler la tablette.", "Le mode personnel se referme seul après une minute sans geste.", "bornes-tablettes"),
}
cfg = {"export": "fichesAppMenuDigital", "prefixe_rapido": "foodeatup-menu-digital-", "prefixe_cle": "app-menu-digital-", "module": "ecrans-bornes",
       "section": "Application Menu digital", "ordre": 100, "app": "l'application FoodEatUp Menu digital", "nom": "FoodEatUp Menu digital", "dossier": ICI,
       "origine": "Écrans réels de l'application (dépôt PrendsTaPart/foodeatup-menu-digital), rendus par son harnais de test avec un restaurant fictif (Bistrot de l'École, n°900)."}
titres = titres_academie(D)
for s, (_, _, l) in X.items():
    assert l is None or l in titres, l
open(os.path.join(D, "src/data/fiches-app-menu-digital.ts"), "w").write(fiches(T, cfg, X, titres))
print("ok")
