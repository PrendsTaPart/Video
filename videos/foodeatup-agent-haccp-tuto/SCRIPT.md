# Tutoriel — Agent HACCP (relevé de température par WhatsApp)

Module **Hygiène & HACCP** (`haccp`). Statut : **script proposé, AUCUN AUDIO GÉNÉRÉ, AUCUN
MONTAGE FAIT** — en attente de validation (règle `FOODEATUP-TUTORIELS-WORKFLOW.md` §3, STOP
obligatoire avant ElevenLabs).

## Intrants reçus de Michael

- `assets/intro.jpg` — carte d'ouverture "AGENT HACCP" (photo réelle, bouton "Rejoignez-nous"
  réutilisé tel quel comme carte de marque — pas de redesign)
- `assets/outro.jpg` — carte de fin CTA, **identique byte-à-byte** (md5 `bd812eb8…`) à
  `foodeatup-predibot-tuto/assets/outro.jpg` déjà utilisée sur toute la série
- `assets/screen.mp4` — écran capturé, 1526x1032, 25 fps, **15,28 s**, avec son (à vérifier si
  exploitable ou à couper — voix off série prend le dessus dans tous les cas)

## Déroulé observé dans le rush (frames extraites, 0,5–1 s)

L'agent conversationnel **"Predibot" / StockVisionAI** (bot WhatsApp de FoodEatUp) est déjà
utilisé pour d'autres actions (création de recette) au début de la capture ; le rush se
concentre sur la partie **HACCP** :

| t (rush) | Contenu |
|---:|---|
| 0,0 – 8,0 s | App WhatsApp "Predibot" : l'historique défile jusqu'à l'échange HACCP — l'utilisateur écrit **"je veux modifier une temperature"** ; StockVisionAI répond en demandant **ID de l'équipement, Température relevée, Notes (optionnel)** avec le lien `foodeatup.com/establishment/26/haccp/temperatures` ; l'utilisateur répond **"ID de l'équipement 158 / Température relevée 20 / Notes : test"** ; StockVisionAI confirme **"température ajoutée avec succès !"** |
| 8,5 – 11,0 s | Bascule sur le navigateur, page **Températures** du module HACCP (`.../haccp/temperatures`) : état **avant** — l'équipement listé est à **10,0 °C**, compteur **3 non conformes** |
| ~13,0 s | La page reflète la mise à jour envoyée par WhatsApp : l'équipement passe à **20,0 °C**, compteur **4 non conformes** (mis à jour automatiquement) |
| 13,0 – 15,28 s | Hold sur la valeur 20,0 °C en surbrillance |

**Le point clé du rush** : la preuve que la valeur envoyée par un simple message WhatsApp
(équipement 158, 20 °C) atterrit instantanément dans le module HACCP de FoodEatUp, sans
ouvrir l'application — c'est le fil conducteur de la vidéo.

## Recherche d'un outil MCP correspondant (règle `LOVABLE-FOODEATUP-DOCS.md` étape 3)

Correspondance directe : `add_temperature(establishment_id, equipment_id, temperature,
measured_at)` — déjà utilisé comme `claudePrompt` sur `foodeatup-temperature-tuto` pour la
même action (relever une température d'équipement). Réutilisation du même texte de prompt
(cohérence demandée par le workflow) :

> Enregistre une température de [température] degrés pour l'équipement [ID ou nom de
> l'équipement] dans mon établissement FoodEatUp (ID [ID établissement]).

Réponse assistant : « Bien sûr ! J'enregistre votre relevé de température… »

→ Séquence "Utilisez cette fonctionnalité avec Claude" (3 étages, module partagé
`_shared/claude_prompt_sequence.py`) à ajouter avant la carte de fin.

## Voix off proposée (9 lignes) — SOUMISE À VALIDATION, AUCUN AUDIO GÉNÉRÉ

Voix Adam FR (ElevenLabs, `TGAegA0zNRi8I6nUdq3i`, `eleven_multilingual_v2`), défauts dashboard.

| # | Texte | Ancrage |
|---|---|---|
| N0 | Relever une température sans ouvrir l'application ? Avec l'Agent HACCP, un message WhatsApp suffit. | intro / accroche |
| N1 | Vous écrivez simplement : je veux modifier une température. | échange WhatsApp — requête utilisateur |
| N2 | L'agent vous demande l'équipement concerné, la température relevée, et une note si besoin. | échange WhatsApp — question du bot |
| N3 | Vous répondez en une ligne : l'équipement, la valeur, et c'est parti. | échange WhatsApp — réponse utilisateur |
| N4 | Température ajoutée avec succès : l'agent confirme aussitôt. | échange WhatsApp — confirmation bot |
| N5 | Et dans FoodEatUp, le relevé est déjà là : l'équipement passe à vingt degrés, et le compteur de non-conformités se met à jour tout seul. | navigateur — preuve avant/après (10 °C → 20 °C) |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | séquence Claude — étages 1+2 (reveal + copié) |
| N7 | Collez-le dans la conversation : votre relevé de température est enregistré en quelques secondes, exactement comme sur WhatsApp. | séquence Claude — étage 3 (chatbot) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) |

