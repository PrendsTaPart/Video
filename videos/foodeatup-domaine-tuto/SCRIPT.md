# Tutoriel — Connecter son Domaine (mon site)

Catalogue 157 tutoriels : module `site-web-vitrine` (Site Web & Vitrine, `#2563EB`),
tutoriel **08 Connecter son Domaine (mon site)** — voir `CATALOGUE-157-TUTORIELS.md`
ligne "3. Site Web & Vitrine". Module actuellement à **0/8 publié**
(`PROGRESSION-157-TUTORIELS.md`) : ce serait le tout premier tutoriel du module.

Rush fourni par Michael : `assets/screen.mp4` (31,6 s, 1920x828, 25 fps, piste audio
quasi silencieuse -91 dB — pas de narration native), `assets/intro.jpg`
(`CONNECTER_TON_DOMAINE.jpg`), `assets/outro.jpg` (`page_fin_vid.jpg`, carte CTA
générique déjà réutilisée sur d'autres tutos).

**⚠️ Point à valider avant de continuer** : `assets/intro.jpg` fourni sous le nom
`CONNECTER_TON_DOMAINE.jpg` affiche à l'écran le titre **« Ajouter du contenu PRO »**
+ CTA « Rejoignez-nous », ce qui correspond visuellement au tutoriel **07 Ajouter du
Contenu sur son site** du même module, pas au 08 Domaine. Voir message de présentation.

## Analyse du rush (frames extraites à 1 fps puis 4 fps sur les zones de clic)

| t | Contenu |
|---:|---|
| 0,0-2,8 s | Page "Contenu du site", scroll de la sidebar, survol de "Domaine" |
| ~2,8 s | **clic** sidebar "Domaine" |
| 3,0-17,0 s | Page Domaine vide → saisie progressive « www.gosushi.fr » dans le champ |
| ~17,5 s | **clic zoom-punch** sur "Connecter" (coord. source ≈ 1201, 489) |
| 17,5-19,5 s | Bouton désactivé (spinner/curseur interdit) |
| 19,5-23,0 s | Toast "Domaine enregistré. Créez le CNAME…", statut "En attente de validation DNS…", SSL —, bloc CNAME `www.gosushi.fr CNAME sites.foodeatup.com` |
| ~23,5-24,0 s | **clic zoom-punch** sur "Copier" (coord. source ≈ 502, 607) → toast "CNAME copié" |
| ~27,3 s | **clic zoom-punch** sur "Vérifier maintenant" (coord. source ≈ 534, 710) → toast "Toujours en attente de propagation DNS" |
| 27,5-31,6 s | Toast puis fin du rush |

## Voix off (proposition, 9 lignes, gabarit `foodeatup-tva-tuto`)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Connecter votre nom de domaine à FoodEatUp ? Voici comment faire en quelques secondes. | carte d'intro |
| N1 | Dans l'onglet Domaine de votre site, saisissez votre nom de domaine, par exemple www.gosushi.fr. | saisie du champ |
| N2 | Cliquez sur Connecter pour l'associer à votre boutique FoodEatUp. | **zoom-punch** clic Connecter |
| N3 | FoodEatUp vous donne l'enregistrement CNAME à créer chez votre registrar, comme OVH ou Gandi. | bloc CNAME affiché |
| N4 | Copiez-le et collez-le dans la zone DNS de votre nom de domaine. | **zoom-punch** clic Copier |
| N5 | Cliquez sur Vérifier maintenant : dès que le DNS se propage, votre site est en ligne sur votre propre domaine, avec le SSL activé automatiquement. | **zoom-punch** clic Vérifier maintenant |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | étages 1+2 (reveal + copié) — **réutilisable tel quel depuis `foodeatup-tva-tuto/vo/N6.mp3`, texte identique** |
| N7 | Collez-le dans la conversation : Claude vérifie aussitôt le statut de votre domaine. | étage 3 (mockup chatbot) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) — **réutilisable tel quel depuis n'importe quel tuto déjà livré** |

## Séquence Claude — module partagé

Aucun outil MCP ne permet de *connecter* un domaine (pas d'équivalent à l'action
"Connecter" du rush), mais `mcp__Foodeatup__get_domain_status(establishment_id)`
("Statut du domaine personnalisé - DNS/SSL") correspond exactement à l'action
"Vérifier maintenant" montrée en fin de rush. Prompt proposé :

> Vérifie le statut de mon nom de domaine pour mon établissement FoodEatUp
> (ID [ID établissement]).

Même texte prévu côté fiche Lovable (`claudePrompt`).

## Statut

**Brouillon — en attente de validation du script avant génération ElevenLabs**
(règle `FOODEATUP-TUTORIELS-WORKFLOW.md` §3, STOP obligatoire).
