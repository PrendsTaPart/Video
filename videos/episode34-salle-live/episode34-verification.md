# Épisode 34 : rapport de vérification (27/10/2026, vers 23 h)

Sources : projet Lovable `66a5a3d7…` (dernière modification 27/10 19:57, commit `79eff12`), dépôt `PrendsTaPart/layout-manager-ai` (AGENTS.md, roadmap.md, routes), site public https://camera.foodeatup.fr, base de données lue en lecture seule. Le projet n'a pas été modifié.

## Ce qu'on voit dans la vidéo et d'où ça vient

| Élément montré | Source | Statut |
|---|---|---|
| Salle 3D, changements de couleur des tables | Page publique `/demo`, 7 étapes capturées le 27/10 | **Démonstration scénarisée** : chaque image est calculée depuis une horloge (`src/lib/demo-scenario.ts`), sans caméra ni restaurant |
| Plan 2D, « 4p · 34′ », 92 % de remplissage, 4,2 min de débarrassage | Même page `/demo` | **Chiffres de démo**, pas des mesures |
| Flux « Événements envoyés » (JSON) | Même page `/demo` | Démo ; même format que la route réelle `device-events` |
| « Comment ça marche » (3 étapes) | Page d'accueil camera.foodeatup.fr | Texte réel du site |
| Règles d'alerte (7) | `src/lib/alerts.ts`, moteur SQL `evaluate_alerts()` | **Développé**, jamais déclenché sur de vraies données |
| Planning IA | `src/lib/forecast.ts`, page `planning.tsx` | **Développé**, aucune prévision calculée (pas d'historique) |
| Connexion FoodEatUp | `foodeatup.server.ts`, roadmap étapes 1, 2, 3, 9 cochées | **Connexion OAuth/MCP codée** ; aucun compte connecté en base |
| Synchro plan, caisse en direct, réservations, retour d'état | roadmap étapes 4 à 8 | **Prévu**, non fait |
| Caméra / boîtier | routes `api/public/device-*`, simulateur | **Codé** ; aucun boîtier réel, aucune installation validée |

## État de la base de production (lecture seule)

2 restaurants, 0 table, 0 boîtier, 0 événement, 0 session, 0 alerte, 0 jeton FoodEatUp.

## Non capturé

Les écrans de la console (Salle live, Éditeur de plan, Alertes, Planning IA, mobile) demandent un compte. Je ne me suis pas connecté et je n'ai créé aucun compte sur la production. Ces écrans ne sont donc pas montrés en capture ; la vidéo montre à la place la démo publique, le code et les textes réels. Pour les filmer, il faudrait une session de démonstration avec un restaurant simulé (le simulateur existe dans l'app).

## Garde-fous respectés

Aucune image de personne. Aucune vente, aucun déploiement ni aucun gain chiffré annoncés. La présentation au client est prévue le 28/10/2026.
