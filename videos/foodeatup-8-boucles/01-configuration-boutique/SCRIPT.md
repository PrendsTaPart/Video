# Boucle 01 — Configuration boutique

Slug : `boucle-01-configuration-boutique` · Durée cible 85 s · Agents : Jarvis puis PrédiBot.

## Voix off (verbatim — ne pas réécrire)

Votre burger, vous le vendez quatorze euros. Vous savez qu'il vous coûte "environ
quatre euros". Sauf que le prix du bœuf a bougé trois fois cette année. Le pain a
augmenté en janvier. Et personne n'a rouvert la fiche depuis dix-huit mois.

Alors vous dites simplement : "Ajoute le poulet fermier à douze euros quatre-vingts
le kilo, chez Metro."

Et là, FoodEatUp ne stocke pas une ligne. Il fait circuler l'information.
L'ingrédient est créé. Le fournisseur est lié. Toutes les fiches techniques qui
contiennent du poulet se recalculent. Le food cost bouge. La marge par plat aussi.

Trois plats viennent de passer sous votre seuil. FoodEatUp vous le dit, et vous
propose l'ajustement. C'est vous qui validez.

Au même moment, votre stock, votre carte en ligne et votre comptabilité travaillent
déjà avec les bons chiffres.

Résultat : votre burger coûte quatre euros trente-huit. Marge : neuf euros soixante-
deux. Soit soixante-huit virgule sept pour cent. Et vous le saviez avant le service.

Si cette boucle est coupée, tout le reste tourne à vide.

## Squelette 7 plans

| # | Rôle |
|---|------|
| 1 | Le problème : burger à 14€, coût "environ 4€", fiche jamais rouverte depuis 18 mois. |
| 2 | La phrase dite à l'agent, en gros : « Ajoute le poulet fermier à 12,80€/kg, chez Metro. » |
| 3 | (le plus long) Cascade, dans cet ordre exact : Prix fournisseur → Ingrédient → Fiche technique → Food cost → Marge par plat → Carte et prix de vente → Achats et production → Stock et rentabilité. Preuve en bas de plan : « 21 outils MCP exécutent cette boucle ». |
| 4 | Bandeau orange « 3 plats sous votre seuil de marge » + carte de proposition avec DEUX boutons visibles, « Valider » et « Ignorer ». Le curseur va sur Valider. |
| 5 | Boucles voisines qui s'allument : StockVisionAI, HACCP, E-commerce, Comptabilité. |
| 6 | Chiffres à l'écran : coût matière 4,38 € · marge 9,62 € · 68,7 % · +0,41 € vs mois dernier. |
| 7 | « Une fiche fausse fausse le food cost, le stock, la marge et le prix. » (VO : « Si cette boucle est coupée, tout le reste tourne à vide. ») |

## Assets à générer / réutiliser

- **Nouveaux visuels RapidoCMS** (règle du 2026-08-07, `studio-video/assets/brand/dishes/`) :
  burger (plan 1, le problème) et poulet fermier cru/prêt à cuisiner (plan 2, l'ingrédient ajouté).
- `mascots/agent-laptop-homme.png` — sert de représentation générique pour Jarvis (plan 2).
- `product-screenshots/` : `ajouter-tva.png`, `ajouter-categorie.png`, `ajout-boutique.png`,
  `ajout-produit-boutique.png`, `ajouter-plat.png`, `ajouter-ingredient.png`,
  `configuration-recette.png` — à intégrer si un plan a besoin d'un écran produit réel.

## Statut
`script` (VO pas encore générée).
