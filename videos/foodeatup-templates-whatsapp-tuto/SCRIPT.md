# Tutoriel — Créer ses templates WhatsApp marketing FoodEatUp

**Livrable monté** : `out/foodeatup-templates-whatsapp-tuto-v1.mp4` — 56,48 s, H.264/yuv420p
1920x828, AAC 48 kHz stéréo, faststart, peak audio **-7,3 dBFS**. Vignette YouTube :
`out/thumbnail-youtube.jpg` (recadrage neutre 1280x720 depuis `assets/intro.jpg`, 96 Ko).
Trois zoom-punch (onglet "Templates WhatsApp", "Nouveau template", "Enregistrer") —
coordonnées mesurées par seuillage couleur (PIL/numpy), vérifiées visuellement après
montage. Dérive résiduelle acceptée sur 2 lignes (N3 +2,41s, N7 +2,85s — narration qui
rattrape légèrement l'écran suivant, comme sur `foodeatup-campagne-marketing-tuto`) :
inhérente à la longueur des lignes N1/N2/N6 face aux fenêtres fixes des zoom-punch (0,9s),
tentatives d'agrandir les segments en amont ne la réduisent pas (les deux ancrages sont
liés à la même chaîne de segments et se décalent ensemble). Pas de `banner()` : la page et
la modale portent déjà leurs propres libellés.

Module 8 « MARKETING, FIDÉLITÉ & IRIS » (`marketing-fidelite`), catalogue 157 tutoriels,
item **08 « Créer ses templates WhatsApp marketing »**. Deuxième tutoriel du module (après
`lancer-une-campagne-marketing`, section "Pack marketing & campagnes").

Intrants fournis par Michael : `assets/intro.jpg` (carte « TEMPLATES WHATSAPP »),
`assets/outro.jpg` (carte CTA générique, réutilisée telle quelle), `assets/screen.mp4`
(screen recording 1920x828, 25 fps, 37,96 s, muet au montage).

## Déroulé observé (frames extraites à 1 fps + zooms ciblés)

| t | Écran | Détail |
|---:|---|---|
| 0-2s | Page « Campagnes & automatisations » | Mêmes stats que le tuto campagne (43,5€ / 3 / 38 / 3-7) |
| 2s | Clic **Templates WhatsApp** (onglet) | Bascule sur la page Templates |
| 3s | Page « Templates whatsapp » (vide) | Bandeau explicatif (fenêtre 24h Meta), bandeau "Twilio non configuré : soumissions simulées", état vide "Aucun template" |
| 4s | Clic **Nouveau template** | Ouvre la modale « Nouveau template » |
| 5-17s | Nom Meta | Validation live (minuscules + underscores) pendant la saisie de **« reconquete_clients »** ; Catégorie **Marketing**, Langue **fr** |
| 18-31s | Corps du message + variables | **« Bonjour {{1}}, on vous attend chez {{2}} ! Profitez de {{3}} avec le code {{4}}. »** — 4 variables détectées ; libellés saisis **« prenom, restaurant, offre, code »** ; image d'en-tête laissée vide |
| 32s | Clic **Enregistrer** | Chargement |
| 33-38s | Toast + carte template | **« Template enregistré ✓ »** — carte "Reconquete_clients", statut **Brouillon**, MARKETING·fr, boutons Modifier / Soumettre à Meta / Supprimer |

Outil MCP correspondant : `create_whatsapp_template` (brouillon) puis `submit_whatsapp_template`
(`confirm:true`, envoi à l'approbation Meta 24-48h, non modifiable après) — le brouillon est
créé dans la vidéo, la soumission Meta est visible comme prochaine étape (bouton) mais pas
cliquée dans le rush.

## Voix off (proposition, 11 lignes) — voix Adam FR (`TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Créer un template WhatsApp sur FoodEatUp ? Suivez le guide. | carte d'intro |
| N1 | Direction l'onglet Templates WhatsApp, pour vos messages hors fenêtre de 24 heures. | clic onglet Templates WhatsApp |
| N2 | Cliquez sur Nouveau template pour rédiger votre premier modèle. | clic Nouveau template |
| N3 | Donnez-lui un nom Meta, une catégorie et sa langue. | nom + catégorie + langue |
| N4 | Rédigez votre message avec des variables, comme accolade un, accolade deux. | corps du message |
| N5 | Nommez ces variables : prénom, restaurant, offre, code. | libellés des variables |
| N6 | Enregistrez : votre template est prêt, encore en brouillon. | clic Enregistrer + toast |
| N7 | Il ne reste plus qu'à le soumettre à Meta pour l'utiliser dans vos campagnes. | carte template (bouton Soumettre à Meta) |
| N8 | Vous pouvez aussi le créer depuis Claude : copiez ce prompt, remplacez les crochets. | séquence Claude — étage 1+2 (reveal + copié) |
| N9 | Collez-le dans la conversation : votre template est prêt en quelques secondes. | séquence Claude — étage 3 (mockup chatbot) |
| N10 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA — réutilisable telle quelle) |

Durée cible : ~45-55 s (raw 38 s, narration plus dense que le rush -> segments ralentis).

## Séquence de fin « cas d'usage + prompt Claude »

`mcp__FoodEatUp__create_whatsapp_template` + `mcp__FoodEatUp__submit_whatsapp_template`
correspondent exactement au flux filmé (créer le brouillon, prêt à soumettre). Séquence en 3
temps (reveal → copié → mockup chatbot) via `videos/_shared/claude_prompt_sequence.py`.

Prompt (identique côté vidéo et côté fiche Lovable `claudePrompt`) :

> Crée un template WhatsApp nommé [nom_meta] (catégorie [MARKETING/UTILITY], langue [fr]) avec le message « [texte avec {{1}}, {{2}}...] » et les variables [prenom, offre, ...], puis soumets-le à l'approbation Meta pour mon établissement FoodEatUp (ID [ID établissement]).

## Fiche Lovable (à ajouter après validation)

```
slug: "creer-ses-templates-whatsapp"
title: "Créer ses templates WhatsApp marketing"
moduleSlug: "marketing-fidelite"
subcategory: "08 · Pack marketing & campagnes"
section: "Pack marketing & campagnes"
order: 8
durationSeconds: ~50 (ajusté après montage)
howItWorks: [
  "Depuis Campagnes & automatisations, ouvrez l'onglet Templates WhatsApp.",
  "Cliquez sur Nouveau template.",
  "Donnez-lui un nom Meta (minuscules + underscores), une catégorie et sa langue.",
  "Rédigez le corps du message avec des variables numérotées {{1}}, {{2}}...",
  "Nommez ces variables dans l'ordre (prénom, offre, code...).",
  "Enregistrez : le template est créé en brouillon, prêt à être soumis à Meta.",
]
whatItsFor: "Écrire à vos clients par WhatsApp même hors de la fenêtre de 24h imposée par Meta — un modèle pré-approuvé, réutilisable dans toutes vos campagnes WhatsApp."
claudePrompt: "<voir ci-dessus>"
```

## À valider avec Michael avant de continuer

1. Script voix off ci-dessus (STOP obligatoire avant génération ElevenLabs).
2. Nom du template utilisé dans le rush, **« reconquete_clients »** — je le garde tel quel ?
