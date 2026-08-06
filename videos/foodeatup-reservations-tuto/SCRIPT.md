# Tutoriel — Tenir ses Réservations au quotidien FoodEatUp

Catalogue : module **Agent IA Caroline** (`caroline-ia`, catégorie *Agent IA Caroline & Salle*,
`#F59E0B`), vidéo **06/06** — voir `videos/CATALOGUE-157-TUTORIELS.md` ligne 87-91. Premier
tutoriel produit pour ce module (encore vide sur le site). Rush fourni par Michael :
`assets/screen.mp4` (78,29 s, 1920x828, 25 fps, piste audio native silencieuse à -91 dB — VO
entièrement ElevenLabs, pas de clip avatar). Intro/outro fournies telles quelles par Michael
(`assets/intro.jpg` = carte "TENIR SES RÉSERVATIONS AU QUOTIDIEN", `assets/outro.jpg` = carte
CTA générique déjà réutilisée sur la série — md5 identique à `foodeatup-produits-tuto/assets/
outro.jpg` et `foodeatup-reception-ean-dlc-tuto/assets/outro.jpg`, donc **N9 reprend l'audio
existant tel quel**, pas de nouvel appel ElevenLabs pour cette ligne).

## Ce que montre le rush

1. Page **Réservations** : liste du jour, compteurs Total/En attente/Aujourd'hui/À venir
   (0,0 → 2,0 s).
2. Clic **"+ Nouvelle réservation"** → modale : bloc Client (Nom, Téléphone, Email) puis bloc
   Créneau (Date, Heure, Couverts) — saisie "nathan dupont", "+33601020304",
   "nathan@contact.fr", 06/08/2026, 17:47, 4 couverts (2,0 → 23,0 s).
3. Sélection de la **Table** : bascule "Toutes / Salle principale / Terrasse", grille de tables
   avec dispo (Auto, T3, T4, T6, T7, T5, Terrasse 1, T9…), choix explicite de **T9**
   (12 couverts, Salle principale) plutôt que l'auto-assignation (23,0 → 33,5 s).
4. Clic **"Créer la réservation"** → la modale se ferme, la réservation apparaît dans la liste
   ("Nathan dupont", jeu. 06/08 16:47, 4 couverts, table T9, statut **En attente** — Total
   13 → 14, En attente 2 → 3) (33,5 → 40,0 s).
5. Bascule sur le **Plan de salle** : clic sur la table T9 → panneau latéral avec son statut
   ("Libre") et un encart **RÉSERVATION 17:47 · nathan dupont (4 pers.)** (40,0 → 46,0 s).
6. Retour à la liste, menu d'action "..." sur la ligne Nathan dupont → **Confirmer** / Check-in /
   Modifier / No-show / Annuler / Supprimer. Clic **Confirmer** → statut passe à **Confirmée**
   (46,0 → 58,0 s).
7. Plan de salle : la table T9 bascule manuellement sur **Réservée** (orange) via "Changer le
   statut" (58,0 → 64,0 s).
8. Retour à la liste, menu d'action à nouveau (Confirmer a disparu, remplacé par **Check-in** en
   tête) → clic **Check-in** → toast **"Client installé. Commande sur place CMD-2026-00111
   créée."** → OK. Le statut de la réservation passe à **Installée** (64,0 → 74,0 s).
9. Plan de salle : la table T9 est maintenant **Occupée** (rouge), avec l'encart **COMMANDE EN
   COURS — CMD-2026-00111 · 0,00 €** (74,0 → 78,29 s).

Arc complet et cohérent pour "tenir ses réservations au quotidien" : créer → assigner une table →
suivre sur le plan de salle → confirmer → installer le client (check-in, commande auto) → salle et
réservations synchronisées en temps réel.

## Voix off proposée (10 lignes) — **à valider avant génération ElevenLabs**

| # | Texte | Ancrage | Nouveau / réutilisé |
|---|---|---|---|
| N0 | Suivez vos réservations du jour, en un coup d'œil, directement dans FoodEatUp. | intro + A (liste + compteurs) | nouveau |
| N1 | Ajoutez une nouvelle réservation : nom, téléphone, e-mail, date, heure et nombre de couverts. | clic + B (formulaire) | nouveau |
| N2 | Assignez la table automatiquement, ou choisissez-la vous-même sur le plan de salle. | C (sélection table T9) | nouveau |
| N3 | Votre réservation apparaît aussitôt dans la liste, et sur le plan de salle. | D + E (liste + panneau table) | nouveau |
| N4 | Confirmez-la dès que le client valide : sa table passe automatiquement en « réservée ». | F + G (Confirmer → Confirmée/Réservée) | nouveau |
| N5 | À son arrivée, un check-in installe le client à table et crée sa commande sur place. | H (Check-in → toast) | nouveau |
| N6 | Réservations et plan de salle restent ainsi synchronisés, du service jusqu'à la dernière table. | I (Installée / Occupée + commande) | nouveau |
| N7 | Vous pouvez aussi créer une réservation depuis Claude : copiez ce prompt, remplacez les crochets. | claude1 (reveal) + claude2 (copié) | nouveau |
| N8 | Collez-le dans la conversation : la réservation est créée en quelques secondes. | claude3 (chatbot mockup) | nouveau |
| N9 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin | **réutilisé tel quel** (`foodeatup-reception-ean-dlc-tuto/vo/N8.mp3`, même texte, même md5 de carte outro) |

