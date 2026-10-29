# Villa Beach — Halloween « Le plus grand château hanté » (samedi 31 octobre)

Vidéo verticale 1080×1920, 40 s, voix off effrayante. Montée le 29/10/2026.

- Vidéo : `villabeach-halloween-40s.mp4` · miniature : `villabeach-halloween-miniature.jpg` · sous-titres : `villabeach-halloween-sous-titres.srt`
- Composition rejouable : `index.html` + `cfg.js` (construit par `build_cfg.py`), rendu avec `node videos/_moteur/render.js videos/villabeach-halloween 30`

## 1. L'univers du site, réutilisé

Source : https://villabeach.foodeatup.fr/ et la charte du connecteur VillaBeach (`voir_charte_graphique`).

| Élément du site | Usage dans la vidéo |
|---|---|
| Accroche « L'heure dorée » / « Ici, la soirée commence quand le soleil se couche » | Ouverture sur la pergola au coucher du soleil, puis la nuit l'avale |
| « Tout est prêt. Il ne manquait que vous. » | Retournée en menace, chuchotée |
| « Villa Beach, la fête sinon rien. » | Détournée en signature : « Villa Beach… la peur, sinon rien. » |
| Or `#caa968`, brique `#a95134`, fond `#171713`, texte `#f2eddf`, titres Bebas | Titres, mots-clés des sous-titres, badge adresse |
| Monogramme VB doré | Carton final |
| Photo `villa-beach-pergola.jpg` | Plans 1 et 2 |

Faits vérifiés : adresse 23 rue des Pyrénées, 91090 Lisses ; téléphone de réservation 01 84 60 20 46 (CTA des événements du site). Date, slogan « le plus grand château hanté », les deux ambiances et la liste des styles musicaux viennent de l'affiche fournie.
**La soirée Halloween n'est pas encore dans l'agenda du site** (`voir_evenements` ne renvoie que Konpa'n Kiz et Good Vibes Only). Aucun horaire ni prix d'entrée n'apparaît dans la vidéo, faute de source.

## 2. Le script voix (ElevenLabs, voix « Kevan – Narrateur Cinématique », eleven_v3)

```
[whispering] Ici… la soirée commence quand le soleil se couche.
[pause] [ominous] Mais samedi trente-et-un octobre… le soleil ne se relèvera pas.
[slow, menacing] Villa Beach devient… le plus grand château hanté.
Deux ambiances. Deux univers musicaux.
D'un côté : hits, R&B, hip-hop, afro, house.
[lower] De l'autre : zouk, kompa, shatta, dancehall, bouyon.
[whispering] Tout est prêt… Il ne manquait que vous.
Samedi trente-et-un octobre. Vingt-trois, rue des Pyrénées, à Lisses.
[slow, sinister] Villa Beach… la peur, sinon rien. [evil laugh]
```
Prise retenue : `son/voix-kevan.mp3` (38 s). Autre prise : `son/voix-kevan-prise2.mp3` (41,7 s).
Flow ElevenLabs : https://elevenlabs.io/app/flows/izymwZ3dhP9Kie8la0Uq

## 3. Découpage (ce qui fait peur)

| t (s) | Image | Effet |
|---|---|---|
| 0–6,9 | Pergola dorée du site | La lumière se vide : désaturation, virage bleu nuit, brouillard qui monte |
| 6,9–11 | Pergola dans le noir, « 31 OCTOBRE » rouge qui tremble | Éclair + tonnerre, noir total 0,35 s + sifflement aigu |
| 11–15,5 | Château de l'affiche | Zoom lent, deux éclairs, vol de chauves-souris |
| 15,5–22,3 | Affiche : les deux ambiances, puis généraliste et caribéenne | Travellings lents, grain, vignette |
| 26,7–29,4 | Dîner puis piste de danse (photos fournies) | Étalonnage sang/glace, lumière qui grésille, battement de cœur + pulsations rouges |
| 30,5–34,1 | Affiche entière vers la date | Éclair, badge adresse |
| 34,5–40,5 | Monogramme VB doré, « LA PEUR, SINON RIEN » | Éclair + sifflement, fondu au noir |

Son : nappe grave synthétisée (55/58 Hz + bruit brun, trémolo), tonnerre, cœur et sifflement générés par ffmpeg (aucune musique sous droits).

## 4. Prompts Higgsfield (à générer toi-même dans l'interface — règle du dépôt)

Rien de Halloween n'existe dans la bibliothèque Higgsfield (vérifié le 29/10 : seuls 3 plans restaurant en plein jour). Pour remplacer les images fixes par de vrais plans animés, génère ces 4 plans en **9:16, 5 s, sans texte**. Modèle conseillé : Seedance 2.5 ou Kling 3.0 avec image de départ.

**Plan A — La pergola bascule dans la nuit** · image de départ : `img/pergola.jpg`
> Locked-off vertical shot of an outdoor wooden pergola restaurant terrace at golden hour. Over five seconds the sun sets abruptly: the warm orange light drains away, the sky turns deep night blue, a full moon appears, cold fog rolls in at ground level between the empty tables, the woven pendant lamps flicker and die one by one. The architecture, tables and plants stay exactly the same. Horror film mood, subtle, no people, no text, no logos.

**Plan B — Le château hanté** · image de départ : `img/affiche.png` recadrée sur le château (haut de l'affiche, sans le texte)
> Slow push-in toward a gothic haunted castle at night on a hill, windows glowing orange, full moon behind, lightning strikes on both sides lighting the clouds, bats flying out of the towers, fog crawling over the iron gates, carved jack-o'-lanterns flickering in the foreground. Cinematic horror, deep blue and orange palette. No text, no letters, no people.

**Plan C — Le dîner hanté** · image de départ : `img/diner.jpg`
> The same group of friends at a candlelit restaurant table raising their glasses, but the scene turns eerie: candles gutter, the light flickers, every guest slowly turns their head toward the camera in unison and smiles too widely. Halloween horror atmosphere, red and dark tones, no gore, no text.

**Plan D — Le jump-scare citrouille**
> Extreme close-up of a giant carved jack-o'-lantern in darkness. For two seconds nothing moves, then its carved eye ignites with a burst of orange fire and the camera snaps forward into the glowing eye. Horror jump scare, fog, embers, no text.

Une fois générés, dépose-les dans `img/` (`plan-a.mp4`…) : je les branche à la place des photos (plans 1, 3, 7 et final).
