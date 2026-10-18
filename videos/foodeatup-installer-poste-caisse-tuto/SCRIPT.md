# Tutoriel — Installer un poste de caisse FoodEatUp

Fiche Académie : `installer-un-poste-de-caisse-foodeatup` (module Installateur de caisse,
section « Poser le poste », ordre 1). Vidéo encore absente du catalogue.

**Statut : script à valider par Michael — étape 3 du workflow
(`videos/FOODEATUP-TUTORIELS-WORKFLOW.md`). Aucune voix générée, rien monté.**

## Sources

- **Brief de la fiche** (`src/data/partenaires.ts` du dépôt Académie) — objectif : « Poser un
  poste complet et le mettre en service sans reprise ». Plan : repérer le comptoir ; monter le
  poste et vérifier la connexion à la boutique ; ouvrir la session et faire un ticket de test ;
  contrôler l'affichage client et l'impression ; laisser le poste allumé, session ouverte.
- **Formation caisse** (PDF du 28/09/2026) : §2 (écran « Qui prend le service ? », session école),
  §10 (carte « Postes de caisse » › Ajouter un poste : nom, repère, imprimante et terminal par
  défaut ; « Caisse 1 » créée seule ; menu Configuration boutique › Intégration › Intégrations).
- **Écrans Figma** (fichier `4GDqEY4E2fLsrIx6KPAHNU`), exportés dans `assets/figma/` en 1440×1024
  (C02 en 1280×800) :

| Fichier | Nœud | Écran |
|---|---|---|
| `ds18-livraison-appairage.png` | 5389:613 | DS18 — suivi de commande matériel & appairage automatique |
| `d20-droits-materiel.png` | 5299:715 | D20 — Utilisateurs, droits & matériel |
| `d01-ouverture-caisse.png` | 5277:97 | D01 — Ouverture de caisse & PIN (session école) |
| `d05-prise-de-commande.png` | 5272:926 | D05 — Prise de commande (barre d'état matériel) |
| `c02-ecran-client.png` | 5455:761 | C02 — Écran client · note en cours |

## Voix off proposée (8 lignes)

Voix Adam FR (`TGAegA0zNRi8I6nUdq3i`, `eleven_multilingual_v2`), comme les autres tutoriels.

| # | Texte | Écran | Ancrage visuel |
|---|---|---|---|
| N0 | Vous installez un poste de caisse FoodEatUp ? Voici l'ordre qui évite de revenir. | carte d'intro | titre INSTALLER UN POSTE DE CAISSE |
| N1 | Branchez l'appareil au courant et au réseau : il démarre sur FoodEatUp et s'appaire tout seul avec le code de son étiquette. | DS18 | zoom sur le bloc « À la livraison », étapes 1 et 2 |
| N2 | Dans Utilisateurs, droits et matériel, vérifiez chaque équipement : imprimante, terminal de paiement, tiroir-caisse. | D20 | zoom sur la carte « Matériel » |
| N3 | Un appareil hors ligne ? Touchez Tester avant d'aller plus loin. | D20 | zoom-punch sur « Tester » (Imprimante Bar, ~1304, 428) |
| N4 | Pour vos essais, activez la session école : les tickets portent la mention ÉCOLE et n'entrent dans aucun chiffre. | D01 | zoom sur l'interrupteur « Session école » (~380, 476) |
| N5 | Faites un ticket de test : il doit s'imprimer, et l'écran client doit afficher la commande en direct. | D05 puis C02 | barre d'état « Imprimante OK · Tiroir fermé · TPE appairé », puis écran client |
| N6 | Avant de partir, laissez le poste allumé, prêt pour le premier service. | D01 | panneau « Session de caisse » |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin | CTA (réutilisable depuis `foodeatup-tva-tuto/vo/`) |

N7 est le texte de fin standard : la ligne déjà générée peut être réutilisée, zéro crédit ElevenLabs.

## Points à trancher avant de générer la voix

1. **Pas de geste physique filmé.** Le brief demande « gestes filmés en plan serré, chaque
   branchement visible ». Les écrans Figma montrent le logiciel, pas les câbles : cette version est
   un tutoriel d'écrans. Si des rushs de branchement existent (ou sont tournés), ils remplacent N1.
2. **Postes multiples (§10 du PDF).** Non repris dans la voix pour tenir la durée. Option : une
   ligne « Un bar et une salle ? Ajoutez un deuxième poste dans Intégrations, avec son imprimante
   et son terminal. » — mais aucun écran Figma ne montre la carte « Postes de caisse » ; il
   faudrait l'écran réel ou une capture.
3. **Session école puis vraie session.** Le PDF dit comment activer la session école, pas comment
   la quitter. N6 reste volontairement neutre (« prêt pour le premier service ») au lieu de
   décrire une manipulation non documentée.
4. **Durée.** Le brief vise 300 s ; ce script fait environ 40 s, comme les autres tutoriels
   d'écran du catalogue. À confirmer.

## Ce qui reste après validation

1. Générer la voix (clé ElevenLabs à fournir à la session, absente aujourd'hui).
2. Monter en HyperFrames 16:9 avec les écrans ci-dessus, sous-titres à la charte.
3. Déposer la vidéo dans la bibliothèque RapidoCMS, récupérer son lien, le renseigner dans la
   fiche Académie ; publier sur les réseaux **après validation humaine de la pièce**.
