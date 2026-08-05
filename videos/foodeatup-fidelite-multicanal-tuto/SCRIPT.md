# Tutoriel — Fidélité Multi-canal (canaux de vente)

**STATUT : BROUILLON — en attente de validation avant génération de la voix off.**

Module 8 « Marketing, Fidélité & Iris » (`marketing-fidelite`), item **19/24** du
catalogue (`videos/CATALOGUE-157-TUTORIELS.md`) : « Fidélité Multi-canal (canaux de
vente) ». Premier tutoriel produit pour ce module (0/24 publiés à ce jour).

Rush fourni par Michael : `assets/screen.mp4` (80,7 s, 1920x828, 25 fps).
Carte intro fournie : `assets/intro.jpg` (« FIDÉLITÉ MULTI-CANAL »).
Carte outro fournie : `assets/outro.jpg` (CTA générique, réutilisée telle quelle).

## Déroulé observé dans le rush (analyse frame-by-frame)

1. **0-6 s** — Back-office, page « Fidélité & jeux » : stats (membres, points en
   circulation, distribués, bons à valider), onglets Programme/Récompenses/Roue
   cadeaux/Sondages/Post-commande. Section « Programme de fidélité » (toggle Actif) :
   mode de gain (par euro dépensé / par passage / hybride), points par € dépensé,
   multiplicateur jours creux (ex. Mar+Mer 11h-14h30, x2, « Points doublés midi »),
   règles (validité 12 mois glissants, plafond 200 pts/commande, crédit même avec
   code promo) → boutons **Enregistrer le programme** / **Voir la page publique**.
2. **6-9 s** — Transition vers le site public (nouvel onglet) : « GoSushi Démo ».
3. **9-78 s** — Page client « Mon compte » : connexion par code à 6 chiffres envoyé
   par email (temps d'attente réel, sera coupé/accéléré au montage).
4. **78-80,7 s** — Une fois connecté : dashboard fidélité côté client — solde de
   points, carte programme, badge « Points doublés midi », « Prochaine récompense :
   café offert, 0/2 pts ».

**Message clé (correspond au titre du catalogue) :** un seul programme configuré côté
back-office est instantanément disponible sur tous les canaux de vente du
restaurateur (caisse, vitrine en ligne...) — le client retrouve ses points et sa
prochaine récompense où qu'il commande.

## Voix off proposée (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Votre programme de fidélité, actif sur tous vos canaux de vente ? C'est automatique avec FoodEatUp. | carte d'intro |
| N1 | Choisissez votre mode de gain : par euro dépensé, par passage, ou hybride. | mode de gain |
| N2 | Ajoutez un multiplicateur sur vos jours creux pour doubler les points, comme le midi. | multiplicateur jours creux |
| N3 | Réglez la validité des points et le plafond par commande, puis enregistrez. | règles + clic Enregistrer |
| N4 | Votre programme est aussitôt actif sur tous vos canaux : caisse, vitrine en ligne, appli. | clic Voir la page publique |
| N5 | Vos clients retrouvent leurs points et leur prochaine récompense, où qu'ils aient commandé. | dashboard fidélité client |
| N6 | Vous pouvez aussi le configurer depuis Claude : copiez ce prompt, remplacez les crochets. | séquence Claude étage 1+2 |
| N7 | Collez-le dans la conversation : votre programme de fidélité est activé en secondes. | séquence Claude étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) — **réutilisée telle quelle** (`N8.mp3` déjà généré sur toute la série) |

## Séquence Claude (outil MCP correspondant)

`mcp__FoodEatUp__update_loyalty_program(establishment_id, active, earn_mode,
earn_rate, points_validity_months, visit_points)` existe et correspond exactement à
l'action montrée (config + activation du programme).

**Prompt proposé (identique côté vidéo et côté fiche Lovable `claudePrompt`) :**

> Active le programme de fidélité de mon établissement FoodEatUp (ID [ID
> établissement]) en mode [par euro dépensé / par passage / hybride], avec
> [points] point(s) par euro dépensé et une validité de [durée] mois.

## À faire une fois le script validé

1. Générer N0-N7 via ElevenLabs (voix Adam FR), réutiliser N8.mp3 existant.
2. Monter `build.py` (zoom-punch sur les clics config + clic « Voir la page
   publique », découpage du long temps d'attente OTP en un raccourci monté).
3. Rendre le MP4 + vignette YouTube (= `assets/intro.jpg`, redimensionnée si besoin).
4. **STOP obligatoire** — livrer à Michael pour validation avant toute publication
   (RapidoCMS, Lovable, réseaux).
5. Après OK : upload RapidoCMS, ajout sur Lovable (`marketing-fidelite`), mise à
   jour de `PROGRESSION-157-TUTORIELS.md`, push GitHub.
