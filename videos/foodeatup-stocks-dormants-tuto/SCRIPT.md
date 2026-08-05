# Tutoriel — Booster les stocks dormants (Iris, opportunités IA)

Catalogue cible : `videos/CATALOGUE-157-TUTORIELS.md`, item **23 « Booster les Stocks
(opportunités IA) »**, module `marketing-fidelite` (Marketing, Fidélité & Iris —
0/24 publié à ce jour). Intrants reçus (chat) :
- `assets/intro.jpg` — carte "BOOSTER LES STOCKS DORMANTS" (photo + logo FoodEatUp,
  CTA "REJOIGNEZ-NOUS").
- `assets/outro.jpg` — carte de fin CTA, **identique** (md5 `bd812eb81382fbbcb5303d06101e6538`)
  à celle déjà réutilisée sur `foodeatup-vitrine-tuto` et `foodeatup-predibot-tuto`.
- `assets/screen.mp4` — écran capturé, 1920×828, 25 fps, **23,40 s**, piste audio
  silencieuse (-91 dB, aucune VO native).

## Déroulé observé dans le rush (frames extraites toutes les 0,25 s)

| t (rush) | Contenu |
|---:|---|
| 0,0 – 5,1 s | Page **Iris** (`L'agent qui détecte les bonnes raisons de publier`), onglet **Opportunités** actif. Une opportunité déjà présente : « Nouveau plat » — Dragon Roll 6 pcs (45 €), score 42. |
| ~5,1 s | Clic sur **Redétecter maintenant** (bouton bleu, bbox mesurée 1478,402→1795,463 sur le rush, centre 1636,432). |
| 5,1 – 8,7 s | Bouton grisé/désactivé (analyse en cours), aucune nouvelle carte encore visible. |
| 8,7 – 11,2 s | Les résultats basculent : cartes **Surstock** (icône boîte), premier lot #20609 / #20610, toast **« 11 signal(aux) détecté(s). »**. |
| 11,2 – 19,8 s | Défilement à travers la liste : #20611, #20612, #20614, #20615, #20616, #20547 — chaque carte affiche `Surstock de Produit importé #<id> (<qté> <unité>, <mult>× le seuil) — une mise en avant l'écoulerait.` et son score `urgence/valeur/fraîcheur`. |
| 19,8 – 23,4 s | Retour en haut de la liste (scroll remonté), la carte #20610 visible sous le bandeau Opportunités. |

Aucune étape de saisie/formulaire : la fonctionnalité est 100 % détection + lecture, un
seul clic ("Redétecter maintenant") déclenche tout.

## Recherche d'un outil MCP correspondant (règle `LOVABLE-FOODEATUP-DOCS.md` étape 3)

Passé en revue les outils `mcp__FoodEatUp__*` disponibles (stock, marketing, finance…).
Aucun outil ne réplique littéralement "détecter mes surstocks" (pas de
`list_high_stocks`/`detect_opportunities`). Le plus proche par la fonction réelle —
un agent IA qui transforme des données business réelles en actions marketing
concrètes — est **`propose_campaigns(establishment_id)`** : *"Agent IA marketing :
2-4 propositions de campagnes chiffrées depuis les données réelles (RFM, jours creux,
marges, marronniers)."* C'est le même geste que celui montré à l'écran (un agent qui
scanne vos données et vous propose une action commerciale), donc le prompt Claude
pousse à appeler cet outil plutôt que d'inventer un outil de détection de stock
inexistant.

## Voix off proposée (9 lignes) — SOUMISE À VALIDATION, AUCUN AUDIO GÉNÉRÉ

| # | Texte | Ancrage |
|---|---|---|
| N0 | Des produits qui dorment en réserve ? Iris les repère pour vous. | carte d'intro |
| N1 | Direction l'agent Iris, onglet Opportunités : elle a déjà une piste pour vous. | A (état initial, carte Nouveau plat) |
| N2 | Cliquez sur Redétecter maintenant pour lancer une analyse fraîche de vos stocks. | clic B (zoom-punch) |
| N3 | En quelques secondes, Iris repère vos surstocks — produit, quantité, seuil dépassé. | C→D (chargement + résultats + toast) |
| N4 | Chaque opportunité est notée sur l'urgence, la valeur commerciale et la fraîcheur. | E (défilement, scores) |
| N5 | Plus le score est élevé, plus une mise en avant écoulera vite ce stock qui dort. | F (fin de défilement, retour en haut) — bénéfice |
| N6 | Vous pouvez aussi demander à Claude d'analyser vos données : copiez ce prompt, remplacez les crochets. | étage 1+2 (reveal + copié) |
| N7 | Collez-le dans la conversation : Claude vous propose des campagnes chiffrées pour écouler le surplus. | étage 3 (mockup chatbot) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA, **réutilisable telle quelle**, même image que `foodeatup-predibot-tuto`) |

