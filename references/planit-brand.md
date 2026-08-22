# Plani't — Casting, catalogue, nommage

Source : `00-STRATEGIE-PLANIT.md` et `01-PROMPTS-HIGGSFIELD-SEEDANCE-2.5.md` (dossier de
stratégie fourni le 2026-08-22). La charte graphique de ces documents a été **corrigée**
dans `studio-planit/CLAUDE.md` d'après le fichier de marque officiel — ce fichier-ci ne
couvre que casting et structure de catalogue, inchangés par cette correction.

## Les 7 agents (le casting de la série)

| Agent | Rôle | Logiciel | Réplique-signature |
|---|---|---|---|
| **L'Orchestrateur** | Chef d'orchestre | Tous | « Vous parlez. Je comprends ce qu'il faut faire, je choisis le bon agent. » |
| **Léo** | Le Chef | FoodEatUp | « Pendant que vous êtes en cuisine, je tiens votre HACCP à jour. » |
| **Nina** | La Commerciale | RapidoCRM | « Vos devis dorment ? Je les relance. » |
| **Théo** | Le Créatif | RapidoCMS | « J'écris, je programme, je publie. Dans votre ton. » |
| **Sam** | Le Manager | RapidoRH | « Je tiens l'équipe pendant que vous tenez l'entreprise. » |
| **Iris** | La Réalisatrice | Plan'It Studio | « Une idée le matin, une vidéo publiée le soir. » |
| **Marc** | Le Directeur | Tous | « Une page. Trois chiffres. Et les trois choses à faire. » |

Les agents ne sont **jamais** des humains photoréalistes. Ils apparaissent comme :
- une **carte-agent** en motion design (portrait avatar 3D du module Profil & Avatar 3D +
  nom + métier + connecteur), incrustée en overlay HyperFrames ;
- une **voix** ElevenLabs, une par agent, figée pour toute la durée du catalogue.

## Les 5 personas humains (fiches personnage Higgsfield)

⚠️ **Nommage** : sur le site, les agents portent les mêmes prénoms que certains parcours
métier. Dans les séries, l'humain porte un **prénom distinct** de celui des agents, pour
éviter la confusion (ex. « Nina l'agente » / un persona humain différent).

| Code | Persona | Prénom série | Description figée |
|---|---|---|---|
| `PH-DIR` | Dirigeant de petite entreprise | **Karim** | Homme, la quarantaine, chemise bleu clair sans logo, chinos anthracite, montre acier, bureau partagé |
| `PH-RES` | Restaurateur | **Bruno** | Homme, la cinquantaine, veste de cuisine blanche sans marque, tablier marine |
| `PH-COM` | Commercial | **Alice** | Femme, la trentaine, blazer anthracite, top crème, open space |
| `PH-AGE` | Agence | **Sonia** | Femme, la trentaine, sweat gris chiné sans logo, studio créatif |
| `PH-RH` | RH | **Jules** | Homme, la trentaine, chemise gris ardoise, lunettes fines, salle de réunion vitrée |

Chaque fiche : générée **une seule fois** en image fixe 9:16, 3 angles (face, trois-quarts,
profil) sur fond gris neutre, enregistrée comme *Reference Element* Higgsfield, réutilisée
dans **tous** les prompts Seedance 2.5 du persona (jusqu'à 50 références/génération).
Inventaire des fiches déjà générées : voir **`references/planit-characters.md`**.

**4 plaques de lieu** à générer et réutiliser de la même façon : `PL-BUREAU` (petit bureau
partagé), `PL-CUISINE` (réserve de restaurant), `PL-OPENSPACE` (open space 6 postes),
`PL-STUDIO` (studio créatif, table longue).

**Règle du dépôt (héritée)** : aucun agent ne génère sur Higgsfield — Claude produit le
prompt, l'humain le génère lui-même dans l'interface Higgsfield.

## Les 4 séries et leurs codes

| Code | Série | Format | Saisons | Épisodes | Rôle marketing |
|---|---|---|---:|---:|---|
| **A** | Une demande | 9:16 · 30 s | 7 | 56 | Acquisition |
| **B** | Le Quai | 9:16 · 35×10 s + film 350 s | 5 | 35 | Marque / manifeste |
| **C** | L'Académie | 9:16 · 60 s | 7 | 43 | Activation / onboarding |
| **D** | La Boucle | 9:16 · 45 s | 5 | 52 | Preuve / conversion |
| | | | **24** | **186** | |

- **Série A — « Une demande »** : une saison par agent (8 épisodes chacune). Structure
  fixe : 0–10 s la scène qui coince (zéro logiciel) · 10–14 s la demande (une phrase) ·
  14–24 s l'agent entre (geste réel, vraie capture d'écran) · 24–30 s résultat + signature
  « Ce n'est pas demain. C'est aujourd'hui. »
  S1 Orchestrateur · S2 Nina · S3 Léo · S4 Théo · S5 Sam · S6 Iris · S7 Marc.
- **Série B — « Le Quai »** : film manifeste, 35 plans de 10 s (S1→S4 : 6 plans chacun,
  S5 : 11 plans) formant un film de 350 s. Une seule personne traverse cinq époques
  (1886 → 2026), même visage, costumes différents ; le dernier plan révèle le dirigeant
  d'aujourd'hui.
- **Série C — « L'Académie »** : les 43 tutoriels existants réhabillés en série, une saison
  par étape du parcours (S0 Comprendre → S6 Piloter). Contenu déjà présent dans le MCP
  `Production video planit` (`tutoriel_spec`).
- **Série D — « La Boucle »** : une saison par persona (S1 Dirigeant · S2 Restaurateur ·
  S3 Commercial · S4 Agence · S5 RH), chaque épisode suit une routine réelle sur 14 jours.

## Convention de nommage des dossiers

```
planit-{serie}-s{saison}e{episode}-{slug}
```

Exemples : `planit-a-s2e1-dix-huit-devis` (Série A, saison 2 = Nina, épisode 1),
`planit-c-v05-utiliser-une-carte-de-prompt` (Série C garde le numéro de tutoriel `V<NN>`
plutôt que `s{saison}e{episode}`, puisque le contenu est piloté par le MCP Académie).

Baseline du produit : « Vos logiciels ont enfin une équipe. »
Signature de fin (Série A/D) : « Ce n'est pas demain. C'est aujourd'hui. »
