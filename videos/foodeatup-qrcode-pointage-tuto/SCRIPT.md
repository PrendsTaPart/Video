# Tutoriel — Générer le QR code de pointage FoodEatUp

Module Équipe & Planning, dossier Drive « 8-Configuration et suppression et
génération du QR code par boutique pour le pointage et la connexion au
logiciel de l'employé ». Durée livrée : **41,36 s** — H.264 High/yuv420p, AAC
48 kHz stéréo, faststart. Audio : true peak **-7,27 dBFS**. Sans avatar
HeyGen, **sans séquence Claude** : aucun outil MCP ne couvre cette
configuration anti-fraude (sécurité/géolocalisation/PIN/badge) — cohérent
avec `creer-son-compte`, `choisir-son-abonnement`, `regler-ses-unites`.

## Voix off (7 lignes)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N1 | Configurez le niveau de sécurité et la géolocalisation, puis générez votre QR code de pointage. | 5,43 s | A1 + clic A2 |
| N2 | Affichez ce QR code au restaurant : vos employés le scannent avec leur téléphone pour pointer automatiquement. | 5,85 s | B |
| N3 | Retrouvez tous vos QR codes dans l'historique : téléchargez, désactivez ou supprimez-les à tout moment. | 5,93 s | C |
| N4 | Ajustez le rayon de géolocalisation, la tolérance hors-zone, et gérez le PIN ou le badge de chaque employé. | 6,27 s | D |
| N5 | En scannant, l'employé retrouve directement son espace pour pointer en un clic. | 4,08 s | E |
| N6 | Un pointage fiable et anti-fraude, sans matériel supplémentaire à acheter. | 4,13 s | F |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (réutilisée) |

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,50 s | GÉNÉRER LE QR CODE DE POINTAGE |
| A1 | 0,00 → 5,20 | 4,40 s | Config « Pointage anti-fraude » : niveau de sécurité, latitude/longitude |
| A2 | 5,20 → 6,00 | 1,60 s | **zoom-punch** sur « + Générer QR Code » (949, 360) |
| B | 7,00 → 13,00 | 6,40 s | QR code actif, URL de connexion, étapes d'usage, actions rapides |
| C | 24,00 → 30,00 | 6,50 s | Historique des QR codes (activer/télécharger/supprimer) |
| D | 30,00 → 36,00 | 6,80 s | Configuration avancée (rayon, tolérance hors-zone) + accès employés (PIN/badge) + badges NFC |
| E | 50,00 → 55,00 | 4,60 s | Test réel : URL du QR ouverte dans un navigateur |
| F | 55,00 → 57,28 | 4,60 s | Écran employé « Qui êtes-vous ? » (sélection de profil pour pointer) |
| outro | carte | 6,20 s | CTA |

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade
(0,28 s), bandeaux d'étape (module `banner()` corrigé — slide-in seul),
encadré orange pulsant sur le clic Générer QR Code.

## Statut publication

Vidéo à livrer à Michael pour validation avant publication RapidoCMS/
LinkedIn/Lovable. RapidoCMS non autorisé dans cette session — publication
CMS/LinkedIn en attente dans tous les cas.