N8 candidat à réutilisation directe (copie du .mp3) depuis un tuto précédent portant
exactement ce texte (ex. `foodeatup-predibot-tuto/vo/N7.mp3`, déjà réutilisé 3× selon
`FOODEATUP-TUTORIELS-WORKFLOW.md`) — à vérifier par relecture du texte avant réemploi,
pas seulement sa durée.

## Découpage envisagé (targets à ajuster sur les durées VO réellement mesurées)

| Seg | Source | Target | Contenu |
|---|---:|---:|---|
| intro | carte | 4,60 s | BOOSTER LES STOCKS DORMANTS |
| A | 0,20 → 5,10 | 5,60 s | État initial : carte "Nouveau plat" + bouton Redétecter (bandeau "1 · Repéré par Iris") |
| B | 5,10 → 5,40 | 0,95 s | **zoom-punch** sur Redétecter maintenant (1636, 432 ; taille ~317×61) |
| C | 5,40 → 8,70 | 1,60 s | Analyse en cours (bouton grisé), accéléré (bandeau "2 · Nouvelle analyse") |
| D | 8,70 → 11,20 | 3,40 s | Résultats + toast "11 signal(aux) détecté(s)" (bandeau "11 opportunités détectées") |
| E | 11,20 → 16,20 | 4,60 s | Défilement scores urgence/valeur/fraîcheur (bandeau "Score : urgence × valeur × fraîcheur") |
| F | 16,20 → 23,40 | 5,20 s | Fin de défilement + retour en haut (bandeau "Prêt à agir") |
| claude1 | carte générée | 3,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,30 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA (réutilisée) |

Durée cible ≈ 38-42 s une fois les segments recalés sur la durée réelle de chaque ligne
VO mesurée après génération (suivre `FOODEATUP-TUTORIELS-WORKFLOW.md`, assertion de
drift dans `build.py` avant tout rendu final).

## Séquence Claude (prompt proposé — identique vidéo / fiche Lovable)

`mcp__FoodEatUp__propose_campaigns(establishment_id)` — agent IA marketing générant
2 à 4 propositions de campagnes chiffrées à partir des données réelles.

> Analyse les données de mon établissement FoodEatUp (ID [ID établissement]) et
> propose-moi 2 à 4 campagnes marketing chiffrées pour écouler mes surstocks.

Réplique assistant (bulle chatbot) : « Bien sûr ! J'analyse vos ventes, vos marges et
vos stocks pour vous proposer des campagnes ciblées… »

## Fiche Lovable envisagée (`src/data/tutorials.ts`)

```ts
{
  slug: "booster-les-stocks-dormants",
  title: "Booster les stocks dormants",
  moduleSlug: "marketing-fidelite",
  subcategory: "Marketing, Fidélité & Iris",
  videoUrl: "<à remplir après upload RapidoCMS>",
  thumbnailUrl: "<à remplir après upload RapidoCMS>",
  durationSeconds: 0, // à remplir après montage
  howItWorks: [
    "Ouvrez l'agent Iris, onglet Opportunités.",
    "Cliquez sur Redétecter maintenant pour lancer une analyse fraîche.",
    "Repérez vos surstocks : produit, quantité, et seuil dépassé.",
    "Comparez les opportunités grâce au score urgence, valeur et fraîcheur.",
    "Mettez en avant les produits prioritaires avant qu'ils ne deviennent une perte.",
  ],
  whatItsFor: "Iris scanne vos stocks chaque nuit et vous signale les produits en " +
    "surstock avant qu'ils ne deviennent une perte sèche — il ne vous reste qu'à " +
    "valider une mise en avant pour les écouler.",
  claudePrompt: "Analyse les données de mon établissement FoodEatUp (ID [ID établissement]) " +
    "et propose-moi 2 à 4 campagnes marketing chiffrées pour écouler mes surstocks.",
  chefTip: "Un stock qui dort est un stock qui coûte cher. Laissez Iris vous prévenir " +
    "avant que ça tourne, et transformez le surplus en promo qui cartonne.",
}
```

## Statut

**Script v1 soumis à validation (STOP obligatoire, règle
`FOODEATUP-TUTORIELS-WORKFLOW.md` §3) — aucun audio ElevenLabs généré, aucun montage
lancé.** En attente d'un retour avant de passer à la génération VO (voix Adam FR
`TGAegA0zNRi8I6nUdq3i`) puis au montage (`build.py`, calqué sur
`foodeatup-mouvements-stock-tuto/build.py`, référence la plus récente pour `banner()`).
