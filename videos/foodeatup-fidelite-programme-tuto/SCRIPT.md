# Tutoriel — Booster la fidélité, le programme (module Marketing, Fidélité & Iris)

Deuxième vidéo publiée du module `marketing-fidelite`, section "Fidélité & récompenses"
(placeholder existant `booster-la-fidelite-programme`, order 12). Intrants fournis par
Michael : `BOOSTER_LA_FIDÉLITÉ.jpg` (intro), `Créer un programme fidélité.mp4` (rush,
1920x828, 25fps, 28,76 s, piste audio native silencieuse à -91 dB — VO entièrement
ElevenLabs), `page_fin_vid..jpg` (outro CTA générique, réutilisée telle quelle).

## Déroulé observé dans le rush

| t≈ | Écran |
|---|---|
| 0-3,5s | Page **Fidélité & jeux** : KPI (Membres fidélité 4, Points en circulation 15, Points distribués 25, Bons à valider 0), onglets (Programme/Récompenses/Roue cadeaux/Sondages/Post-commande), section **Programme de fidélité** (toggle Actif) |
| 3,5-7s | **1 · Mode de gain** : essai rapide des 3 options (Par euro dépensé, Par passage, Hybride), réglage final sur **Par passage — 10 pts/commande** (Points par passage = 10) |
| 7-13s | **2 · Multiplicateurs jours creux** (anti-mardi-vide) : clic « Ajouter un créneau », jours **Mar + Mer** sélectionnés, De **11:00 AM** à **02:30 PM**, Multiplicateur **2**, Libellé « Points doublés » |
| 13-19s | Édition du libellé en **« Points doublés midi »** ; en dessous, **3 · Règles** apparaît (Validité des points, Plafond de points/commande) |
| 19-22,2s | Validité des points : **Illimitée → 12 mois glissants** ; Plafond de points/commande : **Aucun → 200** ; case « Crédité même avec un code promo » cochée |
| 22,2s | Clic **« Enregistrer le programme »** |
| 22,2-25s | Bandeau noir : **« Programme enregistré ✓ »** |
| 25-28,76s | Retour en haut de page, tableau de bord avec le programme actif |

Coordonnées mesurées sur les frames réelles (`ffmpeg -ss t -frames:v 1`, puis fenêtres 5 fps
autour du clic pour pointer le timestamp exact), natif 1920x828 :
`BTN_ENREGISTRER = (789, 671)` (« Enregistrer le programme »).

## Voix off (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Segment |
|---|---|---|
| N0 | Booster la fidélité de vos clients avec FoodEatUp ? Configurez votre programme en quelques clics. | intro + A |
| N1 | Depuis Fidélité et jeux, retrouvez vos membres, vos points en circulation et vos bons à valider. | A |
| N2 | Choisissez le mode de gain : par euro dépensé, par passage, ou hybride - ici 10 points par passage. | B |
| N3 | Ajoutez des créneaux multiplicateurs pour booster vos jours creux, par exemple le mardi et mercredi entre 11h et 14h30. | C |
| N4 | Définissez la validité des points et un plafond par commande pour garder le programme maîtrisé. | D |
| N5 | Cliquez sur Enregistrer le programme : la configuration est active immédiatement. | clic E + F |
| N6 | Vous pouvez aussi configurer votre programme de fidélité depuis Claude : copiez ce prompt, remplacez les crochets. | claude1+2 |
| N7 | Collez-le dans la conversation : votre programme de fidélité est mis à jour aussitôt. | claude3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) — réutilisée depuis `foodeatup-nettoyage-ia-tuto/vo/N5.mp3` |

## Séquence Claude — module partagé

Outil correspondant à l'action montrée à l'écran : `mcp__Foodeatup__update_loyalty_program
(establishment_id, earn_mode, visit_points, points_validity_months, active)` — couvre le
mode de gain (par passage), les points par passage et la validité des points. Les
multiplicateurs jours creux et le plafond de points/commande sont des réglages UI sans
équivalent MCP (schéma vérifié : `active`, `earn_mode`, `earn_rate`, `points_validity_months`,
`visit_points` seulement) — non mentionnés dans le prompt, conformément à la règle du
pipeline.

