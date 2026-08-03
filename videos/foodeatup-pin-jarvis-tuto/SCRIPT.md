# Tutoriel — Créer son code PIN, accès & Jarvis FoodEatUp

Troisième vidéo du module `equipe-planning` (Drive : dossier "CRÉER SON CODE PIN
ACCÈS & JARVIS"). Durée livrée : **23,3 s** — H.264 High/yuv420p, AAC 48 kHz stéréo,
faststart. Audio : true peak **-7,3 dBFS**. Decode 0 erreur, moov avant mdat.

## Ce que montre le rush (et le contexte donné par Michael)

Le rush (29,4 s, 1920x828) montre : le QR code permanent de l'établissement (page
"qr code actif") → section "Accès des employés" (3 employés, statut PIN
défini/absent par ligne) → clic "Définir un PIN" pour Alice Charbit → saisie d'un
code à 4-6 chiffres → clic "Enregistrer" → toast "PIN défini pour alice Charbit".

Le rush ne montre pas à l'écran, mais Michael l'a précisé par message (repris dans
`whatItsFor`/`chefTip`, même principe que les tutos fournisseurs/produits/tâches) :
- le **QR code** sert à **appairer une oreillette Bluetooth à Jarvis** (scan une
  fois, appairage fait) ;
- le **code PIN**, lui, sert à deux choses : **pointer l'équipe** (badgeuse/borne de
  pointage) et **se connecter au logiciel**, avec un accès scopé au **rôle et aux
  permissions** de l'employé (cf. tutoriel `ajouter-ses-employes`, où le rôle est
  choisi à la création).

## Pas de séquence Claude

Aucun outil MCP FoodEatUp ne couvre la définition d'un code PIN employé (feature de
sécurité/accès, pas une donnée métier exposée par le serveur MCP) — même situation
que `creer-son-compte`, `monter-sa-boutique` ou `regler-ses-unites` dans le reste de
la série. Pas de `claudePrompt`/`claudePrompts` sur cette fiche.

## Voix off (7 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Créer un code PIN pour vos employés. | 1,91 s | intro |
| N1 | Ce QR code sert à appairer une oreillette à Jarvis. | 3,00 s | A — QR code Jarvis |
| N2 | Ici, repérez qui a déjà un code PIN. | 2,27 s | B — Accès des employés |
| N3 | Cliquez sur Définir un PIN. | 1,67 s | clic "Définir un PIN" |
| N4 | Entrez quatre à six chiffres, puis Enregistrer. | 2,53 s | D — saisie + clic Enregistrer |
| N5 | Il sert au pointage et à l'accès logiciel, selon le rôle de l'employé. | 4,02 s | F — bénéfice (succès) |
| N6 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé tel quel depuis `foodeatup-produits-tuto`) |

N6 réutilisé tel quel — zéro crédit ElevenLabs dépensé sur cette ligne. Script v1
initialement écrit trop long (25,7s de VO pour ~15s de plan visuel, dérive de VO
jusqu'à 11s) — retravaillé en lignes courtes pour rester au rythme demandé par
Michael sur le tuto précédent.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,60 s | CRÉER SON CODE PIN — ACCÈS & JARVIS |
| A | 0,20 → 8,00 | 4,00 s | QR code permanent, stats, historique |
| B | 8,00 → 9,30 | 1,60 s | "Accès des employés" (3 employés, statuts PIN) |
| C | 9,30 → 9,60 | 0,80 s | **zoom-punch** sur "Définir un PIN" (1494, 198) |
| D | 10,00 → 21,30 | 4,50 s | modale "Code PIN", saisie du code |
| E | 21,30 → 21,60 | 0,80 s | **zoom-punch** sur "Enregistrer" (1021, 521) |
| F | 24,00 → 28,50 | 3,00 s | toast "PIN défini pour alice Charbit" |
| outro | carte | 7,86 s (auto-étendue) | CTA |

Coordonnées de clic mesurées directement sur les frames extraites du rush,
résolution source native 1920x828.

## Statut publication

Montage terminé et checklist de compatibilité passée (H.264 High/yuv420p, AAC 48 kHz
stéréo, faststart, peak -7,3 dBFS, 0 erreur de décodage). **En attente de validation
avant publication** (règle du 2026-08-02, `videos/LOVABLE-FOODEATUP-DOCS.md`) : pas
d'upload RapidoCMS/LinkedIn (RapidoCMS non authentifié dans cette session de toute
façon), pas d'envoi du prompt Lovable tant que la vidéo n'a pas été revue.
