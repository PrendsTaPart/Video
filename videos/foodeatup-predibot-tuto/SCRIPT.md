# Tutoriel — Prédire ses commandes (ventes & production) — PrediBot

Script validé par Michael le 2026-08-03 (« je valide »). Montage terminé : durée livrée
**39,4 s** — H.264 High/yuv420p 1920x828, AAC 48 kHz stéréo, faststart (`ftyp`→`moov`→`mdat`
confirmé). Decode 0 erreur. Audio : peak **-7,19 dBFS** (marge confortable sous 0 dBFS).

Premier ajustement fait pendant le montage : les cibles de segments initiales (calées sur
un total silencieux ~23 s) étaient bien trop courtes pour porter les 8 lignes de VO
mesurées (~38,6 s de voix cumulée) — exactement le piège documenté dans
`FOODEATUP-TUTORIELS-WORKFLOW.md` (« segments trop rapides → outro tenue en silence
exagérément long »). Un premier essai a produit un outro auto-étendu à 22 s de carte
statique. Corrigé en recalibrant les cibles de segments (A/C/E allongées, cf. `build.py`)
sur la durée réelle des lignes VO qu'elles portent ; l'outro ne s'étend plus qu'à 12,4 s
(6,2 s de base + 6,2 s de dérive absorbée), cohérent avec le reste de la série.

Premier tutoriel du module **PrediBot (Agent IA Directeur)** (`predibot`, 0/3 vidéos avant
celle-ci). Intrants reçus de Michael le 2026-08-03 :
- `assets/intro.jpg` — carte d'ouverture "PRÉDIRE SES COMMANDES VENTES & PRODUCTION"
- `assets/outro.jpg` — carte de fin CTA (identique au fichier déjà utilisé sur tous les
  autres tutos, md5 vérifié contre `foodeatup-vitrine-tuto/assets/outro.jpg`)
- `assets/screen.mp4` — écran capturé, 1920x828, 25 fps, **12,88 s**, piste audio silencieuse
  (-91 dB, aucune VO native à extraire)

## Déroulé observé dans le rush (frames extraites toutes les 0,5 s)

| t (rush) | Contenu |
|---:|---|
| 0,0 – 2,0 s | `foodeatup.com/establishment/26/carte` — page "Ma carte", en-tête + barre de recherche |
| 2,0 – 4,5 s | Scroll jusqu'à la grille de plats (PV, Pizza Margherita, PT, RC) |
| 4,5 s | Survol/clic sur l'icône graphique (📈) de la carte "Pizza Margherita napolitaine" |
| 4,5 – 6,5 s | Ouverture de la modale prédictions : tableau Jour / Commandes réelles / Estimation IA / Production réelle / Écart estimation / Écart prod (Mer→Mar, 7 jours ; Estimation IA 17/18/20/16/9/13/14) |
| 6,5 – 8,0 s | "Indice de performance IA : 30 %", "Confiance du modèle : Faible", bandeau "Bonne performance de la prédiction cette semaine !" |
| 8,0 s | Clic "Exporter PDF" → toast "PDF exporté avec succès !" |
| 8,0 – 12,88 s | Le PDF généré s'ouvre dans un nouvel onglet : en-tête FOODEATUP / "Prédiction des commandes" / "Pizza Margherita napolitaine" / Période : 7 jours / Généré le 29 juillet 2026, même tableau |

Pas d'étape de saisie/formulaire ici : la fonctionnalité est 100 % lecture (l'IA calcule,
l'utilisateur consulte et exporte).

## Recherche d'un outil MCP correspondant (règle `LOVABLE-FOODEATUP-DOCS.md` étape 3)

