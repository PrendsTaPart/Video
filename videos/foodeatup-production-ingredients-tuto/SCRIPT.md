# Tutoriel — Détails et impression de la liste des ingrédients de production

Module StockVision AI, sous-catégorie « 2 - détails et impression de la liste des
ingrédients ». Durée livrée : **52,1 s** — H.264 High/yuv420p 1920×828, AAC LC
48 kHz stéréo, faststart confirmé (moov avant mdat), 0 erreur de décodage.
Audio : true peak **−7,3 dBFS** (sous le plafond cible du pipeline).

Rush source : 56,2 s, 1920×828, 25 fps.

## Voix off (10 lignes, Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Imprimer la liste des ingrédients d'une production dans FoodEatUp ? C'est immédiat. | 4,21 s | carte intro (déborde sur A) |
| N1 | Depuis Mes productions, ouvrez le détail d'une production avec Voir les ingrédients. | 4,13 s | A → se termine sur le clic B |
| N2 | Chaque ingrédient affiche la quantité nécessaire, le stock actuel et son statut, avec sa traçabilité à compléter. | 6,53 s | C + D |
| N3 | Ajoutez la photo de la DLC, directement depuis la caméra ou vos fichiers. | 4,44 s | E |
| N4 | Renseignez la quantité, la date limite, le numéro de lot et vos remarques. | 4,08 s | F |
| N5 | Puis cliquez sur PDF pour générer la liste des ingrédients. | 3,19 s | G + clic H |
| N6 | Exportez-la, puis imprimez-la : votre équipe a la fiche complète en cuisine. | 4,41 s | I + clic J + K |
| N7 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étages 1+2 (réutilisé de `tva`) |
| N8 | Collez-le dans la conversation : votre liste d'ingrédients arrive en quelques secondes. | 4,41 s | étage 3 |
| N9 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé de `tva`) |

N7/N9 repris tels quels de `foodeatup-tva-tuto/vo/` (N6/N8 là-bas) — textes relus
avant réutilisation, ils ne nomment aucun objet propre à ce tutoriel.

**Deux lignes fusionnées en cours d'écriture** (règle « mesurer la VO avant de
figer les durées ») : une première version séparait « cliquez sur Voir les
ingrédients » de la description de la liste, et « colonne Action » de la lecture
du tableau. Le rush ne consacre que 1,3 s au tableau seul et 1,1 s au menu Action :
garder 12 lignes imposait des ralentis à 0,25× et faisait dériver la narration de
~2,5 s à chaque étage (le bug documenté sur `tva` v2). Fusionnées → **drift nul**
sur toutes les lignes sauf N1 (+1,61 s, volontaire : elle enchaîne sur N0).

## Découpage

| Seg | Source | Sortie | Facteur | Contenu |
|---|---|---:|---:|---|
| intro | carte | 3,20 s | — | IMPRIMER SES INGRÉDIENTS DE PRODUCTION |
| A | 0,60 → 6,30 | 6,28 s | 0,90× | Mes productions : recherche, compteurs (38 / 7 / 9 / 13), cartes Plateau Découverte |
| B | 6,60 → 7,05 | 0,96 s | 0,50× | **zoom-punch** sur Voir les ingrédients (301, 449) |
| C | 7,20 → 8,70 | 3,96 s | 0,38× | tableau : ingrédient, qté nécessaire, stock actuel, statut, traçabilité |
| D | 8,70 → 10,60 | 3,56 s | 0,53× | menu Action : Photo DLC (Requis), étiquette HACCP, Scanner produit |
| E | 10,60 → 17,50 | 5,12 s | 1,35× | fiche traçabilité Saumon frais : photo de la DLC importée |
| F | 17,50 → 32,50 | 4,80 s | 3,13× | quantité 3000 g, DLC 22/08/2026, n° de lot 40, remarques |
| G | 37,20 → 43,20 | 3,24 s | 1,85× | retour au tableau + en-tête du modal (Étiquettes / PDF / Valider la production) |
| H | 43,20 → 43,60 | 0,92 s | 0,44× | **zoom-punch** sur PDF (1265, 139) |
| I | 44,70 → 48,00 | 3,28 s | 1,01× | page imprimable « FOODEATUP — Liste d'ingrédients » |
| J | 50,30 → 50,70 | 0,92 s | 0,44× | **zoom-punch** sur Exporter PDF (1800, 72), **zoom 1,45×** |
| K | 51,40 → 56,10 | 3,20 s | 1,47× | visionneuse PDF : ingredients-Plateau-Découverte.pdf |
| claude1 | carte générée | 3,00 s | — | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,32 s | — | « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,32 s | — | mockup chatbot Claude |
| outro | carte | 6,20 s | — | CTA |

