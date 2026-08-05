# Tutoriel — Retrouver mes plats sondés (historique)

Module **Hygiène & HACCP**, catalogue `videos/CATALOGUE-157-TUTORIELS.md` module 10,
entrée 06 : « Retrouver mes **Plats sondés** (historique) » (juste après 05 « Sonder ses
**Plats** à cœur » et 04 « Retrouver mes **Relevés** (historique) », déjà publiée sous
`foodeatup-historique-temperature-tuto` / slug `relever-une-temperature-equipement`).

Rush fourni par Michael (`assets/screen.mp4`, 1920x828, 25 fps, **25,80 s**, H.264/AAC,
piste audio native silencieuse — voix off 100% ElevenLabs comme le reste de la série).

## Ce que montre le rush

1. **0,00 → ~4,00 s** — Production > Températures, onglet **Équipements** (contexte),
   bascule vers l'onglet **Plats** : cartes de plats sondés à cœur (Pavé de Saumon aux
   Herbes, Tartine au fromage de chèvre et au miel...) avec stepper +/- de température.
2. **~4,00 → ~10,00 s** — Ajustement de la température à cœur de plusieurs plats
   (steppers +), heure de contrôle affichée par plat.
3. **~10,00 → ~14,00 s** — Clic **« Enregistrer les relevés de température »** → modale
   de confirmation *« Enregistrer les relevés ? 0 équipement(s) modifié(s), 3 plat(s)
   modifié(s) »* → **« Oui, enregistrer ! »** → modale succès *« Enregistré ! Les relevés
   ont été sauvegardés avec succès. »* (KPIs mis à jour : 4 total / 1 conforme / 3 non
   conformes).
4. **~16,00 → ~18,00 s** — Clic sur **Historique** (nav du haut) → page **Historique >
   Températures** : barre de recherche, filtre **Tous les statuts**, filtre **Date**,
   bouton **Exporter CSV**, 6 indicateurs (**19911** Total relevés, **14504** Conformes,
   **1694** Attention, **95** Non conformes, **24** Équipements, **26** Plats).
5. **~18,00 → 25,80 s** — Bascule sur l'onglet **Plats** : liste des plats sondés
   historiques, chacun avec badge **Conforme/Non conforme**, température relevée, seuil
   (**≥ 63°C**), date/heure du contrôle (28/07/2026 14:20), agent (**Soulayma**), bouton
   **Supprimer**.

## Voix off (9 lignes) — brouillon, en attente de validation Michael

| # | Texte | Segment |
|---|---|---|
| N0 | Retrouvez l'historique de tous vos plats sondés à cœur, en un coup d'œil. | intro |
| N1 | Depuis Production, onglet Plats, enregistrez la température à cœur de chaque plat, puis validez. | A — onglet Plats + saisie |
| N2 | Direction Historique pour retrouver tous vos relevés passés. | clic nav Historique |
| N3 | Total des relevés, conformes, non conformes : tout est compté automatiquement, plats et équipements confondus. | C — KPIs |
| N4 | Basculez sur Plats pour voir chaque sonde à cœur : température, seuil, date et responsable. | D — bascule + liste |
| N5 | Recherchez, filtrez par date et exportez en CSV pour votre suivi HACCP. | E — outils (recherche/filtre/export) |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | claude1+2 (réutilisable depuis un tuto existant) |
| N7 | Collez-le dans la conversation : l'historique de vos plats sondés s'affiche aussitôt. | claude3 (spécifique, jamais réutilisée) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin CTA (réutilisable depuis un tuto existant) |

Voix Adam FR — Instructor (`TGAegA0zNRi8I6nUdq3i`, `eleven_multilingual_v2`), comme
l'ensemble de la série FoodEatUp. N6/N8 candidats à la réutilisation telle quelle depuis
`foodeatup-tva-tuto/vo/` (texte identique) pour économiser 2 générations ElevenLabs.

## Séquence Claude — module partagé

