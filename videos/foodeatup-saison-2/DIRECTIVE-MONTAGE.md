# Directive de montage commune aux 30 épisodes

À coller avant le bloc de l'épisode. Chaque fiche de `prompts/` contient déjà la version
complète, épisode substitué : ce fichier n'est là que comme référence de la structure.

```text
Tu es motion designer. Crée avec Remotion (React) une composition verticale 1080×1920, 30 fps,
300 images (10 s), export MP4 H.264, fichier ep{NN}-outro.mp4.

Entrées dans ./assets : logo-foodeatup.svg · palette.json · scene2-last-frame.png · vo.mp3 · sfx/
(clap.wav, whoosh.wav, tick.wav, impact.wav). Voir assets/README.md pour la provenance.

STRUCTURE IMPOSÉE (identique sur les 30 épisodes — c'est la signature de la saison) :
0–2 s : scene2-last-frame plein écran, léger zoom avant, désaturation progressive ; clap de cinéma qui entre par le bas et claque à 0,4 s (SFX clap) ; texte « COUPEZ ! » ; à 1,6 s « Dans la vraie vie… ».
2–4 s : L'élément clé de la scène se transforme en données (motion blur, particules légères, easing expo-out) — précisé par épisode.
4–7 s : Démonstration du bénéfice : maquette d'écran FoodEatUp en 3D légère (rotation ≤ 8°), micro-animations, action en UN tap, ralenti de 6 images sur le tap.
7–9 s : Les modules concernés apparaissent en cartes reliées par des flux lumineux (libellés réels uniquement).
9–10 s : Tout disparaît ; logo FoodEatUp seul, centré, scale 0,9 → 1 + halo ; signature sous le logo ; SFX impact + whoosh ; fondu.

CONTENU DE CET ÉPISODE : [bloc de l'épisode — voir prompts/ep{NN}-*.md]

RÈGLES : L'animation se comprend sans le son. Texte ≥ 64 px, ≤ 6 mots par écran, zone sûre TikTok/Reels/Shorts (marges 220 px haut, 320 px bas, 120 px côtés). Jamais de faux texte d'interface : uniquement les libellés réels. La voix off démarre à 2,0 s et finit avant 9,0 s. Un SFX par apparition ; motion blur sur les zooms. Rendu premium SaaS, humoristique, moderne, lisible sur smartphone.

SORTIES : ep{NN}-outro.mp4 · ep{NN}-outro-muet.mp4 · ep{NN}-thumb.png
```

## Libellés de modules autorisés (68)

Réservations · Plan de salle · Zones · Tables · File d'attente · Commandes · Écran cuisine · Postes · Caisse · Session de caisse · Rapport X · Rapport Z · Paiements · Ardoises · TPE · Lien de paiement · Cartes cadeaux · HACCP · Températures · Équipements · Réception · Étiquettes DLC · Traçabilité · Checklist hygiène · Plan de nettoyage · Stock · Ingrédients · Fournisseurs · Commandes fournisseurs · Livraisons · Recettes · Production · Alertes production · Employés · Planning · Shifts · Congés · Pointages · Contrats · Documents · Recrutement · Offres d'emploi · Candidatures · Clients · Fidélité · Récompenses · Bons · Roue cadeaux · Campagnes · Segments RFM · Avis · Sondages · Site vitrine · Pages · Leads · Livraison · Zones de livraison · Happy hours · Boissons · Événements privés · Devis · Factures · Dépenses · Synthèse financière · Brief du jour · Agent vocal · Notifications · Analyse de la carte

Aucun autre libellé ne peut apparaître à l'écran. `npm run check` le vérifie sur les 30 épisodes.

---
Fichier généré par `scripts/build.mjs`, ne pas éditer à la main.
