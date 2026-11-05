#!/usr/bin/env python3
"""Écrit src/data/fiches-app-recettes.ts dans le dépôt de l'Académie : python3 academie.py <dépôt>."""
import os, sys
ICI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(ICI, "..", "outils-tutos"))
from fiches_academie import fiches, titres_academie
from tutos import T
D = sys.argv[1]
X = {
 "qui-es-tu": ("Se connecter à l'application Recettes avec son prénom et son code personnel, le même qu'à la pointeuse et à la caisse.", "Chacun se connecte à son nom : la formation et les recettes réussies sont suivies pour chaque employé.", "creer-son-code-pin"),
 "trouver-une-recette": ("Trouver une recette par son univers et lire sa fiche : temps, allergènes, ingrédients et quantités.", "« Explique-moi » lit la fiche à voix haute : pratique quand on a les mains prises.", "monter-ses-recettes"),
 "suivre-les-etapes": ("Préparer une recette pas à pas, avec les quantités recalculées selon le nombre de fournées.", "Quantités et gestes viennent de la fiche, jamais de mémoire : c'est ce qui garde le goût constant.", "monter-ses-recettes"),
 "allergenes-et-recherche": ("Répondre à une question d'allergène en une touche, chercher une recette par son nom et choisir la langue de l'application.", "En cas de doute sur un allergène, on ne devine jamais : on montre la fiche au client ou on demande au responsable.", "saisir-ses-ingredients"),
 "etiquette-dlc": ("Imprimer l'étiquette d'une préparation terminée, avec ses dates, ses allergènes et son auteur déjà remplis.", "Étiquette chaque préparation avant de la ranger : l'étiquette part aussi dans l'application HACCP.", "imprimer-ses-etiquettes"),
 "parcours-et-quiz": ("Suivre le parcours de formation sur cinq jours et vérifier ses acquis avec un quiz par recette.", "Un quiz réussi ne suffit pas : le responsable valide ensuite la recette en voyant le geste.", "former-un-employe-mode-ecole"),
 "mode-ecole": ("Découvrir l'application en mode école : le chef montre chaque bouton, sans rien enregistrer pour de vrai.", "Fais faire la visite guidée à chaque nouvel employé avant son premier service.", "mode-ecole-restaurant-fictif"),
 "espace-responsable": ("Ouvrir l'espace responsable avec son code pour piloter le food cost, l'équipe, les médias et les exports.", "Quitte le mode responsable en partant : la tablette repasse en mode employé.", "creer-ses-roles-et-permissions"),
 "couts-et-marges": ("Voir le coût matière, le prix de vente et la marge de chaque recette, et le détail par ingrédient.", "Saisis la main-d'œuvre et les frais généraux pour obtenir un coût complet, pas seulement le coût matière.", "saisir-ses-ingredients"),
 "fiches-pdf": ("Exporter ses fiches techniques en PDF : contenu, recettes et modèle adapté à son métier.", "Les coûts et marges ne sortent pas de la tablette : ils sont dans le PDF de FoodEatUp, avec connexion.", "monter-ses-recettes"),
}
cfg = {"export": "fichesAppRecettes", "prefixe_rapido": "foodeatup-recettes-", "prefixe_cle": "app-recettes-", "module": "stockvision-ai",
       "section": "Application Recettes", "ordre": 100, "app": "l'application FoodEatUp Recettes", "nom": "FoodEatUp Recettes", "dossier": ICI,
       "origine": "Écrans réels de l'application (dépôt PrendsTaPart/foodeatup-recettes), rendus par son harnais de test sur un jeu de démonstration fictif (Bistrot de l'École, n°900)."}
titres = titres_academie(D)
for s, (_, _, l) in X.items():
    assert l is None or l in titres, l
open(os.path.join(D, "src/data/fiches-app-recettes.ts"), "w").write(fiches(T, cfg, X, titres))
print("ok")
