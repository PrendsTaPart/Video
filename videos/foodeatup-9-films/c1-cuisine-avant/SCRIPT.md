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
| Écrans sources | ✅ 12 extraits, remontés en **6 bobines** à la durée exacte des scènes (`build-screens.sh`) |
| Plans d'ambiance | ✅ 2 plans tournés (bibliothèque Higgsfield) — cuisine déserte, portrait du chef |
| Bande son | ✅ musique + 4 bruitages ElevenLabs, 28 événements calés (`assets/audio/c1/`) |
| Composition | ✅ 8 scènes générées par `build-compositions.py` |
| Rendu | ✅ **75,4 s** · `out/c1-cuisine-avant.mp4` |

## Chaîne de fabrication

```bash
./build-screens.sh        # rushes -> 6 bobines d'écran, une par scène
python3 build-compositions.py   # gabarit -> les 8 scènes HTML
cd ../../../studio-video && npx hyperframes lint
npx hyperframes render -c compositions/c1-cuisine-avant.html \
  -o ../videos/foodeatup-9-films/c1-cuisine-avant/out/c1-cuisine-avant.mp4 \
  --video-frame-format png
```

`--video-frame-format png` n'est pas optionnel sur ce film : les sources sont
des captures d'interface, et l'extraction JPEG y laisse des artefacts sur les
aplats et le texte fin.

## Décisions de montage prises

- **Bandeau de sous-titre des rushes** : recadré (1920×828 → 1920×672). Il
  entrait en concurrence avec les coches orange de la grammaire de série.
- **Cadre tablette** : positionné en absolu, pas en `translate(-50%,-50%)`.
  GSAP réécrit tout le `transform` quand il anime `scale`, ce qui décentrait
  le cadre au rendu. Même piège pour le `skewX` du balayage de veille.
- **Fond** : passé du gris froid `#F7F9FC` au crème `#FCF9E6` de la charte du
  site, avec les deux dégradés `hero-glow` et une trame de points, tous
  animés. La vidéo et la page qui l'héberge sont désormais le même univers.
- **Cadre agrandi** de 1360 à 1560 px, mots-clés agrandis (coches 20 → 30 px,
  surtitre 28 → 40 px, horloge 34 → 46 px) : à 1360 px les libellés de
  l'interface étaient illisibles sur mobile.
- **Cartons d'ouverture et de clôture** : images fixes remplacées par des
  plans tournés, avec le personnage `chef-hero` commun à toute la série.
- **Liseré cuisine `#059669`** en haut de cadre, horloge en haut à gauche.
  Les coches orange, elles, sont passées d'une colonne à droite à une rangée
  sous l'écran : la colonne mordait sur le cadre une fois celui-ci élargi.

## Comment la durée a été atteinte

La première génération faisait 42 s : le script d'origine comptait sur quinze
pauses qu'un moteur TTS ne tient pas. Plutôt que d'étirer des plans muets, le
texte a été enrichi — précisions concrètes sur chaque geste, sans changer une
seule des phrases d'origine ni le ton. 1 150 caractères, 70,87 s de voix,
75,37 s avec le carton de clôture.
