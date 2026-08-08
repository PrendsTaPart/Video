# Plans « sans » à tourner — prompts prêts à coller

Les neuf films « sans » sont montés et rendus **sans ces plans** : ils utilisent
les treize plans animés et les cinq photos déjà présents dans la bibliothèque,
ré-étalonnés au registre « sans ». Rien n'est bloqué.

Ce qui suit comblerait les reprises. Aujourd'hui trois plans servent deux fois
chacun (`sept-onglets` sur D1′ et D3′, `bureau-matin` sur D1′ et D2′,
`telephone-comptoir` sur C3′ et S2′, `cahier-spirale` sur C1′ et C3′). Une
reprise ne se voit pas d'un film à l'autre, mais elle se verra le jour où les
neuf seront regardés à la suite.

## Comment les générer

Modèle `seedance_2_0`, 16:9, 6 à 10 secondes, sans audio. Les références de
personnages se citent par leur **UUID** entre `<<<>>>`, pas par leur nom — le
nom n'est pas résolu et le personnage sort différent :

| Personnage | UUID |
|---|---|
| chef-hero | `c841147a-6375-4c5e-b146-e45c1cab7e99` |
| serveur-hero (une **femme**, chemise noire, demi-tablier marine) | `a8f9dfa9-47cf-4ba3-86f8-93ab0b4a11c1` |
| directeur-hero | `2f3b8e65-a41d-429a-abf7-5df04baddf7a` |

Une fois les plans générés, donne-moi les fichiers : le ré-étalonnage au
registre « sans » et le remontage sont automatiques
(`_serie/plans-sans.sh`, puis `_serie/build-sans.py`).

## ⚠️ La clause à ne jamais retirer

Chaque prompt se termine par la même liste d'interdits. Elle n'est pas
décorative : un logiciel tiers reconnaissable à l'image ferait basculer le film
en publicité comparative (NOTES §6.1, art. L122-1 et L122-2 du Code de la
consommation), et le registre ironique de ces films ferait alors tomber le
dénigrement. Si un plan revient avec une interface lisible à l'écran, il est
inutilisable — mieux vaut le relancer que le monter.

> `no readable real text, no invented logo, no invented software interface, no recognizable software UI, no brand, no watermark, no deformed hands, no stock-photo smile, no excessive HDR, no recognizable people or brands, flat overcast desaturated grey palette only, resigned expression, no warm accent light`

---

## 1. Cuisine en service, sans — pour C2′

> Documentary handheld footage, `<<<c841147a-6375-4c5e-b146-e45c1cab7e99>>>` the same chef in a white jacket during a busy lunch service, standing between three separate paper order sources — a spike of impaled tickets, a handwritten notepad on the counter, and a small tablet propped against a fridge — turning his head from one to the other trying to reconcile them, tired and rushed, harsh flat overhead neon, no colour accent, handheld with slight instability, 35mm. *(+ clause)*

**Ce qu'il doit dire :** trois sources qui ne se recoupent pas, et un homme qui
fait le recoupement à sa place.

## 2. Salle en service, sans — pour S2′

> Documentary handheld footage, `<<<a8f9dfa9-47cf-4ba3-86f8-93ab0b4a11c1>>>` the same female server in a black shirt and navy half-apron during service, writing an order on a small paper notepad, then walking to a counter and retyping the same order into a terminal, visible impatience, flat overcast light through the windows, desaturated, no warm tones, 35mm handheld. *(+ clause)*

**Ce qu'il doit dire :** le même geste fait deux fois. Le plan doit contenir la
répétition, pas seulement la fatigue.

## 3. Direction pendant le service, sans — pour D2′

> Documentary handheld footage, `<<<2f3b8e65-a41d-429a-abf7-5df04baddf7a>>>` the same restaurant manager alone in a small cluttered office during service hours, phone pressed to his ear with one hand while scrolling a laptop with the other, papers spread out, a second phone lighting up unanswered on the desk, cold grey daylight from a small window, no warm light, resigned, 35mm. *(+ clause)*

**Ce qu'il doit dire :** il n'est pas au service, et le service ne lui parvient
que par des canaux qui s'interrompent.

## 4. Réception de livraison, sans — pour C1′

> Documentary handheld footage, `<<<c841147a-6375-4c5e-b146-e45c1cab7e99>>>` the same chef in a receiving area early morning, holding a clipboard with a paper form, writing temperatures by hand next to stacked delivery crates, a pen behind his ear, a thermometer resting on a carton, breath faintly visible, harsh cold neon, flat and desaturated, 35mm. *(+ clause)*

**Ce qu'il doit dire :** le relevé existe. Il est sur du papier, et il restera
sur du papier.

## 5. Salle avant l'ouverture, sans — pour S1′

> Documentary static shot of a restaurant host stand before opening, a thick paper reservation book open with crossed-out and overwritten lines, a dozen sticky notes stuck around it in no order, a corded phone off its cradle, no people in frame, flat cold morning light, desaturated grey palette, 50mm, shallow depth of field. *(+ clause)*

**Ce qu'il doit dire :** trois listes pour un seul soir. Le désordre doit être
lisible, pas pittoresque.

## 6. Clôture de caisse, sans — pour S3′

> Documentary top-down shot at closing time, a pair of hands sorting three separate piles on a counter — cash, meal vouchers, and an envelope of tips — a paper till roll unspooled across the surface, a pocket calculator, one hand pausing mid-count, single dim overhead lamp, everything else dark, desaturated, no warm tones, 50mm. *(+ clause)*

**Ce qu'il doit dire :** trois piles, un seul total attendu, et l'écart qui ne
sera jamais expliqué. La photo `comptoir-fin-service` couvre déjà le sujet en
fixe ; c'est le mouvement de la main qui s'arrête qui manque.

---

## Plans déjà utilisés — à ne pas régénérer

Ils sont dans la bibliothèque, récupérés et étalonnés par `_serie/plans-sans.sh`
et `_serie/photos-sans.sh` :

**Animés (13)** — sans-cahier · sans-tablettes · sans-onglets ·
cuisine-vide-matin · cuisine-vide-nuit · couloir-cuisine · salle-chaises ·
salle-prete · salle-apres · imprimante-z · tickets-empiles ·
telephone-comptoir · bureau-matin · devanture-nuit

**Photos (5)** — cahier-spirale · ticket-au-sol · comptoir-fin-service ·
tablettes-depareillees · sept-onglets
