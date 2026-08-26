import { join } from 'node:path';
import type { Analyse, EtapeScript, Script, Zone } from '../schema/index.ts';
import { assurerDossier } from '../util/chemins.ts';
import { lancer } from '../util/ffmpeg.ts';
import { avertir, discret } from '../util/journal.ts';
import { dureeParole } from './script.ts';

export const RALENTI_MIN = 0.7;
export const ACCELERATION_MAX = 1.6;

const L16 = 1920;
const H16 = 1080;
const L9 = 1080;
const H9 = 1920;

/** Facteur de vitesse pour caler la vidéo sur la voix, borné par la charte. */
export const facteurVitesse = (etape: EtapeScript): number => {
  const fenetre = Math.max(0.1, etape.fin_source - etape.debut_source);
  const parole = dureeParole(etape.voix);
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

/** Filtre de floutage des zones sensibles couvrant un segment de temps. */
export const filtreFloutage = (
  analyse: Analyse,
  debut: number,
  fin: number,
): string[] => {
  const filtres: string[] = [];
  for (const zone of analyse.zones_sensibles) {
    const zDebut = zone.t;
    const zFin = zone.fin ?? analyse.duree;
    if (zFin < debut || zDebut > fin) continue;
    const z: Zone = zone.zone ?? { x: 0, y: 0, w: 1, h: 1 };
    const relDebut = Math.max(0, zDebut - debut);
    const relFin = Math.max(relDebut, Math.min(fin, zFin) - debut);
    filtres.push(
      `boxblur=luma_radius=24:luma_power=2:enable='between(t,${relDebut.toFixed(2)},${relFin.toFixed(2)})':` +
        `x=iw*${z.x.toFixed(4)}:y=ih*${z.y.toFixed(4)}:w=iw*${z.w.toFixed(4)}:h=ih*${z.h.toFixed(4)}`,
    );
  }
  return filtres;
};

/**
 * Découpe l'enregistrement en segments d'étape, cale chacun sur la voix, floute
 * les zones sensibles et normalise le format. Retourne le chemin du screencast
 * prêt pour Remotion, relatif à `public/`.
 */
export const preparerScreencast = async (
  dossier: string,
  script: Script,
  analyse: Analyse,
  racinePublic: string,
  format: '16x9' | '9x16',
): Promise<string> => {
  const source = join(dossier, 'source.mp4');
  const travail = assurerDossier(join(dossier, 'tmp'));
  const cibleRelative = join(script.meta.slug, `demo-${format}.mp4`);
  const cible = join(assurerDossier(join(racinePublic, script.meta.slug)), `demo-${format}.mp4`);

  const segments: string[] = [];
  for (const etape of script.demo.etapes) {
    const vitesse = facteurVitesse(etape);
    const duree = etape.fin_source - etape.debut_source;
    const segment = join(travail, `etape-${String(etape.numero).padStart(2, '0')}-${format}.mp4`);

    const filtres = [
      ...filtreFloutage(analyse, etape.debut_source, etape.fin_source),
      `setpts=${(1 / vitesse).toFixed(4)}*PTS`,
      ...(format === '16x9'
        ? [`scale=${L16}:${H16}:force_original_aspect_ratio=decrease`, `pad=${L16}:${H16}:(ow-iw)/2:(oh-ih)/2:color=0xF2F4F7`]
        : [
            cropVertical(etape.zone_focus, analyse.resolution),
            `scale=${L9}:${H9}:force_original_aspect_ratio=increase`,
            `crop=${L9}:${H9}`,
          ]),
      'fps=30',
    ];

    await lancer('ffmpeg', [
      '-y',
      '-ss', etape.debut_source.toFixed(3),
      '-t', duree.toFixed(3),
      '-i', source,
      '-vf', filtres.join(','),
      '-an',
      '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p',
      segment,
    ]);
    segments.push(segment);
    discret(`   étape ${etape.numero} — ${duree.toFixed(1)}s à ${vitesse.toFixed(2)}×`);
  }

  const liste = join(travail, `segments-${format}.txt`);
  const { writeFileSync } = await import('node:fs');
  writeFileSync(liste, segments.map((s) => `file '${s}'`).join('\n'), 'utf8');
  await lancer('ffmpeg', [
    '-y', '-f', 'concat', '-safe', '0', '-i', liste,
    '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p',
    cible,
  ]);
  return cibleRelative;
};

/**
 * En 9:16 on recadre sur la zone active de l'étape — jamais une simple
 * réduction centrée. La zone est élargie pour respecter le ratio 9:16.
 */
const cropVertical = (zone: Zone, resolution: [number, number]): string => {
  const [largeurSource, hauteurSource] = resolution;
  const centreX = zone.x + zone.w / 2;
  const centreY = zone.y + zone.h / 2;
  // Hauteur de découpe : la zone, avec 25 % de marge, plafonnée à l'image.
  const h = Math.min(1, Math.max(zone.h * 1.25, 0.4));
  // Largeur telle que la découpe fasse exactement 9:16 en pixels.
  const w = Math.min(1, (h * hauteurSource * (L9 / H9)) / largeurSource);
  const x = Math.min(Math.max(centreX - w / 2, 0), 1 - w);
  const y = Math.min(Math.max(centreY - h / 2, 0), 1 - h);
  return `crop=iw*${w.toFixed(4)}:ih*${h.toFixed(4)}:iw*${x.toFixed(4)}:ih*${y.toFixed(4)}`;
};