Passé en revue les outils `mcp__FoodEatUp__*` disponibles (production, stock, finance...) :
aucun ne correspond à "prédire les commandes futures d'un plat sur une période". Les outils
les plus proches (`get_production_ingredients`, `list_production_plans`,
`create_production_plan`, `get_daily_brief`) portent sur la planification déclarative, pas
sur une prédiction IA en lecture seule par plat. **Conclusion : pas de `claudePrompt` sur ce
tutoriel** — pas d'outil, pas de prompt inventé (règle du pipeline). Pas de séquence
"Utilisez cette fonctionnalité avec Claude" en fin de vidéo non plus (même règle).

## Voix off proposée (8 lignes) — SOUMISE À VALIDATION, AUCUN AUDIO GÉNÉRÉ

| # | Texte | Ancrage |
|---|---|---|
| N0 | Combien de Pizza Margherita allez-vous vendre cette semaine ? PrediBot vous le dit. | intro / carte A |
| N1 | Depuis Ma carte, repérez le plat à analyser — ici la Pizza Margherita napolitaine. | A→B (scroll grille) |
| N2 | Cliquez sur l'icône graphique du plat pour ouvrir ses prédictions. | clic B (zoom-punch) |
| N3 | PrediBot affiche les commandes estimées, jour par jour, sur les 7 prochains jours. | C (tableau) |
| N4 | Deux repères clés : l'indice de performance IA, et le niveau de confiance du modèle. | C (indices) |
| N5 | Un clic sur Exporter PDF, et le rapport est prêt à partager avec votre équipe en cuisine. | D (clic export + toast) |
| N6 | Fini les ruptures ou le gaspillage : vous produisez juste ce qu'il faut, chaque jour. | E (PDF ouvert) — bénéfice |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA, **réutilisable telle quelle** depuis un tuto précédent) |

Pas de séquence Claude (voir ci-dessus) : N7 enchaîne directement après N6, comme sur les
tutos sans outil MCP correspondant (ex. `regler-ses-unites`).

## Découpage envisagé (à affiner lors du montage, coordonnées de clic à recalibrer par
seuillage colorimétrique comme sur les autres tutos)

| Seg | Source | Contenu |
|---|---|---|
| intro | carte | PRÉDIRE SES COMMANDES VENTES & PRODUCTION |
| A | 0,0 → 4,3 | Ma carte + scroll jusqu'à la grille |
| B | 4,3 → 4,6 | **zoom-punch** sur l'icône graphique de la Pizza Margherita |
| C | 4,6 → 8,0 | Modale prédictions : tableau 7 jours + indices IA |
| D | 8,0 → 8,3 | **zoom-punch** sur "Exporter PDF" + toast succès |
| E | 8,3 → 12,88 | PDF ouvert (en-tête + tableau) |
| outro | carte | CTA (réutilisée) |

Durée cible finale : ~35-45 s une fois les segments recalés sur la durée réelle de chaque
ligne VO (mesurée après génération), en suivant `videos/FOODEATUP-TUTORIELS-WORKFLOW.md`.

## Vignette YouTube

Réutilisation directe de `assets/intro.jpg` (pas de redesign), livrable
`out/thumbnail-youtube.jpg` une fois redimensionnée 1280x720 si besoin.

## Statut

Script validé (2026-08-03). VO générée (ElevenLabs, voix Adam FR `TGAegA0zNRi8I6nUdq3i`) pour
N0-N6 ; N7 (CTA) réutilisé tel quel depuis `foodeatup-fournisseurs-tuto/vo/N8.mp3` (md5
identique sur les 3 tutos précédents qui le réutilisent déjà). Montage terminé :
`out/foodeatup-predibot-tuto-v1.mp4` + `out/thumbnail-youtube.jpg` (1280x720, réutilisation
neutre de `assets/intro.jpg`, aucun redesign).

**STOP obligatoire (règle `FOODEATUP-TUTORIELS-WORKFLOW.md` §6) : vidéo livrée à Michael
pour validation. Pas de publication (RapidoCMS, LinkedIn, Lovable) tant qu'un retour OK
explicite n'est pas reçu.**
