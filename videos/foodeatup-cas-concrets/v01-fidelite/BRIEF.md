# Vidéo 1 — 250 couverts, 10 fidèles

Statut des 4 segments (2026-08-09) :

| Segment | Durée | Statut | Détail |
|---|---|---|---|
| HOOK | 0–3s | ✅ prêt | `../motion/renders/hook-intro.mp4` (déjà instancié sur cette vidéo) |
| PROBLÈME (Higgsfield) | 3–11s | ✅ reçu | `assets/higgsfield/probleme.mp4` — chef de dos, salle qui se vide, clients qui partent. 720×1280, 24fps, 10.08s (à recadrer sur ~8s au montage). Palette plus chaude que demandé (grise/désaturée dans le prompt) mais cadrage et action conformes — utilisable tel quel. |
| SOLUTION (capture écran) | 11–25s | ⏳ en attente | Drive `Créer un programme fidélité.mp4` (11,6 Mo, > limite 10 Mo de l'outil Drive de cette session) — à déposer directement dans le chat |
| RÉSULTAT (HeyGen) | 25–33s | ⏳ en attente | script ci-dessous, avatar Mika (voir `studio-video/CLAUDE.md`) — clé reçue et stockée (`studio-video/.env`), **mais `api.heygen.com` est bloqué par la politique réseau de cette session** (proxy : 403 sur le CONNECT, host non autorisé) ; je ne peux pas appeler l'API depuis ici. À générer manuellement dans HeyGen Studio (avatar Mika) puis déposé ici, comme pour Higgsfield. |
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

## À déposer ici au fur et à mesure

- `assets/higgsfield/probleme.mp4` — le rendu Higgsfield une fois généré
- `assets/solution/programme-fidelite.mp4` — la capture écran Drive (ou je la récupère si
  un lien de partage public est fourni)
- `assets/heygen/resultat.mp4` — le clip avatar HeyGen une fois généré

Dès qu'un de ces 3 fichiers est déposé dans le chat, je le range ici et j'avance le montage.
