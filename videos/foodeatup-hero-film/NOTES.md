# Film héros — « Le même jour, deux fois »

**19ᵉ vidéo du projet, et la plus importante : c'est le film central du site.**
3 min 45 · 16:9 · spécification figée le 2026-08-08.

La timeline exploitable par le pipeline est dans **`hero.json`** — frames,
transitions, lexique sonore, sources S3 résolues, plans à tourner. Ce fichier-ci
explique les décisions ; `hero.json` est ce que le code consomme.

---

## 1. Le concept en une ligne

Une seule journée, jouée deux fois, **phase par phase** :

> Avant sans → **Avant avec** → Pendant sans → **Pendant avec** → Après sans → **Après avec**

Jamais plus de 25 secondes de douleur avant la résolution. Et cette alternance
**est exactement le bouton du site** : le film enseigne le geste qu'on demandera
ensuite au visiteur de faire sur la page.

## 2. Le parti pris qui porte tout

**Pas de narrateur.** Ce sont les trois mêmes personnes qui parlent dans les
deux versions — même chef, même serveur, même directeur. Voix plate et lassée
côté « sans », la même voix redressée côté « avec ». Le spectateur compare
tout seul, ce qui est infiniment plus crédible qu'une voix off qui explique.

Une seule quatrième voix, une seule phrase, à 3:26 :

> « Ce n'est pas la même journée. C'est le même restaurant. »

**Conséquence de tournage, non négociable** : les paires « sans » et « avec »
d'un même personnage se tournent **dos à dos, le même jour**, même cadrage,
même focale, même position de caméra — on ne change que l'accessoire et la
lumière. Deux acteurs différents, ou trois semaines d'écart avec une coupe de
cheveux différente, et tout l'effet s'effondre. Les trois portraits de clôture
se tournent au même réglage lumière, sinon le triptyque final ne tient pas.

## 3. Ce qui est déjà résolu

**13 des 14 séquences d'écran sont récupérables** dans les tutoriels déjà en
ligne — rien à refilmer. Les URLs S3 exactes sont dans `hero.json`
(`sequencesEcranSource`), chacune avec son timecode, son extrait et sa durée.

Une seule est inaccessible : `mes-commandes-tous-canaux`
(`foodeatup-mes-commandes-tuto-v1`, **403**). C'est la même que celle qui
bloquait déjà la série des 9 films — elle porte ici le beat A de la séquence 4,
la convergence multi-canal.

**Deux écrans n'existent nulle part** : le ticket Z (module Caisse POS, à
tourner — et c'est un plan clé) et la rupture non signalée côté « sans » (à
fabriquer en motion design, maquette grise).

## 4. Les trois règles que le pipeline doit faire respecter

**Le balayage bleu.** Ligne verticale `#1E9BF0` traversant l'écran en 21 frames
(700 ms). Désaturation qui se retire, son qui se résout, ligne brisée qui se
recompose : les quatre effets pilotés par **la même** valeur de progression,
un seul hook `useWipeProgress()`. Trois occurrences : frames 1200, 3000, 5100.
La transition inverse est un repli sec de 12 frames, sans easing — le retour à
la douleur ne se fait pas en douceur.

**Le « clin » sonne exactement trois fois.** Frames 3870 (le plat passe au vert),
5940 (le chiffre du jour), 6690 (seul, sur le logo). Un son de marque qui
revient toutes les dix secondes devient un tic ; trois occurrences dont une
isolée, c'est ce qui le grave. Un test doit échouer si le compte diffère.

**La séquence 4 est intouchable.** Frames 3000–4350 : convergence multi-canal,
Jarvis multilingue, l'envoi, Iris. Si le film doit être raccourci, le script
raccourcit S1, S3, S5 — et **échoue** plutôt que d'entamer S4.

## 5. Le beat Jarvis multilingue (frames 3360–3750)

Deux commis, deux langues, même intention. Traitement strictement identique :
même cadrage, même durée à la frame près, même lumière, même taille de
sous-titre. **Aucun label de langue, aucun drapeau, aucun effet de traduction
animée.** Les deux sous-titres en français, dans le même style.

Le propos est que l'outil s'adapte à l'équipe — pas que l'équipe est étrangère.
En cuisine française une brigade parle couramment trois langues ; le montrer
normalement est déjà un argument. Le composant `BeatJarvisMultilingue.tsx`
doit garantir la symétrie **par construction** : mêmes props pour les deux
volets, impossible d'en styliser un différemment.

