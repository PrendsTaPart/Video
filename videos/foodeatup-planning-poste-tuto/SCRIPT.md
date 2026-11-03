# Tutoriel — Imprimer son planning par poste FoodEatUp

Module Équipe & Planning. Durée livrée : **45,48 s** — H.264 High/yuv420p,
AAC 48 kHz stéréo, faststart. Audio : true peak **-7,17 dBFS**. Sans avatar
HeyGen.

Rush source (83 s, "Planning équipe") dense : vue par employé/par poste,
création d'un shift (alerte repos minimum RH + masse salariale en direct),
export PDF, modification d'un shift existant, "Tâches de la semaine". Resserré
sur le fil du titre — vue + création + vue par poste + export PDF — modif de
shift et tâches de la semaine laissées de côté (sujets à part, candidats pour
de futurs tutoriels).

## Voix off (8 lignes)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N1 | Le planning équipe affiche les horaires de chaque employé, par personne ou par poste de travail. | 5,09 s | A |
| N2 | Créez un nouveau shift : FoodEatUp vérifie le repos minimum entre deux services et calcule votre masse salariale. | 6,50 s | B |
| N3 | Passez en vue par poste pour voir la charge de travail de la cuisine, la salle ou la livraison. | 5,38 s | C |
| N4 | Cliquez sur Imprimer pour exporter le planning par poste en PDF. | 3,58 s | D1 + clic D2 |
| N5 | Fini les calculs à la main : temps de travail, coût et repos réglementaires sont suivis automatiquement. | 5,85 s | E |
| N6 | Vous pouvez aussi créer un shift depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étages 1+2 (réutilisée) |
| N7 | Collez-le dans la conversation : le shift est ajouté à votre planning en quelques secondes. | 4,62 s | étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (réutilisée) |

N6/N8 réutilisés depuis `foodeatup-qrcode-tuto/vo/`.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,50 s | IMPRIMER SON PLANNING PAR POSTE |
| A | 0,00 → 5,00 | 5,60 s | Planning équipe, bascule Par employé / Par poste |
| B | 5,00 → 33,00 | 7,00 s | Modal Nouveau shift : champs, alerte repos RH, coût (accéléré ×4) |
| C | 43,00 → 50,00 | 5,90 s | Vue Par poste : Livraison/Cuisine/Salle/Plonge |
| D1 | 50,00 → 52,00 | 1,60 s | approche du bouton PDF |
| D2 | 52,00 → 53,50 | 2,40 s | **zoom-punch** sur « PDF » (1352, 375), vue Par poste |
| E | 75,00 → 82,00 | 6,40 s | confirmation (toasts « Enregistré », vue Par poste finale) |
| claude1 | carte générée | 3,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,30 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

Coordonnées mesurées par extraction de frames pleine résolution (1920×828).

## Séquence Claude — module partagé

Seule action du rush avec un équivalent MCP exact : `create_shift(establishment_id,
professional_id, day, start, end, break_minutes, role_label, note)` — la modal
« Nouveau shift » correspond champ pour champ.

> Crée un shift pour [nom de l'employé] le [date], de [heure début] à [heure
> fin], poste [poste], pour mon établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompt`).

## Astuces supplémentaires (Lovable uniquement, pas dans la vidéo)

Demandées explicitement par Michael, `claudePrompts[]` sur la fiche Lovable
(pas d'équivalent visuel dans le rush, donc pas dans le script vidéo) :
- **Ajuster selon l'affluence** — combine `get_daily_brief` (CA, commandes du
  jour) et une proposition d'ajustement du planning.
- **Anticiper les commandes** — `list_top_productions` (plats les plus produits
  sur 30 jours) pour vérifier que le planning couvre les postes les plus
  sollicités.

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'étape (module `banner()` corrigé sur `foodeatup-qrcode-tuto`,
slide-in seul), encadré orange pulsant sur le clic PDF.

## Statut publication

Vidéo à livrer à Michael pour validation avant publication RapidoCMS/
LinkedIn/Lovable. RapidoCMS non autorisé dans cette session — publication
CMS/LinkedIn en attente dans tous les cas.
