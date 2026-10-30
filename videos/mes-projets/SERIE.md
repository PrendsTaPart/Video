# Série « Mes projets » — un épisode par projet

Format : vertical 1080×1920, ~30 s, voix Noé (eleven_v4), charte FoodEatUp (bleu nuit #0F1A23, bleu #007BFF, orange #FFA500, crème #FCF9E6, police Goodly/Manrope/Poppins) avec l'accent propre au projet.
Structure : hook (ligne 0) → « Voici …, un de mes projets » → 5 à 6 temps forts sur la vraie vidéo / les vrais écrans du projet → CTA « Voir le projet » (lien sous la vidéo).
Moteur : `_engine/serie.js` (au-dessus de `_journal-63-72/engine/journal.js`) + `_engine/incruste.js` (incrustation des vidéos du projet) + `finir.sh`.
Rendu : `node _moteur/render.js <dossier> 30 && node mes-projets/_engine/incruste.js <dossier> && bash _journal-63-72/engine/finir.sh <dossier> <N>`

| Ép. | Projet | Dossier | Statut |
|---|---|---|---|
| 1 | FoodEatUp Caisse Mobile — caisse.foodeatup.fr | mes-projets-ep01-caisse | monté |
| 2 | FoodEatUp Menu digital — tablette.foodeatup.fr | mes-projets-ep02-menu-digital | monté |
| 3 | FoodEatUp HACCP — haccp.foodeatup.fr | mes-projets-ep03-haccp | monté |
| 4 | FoodEatUp Recettes — recette.foodeatup.fr | — | script prêt, voix à générer |
| 5 | FoodEatUp KDS — kds.foodeatup.fr | — | script prêt, voix à générer |
| 6 | FoodEatUp Fidélité — fidelite.foodeatup.fr | — | script prêt, voix à générer |
| 7 | FoodEatUp Laboratoire — lab.foodeatup.fr | — | script prêt, voix à générer |
| 8 | QA Hub — qa.foodeatup.fr | — | script prêt, voix à générer |

Note : « Tablette » et « Menus digital » pointent vers le même projet Lovable (4092c94f…) et le même site (tablette.foodeatup.fr) : un seul épisode (ép. 2).

## Scripts des épisodes 4 à 8

### Ép. 4 — Recettes
La recette existe. Elle n'est juste jamais suivie.
Voici FoodEatUp Recettes, un de mes projets.
Sur la tablette, une étape à la fois, en photo et à voix haute.
Un minuteur se lance tout seul quand il faut attendre.
Les allergènes s'affichent avant de commencer.
Un nouveau apprend en jouant, et le responsable valide.
Et les coûts arrivent tout seuls de FoodEatUp.
Le lien est sous la vidéo : clique sur « Voir le projet ».

### Ép. 5 — KDS (écran de cuisine)
En plein coup de feu, ta cuisine voit tout, en même temps ?
Voici l'écran de cuisine FoodEatUp, un de mes projets.
Chaque poste reçoit ses tickets, avec un minuteur qui change de couleur.
Le pass envoie la table entière en même temps.
Le bon sort sur l'imprimante du poste.
Chaque poste a son propre son, et un mode école pour les nouveaux.
Il marche sur un écran, une tablette ou un téléphone.
Le lien est sous la vidéo : clique sur « Voir le projet ».

### Ép. 6 — Fidélité
Et si tes clients revenaient en dix secondes chrono ?
Voici FoodEatUp Fidélité, un de mes projets.
Au comptoir, une tablette : le client tape juste son numéro.
Il cumule des points à chaque passage.
Il tourne la roue des cadeaux, et il a envie de revenir.
Tout est à tes couleurs, et respecte les règles.
L'appli est gratuite.
Le lien est sous la vidéo : clique sur « Voir le projet ».

### Ép. 7 — Laboratoire
Quatre heures cinquante-huit du matin. Ton labo est déjà prêt.
Voici FoodEatUp Laboratoire, un de mes projets.
Les commandes des boutiques arrivent toutes au même endroit.
La production se planifie, les étiquettes sortent toutes seules.
Le contrôle qualité se fait sur l'écran, le dossier est prêt en un clic.
Les livraisons partent, et le siège suit tout le réseau.
Ton labo, sur un seul écran.
Le lien est sous la vidéo : clique sur « Voir le projet ».

### Ép. 8 — QA Hub
Mes développeurs ne cherchent plus les bugs. Claude les trouve.
Voici QA Hub, un de mes projets.
Claude teste chaque outil de mes logiciels, un par un.
Quand quelque chose casse, il écrit un ticket complet.
Mon développeur reçoit la correction déjà expliquée.
Toute l'équipe voit la même liste, au même endroit.
C'est gratuit.
Le lien est sous la vidéo : clique sur « Voir le projet ».
