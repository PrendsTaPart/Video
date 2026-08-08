# « Une journée avec FoodEatUp » — notes de production

Série de **18 films** : 3 métiers (cuisine / serveur / directeur) × 3 phases
(avant / pendant / après) × 2 versions (**avec** / **sans** FoodEatUp).
Spécifications de référence : **v3** pour les parcours et les 9 films « avec »,
**dossier « Avec / Sans »** pour les 9 films miroir et le bouton bascule
(Michael, 2026-08-08). Ce fichier consigne ce qui est décidé, ce qui est
vérifié, et ce qu'il reste à obtenir.

---

## 1. État au 2026-08-08

| Chantier | État |
|---|---|
| Modèle de données des 3 parcours | ✅ en ligne — `foodeatup-guide-star/src/data/journees.ts` |
| Pages `/journee` et `/journee/:slug` | ⬜ à écrire |
| **Mode « sans » textuel + bouton bascule** | ⬜ **premier livrable, avant toute vidéo** |
| Les 66 captures d'écran | 🟡 sources identifiées, voir §3 |
| Les 42 images d'ambiance IA | ⬜ à générer (RapidoCMS) |
| Les 9 pistes voix off « avec » | ⬜ à générer (ElevenLabs) |
| Pipeline Remotion | ⬜ palier P1 non démarré |
| Les 9 films « sans » | ⬜ après validation du pilote D1′ |

**Parcours figés (107 étapes)** — cuisine 46 (07h00→23h00), salle 32
(09h30→23h00), direction 29 (08h00→18h00). Les 75 slugs référencés existent
tous dans le catalogue. Chronologie vérifiée **par bloc**, pas globalement.

---

## 2. Décisions

- **Les vidéos de caisse se tournent en dernier.** Le module Caisse POS est
  `comingSoon` dans `tutorials.ts`. Les six étapes salle qui en dépendent
  (fond de caisse, encaissement, séparation d'addition, remise, ticket Z midi
  et soir, écarts) s'affichent « bientôt disponible » et **se rallumeront
  d'elles-mêmes** le jour où le module s'ouvre — aucun code à retoucher.
- **Les 66 captures ne se refilment pas.** Elles se prélèvent dans les vidéos
  de tutoriels déjà en ligne : ce sont des enregistrements réels de
  l'interface, ce que la règle « aucune interface générée par IA » exige.
- **Les films ne portent pas encore d'URL.** `PhaseFilm.plannedFile` contient
  le nom de fichier attendu ; `videoUrl` reste vide tant que le fichier n'est
  pas dans la bibliothèque, pour ne jamais afficher un lecteur cassé.

---

## 3. Sources des 66 captures — ce qui est récupérable, ce qui manque

Le catalogue (`CATALOGUE-TUTORIELS.md`) donne l'URL S3 de chaque tutoriel.
Attention : **l'URL ne se déduit pas du slug** (`creer-son-compte` →
`foodeatup-inscription-tuto-v1`). L'inventaire résolu est dans
`sources-video.json`.

Sur les 75 vidéos dont les 9 films ont besoin :

| | Nombre | Suite |
|---|---|---|
| ✅ Téléchargeables directement depuis S3 | **67** | rien à faire — je les récupère et j'y prélève les séquences |
| 🔒 Accès refusé (403) | **2** | à rendre lisibles, voir ci-dessous |
| ⬜ Aucune vidéo (module Caisse POS + 5 sujets neufs) | **6** | tournage prévu en dernier |

### 3.1 — Les 2 vidéos à débloquer

Ces deux fichiers sont référencés dans le catalogue mais renvoient `403` sur
S3. Ce sont les deux seules dont j'ai besoin et que je ne peux pas atteindre.

| Slug | Fichier S3 | Sert aux plans |
|---|---|---|
| `mes-commandes-tous-canaux` | `foodeatup-mes-commandes-tuto-v1` | **C2 — convergence multi-canal** (plan clé), S2 multi-canal salle |
| `retrouver-ses-reservations-du-jour` | `foodeatup-reservations-jour-tuto` | **S1 — réservations du jour** (plan clé), S3 reprise du soir |

Deux façons de les obtenir, au choix :
1. rendre ces deux objets publics dans le bucket, comme les 67 autres ;
2. les déposer dans le Drive — je les importerai via RapidoCMS.

C'est tout ce dont j'ai besoin côté captures. **Pas 22 vidéos : 2.**

### 3.2 — Les 6 vidéos qui n'existent pas encore

À tourner plus tard, dans cet ordre de priorité. Les cinq premières sont du
module Caisse POS ; la dernière est un sujet neuf.

