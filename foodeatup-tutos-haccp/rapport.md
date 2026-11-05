# Rapport — tutoriels de l'application HACCP (05/11/2026)

- **16 vidéos** réalisées, contrôlées puis publiées. Détail ligne par ligne dans `statut.csv`.
- **Écrans** : vrais écrans de l'application (dépôt `foodeatup-haccp`, version 1.7.4).
  - Rendus par son propre harnais de test, dans une copie jetable : le code de l'application n'a pas été modifié.
  - Restaurant fictif « Bistrot de l'École » (n°900). Toutes les données affichées sont des données de démonstration.
  - Les vidéos portent la mention « Démonstration · restaurant fictif ».
- **Voix** : Adam, modèle eleven_v4, une prise par vidéo. Durée de 14 à 17 s.
- **Montage** : HyperFrames 0.9.5, avec le moteur commun `outils-tutos/` (montage, rendu, vignette, fiches Académie).
- **Hébergement** : bibliothèque RapidoCMS, préfixe `foodeatup-haccp-<sujet>-tuto|-vignette`. Les 32 fichiers ont été vérifiés.
- **Académie** : PR #8 fusionnée dans `foodeatup-guide-star-227b4772`.
  - Les fiches sont dans le module `haccp`, section « Application tablette HACCP », ordre 100 à 115.
  - Chaque fiche renvoie, par sa FAQ, à la fiche équivalente du logiciel sur ordinateur.
- **YouTube** : rien n'a été publié, ce n'était pas demandé.

## Non filmé ou signalé

- La première image de l'écran de connexion n'est pas utilisée : dans le harnais de test, le logo y apparaît comme une tache blanche. Les autres écrans de connexion sont utilisés.
- Les relevés montrés sont des relevés de démonstration ; aucun n'est présenté comme un vrai relevé.
- L'ancienne série de 8 vidéos est conservée dans `ancienne-serie/`, mais n'est plus publiée par cette série.
