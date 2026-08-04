# Tutoriel — Ajouter et paramétrer son plan de nettoyage (Zones) FoodEatUp

Module HACCP, dossier Drive `10- Ajouter ,et paramètrer un plan de nettoyage`.
Rush source : `assets/screen.mp4` (1920×828, 25fps, 57,9 s).
Carte d'ouverture fournie par Michael : `assets/intro.jpg` (« PARAMÉTRER SON NETTOYAGE PLAN & ZONES »).

**STATUT : validée par Michael et publiée le 2026-08-04.** RapidoCMS : vidéo + vignette
uploadées (`foodeatup-nettoyage-tuto-v1` / `foodeatup-nettoyage-tuto-thumbnail`). LinkedIn
FoodEatUp : brouillon #613 créé et programmé le **2026-08-16 07h00** (prochain créneau
libre de la rotation 2/jour, la file est pleine jusqu'au 15/08). Lovable : tutoriel
`parametrer-son-plan-de-nettoyage` ajouté dans `src/data/tutorials.ts`, module HACCP,
sous-catégorie « 10 - Ajouter et paramétrer un plan de nettoyage » (juste après
`pointer-ses-actions-de-nettoyage`, déjà présent côté site — voir note plus bas).

Durée livrée : 40,24 s — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart (moov avant
mdat vérifié). Audio : true peak **-6,95 dBFS**.

## Note — écart entre le suivi local et le site Lovable (2026-08-04)

En ajoutant ce tutoriel, `src/data/tutorials.ts` contenait déjà une entrée
`pointer-ses-actions-de-nettoyage` (module HACCP #11, « Éditer votre plan de nettoyage
chaque jour ») que ce dépôt ne référence nulle part (ni `LOVABLE-FOODEATUP-DOCS.md`, ni
aucun dossier `videos/foodeatup-*`). Le site est donc en avance sur le suivi local — signe
que d'autres tutoriels ont été publiés directement (autre session, ou édition manuelle)
sans repasser par ce dépôt. À rapprocher de la question ouverte sur le total de 157 vidéos :
le vrai décompte est peut-être sur Lovable, pas dans ce repo.

## Découpage final (`build.py`, retimé pour éviter l'extension d'outro)

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 4,75 s | PARAMÉTRER SON NETTOYAGE PLAN & ZONES |
| A | 0,30 → 9,00 | 4,60 s | liste des zones (5 zones existantes) |
| B | 9,00 → 9,30 | 0,90 s | **zoom-punch** sur Ajouter une zone de nettoyage (1591, 43) |
| C | 9,60 → 24,90 | 5,20 s | modal Nom « Cuisine » + Description |
| D | 24,90 → 25,20 | 0,90 s | **zoom-punch** sur Enregistrer (1024, 658) |
| E | 25,30 → 29,00 | 3,80 s | toast « Zone créée avec succès ! » + liste mise à jour |
| F | 29,00 → 57,92 | 5,90 s | modal Date de l'action + Valider + détail des postes |
| claude1 | carte générée | 3,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,30 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA (pas d'extension nécessaire après retiming) |

Offsets VO vérifiés contre les ancrages `S[...]` (0 écart) : N0=0.30 N1=5.20 N2=9.86
N3=13.08 N4=16.30 N5=20.52 N6=25.10 N7=29.74 N8=34.39, voice_end=39.41s. Premier build
(segments non retimés) avait forcé l'outro à s'étendre 6,20→13,03s pour absorber le
décalage VO/visuel — corrigé en allongeant A/C/E/F et l'intro avant de rebuilder (bug
déjà documenté dans `FOODEATUP-TUTORIELS-WORKFLOW.md`, reproduit puis évité ici).

## Déroulé observé dans le rush (analyse frame par frame)

1. `0s–4s` : Production, menu Hygiène ouvert → Checklist Hygiène / **Plan Nettoyage** / Conformité.
2. `~9s` : clic sur « Plan Nettoyage » → « Liste des zones à nettoyer » : 5 zones déjà
   existantes (A - Cuisine Quotidien, B - Cuisine Hebdo, C - Zone de Stockage,
   D - Cuisine Mensuel, E - Zone de Préparation), chacune « 5 postes - Jamais nettoyé ».
