# Tutoriel — Lire ses Prévisions PrediBot

Troisième vidéo du module **PrediBot (Agent IA Directeur)** (`predibot`, 2/3 déjà publiées :
`predire-ses-commandes` et le tuto "suivre les suggestions de l'agent IA"/Chat PrediBot).
Catalogue cible (`CATALOGUE-157-TUTORIELS.md`, item 11b-01) : **"Lire ses Prévisions PrediBot"**.

Intrants reçus de Michael :
- `assets/intro.jpg` — carte d'ouverture "LIRE SES PRÉVISIONS PREDIBOT" (logo FoodEatUp,
  mascotte pointant vers une icône œil, bouton "REJOIGNEZ-NOUS")
- `assets/outro.jpg` — carte de fin CTA — **réutilisation confirmée** : md5 identique
  (`bd812eb81382fbbcb5303d06101e6538`) à `foodeatup-abonnement-tuto/assets/outro.jpg` et aux
  88 autres tutos qui la réutilisent déjà. Aucun redesign.
- `assets/screen.mp4` — écran capturé, 1920x828, 25 fps, **35,08 s**, piste audio native
  silencieuse (-91 dB) — VO entièrement ElevenLabs, comme le reste de la série.

## Déroulé observé dans le rush (frames extraites toutes les 0,5-2 s, `ffmpeg -ss t -frames:v 1`)

Page "Analyse & prédictions" — tableau de bord intelligent PrediBot (`GoSushi Démo`,
période 06 août - 13 août 2026).

| t (rush) | Contenu |
|---:|---|
| 0,0 – 2,0 s | Dashboard "Analyse & prédictions" — 4 indicateurs : Alertes actives (0), Économies potentielles (34 496 505,3 €), Précision IA (87 %), Actions complétées (0) |
| 2,0 – 4,3 s | Scroll vers les 5 cartes de modules : **Prédictions de stock** (37 produit(s) à risque), **Prévisions de commandes** (37 commande(s) suggérées), **Production recommandée** (12 recette(s)), Conformité HACCP IA (0 %), Prévisions RH (10 employé(s)) |
| 4,3 s | Clic sur la carte **Prédictions de stock** |
| 4,3 – 12,9 s | Page détail : graphique "Consommation VS Stock" (courbe) + encart "Recommandation IA" ("Tous les stocks sont au niveau optimal...") + tableau produit par produit (stock actuel / seuil mini / seuil critique / statut "Non prévue"/"OK") |
| ~13 s | Retour au dashboard, clic sur la carte **Prévisions de commandes** |
| 14,0 – 21,8 s | Page détail : bandeau "PrediBot recommande une commande anticipée pour la semaine du 22 juillet en raison du pic d'activité prévu (+25 %)" + tableau Produit / Fournisseur / Quantité suggérée / Stock actuel / Seuil critique / Dernière commande / bouton "Ajouter" |
| ~22 s | Retour au dashboard, clic sur la carte **Production recommandée** |
| 24,0 – 30,0 s | Page détail : cartes plats avec badge IA ("Recommandation IA : 1 e Portions", "Stock limité pour 3 ingrédients") — Salade César (précision 92 %, historique +14 %), Lasagnes bolognaises (12 portions recommandées, suggestion fournisseur) — boutons "Ajouter à la production" / "Modifier quantité" + tableau "Planification de production" + résumé "Total à produire / Durée estimée / Lancer la production" |
| 30,0 – 35,08 s | Retour au dashboard "Analyse & prédictions" (boucle de fin du rush) |