## Découpage (estimations — affinées au montage sur les frames exactes)

| Seg | Source (rush) | Sortie visée | Contenu |
|---|---:|---:|---|
| intro | carte | 2,60 s | TENIR SES RÉSERVATIONS AU QUOTIDIEN |
| A | 0,00 → 1,80 | 2,20 s | Réservations du jour, compteurs |
| clic1 | 1,80 → 2,20 | 0,70 s | **zoom-punch** sur "+ Nouvelle réservation" |
| B | 2,20 → 23,00 | 5,50 s | Formulaire client + créneau (setpts accéléré) |
| C | 23,00 → 33,50 | 4,00 s | Choix de la table T9 |
| clic2 | 33,50 → 34,00 | 0,60 s | **zoom-punch** sur "Créer la réservation" |
| D | 36,00 → 40,00 | 3,00 s | Liste : nouvelle réservation "En attente" |
| E | 40,00 → 46,00 | 3,20 s | Plan de salle : table T9, encart réservation |
| clic3 | 46,00 → 50,50 | 0,70 s | **zoom-punch** menu "..." + ouverture |
| F | 51,00 → 52,50 | 2,00 s | Menu d'action : Confirmer / Check-in / … |
| G | ~clic Confirmer | 1,00 s | Statut → **Confirmée** |
| H | 58,00 → 64,00 | 2,80 s | Plan de salle : T9 → **Réservée** (orange) |
| clic4 | 66,00 → 68,50 | 0,70 s | **zoom-punch** menu "..." + Check-in |
| I | 70,00 → 70,50 | 1,20 s | Toast "Client installé. Commande CMD-2026-00111 créée." |
| J | 72,00 → 74,00 | 1,80 s | Statut → **Installée** |
| K | 74,00 → 78,29 | 3,50 s | Plan de salle : T9 **Occupée** + commande en cours |
| claude1 | carte générée | 2,20 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 1,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 2,50 s | mockup chatbot Claude |
| outro | carte | 6,20 s (auto-étendue si besoin) | CTA |

Coordonnées de clic (zoom-punch) à mesurer précisément sur les frames réelles au montage
(`ffmpeg -ss t -frames:v 1`), pas encore relevées ici.

## Séquence Claude — module partagé

`mcp__Foodeatup__create_reservation(establishment_id, customer_name, party_size, date, time,
customer_phone?, customer_email?, table_id?, zone?)` couvre exactement la création d'une
réservation avec ses coordonnées client et son créneau — l'action la plus proche d'un geste
utilisateur unique dans ce rush (les étapes suivantes, confirmer/check-in, sont aussi couvertes
par `mcp__Foodeatup__confirm_reservation` et `mcp__Foodeatup__checkin_reservation`, mais un seul
prompt copier-coller doit rester simple : on montre la création, point d'entrée du flux).

> Crée une réservation chez FoodEatUp pour [nom du client] ([téléphone]), le [date] à [heure],
> pour [nombre] couverts. Établissement ID [ID établissement].

Même texte côté fiche Lovable (`claudePrompt`).

## Animations

Mêmes principes que la série : `setpts` pour la vitesse (jamais `zoompan` sur vidéo réelle),
zoom-punch en crop fixe (~1.20x, coordonnées mesurées sur frame réelle), bandeaux rendus en PNG
+ `overlay` (pas `drawbox` animé sur `t` — piège documenté dans
`FOODEATUP-TUTORIELS-WORKFLOW.md`), xfade 0,28 s, cartes intro/outro en fond flou + overlay net,
séquence Claude 3 temps (module partagé `videos/_shared/claude_prompt_sequence.py`).

## Statut

Script validé par Michael le 2026-08-06. VO générée (ElevenLabs, Adam FR `TGAegA0zNRi8I6nUdq3i`,
N9 réutilisée telle quelle depuis `foodeatup-reception-ean-dlc-tuto/vo/N8.mp3`). Montage terminé
(`build.py`) et checklist de compatibilité passée : H.264 High/yuv420p, AAC 48 kHz stéréo,
faststart (`moov` avant `mdat`), 0 erreur de décodage, peak -7,2 dBFS. Vignette YouTube générée
depuis `assets/intro.jpg` sans recadrage créatif (`out/thumbnail-youtube.jpg`, 1280x720).

**Publiée le 2026-08-06** (validation de Michael reçue) : RapidoCMS (vidéo + vignette uploadées
sur S3), LinkedIn programmé sur le compte FoodEatUp le 2026-08-29 07h (rotation pleine jusque
fin août), et Lovable (`src/data/tutorials.ts`, module `caroline-ia`, commit `630d78e` — a
remplacé une fiche stub déjà en place, mêmes `slug`/`section`/`order`). Voir l'entrée #33 dans
`videos/LOVABLE-FOODEATUP-DOCS.md` pour le détail complet. Workspace Lovable **Braindcode**
(changé le 2026-08-06, même `project_id`).
