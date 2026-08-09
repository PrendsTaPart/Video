# Vidéo 1 — 250 couverts, 10 fidèles

Statut des 4 segments (2026-08-09) :

| Segment | Durée | Statut | Détail |
|---|---|---|---|
| HOOK | 0–3s | ✅ prêt | `../motion/renders/hook-intro.mp4` (déjà instancié sur cette vidéo) |
| PROBLÈME (Higgsfield) | 3–11s | ✅ reçu | `assets/higgsfield/probleme.mp4` — chef de dos, salle qui se vide, clients qui partent. 720×1280, 24fps, 10.08s (à recadrer sur ~8s au montage). Palette plus chaude que demandé (grise/désaturée dans le prompt) mais cadrage et action conformes — utilisable tel quel. |
| SOLUTION (capture écran) | 11–25s | ✅ reçu | `assets/solution/programme-fidelite.mp4` — capture horizontale 1920×828, 25fps, 28.76s, confirme bien l'écran "Fidélité & jeux" (points, multiplicateurs, Enregistrer le programme). À recadrer/zoomer en 9:16 et raccourcir à ~14s (2-3 gestes utiles + Enregistrer) au montage. |
| RÉSULTAT (HeyGen) | 25–33s | ⚠️ reçu, à refaire | `assets/heygen/resultat-v1-a-refaire.mp4` — voir "Problème sur le clip HeyGen reçu" ci-dessous |
| PUNCHLINE | 33–37s | ✅ prêt | `../motion/renders/punchline-outro.mp4` |

## Prompt Higgsfield à générer manuellement

Référence image 1 : `studio-video/assets/brand/profile/michael-chef-mascot.jpg`

```
Plan unique continu de 8 secondes, vertical 9:16, 4K, 24 images/seconde, style
documentaire, grain fin. Palette froide et désaturée : gris #8A9099, surfaces #EDEEF0,
encre #3A3F45. Lumière plate de néon, sans chaleur. Référence image 1 = photo du chef :
visage, morphologie et tenue à conserver strictement à l'identique. Son d'ambiance seul,
aucune voix, aucune musique. Aucune coupe, aucun personnage dupliqué, aucun texte à
l'écran, aucun logo, aucune marque ni application identifiable, aucun sous-titre.

Action : fin de service, le chef debout au comptoir regarde une salle qui se vide, les
tables se libèrent une à une, les clients sortent sans un mot ni un regard vers lui. Il
reste seul devant l'entrée.
Caméra : plan fixe depuis le fond de la salle, très légère avancée.
Son : chaises, porte, brouhaha qui s'éteint.
Fin de plan : la salle vide, lui de dos.
```

## Script HeyGen (avatar Mika)

```
Vidéo avatar de 8 secondes, format vertical 9:16, 1080 × 1920. Avatar : homme, la
quarantaine, veste de cuisine blanche col ouvert, cadrage buste, regard caméra. Décor :
cuisine professionnelle floutée en arrière-plan, tons chauds. Voix française masculine,
ton posé et direct, débit naturel, pas de ton commercial. Sous-titres désactivés — ils
sont ajoutés au montage. Aucun logo, aucun texte incrusté.

Script exact : « Tu ne perds pas des clients. Tu ne les reconnais pas. Le programme se
déclenche à la première visite, et le deuxième passage arrive tout seul. »
```

## Problème sur le clip HeyGen reçu (2026-08-09)

`assets/heygen/resultat-v1-a-refaire.mp4` (1080×1920, 25fps, 7.56s) — le chef Mika dit bien
le bon texte, la voix est bonne. Mais ce n'est pas un avatar "propre" comme demandé dans le
plan :

- Il ne parle que **~3 secondes** (« Tu ne perds pas des clients. Tu ne les reconnais
  pas. »), puis le clip **coupe sur un template graphique générique** HeyGen pendant les
  ~4,5s restantes : fond bleu, titre « FIDÉLITÉ AUTOMATIQUE », sous-titre « L'expérience
  client réinventée », photo stock d'une femme avec une tablette (pas un vrai visuel
  FoodEatUp), fin du texte incrustée dedans.
- **Logo FoodEatUp et sous-titres brûlés à l'image** sur toute la durée — le plan les veut
  ajoutés au montage, pas incrustés par HeyGen (pour rester dans notre propre habillage,
  cohérent avec le carton HOOK/PUNCHLINE déjà fait).

→ Ça vient du **type de génération choisi dans HeyGen Studio** : un mode "template/scene"
plutôt qu'un export "avatar seul". Pour la vidéo 1 (et pareil pour les 9 suivantes), il
faut régénérer en choisissant l'option **avatar seul / plan unique**, sans template de
scène ni sous-titres/logo intégrés — juste Mika qui parle les 8 secondes pleines, cadrage
buste, fond de cuisine flouté, comme décrit dans le script ci-dessus. C'est ce clip-là que
je monterai avec nos propres sous-titres et notre propre logo (déjà faits dans
`../motion/`).

## À déposer ici au fur et à mesure

- `assets/higgsfield/probleme.mp4` — le rendu Higgsfield une fois généré
- `assets/solution/programme-fidelite.mp4` — la capture écran Drive (ou je la récupère si
  un lien de partage public est fourni)
- `assets/heygen/resultat.mp4` — le clip avatar HeyGen une fois généré

Dès qu'un de ces 3 fichiers est déposé dans le chat, je le range ici et j'avance le montage.
