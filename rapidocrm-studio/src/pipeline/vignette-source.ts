import { copyFileSync, createWriteStream, existsSync } from 'node:fs';
import { join } from 'node:path';
import { Readable } from 'node:stream';
import { pipeline as flux } from 'node:stream/promises';
import { z } from 'zod';
import { PublicationSchema, type Script } from '../schema/index.ts';
import { appelMcp } from '../mcp/pont.ts';
import { assurerDossier, lireJson } from '../util/chemins.ts';
import { avertir, discret } from '../util/journal.ts';

const FicheTutorielSchema = z
  .object({
    vignette_url: z.string().url().optional(),
    thumbnail_url: z.string().url().optional(),
    seo_og_image: z.string().url().optional(),
  })
  .passthrough();

/**
 * Récupère la vignette à afficher en ouverture de vidéo, dans cet ordre :
 *
 * 1. le lien déjà connu dans `publication.json` (bibliothèque RapidoCMS) ;
 * 2. la fiche du tutoriel sur le site, via le MCP « RapidoCRM tuto »
 *    (`obtenir_tutoriel`) — c'est la vignette réellement en ligne ;
 * 3. la vignette produite localement (`out/thumb-16x9.jpg`).
 *
 * Retourne un chemin relatif à `public/`, ou `null` si aucune vignette n'existe
 * encore : l'ouverture se réduit alors à un fond de charte.
 */
export const recupererVignette = async (
  dossier: string,
  script: Script,
  racinePublic: string,
): Promise<string | null> => {
  const destinationDossier = assurerDossier(join(racinePublic, script.meta.slug));
  const relatif = join(script.meta.slug, 'vignette-ouverture.jpg');
  const destination = join(destinationDossier, 'vignette-ouverture.jpg');

  // 1. Lien déjà obtenu à la publication RapidoCMS.
  const cheminPublication = join(dossier, 'publication.json');
  if (existsSync(cheminPublication)) {
    const publication = PublicationSchema.parse(lireJson(cheminPublication));
    const url = publication.rapidocms?.thumbnail_url;
    if (url && (await telecharger(url, destination))) {
      discret('   vignette d\'ouverture : lien AWS de publication.json');
      return relatif;
    }
  }

  // 2. La fiche en ligne, via le MCP du site.
  const cleApi = process.env.RAPIDO_ACADEMIE_API_KEY;
  if (cleApi) {
    try {
      const fiche = appelMcp(
        dossier,
        'RapidoCMS tutoriels',
        'obtenir_tutoriel',
        {
          cle_api: cleApi,
          slug: script.meta.slug,
          module: script.meta.module,
          numero: script.meta.numero,
          consigne:
            'Retourne la fiche du tutoriel ; on cherche l\'URL de sa vignette ' +
            '(vignette_url, thumbnail_url ou seo_og_image).',
        },
        FicheTutorielSchema,
        'vignette-ouverture',
      );
      const url = fiche.vignette_url ?? fiche.thumbnail_url ?? fiche.seo_og_image;
      if (url && (await telecharger(url, destination))) {
        discret('   vignette d\'ouverture : fiche du site (MCP RapidoCRM tuto)');
        return relatif;
      }
    } catch (e) {
      if ((e as Error).name === 'DemandeEnAttente') throw e;
      avertir(`Vignette du site indisponible : ${(e as Error).message}`);
    }
  } else {
    discret(
      '   RAPIDO_ACADEMIE_API_KEY absente — la vignette du site n\'est pas interrogée',
    );
  }

  // 3. Repli local.
  const locale = join(dossier, 'out', 'thumb-16x9.jpg');
  if (existsSync(locale)) {
    copyFileSync(locale, destination);
    discret('   vignette d\'ouverture : out/thumb-16x9.jpg');
    return relatif;
  }

  avertir(
    'Aucune vignette disponible : l\'ouverture affichera un fond de charte. ' +
      'Lancez `npm run vignette` avant le rendu.',
  );
  return null;
};

const telecharger = async (url: string, destination: string): Promise<boolean> => {
  try {
    const reponse = await fetch(url);
    if (!reponse.ok || !reponse.body) return false;
    await flux(Readable.fromWeb(reponse.body as never), createWriteStream(destination));
    return true;
  } catch {
    return false;
  }
};
