# Tutoriel — Retrouver l'historique de ses zones de nettoyage (HACCP)

Module `haccp` (déjà 7 tutoriels publiés : valider-une-production, tracer-ses-productions-historique,
retrouver-lhistorique-des-temperatures, creer-une-tracabilite-simplifiee, declarer-ses-equipements,
ajouter-temperature-plat, relever-une-temperature-equipement). Cette vidéo est la jumelle de
`retrouver-lhistorique-des-temperatures` : même page "historique haccp" (4 cartes : Températures,
Traçabilité, Plan de nettoyage, Production), ici sur la carte **Plan de nettoyage**.

Intrants reçus de Michael le 2026-08-03 :
- `assets/intro.jpg` — carte d'ouverture "RETROUVER MES ZONES HISTORIQUE"
- `assets/outro.jpg` — carte de fin CTA (réutilisation confirmée, md5 identique à tous les tutos précédents)
- `assets/screen.mp4` — écran capturé, 1920x828, 25 fps, **41,32 s**, piste audio silencieuse (-91 dB)

## Déroulé observé dans le rush

| t (rush) | Contenu |
|---:|---|
| 0,0 – 4,6 s | Menu Hygiène : "Liste des zones à nettoyer" (A - Cuisine Quotidien, B - Cuisine Hebdo, C - Zone de Stockage) |
| 4,6 – 7,0 s | Clic sur "Historique" (nav du haut) |
| 7,0 – 7,3 s | Page "historique haccp" : 4 cartes (Températures 0, Traçabilité 0, **Plan de nettoyage 5 actions**, Production 0) — clic sur la carte Plan de nettoyage |
| 7,3 – 13,5 s | Page "Actions de nettoyage" : fil d'Ariane, recherche, "Exporter PDF", 4 compteurs (6 Total, 5 Effectuées, 0 En cours, 1 Reportée), calendrier "Juillet 2026" (vues Mois/Semaines/Jour/Liste), jours avec badges (28→1, 29→4, 31→1) |
| 13,5 – 16,3 s | Clic sur l'action du 28 ("A - Cuisine Quotidien") |
| 16,3 – 19,5 s | Modale "Actes de nettoyage" : Zone, Poste (Inox), Commentaires, Statut **Reporté**, boutons Supprimer/Annuler/Modifier |
| 19,5 – 22,5 s | Statut changé en Effectué → toast "Action mise à jour avec succès", compteurs recalculés (6 Total, **6 Effectuées**, 0 En cours, 0 Reportée) |
| 22,5 – 34,3 s | (Non retenu au montage : réouverture de la même action + consultation d'une 2ᵉ action "Matériel de cuisson" — redondant, coupé pour rester concis) |
| 34,3 – 34,6 s | Clic sur "Exporter PDF" |
| 34,6 – 37,5 s | Téléchargement (popup navigateur) |
| 37,5 – 41,32 s | PDF ouvert : "Rapport Plan de Nettoyage - food Co." — page 1 (100% taux de réalisation, répartition par statut, top zones, actions par utilisateur), page 2 (tableau détaillé Date/Zone/Poste/Utilisateur/Statut/Commentaires) |

## Outil MCP FoodEatUp correspondant

`mcp__FoodEatUp__list_cleaning_actions(establishment_id, date_from?, date_to?, limit?)` — lecture
de l'historique des actions de nettoyage, filtrable par période. Correspond exactement à ce que
montre le rush (page Actions de nettoyage, filtrée par calendrier/période, exportable). Séquence
Claude ajoutée en fin de vidéo (règle du pipeline, template `foodeatup-tva-tuto` réutilisé).

`mcp__FoodEatUp__record_cleaning_action(establishment_id, poste_nettoyage_id, statut?, commentaires?)`
existe aussi (enregistrer une action) — pas montré à l'écran (le rush modifie une action existante,
pas de tool `update_cleaning_action` dans le MCP), mais assez proche pour un 3ᵉ `claudePrompt`
variante "créer", suivant le même patron que `retrouver-lhistorique-des-temperatures` (qui propose
aussi un prompt de création en 3ᵉ position alors que la vidéo ne montre que de la lecture).