3. `~10s` : clic sur **Ajouter une zone de nettoyage** (bouton bleu en haut à droite) →
   modal « Ajouter une zone de nettoyage » (champs Nom / Description).
4. `~14–24s` : saisie Nom = « Cuisine », Description = « Quisine 1 » (texte du rush,
   coquille source — pas reprise dans la narration).
5. `~25s` : clic **Enregistrer** → toast « Zone créée avec succès ! » → la zone « Cuisine »
   apparaît en bas de liste (pagination page 2).
6. `~30s` : ouverture de la fiche de la zone « Cuisine » → modal **« Date de l'action de
   nettoyage »** (Date + Heure, bouton « Maintenant », info : l'action s'applique à tous
   les postes de la zone) → clic **Valider** → toast « Date d'action enregistrée avec succès ! ».
7. `~50–58s` : détail de la zone « Cuisine » (fil d'ariane Accueil > Liste des zones à
   nettoyer > Cuisine) : Poste 1 / Poste 2 / Poste 3, chacun marqué **Récent** avec sa
   dernière action horodatée.

## Outil MCP FoodEatUp correspondant

`mcp__FoodEatUp__create_cleaning_zone(establishment_id, nom_zone, postes[], description)`
— correspond exactement à l'action filmée (création d'une zone avec nom + description).
`record_cleaning_action` / `list_cleaning_actions` existent aussi (postes 6-7 du rush)
mais correspondent au tutoriel Drive suivant, le **11 — « Éditer votre plan de nettoyage
chaque jour avec les actions de votre équipe »** : on ne les met donc pas en avant dans
le `claudePrompt` de cette vidéo-ci (créer une zone), pour rester fidèle au titre du
dossier Drive #10. Ils seront le sujet naturel du prompt Claude du tutoriel #11.

## Voix off — brouillon (9 lignes, à valider avant génération ElevenLabs)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Organiser le nettoyage de votre cuisine sur FoodEatUp ? Un plan clair en quelques clics. | carte d'intro |
| N1 | Depuis Hygiène, ouvrez Plan Nettoyage : vos zones sont déjà listées avec leurs postes. | menu Hygiène → Plan Nettoyage |
| N2 | Cliquez sur Ajouter une zone de nettoyage pour créer la vôtre. | zoom-punch bouton Ajouter |
| N3 | Donnez-lui un nom et une description, puis enregistrez. | modal Nom + Description |
| N4 | Votre zone est créée avec ses postes de nettoyage, prêts à être suivis. | toast succès + liste mise à jour |
| N5 | Marquez une action de nettoyage réalisée en un clic, avec la date et l'heure. | modal Date de l'action + Valider |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | **étage 1+2** (réutilisé depuis tva-tuto) |
| N7 | Collez-le dans la conversation : votre zone de nettoyage est créée en quelques secondes. | **étage 3** (mockup chatbot) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA, réutilisé) |

N6/N8 réutilisables tels quels (copie directe des `.mp3` depuis `foodeatup-tva-tuto/vo/`,
texte générique déjà validé). N7 nomme l'objet créé — toujours régénéré, jamais copié
(leçon du tutoriel fournisseurs).

## Séquence Claude (prompt proposé, à valider en même temps que le script)

> Crée la zone de nettoyage [nom de la zone] avec les postes [poste 1, poste 2, ...]
> pour mon établissement FoodEatUp (ID [ID établissement]).

Même texte prévu côté fiche Lovable (`claudePrompt`).

## À valider par Michael avant de continuer

- [ ] Texte des 9 lignes VO ci-dessus (N0-N8)
- [ ] Prompt Claude proposé
- [ ] Confirmation que le tutoriel s'appelle bien « Ajouter et paramétrer son plan de
      nettoyage (Zones) » et couvre la création de zone uniquement (pas le marquage
      d'action quotidien, réservé au tutoriel Drive #11)