> Configure mon programme de fidélité FoodEatUp (ID [ID établissement]) en mode par
> passage : [X] points par passage, points valables [Y] mois, programme actif.

## Animations

Mêmes principes que toute la série : `setpts` pour la vitesse (jamais `zoompan` sur la
vidéo réelle — ici plusieurs segments tournent en ralenti car le rush (28,76 s) est plus
court que le script VO, un cas classique documenté dans `FOODEATUP-TUTORIELS-WORKFLOW.md`),
zoom-punch sur le clic « Enregistrer » (1,00 s — pas 0,35 s : un test à 0,35 s a produit un
artefact visuel, deux xfade de 0,28 s de part et d'autre se chevauchant presque entièrement
sur un segment aussi court, corrigé en portant le segment à 1,00 s), bandeaux d'étape en
deux `drawtext` (plate = `box=1`), xfade 0,28 s partout, cartes intro/outro en fond flou +
overlay net. Pas de clip avatar. Séquence "Utilisez cette fonctionnalité avec Claude" en 3
temps, module partagé `videos/_shared/claude_prompt_sequence.py`, étages allongés
(4,30 / 2,40 / 5,15 s) car N6 et N7 sont plus longues que la moyenne de la série.

**Dérive corrigée avant livraison** : un premier montage dimensionnait les segments trop
courts par rapport au script (9 lignes, contenu dense) — la narration dérivait jusqu'à 7,7 s
par rapport à son ancrage visuel (ex : la ligne décrivant le multiplicateur jours creux
jouait pendant le segment "Règles"). Corrigé en recalculant chaque durée de segment sur les
offsets réels de la première passe (`build.py` imprime `offsets`/`stage starts`) plutôt que
sur une estimation a priori — dérive résiduelle sous 0,5 s partout après correction.

## Fiche Lovable

- **slug** : `booster-la-fidelite-programme` — placeholder déjà existant dans le scaffold
  du module (order 12, section "Fidélité & récompenses"), rempli avec le contenu complet.
- **title** : Booster la fidélité — le programme
- **moduleSlug** : `marketing-fidelite`
- **subcategory** : 12 · Fidélité & récompenses
- **whatItsFor** : Configurer votre programme de fidélité FoodEatUp de A à Z — mode de gain
  (par euro, par passage ou hybride), multiplicateurs pour booster les jours creux, validité
  des points et plafond par commande — pour transformer vos clients réguliers en habitués.
- **howItWorks** :
  1. Ouvrez Fidélité & jeux puis l'onglet Programme.
  2. Choisissez le mode de gain (par euro dépensé, par passage, ou hybride) et son taux.
  3. Ajoutez un créneau multiplicateur pour booster un jour ou un horaire creux.
  4. Définissez la validité des points et un plafond de points par commande.
  5. Cliquez sur Enregistrer le programme : la configuration est active immédiatement.
- **chefTip** : Utilisez les multiplicateurs jours creux pour cibler précisément vos heures
  mortes (comme le mardi ou mercredi midi) plutôt que d'augmenter le taux de gain partout :
  vous boostez la fréquentation là où vous en avez besoin, sans gonfler le coût du programme
  sur vos heures déjà pleines.
- **chefTipAvatar** : `michael-chef-mascot.jpg`
- **claudePrompt** : voir prompt ci-dessus (`update_loyalty_program`)

## Statut

Vidéo montée, VO générée et publiée à la demande de Michael (workflow complet demandé dans
le même message : montage, VO ElevenLabs, publication Lovable FoodEatUp Academy, mise à
jour du dépôt, ajout du thumbnail). Publication limitée à Lovable + dépôt GitHub, comme
demandé — pas d'upload RapidoCMS ni de programmation LinkedIn dans cette tâche. Placeholder
existant rempli directement (slug déjà connu depuis la production précédente), pas de
doublon créé cette fois.
