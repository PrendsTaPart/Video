# Vidéo 14 · Mes agents traquent les bugs (FoodEatUp QA Hub)

Format vertical 1080 × 1920, 49 s. Voix Noé (ElevenLabs, `eleven_v4`), effets sonores d'échec et de réussite. **Rien n'a été publié, aucune donnée n'a été modifiée.**

## Voix off

> Pour tester mes MCP et valider mes logiciels, j'ai développé mon propre outil de contrôle qualité.
>
> Parce que créer un logiciel avec l'IA, c'est bien… Mais qui vérifie que tout fonctionne ?
>
> Dans mon QA Hub, un scénario appelle un outil MCP ou une API, puis compare la réponse au résultat attendu : le code, la valeur, le texte. Chaque exécution garde ses preuves.
>
> Quand un test échoue, l'idée, c'est de créer un ticket avec ces preuves, et un prompt de débogage pour Claude Code. Claude corrige sur une branche, les tests repartent, et on vérifie que le bug a disparu.
>
> Mon objectif, c'est que cette boucle tourne seule, avec une validation humaine avant chaque mise en production. Et tant que ça ne passe pas… la boucle continue !
>
> Avant, je cherchais les bugs. Maintenant, mes agents m'aident à les traquer, à préparer les corrections et à vérifier le résultat.
>
> Et demain, je te montre jusqu'où cette boucle peut aller !

## Écarts avec le brief

- **« J'ai connecté mes outils à OpenAI et Claude » est retiré.** Je n'ai trouvé aucune intégration OpenAI vérifiable.
- **Le MCP QAtest était injoignable dans cette session (erreur 503).** Aucun de ses outils n'a donc été appelé, et le cas d'échec montré est une **démonstration simulée**, signalée à l'écran.
- **L'intérieur du QA Hub n'a pas été filmé.** Il demande un compte, et le parcours connecté est bloqué tant que la base est en pause (`roadmap.md`).

## Ce qui existe vraiment (code du projet Lovable e9adf807, lu le 26/10)

| Étape de la boucle | État |
|---|---|
| Scénarios automatisés : appel d'outil MCP ou d'API, vérification du code, d'une valeur JSON ou d'un texte | ✅ dans le code (`src/lib/automation.ts`) |
| Preuves : requête et réponse de chaque étape | ✅ dans le code (`test_runs.step_results`) |
| Tickets de bug, statuts, bugs similaires, matrice de traçabilité, go / no-go | ✅ 64 outils MCP dans `src/lib/mcp/tools/` |
| 20 tests MCP isolés | ✅ réussis (`roadmap.md`) |
| Prompt de débogage généré depuis un ticket et transmis à Claude Code | 🟠 objectif, non vérifié |
| Relance automatique après correction, sans intervention | 🟠 objectif |
| Validation et mise en production | 🔵 humaines |

La scène finale (« L'IA développe. L'IA teste. L'IA corrige. ») est présentée comme le concept. Une mention à l'écran précise ce qui est réellement automatisé aujourd'hui.
