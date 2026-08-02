# Tutoriel — Configurer son profil entreprise

Module 1 « CONFIGURATION », dossier Drive `4 - profil entreprise`.
**Rebuild** : même situation que l'abonnement — une v1 pré-existante avec le bug audio
96kHz mono / pas de faststart et sans animations. Michael a redéposé les mêmes assets ;
refait avec le pipeline actuel.

Durée livrée : **25,5 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart.
Audio : true peak **-7,3 dBFS** (mesuré sur le MP4 final).

## Voix off

| # | Texte | Durée | Placement |
|---|---|---:|---|
| N0 | Modifier le profil de votre entreprise ne prend qu'un instant. | 3,16 s | carte d'intro |
| N1 | Depuis l'onglet Entreprise, cliquez sur Modifier les informations. | 3,29 s | onglet + clic |
| N2 | Mettez à jour le SIRET, le RIB et le statut juridique de votre entreprise. | 4,26 s | modal d'édition |
| N3 | Un clic sur Modifier, et vos changements sont enregistrés. | 3,11 s | clic Modifier |
| N4 | Vos informations sont à jour, prêtes pour vos factures et devis. | 3,47 s | confirmation |
| N5 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA) |

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,6 s | CONFIGURER SON PROFIL ENTREPRISE |
| A | 0,20 → 2,00 | 2,30 s | page « Informations sur l'entreprise » |
| B | 2,00 → 2,50 | 0,90 s | **zoom-punch** sur Modifier les informations (1616, 170) |
| C | 3,00 → 4,50 | 3,00 s | modal ouverte, Nom/SIRET |
| D | 4,50 → 9,50 | 5,00 s | saisie RIB + statut juridique (SARL) |
| E | 9,50 → 9,80 | 0,90 s | **zoom-punch** sur Modifier / enregistrer (1024, 702) |
| F | 10,00 → 14,20 | 3,80 s | toast de confirmation + profil mis à jour |
| outro | carte | 8,84 s (auto-étendue) | CTA |

Rush très court (14,2 s au total) — le plus bref de la série jusqu'ici.

## Point de vigilance — leçon appliquée dès cette passe

Après le dérapage sur `foodeatup-abonnement-tuto` (outro étirée à 22 s faute d'avoir vérifié
les durées VO avant de fixer les segments), cette fois les cibles de segment ont été choisies
**après** avoir généré et mesuré les 6 lignes VO (22,3 s au total), pas avant. Résultat :
extension d'outro limitée à 8,84 s (contre 6,2 s de base), largement dans la norme des autres
vidéos de la série.

## Animations

Mêmes principes que les précédents : Ken Burns sur les cartes, xfade (0,28 s), bandeaux
d'étape, encadré orange pulsant sur les 2 clics. Pas de clip avatar dans ce dossier.

## MCP FoodEatUp — pas de prompt Claude

Vérifié : aucun outil `mcp__FoodEatUp__*` ne couvre la modification du profil de
l'entreprise elle-même (SIRET, RIB, statut juridique) — les outils disponibles opèrent sur
des entités du restaurant (clients, employés, plats...) une fois l'établissement déjà
configuré, pas sur sa propre fiche d'identité. Pas de `claudePrompt` sur ce tutoriel.
