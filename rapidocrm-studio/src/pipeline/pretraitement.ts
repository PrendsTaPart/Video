import { join } from 'node:path';
import type { Alignement, Analyse, EtapeScript, Script, Zone } from '../schema/index.ts';
import { copyFileSync } from 'node:fs';
import { assurerDossier } from '../util/chemins.ts';
import { lancer } from '../util/ffmpeg.ts';
import { avertir, discret } from '../util/journal.ts';
import { dureeParole } from './script.ts';

export const RALENTI_MIN = 0.7;
export const ACCELERATION_MAX = 2.2;

const L16 = 1920;
const H16 = 1080;
const L9 = 1080;
const H9 = 1920;

/**
 * Facteur de vitesse pour caler la vidéo sur la voix, borné par la charte.
 *
 * Le plafond est passé de 1,6× à 2,2× : les scripts du module Comptabilité sont
 * volontairement courts, et à 1,6× la démonstration traînait derrière une voix
 * déjà finie. 2,2× reste lisible parce que la zone active est désignée par le
 * cercle vert et que le libellé d'étape tient sous la vidéo.
 *
 * On prend la durée RÉELLE de la piste quand elle existe : l'estimation à
 * 150 mots/minute sert à écrire le script, pas à monter. Utiliser l'estimation
 * ici décalerait la vidéo de sa propre voix.
 */
export const facteurVitesse = (etape: EtapeScript, dureeVoix?: number): number => {
  const fenetre = Math.max(0.1, etape.fin_source - etape.debut_source);
  const parole = dureeVoix ?? dureeParole(etape.voix);
  if (parole <= 0) return 1;
  const brut = fenetre / parole; // < 1 = ralenti
  const borne = Math.min(ACCELERATION_MAX, Math.max(RALENTI_MIN, brut));
  if (borne !== brut) {
    avertir(
      `Étape ${etape.numero} : facteur ${brut.toFixed(2)}× ramené à ${borne.toFixed(2)}× ` +
        '— au-delà, le mouvement devient illisible.',
    );
  }
  return borne;
};

/**
 * Chaîne de floutage des zones sensibles couvrant un segment de temps.
 *
 * `boxblur` ne sait pas flouter une région : il faut découper la zone, la
 * flouter, puis la ré-incruster à sa place. On construit donc un filter_complex
 * — un overlay par zone — plutôt qu'un simple `-vf`.
 *
 * @returns les maillons du graphe et le label de sortie à enchaîner.
 */
export const grapheFloutage = (
  analyse: Analyse,
  debut: number,
  fin: number,
  entree = '0:v',
): { maillons: string[]; sortie: string } => {
  const zones = analyse.zones_sensibles.filter((zone) => {
    const zFin = zone.fin ?? analyse.duree;
    return zFin >= debut && zone.t <= fin;
  });
  if (zones.length === 0) return { maillons: [], sortie: entree };

  const maillons: string[] = [];
  const sorties = zones.map((_, i) => `bl${i}`);
  maillons.push(
    `[${entree}]split=${zones.length + 1}[base0]${sorties.map((s) => `[${s}]`).join('')}`,
  );

  let courant = 'base0';
  zones.forEach((zone, i) => {
    const z: Zone = zone.zone ?? { x: 0, y: 0, w: 1, h: 1 };
    // Dimensions paires : x264 refuse les tailles impaires.
    const dim = (fraction: number, ref: string) => `trunc(${ref}*${fraction.toFixed(4)}/2)*2`;
    const relDebut = Math.max(0, zone.t - debut);
    const relFin = Math.max(relDebut, Math.min(fin, zone.fin ?? analyse.duree) - debut);

    maillons.push(
      `[${sorties[i]}]crop=w=${dim(z.w, 'iw')}:h=${dim(z.h, 'ih')}:` +
        `x=${dim(z.x, 'iw')}:y=${dim(z.y, 'ih')},` +
        // Les rayons restent modestes : le plan chroma est deux fois plus petit
        // et ffmpeg refuse un rayon supérieur à sa demi-hauteur.
        `boxblur=luma_radius=12:luma_power=3:chroma_radius=6:chroma_power=2[flou${i}]`,
    );
    const suivant = i === zones.length - 1 ? 'floute' : `base${i + 1}`;
    maillons.push(
      `[${courant}][flou${i}]overlay=x=${dim(z.x, 'main_w')}:y=${dim(z.y, 'main_h')}:` +
        `enable='between(t,${relDebut.toFixed(2)},${relFin.toFixed(2)})'[${suivant}]`,
    );
    courant = suivant;
  });

  return { maillons, sortie: courant };
};

