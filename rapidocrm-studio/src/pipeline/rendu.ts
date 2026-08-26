import { copyFileSync, existsSync, statSync } from 'node:fs';
import { join } from 'node:path';
import { bundle } from '@remotion/bundler';
import { renderMedia, selectComposition } from '@remotion/renderer';
import {
  AlignementSchema,
  AnalyseSchema,
  RenduSchema,
  ScriptSchema,
  type Alignement,
  type Rendu,
  type Script,
} from '../schema/index.ts';
import { assurerLogos, cheminLogo, LOGOS, type NomLogo } from '../brand/logos.ts';
import { calculerMinutage, FPS } from '../template/minutage.ts';
import { assurerDossier, ecrireJson, lireJson, racineProjet } from '../util/chemins.ts';
import { lancer } from '../util/ffmpeg.ts';
import { avertir, discret, etape, info } from '../util/journal.ts';
import { preparerScreencast } from './pretraitement.ts';

export type Format = '16x9' | '9x16' | 'tous';

export interface OptionsRendu {
  format?: Format;
  preview?: boolean;
  force?: boolean;
}

const DUREE_MIN = 80;
const DUREE_MAX = 170;

/** Étape 5 — rendu vidéo. */
export const rendre = async (dossier: string, options: OptionsRendu = {}): Promise<Rendu> => {
  const script = ScriptSchema.parse(lireJson(join(dossier, 'script.json')));
  const analyse = AnalyseSchema.parse(lireJson(join(dossier, 'analyse.json')));
  const alignement: Alignement | null = existsSync(join(dossier, 'voix', 'alignement.json'))
    ? AlignementSchema.parse(lireJson(join(dossier, 'voix', 'alignement.json')))
    : null;

  if (!alignement) {
    avertir('Aucun alignement de voix : le minutage retombe sur les durées du script.');
  }

  const racinePublic = assurerDossier(join(racineProjet(), 'public'));
  await assurerLogos();
  for (const nom of Object.keys(LOGOS) as NomLogo[]) {
    const destination = join(assurerDossier(join(racinePublic, 'logos')), `${nom}.png`);
    if (!existsSync(destination)) copyFileSync(cheminLogo(nom), destination);
  }

  const sortie = assurerDossier(join(dossier, 'out'));
  const formats: ('16x9' | '9x16')[] =
    options.format === 'tous' || !options.format ? ['16x9', '9x16'] : [options.format];

  // 2. Pré-traitement ffmpeg de l'enregistrement source.
  const screencasts: Record<string, string> = {};
  for (const format of formats) {
    etape(`Pré-traitement de l'enregistrement (${format})`);
    screencasts[format] = await preparerScreencast(
      dossier,
      script,
      analyse,
      racinePublic,
      format,
    );
  }

  // Piste voix rendue accessible à Remotion.
  let audioSrc: string | null = null;
  const complete = join(dossier, 'voix', 'complete.mp3');
  if (existsSync(complete)) {
    audioSrc = join(script.meta.slug, 'voix.mp3');
    copyFileSync(complete, join(racinePublic, audioSrc));
  }

  // 3. Rendu Remotion.
  etape('Bundle Remotion');
  const serveUrl = await bundle({
    entryPoint: join(racineProjet(), 'src', 'template', 'index.ts'),
    publicDir: racinePublic,
  });

  const minutage = calculerMinutage(script, alignement);
  const fichiers: { chemin: string; octets: number }[] = [];

  for (const format of formats) {
    const id = format === '16x9' ? 'Tutoriel16x9' : 'Tutoriel9x16';
    const props = {
      script,
      alignement,
      demoSrc: screencasts[format] ?? null,
      audioSrc,
      vertical: format === '9x16',
    };
    const composition = await selectComposition({ serveUrl, id, inputProps: props });
    const brut = join(dossier, 'tmp', `remotion-${format}.mp4`);
    assurerDossier(join(dossier, 'tmp'));

    etape(`Rendu ${id}${options.preview ? ' (prévisualisation 720p)' : ''}`);
    await renderMedia({
      composition: {
        ...composition,
        durationInFrames: minutage.total,
        ...(options.preview ? { width: 1280, height: 720 } : {}),
      },
      serveUrl,
      codec: 'h264',
      crf: options.preview ? 30 : 18,
      x264Preset: options.preview ? 'veryfast' : 'slow',
      outputLocation: brut,
      inputProps: props,
      onProgress: ({ progress }) =>
        process.stdout.write(`\r   ${(progress * 100).toFixed(0)} %   `),
    });
    process.stdout.write('\n');

    // 4. Mixage audio : voix au premier plan, musique duckée sous la voix.
    const nom = options.preview ? `preview-${format}.mp4` : `master-${format}.mp4`;
    const final = join(sortie, nom);
    await mixer(brut, complete, final, options.preview === true);
    fichiers.push({ chemin: final, octets: statSync(final).size });
    info(`   ${nom} — ${(statSync(final).size / 1024 / 1024).toFixed(1)} Mo`);
  }

  // 6. Rapport.
  const duree = minutage.total / FPS;
  const rapport: Rendu = RenduSchema.parse({
    duree,
    fichiers,
    sequences: [
      { nom: 'hook', debut: minutage.hook.debut / FPS, fin: (minutage.hook.debut + minutage.hook.duree) / FPS },
      { nom: 'titre', debut: minutage.titre.debut / FPS, fin: (minutage.titre.debut + minutage.titre.duree) / FPS },
      { nom: 'demo', debut: minutage.demo.debut / FPS, fin: (minutage.demo.debut + minutage.demo.duree) / FPS },
      { nom: 'claude', debut: minutage.claude.debut / FPS, fin: (minutage.claude.debut + minutage.claude.duree) / FPS },
      { nom: 'punchline', debut: minutage.punchline.debut / FPS, fin: (minutage.punchline.debut + minutage.punchline.duree) / FPS },
    ],
    chapitres_youtube: chapitresYoutube(script, minutage),
    avertissements: controler(duree, script),
  });
  ecrireJson(join(dossier, 'rendu.json'), rapport);
  for (const a of rapport.avertissements) avertir(a);
  return rapport;
};

