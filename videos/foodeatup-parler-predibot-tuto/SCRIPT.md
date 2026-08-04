# Tutoriel — Parler à PrediBot, votre agent RH

Module **PrediBot (Agent IA Directeur)**, 3e et dernière vidéo du module
(`predire-ses-commandes`, `marketplace-de-prompts`, puis celle-ci). Rush fourni par
Michael : conversation WhatsApp avec **Predibot** (53,76 s, 1526×1032, capture fenêtre
desktop WhatsApp). Intro/outro fournies telles quelles (`assets/intro.jpg` = carte
"AGENT GESTION RH", `assets/outro.jpg` = CTA standard réutilisé).

Contrairement aux tutoriels "screen recording produit" habituels, il n'y a ici aucun
clic à zoomer : le rush est une suite d'échanges WhatsApp (question envoyée en bulle
verte, réponse Predibot en bulle blanche avec les données FoodEatUp). Traitement retenu
donc : segments "lecture" (scroll de la conversation) avec `setpts` pour resserrer le
rythme, bandeau d'étape par segment, pas de `punch_highlight`.

## Ce que montre le rush (6 commandes RH, dans l'ordre)

1. `Liste mes employés` → liste des employés (poste, email, téléphone, statut) —
   correspond à `list_employees`.
2. `Liste les congés` → demandes de congé en attente (type, dates, durée) —
   `list_leaves`.
3. `Approuve le congé 995` → "Congé #995 approuvé avec succès !" — `approve_leave`.
4. `Rejette le congé 1023 en raison de test` → "Congé #1023 rejeté avec succès !" —
   `reject_leave`.
5. `Vérifie les pointages du 01/01/2026 au 30/01/2026` → historique de pointage —
   `list_attendances`.
6. `Classement des employés` → classement par score (heures, retards, congés) —
   fonctionnalité d'analyse Predibot au-dessus des données RH (pas d'outil MCP dédié
   à ce classement précis).

Le tout premier échange du rush (validation d'une commande fournisseur, StockVisionAI)
n'est **pas RH** — volontairement coupé au montage pour rester focalisé sur la
gestion d'équipe, cohérent avec la carte d'intro fournie.

## Voix off (8 lignes, Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Ancrage |
|---|---|---|
| N1 | Gérer votre équipe sans ouvrir une seule page ? Posez la question à Predibot, votre agent RH, sur WhatsApp. | Seg A — Liste employés |
| N2 | Demandez la liste de vos employés, ou celle des congés en attente, avec les dates et la durée. | Seg B — Liste congés |
| N3 | Approuvez un congé en une phrase... | Seg C — Approuve 995 |
| N4 | ...ou refusez-le en précisant le motif, en quelques secondes. | Seg D — Rejette 1023 |
| N5 | Contrôlez les pointages sur la période de votre choix... | Seg E — Pointages |
| N6 | ...et laissez Predibot classer vos employés par performance. | Seg F — Classement |
| N7 | Toute votre gestion RH, pilotée à la voix, où que vous soyez. | Bénéfice, avant séquence Claude |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | Carte de fin (CTA) |

## Séquence "cas d'usage avec Claude" (avant la carte de fin)

Correspond à un outil MCP FoodEatUp direct → séquence animée en 3 temps ajoutée
(module partagé `videos/_shared/claude_prompt_sequence.py`), prompt basé sur
`approve_leave` (l'action la plus proche de ce que montre le rush) :

```
Approuve le congé n°[id congé] de [nom employé], commentaire : "[motif]".
```

Réponse assistant simulée : confirmation de l'approbation + rappel que Claude peut
aussi lister les employés/congés ou refuser une demande avec `reject_leave`.

## Découpage (source rush, secondes)

| Seg | Source | Cible | Contenu |
|---|---:|---:|---|
| intro | carte | 2,2 s | AGENT GESTION RH |
| A | 6.0 → 17.0 | ~5,5 s | Liste des employés (scroll) |
| B | 21.0 → 29.0 | ~4,5 s | Liste des congés en attente |
| C | 29.0 → 33.5 | ~4,0 s | Approuve congé 995 + confirmation |
| D | 33.5 → 39.5 | ~4,5 s | Rejette congé 1023 + confirmation |
| E | 39.5 → 44.5 | ~4,0 s | Vérifie les pointages |
| F | 44.5 → 53.76 | ~5,0 s | Classement des employés |
| claude | généré | ~6 s | Séquence 3 temps (prompt Claude) |
| outro | carte | ajustée à la VO | CTA |

Durées cibles calibrées sur la durée réelle des lignes VO générées (voir `build.py`),
pas l'inverse.

## Statut

Montage + publication demandés explicitement par Michael en une seule passe (pas de
STOP intermédiaire cette fois) : montage → Lovable (module `predibot`, remplit le 3e
et dernier slot du module) → dépôt GitHub.
