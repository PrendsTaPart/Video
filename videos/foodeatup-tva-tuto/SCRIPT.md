# Tutoriel — Paramétrer sa TVA FoodEatUp

Module 1 « CONFIGURATION », dossier Drive `5 - vos taux de TVA`.
Durée livrée : **29,4 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart.
Audio : true peak **-7,2 dBFS** (mesuré sur le MP4 final).

**Première vidéo avec un vrai prompt Claude** — voir §"Séquence Claude" plus bas.

## Voix off

| # | Texte | Durée | Placement |
|---|---|---:|---|
| N0 | Paramétrer votre TVA ne prend que quelques secondes. | 2,59 s | carte d'intro |
| N1 | Cliquez sur Ajouter TVA pour créer un nouveau taux. | 2,95 s | clic Ajouter TVA |
| N2 | Donnez-lui un nom et un pourcentage, puis validez avec Ajouter. | 3,34 s | modal + clic Ajouter |
| N3 | Votre taux de TVA apparaît aussitôt dans la liste. | 2,74 s | liste mise à jour |
| N4 | Pour le modifier, cliquez sur le crayon et ajustez le pourcentage. | 3,76 s | clic crayon + modification |
| N5 | Cliquez sur Sauvegarder pour enregistrer les changements. | 3,00 s | clic Sauvegarder |
| N6 | Vous pouvez aussi créer ce taux de TVA directement avec Claude. | 3,34 s | carte prompt Claude |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA) |

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,6 s | PARAMÉTRER SA TVA FOODEATUP |
| A | 0,20 → 1,40 | 2,00 s | liste vide (« Aucune TVA ») |
| B | 1,40 → 1,55 | 0,90 s | **zoom-punch** sur Ajouter TVA (1708, 351) |
| C | 2,00 → 5,90 | 2,50 s | modal, nom + pourcentage (7) |
| D | 6,30 → 6,55 | 0,90 s | **zoom-punch** sur Ajouter / submit (1204, 602) |
| E | 7,00 → 9,00 | 2,70 s | taux créé, visible dans la liste |
| F | 9,30 → 9,55 | 0,90 s | **zoom-punch** sur le crayon d'édition (1489, 537) |
| G | 10,00 → 14,90 | 2,90 s | modification du pourcentage (7 → 8) |
| H | 15,20 → 15,55 | 0,90 s | **zoom-punch** sur Sauvegarder (1172, 602) |
| I | 16,00 → 18,20 | 2,10 s | taux mis à jour (8%) |
| claude | carte générée | 4,60 s | prompt Claude copier-coller |
| outro | carte | 9,15 s (auto-étendue) | CTA |

## Séquence Claude (nouvelle règle, première application)

`mcp__FoodEatUp__create_tva(establishment_id, name, percentage)` existe — première vidéo
de la série où une vraie correspondance MCP a été trouvée. Ajout d'une carte dédiée avant
l'outro : titre « Utilisez cette fonctionnalité avec Claude » + bloc de code (police
monospace, fond marine, filet orange) avec le prompt copier-coller :

> Crée un taux de TVA nommé [nom du taux] à [pourcentage]% pour mon établissement
> FoodEatUp (ID [ID établissement]).

Même texte utilisé côté site Lovable (`claudePrompt`), pour rester cohérent entre la
vidéo et la fiche tutoriel.

### Deux bugs rencontrés sur cette carte (corrigés)

1. **Ligne du milieu disparue.** Le texte `[pourcentage]% pour mon établissement`
   contient un `%` isolé — `drawtext` l'interprète par défaut comme le début d'un
   token d'expansion `%{...}` et abandonne silencieusement tout le filtre. Corrigé
   avec `expansion=none` sur les drawtext du bloc de code.
2. **Fond crème viré au kaki/taupe.** Un `color=c=0xFCF9E6` (source lavfi) encodé puis
   passé dans la chaîne `xfade` ressortait avec des pixels visiblement plus sombres/
   désaturés que la couleur source. Plutôt que de chasser la cause exacte (conversion
   RGB→YUV probable), la carte est désormais **rendue en PNG statique d'abord**, puis
   passée dans la fonction `card()` déjà éprouvée pour les cartes intro/outro — même
   traitement, donc mêmes couleurs garanties. (Le pixel « décalé » mesuré ensuite lors
   du contrôle correspondait en fait, sans rapport, à la marge floutée assombrie de la
   carte outro — dont l'image source 1281×721 ne remplit pas le cadre 1920×828 —
   comportement voulu, pas un bug.)

## Animations

Mêmes principes que les précédents : Ken Burns sur les cartes, xfade (0,28 s), bandeaux
d'étape, encadré orange pulsant sur les 4 clics. Pas de clip avatar dans ce dossier.