const timecode = (secondes: number): string => {
  const m = Math.floor(secondes / 60);
  const s = Math.floor(secondes % 60);
  return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
};

const chapitresYoutube = (
  script: Script,
  minutage: ReturnType<typeof calculerMinutage>,
): { timecode: string; titre: string }[] => [
  { timecode: '00:00', titre: script.hook.texte },
  { timecode: timecode(minutage.titre.debut / FPS), titre: script.meta.titre },
  ...minutage.demo.etapes.map((bloc, i) => ({
    timecode: timecode(bloc.debut / FPS),
    titre: script.demo.etapes[i]?.titre ?? `Étape ${i + 1}`,
  })),
  { timecode: timecode(minutage.claude.debut / FPS), titre: 'Faites-le avec Claude' },
  { timecode: timecode(minutage.punchline.debut / FPS), titre: 'À retenir' },
];

/**
 * Voix à -16 LUFS au premier plan, musique de fond à -26 dB abaissée à -34 dB
 * sous la voix (ducking par sidechaincompress), effets aux transitions.
 */
const mixer = async (
  video: string,
  voix: string,
  destination: string,
  preview: boolean,
): Promise<void> => {
  const musique = join(racineProjet(), 'assets', 'musique', 'fond.mp3');
  const aVoix = existsSync(voix);
  const aMusique = existsSync(musique);

  if (!aVoix && !aMusique) {
    copyFileSync(video, destination);
    return;
  }

  const entrees = ['-i', video];
  if (aVoix) entrees.push('-i', voix);
  if (aMusique) entrees.push('-stream_loop', '-1', '-i', musique);

  const indexVoix = 1;
  const indexMusique = aVoix ? 2 : 1;

  let filtre: string;
  if (aVoix && aMusique) {
    filtre =
      `[${indexVoix}:a]loudnorm=I=-16:TP=-1.5:LRA=11,asplit=2[voix][cle];` +
      `[${indexMusique}:a]volume=-26dB[fond];` +
      `[fond][cle]sidechaincompress=threshold=0.05:ratio=8:attack=20:release=400[fondDucke];` +
      `[voix][fondDucke]amix=inputs=2:duration=first:dropout_transition=0[sortie]`;
  } else if (aVoix) {
    filtre = `[${indexVoix}:a]loudnorm=I=-16:TP=-1.5:LRA=11[sortie]`;
  } else {
    filtre = `[${indexMusique}:a]volume=-26dB[sortie]`;
  }

  await lancer('ffmpeg', [
    '-y', ...entrees,
    '-filter_complex', filtre,
    '-map', '0:v', '-map', '[sortie]',
    '-c:v', 'copy',
    '-c:a', 'aac', '-b:a', preview ? '128k' : '192k',
    '-shortest', '-movflags', '+faststart',
    destination,
  ]);
};

/** Contrôles automatiques avant de valider le rendu. */
const controler = (duree: number, script: Script): string[] => {
  const alertes: string[] = [];
  if (duree < DUREE_MIN || duree > DUREE_MAX) {
    alertes.push(
      `Durée finale ${duree.toFixed(0)}s, hors de la fenêtre ${DUREE_MIN}–${DUREE_MAX}s.`,
    );
  }
  if (script.meta.titre_court.length > 28) {
    alertes.push('titre_court dépasse 28 caractères : la vignette sera illisible en petit.');
  }
  discret('   contrôles de charte : voir `npm run qa` pour l\'inspection des frames');
  return alertes;
};
