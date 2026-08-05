# SCRIPT — eatnow-whatsapp-agent

**Client :** EatNow — système de réservation tout-en-un pour restaurants
**Objet :** vidéo de lancement du WhatsApp Agent (source : `EatNow_Brief_Motion_WhatsApp_Agent.pdf`, brief fourni le 2026-08-04)
**Registre :** le brief d'origine prévoyait aucune voix off (lecture 100% à l'écran). **Ajout demandé par l'agence le 2026-08-05 : une voix off féminine FR**, en complément — jamais en répétition verbatim des bulles de chat (voir § Voix off). Le reste de l'information continue de se lire à l'écran (UI de chat, cartons de texte, interface produit).

---

## Concept

> « Personne n'a décroché.
> La table est réservée. »

Une vraie conversation WhatsApp qui devient une table réservée — pendant le service, sans qu'un membre de l'équipe intervienne. Le fil est réel (bulle verte WhatsApp), tout le cadrage autour reste marque EatNow (Ink / Navy / Beige / Paper).

## Règle de style (non négociable)

Le **vert WhatsApp** ne vit **qu'à l'intérieur de la bulle de chat** — c'est la réalité du client, pas la marque. Tout le reste (cadre, titres, carte de résa, générique, CTA) reste en langage EatNow. La marque reste lisible sur la surface de quelqu'un d'autre — jamais un logo WhatsApp mis en avant, jamais le vert utilisé en dehors du fil de discussion.

## Format & livrables

- **Master 1:1** (1080×1080), décliné en **9:16**. **24 fps. 22–24 s.**
- Sous-titres brûlés inclus, **+ variante sans sous-titres** livrée à part.
- Livrables : **MP4 (1:1 + 9:16)** uniquement. *(Le brief demande aussi un projet source After Effects — non applicable ici : ce studio produit en HyperFrames/HTML-GSAP, pas en AE. À signaler au client si le fichier source AE est un vrai bloquant côté leur intégration.)*
- Son calme uniquement : notification douce, whoosh subtils sur les transitions de carte — jamais bruyant, aucune musique identifiée dans le brief.

## Texte à l'écran — VERBATIM (ne pas reformuler)

### Plan 1 — carton d'ouverture (Fraunces italic)
    Personne n'a décroché.

### Plan 2 — bulle client (verte, WhatsApp)
    Bonsoir, vous avez une terrasse ? Ouvert dimanche soir ?

En-tête du fil : **Le Comptoir · Agent IA · en ligne**

### Plan 3 — bulle agent + repère
    Grande terrasse côté jardin, service dimanche jusqu'à 23h.

Repère Navy : **Depuis votre base de connaissances**

### Plan 4 — carte de réservation
    4 couverts · dimanche 20h30 · terrasse · table 12

Pastille : **Confirmé** (vert `#3D7A58`, EXCEPTION à la règle du vert WhatsApp — c'est un vert EatNow distinct, voir palette)

### Plan 5 — carton (Fraunces italic)
    Et ça tombe dans votre carnet, avec toutes les autres.

Logos canaux qui convergent : **WhatsApp · Google · Instagram · site**

### Plan 6 — clôture
    Un agent qui répond et réserve.

CTA : **Demander une démo →**
Preuves : **24/7 · 0% commission**

### Générique bas de page (dernier carton, texte fixe du brief)
    EatNow — le système de réservation tout-en-un pour les restaurants.
    Demander une démo →
    Contact : wa.me/33651240020 · eat-now.io/solutions/reservation-whatsapp

---

## Charte

| Rôle | Couleur | Usage |
|---|---|---|
| Ink | `#141210` | fond des plans 1 et 6, texte principal |
| Navy | `#10386B` | repères, ligne de connexion plan 5, accents |
| Beige | `#DDD6C6` | surfaces secondaires |
| Paper | `#FAF8F2` | fond téléphone/carte, texte sur fond sombre |
| Confirmé | `#3D7A58` | pastille de confirmation uniquement |
| Vert WhatsApp | officiel WhatsApp | **uniquement** à l'intérieur de la bulle client |

**Typo :** Geist Bold pour les titres (tracking −0.04em) · Fraunces italic pour une ligne émotionnelle par écran (plans 1 et 5).
**Motif :** champ de points 8px, densité différente par surface (dense sur Ink, discret sur Paper).

## Voix off

**Voix :** ElevenLabs (connecteur MCP de la session, `eleven_multilingual_v2`), voix **Charlotte** (`XB0fDUnXU5powFXDhCwa`) — voix féminine chaleureuse. *Première version livrée avec Kokoro local (`ff_siwis`, seule voix FR du moteur offline) ; l'agence a demandé une voix "plus chaleureuse" — remplacée par cette voix ElevenLabs via le connecteur MCP déjà autorisé dans la session (pas besoin de clé API).*
**Vitesse :** naturelle (pas de contrôle de vitesse exposé par le connecteur MCP, contrairement à Kokoro).
**Direction :** autorité tranquille, registre praticien (cf. `BRAND.md` § 9 Voix & Ton) — jamais démonstratif, phrases courtes, silence assumé entre les lignes. La voix off **complète** ce qui est à l'écran, elle ne le répète pas verbatim (exception : la ligne Fraunces du plan 5, reprise à l'identique — technique standard "la voix lit le carton").