Rush 100 % lecture (aucune saisie/formulaire) : l'IA calcule ses prévisions, l'utilisateur
navigue et consulte — même nature que `predire-ses-commandes`, élargi ici aux 3 volets
stock / commandes / production du tableau de bord PrediBot (pas de clic sur "Conformité
HACCP IA" ni "Prévisions RH" dans ce rush — hors périmètre de cette vidéo).

## Recherche d'un outil MCP correspondant (règle du pipeline, §3 `LOVABLE-FOODEATUP-DOCS.md`)

Outils `mcp__Foodeatup__*` passés en revue pour un candidat : `list_low_stocks` (stock bas
*actuel*, pas une prédiction IA à venir), `list_production_alerts` (ingrédients manquants sur
production déjà planifiée, pas une recommandation IA de quantité à produire),
`list_top_productions` (historique des plats les plus produits, pas une prévision),
`get_daily_brief` (brief opérationnel du jour, ne calcule aucune prédiction). Aucun ne
reproduit ce que fait PrediBot ici (prédiction de consommation/stock, suggestion de commande
avec seuil, recommandation de production avec % de précision). **Conclusion, cohérente avec
`predire-ses-commandes`** : pas de `claudePrompt`, pas de séquence "Utilisez cette
fonctionnalité avec Claude" en fin de vidéo — pas de prompt inventé.

## Voix off proposée (7 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`) — SOUMISE À VALIDATION,
## AUCUN AUDIO GÉNÉRÉ

| # | Texte | Ancrage |
|---|---|---|
| N0 | Combien allez-vous vendre, produire ou commander cette semaine ? PrediBot vous le dit d'un coup d'œil. | intro / carte |
| N1 | Depuis Analyse et prédictions, retrouvez vos indicateurs clés : alertes, économies potentielles, précision de l'IA. | A (dashboard + scroll cartes) |
| N2 | Cliquez sur Prédictions de stock pour visualiser votre consommation face à vos niveaux de stock. | clic B (zoom-punch) + C (graphique + reco IA) |
| N3 | Sur Prévisions de commandes, PrediBot vous suggère quoi commander, produit par produit, avant la rupture. | clic D (zoom-punch) + E (tableau commandes) |
| N4 | Et sur Production recommandée, l'IA vous conseille les plats à préparer selon l'historique de vos ventes. | clic F (zoom-punch) + G (cartes plats + résumé) |
| N5 | Une vision complète pour anticiper vos besoins, éviter les ruptures et ne produire que le nécessaire. | retour dashboard — bénéfice |
| N6 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA, **réutilisable telle quelle** — voir note ci-dessous) |

Note N6 : réutilisation directe d'un `.mp3` CTA déjà généré sur un tuto précédent (même texte
mot pour mot, ex. `foodeatup-fournisseurs-tuto/vo/N8.mp3`) — pas de nouvel appel ElevenLabs
nécessaire pour cette ligne.

## Découpage envisagé (à affiner au montage — coordonnées de clic à mesurer sur les frames
## réelles du clic, pas estimées à l'œil)

| Seg | Source | Contenu |
|---|---|---|
| intro | carte | LIRE SES PRÉVISIONS PREDIBOT |
| A | 0,0 → 4,3 | Dashboard + scroll 5 cartes modules |
| B | ~4,3 | **zoom-punch** carte "Prédictions de stock" |
| C | 4,3 → 12,9 | Graphique Consommation VS Stock + Recommandation IA |
| D | ~13 | **zoom-punch** carte "Prévisions de commandes" |
| E | 14,0 → 21,8 | Tableau prévisions commandes + bandeau pic d'activité |
| F | ~22 | **zoom-punch** carte "Production recommandée" |
| G | 24,0 → 30,0 | Cartes plats recommandés + planification production |
| outro | carte | CTA (réutilisée) |

Durée cible finale : ~40-50 s une fois les segments calés sur la durée réelle des lignes VO
mesurées après génération (règle `FOODEATUP-TUTORIELS-WORKFLOW.md`).

## Vignette YouTube

Réutilisation directe de `assets/intro.jpg` (pas de redesign), livrable
`out/thumbnail-youtube.jpg` une fois redimensionnée 1280x720 si besoin.

## Statut

Script validé par Michael (« c'est validé »). VO générée (ElevenLabs, voix Adam FR) pour
N0-N5 ; N6 (CTA) réutilisé tel quel depuis `foodeatup-accueil-role-tuto/vo/N8.mp3` (md5
identique aux 82 autres tutos qui le réutilisent déjà). Montage terminé :
`out/foodeatup-predibot-previsions-tuto-v1.mp4` (42,48 s — H.264 High/yuv420p 1920x828, AAC
48 kHz stéréo, faststart confirmé `ftyp`→`moov`→`mdat`, decode 0 erreur, peak audio
**-7,18 dBFS**) + `out/thumbnail-youtube.jpg` (1280x720, réutilisation neutre de
`assets/intro.jpg`, aucun redesign). Vérification visuelle des bandeaux d'étape et des
zoom-punch sur les 3 clics (frames extraites du rendu final) : OK, aucune boîte invisible
(piège `drawbox` documenté dans `FOODEATUP-TUTORIELS-WORKFLOW.md` évité par construction —
bandeau en `drawtext`/`box`, jamais de `drawbox` animé sur `t`).

Ajustement fait pendant le montage : les cibles de segments initiales étaient trop courtes
pour porter les 7 lignes de VO (~41,7 s cumulées) — même piège documenté dans
`FOODEATUP-TUTORIELS-WORKFLOW.md` (« segments trop rapides → outro tenue en silence
exagérément long », outro auto-étendue à 12,3 s dans un premier essai). Corrigé en
recalibrant les cibles des segments A/C/E/G sur la durée réelle des lignes VO qu'ils
portent ; l'outro ne s'étend plus qu'à 7,86 s (contre 6,2 s de base).

Publication demandée explicitement par Michael dans le même tour ("publie la vidéo... FoodEatUp
académy... met à jour le dépôt github") — pas de second STOP de validation post-montage,
conformément à cette instruction directe.
