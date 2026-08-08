# C2 · Cuisine — pendant le service

Deuxième film de la série. Il reprend la grammaire fixée par C1 : fond crème
de la charte du site, cadre écran 1560 px, coches orange en rangée sous
l'écran, liseré cuisine `#059669`.

Couvre les 10 étapes de la phase « pendant » du parcours cuisine, 12h00 →
19h00 (`src/data/journees.ts`).

## Voix off (verbatim)

Midi. Les premières commandes tombent. À partir de maintenant, tout se joue à
la minute, et plus rien ne s'écrit sur un carnet.

J'affiche mon écran de cuisine, poste par poste. Chaud, pass, froid : chacun
voit ce qui le concerne, et rien d'autre. Quinze tickets en attente, l'heure
de chacun, la table de chacun.

Les commandes arrivent de partout. La salle, le comptoir, le site, les
plateformes de livraison. Elles entrent toutes au même endroit, dans le même
ordre, avec la même horloge. Je n'ai plus trois écrans à surveiller : j'en ai
un seul.

Je fais avancer les plats, un geste par plat. La salle sait où j'en suis sans
venir me le demander, et le client sait quand il mange.

Un plat en rupture ? Je le retire une fois. Il disparaît de la carte, du site
et des plateformes en même temps.

Dix-huit heures. Je pointe mon retour, je reprends mes températures, et je
regarde ce que la soirée annonce.

PrediBot a lu mes trois dernières semaines. Il me dit ce qui va sortir ce
soir, et en quelle quantité. Je valide ma production complémentaire avant le
coup de feu, pas pendant.

Dix-neuf heures. Je relance mon écran. Le service du soir peut commencer.

## Étapes couvertes

| Heure | Étape | Écran |
|---|---|---|
| 12h00 | J'ouvre mon fond de caisse | ⬜ à tourner — non montré |
| 12h10 | J'affiche mon écran cuisine par poste | KDS (config) |
| 12h15 | Je vois arriver les commandes de tous les canaux ★ | COMMANDES |
| 12h20 | Je fais avancer les plats sur le KDS | KDS (tableau en direct) |
| 13h30 | Je passe un plat en rupture ★ | ⬜ aucune fiche — traité en voix off seule |
| 18h00 | Je pointe mon retour | (repris de C1) |
| 18h05 | Deuxième relevé de température | (repris de C1) |
| 18h10 | Je regarde ce que PrediBot annonce | PREDIBOT |
| 18h30 | Je valide ma production complémentaire | PRODUCTION |
| 19h00 | Je relance mon KDS pour le soir | KDS (tableau en direct) |

Deux étapes sur dix n'ont pas d'écran disponible. Elles ne sont pas
escamotées : la voix les dit, et l'image reste sur le plan précédent plutôt
que d'inventer une interface qui n'existe pas.

## Sources écran

| Réf | Tutoriel | Remarque |
|---|---|---|
| `KDS` | `foodeatup-kds-par-poste-tuto` | 49,16 s — contient **et** l'écran de configuration **et** le tableau en direct |
| `COMMANDES` | `foodeatup-mes-commandes-tuto-v1` | 30,88 s — fourni par Michael, S3 le refuse (403) |
| `PREDIBOT` | `foodeatup-predibot-previsions-tuto-v1` | 42,48 s |
| `PRODUCTION` | `foodeatup-valider-une-production` | 47,00 s — déjà utilisé dans C1, autre fenêtre |

⚠️ Le catalogue donne pour `gerer-une-commande-en-direct-kds` une URL qui
pointe en réalité sur un tutoriel d'abonnement et de paiement Stripe. Vérifié
image par image. Le tableau KDS en direct est prélevé dans `KDS`, qui le
contient — voir `sources-video.json`, section `mauvaisMapping`.
