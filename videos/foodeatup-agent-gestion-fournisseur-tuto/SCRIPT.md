# Tutoriel — Agent Gestion Fournisseur (Predibot) FoodEatUp

Intrants fournis par Michael : carte d'ouverture `Agent_gestion_fournisseur.jpg`, carte de
fin (CTA générique, réutilisée telle quelle — identique octet pour octet à `outro.jpg` des
tutos précédents), rush `agent_gestion_fournisseur.mp4`.

Rush : **26,32 s**, H.264 1526x1032, AAC 48 kHz stéréo, 25 fps.

## Ce que montre le rush

Conversation avec **Predibot**, l'agent IA FoodEatUp joignable depuis WhatsApp (déjà
identifié au catalogue comme module 11b, `predibot`) :

1. (Historique déjà visible en haut, hors script — l'agent vient de créer une recette et
   d'enregistrer une température HACCP : preuve que Predibot ne fait pas que les
   fournisseurs, réutilisé en astuce du chef ci-dessous.)
2. L'utilisateur écrit **« Liste mes commandes »** → Predibot renvoie les **8 dernières
   commandes fournisseurs (sur 58 au total)** : n° de commande, fournisseur, date prévue,
   statut (conforme / en attente), avec les noms de fournisseurs réels (louay, Les Jardins
   Gourmets, soulayma, Fournisseur1…).
3. L'utilisateur écrit **« Valide la commande 2886, conforme, Produits laitiers, RAS »**
   (validation d'une réception en langage naturel, en une phrase).
4. Predibot répond **« Commande 2886 validée avec succès »** avec un lien vers la fiche de
   réception HACCP.
5. Bascule navigateur : la fiche de réception **CMD-2026052415…** est déjà à jour dans
   FoodEatUp (fournisseur *louay*, date prévue/effective, quantité commandée/reçue 12 kg) —
   preuve que la validation par chat écrit bien dans l'application.

## Outil MCP correspondant

`mcp__FoodEatUp__create_haccp_reception(establishment_id, date_controle, heure_controle,
etat_livraison, fournisseur_nom, reference_bl, commentaires, validate)` couvre exactement
l'action montrée (validation d'une réception avec état + commentaire). `list_deliveries`
couvre la consultation ("Liste mes commandes") qui précède.

> Valide la réception de la commande [référence BL], fournisseur [nom du fournisseur],
> état [conforme/non conforme], avec le commentaire [RAS ou détail], pour mon établissement
> FoodEatUp (ID [ID établissement]).

## Voix off (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Gérer vos commandes fournisseurs sans ouvrir FoodEatUp ? C'est le travail de l'agent. | carte d'intro |
| N1 | Depuis WhatsApp, demandez simplement la liste de vos commandes fournisseurs. | "Liste mes commandes" envoyé |
| N2 | L'agent affiche vos dernières commandes : fournisseur, date et statut. | liste des 8 commandes |
| N3 | Validez une réception en une phrase : conforme, produit, remarque. | message de validation envoyé |
| N4 | En quelques secondes, la commande est validée et tracée. | réponse "validée avec succès" |
| N5 | La fiche de réception est déjà à jour dans FoodEatUp : fournisseur, quantités, tout y est. | page navigateur, fiche réception |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | **étage 1+2** (réutilisé) |
| N7 | Collez-le dans la conversation : votre réception fournisseur est validée en quelques secondes. | **étage 3** |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA, réutilisé tel quel) |

N6 et N8 seront réutilisés tels quels depuis un tuto précédent (même voix, texte
générique) — zéro crédit ElevenLabs sur ces deux lignes. N0, N1, N2, N3, N4, N5, N7 sont
propres à cette vidéo et seront générés.

## Astuce du chef (chefTip, à la demande explicite du demandeur)

Ce même agent Predibot (visible en haut de la conversation, non narré pour rester focalisé
sur les fournisseurs) vient aussi de créer une fiche recette et d'enregistrer une
température HACCP dans le même fil de discussion : **un seul agent WhatsApp couvre vos
fournisseurs, vos recettes et votre HACCP**, sans changer d'écran ni ouvrir l'application.

## Découpage prévisionnel (à affiner une fois les VO mesurées)

| Seg | Source | Contenu |
|---|---|---|
| intro | carte | AGENT GESTION FOURNISSEUR |
| A | ~13.0 → 16.5 | "Liste mes commandes" → liste des 8 commandes |
| B | ~17.0 → 19.5 | saisie + envoi "Valide la commande 2886, conforme, Produits laitiers, RAS" |
| C | ~19.5 → 23.0 | réponse "Commande 2886 validée avec succès" |
| D | ~23.0 → 26.3 | bascule navigateur, fiche de réception à jour |
| claude1/2/3 | cartes générées | séquence "Utilisez cette fonctionnalité avec Claude" |
| outro | carte | CTA |

Les 0-13s du rush (historique recette + température, avant "Liste mes commandes") ne sont
pas repris à l'image pour rester centré sur le sujet fournisseurs annoncé par la carte
d'intro — seule l'astuce du chef en fait mention.

## Statut

**Script validé par Michael le 2026-08-04.** VO générée (ElevenLabs, voix Adam FR ;
N6/N8 réutilisés tels quels depuis `foodeatup-fournisseurs-tuto/vo/`, zéro crédit dépensé
dessus). Montage terminé : **41,96 s**, H.264 High/yuv420p 1526x1032, AAC 48 kHz stéréo,
faststart (moov avant mdat confirmé), decode 0 erreur, peak audio **-7,16 dBFS** (pas de
saturation). Vignette YouTube livrée telle quelle depuis `assets/intro.jpg` (aucun
redesign), redimensionnée en 1280x720 neutre : `out/thumbnail-youtube.jpg`.

**Validée par Michael le 2026-08-04, publiée sur Lovable le 2026-08-04.** Catégorisation
retenue : module `comptabilite`, nouvelle sous-catégorie "11 · Agent Fournisseurs
(WhatsApp)" — le module `predibot` était déjà complet (3/3, dont un tutoriel WhatsApp
existant sur un autre sujet RH, `parler-a-predibot-avec-nos-prompts`) ; le module `haccp`
avait déjà le même principe de sous-catégorie bonus pour son propre agent WhatsApp
(`agent-haccp-whatsapp`, sous-catégorie "31"), repris ici à l'identique côté `comptabilite`
pour rester cohérent avec ce précédent. Entrée Lovable : `src/data/tutorials.ts`, slug
`agent-gestion-fournisseur-whatsapp`, commit `8784264`.

**RapidoCMS non fait** : le serveur MCP RapidoCMS n'était pas connecté à cette session (pas
dans la liste d'outils disponibles). `videoUrl`/`thumbnailUrl` sur Lovable pointent donc
temporairement vers les URLs GitHub raw de cette branche
(`claude/foodeatup-video-tutorial-2z3kid`) — même solution de repli déjà utilisée par
d'autres tutoriels de la série le temps que RapidoCMS soit accessible (voir
`LOVABLE-FOODEATUP-DOCS.md`, plusieurs entrées "RapidoCMS/LinkedIn en attente (URLs GitHub
raw temporaires)"). À refaire proprement (upload S3 RapidoCMS + mise à jour des deux champs
Lovable) dès que l'outil est disponible dans une session. LinkedIn non demandé.