/**
 * Découpe l'enregistrement en segments d'étape, cale chacun sur la voix, floute
 * les zones sensibles et normalise le format. Retourne un chemin par étape,
 * relatif à `public/`.
 */
export const preparerScreencast = async (
  dossier: string,
  script: Script,
  analyse: Analyse,
  racinePublic: string,
  format: '16x9' | '9x16',
  alignement?: Alignement | null,
): Promise<string[]> => {
  const source = join(dossier, 'source.mp4');
  const travail = assurerDossier(join(dossier, 'tmp'));
  const dossierPublic = assurerDossier(join(racinePublic, script.meta.slug));
  const relatifs: string[] = [];
  const segments: string[] = [];
  for (const etape of script.demo.etapes) {
    const bloc = alignement?.blocs.find(
      (b) => b.id === `etape-${String(etape.numero).padStart(2, '0')}`,
    );
    const vitesse = facteurVitesse(etape, bloc?.duree);
    const duree = etape.fin_source - etape.debut_source;
    const segment = join(travail, `etape-${String(etape.numero).padStart(2, '0')}-${format}.mp4`);

    const flou = grapheFloutage(analyse, etape.debut_source, etape.fin_source);
    const mise = [
      `setpts=${(1 / vitesse).toFixed(4)}*PTS`,
      ...(format === '16x9'
        ? [
            `scale=${L16}:${H16}:force_original_aspect_ratio=decrease`,
            `pad=${L16}:${H16}:(ow-iw)/2:(oh-ih)/2:color=0xF2F4F7`,
          ]
        : pleineLargeur(analyse.resolution)),
      'fps=30',
    ].join(',');

    const graphe = [...flou.maillons, `[${flou.sortie}]${mise}[v]`].join(';');

    await lancer('ffmpeg', [
      '-y',
      '-ss', etape.debut_source.toFixed(3),
      '-t', duree.toFixed(3),
      '-i', source,
      '-filter_complex', graphe,
      '-map', '[v]',
      '-an',
      '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p',
      segment,
    ]);
    segments.push(segment);

    // Un fichier par étape : chaque <Sequence> lit le sien depuis son début.
    // Un fichier concaténé unique rejouerait le début de l'enregistrement à
    // chaque étape, puisqu'une Sequence démarre sa vidéo à zéro.
    const nom = `demo-${format}-etape-${String(etape.numero).padStart(2, '0')}.mp4`;
    copyFileSync(segment, join(dossierPublic, nom));
    relatifs.push(join(script.meta.slug, nom));

    discret(`   étape ${etape.numero} — ${duree.toFixed(1)}s à ${vitesse.toFixed(2)}×`);
  }

  return relatifs;
};

/**
 * En 9:16, l'écran du logiciel est montré **en entier**, sur toute sa largeur.
 *
 * On a d'abord essayé de recadrer — une bande horizontale, puis la colonne utile
 * — et les deux coupaient l'interface. Un tutoriel montre un logiciel : le couper
 * fait perdre le contexte. On garde donc l'image complète, mise à la largeur du
 * cadre vertical, et c'est le mockup qui lui donne sa hauteur.
 */
const pleineLargeur = (resolution: [number, number]): string[] => {
  const [largeur, hauteur] = resolution;
  const hauteurCible = Math.round((L9 * hauteur) / largeur / 2) * 2;
  return [`scale=${L9}:${hauteurCible}`];
};

/** Rapport largeur/hauteur du plan vertical, à donner au mockup. */
export const ratioSource = (resolution: [number, number]): number =>
  resolution[0] / resolution[1];
