# Habillage Plan'It — trois gabarits réutilisables

Ouverture, bulle de présentation, fin. Ce sont les trois plans qui encadrent
**toutes** les vidéos Plan'It. Ils vivent ici, hors des épisodes, pour être
réutilisés tels quels : une série de tutoriels, une annonce produit, une
capsule marketing prennent le même habillage sans le réécrire.

Format commun : **1080 × 1920, 30 fps, H.264 High, yuv420p, CRF 18.**

| Gabarit | Durée | Son | Fichier |
|---|---|---|---|
| Ouverture | 3,6 s (fixe) | muet | `ouverture.py` |
| Présentatrice | celle de la voix | voix off intégrée | `presentatrice.py` |
| Fin | 5,2 s (fixe) | muet | `fin.py` |

---

## Se servir des gabarits

### En Python

```python
from pathlib import Path
from habillage import (Ouverture, rendre_ouverture,
                       Presentatrice, rendre_presentatrice,
                       Fin, rendre_fin)

rendre_ouverture(Ouverture(titre="Brancher un MCP", numero=13),
                 Path("out/intro.mp4"))

rendre_presentatrice(
    Presentatrice(titre="Brancher un MCP",
                  promesse="Vos logiciels métier deviennent utilisables par vos agents.",
                  numero=13, voix=Path("vo/N0.mp3")),
    Path("out/presenter.mp4"))

rendre_fin(Fin(suivant="Gérer ses connecteurs", couleur="#8236F8"),
           Path("out/outro.mp4"))
```

Le dossier `planit-academy` doit être sur le `sys.path` — c'est ce que fait
chaque `episode.py` :

```python
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))
```

### En ligne de commande

```bash
cd videos/planit-academy

python3 -m habillage ouverture --titre "Brancher un MCP" --numero 13
python3 -m habillage fin --suivant "Gérer ses connecteurs" --couleur "#8236F8"
python3 -m habillage presentatrice \
        --titre "Brancher un MCP" \
        --promesse "Vos logiciels métier deviennent utilisables." \
        --numero 13 --voix ../planit-tuto-13-brancher-un-serveur-mcp/vo/N0.mp3

python3 -m habillage --modules      # les couleurs de module
```

Sans `--sortie`, le rendu atterrit dans `./rendu/<gabarit>.mp4`.

---

## Ce que fait chaque gabarit

### Ouverture — `Ouverture(titre, numero=None, chapeau=None, marque="Plan'It")`

Fond dégradé de marque (rose → violet, de haut en bas), balayé par une bande de
lumière oblique. Puis, dans l'ordre :

| à | élément | mouvement |
|---:|---|---|
| 0,25 s | logo blanc | tombe de 190 px, `ease_out_back` |
| 0,85 s | mot-marque « Plan'It », Sora 800 / 168 | monte de 52 px |
| 1,25 s | filet blanc | s'ouvre depuis le centre |
| 1,50 s | titre court, Sora 700 / 88 | monte de 44 px |
| 1,95 s | puce « ACADÉMIE PLAN'IT · TUTORIEL NN » | monte de 34 px |
| 3,15 s | fondu vers le lavande `#EDEAFE` | enchaîne sans coupure |

Le titre et la puce se réduisent automatiquement s'ils sont trop longs
(`fitted`), jusqu'à 14 px. Aucun texte ne déborde.

### Présentatrice — `Presentatrice(titre, promesse, voix, numero=None, plan=…)`

Le seul gabarit dont la durée est libre : **elle vaut exactement celle du MP3
de voix off**. C'est la règle de la série — le plan suit la voix, jamais
l'inverse.

Le plan de l'avatar (`assets/avatar-generique.mp4`) est rendu **une seule fois
pour toute la série** puis bouclé en aller-retour, ce qui évite le saut d'un
raccord bout-à-bout. Le passer en `plan=` pour utiliser un autre avatar.

- **Enveloppe sonore** : le MP3 est décodé en mono 16 kHz, une valeur RMS par
  image, normalisée puis compressée en `x ** 0.55`. Cette courbe pilote le
  halo, le diamètre de l'anneau et les treize barres de niveau.
- **Anneau dégradé** rose → violet, dessiné arc par arc, en rotation continue
  (−26 °/s). Son épaisseur suit le niveau (16 → 28 px).
- **Voile de bord** : le plan de l'avatar arrive sur fond gris studio. Un
  détourage par `colorkey` est exclu — c'est un rendu 3D plein de tons neutres
  et la clé mange cheveux, peau et col. Un dégradé radial fond donc le pourtour
  vers le lavande de la marque sans jamais toucher le visage.
- Le titre arrive à 1,0 s, la promesse à 1,35 s (retour à la ligne
  automatique), la pastille du numéro à 1,7 s.

### Fin — `Fin(suivant="", couleur="#4F2DF9", baseline=…)`

