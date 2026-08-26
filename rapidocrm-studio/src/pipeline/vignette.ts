import { copyFileSync, existsSync, statSync } from 'node:fs';
import { join } from 'node:path';
import { bundle } from '@remotion/bundler';
import { renderStill, selectComposition } from '@remotion/renderer';
import sharp from 'sharp';
import { AnalyseSchema, ScriptSchema, type Analyse, type Script } from '../schema/index.ts';
import { assurerLogos, cheminLogo, LOGOS, type NomLogo } from '../brand/logos.ts';
import { assurerDossier, lireJson, racineProjet } from '../util/chemins.ts';
import { lancer } from '../util/ffmpeg.ts';
import { etape, info } from '../util/journal.ts';
import { copierPresentateur } from './rendu.ts';

const QUALITE = 90;
const POIDS_MAX = 2 * 1024 * 1024; // limite YouTube
const MAX_TITRE_COURT = 28;

/** Étape 6 — vignettes 16:9 et 9:16, rendues avec Remotion pour rester à la charte. */
export const genererVignettes = async (dossier: string): Promise<string[]> => {
  const script = ScriptSchema.parse(lireJson(join(dossier, 'script.json')));
  const analyse = AnalyseSchema.parse(lireJson(join(dossier, 'analyse.json')));

  if (script.meta.titre_court.length > MAX_TITRE_COURT) {
    throw new Error(
      `titre_court « ${script.meta.titre_court} » fait ${script.meta.titre_court.length} ` +
        `caractères. Au-delà de ${MAX_TITRE_COURT}, il n'est plus lisible à 320 px de large. ` +
        'Fournissez une version plus courte.',
    );
  }

  const racinePublic = assurerDossier(join(racineProjet(), 'public'));
  await assurerLogos();
  for (const nom of Object.keys(LOGOS) as NomLogo[]) {
    const destination = join(assurerDossier(join(racinePublic, 'logos')), `${nom}.png`);
    if (!existsSync(destination)) copyFileSync(cheminLogo(nom), destination);
  }

  copierPresentateur(racinePublic);
  const capture = await extraireCaptureCle(dossier, script, analyse, racinePublic);
  const serveUrl = await bundle({
    entryPoint: join(racineProjet(), 'src', 'template', 'index.ts'),
    publicDir: racinePublic,
  });

  const sortie = assurerDossier(join(dossier, 'out'));
  const produits: string[] = [];

  for (const [id, nom, vertical] of [
    ['Vignette16x9', 'thumb-16x9.jpg', false],
    ['Vignette9x16', 'thumb-9x16.jpg', true],
  ] as const) {
    etape(`Vignette ${nom}`);
    const props = { script, captureSrc: capture, vertical };
    const composition = await selectComposition({ serveUrl, id, inputProps: props });
    const png = join(dossier, 'tmp', nom.replace('.jpg', '.png'));
    assurerDossier(join(dossier, 'tmp'));
    await renderStill({
      composition,
      serveUrl,
      output: png,
      inputProps: props,
      imageFormat: 'png',
    });

    const jpeg = join(sortie, nom);
    await sharp(png).jpeg({ quality: QUALITE, mozjpeg: true }).toFile(jpeg);
    const poids = statSync(jpeg).size;
    if (poids > POIDS_MAX) {
      await sharp(png).jpeg({ quality: 78, mozjpeg: true }).toFile(jpeg);
    }
    info(`   ${nom} — ${(statSync(jpeg).size / 1024).toFixed(0)} Ko`);
    produits.push(jpeg);
  }
  return produits;
};

/**
 * La frame la plus représentative : le milieu de l'étape la plus longue, qui est
 * en général celle où l'écran clé du tutoriel est complet.
 */
const extraireCaptureCle = async (
  dossier: string,
  script: Script,
  analyse: Analyse,
  racinePublic: string,
): Promise<string> => {
  const plusLongue = [...script.demo.etapes].sort(
    (a, b) => b.fin_source - b.debut_source - (a.fin_source - a.debut_source),
  )[0];
  const t = plusLongue
    ? (plusLongue.debut_source + plusLongue.fin_source) / 2
    : analyse.duree / 2;

  const relatif = join(script.meta.slug, 'capture-cle.jpg');
  const cible = join(assurerDossier(join(racinePublic, script.meta.slug)), 'capture-cle.jpg');
  await lancer('ffmpeg', [
    '-y', '-ss', t.toFixed(2), '-i', join(dossier, 'source.mp4'),
    '-frames:v', '1', '-q:v', '2', cible,
  ]);
  return relatif;
};

/** Régénère les vignettes de tout un module — utile après un ajustement du template. */
export const vignettesEnLot = async (dossiers: string[]): Promise<void> => {
  for (const dossier of dossiers) {
    info(`▸ ${dossier}`);
    await genererVignettes(dossier);
  }
};
