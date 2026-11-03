# Tutoriel — Sortir un rapport et son historique (FoodEatUp)

Module Statistiques & Rapports (Analytix BI), établissement de test GoSushi
(ID 26). Durée livrée : **44,4 s** — H.264 High/yuv420p, AAC 44,1 kHz mono,
1280x720/30fps.

## Note méthode — rush corrompu

Le screen recording fourni (`Création d'un rapport et Historique des
statistiques par Module.mp4`) n'a que ~4 s de contenu exploitable (écran
Analytix BI figé) ; le reste (~20 s) est un aplat de couleur illisible.
Aucun accès identifiants/URL n'était disponible pour re-filmer le flux réel
au moment de la production, donc la piste visuelle est une scène HTML/CSS
(`scene.html`, animations pilotées par `animation-delay`) rejouant le même
écran Analytix BI réel (capture utilisable du rush) avec curseur, clic,
zoom-punch CSS, et un panneau d'historique + un encadré astuce du chef,
plutôt qu'un montage `build.py` sur rush brut comme les autres tutos de la
série. Capture via Playwright (`record.js`, Chromium headless, fichier
local — pas d'accès réseau nécessaire). Données affichées (session caisse,
factures) : réelles, tirées de `mcp__FoodEatUp__get_pos_report` /
`list_invoices` sur l'établissement GoSushi (ID 26), pas inventées.

**Synchronisation voix off / vidéo** : la piste visuelle vient d'un
enregistrement navigateur (horloge de rendu réelle), pas d'un montage
ffmpeg frame-exact ; le décalage entre le délai CSS nominal et l'instant
réel où chaque scène apparaît à l'écran n'était pas constant (dérive
d'environ 0,4 s à 2,9 s sur la durée totale, horloge d'enregistrement VP8).
Plutôt que de supposer un offset fixe, un marqueur de 9 couleurs (coin
bas-droit, retiré de la version finale de `scene.html`) a été flashé à
chaque frontière de ligne VO puis détecté par balayage image par image du
`.webm` enregistré, pour obtenir l'instant réel de chaque transition. Les 9
offsets mesurés (ms, table ci-dessous) sont ceux utilisés par `mux.sh` —
voir ce fichier pour la commande exacte.

## Voix off (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Offset mesuré | Ancrage |
|---|---|---:|---:|---|
| N0 | Sortir un rapport de caisse et son historique dans FoodEatUp ? Suivez le guide. | 4,31 s | 0,40 s | carte d'intro |
| N1 | Ouvrez le module Analytix BI et choisissez votre période. | 3,34 s | 5,04 s | curseur vers le sélecteur de dates |
| N2 | Cliquez sur Rapport PDF pour générer votre rapport. | 2,95 s | 9,12 s | zoom-punch clic "Rapport PDF" |
| N3 | Chiffre d'affaires, commandes, marge brute, score HACCP : tout est là. | 5,88 s | 12,48 s | highlight séquentiel des 4 cartes stats |
| N4 | Faites défiler pour retrouver l'historique de vos sessions et de vos factures. | 3,79 s | 19,12 s | panneau "Historique des rapports" (données réelles GoSushi) |
| N5 | Clôturez votre caisse chaque soir : votre historique reste fiable, et les écarts sautent aux yeux. | 5,75 s | 23,28 s | encadré astuce du chef |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | 29,56 s | **réutilisé tel quel** depuis `foodeatup-fournisseurs-tuto/vo/N6.mp3` — étages 1+2 |
| N7 | Collez-le dans la conversation : votre rapport de caisse s'affiche en quelques secondes. | 4,21 s | 34,44 s | étage 3 (mockup chatbot) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | 39,04 s | **réutilisé tel quel** depuis `foodeatup-fournisseurs-tuto/vo/N8.mp3` — carte de fin CTA |

N6/N8 copiés directement (mêmes lignes génériques que le reste de la
série, zéro crédit ElevenLabs dépensé). N0-N5 et N7 régénérés pour ce
tutoriel (voix Adam FR, `mcp__ElevenLabs__text_to_speech`, `language_code=fr`).

## Séquence Claude — module partagé

`mcp__FoodEatUp__get_pos_report(establishment_id, session_id?)` — rapport
X/Z de caisse (CA, ticket moyen, par mode, par opérateur, TVA, remises) :
correspond exactement à "sortir un rapport". Prompt utilisé (identique côté
vidéo et côté fiche Lovable, `claudePrompt`) :

> Sors-moi le rapport de caisse de la session en cours, avec le chiffre
> d'affaires, le ticket moyen et la TVA, pour mon établissement FoodEatUp
> (ID [ID établissement]).

Réponse assistant (étage 3, mockup) : "Bien sûr ! Session en cours : 139,10 €
de CA, ticket moyen 34,78 €. Voici le détail complet, mode de paiement par
mode de paiement…" — reprend les vraies données de la session caisse #1 de
GoSushi (`get_pos_report`), pas des chiffres inventés.

Rendu via `videos/_shared/claude_prompt_sequence.py`
(`render_claude_stage1/2/3_png`), 1920x828 natif puis recadré/mis à
l'échelle en 1280x720 (`scale=1670:720,crop=1280:720:195:0`) pour coller au
canevas de cette vidéo.

## Astuce du chef (Lovable) — capacités montrées dans le rush

Contrairement à d'autres tutos, l'astuce du chef ("clôturez votre caisse
chaque soir") correspond directement à ce que montre l'écran (l'historique
de sessions/factures affiché) — pas une capacité cachée non filmée.

## Découpage (scène HTML, voir `scene.html`)

| Scène | Fenêtre (offset mesuré) | Contenu |
|---|---|---|
| intro | 0,40 s → ~5,0 s | carton "SORTIR UN RAPPORT ET SON HISTORIQUE" |
| app (Analytix BI) | ~5,0 s → 29,0 s | curseur → clic Rapport PDF (zoom-punch) → 4 cartes stats en surbrillance → panneau historique (données réelles) → astuce du chef |
| claude1/2/3 | 29,56 s → 39,0 s | reveal prompt (crème) → copié (vert) → mockup chatbot Claude |
| outro | 39,04 s → 44,4 s | carton CTA "Essayez gratuitement dès aujourd'hui !" |

## Statut publication

Livré à Michael pour validation (`SendUserFile`) avant intégration Lovable.
Après retour "publie" : ajout prévu dans
`videos/../foodeatup-guide-star` (workspace Lovable Contact.prendstapart,
projet "FoodEatUp Academy") — tutoriel `sortir-un-rapport-et-son-historique`,
module `comptabilite` (Comptabilité & Achats), champ `claudePrompt` identique
au prompt ci-dessus.
