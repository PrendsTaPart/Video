# Tutoriel — Utiliser nos modeles FoodEatUp (HACCP > Documents)

Rush source : "Retrouver nos templates FoodEatUp" (14,68 s, 1920x828, 25 fps).
Duree livree : **36,04 s** — H.264 High/yuv420p, AAC 48 kHz stereo, faststart.
Audio : true peak **-7,3 dBFS**. Decode 0 erreur.

## Pas de sequence Claude sur cette video

Verifie : `mcp__FoodEatUp__*` n'expose aucun outil pour parcourir/telecharger la
bibliotheque de modeles de documents HACCP prets a l'emploi (le dossier
"Documents" montre a l'ecran est une bibliotheque de fichiers statiques —
`list_employee_documents` concerne les documents administratifs des employes,
`list_site_templates`/`apply_site_template` concernent les templates du site
vitrine, aucun des deux ne correspond). Pas de sequence "Utilisez cette
fonctionnalite avec Claude" sur cette video (regle : ne jamais inventer de
prompt sans outil correspondant — meme principe que `foodeatup-unites-tuto`).

## Carte d'intro fournie sans rush correspondant

Un deuxieme visuel a ete fourni pour ce tour ("RETROUVER MES ETIQUETTES
HISTORIQUE") mais aucun enregistrement d'ecran ne montre cette fonctionnalite
(recherche dans l'historique des etiquettes) — le seul rush fourni
("Retrouver_nos_templates_FoodEatUp.mp4") correspond a l'autre carte fournie
("UTILISER NOS MODELES FOODEATUP", bibliotheque de documents HACCP
predefinis), utilisee ici comme carte d'intro. Un futur tutoriel sur les
etiquettes/historique attendra son propre enregistrement d'ecran.

## Voix off (6 lignes)

| # | Texte | Duree | Ancrage |
|---|---|---:|---|
| N0 | Utiliser nos modeles FoodEatUp : des documents HACCP prets a l'emploi, en quelques clics. | 6,11 s | carte d'intro |
| N1 | Depuis le module HACCP, ouvrez Documents pour acceder a vos modeles. | 4,36 s | scroll grille HACCP + clic Documents |
| N2 | Chaque dossier — Temperatures, Tracabilite, Nettoyage, Controle a reception — contient des fichiers predefinis. | 7,24 s | page Documents, apercu des dossiers |
| N3 | Ouvrez un dossier pour retrouver la liste de vos fiches pratiques et modeles. | 3,79 s | clic dans le dossier Temperatures + liste des fichiers |
| N4 | Telechargez un document en un clic, pret a imprimer ou a remplir. | 3,71 s | clic telechargement + notification + apercu PDF |
| N5 | Passez a la restauration intelligente avec FoodEatUp. Essayez gratuitement des aujourd'hui ! | 5,02 s | carte de fin (CTA, **reutilisee**) |

N5 copiee directement depuis `foodeatup-reception-stock-tuto/vo/N8.mp3` (texte
generique, 0 credit ElevenLabs). N0-N4 generees via ElevenLabs (voix Adam FR,
`TGAegA0zNRi8I6nUdq3i`).

## Piege deja rencontre, evite ici

**Lecture de planches-contact redimensionnees non fiable pour dater des points
de coupe precis** (bug rencontre et corrige sur `foodeatup-reception-stock-tuto`,
reproduit une premiere fois ici : une premiere lecture avait situe le clic sur
la tuile "Documents" vers t=3,8-4,1s alors qu'il a lieu vers t=2,7-2,9s).
Corrige en verifiant chaque point de coupe critique sur des frames en taille
native (1920x828) avant de figer `build.py`, jamais uniquement sur une planche-
contact redimensionnee a 30-40%.

**Segments calibres sur la duree VO des le premier build** (pas en plusieurs
passes cette fois) : chaque groupe de segments associe a une ligne VO a ete
dimensionne avec une marge (duree VO + ~0,3-0,4 s) avant le premier rendu.
Resultat : derive residuelle de 0,29 s (N1) et 0,16 s (N3) seulement, aucune
ligne ne recouvre un autre segment que celui prevu.

## Decoupage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 4,00 s | UTILISER NOS MODELES FOODEATUP |
| A | 0,20 -> 1,20 | 2,80 s | tableau de bord, 4 tuiles visibles |
| B | 1,30 -> 2,70 | 4,00 s | scroll vers la grille complete (8 tuiles), survol Documents |
| C | 2,70 -> 2,95 | 1,30 s | **zoom-punch** clic tuile "Documents" (745,531) |
| D | 3,00 -> 4,90 | 7,60 s | page Documents : dossiers Tracabilite / Temperatures / Nettoyage / Formation / Controle a reception / Journal (tous "Predefini") |
| E | 4,90 -> 5,20 | 1,00 s | clic dans le dossier Temperatures |
| F | 5,50 -> 8,30 | 3,80 s | liste des fichiers (Controle des temperatures, Pratique Hygiene N9-N11) |
| G | 8,35 -> 8,55 | 1,00 s | **zoom-punch** clic telechargement (1650,307) |
| H | 8,60 -> 10,70 | 3,80 s | notification de telechargement |
| I | 11,00 -> 14,68 | 3,00 s | apercu PDF du modele "Controle des temperatures des enceintes refrigerees" |
| outro | carte | ~10,3 s (auto-etendue) | CTA |

Coordonnees des boutons mesurees par seuillage colorimetrique sur les frames
reelles (script Python, pas a l'oeil) — voir `build.py`.

## Animations

Memes principes que toute la serie : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'etape (3), encadre orange pulsant sur les 2 clics. Pas de clip
avatar dans ce dossier.

## Astuce du chef (Lovable)

Les dossiers marques "Predefini" sont fournis prets a l'emploi par FoodEatUp
(grilles de temperature, fiches de bonnes pratiques d'hygiene) — inutile de
les recreer, il suffit de les telecharger et de les afficher en cuisine.

## Statut publication

**Publication demandee explicitement par l'utilisateur des la fin du montage
("publie la video une fois fini").** RapidoCMS : video + vignette uploadees
(`foodeatup-templates-tuto-v1` / `-thumbnail`). Lovable : tutoriel
`utiliser-nos-modeles-foodeatup` ajoute dans `src/data/tutorials.ts`, module
HACCP, sans `claudePrompt` (pas d'outil MCP correspondant).
