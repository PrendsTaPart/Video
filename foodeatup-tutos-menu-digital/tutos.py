# Série « Application Menu digital » : 13 tutoriels, un geste par vidéo.
# Écrans : vraies images de l'app (captures/), rendues par outils/preparer.sh
# avec un restaurant FICTIF (« Bistrot de l'École », établissement 900).
# Les points touchés viennent de captures/manifeste.json (centre du bouton réellement touché).
import json, os
_M = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "captures", "manifeste.json")))
def _e(cle): return [[f] if x is None else [f, x, y] for f, x, y in _M["app-menu-digital-" + cle]]
P = "app-menu-digital-"
T = [
 {"cle": P+"installer-et-connecter", "vignette": 2, "titre": "Installer la tablette et la connecter", "chef": "app-menu-digital.webp",
  "hook": "Ta carte sur la tablette en 2 minutes",
  "etapes": ["Choisis l'onglet Clé API", "Colle l'identifiant et le secret FoodEatUp", "Touche Connecter la tablette", "Choisis ton établissement"],
  "voix": "[excited] Ta carte sur la tablette, en deux minutes ! Le code d'appairage arrive bientôt : aujourd'hui, j'utilise la clé API créée dans FoodEatUp. Je colle l'identifiant et le secret, je touche Connecter la tablette. [amazed] L'appli montre ce qu'elle a trouvé, puis je choisis mon établissement. Aucune carte à ressaisir, t'as vu ?"},
 {"cle": P+"table-et-code-personnel", "vignette": 6, "titre": "Choisir la table et le code du personnel", "chef": "mission-table-action.webp",
  "hook": "Une tablette, une table",
  "etapes": ["Touche la table où la tablette est posée", "Crée le code du personnel", "Tape-le une deuxième fois", "Termine l'installation"],
  "voix": "[excited] Une tablette, une table ! Je touche la table sept, là où la tablette est posée. Puis je crée le code du personnel, et je le tape une deuxième fois pour confirmer. [amazed] Ce code protège les réglages : les clients ne peuvent rien changer. Je termine, et l'accueil de la table sept s'affiche. Prêt pour le service !"},
 {"cle": P+"choisir-son-theme", "vignette": 2, "titre": "Choisir le thème de son menu", "chef": "app-menu-digital.webp",
  "hook": "Ton menu à tes couleurs",
  "etapes": ["Choisis un modèle de départ", "Ou la charte libre", "Ajuste couleurs, police et boutons", "Le contraste est vérifié tout seul"],
  "voix": "[excited] Ton menu, à tes couleurs ! Je choisis un modèle de départ, ici Brasserie, et l'aperçu change tout de suite. [amazed] Avec la charte libre, je règle mes couleurs, ma police et mes boutons. Si une couleur est trop claire, l'appli la corrige pour que tout reste lisible. Simple et propre, t'as vu ?"},
 {"cle": P+"parcourir-la-carte", "vignette": 1, "titre": "Parcourir la carte et chercher un plat", "chef": "app-menu-digital.webp",
  "hook": "Toute la carte d'un doigt",
  "etapes": ["Touche Voir la carte et commander", "Change de catégorie à gauche", "Filtre les sous-catégories en haut", "Cherche « sans gluten » dans la barre"],
  "voix": "[excited] Toute la carte, d'un doigt ! Le client touche Voir la carte. À gauche, les catégories ; en haut, les sous-catégories. Un plat épuisé est grisé, il ne peut pas être commandé. [amazed] Et dans la recherche, il tape : sans gluten. L'appli montre les plats sans gluten d'après les fiches ingrédients. Malin, non ?"},
 {"cle": P+"fiche-plat-et-options", "vignette": 3, "titre": "Ouvrir un plat et choisir ses options", "chef": "commande-en-ligne.webp",
  "hook": "Cuisson, suppléments, allergènes",
  "etapes": ["Touche le plat", "Lis les allergènes", "Choisis la cuisson et les suppléments", "Ajoute au panier : le prix suit"],
  "voix": "[excited] Cuisson, suppléments, allergènes : tout est sur la fiche ! Je touche le burger. Les allergènes viennent des fiches ingrédients. [amazed] Je choisis à point, j'ajoute du bacon, et le prix suit tout seul. Une précision pour la cuisine ? Elle s'écrit juste en dessous. J'ajoute au panier. Facile, t'as vu ?"},
 {"cle": P+"composer-une-formule", "vignette": 3, "titre": "Composer une formule", "chef": "commande-en-ligne.webp",
  "hook": "La formule se compose étape par étape",
  "etapes": ["Ouvre Formules", "Choisis la formule", "Un choix à chaque étape", "Ajoute la formule au panier"],
  "voix": "[excited] Une formule, étape par étape ! J'ouvre Formules, puis le menu du midi. Je choisis une salade César, puis une tarte au citron. [amazed] À droite, le compteur suit mes choix. J'ajoute la formule au panier : elle est transmise au serveur, qui la valide en caisse. Rien n'est oublié !"},
 {"cle": P+"panier-et-envoi-en-cuisine", "vignette": 3, "titre": "Valider le panier et envoyer en cuisine", "chef": "mission-caisse-action.webp",
  "hook": "La commande part en cuisine sans attendre",
  "etapes": ["Ajoute les plats au panier", "Ouvre le panier", "Une note pour la cuisine si besoin", "Envoie : le suivi s'affiche"],
  "voix": "[excited] La commande part en cuisine, sans attendre le serveur ! J'ajoute deux citronnades, j'ouvre le panier. Les prix viennent de FoodEatUp : la tablette n'envoie jamais un prix. [amazed] J'écris : servir ensemble, et j'envoie. Le suivi s'affiche : reçue, en préparation, prête, servie. Génial, non ?"},
 {"cle": P+"addition-et-paiement", "vignette": 1, "titre": "Voir l'addition et payer", "chef": "qr-table.webp",
  "hook": "L'addition, sans lever la main",
  "etapes": ["Touche Addition", "Le reste à payer vient de la caisse", "Paye avec son téléphone par le QR code", "Ou demande l'addition au serveur"],
  "voix": "[excited] L'addition, sans lever la main ! Le client touche Addition : les lignes et le reste à payer viennent de la caisse. [amazed] Il peut payer avec son téléphone, en scannant le QR code. Ou il demande l'addition au serveur, qui est prévenu tout de suite. Fini l'attente, t'as vu ?"},
 {"cle": P+"appeler-un-serveur", "vignette": 2, "titre": "Appeler un serveur", "chef": "mission-table-reussi.webp",
  "hook": "Un serveur prévenu en 1 toucher",
  "etapes": ["Touche Appeler un serveur", "Choisis le motif", "Touche Prévenir un serveur", "Le serveur reçoit l'appel avec la table"],
  "voix": "[excited] Un serveur prévenu, en un toucher ! Le client touche Appeler un serveur, et choisit le motif : de l'eau. [amazed] Il touche Prévenir : l'équipe reçoit l'alerte avec le numéro de table. Et s'il appuie deux fois, l'appli évite le doublon. Le service reste fluide !"},
 {"cle": P+"fidelite-et-jeux", "vignette": 1, "titre": "Fidélité et jeux depuis la table", "chef": "mission-fidelite-action.webp",
  "hook": "Le client rejoint ta fidélité à table",
  "etapes": ["Touche Fidélité", "Prénom, nom et téléphone pour s'inscrire", "Ou voir ses points avec son téléphone", "Touche Jeux : le QR ouvre la roue"],
  "voix": "[excited] Ton client rejoint ta fidélité, directement à table ! Il touche Fidélité, et s'inscrit avec son prénom, son nom et son téléphone. [amazed] Déjà membre ? Il tape son téléphone et voit ses points et sa prochaine récompense. Et dans Jeux, un QR code ouvre la roue. Fidèle et ludique !"},
 {"cle": P+"langues-et-accessibilite", "vignette": 4, "titre": "Langues et accessibilité", "chef": "app-menu-digital.webp",
  "hook": "Ton menu dans 4 langues",
  "etapes": ["Touche une langue sur l'accueil", "Français, anglais, espagnol ou chinois", "Touche le bouton Accessibilité", "Basse vision : texte agrandi"],
  "voix": "[excited] Ton menu, dans quatre langues ! Sur l'accueil, le client touche English : tout l'écran passe en anglais. Français, espagnol ou chinois, au choix. [amazed] Et avec le bouton Accessibilité, il choisit basse vision : le texte grandit, le contraste aussi. Personne n'est laissé de côté !"},
 {"cle": P+"plat-epuise-en-direct", "vignette": 1, "titre": "Un plat épuisé pendant la commande", "chef": "mission-caisse-reussi.webp",
  "hook": "Épuisé ? Remplacé au même prix",
  "etapes": ["Un plat est dans le panier", "La cuisine le passe en épuisé", "La tablette prévient le client", "Remplacer : même prix, même catégorie"],
  "voix": "[excited] Un plat s'épuise pendant que le client commande ? Pas de panique ! La tablette le voit tout de suite et prévient le client. [amazed] Elle propose un remplaçant de la même catégorie, au même prix. Il touche Remplacer, et le panier est à jour. Zéro déception, t'as vu ?"},
 {"cle": P+"mode-personnel", "vignette": 3, "titre": "Ouvrir le mode personnel", "chef": "mission-table-action.webp",
  "hook": "Les réglages, réservés à l'équipe",
  "etapes": ["Appui long de 5 secondes sur le logo", "Tape le code du personnel", "Change de table ou recharge la carte", "Le mode se ferme tout seul"],
  "voix": "[excited] Les réglages, réservés à l'équipe ! J'appuie cinq secondes sur le nom du restaurant, et je tape le code du personnel. [amazed] Le mode personnel s'ouvre : changer de table, recharger la carte, le thème, l'accessibilité. Après une minute sans geste, il se referme tout seul. Sécurisé, t'as vu ?"},
]
for v in T:
    v["ecrans"] = _e(v["cle"][len(P):])
    v["ecran_vignette"] = v["ecrans"][v.pop("vignette")][0]
