# Ce qu'il reste à faire — 30 août 2026, fin de session

## Où on en est

| Pièce | Présent | Sur 367 |
|---|---:|---:|
| Plan Higgsfield | **264** | 367 |
| Story 10 s | 240 | 367 |
| Short YouTube | 240 | 367 |
| Paysage 16:9 | 240 | 367 |
| Facebook | 240 | 367 |
| TikTok | 240 | 367 |
| Master 37,5 s | 90 | 367 |

**Les cinq déclinaisons sont maintenant complètes pour tout épisode qui a une
story.** Il n'y a plus un seul trou de montage en aval : 154 Shorts, 8 paysages,
22 Facebook et 22 TikTok ont été montés depuis les stories existantes, sans une
seule génération. Ce qui manque est en amont — le plan, puis le master.

## 1. Cent trois plans Higgsfield à générer

C'est le seul poste qui coûte des crédits, et le seul verrou réel : sans plan,
pas de story, donc aucune des cinq déclinaisons.

| Série | Saison | À générer |
|---|---|---:|
| Le Coup de Feu | S8 — Dis-le, c'est fait | 28 |
| Le Coup de Feu | S7 — Les Végé-Fruités font leur cinéma | 25 |
| Le Coup de Feu | S6 — L'orchestration du restaurant | 21 |
| L'IA dans FoodEatUp | S3 — Brancher, et faire tourner | 12 |
| L'IA dans FoodEatUp | S1 et S2 | 9 |
| Michael fait son cinéma | S1 — les six derniers | 6 |
| Le Coup de Feu | S4 et S5 | 3 |

**Cent cinq de ces épisodes n'ont pas encore de prompt écrit.** C'est le travail
qui précède la génération, et il ne coûte rien.

Avant de lancer quoi que ce soit, deux règles tirées de la saison 1 : le clip
doit tenir **un seul plan sur 9,5 s** — cinq clips sur vingt-quatre enchaînaient
sur un deuxième cadre entre 7,2 et 8,5 s — et le temps fort doit tomber à
**5,0 s**, c'est là que la punchline entre.

## 2. Deux cent soixante-dix-sept masters

Cinquante-quatre épisodes ont leur plan mais pas leur master : il leur manque le
screencast ou l'avatar. Trente-deux attendent un tournage — les modules Caisse
POS, HubRise et KDS n'ont que des JPG dans le Drive. Le reste suit
mécaniquement les plans du point 1.

Les vingt-quatre épisodes de « Michael fait son cinéma » dont les plans viennent
d'être récupérés n'ont pas encore de chaîne de montage : la série est faite de
deux plans de dix secondes plus dix secondes de démonstration, ce n'est pas
l'anatomie du Coup de Feu. Un `build-cinema.sh` reste à écrire.

## 3. Trois voix qui contredisent leur montage

| Épisode | Ce qui dit encore « dix » |
|---|---|
| EP010 | punchline ElevenLabs |
| EP013 | script HeyGen de l'avatar |
| EP022 | punchline ElevenLabs |

Ils sont montés dans leur état cible et marqués `a_refaire`. Ils ne doivent pas
être publiés avant que la voix ait rattrapé le texte, et leurs masters n'ont
volontairement **pas** été poussés dans la bibliothèque : l'ancienne version est
la seule qui soit cohérente avec elle-même.

Bloquant : **l'identifiant de la voix des punchlines n'est écrit nulle part**.
`config/voices.json`, que le brief 08 réclame, n'existe pas. Réglages figés par
ailleurs : `eleven_multilingual_v2`, stability 0.55, similarity 0.80, style
0.15, speaker boost, `mp3_44100_128`.

## 4. Six cent soixante-cinq pièces encore sur GitHub

Le Short est réglé : **les 232 sont sur la bibliothèque**, et les vingt et un
masters remontés de la saison 1 y ont été réécrits en place — même adresse,
nouvelle version. Restent le paysage 16:9, Facebook et TikTok, à un fichier sur
218 chacun, plus les stories et les masters des autres saisons.

La bascule passe par un appel par fichier — il n'y a pas de mode lot côté
RapidoCMS. Le nommage à respecter, relevé sur l'existant :

| Pièce | Nom dans la bibliothèque |
|---|---|
| master | `FoodEatUp-{EP}-{titre}` |
| story | `story-{EP}` |
| Short YouTube | `yt-{EP}` |
| paysage 16:9 | `yt16-{EP}` |
| Facebook | `fb-{EP}` |
| TikTok | `tk-{EP}` |

## 5. La diffusion

**YouTube** : 5 épisodes publiés, 30 planifiés — UpEatFood est bouclé jusqu'au
1er octobre. Restent **197 Shorts** à planifier, un appel par vidéo, à la date du
calendrier. Le quota est la contrainte dure : 10 000 unités par jour, 1 600 par
envoi, six vidéos par jour maximum. Le mode `upload_at_time` fait porter le coût
au jour de diffusion, pas au jour de planification.

**Facebook, Instagram, TikTok, LinkedIn** : rien n'est planifié, et rien ne peut
l'être avant le point 4. Le catalogue impose en plus un verrou humain — une
pièce doit passer en `valide` par quelqu'un qui l'a regardée en entier ; aucun
outil n'écrit cet état, et c'est voulu.

## 6. Les arbitrages de montage laissés ouverts

Détaillés dans `AUDIT-MONTAGE-SAISON-1.md` : la fin à neuf secondes (deux
cartons de marque à la suite, 24 % de l'épisode), le carton du milieu (6,2 s
figées sur 9), et le screencast incrusté trop petit pour se lire sur un
téléphone. Les trois touchent les gabarits communs, donc les 150 épisodes d'un
coup.
