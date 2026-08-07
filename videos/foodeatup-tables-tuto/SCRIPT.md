# Tutoriel — Gérer ses tables (ajout & blocage)

Module `caroline-ia` (Agent IA Caroline & Salle), catalogue 157 tutoriels, 6a-04
« Gérer ses Tables (ajout & blocage) ». Rush fourni par Michael : 64,08 s, 1920x828,
25 fps, piste audio silencieuse (-91 dB — pas de voix native à conserver).
Carte d'intro et carte de fin (CTA générique) fournies telles quelles par Michael.

## Voix off (13 lignes, Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Segment |
|---|---|---|
| N0 | Ajouter une table, la bloquer le temps d'un imprévu : tout se passe dans Plan de salle. | carte intro |
| N1 | Ici, vous voyez toutes vos tables d'un coup d'œil, avec leur statut en temps réel : libre, réservée, occupée, en nettoyage ou bloquée. | A |
| N2 | Cliquez sur Éditer, puis sur Ajouter une table pour en créer une nouvelle. | clic B + C |
| N3 | Choisissez sa forme, ronde, carrée ou rectangulaire. | E |
| N4 | Réglez son nombre de couverts, affectez-la à une zone comme la Salle principale, puis cliquez sur Enregistrer. | F + clic G |
| N5 | Votre table apparaît aussitôt sur le plan, prête à accueillir vos clients. | H |
| N6 | D'un clic, changez son statut : réservée pour un client attendu, en nettoyage entre deux services. | I |
| N7 | Et si une table est cassée ou hors service, passez-la en Bloquée : elle disparaît des disponibilités sans être supprimée. | clic J + K |
| N8 | Un nouveau clic suffit pour la libérer dès qu'elle est de nouveau utilisable. | clic L + M |
| N9 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | étages 1+2 (réutilisé du module) |
| N10 | Collé dans le presse-papiers ! | étage 2 |
| N11 | Collez-le dans la conversation : votre table est ajoutée en quelques secondes. | étage 3 |
| N12 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (réutilisé de la série) |

N9 réutilisée telle quelle (règle du workflow) ; N11 est spécifique à ce tutoriel (nomme
l'objet créé par Claude) — ne jamais la copier telle quelle d'un autre tuto.

## Découpage (timeline du rush)

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 4,60 s | GÉRER SES TABLES AJOUT & BLOCAGE |
| A | 0,00 → 4,30 | 5,00 s | Plan de salle : 8 tables, compteurs (Libres/Occupées/Réservées/Taux), légende des 5 statuts, table T3 « Occupée » sélectionnée |
| B | 4,30 → 4,60 | 0,90 s | **zoom-punch** sur le bouton Éditer |
| C | 4,60 → 10,60 | 4,20 s | mode édition, en-tête « Mode édition — glissez les tables puis Enregistrer », bouton Ajouter une table |
| D | 10,60 → 10,90 | 0,90 s | **zoom-punch** sur Ajouter une table |
| E | 10,90 → 19,20 | 4,60 s | table T9 créée (4 couverts, forme Carrée) puis forme changée en Rectangle |
| F | 19,20 → 40,00 | 6,50 s | capacité 4 → 8 → 12 couverts, zone réglée sur Salle principale (accéléré) |
| G | 40,00 → 40,30 | 0,90 s | **zoom-punch** sur Enregistrer |
| H | 40,30 → 44,00 | 3,20 s | retour en vue normale, T9 visible sur le plan en vert « Libre », compteurs mis à jour (9 tables, Salle principale 4) |
| I | 44,00 → 50,00 | 4,60 s | panneau « Changer le statut » : Libre (par défaut) puis Réservée |
| J | 50,00 → 53,00 | 3,20 s | Réservée (orange) → Nettoyage (gris) — cycle accéléré |
| K | 53,00 → 56,00 | 0,90 s | **zoom-punch** sur Bloquée |
| L | 56,00 → 60,50 | 4,00 s | table T9 en noir « Bloquée » — disparaît des disponibilités |
| M | 60,50 → 64,08 | 3,60 s | retour à Libre (vert) en un clic — table de nouveau disponible |
| claude1 | carte générée | 5,50 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,60 s | « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,80 s | mockup chatbot Claude |
| outro | carte | 6,20 s (auto-étendue) | CTA |

Découpage établi par extraction d'images (1 img/s puis 2 img/s sur les fenêtres
sensibles, `ffmpeg -vf fps=...`) et détection de changements de scène
(`select='gt(scene,0.03)'`) recoupée avec une inspection visuelle image par image —
pas de timestamp deviné. Le cycle Réservée/Nettoyage (segment J) est montré rapidement
sans zoom-punch dédié (déjà illustré une fois par Libre en segment I) ; seul le clic sur
**Bloquée** (le second mot du titre, avec Ajouter une table et Enregistrer) reçoit un
zoom-punch, cohérent avec la règle « 3 clics clés » du reste de la série.