| # | Ligne | Départ global | Durée réelle | Plan |
|---|---|---|---|---|
| 1 | « Personne n'a décroché. » | 0.6s | 1.44s | 1 |
| 2 | « Un message arrive, un dimanche soir. » | 3.2s | 2.51s | 2 |
| 3 | « L'agent répond avec ce que vous savez déjà. » | 8.0s | 2.27s | 3 |
| 4 | « La conversation devient une table. » | 12.3s | 2.09s | 4 |
| 5 | « Et ça tombe dans votre carnet, avec toutes les autres. » | 16.3s | 3.16s | 5 |
| 6 | « EatNow. Un agent qui répond, et réserve. » | 20.4s | 2.69s | 6 |

Fichiers : `assets/voice/line-01.mp3` → `line-06.mp3`. Aucun chevauchement entre lignes ; silences généreux entre les beats (~45% du film reste sans voix) — cohérent avec le registre "calme, jamais fort" de la marque.

## Habillage sonore (SFX)

Bibliothèque offline Pixabay (licence libre, sans attribution requise) via le skill `media-use`. Volume ~0.3, toujours sous la voix.

| Cue | Fichier | Départ global | Usage |
|---|---|---|---|
| Notification | `assets/sfx/notification.mp3` | 5.2s | arrivée bulle client (plan 2) |
| Notification | `assets/sfx/notification.mp3` | 8.15s | arrivée bulle agent (plan 3) |
| Pop | `assets/sfx/pop.mp3` | 9.7s | repère "base de connaissances" (plan 3) |
| Whoosh (court) | `assets/sfx/whoosh-short.mp3` | 12.5s | dépliage de la carte (plan 4) |
| Chime | `assets/sfx/chime.mp3` | 14.5s | pastille "Confirmé" (plan 4) |
| Whoosh (court) | `assets/sfx/whoosh-short.mp3` | 16.0s | la carte glisse vers le carnet (plan 5) |
| Chime (volume réduit ~0.22) | `assets/sfx/chime.mp3` | 20.85s | le repère EatNow se dessine (plan 6) — signal calme, pas une 2ᵉ confirmation |

Pas de musique de fond (aucune mentionnée dans le brief, confirmé silence assumé + son design seul).

## Statut assets

- **Vrai kit de marque reçu le 2026-08-05** (`amine.zip`, 3ᵉ envoi — les deux précédents étaient
  corrompus, fichiers à 0 octet). Assets officiels intégrés dans `assets/brand/official/` :
  brandmark (grille 5×5, 17 points), wordmark (tracé vectoriel réel), `BRAND.md` (charte complète),
  `tokens.json` (couleurs). Plus aucun placeholder logo/wordmark dans la composition.
- Le motif recréé à partir de l'image de référence envoyée par le client correspondait exactement
  à la grille officielle — aucune reprise structurelle nécessaire, seul le SVG source a été
  remplacé au Frame 6.
- Polices **Geist** (400/500/700) et **Fraunces italic** (300) vendorées dans `assets/fonts/`
  (Google Fonts, fichiers statiques). Détail des réglages `font-variation-settings` et la limite
  connue (axes variables SOFT/WONK/opsz non pilotables sur un fichier statique) dans
  `assets/brand/README.md`.

## Références de style (fournies par le client)

4 vidéos de référence — publicités officielles WhatsApp/Meta (pas EatNow) : type d'animation visé —
UGC main-tenant-un-téléphone + bulle de chat incrustée, pictos ligne verts animés, typographie
outline en fond ("NEW"), logo qui se révèle proprement en clôture. À retenir comme référence de
**rythme et de propreté d'exécution**, pas comme référence de palette (EatNow reste Ink/Navy/Beige/Paper).
