---
description: Relance uniquement l'écriture du script d'un tutoriel
argument-hint: <module> <numero>
---

Réécris le script du tutoriel **$1 V$2**.

1. `npm run tuto -- $1 $2 --from script --to script --force`
2. Suis la consigne de `script-demande.md` et le squelette de
   `script-squelette.json`.
3. Respecte le ton de `CLAUDE.md` : vouvoiement, phrases courtes, zéro jargon non
   expliqué, jamais « il suffit de ».
4. Propose **3 hooks** et **3 punchlines** dans les champs `alternatives`.
5. Vérifie le débit : 150 mots/minute, chaque voix d'étape doit tenir dans sa
   fenêtre vidéo. Durée cible 90–150 s.
6. Présente-moi `script.md` et les choix à faire.

Ne relance ni la voix off ni le rendu : ce sont des étapes séparées.
