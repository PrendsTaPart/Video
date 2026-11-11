---
description: Relance uniquement les trois publications d'un tutoriel
argument-hint: <module> <numero>
---

Publie le tutoriel **$1 V$2** déjà rendu.

1. `npm run qa -- content/$1/V$2*` — la publication est refusée tant que la QA
   n'est pas verte.
2. `npm run publier:cms -- content/$1/V$2*` → lien AWS
3. `npm run publier:youtube -- content/$1/V$2*` → lien YouTube
4. `npm run publier:site -- content/$1/V$2*` → page en ligne, **sans validation
   admin** : ce qui part est immédiatement public.

Chaque étape peut demander un appel MCP : exécute l'outil, dépose la réponse dans
le fichier `.reponse.json`, relance.

Termine en affichant les trois liens en clair.