Même dégradé, monté à l'envers (violet → rose). On entre depuis le lavande de
l'application, en fondu de 0,4 s.

| à | élément |
|---:|---|
| 0,15 s | logo blanc |
| 0,65 s | « Vous planifiez une fois. » |
| 1,05 s | « Vos agents s'occupent du reste. » |
| 1,50 s | filet blanc |
| 1,85 s | baseline, en pastille blanche **teintée de la couleur du module** |
| 2,35 s | « Tutoriel suivant · … » — masqué si `suivant` est vide |

---

## Les tokens de marque

Tout est dans `noyau.py`, repris de `lib/core/theme/app_colors.dart` du dépôt
`PrendsTaPart/planit-app`. **Ne pas les redéfinir ailleurs.**

| Token | Valeur |
|---|---|
| `PRIMARY` | `#4F2DF9` |
| `PRIMARY_BUTTON` | `#8236F8` |
| `ACCENT` | `#FE64D5` |
| `BACKGROUND_PAGE` | `#EDEAFE` |
| `TEXT_DARK` | `#0B0516` |
| `BUBBLE_EDGE` | `#DCD2FA` |

`BRAND_GRADIENT` est la rampe à neuf paliers de `#FE64D5` à `#4F2DF9`.

Couleurs de module, telles que le MCP les renvoie :

| Module | Couleur |
|---|---|
| Prompts | `#772FF3` |
| Tâches | `#6A2EF5` |
| Connexions API & MCP | `#8236F8` |
| Base de connaissance | `#A63FE8` |
| Skills & Plugins | `#B846E0` |
| Authentification | `#4F2DF9` |

Polices : **Sora** (600/700/800) pour les titres, **Manrope** (400/500/600/700)
pour le texte courant, dans `videos/_shared/fonts/`.

---

## Les fichiers

```
habillage/
├── noyau.py           tokens, courbes, primitives de composition, encodage
├── ouverture.py       gabarit « Ouverture »
├── presentatrice.py   gabarit « Présentatrice »
├── fin.py             gabarit « Fin »
├── __main__.py        ligne de commande
└── README.md          ce fichier

../assets/
├── white_logo.png            logo sur fond de marque (ouverture, fin)
├── black_logo.png            logo sur fond clair (présentatrice)
├── avatar-generique.mp4      plan de l'avatar qui parle
├── avatar-presentatrice.png  portrait fixe, pour les vignettes
└── audio/                    sting d'entrée, signature de fin, musique
```

---

## Règles à ne pas casser

1. **Un plan dure exactement sa ligne de voix off.** La vitesse du plan en
   découle ; aucune durée n'est fixée au jugé.
2. **Aucune ligne de voix off ne dépasse 6 secondes.** Au-delà, elle déborde de
   son plan et le décalage s'accumule.
3. **Zéro génération Higgsfield.** Tout l'habillage est dessiné avec Pillow +
   ffmpeg à partir des tokens de l'application. Règle du dépôt.

---

## Vérifier après modification

Les trois gabarits sont déterministes : à réglages égaux, le MP4 est identique
au bit près. C'est le contrôle le plus simple après un changement.

```bash
cd videos/planit-tuto-13-brancher-un-serveur-mcp
python3 episode.py
git status --short out/        # aucune ligne = rendu inchangé
```

---

## Le catalogue en ligne

`catalogue.html` est une page autonome — aperçus animés des trois gabarits,
images-clés, tokens, code à copier. Aucune dépendance externe hors Google
Fonts : logo et aperçus vidéo sont embarqués. L'ouvrir directement dans un
navigateur, ou la republier telle quelle.

Elle est publiée ici :
<https://claude.ai/code/artifact/2f9a3e67-2cd3-4045-865f-586526429927>

Après un changement d'habillage, régénérer les aperçus puis la page :

```bash
# 1. rendre les trois gabarits
cd videos/planit-academy
python3 -m habillage ouverture --titre "Brancher un MCP" --numero 13 --sortie /tmp/intro.mp4
python3 -m habillage fin --suivant "Gérer ses connecteurs" --couleur "#8236F8" --sortie /tmp/outro.mp4
python3 -m habillage presentatrice --titre "Brancher un MCP" \
        --promesse "Vos logiciels métier deviennent utilisables." --numero 13 \
        --voix ../planit-tuto-13-brancher-un-serveur-mcp/vo/N0.mp3 --sortie /tmp/presenter.mp4

# 2. réduire pour l'embarquement (≈ 30 Ko pièce)
for f in intro outro presenter; do
  ffmpeg -y -v error -i /tmp/$f.mp4 -an -vf "scale=288:512:flags=lanczos" \
         -c:v libx264 -profile:v main -pix_fmt yuv420p -crf 30 /tmp/apercu-$f.mp4
done

# 3. remplacer les data URI correspondantes dans catalogue.html
```
