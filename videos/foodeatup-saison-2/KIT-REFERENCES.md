# Kit de références et voix de Michael — à créer une seule fois

## 1) Références Higgsfield (uploadées une fois, réutilisées sur les 60 prompts)

| Référence | Contenu | Rôle dans le prompt |
|---|---|---|
| `@Image 1` | Portrait de Michael, face caméra, lumière douce, fond neutre, expression neutre, pas de lunettes de soleil | Identité (visage, cheveux, morphologie) |
| `@Image 2` | Michael en pied, **tenue de saison verrouillée** — telle qu'elle apparaît dans les plans déjà générés : **veste de cuisinier blanche, tablier blanc portant le logo FoodEatUp, toque blanche** | Tenue |
| `@Image 3` | La salle du restaurant, vide, de jour, sans enseigne lisible | Lieu salle |
| `@Image 4` | La cuisine professionnelle, passe et inox | Lieu cuisine |
| Option | Soul ID « Michael » entraîné dans Higgsfield, sélectionné en plus de `@Image 1` | Verrou d'identité renforcé |

⚠️ La tenue décrite ci-dessus est celle **constatée dans les plans de l'épisode 01 déjà générés**
(veste et tablier blancs, toque, logo brodé) — elle diffère de la proposition initiale du brief
(chemise blanche, tablier noir). C'est la version tournée qui fait foi : elle est reconduite sur
les 29 autres épisodes. Toute décision de la changer implique de regénérer les plans existants.

Sur Higgsfield, adaptez la numérotation à l'ordre réel de vos uploads. Chaque prompt commence par :

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit), keep identical. Location = @Image 3.
```

Tout ce qui doit rester identique est **référencé, jamais décrit**. Un accessoire de genre maximum
par épisode (sifflet, casque de livreur, visière de croupier, trench, veste de smoking) : il est
ajouté dans la ligne REF, il ne remplace jamais la tenue de saison.

## 2) Les 10 règles appliquées dans chaque prompt

1. Références d'abord, prompt ensuite.
2. Le prompt est une shot list avec timecodes (0–2 / 2–5 / 5–8 / 8–10 s), une action par plan, verbes observables.
3. Un hook dans les 2 premières secondes.
4. Les sélecteurs portent le genre (époque, lumière, physique, objectif) : on ne les répète pas dans le texte.
5. Dialogue en français, très court, entre guillemets, avec `spoken French, slow and clear, natural lip-sync`.
6. Jamais de texte lisible à l'image : tous les textes arrivent au montage.
7. Aucun âge, aucun mineur, aucune célébrité : des adultes décrits par leur rôle et leur tenue.
8. Corps du prompt en anglais, répliques en français.
9. Physique « réaliste » par défaut, « hyperbolique » seulement quand le gag l'exige.
10. Le visage, la coiffure et la tenue de saison ne changent jamais.

## 3) Lexique voix de Michael (anti-mauvaise prononciation)

Phrases de 1 à 4 mots, une idée par phrase, débit lent, ton sérieux dans l'absurde. Mots courants,
voyelles ouvertes, pas de liaisons piégeuses.

**Répliques de la saison** : « Attends. » · « C'est ma table. » · « Il est là. » · « Ils arrivent. » ·
« Il manque cinq euros. » · « J'ai dit dix. » · « C'est laquelle ? » · « Silence. » · « Encore ? » ·
« Une seconde. » · « Suivant. » · « Envoyer. » · « Belle journée. » · « Coupable. » · « Trois cents. » ·
« Parfait. » · « C'est pas ici. » · « Ça marche pas. » · « Je suis. » · « C'est presque ça. » ·
« Donne. » · « Je réponds plus. » · « Moi ? » · « Je gère. » · « Trente. » · « Il paie quand ? » ·
« Faites tourner la roue ! » · « Merci maman. » · « Oh. » · « Ah. » · « Coupez. »

**À éviter** : « malheureusement », « organisationnellement », « synchronisation »,
« approvisionnement », « spécifiquement », les chiffres au-dessus de vingt dits en une fois
(préférer « trois cents »), les anglicismes.
Exception assumée : « Deux cent quatre-vingt-dix-neuf » (épisode 17), c'est le gag.

**La marque** : « FoodEatUp » n'est **jamais** dit par l'avatar Seedance. Il est dit par la voix off
du montage (ElevenLabs, même voix sur les 30 épisodes). Ce point est vérifié automatiquement par
`npm run check`. Si vous voulez absolument le faire dire à Michael (épisode 30), écrivez dans le
prompt : `pronounced "Foud-Ite-Eup"`.

## 4) Ce que Seedance 2.5 change (vérifié août 2026)

| Capacité | Conséquence pour la saison |
|---|---|
| Clips jusqu'à 30 s en une génération | On reste sur 2 × 10 s : moins cher à re-roller, plus simple à corriger |
| Audio généré dans la même passe | Les répliques françaises se placent dans le prompt, entre guillemets |
| Jusqu'à 50 références | Michael est référencé, pas décrit |
| Region edit | Un visage qui dérive = une retouche, pas un re-roll |
| Shot re-generate | Une chute ratée = un plan à refaire, pas 10 s |
| Sélecteurs (époque, genre, lumière, physique, objectif, émotion, rythme) | Le look se règle dans l'interface, le prompt ne porte que l'action |
| 480p / 720p / 1080p + upscale 4K | 480p pour valider, 720p ou 1080p pour le rendu final |
