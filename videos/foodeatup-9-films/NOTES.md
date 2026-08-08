# « Une journée avec FoodEatUp » — notes de production

Série de 9 films : 3 métiers (cuisine / serveur / directeur) × 3 phases
(avant / pendant / après le service). Spécification de référence : **v3**
(dossier de Michael, 2026-08-08). Ce fichier consigne ce qui est décidé,
ce qui est vérifié, et ce qu'il reste à obtenir.

---

## 1. État au 2026-08-08

| Chantier | État |
|---|---|
| Modèle de données des 3 parcours | ✅ en ligne — `foodeatup-guide-star/src/data/journees.ts` |
| Pages `/journee` et `/journee/:slug` | ⬜ à écrire |
| Les 66 captures d'écran | 🟡 sources identifiées, voir §3 |
| Les 42 images d'ambiance IA | ⬜ à générer (RapidoCMS) |
| Les 9 pistes voix off | ⬜ à générer (ElevenLabs) |
| Pipeline Remotion | ⬜ palier P1 non démarré |

**Parcours figés (107 étapes)** — cuisine 46 (07h00→23h00), salle 32
(09h30→23h00), direction 29 (08h00→18h00). Les 75 slugs référencés existent
tous dans le catalogue. Chronologie vérifiée **par bloc**, pas globalement.

---

## 2. Décisions

- **Les vidéos de caisse se tournent en dernier.** Le module Caisse POS est
  `comingSoon` dans `tutorials.ts`. Les six étapes salle qui en dépendent
  (fond de caisse, encaissement, séparation d'addition, remise, ticket Z midi
  et soir, écarts) s'affichent « bientôt disponible » et **se rallumeront
  d'elles-mêmes** le jour où le module s'ouvre — aucun code à retoucher.
- **Les 66 captures ne se refilment pas.** Elles se prélèvent dans les vidéos
  de tutoriels déjà en ligne : ce sont des enregistrements réels de
  l'interface, ce que la règle « aucune interface générée par IA » exige.
- **Les films ne portent pas encore d'URL.** `PhaseFilm.plannedFile` contient
  le nom de fichier attendu ; `videoUrl` reste vide tant que le fichier n'est
  pas dans la bibliothèque, pour ne jamais afficher un lecteur cassé.

---

## 3. Sources des 66 captures — ce qui est récupérable, ce qui manque

Le catalogue (`CATALOGUE-TUTORIELS.md`) donne l'URL S3 de chaque tutoriel.
Attention : **l'URL ne se déduit pas du slug** (`creer-son-compte` →
`foodeatup-inscription-tuto-v1`). L'inventaire résolu est dans
`sources-video.json`.

Sur les 75 vidéos dont les 9 films ont besoin :

| | Nombre | Suite |
|---|---|---|
| ✅ Téléchargeables directement depuis S3 | **67** | rien à faire — je les récupère et j'y prélève les séquences |
| 🔒 Accès refusé (403) | **2** | à rendre lisibles, voir ci-dessous |
| ⬜ Aucune vidéo (module Caisse POS + 5 sujets neufs) | **6** | tournage prévu en dernier |

### 3.1 — Les 2 vidéos à débloquer

Ces deux fichiers sont référencés dans le catalogue mais renvoient `403` sur
S3. Ce sont les deux seules dont j'ai besoin et que je ne peux pas atteindre.

| Slug | Fichier S3 | Sert aux plans |
|---|---|---|
| `mes-commandes-tous-canaux` | `foodeatup-mes-commandes-tuto-v1` | **C2 — convergence multi-canal** (plan clé), S2 multi-canal salle |
| `retrouver-ses-reservations-du-jour` | `foodeatup-reservations-jour-tuto` | **S1 — réservations du jour** (plan clé), S3 reprise du soir |

Deux façons de les obtenir, au choix :
1. rendre ces deux objets publics dans le bucket, comme les 67 autres ;
2. les déposer dans le Drive — je les importerai via RapidoCMS.

C'est tout ce dont j'ai besoin côté captures. **Pas 22 vidéos : 2.**

### 3.2 — Les 6 vidéos qui n'existent pas encore

À tourner plus tard, dans cet ordre de priorité. Les cinq premières sont du
module Caisse POS ; la dernière est un sujet neuf.

| Fichier attendu | Sujet | Débloque |
|---|---|---|
| `cloturer-sa-caisse-v1.mp4` | Le ticket Z | S3 (plan clé), salle 14h30 et 22h30 |
| `ouvrir-son-fond-de-caisse-v1.mp4` | Fond de caisse | cuisine 12h00, salle 11h45 |
| `encaisser-une-commande-v1.mp4` | Encaissement comptoir | salle 12h10 |
| `separer-une-addition-v1.mp4` | Multi-paiement | salle 13h30 |
| `appliquer-une-remise-v1.mp4` | Remise et avoirs | salle 13h40 |
| `suivre-les-ecarts-de-caisse-v1.mp4` | Écarts de caisse | salle 14h40 |

Cinq autres étapes du parcours n'ont aucune fiche et restent en
« bientôt disponible » : mise en place (cuisine 07h40), production → caisse
(cuisine 11h05), plat en rupture (cuisine 13h30), plat indisponible
multi-canal (salle 11h00), validation de congé (direction 10h50).

---

## 4. Ce que je fournis, ce que Michael fournit

**Moi** — les 42 images d'ambiance (RapidoCMS, jamais d'interface), les 9
pistes voix off (ElevenLabs, une voix par métier), le prélèvement des 66
séquences dans les vidéos existantes, le pipeline Remotion, les pages Academy.

**Michael** — les 2 vidéos à débloquer (§3.1), les 6 tournages de caisse
(§3.2), et l'arbitrage sur les chiffres si les voix off doivent citer des
données réelles plutôt que des exemples.

---

## 5. Grammaire des 9 films (rappel v2/v3)

Ligne de temps bleue `#1E9BF0` en bas de cadre, jamais interrompue, même sur
les coupes. Liseré métier en haut : cuisine `#059669`, salle `#F59E0B`,
direction `#475569`. Écrans logiciel incrustés dans un cadre de tablette
incliné 6°, action démarrant 250 ms après l'apparition du cadre. Coches
orange `#FFA500` en trim path 200 ms, accumulées en colonne à droite.
Sous-titres burn-in au-dessus de la ligne de temps, 42 caractères, 2 lignes.
Musique en ré mineur sur les neuf : avant 90 BPM montant, pendant 124 BPM
tendu, après 76 BPM descendant. Ducking −9 dB, normalisation −14 LUFS.

**Palette des films** : `#1E9BF0` `#1B2A41` `#F7F9FC` `#FFA500` + les trois
couleurs métier. À ne pas confondre avec la palette du site Academy
(`#FCF9E6` `#0F1A23` `#007BFF` `#FFA500`).
