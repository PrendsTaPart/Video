# Storyboard — Ajouter une température de production (Plats)

Module cible : **HACCP** (1ère vidéo publiée de ce module — 30 attendues au total, voir
`videos/LOVABLE-FOODEATUP-DOCS.md`).

Intrants reçus :
- `assets/intro.jpg` — "SONDER SES PLATS À CŒUR" (carte d'ouverture fournie).
- `assets/outro.jpg` — carte CTA standard, **identique octet pour octet** à celle déjà
  utilisée sur toute la série (`md5sum` confirmé contre `foodeatup-tva-tuto/assets/outro.jpg`).
- `assets/screen.mp4` — 1920×828, 25 fps, 73,88 s. Titre d'origine : "Ajouter les
  températures de ma production ou sélectionner un plat pour Ajouter une température".

## Déroulé reconstitué (frames extraites à 1-2 fps)

Écran : module **Production > Températures**, onglet **Plats** (à côté de "Équipements").
Cartes stats en haut : Total aujourd'hui / Conformes / Alertes / Non conformes.

| t≈ | Action | Détail |
|---:|---|---|
| 0–4s | État initial | Liste vide, "Aucun plats — Commencez par créer votre premier plat". Bouton "+ Ajouter un relevé" (haut droite ET centre). |
| ~4,7s | **Clic** "+ Ajouter un relevé" | Bouton haut-droite, ouvre la modale "Ajouter un relevé". |
| 5–10s | Modale ouverte | Champs : "Sélectionner un plat" (dropdown), "Saisie température" (stepper -/+, défaut 63.0), texte "Recommandé : +63°C minimum", zone "Pièce jointe" (glisser-déposer, PDF/JPG/PNG, 5 Mo max). Lien "+ Ajouter une recette" à droite du dropdown. |
| ~9–11s | **Clic** dropdown → sélection | Choix d'un plat existant : "suchi - haccp_recipe". |
| ~15–21s | Ajustement température | Édition du champ (63.0 → 64.0 dans le rush, revient à 63.0 plus tard) + upload d'une photo justificative ("Recette.png", 71.05 Ko) dans "Pièce jointe" de la modale principale. |
| ~24,5s | **Clic** "+ Ajouter une recette" | Ouvre une seconde modale par-dessus la première : "Nouvelle recette". |
| 26–45s | Formulaire "Nouvelle recette" | Nom du plat ("pizza"), cases Allergène (14 options, ex. Lactose coché), lien "+ Ajouter un ingrédient", "Durée de vie (jours)", "Instructions (optionnel)", "Portions", "Difficulté" (Facile), "Catégorie (optionnel)" (Conserves). Boutons Annuler / Enregistrer. |
| ~55s | **Clic** "Enregistrer" (sous-modale) | Retour à la modale "Ajouter un relevé" : température 63.0, pièce jointe "Recette.png" toujours attachée. |
| ~61s | **Clic** "Enregistrer" (modale principale) | État "Enregistrement…" (bouton désactivé). |
| ~65–66s | Résultat | Modale fermée, retour à la liste : carte "Pizza", vignette plat, badge **63.0°C** en vert, "Heure de contrôle : 14:00", stepper température sur la carte. Stats mises à jour : Total 1 / Conformes 1 / Alertes 0 / Non conformes 0. |
| 71–74s | Fin de rush | Scroll remonté sur l'en-tête (nav Production/Hygiène/Documents/Historique), dernière frame revient sur un état vide ("Aucun plats") — probablement un reset de démo, pas à reproduire dans le montage. |

## Deux chemins montrés (le titre du rush le dit explicitement)

1. **Sélectionner un plat existant** dans le dropdown ("suchi - haccp_recipe").
2. **Créer un nouveau plat à la volée** via "+ Ajouter une recette" (nom, allergènes,
   durée de vie, catégorie) sans quitter le flux d'ajout de température.

Les deux méritent chacun une ligne VO dédiée (voir SCRIPT.md).

## Séquence "Utilisez cette fonctionnalité avec Claude" — PAS APPLICABLE

Vérifié contre la liste `mcp__FoodEatUp__*` :
- `add_temperature` existe mais prend un `equipment_id` — c'est l'onglet **Équipements**
  de cette même page, pas l'onglet **Plats** montré dans ce rush.
- `create_recipe` et `create_dish` existent mais aucun des deux ne couvre les champs vus
  ici (allergènes, durée de vie en jours, pièce jointe photo, "Recommandé : +63°C minimum")
  — c'est un objet "recette HACCP" à part, sans outil MCP correspondant.

Donc, conformément à la règle du pipeline ("si aucun outil MCP ne correspond, ne pas
ajouter cette séquence — pas de prompt inventé"), **pas de séquence chatbot Claude ni de
`claudePrompt` sur cette vidéo.**

## Boutons / coordonnées à affiner en phase montage (build.py)

Coordonnées pixel exactes (espace source 1920×828) à reconfirmer sur les frames haute
résolution au moment du montage, une fois le script validé — non bloquant pour la
validation du script :
- "+ Ajouter un relevé" (haut droite)
- Dropdown "Sélectionner un plat"
- "+ Ajouter une recette"
- "Enregistrer" (sous-modale Nouvelle recette)
- "Enregistrer" (modale principale, submit final)
