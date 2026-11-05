#!/usr/bin/env python3
"""Écrit src/data/fiches-app-haccp.ts dans le dépôt de l'Académie : python3 academie.py <dépôt>."""
import os, re, sys
ICI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(ICI, "..", "outils-tutos"))
from fiches_academie import fiches
from tutos import T
D = sys.argv[1]
src = open(os.path.join(D, "src/data/tutorials.ts")).read()
titres = {}
for b in re.split(r"\n  \{", src):
    s, t = re.search(r'slug: "([^"]+)"', b), re.search(r'title: "([^"]+)"', b)
    if s and t: titres[s.group(1)] = t.group(1)
X = {
 "installer-et-se-connecter": ("Installer l'application HACCP sur une tablette ou un téléphone et la relier à son établissement FoodEatUp, chaque employé signant ses relevés à son nom.", "Chaque employé touche son nom avant de commencer : ainsi chaque relevé porte la bonne signature.", "ouvrir-son-classeur-haccp"),
 "relever-une-temperature": ("Saisir un relevé de température d'équipement en quelques secondes, avec le verdict conforme ou hors seuil et l'action corrective quand il le faut.", "Les seuils viennent des équipements déclarés dans FoodEatUp : déclarez-les bien une fois, l'appli s'en sert ensuite.", "relever-une-temperature-equipement"),
 "jarvis-a-la-voix": ("Faire un relevé de température à la voix, mains prises, avec Jarvis qui relit avant d'enregistrer.", "Rien n'est enregistré sans votre « oui » : Jarvis relit toujours la valeur avant.", "relever-une-temperature-equipement"),
 "etiquette-dlc": ("Préparer et imprimer une étiquette DLC avec les allergènes, la DLC étant calculée automatiquement.", "Scannez le code-barres quand il existe : le produit et ses informations se remplissent tout seuls.", "imprimer-ses-etiquettes"),
 "produits-ouverts": ("Suivre les produits entamés classés par DLC pour ne rien oublier au frigo.", "Regardez cette liste en début de service : ce qui expire aujourd'hui ressort en premier.", "retrouver-historique-etiquettes"),
 "controle-reception": ("Contrôler une livraison à la porte : températures, conformité, motif de refus et photo du bon.", "Notez la température des produits frais avant de les ranger : c'est ce que le contrôleur regarde en premier.", "controler-reception-livraisons"),
 "tracabilite": ("Créer une fiche de traçabilité (produit, lot, DLC, quantité) puis la compléter quand le produit est fini.", "Gardez les étiquettes des lots : le numéro de lot saisi doit pouvoir être retrouvé sur l'emballage.", "creer-une-tracabilite-simplifiee"),
 "plan-de-nettoyage": ("Pointer les postes nettoyés du plan de nettoyage avec photo de preuve, et voir ce qui est fait, à faire ou en retard.", "Une photo de preuve par zone suffit : elle est gardée avec le pointage.", "pointer-ses-actions-de-nettoyage"),
 "controle-hygiene": ("Faire un contrôle d'hygiène à partir d'un modèle, avec Oui, Non ou Non évalué, un commentaire et une signature.", "Commencez par les modèles conseillés : ils couvrent déjà les points habituels d'un contrôle.", "faire-son-controle-de-conformite"),
 "huiles-de-friture": ("Suivre l'huile de chaque friteuse : tests de composés polaires, filtrations et remplacements.", "Un test au-dessus du seuil demande un changement d'huile : il reste visible tant qu'il n'est pas fait.", "declarer-ses-equipements"),
 "refroidissement": ("Suivre un cycle de refroidissement ou de remise en température avec les relevés à cœur.", "Lancez le cycle dès la sortie de cuisson : l'appli vous dit si le rythme permet d'atteindre la cible à temps.", "ajouter-temperature-plat"),
 "production-du-jour": ("Valider la production du jour avec la quantité produite et la température à cœur.", "Chaud : 63 °C ou plus. Froid : 3 °C ou moins. Entre les deux, l'appli propose un refroidissement.", "consulter-ses-productions-en-cours"),
 "historique-et-export": ("Retrouver tous ses relevés HACCP par période et les exporter en PDF ou en tableur.", "Exportez le PDF du mois en fin de mois : c'est le document à présenter lors d'un contrôle.", "exporter-les-historiques-haccp"),
 "alertes-et-automatisations": ("Régler les alertes de l'application et demander une automatisation à FoodEatUp.", "N'activez que les alertes utiles à votre équipe : trop d'alertes finissent par ne plus être lues.", "declarer-ses-equipements"),
 "mode-ecole": ("Former son équipe avec le mode école : fiches, missions et quiz, sans rien envoyer dans le vrai registre.", "Faites faire une mission à chaque nouvel employé avant son premier service.", "ouvrir-son-classeur-haccp"),
 "langue-et-theme": ("Choisir la langue de l'application pour chaque employé et le thème d'affichage.", "Les relevés restent enregistrés en français dans FoodEatUp, quelle que soit la langue de l'employé.", "ouvrir-son-classeur-haccp"),
}
cfg = {"export": "fichesAppHaccp", "prefixe_rapido": "foodeatup-haccp-", "prefixe_cle": "app-haccp-", "module": "haccp",
       "section": "Application tablette HACCP", "ordre": 100, "app": "l'application FoodEatUp HACCP", "nom": "FoodEatUp HACCP", "dossier": ICI,
       "origine": "Écrans réels de l'application (dépôt PrendsTaPart/foodeatup-haccp), rendus par son harnais de test avec un restaurant fictif (Bistrot de l'École, n°900)."}
open(os.path.join(D, "src/data/fiches-app-haccp.ts"), "w").write(fiches(T, cfg, X, titres))
print("ok")
