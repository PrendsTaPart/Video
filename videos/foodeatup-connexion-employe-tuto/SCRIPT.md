# Tutoriel — Se connecter côté employé (URL & code PIN) FoodEatUp

Cinquième vidéo du module `equipe-planning` (Drive : "SE CONNECTER CÔTÉ EMPLOYÉ —
URL & CODE PIN"). Durée livrée : **31,6 s** — H.264 High/yuv420p, AAC 48 kHz stéréo,
faststart. Audio : true peak **-6,7 dBFS**. Decode 0 erreur, moov avant mdat.

## Ce que montre le rush

Le rush (26,0 s, 1920x828) montre : la page "qr code actif" (déjà vue dans
`creer-son-code-pin`) → champ "URL DE CONNEXION" → clic "Copier" → **nouvel onglet
navigateur** (simulant le téléphone/la tablette de l'employé) → l'URL est collée
dans la barre d'adresse → page "Qui êtes-vous ?" → clic sur le profil "alice
Charbit" → saisie du code PIN (4 chiffres) → clic "Mon espace" → page "mon espace" :
grille de modules et menu du haut limités au rôle de l'employé (ici manager).

Contrairement au tuto PIN précédent qui montrait la création du code côté
back-office, celui-ci montre le point de vue de l'employé : comment il utilise
cette URL et ce PIN pour se connecter lui-même, sans repasser par un administrateur.

## Pas de séquence Claude

Aucun outil MCP FoodEatUp ne couvre la connexion côté employé (URL/QR + PIN) —
même situation que `creer-son-code-pin` ou `creer-son-compte` dans le reste de la
série. Pas de `claudePrompt`/`claudePrompts` sur cette fiche.

## Voix off (8 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Vos employés peuvent se connecter eux-mêmes, sans passer par vous. | 3,58 s | intro |
| N1 | Copiez l'URL de connexion, juste sous le QR code. | 3,24 s | A — URL de connexion / clic Copier |
| N2 | Ouvrez-la sur le téléphone ou la tablette de l'employé. | 2,87 s | C — nouvel onglet côté employé |
| N3 | Il sélectionne son profil dans la liste. | 1,80 s | D/E — Qui êtes-vous / clic profil |
| N4 | Puis saisit son code PIN personnel, à quatre ou six chiffres. | 3,29 s | F — saisie du code PIN |
| N5 | Il peut pointer ses heures, ou ouvrir Mon espace. | 3,19 s | G — clic Mon espace |
| N6 | Son espace n'affiche que les modules autorisés par son rôle. | 3,11 s | H2 — grille de modules |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé tel quel depuis `foodeatup-produits-tuto`) |

N7 réutilisé tel quel — zéro crédit ElevenLabs dépensé sur cette ligne. Lignes
courtes dès l'écriture initiale (leçon du tuto PIN précédent) : dérive maximale
observée au premier rendu : 0,88 s, aucune cascade.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,20 s | SE CONNECTER CÔTÉ EMPLOYÉ — URL & CODE PIN |
| A | 0,20 → 3,30 | 4,20 s | "qr code actif", champ URL de connexion |
| B | 3,45 → 3,75 | 0,80 s | **zoom-punch** sur "Copier" (1740, 500) |
| C | 5,30 → 6,60 | 2,80 s | nouvel onglet, URL collée dans la barre d'adresse |
| D | 8,40 → 9,40 | 1,80 s | "Qui êtes-vous ?", liste des profils |
| E | 9,40 → 9,80 | 0,80 s | **zoom-punch** sur la carte "alice Charbit" (1175, 715) |
| F | 10,00 → 13,60 | 4,20 s | saisie du code PIN (4 chiffres) |
| G | 14,55 → 14,95 | 0,80 s | **zoom-punch** sur "Mon espace" (1615, 740) |
| H1 | 17,00 → 19,40 | 3,20 s | page "mon espace", en-tête + première rangée |
| H2 | 20,00 → 23,00 | 4,00 s | grille complète des modules autorisés |
| H3 | 24,00 → 25,80 | 2,60 s | retour en haut, menu du haut (même logique de rôle) |
| outro | carte | 6,20 s | CTA |

Coordonnées de clic mesurées directement sur les frames extraites du rush,
résolution source native 1920x828.

## Transitions

`slideleft` sur les 3 vraies coupures de scène (B→C nouvel onglet, C→D navigation
vers la page de connexion, G→H1 nouvelle page `/employee/hub`) ; `fade` partout
ailleurs (continuité de scroll/clic sur le même écran).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'étape, encadré orange pulsant sur les 3 clics ("Copier", carte profil
"alice Charbit", "Mon espace"). Pas de zoom-punch sur la saisie des chiffres du
PIN (frappe continue, pas un bouton isolé) — même logique que la saisie de
formulaire dans les tutos précédents. Pas de clip avatar dans ce dossier.

## Statut publication

Montage terminé et checklist de compatibilité passée (H.264 High/yuv420p, AAC 48 kHz
stéréo, faststart, peak -6,7 dBFS, 0 erreur de décodage). **En attente de validation
avant publication** (règle du 2026-08-02, `videos/LOVABLE-FOODEATUP-DOCS.md`) : pas
d'upload RapidoCMS/LinkedIn (RapidoCMS non authentifié dans cette session de toute
façon), pas d'envoi du prompt Lovable tant que la vidéo n'a pas été revue.
