# Série « Application Recettes » : 10 tutoriels, un geste par vidéo.
# Écrans : vraies images de l'app, rendues par outils/preparer.sh dans une copie jetable,
# sur un jeu de démonstration FICTIF (« Bistrot de l'École », outils/bistrot_demo.py).
import json, os
_M = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "captures", "manifeste.json")))
P = "app-recettes-"
def _e(cle): return [[f] if x is None else [f, x, y] for f, x, y in _M[P + cle]]
T = [
 {"cle": P+"qui-es-tu", "vignette": 1, "titre": "Se connecter avec son prénom et son code", "chef": "mission-recette-action.webp",
  "hook": "Ta tablette de recettes en 2 touches",
  "etapes": ["Touche ton prénom", "Tape ton code personnel", "Le même code qu'à la pointeuse", "L'accueil montre tes univers"],
  "voix": "[excited] Tes recettes, en deux touches ! Je touche mon prénom, Camille, et je tape mon code personnel : le même qu'à la pointeuse et à la caisse. [amazed] L'accueil s'ouvre, avec tous les univers de la carte : préparations, cafés, boissons, plats, desserts. Prêt à cuisiner, t'as vu ?"},
 {"cle": P+"trouver-une-recette", "vignette": 2, "titre": "Trouver une recette et lire sa fiche", "chef": "mission-recette-action.webp",
  "hook": "La bonne fiche en 2 touches",
  "etapes": ["Touche l'univers", "Touche la recette", "Temps, allergènes, ingrédients", "Commencer ou Explique-moi"],
  "voix": "[excited] La bonne fiche, en deux touches ! Je touche Plats du midi, puis le croque-monsieur. [amazed] Tout est là : le temps, les allergènes en orange, les ingrédients avec leurs quantités. Je touche Commencer pour la préparer, ou Explique-moi pour l'écouter. Simple, non ?"},
 {"cle": P+"suivre-les-etapes", "vignette": 1, "titre": "Préparer une recette pas à pas", "chef": "mission-recette-reussi.webp",
  "hook": "Une étape à la fois, sans se tromper",
  "etapes": ["Choisis le nombre de fournées", "Les quantités se recalculent", "Une étape à la fois, lue à voix haute", "À la fin : étiquette et quiz"],
  "voix": "[excited] Une étape à la fois, sans se tromper ! Je choisis le nombre de fournées, et les quantités se recalculent. [amazed] Ensuite, une seule étape à l'écran : la voix peut la lire, et je touche Suivant. À la fin, bravo ! L'appli me rappelle d'étiqueter, et me propose le quiz. Génial, t'as vu ?"},
 {"cle": P+"allergenes-et-recherche", "vignette": 0, "titre": "Allergènes, recherche et langue", "chef": "mission-recette-action.webp",
  "hook": "« Il y a du lait ? » Réponse en 1 touche",
  "etapes": ["Ouvre Allergènes", "Touche l'allergène du client", "Ou cherche une recette par son nom", "Change la langue de l'appli"],
  "voix": "[excited] Il y a du lait ? Réponse en une touche ! Dans Allergènes, je touche celui du client : les recettes qui en contiennent sont grisées. [amazed] Je peux aussi chercher une recette par son nom, et changer la langue de l'appli : français, anglais ou vietnamien. Les fiches, elles, restent comme dans FoodEatUp."},
 {"cle": P+"etiquette-dlc", "vignette": 1, "titre": "Imprimer l'étiquette d'une préparation", "chef": "mission-etiquette-action.webp",
  "hook": "L'étiquette DLC part toute seule",
  "etapes": ["Ouvre la recette terminée", "Touche Imprimer l'étiquette", "Dates, allergènes et auteur déjà remplis", "L'étiquette arrive aussi dans l'appli HACCP"],
  "voix": "[excited] L'étiquette DLC, sans rien recopier ! La tarte au citron est prête : j'imprime son étiquette. [amazed] La date de fabrication, la DLC, les allergènes et mon prénom sont déjà remplis. Et l'étiquette part aussi dans l'application HACCP. Zéro ressaisie, t'as vu ?"},
 {"cle": P+"parcours-et-quiz", "vignette": 0, "titre": "Suivre sa formation et faire un quiz", "chef": "mission-recette-reussi.webp",
  "hook": "Formé en 5 jours, recette par recette",
  "etapes": ["Ouvre Ma formation", "Un parcours sur 5 jours", "Chaque recette : découverte puis entraînement", "Un quiz vérifie ce que tu sais"],
  "voix": "[excited] Formé en cinq jours, recette par recette ! Dans Ma formation, chaque jour a son thème : cafés, préparations, boissons, plats, desserts. [amazed] Après une recette, un quiz vérifie ce que tu as retenu : ici, dans quoi sert-on le cappuccino ? Tu progresses, et ça se voit !"},
 {"cle": P+"mode-ecole", "vignette": 0, "titre": "Découvrir l'appli avec le mode école", "chef": "mission-recette-action.webp",
  "hook": "Apprendre sans rien abîmer",
  "etapes": ["Ouvre le mode école", "Le chef montre chaque bouton", "Rien n'est enregistré pour de vrai", "Le badge se fait valider par le responsable"],
  "voix": "[excited] Apprendre, sans rien abîmer ! En mode école, aucune étiquette et aucune production ne sont enregistrées. [amazed] Le chef montre chaque bouton, puis propose des missions. À la fin, le badge se fait valider par ton responsable. Parfait pour un premier jour !"},
 {"cle": P+"espace-responsable", "vignette": 1, "titre": "Ouvrir l'espace responsable", "chef": "mission-recette-reussi.webp",
  "hook": "Le pilotage, réservé au responsable",
  "etapes": ["Touche Responsable", "Tape le code responsable", "Food cost, équipe, export PDF", "Suis la formation de chacun"],
  "voix": "[excited] Le pilotage, réservé au responsable ! Je touche Responsable et je tape mon code. [amazed] L'espace s'ouvre : food cost, équipe, recettes et médias, export PDF, alertes prix. Dans Équipe, je vois où en est chacun, et je valide ses recettes. Tout est sous contrôle !"},
 {"cle": P+"couts-et-marges", "vignette": 1, "titre": "Voir le coût et la marge de ses recettes", "chef": "mission-recette-reussi.webp",
  "hook": "Ta marge, recette par recette",
  "etapes": ["Ouvre Food cost", "Coût, prix et marge de chaque recette", "Touche une recette : le détail par ingrédient", "Main-d'œuvre et frais à saisir"],
  "voix": "[excited] Ta marge, recette par recette ! Dans Food cost, chaque recette affiche son coût, son prix de vente et sa marge. [amazed] Je touche le croque-monsieur : le détail par ingrédient s'affiche. La main-d'œuvre et les frais généraux se saisissent pour un coût complet. Fini les marges au hasard !"},
 {"cle": P+"fiches-pdf", "vignette": 0, "titre": "Exporter ses fiches en PDF", "chef": "mission-recette-action.webp",
  "hook": "Tes fiches techniques en PDF",
  "etapes": ["Ouvre Export PDF", "Choisis le contenu et les recettes", "Choisis un modèle selon ton métier", "Exporte le PDF"],
  "voix": "[excited] Tes fiches techniques, en PDF ! Dans Export PDF, je choisis le contenu : fiche technique, pas à pas, allergènes ou classeur complet. [amazed] Je coche mes recettes, je choisis un modèle selon mon métier, parmi vingt, et j'exporte. Prêt à imprimer, t'as vu ?"},
]
for v in T:
    v["ecrans"] = _e(v["cle"][len(P):])
    v["ecran_vignette"] = v["ecrans"][v.pop("vignette")][0]