Outil le plus proche : `list_haccp_temperatures(establishment_id, equipment_id?, type?,
start_date?, end_date?)` — même outil que la vidéo sœur `foodeatup-historique-temperature-
tuto` (Équipements). Utilisé ici **sans `equipment_id`**, sur une période, pour retrouver
les relevés côté plats.

> Liste l'historique de mes plats sondés (température à cœur) entre le [date de début] et
> le [date de fin], pour mon établissement FoodEatUp (ID [ID établissement]).

**Point à confirmer avec Michael avant de générer la VO/monter** : la description de
l'outil MCP mentionne un filtre `type` documenté comme « type d'**équipement** » — pas de
filtre dédié « plat » explicite. Le rush montre bien un total unifié (relevés
équipements + plats dans les mêmes compteurs), ce qui suggère un stockage commun, mais ce
n'est pas garanti par la doc de l'outil seule. Si Michael confirme que l'outil couvre
aussi les plats, on garde ce prompt tel quel ; sinon, on retire la séquence Claude
(règle du pipeline : pas de prompt inventé).

## Découpage prévu (à affiner au montage)

| Seg | Source | Contenu |
|---|---|---|
| intro | carte (fournie par Michael) | RETROUVER MES PLATS SONDÉS HISTORIQUE |
| A | 0,00 → ~10,00 | onglet Plats, ajustement des températures à cœur |
| clic+modales | ~10,00 → ~14,00 | Enregistrer → confirmation → succès (zoom-punch sur le bouton) |
| B | ~16,00 → 18,00 | clic nav Historique |
| C | ~18,00 → ~20,00 | Historique > Températures : 6 KPIs |
| D | ~20,00 → ~22,50 | bascule onglet Plats + liste des plats sondés (badges conforme/non conforme, seuil) |
| E | ~22,50 → 25,80 | recherche / filtre Date / Exporter CSV (survol) |
| claude1 | carte générée | reveal — prompt en gros, fond crème |
| claude2 | carte générée | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | mockup chatbot Claude |
| outro | carte (fournie par Michael, CTA générique réutilisée) | CTA |

## Assets reçus

- `assets/intro.jpg` — carte "RETROUVER MES PLATS SONDÉS HISTORIQUE" (fournie).
- `assets/outro.jpg` — carte CTA générique FoodEatUp (identique pixel pour pixel à celle
  déjà utilisée sur toute la série — même hash MD5 `bd812eb8...`, zéro travail de design).
- `assets/screen.mp4` — rush 1920x828, 25 fps, 25,80 s.

## Statut

**Script validé par Michael.** VO générée (ElevenLabs Adam FR Instructor pour N0-N5/N7 ;
N6/N8 réutilisées telles quelles depuis `foodeatup-tva-tuto/vo/`, texte identique).

**Montage terminé** — `out/foodeatup-plats-sondes-historique-tuto-v1.mp4`, **56,48 s**,
H.264 High/yuv420p, 1920×828, 25 fps, AAC 48 kHz stéréo, +faststart (moov avant mdat
confirmé), decode 0 erreur. Peak audio **-7,12 dBFS** (marge saine sous le limiteur
`alimiter=0.6`, ~-4,4 dBFS). Bandeaux d'étape avec le correctif `drawtext` double-passage
(pas `drawbox`, cf. bug documenté plus haut dans `FOODEATUP-TUTORIELS-WORKFLOW.md`) —
vérifiés visibles sur chaque segment par extraction de frames. Zoom-punch vérifié sur le
bouton "Enregistrer les relevés de température". Séquence Claude vérifiée avec accents
français corrects (un premier rendu avait perdu les accents, corrigé avant livraison).
Chaque ligne VO vérifiée dans la fenêtre de son segment visuel (script de vérification
dédié, aucun dépassement). Vignette `out/thumbnail-youtube.jpg` (1280×720, crop neutre de
la carte d'intro, pas de redesign).

Publication lancée sur instruction explicite de Michael ("continue le montage vidéo et
ajoute à lovable"), sans repasser par la livraison-validation intermédiaire (précédent
déjà appliqué sur `saisir-un-mouvement-de-stock`, voir `LOVABLE-FOODEATUP-DOCS.md`).
