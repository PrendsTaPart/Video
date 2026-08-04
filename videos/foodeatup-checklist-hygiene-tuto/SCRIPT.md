# Tutoriel — Créer sa check-list hygiène (HACCP)

Module HACCP (menu « Hygiène » → « Checklist hygiène »). Rush source :
`assets/screen.mp4`, 1920x828, 25 fps, 67,8 s.

## Ce que montre le rush

1. `0-9s` — Accueil HACCP, puis navigation vers Hygiène → Checklist hygiène (tabs
   « Hygiène du personnel » / « État des locaux »).
2. `9-30s` — Clic « Ajouter une checklist » → modale « Ajouter une nouvelle checklist » :
   nom du point de contrôle (« Contrôle hygiène équipe — service du soir »), catégorie
   (Hygiène du personnel), description.
3. `30-36s` — Soumission → toast « Checklist créée avec succès ! », nouvel item dans la
   liste (« Jamais validé »).
4. `36-48s` — Clic sur le nouvel item → modale « Validation de la checklist hygiène » :
   date/heure du relevé (pré-remplie), zone contrôlée (« Cuisine »), réponse
   Oui/Non/Non Évalué, commentaire, upload de justificatif (non utilisé dans le rush).
5. `48-60s` — Sélection « Oui », clic « Valider ».
6. `60-67,8s` — Toast « Checklist validée avec succès ! », retour au module Hygiène.

## Séquence Claude — deux outils MCP correspondent

- `mcp__Foodeatup__create_hygiene_checklist` (nom, catégorie, points de contrôle) —
  couvre l'étape 2 du rush.
- `mcp__Foodeatup__create_hygiene_checklist_validation` (template_id, réponses,
  statut, zone) — couvre l'étape 4-5 du rush.
Séquence animée 3 temps (module partagé `claude_prompt_sequence.py`) construite sur le
prompt de **création** (action la plus fréquente) ; le prompt de **validation** est
fourni en complément côté site Lovable (`claudePrompts[]`, 2 entrées), même principe que
`saisir-ses-ingredients`.

## Voix off proposée (9 lignes) — À VALIDER AVANT GÉNÉRATION AUDIO

| # | Texte | Ancrage |
|---|---|---|
| N0 | Créer une check-list hygiène sur FoodEatUp, en quelques clics. | carte d'intro |
| N1 | Depuis Hygiène, ouvrez Checklist hygiène, puis cliquez sur Ajouter une checklist. | navigation + clic |
| N2 | Donnez-lui un nom, une catégorie, et une description, puis cliquez sur Créer. | formulaire + soumission |
| N3 | Elle apparaît aussitôt dans la liste : ouvrez-la pour la valider. | succès + ouverture validation |
| N4 | Choisissez la zone contrôlée, cochez Oui, Non, ou Non évalué, et validez. | zone + réponse + validation |
| N5 | Vous gardez une trace claire et datée de chaque contrôle, prête en cas d'inspection HACCP. | bénéfice |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | étages Claude 1+2 (réutilisable) |
| N7 | Collez-le dans la conversation : votre checklist est créée en quelques secondes. | étage Claude 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA, réutilisable) |

N6/N8 réutilisables tels quels depuis un `vo/N*.mp3` existant de la série (texte
identique) — zéro crédit ElevenLabs.

## Prompt Claude (vidéo, étages 1-3)

```
Crée une checklist hygiène [nom du point de contrôle] pour la catégorie
[hygiène du personnel / état des locaux], avec les points de contrôle
[liste des points], pour mon établissement FoodEatUp (ID [ID établissement]).
```

## Prompts Lovable (`claudePrompts[]`, 2 entrées)

1. **Créer une checklist hygiène** — prompt ci-dessus.
2. **Valider une checklist hygiène** — `Valide la checklist [nom du point de
   contrôle] pour la zone [zone contrôlée] : réponse [Oui/Non/Non évalué],
   commentaire [commentaire], pour mon établissement FoodEatUp (ID [ID
   établissement]).`
