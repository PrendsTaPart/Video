# Tutoriel — Retrouver mes Plats sondés (historique) — module HACCP

Catalogue : module **Hygiène & HACCP**, item **06 — Retrouver mes Plats sondés (historique)**
(`videos/CATALOGUE-157-TUTORIELS.md`). Carte d'intro fournie : `RETROUVER MES PLATS SONDÉS
HISTORIQUE.jpg` — correspond exactement à cet intitulé catalogue. Carte de fin fournie :
CTA générique FoodEatUp (réutilisable telle quelle, déjà vue sur toute la série).

Rush source : `Historique de mes plats, température de mes production.mp4` — **25,8 s**,
H.264 (Main)/yuv420p, 1920×828, 25 fps, AAC 48kHz stéréo (piste silencieuse, peak -inf dBFS,
pas de voix native). Decode 0 erreur.

## Ce que montre le rush (deux actions liées, même écran de départ)

Le rush couvre deux étapes consécutives — même principe que `foodeatup-mouvement-stock-tuto`
(créer puis consulter) :

1. **Sonder ses plats** (0,0 → 16,3 s) : module `Production > Températures`, onglet
   **Équipements** actif par défaut (1 équipement, "Frigo 5"), clic sur l'onglet **Plats** →
   grille de plats avec badge de température, stepper +/-, heure de contrôle (Pavé de Saumon
   aux Herbes, Tartine au fromage de chèvre et au miel, etc.). Clic **« Enregistrer les
   relevés de température »** → modale de confirmation (« 0 équipement(s) modifié(s), 3
   plat(s) modifié(s) ») → **« Oui, enregistrer ! »** → modale **« Enregistré ! »** → **OK**.
   Retour à la liste : les compteurs se mettent à jour (4 total aujourd'hui, 1 conforme, 3
   non conformes) et les plats non conformes sont marqués.
2. **Retrouver l'historique** (16,3 → 25,8 s) : clic sur **Historique** (nav du haut) → page
   **« historique haccp »** (cartes Températures 340 relevés, Traçabilité, Plan de nettoyage,
   Production, Contrôle à réception, Checklist Hygiène, Étiqueteuse) → clic sur la carte
   **Températures** → tableau de bord Historique > Températures (19911 relevés, 14504
   conformes, 1694 attention, 95 non conformes, 24 équipements, 26 plats), onglet
   **Équipements** actif par défaut (Frigo 1, Frigo 5) → clic sur l'onglet **Plats** → liste
   des plats sondés : température, seuil de conformité (`≥63°C`), badge Conforme/Non
   conforme, date/heure, employé (Soulayma), bouton **Supprimer** par fiche.

## Pas de séquence Claude sur cette vidéo

Vérifié sur le schéma des outils `mcp__FoodEatUp__*` disponibles :
- `add_temperature(establishment_id, equipment_id, temperature, measured_at?)` — nécessite
  un `equipment_id` : couvre uniquement les relevés **équipement** (frigo, congélateur...),
  pas de champ pour un plat/une recette.
- `list_haccp_temperatures(establishment_id, equipment_id?, type?, start_date?, end_date?)`
  — le paramètre `type` est documenté comme **« Type d'équipement »**, et le seul filtre
  d'entité est `equipment_id` : rien ne permet de cibler un plat sondé.

Aucun outil MCP n'expose la lecture ou l'écriture des relevés « Plats » (sonde à cœur) —
seul le volet Équipements est couvert côté MCP. Donc, même principe que sur
`foodeatup-templates-tuto`/`foodeatup-unites-tuto` : **pas de `claudePrompt` inventé**, la
section correspondante reste masquée côté Lovable.

## Voix off (10 lignes) — PROPOSITION, à valider avant génération ElevenLabs

| # | Texte | Ancrage |
|---|---|---|
| N0 | Vos plats sondés à cœur : température, conformité, tout se retrouve en un clic dans FoodEatUp. | carte d'intro |
| N1 | Depuis Production, ouvrez Températures puis l'onglet Plats pour saisir vos relevés du jour. | clic onglet Plats |
| N2 | Ajustez la température sondée de chaque plat, un par un. | scroll grille des plats |
| N3 | Un clic sur Enregistrer, une confirmation, et vos relevés sont sauvegardés. | clic Enregistrer + Oui, enregistrer |
| N4 | Les plats non conformes sont aussitôt signalés, pour réagir sans attendre. | Enregistré/OK + liste mise à jour |
| N5 | Direction Historique, pour retrouver tous vos relevés HACCP au même endroit. | clic nav Historique |
| N6 | Ouvrez la carte Températures, puis basculez sur l'onglet Plats. | clic carte Températures + clic onglet Plats (historique) |
| N7 | Température, seuil de conformité, date et employé : chaque plat sondé garde sa fiche complète, à supprimer si besoin. | scroll liste historique des plats |
| N8 | De quoi prouver votre suivi HACCP en un coup d'œil, à tout moment. | bénéfice (même écran) |
| N9 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA, réutilisable, 0 crédit ElevenLabs) |

Voix Adam FR (`TGAegA0zNRi8I6nUdq3i`, `eleven_multilingual_v2`), ton chef qui explique à un
confrère — identique au reste de la série. N9 sera copiée telle quelle depuis un tuto
existant (texte CTA identique) plutôt que régénérée.

## Découpage prévu (segments source → cible, avant calibrage fin sur durée VO réelle)

| Seg | Source | Contenu | Zoom-punch |
|---|---|---|---|
| intro | carte | RETROUVER MES PLATS SONDÉS HISTORIQUE | — |
| A | 0,00 → 2,95 | Températures, onglet Équipements (Frigo 5) | — |
| clic1 | 2,95 → 3,30 | clic onglet **Plats** | (329, 147) |
| B | 3,30 → 11,00 | grille des plats, ajustement température | — |
| clic2 | 11,00 → 11,30 | clic **Enregistrer les relevés de température** | (1595, 753) |
| C | 11,30 → 11,90 | modale « Enregistrer les relevés ? » | — |
| clic3 | 11,90 → 12,20 | clic **Oui, enregistrer !** | (872, 608) |
| D | 12,20 → 13,60 | modale **Enregistré !** | — |
| clic4 | 13,60 → 13,90 | clic **OK** | (961, 595) |
| E | 13,90 → 16,30 | retour liste, compteurs + non-conformes | — |
| clic5 | 16,30 → 16,60 | clic nav **Historique** | (1390, 138) |
| F | 16,60 → 17,00 | page « historique haccp » (cartes modules) | — |
| clic6 | 17,00 → 17,30 | clic carte **Températures** | (342, 650) |
| G | 17,30 → 19,30 | Historique > Températures, onglet Équipements | — |
| clic7 | 19,30 → 19,65 | clic onglet **Plats** | (335, 311) |
| H | 19,65 → 25,80 | liste historique des plats sondés (scroll) | — |
| outro | carte | CTA FoodEatUp | — |

7 zoom-punches, coordonnées mesurées visuellement sur les frames extraites (`work/hi/`,
1920×828 natif) — à revérifier par seuillage colorimétrique avant le premier rendu, comme
sur le reste de la série. Durées cible de chaque segment à calibrer sur la VO réelle une
fois les lignes N0-N9 générées (règle du pipeline : mesurer d'abord, dimensionner ensuite).

## Astuce du chef (Lovable)

Un plat non conforme reste visible et modifiable jusqu'à l'enregistrement suivant : ajustez
la sonde, resaisissez la température, et le badge repasse au vert — pas besoin de tout
ressaisir depuis le début.

## howItWorks / whatItsFor (Lovable, brouillon)

- **howItWorks** :
  1. Depuis Production > Températures, ouvrez l'onglet Plats.
  2. Ajustez la température sondée de chaque plat et cliquez sur Enregistrer.
  3. Confirmez l'enregistrement des relevés.
  4. Depuis Historique > Températures, basculez sur l'onglet Plats pour retrouver tout
     l'historique (température, conformité, date, employé), avec suppression possible.
- **whatItsFor** : Prouver votre suivi HACCP sur la température à cœur de vos plats, en
  gardant une trace datée et attribuée de chaque contrôle, consultable et corrigeable à
  tout moment.

## Statut

**Script en attente de validation — STOP obligatoire avant génération ElevenLabs et montage**
(règle `videos/FOODEATUP-TUTORIELS-WORKFLOW.md`, étape 3). Ne pas générer les .mp3 ni lancer
`build.py` avant retour explicite.
