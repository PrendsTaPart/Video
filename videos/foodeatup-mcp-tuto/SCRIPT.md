# Tutoriel — Brancher son MCP sur Claude

Vidéo transversale (pas rattachée à un module produit) : configurer et
connecter le MCP FoodEatUp à Claude. Durée livrée : **35,68 s** — H.264
High/yuv420p, AAC 48 kHz stéréo, faststart. Audio : true peak **-7,33 dBFS**.
Sans avatar HeyGen, **sans séquence Claude en fin de vidéo** (cette vidéo EST
déjà entièrement "utiliser avec Claude" — un appendice aurait été circulaire).

## Voix off (7 lignes)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N1 | Depuis la Marketplace de prompts FoodEatUp, copiez l'URL de votre MCP. | 4,36 s | A (zoom-punch) |
| N2 | Dans Claude, ouvrez Paramètres puis Connecteurs, et ajoutez un connecteur personnalisé avec cette URL. | 6,11 s | B |
| N3 | Cliquez sur Ajouter pour créer la connexion. | 2,27 s | C (zoom-punch) |
| N4 | Claude liste aussitôt tous les outils FoodEatUp disponibles. | 3,00 s | D |
| N5 | Autorisez l'accès pour que Claude puisse utiliser vos données et actions FoodEatUp. | 4,26 s | E (zoom-punch) |
| N6 | Vous choisissez précisément quels outils Claude peut utiliser, et vous pouvez révoquer l'accès à tout moment. | 5,69 s | F |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (réutilisée depuis planning-poste-tuto) |

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,50 s | BRANCHER SON MCP SUR CLAUDE |
| A | 0,00 → 7,00 | 4,90 s | Marketplace de prompts, carte « Foodeatup mcp », **zoom-punch** sur « Copier l'URL » (1663, 429) |
| B | 12,00 → 26,00 | 6,60 s | Claude > Connecteurs > Ajouter un connecteur personnalisé (nom + URL) |
| C | 26,00 → 27,50 | 2,80 s | **zoom-punch** sur « Ajouter » (1271, 742) |
| D | 28,00 → 33,00 | 3,50 s | Liste des outils FoodEatUp requis/disponibles |
| E | 34,00 → 37,50 | 4,80 s | **zoom-punch** sur « Autoriser » (742, 595), écran OAuth 2.0 |
| F | 42,00 → 48,00 | 6,20 s | État connecté final, autorisations par outil (Autoriser tout / Personnaliser) |
| outro | carte | 6,20 s | CTA |

URL MCP FoodEatUp confirmée à l'écran : `https://foodeatup.com/api/mcp`.

## Contenu Lovable demandé par Michael (au-delà de la fiche standard)

- **Lien du MCP** : `https://foodeatup.com/api/mcp` (visible dans le rush).
- **Redirections vers les connecteurs Claude / Mistral / OpenAI** : pointées
  vers les applications elles-mêmes (`claude.ai`, `chat.mistral.ai`,
  `chatgpt.com`) plutôt qu'une URL profonde de réglages devinée — le rush ne
  montre que la navigation Claude (Paramètres → Connecteurs), donc le texte
  décrit cette même navigation pour les 3, sans fabriquer un chemin d'URL non
  vérifié pour Mistral/OpenAI.
- **Explication de ce à quoi sert le MCP** : dans `whatItsFor`/`chefTip`.
- **Placement** : demande explicite d'une place sur l'accueil du site en plus
  de la fiche tutoriel — remonté à l'agent Lovable pour qu'il choisisse
  l'emplacement (composant d'accueil) cohérent avec le reste du site.

## Statut publication

Vidéo à livrer à Michael pour validation avant publication RapidoCMS/
LinkedIn/Lovable. RapidoCMS non autorisé dans cette session — publication
CMS/LinkedIn en attente dans tous les cas.
