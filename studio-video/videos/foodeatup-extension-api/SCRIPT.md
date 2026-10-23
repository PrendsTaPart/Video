# Créer une extension connectée à FoodEatUp — 57 s, 16:9

Vidéo de la page **Documentation API** de l'Académie (`/documentation-api`), pour les
restaurateurs qui automatisent, les développeurs et les agents IA.

**Source unique du contenu : `src/data/api-documentation.ts` du dépôt Académie**
(`NOMBRE_OUTILS_API`, `ETAPES_AUTH`, `ETAPES_MCP`, `FAMILLES_OUTILS`, `CAS_USAGE`).
Les noms d'outils affichés à l'écran (`list_low_stocks`, `list_orders`, `finance_summary`)
existent dans le MCP produit FoodEatUp. Aucun endpoint inventé.

- Voix : **Adam - Instructor** (`TGAegA0zNRi8I6nUdq3i`), `eleven_multilingual_v2`, prise 1 sur 2.
- Musique : ElevenLabs Music v2.5, lo-fi électro instrumentale (contrôlée sans paroles), volume 0,15.
- Audio normalisé à −16 LUFS (ffmpeg `loudnorm`).
- Sous-titres calés sur la transcription mot à mot ElevenLabs Scribe (identique au script).
- Flow ElevenLabs : `caivfz3nwbPiMUz2UmJn`.

| Temps | Scène | Voix off | Visuel |
|---|---|---|---|
| 0 → 5,9 s | Votre outil | Vous voulez brancher votre propre outil sur FoodEatUp ? Une extension, un script, un tableau de bord ? | Trois pastilles reliées par des câbles au logo FoodEatUp |
| 5,9 → 11,5 s | Une seule porte | Tout le logiciel passe par une seule porte : l'API FoodEatUp, et ses cent quatre-vingt-treize outils. | Porte « API », grille de 193 cases, compteur 0 → 193 |
| 11,5 → 20,25 s | La clé | D'abord, créez une clé d'établissement dans Mon profil, API Clients. Notez le client ID et le client secret : le secret ne s'affiche qu'une fois. | Fenêtre Mon profil › API Clients, champs client_id / client_secret, badge « Affiché une seule fois » |
| 20,25 → 26,15 s | Le jeton | Échangez cette clé contre un jeton, valable vingt-quatre heures. Chaque jeton ne voit que votre établissement. | Clé → jeton Bearer, horloge 24 h, cadenas « 1 jeton = 1 établissement · GET /api/me » |
| 26,15 → 34,75 s | Point d'entrée | Ensuite, un seul point d'entrée : slash API, slash MCP. Tools list pour découvrir les outils, tools call pour agir. | Terminal : POST /api/mcp, tools/list, tools/call, result.content[0].text |
| 34,75 → 43,7 s | Tout FoodEatUp | Stocks, carte, commandes, HACCP, équipe, comptabilité : votre extension lit et écrit dans tout FoodEatUp. | Six tuiles qui s'allument sur chaque mot, carte « Votre extension · lit · écrit » |
| 43,7 → 50,75 s | Cas d'usage | Une alerte de stock bas sur WhatsApp, l'export comptable chaque matin, ou un agent IA qui répond sur vos vrais chiffres. | Trois cartes : WhatsApp (scénario n8n), export 07:00, agent IA |
| 50,75 → 57 s | Fin | Toute la documentation est sur l'Académie FoodEatUp. À vous de construire. | Logo, tutoriel.foodeatup.com/documentation-api, « À vous de construire » |

Rendu : `renders/foodeatup-extension-api-v1.mp4` (1920×1080, 30 i/s, H.264 + AAC).

## Publication
Vidéo archivée dans la bibliothèque RapidoCMS. **Aucune publication sur les réseaux sans
validation humaine de la pièce.** Après validation : l'ajouter à la page Documentation API
de l'Académie et, en option, une déclinaison verticale 1080×1920 pour les Reels.
