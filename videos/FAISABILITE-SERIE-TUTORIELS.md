# Faisabilité — série de tutoriels produit depuis le Drive

Audit du dossier Drive `1LpWivm0KEPwX5XhNHiw08426NjT6PXHC` réalisé le 2026-08-02.
Objectif : déterminer si les ~107 vidéos annoncées peuvent être produites avec le
pipeline décrit dans `FOODEATUP-TUTORIELS-WORKFLOW.md`.

**Verdict court** : le contenu est là — 91 dossiers sur 92 ont les assets nécessaires.
Mais il n'y a **pas 107 vidéos dans le Drive, il y en a 92**, et deux points bloquants
opérationnels (ingestion des rushes, coût unitaire du montage) doivent être traités
avant de lancer la série. Détail ci-dessous.

---

## 1. Inventaire réel — d'où vient l'écart avec 107

| Module | Nom du dossier | Annoncé | Sous-dossiers réels |
|---|---|---:|---:|
| 1 | MODULE CONFIGURATION | 14 | **12** |
| 2 | MODULE ÉQUIPE & PLANNING | 20 | 20 |
| 3 | MODULE COMPTABILITÉ | 10 | 10 |
| 4 | MODULE HACCP | 30 | 30 |
| 5 | MODULE STOCKVISION AI | 20 | 20 |
| | **Total** | **94** | **92** |

Deux écarts distincts :

- **94 vs 107** — le chiffre 107 ne correspond à rien de trouvable dans le Drive.
  Même en additionnant les intitulés de dossiers on tombe à 94. Les 13 vidéos
  d'écart sont soit un module non encore partagé, soit un décompte incluant des
  déclinaisons (formats 9x16 / TikTok ?) qui ne sont pas dans cette arborescence.
  **À clarifier avant de planifier.**
- **94 vs 92** — le module 1 annonce 14 vidéos mais ne contient que 12 dossiers :
  la numérotation saute le **7** et le **12** (elle va 6 → 8 et 11 → 13). Les deux
  sujets correspondants n'existent pas dans le Drive.

Le périmètre réellement productible aujourd'hui est donc **92 vidéos**, pas 107.

---

## 2. Complétude des assets — 91/92

Le pipeline a besoin de 3 intrants par vidéo : carte d'intro, enregistrement d'écran,
carte de fin. Vérification faite dossier par dossier sur les 92 :

| Module | Dossiers | Carte intro | Enregistrement écran | Prêts à monter |
|---|---:|---:|---:|---:|
| 1 — Configuration | 12 | 12 | 12 | **12** |
| 2 — Équipe & Planning | 20 | 20 | 20 | **20** |
| 3 — Comptabilité | 10 | 10 | 9 | **9** |
| 4 — HACCP | 30 | 30 | 30 | **30** |
| 5 — StockVision AI | 20 | 20 | 20 | **20** |
| | **92** | **92** | **91** | **91** |

**Le seul trou réel** : module 3, dossier `2- Ajout et modifications/Suppression d'un client`.
Il contient bien la carte d'intro (`GÉRER SES CLIENTS CÔTÉ VENTES.png`), la carte de fin
et le clip avatar `Script_2_-_on_gère_vos_clients.mp4`, **mais aucun enregistrement d'écran**.
Cette vidéo est bloquée tant que le rush n'est pas déposé.

La carte de fin (`page fin vid.jpg`, 174 269 octets, strictement identique partout) manque
dans une partie des dossiers du module 4 — **non bloquant** : c'est un asset unique et
réutilisable, déjà présent dans le dépôt (`videos/*/assets/outro.jpg`).

---

## 3. Anomalies à faire vérifier

1. **Module 4 (HACCP) n'a aucun clip avatar.** Les modules 1, 2, 3 et 5 contiennent
   systématiquement un `Script N - ..._1080p.mp4` (~2–4 Mo, avatar parlant pré-généré).
   Les 30 dossiers HACCP n'en ont aucun. Si ce plan avatar fait partie du format
   cible, il manque 30 clips à produire. Si le format est « carte intro + écran
   commenté en voix off » (celui des 4 tutos déjà livrés), ce n'est pas un problème.
   **À trancher.**

2. **Doublon probable module 2.** Les enregistrements des dossiers 14
   (`Affichages de l'interface d'accueil des employés...`) et 15
   (`Gestion des pauses, pointage...`) font exactement la même taille au
   octet près : **31 001 599 octets**. C'est très probablement le même fichier
   déposé deux fois — le rush du 14 serait alors le mauvais. À vérifier avant montage.

3. **Deux propriétaires distincts** sur les fichiers (`cocuisinage.social@gmail.com`
   et `toumi.mouna07@gmail.com`), avec deux conventions de nommage
   (`video-NN <titre>.mp4` vs `<titre>.mp4`). Sans impact technique, mais il faudra
   une règle de résolution automatique pour identifier « le » rush d'un dossier.

---

## 4. Chaîne technique — ce qui marche, ce qui bloque

### Ce qui est validé
- **ffmpeg / ffprobe** : absents de l'image par défaut, mais `apt-get update && apt-get install -y ffmpeg`
  fonctionne (v6.1.1 installée et testée pendant cet audit). À intégrer dans un hook
  de démarrage pour ne pas le refaire à chaque session.
- **Chaîne voix off — validée de bout en bout.** Test réel effectué : génération via
  le MCP ElevenLabs (voix Adam FR `TGAegA0zNRi8I6nUdq3i`, `eleven_multilingual_v2`),
  puis téléchargement du MP3 dans le conteneur et lecture par `ffprobe` (2,69 s,
  60 151 octets). Le MCP renvoie un lien signé sur `storage.googleapis.com`, hôte
  **autorisé** par la politique réseau. Aucun obstacle sur ce maillon.