Bandeaux d'étape : 1 · Vos productions planifiees — 2 · Quantite, stock et statut —
3 · Completez la tracabilite — 4 · Photo de la DLC — 5 · Quantite, DLC et lot —
6 · Imprimez votre liste — 7 · La liste generee.

### Deux particularités du rush

- **La fiche de traçabilité est remplie puis annulée** dans l'enregistrement (le
  clic final est sur *Annuler*, la ligne reste « À compléter » à l'écran ensuite).
  Le montage s'arrête donc sur le formulaire rempli et **aucune ligne VO ne
  prétend que la fiche a été validée** — N3/N4 décrivent la saisie, pas sa
  validation.
- **Un toast McAfee WebAdvisor** (extension navigateur, sans rapport avec le
  produit) apparaît en bas à droite à partir de ~48 s, source y ≥ 640. D'où :
  segment I coupé à 48,00 s, et punch J en **zoom 1,45×** au lieu de 1,20× pour
  que sa fenêtre de crop (x 596-1920, y 0-571) s'arrête au-dessus du toast. K ne
  démarre qu'une fois la visionneuse PDF plein écran, qui le recouvre.

## Séquence Claude — module partagé

Outil correspondant : `get_production_ingredients(establishment_id, production_id)`
— exactement ce que montre la vidéo (la liste des ingrédients d'une production avec
quantité nécessaire et statut de stock).

> Donne-moi la liste des ingrédients de ma production [nom de la production] du
> [date], avec les quantités nécessaires et le stock disponible, pour mon
> établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompt`). Réponse de l'assistant sur l'étage 3 :
« Bien sûr ! Voici la liste des ingrédients de votre production… ».

## Correctif moteur apporté sur ce build (à reprendre sur les prochains)

**Les bandeaux d'étape ne s'affichaient pas** — seul leur texte apparaissait, en
blanc sur la page, illisible sur une UI claire. Cause : `banner()` dessinait le
filet orange et la plaque bleue avec deux `drawbox` dont le `x` était une
expression de `t` (glissement latéral). **`drawbox` (ffmpeg 6.1) n'évalue x/y/w/h
qu'une seule fois, à la configuration du filtre**, donc à `t=0` — où l'expression
de glissement vaut encore `x=-640`, hors champ. Les deux boîtes n'étaient jamais
dessinées ; seul `drawtext`, lui, réévalue bien son `x` à chaque frame, d'où le
texte nu qui glissait sur un fond absent.

Correctif : le bandeau complet (filet + plaque + texte) est rendu **une fois en
PNG RGBA avec PIL** (`render_banner_png`), puis glissé avec `overlay` qui, lui,
honore `eval=frame`. Deux points à ne pas oublier en le reprenant :

- `overlay` doit recevoir **`shortest=1`** : le PNG est une entrée `-loop 1`
  infinie, sans quoi l'encodage ne s'arrête jamais à la fin du segment (rencontré
  sur ce build, ffmpeg tournait toujours après 10 minutes).
- `punch_highlight()` a été passé en **géométrie statique** pour la même raison :
  son pulse `6*sin(2*PI*t*2.2)` était figé à sa valeur t=0 de toute façon. Sur
  0,9 s de punch, un cadre fixe est de toute façon plus lisible qu'un pulse.

Ce correctif vaut pour toute la série : les tutoriels déjà publiés ont le même
défaut de bandeau et gagneraient à être re-rendus avec ce `build.py` comme base.

## Statut

Vidéo livrée à Michael + fiche publiée sur le site Lovable (module StockVision AI).
Pas de publication RapidoCMS/LinkedIn sur ce tutoriel (non demandée).
