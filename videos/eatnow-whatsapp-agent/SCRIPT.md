# SCRIPT — eatnow-whatsapp-agent

**Client :** EatNow — système de réservation tout-en-un pour restaurants
**Objet :** vidéo de lancement du WhatsApp Agent (source : `EatNow_Brief_Motion_WhatsApp_Agent.pdf`, brief fourni le 2026-08-04)
**Registre :** aucune voix off — la vidéo se lit entièrement à l'écran (UI de chat, cartons de texte, interface produit). Silence + son design uniquement.

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

## Statut assets (bloquant à lever avant rendu final)

- **Kit de marque reçu (`amine.zip`) corrompu** — tous les fichiers (logo, wordmark, motifs SVG/PNG, `BRAND.md`) sont à 0 octet. Aucun asset réel récupéré.
- **Décision (validée avec le client interne 2026-08-05) : on avance avec un wordmark texte placeholder** (« EatNow », Geist Bold) et un motif de tampon recréé à partir de l'image de référence envoyée (grille 5×5 de carrés arrondis), en attendant le vrai zip. À remplacer dès réception des vrais fichiers `01-brandmark/`, `02-wordmark/`, `06-motifs/`.
- **Polices Geist et Fraunces non vendorées dans le repo** — à télécharger (Google Fonts / Vercel) et déposer dans `assets/fonts/` avant le rendu (règle du studio : jamais de CDN dans une composition HyperFrames).

## Références de style (fournies par le client)

4 vidéos de référence — publicités officielles WhatsApp/Meta (pas EatNow) : type d'animation visé —
UGC main-tenant-un-téléphone + bulle de chat incrustée, pictos ligne verts animés, typographie
outline en fond ("NEW"), logo qui se révèle proprement en clôture. À retenir comme référence de
**rythme et de propreté d'exécution**, pas comme référence de palette (EatNow reste Ink/Navy/Beige/Paper).
