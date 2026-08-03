# Tutoriel — Suivre les suggestions de l'agent IA (PrediBot) FoodEatUp

Deuxième vidéo du module PrediBot (Agent IA Directeur), après `predire-ses-commandes`.
Rush fourni par Michael : `assets/screen.mp4` (42,24 s, 1920x828, piste audio native
silencieuse à -91 dB — VO entièrement ElevenLabs, comme sur `foodeatup-produits-tuto`).
Pas de clip avatar dans ce dossier.

## Ce que montre le rush

1. Tableau de bord StockVisionAI : carte "Stock critique" — 12 rupture(s) · 6 en stock
   faible (0,0 → 2,2 s).
2. Clic sur le menu hamburger (2,2 → 2,6 s) → le menu latéral s'ouvre : Équipe,
   StockVisionAI, Comptabilité, HACCP, **PrediBot**, **Agent IA**, Module Service,
   Module Marketing, Configuration boutique.
3. Le sous-menu PrediBot se déploie (Tableau de bord, Prédictions stock, Prévisions
   commandes, Production recommandée, **Chat PrediBot**) puis clic sur "Chat PrediBot"
   (6,0 → 6,3 s).
4. Chargement ("Connexion à PrédiBot...") puis message d'accueil de l'agent avec des
   **suggestions cliquables** : Stocks / Commandes / HACCP (6,3 → 11,5 s) — c'est
   littéralement "suivre les suggestions de l'agent IA", le titre de la vidéo.
5. L'utilisateur pose sa question en langage naturel : "Quels sont les produits en
   rupture de stock ?" (11,5 → 12,8 s).
6. L'agent réfléchit ("Thinking...", "Réflexion durant 11s", 12,8 → 28,5 s).
7. Réponse détaillée, produit par produit (Dragon Roll, mozzarella, ...), avec
   quantité, seuil, emplacement, fournisseur, prix d'achat, péremption, et un lien
   direct vers la page stocks de l'établissement (28,5 → 42,2 s).

## Voix off (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Segment |
|---|---|---|
| N0 | Le tableau de bord de FoodEatUp repère vos stocks à risque, et vous suggère de demander de l'aide à l'agent IA. | intro + A |
| N1 | Ouvrez le menu et retrouvez PrediBot, votre agent IA. | clic B (hamburger) |
| N2 | Cliquez sur Chat PrediBot pour lui parler directement. | C + clic D |
| N3 | L'agent vous propose déjà des suggestions : stocks, commandes, HACCP. | E — accueil + suggestions |
| N4 | Posez votre question en langage naturel, par exemple sur vos ruptures de stock. | F — question posée |
| N5 | PrediBot analyse vos données et répond aussitôt, produit par produit, prêt à agir. | G + H — réflexion + réponse |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | claude1+2 (réutilisé de `foodeatup-produits-tuto/vo/N6.mp3`) |
| N7 | Collez-le dans la conversation : vos produits en stock bas apparaissent aussitôt. | claude3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (réutilisé de `foodeatup-produits-tuto/vo/N8.mp3`) |

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,60 s | SUIVRE LES SUGGESTIONS DE L'AGENT IA |
| A | 0,00 → 2,20 | 2,40 s | Tableau de bord, carte "Stock critique" |
| B | 2,20 → 2,60 | 0,70 s | **zoom-punch** sur le menu hamburger (145, 138) |
| C | 2,60 → 6,00 | 2,60 s | Menu ouvert, sous-menu PrediBot déployé |
| D | 6,00 → 6,30 | 0,70 s | **zoom-punch** sur "Chat PrediBot" (250, 748) |
| E | 6,30 → 11,50 | 3,20 s | Accueil PrediBot + suggestions (Stocks/Commandes/HACCP) |
| F | 11,50 → 12,80 | 1,80 s | Question posée : "Quels sont les produits en rupture de stock ?" |
| G | 12,80 → 28,50 | 3,00 s | Réflexion de l'agent ("Thinking...", 11s) |
| H | 28,50 → 42,24 | 7,50 s | Réponse détaillée + lien vers la page stocks |
| claude1 | carte générée | 2,20 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 1,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 2,50 s | mockup chatbot Claude |
| outro | carte | 6,20 s (auto-étendue si besoin) | CTA |

Coordonnées mesurées sur les frames réelles (`ffmpeg -ss t -frames:v 1`), pas
estimées à l'oeil.

## Séquence Claude — module partagé

Outil correspondant à ce que montre le rush : `mcp__Foodeatup__list_low_stocks
(establishment_id)` — liste les articles en stock dont le niveau est bas
(`is_low = true`), exactement la question posée à l'oral ("produits en rupture de
stock").

> Montre-moi les produits en stock bas ou en rupture pour mon établissement
> FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompt`).

## Animations

Mêmes principes que toute la série : `setpts` pour la vitesse (jamais `zoompan` sur
la vidéo réelle), zoom-punch en crop fixe sur les 2 clics, bandeaux d'étape (pas
d'apostrophe dans les textes de bandeau), xfade 0,28 s partout, cartes intro/outro en
fond flou + overlay net. Pas de clip avatar. Séquence "Utilisez cette fonctionnalité
avec Claude" en 3 temps, module partagé `videos/_shared/claude_prompt_sequence.py`.

## Statut publication

Vidéo montée et livrée à Michael dans la foulée de sa demande explicite ("réalise la
vidéo ... publie sur le compte Lovable ... FoodEatUp académy"). Publication limitée à
Lovable (site FoodEatUp Academy) comme demandé — pas d'upload RapidoCMS ni de
programmation LinkedIn, non demandés dans cette tâche.
