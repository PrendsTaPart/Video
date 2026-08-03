# Tutoriel — Ajouter une température de production (Plats) FoodEatUp

Module **HACCP** (1ère vidéo publiée du module, voir `videos/LOVABLE-FOODEATUP-DOCS.md`).

**STATUT : BROUILLON — en attente de validation avant toute génération audio ou montage**
(règle `FOODEATUP-TUTORIELS-WORKFLOW.md`, étape 3 : STOP obligatoire).

## Pas de séquence Claude sur cette vidéo

`add_temperature` (MCP) ne couvre que l'onglet Équipements (température frigo/four…),
pas l'onglet Plats montré ici. `create_recipe`/`create_dish` n'ont pas les champs vus à
l'écran (allergènes, durée de vie, pièce jointe, seuil recommandé). Aucun outil MCP ne
correspond exactement à l'action filmée → pas de prompt inventé, pas de séquence chatbot
en fin de vidéo (voir détail dans STORYBOARD.md).

## Voix off (brouillon, 8 lignes, voix Adam FR)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Contrôler la température de vos plats sur FoodEatUp ? Quelques secondes suffisent. | carte d'intro |
| N1 | Dans Production, ouvrez Températures puis cliquez sur Ajouter un relevé. | clic "+ Ajouter un relevé" |
| N2 | Choisissez un plat déjà enregistré dans la liste... | sélection dropdown ("suchi - haccp_recipe") |
| N3 | ...ou créez-en un nouveau à la volée avec Ajouter une recette : nom, allergènes, durée de conservation. | modale "Nouvelle recette" |
| N4 | Saisissez la température mesurée : FoodEatUp la compare aussitôt au seuil recommandé. | champ "Saisie température" + "Recommandé : +63°C minimum" |
| N5 | Ajoutez une photo si besoin, puis validez avec Enregistrer. | pièce jointe + clic "Enregistrer" |
| N6 | Votre relevé apparaît dans la liste, conforme ou non conforme en un coup d'œil. | résultat : carte "Pizza" 63.0°C, stats mises à jour |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) |

N7 est la ligne CTA standard, réutilisable telle quelle (déjà en stock dans plusieurs
`vo/N*.mp3` d'autres tutoriels si on veut éviter un aller-retour ElevenLabs).

## Points à confirmer avant de lancer la génération

1. **Nom exact à donner au tutoriel / slug Lovable** — proposition : `ajouter-temperature-plat`
   (module `haccp`, sous-catégorie à préciser — quel est le nom du sous-dossier Drive
   correspondant, pour rester cohérent avec `LOVABLE-FOODEATUP-DOCS.md` ?).
2. Le rush montre aussi une recette "suchi" existante utilisée comme exemple — nom à
   garder tel quel dans la démo ou anonymiser ?
3. Durée cible : le rush brut fait 73,9 s mais contient un remplissage assez long du
   formulaire "Nouvelle recette" (allergènes, portions, difficulté, catégorie) qui sera
   fortement accéléré au montage (comme le remplissage de tags sur `foodeatup-categories-tuto`).
   OK pour viser ~35-45 s de vidéo finale ?
4. Confirmer l'absence de séquence Claude (voir ci-dessus) — ou signaler un outil MCP
   Plats/HACCP que j'aurais manqué.

Une fois ce script validé (tel quel ou après ajustements), je lance la génération des
lignes VO (ElevenLabs, voix Adam FR) puis le montage.