**N8 réutilisable tel quel** (byte-identique déjà présent sur plusieurs tutos, ex.
`foodeatup-predibot-tuto/vo/N7.mp3` / `foodeatup-fournisseurs-tuto/vo/N8.mp3`) — pas besoin de
le régénérer si Michael valide. **N7 est spécifique à ce tutoriel** (nomme l'objet créé : un
relevé de température), pas de réutilisation par réflexe (piège documenté dans le workflow).

## Découpage envisagé (coordonnées de clic à recalibrer par seuillage colorimétrique au montage)

| Seg | Source | Contenu |
|---|---|---|
| intro | carte | AGENT HACCP |
| A | 0,0 → ~8,0 (WhatsApp) | échange complet : requête → question agent → réponse → confirmation (light zoom/pan, pas de vrai clic à puncher — c'est un fil de discussion) |
| B | 8,5 → 11,0 | page Températures — état avant (10,0 °C, 3 non conformes) |
| C | ~13,0 → 15,28 | page Températures — état après (20,0 °C, 4 non conformes) |
| claude1-3 | cartes générées | séquence "Utilisez cette fonctionnalité avec Claude" (module partagé) |
| outro | carte | CTA (réutilisée) |

Durée cible finale : ~40-48 s une fois les segments calés sur la durée réelle de chaque ligne
VO mesurée après génération (règle `FOODEATUP-TUTORIELS-WORKFLOW.md`).

## Champs Lovable envisagés (`src/data/tutorials.ts`, étape 2-3 de `LOVABLE-FOODEATUP-DOCS.md`)

```
slug: "agent-haccp-whatsapp"
title: "Agent HACCP : relevez vos températures depuis WhatsApp"
moduleSlug: "haccp"
subcategory: "Agent HACCP (WhatsApp)"
howItWorks: [
  "Écrivez à l'Agent HACCP sur WhatsApp : « je veux modifier une température ».",
  "Répondez avec l'ID de l'équipement, la température relevée et une note optionnelle.",
  "L'agent confirme, et le relevé apparaît aussitôt dans votre module HACCP FoodEatUp.",
]
whatItsFor: "Relevez vos températures HACCP sans ouvrir l'application, directement depuis WhatsApp — gain de temps en cuisine, traçabilité identique."
claudePrompt: "Enregistre une température de [température] degrés pour l'équipement [ID ou nom de l'équipement] dans mon établissement FoodEatUp (ID [ID établissement])."
chefTip: (à écrire — astuce du chef sur l'usage terrain, ex: "Gardez votre téléphone sous la main pendant le service : un relevé pris en marchant vaut mieux qu'un relevé oublié.")
chefTipAvatar: (photo réelle de Michael si fournie, sinon icône chef par défaut)
```

## STOP obligatoire

Script ci-dessus **proposé, pas validé**. Pas de génération audio ElevenLabs, pas de montage,
pas de publication (RapidoCMS/LinkedIn/Lovable/GitHub) tant que Michael n'a pas donné son
accord explicite (ou demandé des ajustements — dans ce cas, corriger puis re-soumettre).