## 6. L'identité sonore

C'est la partie la plus sous-estimée du projet et probablement celle qui fera
la différence. **Le son du passe est le seul langage que partagent la cuisine,
la salle et le bureau.**

Le « clin » s'enregistre en vrai, sur une vraie cloche, avec la réverbération
du lieu — jamais une banque de sons — et s'accorde sur la tonique de la musique
(ré), pour que le dernier tombe pile sur la résolution. C'est ce qui le fait
ressentir comme un soulagement plutôt que comme un signal.

Distinction à tenir : **les sons d'action sont enregistrés dans le réel** (bip
de scanner, imprimante, tiroir, cloche), **le son de Jarvis est musical**.
C'est ce qui rend Jarvis attachant plutôt qu'inquiétant.

Les séquences « sans » sont mixées **1,5 dB plus fort** que les « avec » :
l'oreille perçoit le passage comme un soulagement physique, sans savoir
pourquoi. Leur inconfort ne vient pas du volume mais du **désaccord** (un quart
de ton) et de la **non-résolution** — la boucle ne retombe jamais sur sa
tonique, les fins de séquence sont coupées en milieu de mesure.

Trois silences complets, et ce sont des instruments : frames 0–360, 6210–6330
(les trois visages), et après le dernier clin.

## 7. Interdits de montage

Fondu au blanc, glitch, zoom transition, wipe circulaire, effet de particules.
Chacun crie « vidéo faite par une IA » et détruit la crédibilité documentaire
du film — qui est tout ce sur quoi il repose.

Contrainte juridique identique à la série « sans » : **aucun concurrent
identifiable**, même implicitement. Les interfaces grises sont des maquettes
neutres fabriquées par nous. Voir `../foodeatup-9-films/NOTES.md` §6.1.

## 8. Ce qu'il reste à obtenir

| | Nombre | Détail |
|---|---|---|
| Séquences d'écran récupérables | 13 | rien à faire, URLs dans `hero.json` |
| Séquence d'écran bloquée (403) | 1 | `foodeatup-mes-commandes-tuto-v1` |
| Écrans à créer | 2 | ticket Z (tournage) · rupture non signalée (motion) |
| Plans à tourner | 17 | dont 3 portraits de clôture, même réglage lumière |
| Sons à enregistrer | 8 | le clin en premier |
| Pistes voix | 4 | chaque métier enregistre « sans » et « avec » **dans la même session** |
| Images d'ambiance à générer | 10 | HERO-01 à HERO-10, prompts dans le dossier de production |

## 9. Ordre recommandé

1. **Enregistrer le « clin »** — une vraie cloche, plusieurs prises. C'est le
   seul asset dont dépend l'identité sonore de toute la marque, et il coûte
   une heure.
2. **Enregistrer les trois voix**, chacune ses répliques « sans » et « avec »
   à la suite. Puis les écouter bout à bout, sans image : **si ça tient debout
   à l'oreille seule, le film est bon.**
3. **Extraire les 13 séquences d'écran** — gratuit, une demi-journée.
4. **Tourner les 17 plans**, en une journée, dans un seul restaurant.
5. **Lancer le pipeline**, en validant le balayage bleu (palier P2) avant tout
   le reste.

## 10. Intégration au site

Le hero vidéo va sur le **site marketing** (`food-heartbeat-site`), pas sur
l'Academy — ce dépôt n'est pas dans le périmètre de la session actuelle.

Le point à ne pas rater : **une vidéo de 3 min 45 ne peut pas être le hero.**
Les navigateurs n'autorisent l'autoplay que muet, or le son *est* le concept.
D'où l'architecture retenue : boucle silencieuse de 12 s en fond (livrable à
part entière, composée spécifiquement — quatre plans de 3 s, aucun visage qui
parle, point de boucle invisible), poster JPEG en élément LCP préchargé, et le
film complet **avec le son** en lightbox au clic sur « Voir le film — 3 min 45 »
(annoncer la durée augmente nettement le taux de lecture).

Le film de 3'45 ne se charge qu'à l'ouverture de la lightbox. Pas de boucle du
tout si `prefers-reduced-motion`, `saveData`, ou connexion 2G.
