# Tutoriel — Relever une température d'équipement FoodEatUp

Module **HACCP**, sous-catégorie proposée : **« Relevé des températures des équipements »**
(à confirmer/corriger si le sous-dossier Drive porte un autre intitulé exact).

Source : `assets/screen.mp4` (1920×828, 25fps, 20,68s) — page **Production > Températures**.

## Déroulé observé (frames extraites à 2fps)

1. Page « Températures » : compteurs du jour (Total, Conformes, Alertes, Non conformes) à 0,
   tableau des équipements de froid — Frigo 5 (min 0°C/max 4°C) à 6,0°C, Frigo 1 (min 0°C/max
   4°C) à 13,0°C.
2. Ajustement de la température de Frigo 5 via les boutons **+**/**−** : 6,0°C → 9,0°C
   (simule la lecture du thermomètre du jour).
3. Clic sur le bouton vert **« Enregistrer les relevés de température »**.
4. Modal de confirmation « Enregistrer les relevés ? — 1 équipement(s) modifié(s) » → clic
   **« Oui, enregistrer ! »**.
5. Modal de succès « Enregistré ! Les relevés ont été sauvegardés avec succès. » → **OK**.
6. Retour à la liste : compteurs mis à jour automatiquement — **1 Total aujourd'hui**,
   **1 Non conforme** (9°C > 4°C max détecté sans action supplémentaire de l'utilisateur).

Ce dernier point (détection auto de non-conformité) est le bénéfice pédagogique fort de la
vidéo — bon candidat pour la ligne N4 (bénéfice) et l'« astuce du chef ».

## Voix off proposée (7 lignes + séquence Claude, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Relever la température d'un équipement sur FoodEatUp ? Quelques secondes suffisent. | carte d'intro |
| N1 | Direction Production puis Températures : tous vos équipements de froid, d'un coup d'œil. | liste équipements |
| N2 | Utilisez les boutons plus et moins pour saisir la température mesurée du jour. | clic +/- sur Frigo 5 |
| N3 | Un clic sur Enregistrer les relevés, puis confirmez. | clic bouton vert + modal confirmation |
| N4 | FoodEatUp compare aussitôt chaque relevé à ses seuils et repère les non-conformités pour vous. | modal succès + compteurs mis à jour |
| N5 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | **étage 1+2** (reveal + copié) |
| N6 | Collez-le dans la conversation : votre relevé est enregistré en quelques secondes. | **étage 3** (mockup chatbot) |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) — **réutilise tel quel** `videos/foodeatup-tva-tuto/vo/N8.mp3` (texte identique) |

## Séquence « cas d'usage + prompt Claude »

Outil MCP correspondant : `mcp__FoodEatUp__add_temperature(establishment_id, equipment_id,
temperature, measured_at?)`.

Prompt (identique côté vidéo et côté fiche Lovable `claudePrompt`) :

> Enregistre un relevé de température de [température]°C pour l'équipement [nom de
> l'équipement] (ID [ID équipement]) de mon établissement FoodEatUp (ID [ID établissement]).

Réponse assistant (étage 3, mockup) : "Relevé enregistré pour [nom de l'équipement] : [X]°C.
FoodEatUp signale automatiquement si la température dépasse le seuil autorisé."

## Astuce du chef (site Lovable, `chefTip`)

"Un relevé hors seuil (comme ici Frigo 5 à 9°C pour un max de 4°C) reste enregistré et visible
dans l'historique — c'est justement le but : FoodEatUp trace la non-conformité au lieu de la
laisser passer inaperçue, pour votre traçabilité HACCP."

## Cas d'usage (site Lovable, `whatItsFor`)

Suivre la chaîne du froid au quotidien sans papier : un relevé pris en quelques secondes sur
chaque frigo/congélateur/chambre froide, avec détection automatique des écarts par rapport aux
seuils réglementaires — utile pour les contrôles HACCP et pour anticiper une panne de froid.
