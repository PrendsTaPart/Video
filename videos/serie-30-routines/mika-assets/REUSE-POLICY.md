# Politique de réutilisation Mika (réduction des frais HeyGen)

Décision Michael (2026-07-10) : garder les clips HeyGen en assets, **réutiliser au maximum**,
ne générer un nouveau clip **que si nécessaire**.

## Règle d'or
**Avant toute génération HeyGen → consulter `MANIFEST.md`.** Si un clip au texte identique existe,
le réutiliser. Sinon générer, puis l'ajouter au manifeste (jamais deux fois le même).

## Ce qui est réutilisé vs regénéré

| Bloc | Stratégie | Coût HeyGen |
|---|---|---|
| **Hook (bloc 1)** | **Propre à chaque épisode** — Mika prononce le hook (c'est le scroll-stopper). 1 génération/épisode, sauvegardée en bibliothèque. | 30 clips (dont E1 fait) |
| **Outro (bloc 5)** | **3 clips CTA génériques (A/B/C)** générés UNE fois, réutilisés sur les 30. Rotation `(N-1) mod 3`. Le **teaser « Demain : … » est incrusté en texte** (pas dans la voix), donc l'outro reste générique et réutilisable. | 3 clips au total |

**Économie** : 30 hooks + 3 outros = **33 clips** au lieu de 60 (~45 % de frais HeyGen en moins),
tout en gardant un hook parlé par Mika à chaque épisode.

## Variante « frais minimum » (si Michael la valide)
Remplacer le hook parlé par un **hook en texte cinétique** (voix off narrateur) sur un **intro Mika
générique** réutilisé → **~4 clips HeyGen pour toute la série**. Hook un peu moins incarné, mais coût
quasi nul. Par défaut on garde le hook parlé (meilleur pour TikTok).

## Mécanique de montage (rappel)
- Source = clip brut `raw/*.mp4` (bandes vertes) → `crop=1080:608:0:656` → posé sur fond de marque
  `#EDF1FB` à `y=540` → sous-titres incrustés (boîte indigo `#5A67F2`, `MarginV≈95`).
- Overlays permanents : `BraindCode` (haut-gauche) + `E{N}/30` (haut-droite).
- Teaser d'épisode : incrusté en texte sur l'outro générique.

## Persistance
Les clips vivent dans `mika-assets/raw/` (committés) — le scratchpad est éphémère. Option : les
uploader aussi en bibliothèque RapidoCMS (`upload_file_tool`, nommage `mika — <type> — <ref>`) pour
que la routine R9 les retrouve par nom.
