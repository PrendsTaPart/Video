# Publication YouTube — chaîne Plan-it

Chaîne `UCj2P8FZ4YwygALBLITfOKNA` (« Plan-it »), publications du 27/08/2026.
Format Shorts : vertical 1080 × 1920, moins de 70 s, `#Shorts` dans le titre,
description portant le lien vers la fiche du site.

## Publiées — 18 vidéos, toutes en public

| Fiche | Titre | Lien |
|---|---|---|
| 01 | Se connecter à son espace | https://www.youtube.com/watch?v=W4j-Y6lPD5o |
| 02 | Retrouver son mot de passe | https://www.youtube.com/watch?v=LMa_x0eYaA8 |
| 03 | Les premiers réglages de votre entreprise | https://www.youtube.com/watch?v=f9TTHEuZ4pU |
| 05 | Utiliser une carte de prompt | https://www.youtube.com/watch?v=YyhBV1EA0uQ |
| 06 | Chercher la bonne carte de prompt | https://www.youtube.com/watch?v=KJ-d-L72fmQ |
| 07 | Enregistrer sa propre carte de prompt | https://www.youtube.com/watch?v=G2QXbFd52Zc |
| 10 | Lancer une tâche qui prend du temps | https://www.youtube.com/watch?v=Njk8EXxxQXg |
| 11 | Suivre l'avancement de ses tâches | https://www.youtube.com/watch?v=rYFhCVgXpwk |
| 12 | Brancher Google Agenda et Gmail | https://www.youtube.com/watch?v=bru7Eb2AXfk |
| 13 | Brancher un serveur MCP | https://www.youtube.com/watch?v=YUk_gg52qZU |
| 14 | Gérer et débrancher ses connecteurs | https://www.youtube.com/watch?v=kTfRPw6U2Ns |
| 21 | Déposer ses documents dans la base de connaissance | https://www.youtube.com/watch?v=0ArqaoTaBm8 |
| 22 | Organiser sa base de connaissance | https://www.youtube.com/watch?v=om5rfkJzcPk |
| 23 | Mettre à jour un document déjà déposé | https://www.youtube.com/watch?v=q3B_1izfXNQ |
| 25 | Retirer un document de la base | https://www.youtube.com/watch?v=bx8jVibD5Gs |
| 26 | Comprendre à quoi servent les skills | https://www.youtube.com/watch?v=iD_Vo6qTPow |
| 27 | Activer un skill sur un agent | https://www.youtube.com/watch?v=nMLqbGVb_aY |
| 28 | Installer un plugin | https://www.youtube.com/watch?v=4Nmehan_smg |

## Restent à publier

| Fiche | Motif |
|---|---|
| 00 · Créer son compte | quota ; le fichier corrigé est déposé et prêt |
| 04 · Lire son tableau de bord | quota |
| 08 · Transformer une carte en routine | quota |
| 29 · Désactiver un skill ou un plugin | quota |
| 33 · Choisir l'avatar 3D de son agent | quota |
| 34 · Personnaliser la fiche de son agent | quota |
| 36 · Suivre ses indicateurs | quota |
| 39 · Régler ses notifications | quota |
| 40 · Comprendre ses crédits | quota |

YouTube refuse avec `uploadLimitExceeded` — « The user has exceeded the number
of videos they may upload ». Le quota était déjà entamé le 27/08 par les vidéos
RapidoCRM, et l'était encore le 28/08 à 12 h 20. Il se réinitialise sous 24 h.

Attention avant de reprendre : la chaîne active était repassée sur **RapidoCRM**
le 28/08 au matin. `get_channel_status` d'abord, `switch_channel` vers
`UCj2P8FZ4YwygALBLITfOKNA` ensuite — publier sans vérifier déposerait les
tutoriels Plan'It sur la mauvaise chaîne.

## Deux réserves

**Le tutoriel 00 avait été refusé par YouTube.** Sa capture laissait voir des
adresses e-mail — celle du compte de démonstration, mais surtout **trois
adresses réelles de tiers** dans la barre de suggestions du clavier, tirées de
l'historique du téléphone. Le montage republié est masqué et vérifié image par
image (`masquer.py`, `verifier_masquage.py`). L'ancienne version reste sur la
chaîne en **non répertorié** (`hMKF-nSLNvQ`) : le MCP ne sait ni supprimer une
vidéo ni changer sa confidentialité, il faut la retirer depuis YouTube Studio.

**Les liens YouTube ne sont pas stockés sur les fiches.** Le MCP Plan'It Video
n'expose pas d'outil `enregistrer_youtube` — contrairement aux MCP Académie de
RapidoCMS, RapidoCRM et RapidoRH. Ce fichier tient donc lieu de registre.

## La fiche 15 n'est pas publiée

Elle est en `en_montage` : son montage a été déplacé sur la fiche 3, dont il
décrit réellement le contenu. Elle attend une capture d'un premier échange.

## `enregistrer_video` est en panne côté serveur (28/08)

Le MCP Plan'It Video refuse « Adresse de vidéo invalide » sur toutes les URL,
**y compris celle que la fiche 40 porte déjà en base**. Ce n'est donc pas une
question de forme d'URL : la validation elle-même est cassée. Le MCP RapidoTuto
répondait au même moment en 502.

Les fiches 08 et 34 ont donc reçu leur vignette et leur transcription, mais pas
leur vidéo. Les fichiers sont sur S3, prêts à être rattachés :

- `planit-academie-tuto-08-transformer-une-carte-en-routine` — 50 s
- `planit-academie-tuto-34-personnaliser-la-fiche-agent` — 54 s

Les chapitres à redéposer avec sont dans le journal de la session ; ils se
recalculent aussi depuis `out/render.log` de chaque épisode.
