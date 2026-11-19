# Villa Beach · vidéos des fêtes (Remotion)

Six vidéos des menus de Noël et du Nouvel An de la Villa Beach (Le Garden, 23 rue des Pyrénées, 91090 Lisses, 01 84 60 20 46).

| Fichier (out/) | Format | Durée |
|---|---|---|
| villa-beach-noel-menu-1080x1920.mp4 | Reels / TikTok / Stories | 20 s |
| villa-beach-nouvel-an-menu-1080x1920.mp4 | Reels / TikTok / Stories | 20 s |
| villa-beach-noel-teaser-1080x1920.mp4 | Teaser « Places limitées » | 8 s |
| villa-beach-nouvel-an-teaser-1080x1920.mp4 | Teaser « Places limitées » | 8 s |
| villa-beach-noel-menu-1080x1350.mp4 | Post Instagram 4:5 | 20 s |
| villa-beach-nouvel-an-menu-1080x1350.mp4 | Post Instagram 4:5 | 20 s |

## Modifier les textes, plats, prix et dates

Tout est dans `src/data/fetes.ts` (restaurant, charte, tempo, menus, prix, dates, accroches, musiques, photos).

## Rendre

```bash
npm install
bash rendre.sh          # rend les six vidéos dans out/ et trois images de contrôle par vidéo dans out/controle/
npx remotion studio     # aperçu interactif
```

`rendre.sh` appelle `npx remotion render` avec le Chrome headless de la machine (variable `REMOTION_BROWSER` pour en changer).
`bash apercu.sh <dossier> composition:image …` rend des images fixes et une planche contact.

## Ressources (assets/)

- `logo.png` : logo officiel VB doré (fond transparent).
- `hero-noel.png`, `hero-nouvel-an.png` : images d'ouverture. **Provisoires** : ce sont des photos réelles de plats de la Villa Beach
  (foie gras, brioche flambée) ; remplacez-les par vos visuels de fêtes en gardant le même nom.
- Photos de plats : bibliothèque d'assets FoodEatUp de la Villa Beach. Elles servent d'ambiance derrière les menus ; elles ne
  représentent pas les plats exacts des menus de fêtes.
- `music-noel.mp3`, `music-nye.mp3` : musiques instrumentales générées pour la Villa Beach avec ElevenLabs Music (piano « dîner »
  et électro). Remplaçables par toute piste libre de droits du même nom ; la seconde de départ se règle dans `fetes.ts`
  (`musique.debut`). Fondu d'entrée 1 s, de sortie 1,5 s.

## Rythme

Toutes les transitions tombent sur la grille 120 BPM (un temps = 0,5 s = 15 images) : Noël = intro 3 s, trois sections de 4 s,
final 5 s ; Nouvel An = intro 2 s, trois sections de 3 s, prix 3 s, compte à rebours 3-2-1 (1 s chacun), confettis et appel final 3 s ;
teasers = une coupe toutes les 2 temps (1 s) avec flash doré.