## Séquence Claude — module partagé

`mcp__FoodEatUp__create_table(establishment_id, name, capacity, shape, zone_id)` couvre
exactement l'ajout de table montré dans le rush (nom, forme, capacité, zone). Prompt
utilisé dans la vidéo :

> Ajoute une table nommée [nom] pouvant accueillir [nombre] couverts dans mon
> établissement FoodEatUp (ID [ID établissement]).

Second outil couvrant le blocage (`mcp__FoodEatUp__update_table_status`, status=
`blocked`), documenté en `claudePrompts[]` côté site uniquement (pas animé dans la
vidéo, un seul prompt est mis en scène par rush) :

> Passe la table [nom de la table] en statut Bloquée pour mon établissement FoodEatUp
> (ID [ID établissement]).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade 0,28 s, bandeaux
d'étape (aucune apostrophe — bug `drawtext` connu), encadré orange pulsant→statique sur
les 3 clics (Éditer, Ajouter une table, Bloquée), `setpts` pour la vitesse (jamais
`zoompan` sur du rush réel).

## Comment ça marche (`howItWorks`, pour la fiche Lovable)

1. Ouvrez **Plan de salle** pour voir toutes vos tables et leur statut en temps réel.
2. Cliquez sur **Éditer** puis sur **Ajouter une table**.
3. Choisissez sa **forme** (ronde, carrée, rectangle) et son **nombre de couverts**.
4. Affectez-la à une **zone** (Salle principale, Terrasse…), puis cliquez sur
   **Enregistrer**.
5. Sélectionnez une table sur le plan pour changer son **statut** en un clic : Libre,
   Réservée, Occupée, Nettoyage ou Bloquée.
6. Passez une table cassée ou hors service en **Bloquée** : elle reste dans votre plan
   mais disparaît des disponibilités, sans être supprimée.
7. Un nouveau clic sur **Libre** la remet en service dès qu'elle est de nouveau
   utilisable.

## Astuce du chef (`chefTip`)

Ne supprimez jamais une table pour la sortir temporairement du service : ça casse
l'historique de ses commandes et il faut tout reconfigurer (forme, capacité, zone,
QR code) quand elle revient. Le statut **Bloquée** fait exactement ce qu'il faut — la
table disparaît des tables proposables (réservation, plan de salle client) mais tout
son paramétrage reste intact, prêt à repasser en Libre en un clic dès que la table est
de nouveau disponible (réparation, table en trop en période creuse, etc.).

## Cas d'usage

- **Table endommagée** : un pied cassé, une chaise en réparation → Bloquée le temps de
  la remise en état, sans perdre la fiche de la table.
- **Ajustement saisonnier** : une salle qui se resserre en semaine creuse → bloquer les
  tables en trop plutôt que les supprimer, pour les rouvrir d'un clic le week-end.
- **Nouvelle terrasse ou extension** : ajouter rapidement les tables d'une nouvelle
  zone (capacité, forme, zone) avant l'ouverture, ou depuis Claude en langage naturel.
- **Formation d'un nouvel employé** : montrer le cycle complet des 5 statuts
  (Libre → Réservée → Occupée → Nettoyage → Bloquée) sur une table de test.

## Statut publication

Vidéo montée à partir du rush + de la carte d'intro + de la carte de fin fournis par
Michael. Voir `LOVABLE-FOODEATUP-DOCS.md` pour la publication (module `caroline-ia`,
catégorie « Agent IA Caroline & Salle »).
