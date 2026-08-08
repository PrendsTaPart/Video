# C1 · Cuisine — avant le service

Premier film de la série « Une journée avec FoodEatUp ». Film étalon : une fois
validé, les huit autres en découlent.

## Voix off (verbatim — générée)

Sept heures. La cuisine est vide. Dans quatre heures, tout doit être prêt.

Je pointe. Je récupère mes tâches. Je relève mes températures.

La livraison arrive. Je valide. Je scanne l'EAN et la DLC. Produit par produit.
La facture part au scan. Les prix se mettent à jour tout seuls.

Ce que je sors du stock, je le dis. À voix haute.

Mes fiches techniques du jour. Ma production. Ma liste d'ingrédients.
Je descends en plonge avec un papier, pas avec un doute.

Chaque préparation reçoit son étiquette. Chaque plat de vente, sa DLC et ses
allergènes.

Onze heures. Je valide ma production, je sonde mes plats. Ma matinée est tracée.
Je n'ai pas ouvert un seul classeur.

## État

| | |
|---|---|
| Voix off | ✅ **70,87 s** — texte enrichi pour tenir la cible des 75 s |
| Écrans sources | ✅ 12 extraits découpés, bandeau incrusté recadré |
| Images d'ambiance | ✅ 3 générées (cuisine vide, chef qui dicte, étiquette) |
| Composition | ✅ 8 scènes · `studio-video/compositions/c1-cuisine-avant.html` |
| Rendu | ✅ **75,4 s** · `out/c1-cuisine-avant.mp4` |

## Comment la durée a été atteinte

La première génération faisait 42 s : le script d'origine comptait sur quinze
pauses qu'un moteur TTS ne tient pas. Plutôt que d'étirer des plans muets, le
texte a été enrichi — précisions concrètes sur chaque geste, sans changer une
seule des phrases d'origine ni le ton. 1 150 caractères, 70,87 s de voix,
75,37 s avec le carton de clôture.

## Décisions de montage prises

- **Bandeau de sous-titre des rushes** : recadré (1920×828 → 1920×672). Il
  entrait en concurrence avec les coches orange de la grammaire de série.
- **Cadre tablette** : positionné en absolu, pas en `translate(-50%,-50%)`.
  GSAP réécrit tout le `transform` quand il anime `scale`, ce qui décentrait
  le cadre au rendu.
- **Liseré cuisine `#059669`** en haut de cadre, horloge en haut à gauche,
  coches orange accumulées à droite — conforme à la grammaire commune.