| Fichier attendu | Sujet | Débloque |
|---|---|---|
| `cloturer-sa-caisse-v1.mp4` | Le ticket Z | S3 (plan clé), salle 14h30 et 22h30 |
| `ouvrir-son-fond-de-caisse-v1.mp4` | Fond de caisse | cuisine 12h00, salle 11h45 |
| `encaisser-une-commande-v1.mp4` | Encaissement comptoir | salle 12h10 |
| `separer-une-addition-v1.mp4` | Multi-paiement | salle 13h30 |
| `appliquer-une-remise-v1.mp4` | Remise et avoirs | salle 13h40 |
| `suivre-les-ecarts-de-caisse-v1.mp4` | Écarts de caisse | salle 14h40 |

Cinq autres étapes du parcours n'ont aucune fiche et restent en
« bientôt disponible » : mise en place (cuisine 07h40), production → caisse
(cuisine 11h05), plat en rupture (cuisine 13h30), plat indisponible
multi-canal (salle 11h00), validation de congé (direction 10h50).

---

## 4. Ce que je fournis, ce que Michael fournit

**Moi** — les 42 images d'ambiance (RapidoCMS, jamais d'interface), les 9
pistes voix off (ElevenLabs, une voix par métier), le prélèvement des 66
séquences dans les vidéos existantes, le pipeline Remotion, les pages Academy.

**Michael** — les 2 vidéos à débloquer (§3.1), les 6 tournages de caisse
(§3.2), et l'arbitrage sur les chiffres si les voix off doivent citer des
données réelles plutôt que des exemples.

---

## 5. Grammaire des 9 films (rappel v2/v3)

Ligne de temps bleue `#1E9BF0` en bas de cadre, jamais interrompue, même sur
les coupes. Liseré métier en haut : cuisine `#059669`, salle `#F59E0B`,
direction `#475569`. Écrans logiciel incrustés dans un cadre de tablette
incliné 6°, action démarrant 250 ms après l'apparition du cadre. Coches
orange `#FFA500` en trim path 200 ms, accumulées en colonne à droite.
Sous-titres burn-in au-dessus de la ligne de temps, 42 caractères, 2 lignes.
Musique en ré mineur sur les neuf : avant 90 BPM montant, pendant 124 BPM
tendu, après 76 BPM descendant. Ducking −9 dB, normalisation −14 LUFS.

**Palette des films** : `#1E9BF0` `#1B2A41` `#F7F9FC` `#FFA500` + les trois
couleurs métier. À ne pas confondre avec la palette du site Academy
(`#FCF9E6` `#0F1A23` `#007BFF` `#FFA500`).

---

## 6. Le volet « Sans FoodEatUp »

Neuf films miroir, un par film « avec », et un mode « sans » sur les trois
pages de parcours. Le raisonnement : une journée « avec », seule, donne
l'impression que le logiciel réclame 46 gestes par jour. Le miroir montre que
ces gestes existent de toute façon — répartis dans sept outils qui ne se
parlent pas, saisis deux fois, et souvent abandonnés.

### 6.1 ⚠️ Contrainte juridique — à lire avant d'écrire une seule ligne

**Aucun concurrent ne doit être identifiable, ni explicitement ni
implicitement.** En droit français (art. L122-1 et L122-2 du Code de la
consommation), il suffit que le spectateur puisse reconnaître un acteur pour
que le film bascule en publicité comparative. Le registre de ces films étant
l'ironie de situation, un acteur reconnaissable ferait tomber le dénigrement.

Interdits sans exception : logo, marque, nom de produit prononcé ou affiché,
capture d'écran d'un logiciel tiers, palette ou typographie reconnaissable
d'un éditeur, interface reproduisant visuellement un produit du marché, prix
attribué à un acteur identifiable.

Les interfaces « sans » sont des **maquettes neutres fabriquées par nous** :
gris `#8A9099`, typographie système, aucune identité. Elles doivent évoquer
« un logiciel quelconque », jamais un logiciel précis.

Deux garde-fous à écrire :
- `no-competitor-check.ts` — échoue si un nom d'une liste de marques apparaît
  dans un fichier de la série « sans » ou dans les champs `sans.tool` /
  `sans.action` des parcours. Michael fournit la liste.
- **Relecture par un avocat avant toute diffusion.** Ces films seront vus par
  les concurrents ; un seul plan ambigu suffit.

**Le contournement est aussi la meilleure idée du projet : ne pas montrer des
marques, montrer le nombre.** Sept fenêtres, sept identifiants, sept
prélèvements. Le sujet n'est pas « tel logiciel est mauvais », c'est
« vous en avez sept ». Inattaquable, et ça vise tout le marché d'un coup.

### 6.2 Chiffres

