# Tutoriel — Gérer ses Tables (ajout & blocage)

Module `caroline-ia` (Agent IA Caroline & Salle), tutoriel **04/6** — catalogue
`videos/CATALOGUE-157-TUTORIELS.md` : « 04 Gérer ses **Tables** (ajout & blocage) ».
Module vierge à ce jour (0/6 publiés, voir `videos/PROGRESSION-157-TUTORIELS.md`) : premier
tutoriel de la série `caroline-ia`.

Intrants reçus le 2026-08-06 :
- `assets/intro.jpg` — carte d'ouverture "GÉRER SES TABLES AJOUT & BLOCAGE"
- `assets/outro.jpg` — carte de fin CTA (réutilisation confirmée, md5 `bd812eb81382fbbcb5303d06101e6538`,
  identique à 89 autres tutoriels déjà publiés, ex. `foodeatup-abonnement-tuto/assets/outro.jpg`)
- `assets/screen.mp4` — écran capturé, 1920x828, 25 fps, **64,09 s**, piste audio silencieuse
  (-91 dB, vérifié par `volumedetect`)

## Déroulé observé dans le rush

| t (rush) | Contenu |
|---:|---|
| 0,0 – 4,5 s | Page "Plan de salle" (vue normale) : compteurs (Tables 8, Libre 0, Occupées 4, Réservées 1, Taux d'occupation 63%), légende (Libre/Réservée/Occupée/Nettoyage/Bloquée), onglets Toutes/Salle principale/Terrasse. Table **T3** (occupée, rouge) sélectionnée — panneau "Changer le statut" à droite |
| 4,5 – 5,5 s | Clic sur "Éditer" (bouton haut droit) |
| 5,5 – 8,5 s | Bascule en **Mode édition** : "Ajoutez, gérez vos tables puis Enregistrer", boutons "Ajouter une table" / "Enregistrer" / "Vue" |
| 8,5 – 9,5 s | Clic sur "Ajouter une table" → nouvelle table **T9** créée, formulaire à droite : Nom de la table, Forme (Ronde/Carrée/Rectangle), Capacité (couverts, stepper), Zone (menu déroulant) |
| 9,5 – 32,0 s | Configuration de T9 : forme réglée sur **Rectangle**, capacité augmentée via le stepper (4 → 12 couverts), zone réglée sur **Salle principale** |
| 32,0 – 40,5 s | Clic sur "Enregistrer" → retour à la vue normale. Compteurs mis à jour (Tables **9**, Libre **1**, Taux d'occupation 56%) |
| 40,5 – 41,5 s | Clic sur la nouvelle table **T9** (verte, Libre) → panneau "Changer le statut" : Libre (vert, actif) / Réservée / Occupée / Nettoyage / Bloquée |
| 41,5 – 53,0 s | Clic sur **Réservée** → badge T9 passe orange, compteurs mis à jour (Réservées 2, occupation 67%) |
| 53,0 – 56,0 s | Clic sur **Nettoyage** → badge T9 passe gris |
| 56,0 – 58,0 s | Clic sur **Bloquée** → badge T9 passe noir, table grisée/assombrie sur le plan |
| 58,0 – 61,5 s | Curseur reste sur "Bloquée" quelques secondes (mise en avant du statut), puis clic sur **Libre** |
| 61,5 – 64,1 s | Badge T9 repasse vert (Libre) → la table redevient disponible |

Séquence clé : la table T9 traverse **Libre → Réservée → Nettoyage → Bloquée → Libre**,
démontrant que le blocage est réversible en un clic (pas de suppression).

## Outils MCP FoodEatUp correspondants

`mcp__FoodEatUp__create_table(establishment_id, name, shape?, capacity?, zone_id?)` —
correspond exactement à l'étape "Ajouter une table" du rush (nom, forme, capacité, zone).

`mcp__FoodEatUp__update_table_status(establishment_id, table_id, status)` — statuts
`free|reserved|occupied|cleaning|blocked` — correspond exactement à l'étape "Changer le
statut" du rush (blocage puis déblocage de T9).

**Séquence Claude affichée dans la vidéo (1 seul prompt, règle du pipeline)** : choix du
prompt "Ajouter une table" (`create_table`), car c'est le premier geste métier du rush et le
plus proche d'une création de contenu classique de la série.

> Ajoute une table nommée [nom de la table] pour mon établissement FoodEatUp (ID [ID
> établissement]), capacité [nombre] couverts, forme [ronde/carrée/rectangle].

**Second prompt, fiche Lovable uniquement (`claudePrompts[1]`, pas dans la vidéo — les deux
actions sont montrées à l'écran, mais la règle du pipeline limite la vidéo à un seul prompt
affiché)** :

> Bloque la table [nom ou numéro de la table] pour mon établissement FoodEatUp (ID [ID
> établissement]) — par exemple pour une panne ou des travaux.

## Voix off (9 lignes) — N6 et N8 réutilisables tels quels (zéro coût ElevenLabs)

| # | Texte | Source |
|---|---|---|
| N0 | Une table cassée, en travaux, ou un service qui s'annonce chargé ? Voici comment gérer vos tables dans FoodEatUp. | à générer |
| N1 | Depuis le plan de salle, passez en mode édition pour ajouter ou modifier vos tables. | à générer |
| N2 | Cliquez sur Ajouter une table : choisissez sa forme, sa capacité, et sa zone. | à générer |
| N3 | Enregistrez : votre nouvelle table apparaît aussitôt sur le plan, disponible. | à générer |
| N4 | Cliquez sur une table pour changer son statut : réservée, en nettoyage, ou bloquée si elle est indisponible. | à générer |
| N5 | Une table bloquée n'est plus proposée en réservation — idéal pour une panne ou des travaux. Un clic suffit pour la remettre disponible. | à générer |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | **réutilisable** (ex. `foodeatup-zones-nettoyage-tuto/vo/N6.mp3`, texte identique) |
| N7 | Collez-le dans la conversation : votre table est ajoutée à votre plan de salle en quelques secondes. | à générer (spécifique, jamais réutilisable) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | **réutilisable** (carte de fin CTA, md5 identique sur toute la série) |

## Découpage envisagé (segments, à affiner sur coordonnées pixel au montage)

| Seg | Source (raw) | Contenu |
|---|---|---|
| intro | carte | GÉRER SES TABLES AJOUT & BLOCAGE |
| A | 0,00 → 5,50 | Vue normale + **zoom-punch** clic "Éditer" |
| B | 5,50 → 8,50 | Mode édition + **zoom-punch** clic "Ajouter une table" |
| C | 8,50 → 32,00 | Formulaire T9 : forme / capacité / zone |
| D | 32,00 → 40,50 | **zoom-punch** clic "Enregistrer" → retour vue normale, compteurs à jour |
| E | 40,50 → 41,50 | **zoom-punch** clic sur T9 (verte) → panneau statut |
| F | 41,50 → 58,00 | Cycle de statuts : Réservée → Nettoyage → Bloquée (badge + table s'assombrissent) |
| G | 58,00 → 64,09 | **zoom-punch** clic "Libre" → table redevient disponible |
| claude1-3 | générées | séquence "Utilisez cette fonctionnalité avec Claude" (module partagé `_shared/claude_prompt_sequence.py`), prompt "Ajouter une table" |
| outro | carte | CTA (réutilisée) |

## Fiche Lovable (à publier après validation vidéo)

- **howItWorks** :
  1. Ouvrez votre Plan de salle et passez en mode édition.
  2. Cliquez sur Ajouter une table : donnez-lui un nom, une forme et une capacité.
  3. Assignez-la à une zone (salle principale, terrasse…) puis enregistrez.
  4. Cliquez sur une table existante pour changer son statut : libre, réservée, occupée,
     nettoyage ou bloquée.
  5. Bloquez une table indisponible (panne, travaux) — elle ne sera plus proposée en
     réservation tant qu'elle reste bloquée, et redevient disponible en un clic.
- **whatItsFor** (cas d'usage) : Adaptez votre plan de salle en temps réel : ajoutez une
  table pour un service chargé, ou bloquez-en une indisponible (table cassée, travaux,
  terrasse fermée) sans la supprimer — elle redevient disponible en un clic dès que la
  situation est réglée.
- **chefTip** (astuce du chef) : Plutôt que de supprimer une table indisponible, bloquez-la.
  Vous gardez son historique et ses réservations, et elle réapparaît instantanément dès que
  vous la repassez en Libre.
- **claudePrompt** : voir prompt "Ajouter une table" ci-dessus.
- **claudePrompts[1]** : prompt "Bloquer une table" ci-dessus (titre : "Bloquer une table").

## Statut

Montage terminé : durée livrée **63,40 s** — H.264/yuv420p 1920x828, AAC 48 kHz stéréo,
faststart confirmé. VO générée pour N0-N5 et N7 (Adam FR, ElevenLabs) ; N6 et N8 réutilisés
tels quels (texte identique, zéro coût). Peak audio final **-7,21 dBFS** (`astats`), aucun
écrêtage. Bug rencontré et corrigé pendant le montage : le zoom-punch du segment final
("Bloquée → Libre") couvrait toute la fin du rush (57,45→64,09 s source) alors que la page
défile et revient en haut d'écran sur les 2 dernières secondes — même piège que documenté
dans `FOODEATUP-TUTORIELS-WORKFLOW.md` ("ne pas supposer un bouton immobile d'un bout à
l'autre du rush"), corrigé en recadrant la source du segment à 57,45→62,00 s (juste après la
confirmation visuelle du retour à Libre, avant que la page ne défile). Vérification visuelle
faite sur bandeaux (lisibles), zoom-punch (cadrage correct sur toute sa durée après
correction), séquence Claude (3 étages corrects), première/dernière frame (cartes intro/outro).

**STOP obligatoire (règle `LOVABLE-FOODEATUP-DOCS.md` §"Règle de validation") : vidéo livrée
pour validation. Pas de publication (RapidoCMS, LinkedIn, Lovable) tant qu'un retour OK
explicite n'est pas reçu.**