Prompt embarqué dans la vidéo (séquence Claude, 1 seul prompt affiché à l'écran) :
> Liste mes actions de nettoyage de la zone [nom de la zone] entre le [date de début] et le
> [date de fin], pour mon établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompts[0]`).

## Voix off (9 lignes) — N6 et N8 réutilisés tels quels (zéro coût ElevenLabs)

| # | Texte | Source |
|---|---|---|
| N0 | Un contrôle sanitaire demain, et vous cherchez qui a nettoyé quoi la semaine dernière ? Voici comment le retrouver en un clic. | généré |
| N1 | Depuis le menu Historique, ouvrez la carte Plan de nettoyage. | généré |
| N2 | Vous retrouvez le total de vos actions, celles effectuées, en cours, ou reportées, avec un calendrier mois par mois. | généré |
| N3 | Cliquez sur une action pour voir son détail : la zone, le poste, et son statut. | généré |
| N4 | Vous pouvez la mettre à jour à tout moment — ici, une action reportée passe en effectuée. | généré |
| N5 | Un clic sur Exporter PDF, et vous obtenez un rapport complet : taux de réalisation, répartition par statut, et détail de chaque action. | généré |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | **réutilisé** (`foodeatup-fournisseurs-tuto/vo/N6.mp3`, md5 identique) |
| N7 | Collez-le dans la conversation : votre historique de nettoyage s'affiche en quelques secondes. | généré (spécifique, jamais réutilisable) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | **réutilisé** (carte de fin CTA, md5 identique sur toute la série) |

## Découpage envisagé (segments retenus, coordonnées mesurées sur les frames extraites)

| Seg | Source (raw) | Contenu |
|---|---|---|
| intro | carte | RETROUVER MES ZONES HISTORIQUE |
| A | 0,00 → 6,80 | Zones à nettoyer (Hygiène) + clic sur Historique |
| B | 6,80 → 7,10 | **zoom-punch** carte "Plan de nettoyage" |
| C | 7,30 → 13,50 | Page Actions de nettoyage : compteurs + calendrier |
| D | 13,50 → 16,10 | **zoom-punch** action du 28 (clic) |
| E | 16,30 → 22,50 | Modale détail + changement de statut + toast succès |
| F | 34,30 → 34,60 | **zoom-punch** "Exporter PDF" |
| G | 37,50 → 41,32 | Rapport PDF ouvert (2 pages) |
| claude1-3 | générées | séquence "Utilisez cette fonctionnalité avec Claude" (module partagé `_shared/claude_prompt_sequence.py`) |
| outro | carte | CTA (réutilisée) |

Portion 22,5→34,3 du rush volontairement coupée (réouverture redondante de la même action + 2ᵉ
action non commentée par le script) pour rester concis.

## Vignette YouTube

Réutilisation directe de `assets/intro.jpg` (pas de redesign), `out/thumbnail-youtube.jpg` recadrée
neutre en 1280x720.

## Statut

Montage terminé : durée livrée **54,24 s** — H.264 High/yuv420p 1920x828, AAC 48 kHz stéréo,
faststart confirmé (`ftyp`→`moov`→`mdat`). Decode 0 erreur. Audio : peak **-7,19 dBFS**. VO
générée pour N0-N5 et N7 (Adam FR, ElevenLabs) ; N6 et N8 réutilisés tels quels (md5 identiques
à `foodeatup-fournisseurs-tuto/vo/`). Aucune extension d'outro nécessaire — le calibrage des
segments sur la durée des lignes VO (retenu suite au correctif fait sur `foodeatup-predibot-tuto`)
a suffi du premier coup (dérive max 1,46 s). Bug rencontré et corrigé pendant le montage : la
légende de bandeau du segment E contenait une apostrophe (« Détail d'une action ») — même bug que
documenté dans `FOODEATUP-TUTORIELS-WORKFLOW.md`, corrigé en reformulant sans apostrophe.
`out/thumbnail-youtube.jpg` = réutilisation neutre de `assets/intro.jpg` (1280x720).

**STOP obligatoire (règle `LOVABLE-FOODEATUP-DOCS.md` §"Règle de validation") : vidéo livrée à
Michael pour validation. Pas de publication (RapidoCMS, LinkedIn, Lovable) tant qu'un retour OK
explicite n'est pas reçu.**