Toujours une **fourchette**, jamais une valeur unique — un chiffre unique est
attaquable, une fourchette sourcée ne l'est pas. Référence retenue : un
indépendant correctement équipé se situe entre **5 et 8 abonnements** et
**350 à 900 €/mois**. À revérifier avant diffusion : une publicité
comparative doit être *vérifiable*.

L'argument le plus solide n'est d'ailleurs pas le prix : **aucun de ces outils
ne parle aux autres.** Le stock ignore ce que la caisse a vendu, le planning
ignore les réservations, le HACCP ignore la production. Chaque jonction est
une ressaisie. C'est là que les équipes lâchent.

### 6.3 Grammaire inversée

| | Avec | Sans |
|---|---|---|
| La ligne | une, bleue `#1E9BF0`, continue | **sept lignes grises** brisées, qui ne se touchent jamais |
| Palette | charte pleine | `#8A9099` gris · `#3A3F45` anthracite · `#EDEEF0` blanc froid · `#D64545` alerte |
| Validations | coches orange qui s'accumulent | croix rouges, cases vides, points d'interrogation |
| Compteur | `12 actions tracées` | `7 abonnements · 2 h 14 perdues · 3 saisies en double` |
| Rythme | geste → validation → geste | haché, chaque geste bute sur une friction |
| Son | ré mineur tenu | même tonalité désaccordée d'un quart de ton, sans résolution |

**Le plan obligatoire dans les 9 films** : un écran, sept onglets ouverts, le
curseur qui passe de l'un à l'autre en recopiant un chiffre à la main
(composant `TabChaos`, 1,2 s par aller-retour, 3 minimum).

**Le refrain** — une phrase sur l'abandon des outils, à 20 % de la durée, dans
les neuf films. Ex. : « Je paie sept abonnements. Mon équipe en utilise deux. »

**Le carton final**, identique sur les neuf, seul moment où la charte
réapparaît : fond marine `#1B2A41`, « Avec FoodEatUp, une seule application. »
puis 800 ms plus tard « Et si c'est encore trop, vous parlez à Jarvis. » La
musique « avec » reprend alors sur sa tonique — **la résolution musicale est
l'argument**.

### 6.4 Le bouton bascule — une page, deux états

Pas deux pages : le même parcours, la même heure, les mêmes blocs, avec un
interrupteur. L'utilisateur fait la comparaison lui-même.

Bascule en cascade sur 800 ms, jamais simultanée : la ligne se brise (0 ms) →
la couleur se retire (100 ms) → le contenu se substitue sur place, l'heure et
l'intertitre ne bougeant pas (200 ms) → les compteurs montent (400 ms).

Décisions structurantes :
- **Les deux versions restent dans le DOM**, l'inactive en `visibility:hidden`
  + `aria-hidden` + `inert`. Un rendu conditionnel ferait perdre le SEO du
  texte « sans », qui capte justement les requêtes-problème.
- État dans l'URL (`?mode=sans`), canonical toujours vers la version « avec ».
- `prefers-reduced-motion` → crossfade unique de 150 ms. Non négociable.
- Pas de `filter: grayscale` global (ça salit les vignettes) : on anime les
  variables CSS.
- Pas de librairie d'animation : transitions CSS + interpolation de path en
  `requestAnimationFrame`.
- **Une étape « sans » n'est cliquable nulle part.** Le mode « sans » est un
  cul-de-sac, le mode « avec » ouvre sur 149 vidéos. L'asymétrie est un
  argument.

### 6.5 Ordre d'exécution retenu

1. **Le mode « sans » textuel et le bouton bascule, sans aucune vidéo.**
   Trois pages, deux états, la ligne brisée. C'est déjà 80 % de l'effet.
2. **Les 6 vidéos de caisse** — le parcours salle est troué en son milieu,
   au moment exact du ticket Z. Plus urgent que neuf nouveaux films.
3. **Un seul film « sans » : D1′** — sept onglets, sept identifiants, sept
   prélèvements. Le plus facile à tourner, le plus universel. Pilote.
4. **La série complète**, si D1′ tient.

### 6.6 Faiblesses identifiées à traiter

- **La journée est trop longue pour un premier contact** (46 étapes en
  cuisine). Les films doivent rester *au-dessus* du parcours, jamais noyés
  dedans — ne pas céder à la tentation de mettre la liste en premier.
- **Le parcours salle est troué au pire endroit** : six vidéos de caisse
  manquantes, dont le ticket Z, exactement là où le prospect pense à ses
  obligations légales.
- **Le parcours prouve que le produit est complet, pas qu'il est simple.**
  C'est précisément ce que le volet « sans » corrige.
