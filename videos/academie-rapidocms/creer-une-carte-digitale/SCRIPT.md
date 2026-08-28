# Tutoriel 16 — La page Carte digitale : quota, liste et formulaire d'ajout

**Module** : Éditeur · **Slug** : `creer-une-carte-digitale`
**Capture source** : `_sources/cartedigital_CMS.mp4` — 53,8 s. La voix
d'origine est supprimée et remplacée par la voix off ci-dessous ; la bande de
sous-titres incrustés est retirée au montage.

**Promesse** : à la fin de cette vidéo, vous savez lire votre quota de cartes
digitales, comprendre l'anneau des statistiques, et ouvrir le formulaire
d'ajout en sachant ce qu'il attend de vous.

---

## Ce que montre réellement la capture

La page « Carte digitale » d'un compte de démonstration **entièrement vide** :
quota de dix cartes, anneau des statistiques tout vert, et « Liste des cartes »
affichant « Il n'y a actuellement aucune donnée à afficher ». Puis la fenêtre
« Ajouter une carte » et ses six champs.

Trois limites que le script assume :

- **aucun champ n'est rempli** — le formulaire reste vide du début à la fin ;
  la ligne N10 le dit franchement ;
- **le bouton « Ajouter » n'est jamais cliqué** — la capture s'arrête sur son
  survol ; la ligne N11 décrit donc ce que le bouton fera, au futur ;
- **aucune carte existante n'est visible** — ce que la liste et l'anneau
  afficheront une fois remplis est annoncé au futur, jamais montré.

Plages non montées : 0 → 24 s (six images strictement identiques, écran figé),
36 → 44 s (même formulaire vide), et la fin figée après 50 s. Les extraits
utilisés vont de 24 à 36 s, et de 45 à 50 s.

Les libellés fautifs de l'interface (« Carte digital », « Nombre maximale
autorisée », « Aucune données est disponible ») sont dits correctement dans la
voix off, sans être soulignés.

---

## Voix off

Cadence 150 mots par minute. Une ligne = un plan ; chaque plan dure exactement
la durée de sa ligne.

| # | Chapitre | Source | Texte |
|---|---|---|---|
| N1 | **1 · La page Carte digitale** | 24,0 → 27,0 | Une carte de visite qui ne s'imprime pas, qui se partage en une seconde et se corrige à tout moment : la carte digitale. |
| N2 | | 24,5 → 27,5 | Menu de gauche, section Éditeur : l'entrée « Carte digitale » ouvre la page qui recense toutes vos cartes. |
| N3 | **2 · Vos statistiques** | 25,0 → 28,0 | En haut, la section « Statistiques ». À gauche, votre quota : sur ce compte, dix cartes digitales autorisées, pas une de plus. |
| N4 | | 24,0 → 27,0 | Au centre, un anneau partage les cartes créées et les cartes restantes. Ici il est entièrement vert : aucune carte n'existe encore. |
| N5 | **3 · La liste des cartes** | 24,5 → 27,5 | Plus bas, la « Liste des cartes ». Vide pour l'instant, elle affichera chaque carte enregistrée dès que vous en créerez une. |
| N6 | **4 · Créer une carte** | 28,0 → 31,5 | En haut à droite, un seul bouton d'action : « Créer une carte ». Il passe en bleu plein au survol. |
| N7 | | 29,0 → 32,0 | Le champ « Chercher », à gauche, ne servira que le jour où cette liste comptera plusieurs cartes. |
| N8 | **5 · Le formulaire** | 32,0 → 35,5 | La fenêtre « Ajouter une carte » s'ouvre. Six champs : le nom de la carte, puis le nom et le prénom du propriétaire. |
| N9 | | 33,0 → 36,0 | Ensuite l'adresse e-mail, le numéro de téléphone, et une zone libre pour les informations supplémentaires que vous voulez inclure. |
| N10 | | 45,0 → 48,5 | À l'écran, le formulaire reste vide : la démonstration ne remplit rien. Chez vous, c'est à ce moment que vous saisissez vos données. |
| N11 | | 46,5 → 50,0 | Le bouton bleu « Ajouter », en bas, enregistre la carte. Elle rejoint alors la liste, et l'anneau des statistiques change de couleur. |
| N12 | **6 · La Version Minute** | *carte* | Six champs à taper et une fenêtre à ouvrir : c'est exactement le genre de chose qu'une seule phrase remplace. |
| N13 | | *carte* | Dans Claude, l'outil `add_digital_card` du MCP RapidoCMS crée la carte, et `add_card_page_link` y accroche vos liens. |
| N14 | **7 · L'astuce** | 28,0 → 31,5 | L'astuce : nommez vos cartes par usage, « Accueil », « Salon », « Terrain », plutôt que par personne. Avec dix cartes au maximum, vous saurez laquelle rééditer. |
| FIN | *outro* | — | Retenez ceci : dix cartes, une liste, un formulaire. Vous avez fait le tour du module Éditeur — la suite de l'Académie RapidoCMS vous attend. |

## Chapitres prévisionnels

| Timecode | Chapitre |
|---|---|
| 00:00 | Ouverture |
| 00:04 | 1 · La page Carte digitale |
| 00:16 | 2 · Vos statistiques |
| 00:29 | 3 · La liste des cartes |
| 00:35 | 4 · Créer une carte |
| 00:46 | 5 · Le formulaire |
| 01:12 | 6 · La Version Minute |
| 01:24 | 7 · L'astuce |

*(Les timecodes définitifs sont recalculés par le montage, à partir de la durée
réelle de chaque ligne de voix off.)*

## Astuce retenue pour la fiche

Nommer les cartes par usage — « Accueil », « Salon », « Terrain » — plutôt que
par personne : avec un quota de dix cartes, on retrouve immédiatement celle
qu'il faut rééditer.

## Cas d'usage

- Un gérant crée une carte digitale par point de contact plutôt qu'une par
  salarié, pour rester dans son quota.
- Une équipe commerciale doit corriger un numéro de téléphone sans réimprimer
  quoi que ce soit.
- Une entreprise veut suivre combien de cartes il lui reste sur son abonnement.
