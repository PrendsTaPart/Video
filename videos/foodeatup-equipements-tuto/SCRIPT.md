# Tutoriel — Déclarer ses équipements (Module HACCP)

Dossier Drive / module « Hygiène & HACCP ». Rush fourni : `Ajouter_Supprimer_Modifier_un_équipement.mp4`
(1920x828, 25fps, 42,32 s). Intro fournie : `DÉCLARER SES ÉQUIPEMENTS MODULE HACCP.jpg`.
Outro CTA générique (réutilisée telle quelle, déjà utilisée sur les autres tutos).

Pas d'avatar sur ce rush — VO ElevenLabs (Adam FR, `TGAegA0zNRi8I6nUdq3i`) sur toute la vidéo.

## Statut build (2026-08-03)

Durée livrée : **50,92 s**. Checklist de compatibilité passée : H.264 High/yuv420p,
AAC LC 48 kHz stéréo, faststart (moov avant mdat), 0 erreur de décodage, true peak
**-7,26 dBFS** (bonne marge sous 0 dBFS). Offsets VO calculés sans dérive (`drift: none
-- all lines on their anchors`) après calibration des durées de segment sur les VO
réelles (règle du pipeline : dimensionner chaque segment sur sa ligne VO, pas l'inverse).

## Déroulé observé dans le rush (analyse frame-by-frame, 1fps + zooms)

| t≈ | Écran |
|---|---|
| 0-4s | Module HACCP > Températures > onglet Équipements, liste vide ("Aucun équipement — Commencez par créer votre premier équipement") |
| 4-6s | Clic **« + Ajouter un équipement »** → modale |
| 6-12s | Saisie du champ **Nom** : « frigidaire » |
| 12-14s | Sélection du **Type** : radio « Congélateur (min -25°C, max -18°C) » → aperçu live affiché |
| 14-18s | Saisie de l'**Emplacement** (optionnel) : « cuisine » |
| 18-20s | Clic **« Enregistrer »** |
| 20-22s | Retour à la liste : ligne « frigidaire », -20,0°C, statut Congélateur, icônes crayon/corbeille |
| 22-24s | Clic sur le **crayon** → modale « Modifier un équipement » (champs pré-remplis) |
| 24-30s | Relecture des champs (Nom, Type, Emplacement) |
| 30-32s | Clic **« Enregistrer »** (modale Modifier) → retour à la liste |
| 32-34s | Liste avec la ligne « frigidaire » |
| 34-36s | Clic sur la **corbeille** → modale de confirmation « Êtes-vous sûr ? » |
| 36-40s | Confirmation affichée, texte « Voulez-vous supprimer l'équipement "frigidaire" ? » |
| 40-42s | Clic **« Oui, supprimer ! »** → liste de nouveau vide |

Titre observé sur les 3 modales : « Ajouter un équipement » / « Modifier un équipement » — même
formulaire (Nom, Type radio, Emplacement optionnel), c'est le composant réutilisé partagé.

## Voix off (9 lignes)

| # | Texte | Segment | Notes |
|---|---|---|---|
| N0 | Vos équipements FoodEatUp : frigos, congélateurs, chambres froides… tout se déclare en quelques clics. | intro / liste vide | accroche |
| N1 | Cliquez sur « Ajouter un équipement », donnez-lui un nom et choisissez son type : congélateur, frigo ou maintien au chaud. | clic bouton + saisie Nom + Type | |
| N2 | Ajoutez son emplacement, comme « cuisine », puis cliquez sur « Enregistrer ». | Emplacement + clic Enregistrer | |
| N3 | Votre équipement apparaît dans la liste, avec sa plage de température réglementaire déjà appliquée. | retour liste | |
| N4 | Besoin de le renommer ou de changer son type ? Cliquez sur le crayon, modifiez, puis enregistrez. | clic crayon + modale Modifier | |
| N5 | Pour le retirer, cliquez sur la corbeille et confirmez la suppression. | clic corbeille + confirmation | |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | séquence Claude étages 1+2 | **réutilisée telle quelle** (identique à `foodeatup-vitrine-tuto`/`foodeatup-tva-tuto`) |
| N7 | Collez-le dans la conversation : votre équipement est déclaré en quelques secondes. | séquence Claude étage 3 | spécifique à ce tuto |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) | **réutilisée telle quelle** |

## Séquence Claude — outil MCP correspondant

`create_equipment(establishment_id, label, type, emplacement)` correspond exactement à l'action
« Ajouter un équipement » montrée dans le rush (seule action de ce tuto exposée en MCP — modifier/
supprimer un équipement n'ont pas d'outil MCP dédié, donc pas de prompt pour ces deux actions,
conformément à la règle du pipeline).

> Crée l'équipement [nom de l'équipement] de type [congélateur / frigo / chambre_froide / cellule /
> four] à l'emplacement [emplacement] pour mon établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompt`).

## Fiche Lovable (à confirmer avec le script)

- **slug** : `declarer-ses-equipements`
- **title** : Déclarer ses équipements (Module HACCP)
- **moduleSlug** : `haccp`
- **subcategory** : Équipements : ajouter, modifier, supprimer
- **whatItsFor** : Déclarer chaque frigo, congélateur ou chambre froide de votre cuisine en
  quelques clics, avec sa plage de température réglementaire appliquée automatiquement selon le
  type choisi — la base indispensable avant de démarrer vos relevés de température HACCP.
- **chefTip** : Le type choisi (Congélateur, Frigo, Chaud) fixe automatiquement la plage de
  température réglementaire de l'équipement — c'est elle qui détermine ensuite si un relevé est
  "conforme" ou "non conforme". Un mauvais type sélectionné par réflexe peut donc déclencher de
  fausses alertes non conformes sur un équipement qui fonctionne pourtant normalement : vérifiez
  toujours le type avant d'enregistrer. Et ne vous inquiétez pas pour la suppression : FoodEatUp
  demande toujours une confirmation explicite ("Êtes-vous sûr ?") avant de retirer un équipement,
  impossible de le supprimer par un clic accidentel.
- **chefTipAvatar** : `michael-chef-mascot.jpg` (comme les tutos précédents)

## Statut

Vidéo montée et livrée à Michael pour validation. **Ne pas publier (RapidoCMS, LinkedIn,
Lovable) avant retour explicite** — règle STOP obligatoire du pipeline
(`FOODEATUP-TUTORIELS-WORKFLOW.md`).