- **Moteur de montage** : `build.py` est éprouvé — les pièges connus (zoompan qui gèle
  l'image, `loudnorm` sur mix composite, `alimiter` sans `level=disabled`) sont
  documentés et corrigés.
- **Lecture du Drive** : le MCP Google Drive liste et lit correctement toute
  l'arborescence.

### Ingestion des rushes : ce n'est pas un mur réseau, c'est un manque d'identifiants

Le point à traiter, mais il est plus simple qu'il n'y paraît. Résultats des tests
de joignabilité depuis le conteneur :

| Hôte | Statut | Lecture |
|---|---|---|
| `www.googleapis.com` | 404 | **joignable** (API Drive) |
| `oauth2.googleapis.com` | 404 | **joignable** |
| `accounts.google.com` | 302 | **joignable** |
| `storage.googleapis.com` | 400 | **joignable** |
| `drive.google.com` | — | bloqué (403 au CONNECT) |
| `api.elevenlabs.io` | — | bloqué (403 au CONNECT) |

Seul l'hôte **web** `drive.google.com` est bloqué. L'**API** Drive, elle, répond
parfaitement : un appel à
`https://www.googleapis.com/drive/v3/files/<id>?alt=media` sans authentification
renvoie un `403 "The request is missing a valid API key"` — c'est-à-dire une vraie
réponse applicative Google, pas un refus du proxy.

**Conséquence : il suffit d'identifiants.** Avec un compte de service Google (ou un
client OAuth) ayant accès en lecture au dossier partagé, les ~2,3 Go de rushes se
téléchargent directement dans le conteneur avec un simple script, sans rclone ni
accès à l'interface web. C'est quelques dizaines de lignes, pas un chantier.

À éviter en revanche : `download_file_content` du MCP Drive, qui renvoie le fichier
**en base64 dans le contexte du modèle** — un rush de 30 Mo ≈ 40 Mo de base64, hors
de portée d'une fenêtre de contexte. Ce canal ne convient qu'aux cartes JPG (~250 Ko).

**Ce qu'il faut fournir** : un JSON de compte de service, partagé au dossier Drive
en lecture, déposé comme secret d'environnement (jamais dans le dépôt).

### Note sur la clé API ElevenLabs

`api.elevenlabs.io` étant bloqué par la politique réseau, une clé API en clair est
**inutilisable directement** depuis cet environnement — et de toute façon inutile :
le MCP ElevenLabs couvre déjà le besoin et son résultat est téléchargeable (testé
ci-dessus). Aucune clé ne doit être stockée dans ce dépôt.

---

## 5. Le vrai coût : le montage n'est pas générique

C'est le point le plus important pour estimer le délai, et il est facile à sous-estimer.

`build.py` **n'est pas un template réutilisable en l'état**. Chaque vidéo demande
des valeurs déterminées à la main en regardant le rush image par image :

```python
BTN_EDIT_INFO = (1617, 267)   # coordonnées pixel du bouton cliqué
segs = [
    ("A", 0.0, 2.5,  0.69, None, None),          # découpe + facteur de vitesse
    ("B", 2.5, 2.8,  0.60, 2.5,  BTN_EDIT_INFO), # instant exact du clic
    ...
]
anchor = {"N0": 0.30, "N1": boundary["A"] + 0.20, ...}  # calage de chaque ligne VO
```

Soit, par vidéo : extraction de frames pour reconstituer le déroulé, relevé des
timestamps et des coordonnées de chaque clic, calcul des facteurs de vitesse pour
que chaque segment dure exactement le temps de la ligne de voix off qui le commente,
écriture du script, **validation obligatoire avec Michael avant génération audio**,
TTS, montage, contrôle du pic audio sur le fichier encodé, vignette, publication CMS.

Sur les 92 vidéos, **4 sont déjà livrées** (abonnement, profil entreprise, unités,
fournisseurs — toutes du module 1). Il en reste **87 productibles + 1 bloquée**.

À ce rythme artisanal, 88 vidéos représentent un volume de travail hors de proportion
avec un traitement « en une passe ». Deux leviers changent l'équation :

- **Paramétrer le moteur.** Sortir `build.py` en moteur partagé piloté par un
  `spec.json` par vidéo (segments, clics, ancres VO). Le travail unitaire retombe
  alors à : analyser le rush → écrire le spec → écrire le script. Le code de montage,
  lui, ne se réécrit plus. C'est le prérequis à toute production en série.
- **Grouper les validations.** L'étape « STOP validation script » est séquentielle et
  bloque tout. La passer en validation par lot (les 20 scripts d'un module d'un coup)
  supprime le principal temps d'attente.

---

## 6. Recommandation

La série est **faisable sur 91 vidéos**, pas 107. Dans cet ordre :

1. **Clarifier le périmètre** — d'où viennent les 107 ? Les 13 manquantes sont-elles
   un module non partagé, ou des déclinaisons 9x16 ?
2. **Fournir un compte de service Google** en lecture sur le dossier partagé (§4).
   C'est le seul prérequis d'infrastructure, et il est léger.
3. **Trancher la question du plan avatar** sur HACCP (§3.1).
4. **Faire déposer le rush manquant** du module 3 / dossier 2, et vérifier le
   doublon du module 2 (dossiers 14 et 15).
5. **Industrialiser le moteur** (`spec.json` + build partagé) sur un module pilote —
   le module 3 (10 vidéos, 9 prêtes) est le bon candidat : petit, homogène, et ses
   rushes sont parmi les plus légers.
6. Puis dérouler module par module, en validant les scripts par lot.
