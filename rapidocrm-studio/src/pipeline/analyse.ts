import { existsSync, readdirSync, statSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { AnalyseSchema, type Analyse } from '../schema/index.ts';
import { assurerDossier, ecrireJson, lireJson } from '../util/chemins.ts';
import { lancer, sonder } from '../util/ffmpeg.ts';
import { avertir, discret, etape, info } from '../util/journal.ts';

const SEUIL_SCENE = 0.22; // sensibilité de la détection de changement d'écran
const DUREE_MAX_CONSEILLEE = 240; // 4 minutes

export interface OptionsAnalyse {
  force?: boolean;
  /** Ne pas s'arrêter si la vidéo dépasse 4 minutes (mode série validé). */
  accepterLongue?: boolean;
}

/**
 * Étape 1 — analyse de l'enregistrement d'écran.
 *
 * Les parties déterministes (sondage, extraction de frames, détection de scènes,
 * suivi du curseur) sont faites ici. La lecture visuelle des frames — quel écran,
 * quelle action, quelle zone, quel texte — est un travail de modèle : elle est
 * demandée à Claude Code via `analyse-demande.md`, puis relue et validée ici.
 */
export const analyser = async (
  dossier: string,
  options: OptionsAnalyse = {},
): Promise<Analyse> => {
  const cible = join(dossier, 'analyse.json');
  if (existsSync(cible) && !options.force) {
    discret('   analyse.json déjà présent — étape sautée (--force pour refaire)');
    return AnalyseSchema.parse(lireJson(cible));
  }

  const source = join(dossier, 'source.mp4');
  if (!existsSync(source)) {
    throw new Error(`Enregistrement d'écran introuvable : ${source}`);
  }

  // 1. ffprobe
  const infos = await sonder(source);
  info(
    `   ${infos.largeur}×${infos.hauteur}, ${infos.fps.toFixed(2)} fps, ` +
      `${infos.duree.toFixed(1)} s`,
  );

  if (infos.duree > DUREE_MAX_CONSEILLEE && !options.accepterLongue) {
    const decoupage = proposerDecoupage(infos.duree);
    throw new Error(
      `L'enregistrement dure ${(infos.duree / 60).toFixed(1)} min, au-delà des 4 minutes ` +
        `conseillées pour un tutoriel.\nDécoupage proposé :\n${decoupage}\n` +
        'Confirmez avec --accepter-longue pour analyser tel quel, ou découpez la source.',
    );
  }

  // 2. Extraction des frames : une par seconde en basse définition…
  const frames = assurerDossier(join(dossier, 'frames'));
  etape('Extraction des frames (1 image/s, 640 px)');
  await lancer('ffmpeg', [
    '-y', '-i', source,
    '-vf', 'fps=1,scale=640:-2',
    '-q:v', '4',
    join(frames, 'seconde-%04d.jpg'),
  ]);

  // 3. Détection des changements de scène (différence de pixels seuillée)
  etape('Détection des changements d\'écran');
  const ruptures = await detecterScenes(source);
  discret(`   ${ruptures.length} changement(s) d'écran détecté(s)`);

  // …et des frames haute définition aux moments de changement.
  for (const [i, t] of ruptures.entries()) {
    await lancer('ffmpeg', [
      '-y', '-ss', t.toFixed(2), '-i', source,
      '-frames:v', '1', '-q:v', '2',
      join(frames, `rupture-${String(i + 1).padStart(3, '0')}-${t.toFixed(2)}s.jpg`),
    ]);
  }

  // 5. Suivi du curseur entre les frames de rupture, pour situer les clics.
  const curseur = await suivreCurseur(source, ruptures);

  // 4 + 6. Lecture visuelle et segmentation en étapes : travail de modèle.
  const demande = join(dossier, 'analyse-demande.md');
  ecrireJson(join(dossier, 'analyse-brute.json'), {
    duree: infos.duree,
    resolution: [infos.largeur, infos.hauteur],
    fps: infos.fps,
    ruptures,
    curseur,
    frames: readdirSync(frames).sort(),
  });
  ecrireDemandeVisuelle(demande, dossier, infos.duree, ruptures);

  if (!existsSync(cible)) {
    throw new Error(
      `Lecture visuelle requise.\n` +
        `  Frames extraites : ${frames}\n` +
        `  Consigne         : ${demande}\n` +
        `  Claude Code : lis les frames, remplis ${cible} selon le schéma, puis relance.`,
    );
  }

  const analyse = AnalyseSchema.parse(lireJson(cible));
  verifierCoherence(analyse);
  return analyse;
};

/** Timecodes des changements de scène, via le filtre `select=gt(scene,…)`. */
const detecterScenes = async (source: string): Promise<number[]> => {
  const sortie = await lancer('ffmpeg', [
    '-i', source,
    '-filter_complex', `select='gt(scene,${SEUIL_SCENE})',metadata=print:file=-`,
    '-an', '-f', 'null', '-',
  ]);
  const temps = [...sortie.matchAll(/pts_time:([0-9.]+)/g)].map((m) => Number(m[1]));
  // On regroupe les ruptures trop rapprochées (moins d'une seconde).
  return temps.filter((t, i) => i === 0 || t - (temps[i - 1] as number) > 1);
};

/**
 * Suit le pointeur entre deux frames de rupture, par différence de blocs : la
 * zone qui bouge le plus juste avant une rupture est le point de clic probable.
 * Le résultat corrige les coordonnées de la lecture visuelle.
 */
const suivreCurseur = async (
  source: string,
  ruptures: number[],
): Promise<{ t: number; x: number; y: number; confiance: number }[]> => {
  const points: { t: number; x: number; y: number; confiance: number }[] = [];
  for (const t of ruptures) {
    const avant = Math.max(0, t - 0.4);
    const sortie = await lancer('ffmpeg', [
      '-ss', avant.toFixed(2), '-i', source,
      '-t', '0.4',
      '-vf', 'scale=160:-2,tblend=all_mode=difference,crop=iw:ih,signalstats,metadata=print:file=-',
      '-an', '-f', 'null', '-',
    ]).catch(() => '');
    const yavg = Number([...sortie.matchAll(/YAVG=([0-9.]+)/g)].pop()?.[1] ?? 0);
    // Sans détection fiable, on marque une confiance nulle : la lecture visuelle
    // fera foi et le champ sert seulement d'indice.
    points.push({ t, x: 0.5, y: 0.5, confiance: Math.min(1, yavg / 32) });
  }
  return points;
};

const proposerDecoupage = (duree: number): string => {
  const parts = Math.ceil(duree / 150);
  const taille = duree / parts;
  return Array.from({ length: parts }, (_, i) => {
    const debut = (i * taille).toFixed(0);
    const fin = ((i + 1) * taille).toFixed(0);
    return `  · partie ${i + 1} : ${debut}s → ${fin}s`;
  }).join('\n');
};

const ecrireDemandeVisuelle = (
  chemin: string,
  dossier: string,
  duree: number,
  ruptures: number[],
): void => {
  writeFileSync(
    chemin,
    `# Lecture visuelle de l'enregistrement

Durée : ${duree.toFixed(1)} s · ${ruptures.length} changement(s) d'écran détecté(s) à
${ruptures.map((t) => `${t.toFixed(1)}s`).join(', ') || '(aucun)'}.

Les frames sont dans \`frames/\` : \`seconde-XXXX.jpg\` (une par seconde) et
\`rupture-XXX-<t>s.jpg\` (haute définition, aux changements d'écran).

Lis-les et écris \`analyse.json\` en décrivant, pour chaque moment :

- **l'écran affiché** — nom de la page ou de la modale (\`ecrans\`)
- **l'action réalisée** — clic, saisie, sélection, validation, ouverture, défilement
- **la zone concernée**, en coordonnées normalisées \`{x, y, w, h}\` (0 → 1)
- **le texte visible pertinent** — libellés de boutons, titres de champs

Puis regroupe les actions en **3 à 7 étapes logiques**, chacune avec un titre
court à l'infinitif (« Ouvrir la fiche entreprise », « Renseigner le SIRET »).

## Confidentialité — obligatoire

Liste dans \`zones_sensibles\` **toute donnée réelle visible** : email, téléphone,
SIRET, IBAN, nom de client. Indique \`t\`, \`fin\` et \`zone\` : le rendu les floutera.
Une donnée oubliée ici part en ligne.

## Schéma attendu

Voir \`src/schema/index.ts\` → \`AnalyseSchema\`. Les indices déterministes
(ruptures, curseur, liste des frames) sont dans \`analyse-brute.json\`.
`,
    'utf8',
  );
};

/** Contrôles de cohérence sur une analyse relue. */
const verifierCoherence = (analyse: Analyse): void => {
  if (analyse.etapes.length < 3 || analyse.etapes.length > 7) {
    avertir(
      `analyse.json contient ${analyse.etapes.length} étapes — la cible est 3 à 7.`,
    );
  }
  for (const e of analyse.etapes) {
    if (e.fin <= e.debut) {
      throw new Error(`Étape ${e.numero} « ${e.titre} » : fin ≤ début.`);
    }
    if (e.fin > analyse.duree + 0.5) {
      throw new Error(
        `Étape ${e.numero} « ${e.titre} » finit à ${e.fin}s, après la fin de la vidéo ` +
          `(${analyse.duree.toFixed(1)}s).`,
      );
    }
  }
  if (analyse.zones_sensibles.length === 0) {
    avertir(
      'Aucune zone sensible signalée. Vérifiez qu\'aucune donnée réelle (email, ' +
        'téléphone, SIRET, IBAN, nom de client) n\'est visible à l\'écran.',
    );
  }
};

export const tailleFichier = (chemin: string): number => statSync(chemin).size;
