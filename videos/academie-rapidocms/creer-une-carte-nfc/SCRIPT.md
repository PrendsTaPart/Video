# Tutoriel 15 — Choisir un modèle de carte NFC dans la galerie de l'Éditeur

**Module** : Éditeur · **Slug** : `creer-une-carte-nfc`
**Capture source** : `_sources/TEMPLATE_DE_CARTE_NFC.mp4` — 69,5 s. La voix
d'origine est supprimée et remplacée par la voix off ci-dessous ; la bande de
sous-titres incrustés est retirée au montage.

**Promesse** : à la fin de cette vidéo, vous savez trier la galerie de cartes
NFC, distinguer les deux formats proposés, et ouvrir le modèle de votre réseau
dans l'éditeur de personnalisation.

---

## Ce que montre réellement la capture

La galerie « Proposition de thème de Cartes NFC pour vous » avec six modèles
Instagram, Facebook et FoodEatUp, le panneau de tri ouvert puis refermé, la
fenêtre de fiche du modèle « Carte NFC Instagram », puis ce modèle ouvert dans
l'éditeur de personnalisation.

Deux limites que le script assume au lieu de les masquer :

- **la technologie NFC n'est jamais expliquée** — rien à l'écran ne montre
  comment associer le visuel à une puce ;
- **le QR code n'est jamais configuré** — on ne voit nulle part où saisir le
  lien qu'il doit pointer.

La ligne N12 le dit explicitement : à cet écran, on dessine le visuel, le reste
se règle ailleurs. Aucune saisie de texte, aucun changement de couleur, aucun
envoi de logo n'est effectué dans la capture, et rien n'est enregistré.

Le tri est ouvert puis refermé **sans être appliqué** : la ligne N4 le dit tel
quel plutôt que de laisser croire à un filtrage.

Plages non montées : 8 → 24 s (écran figé), 28 → 40 s (défilement lent),
44 → 48 s (fenêtre immobile), 60 s (image sans action). Les extraits utilisés
vont de 0 à 8 s, 24 à 28 s, et 40 à 68 s.

Le libellé fautif de l'interface (« Editeur-Personalisation ») est dit
correctement dans la voix off, sans être souligné.

---

## Voix off

Cadence 150 mots par minute. Une ligne = un plan ; chaque plan dure exactement
la durée de sa ligne.

| # | Chapitre | Source | Texte |
|---|---|---|---|
| N1 | **1 · La galerie NFC** | 0,0 → 4,0 | Un client vous suit sur Instagram d'un simple geste, sans taper votre nom. Ça commence par un visuel de carte NFC, déjà dessiné. |
| N2 | | 0,5 → 4,0 | Menu de gauche, section Éditeur, « Templates ». La galerie affiche « Proposition de thème de Cartes NFC pour vous ». |
| N3 | **2 · Trier la galerie** | 4,0 → 8,0 | Le bouton « Filtre : Tout » ouvre un panneau de tri : par date croissante ou décroissante, de A à Z, de Z à A, puis « Appliquer ». |
| N4 | | 4,5 → 8,0 | Ici, ce tri est ouvert puis refermé sans être appliqué : la grille reste exactement dans son ordre d'origine. |
| N5 | **3 · Le catalogue par usage** | 24,0 → 28,0 | Six modèles, deux formats : les « Support NFC », en grand, et les « Carte NFC », au format poche. Instagram, Facebook, FoodEatUp. |
| N6 | | 40,0 → 44,0 | Sous la vignette « Carte NFC Instagram », le bouton « Choisir ce modèle » devient bleu plein dès que vous le survolez. |
| N7 | **4 · La fiche du modèle** | 48,0 → 52,0 | La fenêtre « Acheter un template » affiche le badge vert « Gratuit », le nom du modèle, sa description et ses mots-clés sous « Tag ». |
| N8 | | 48,5 → 52,0 | En bas à droite, « Utiliser ce template » ouvre le modèle dans l'éditeur de personnalisation. |
| N9 | **5 · Personnaliser la carte** | 52,0 → 56,0 | Le voilà : dégradé rose, logo Instagram, pictogramme NFC, le titre « Suivez-nous », l'identifiant du compte, et le grand QR code. |
| N10 | | 56,0 → 60,0 | Cliquez sur le logo : cadre bleu, étiquette « Image ». Texte, image ou conteneur, chaque élément se sélectionne de la même façon. |
| N11 | | 64,0 → 68,0 | À droite, la bibliothèque de blocs : QR code, Cartes, et les blocs de base — citation, section de texte, texte, image. |
| N12 | | 52,5 → 56,0 | À cet écran, vous dessinez le visuel. Le lien du QR code et l'encodage de la puce NFC, eux, se règlent ailleurs, plus tard. |
| N13 | **6 · La Version Minute** | *carte* | Et si vous n'aviez pas à parcourir la galerie pour savoir quel modèle NFC existe déjà ? |
| N14 | | *carte* | Dans Claude, l'outil `list_card_templates` du MCP RapidoCMS vous les liste, et `assign_card_template` applique celui que vous voulez. |
| N15 | **7 · L'astuce** | 24,0 → 28,0 | L'astuce : choisissez le format avant le réseau. Un « Support NFC » se pose sur un comptoir, une « Carte NFC » se glisse dans une poche. |
| FIN | *outro* | — | Retenez ceci : le modèle fait le visuel, pas la puce. Dans la prochaine vidéo, on crée une carte digitale. |

## Chapitres prévisionnels

| Timecode | Chapitre |
|---|---|
| 00:00 | Ouverture |
| 00:04 | 1 · La galerie NFC |
| 00:17 | 2 · Trier la galerie |
| 00:31 | 3 · Le catalogue par usage |
| 00:44 | 4 · La fiche du modèle |
| 00:56 | 5 · Personnaliser la carte |
| 01:22 | 6 · La Version Minute |
| 01:34 | 7 · L'astuce |

*(Les timecodes définitifs sont recalculés par le montage, à partir de la durée
réelle de chaque ligne de voix off.)*

## Astuce retenue pour la fiche

Choisir le format avant le réseau : un « Support NFC » se pose sur un comptoir,
une « Carte NFC » se glisse dans une poche. Le réseau, lui, se change en
remplaçant le logo dans l'éditeur.

## Cas d'usage

- Un restaurant veut un support à poser en caisse pour gagner des abonnés.
- Un commerçant distribue des cartes au format poche lors d'un salon.
- Une marque décline le même visuel pour Instagram et pour Facebook.
