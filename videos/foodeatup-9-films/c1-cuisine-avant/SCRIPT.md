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
| Voix off | ✅ générée — **42,24 s** (ElevenLabs, Adam - Instructor) |
| Écrans sources | ✅ les 12 téléchargés et sondés — voir `assets/screens.json` |
| Images d'ambiance | ⬜ 6 à générer (IMG-C1-a à f) |
| Composition | ⬜ bloquée, voir « décisions à prendre » |

## Écart de durée à arbitrer

Le storyboard vise **75 s**. La voix off fait **42,24 s**. L'écart vient des
pauses : le script en note une quinzaine (`[pause]`, `[pause courte]`) qu'un
moteur TTS ne tient pas de lui-même.

Trois issues :
1. **Assumer 42 s** — le film devient plus dense, ~52 s avec l'ouverture et le
   CTA. C'est cohérent avec les 9 vidéos des boucles (55-67 s).
2. **Regénérer avec des silences explicites** — insérer des balises de pause
   dans le texte pour atteindre ~60 s.
3. **Tenir 75 s** en étirant les plans muets (ouverture, étiquetage, clôture).

⚠️ Ce choix engage toute la série : le film « sans » jumeau devra faire la
**même durée à la frame près**.

## Ce que les rushes ont révélé

- **Format 1920×828** (2,32:1), pas du 16:9. Incrustés tels quels dans un cadre
  1920×1080, ils laissent des bandes.
- **Un bandeau de sous-titre bleu est déjà incrusté** en bas des tutoriels
  (« Livraison controlee et tracee »…). Soit on recadre pour l'exclure, soit on
  l'assume comme libellé d'action — mais on ne peut pas l'ignorer.
