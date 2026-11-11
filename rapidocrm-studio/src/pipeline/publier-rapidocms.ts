import { createHash } from 'node:crypto';
import { existsSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import { z } from 'zod';
import { PublicationSchema, ScriptSchema, type Publication } from '../schema/index.ts';
import { appelMcp } from '../mcp/pont.ts';
import { ecrireJson, lireJson } from '../util/chemins.ts';
import { discret, etape, info } from '../util/journal.ts';

const ReponseUploadSchema = z.object({
  url: z.string().url(),
  nom: z.string().optional(),
});

const empreinte = (chemin: string): string =>
  createHash('sha256').update(readFileSync(chemin)).digest('hex').slice(0, 16);

interface Media {
  cle: 'video_url' | 'video_vertical_url' | 'thumbnail_url' | 'thumbnail_vertical_url';
  fichier: string;
  suffixe: string;
  obligatoire: boolean;
}

/** Étape 7 — dépôt des médias dans la bibliothèque RapidoCMS, liens AWS S3 en retour. */
export const publierRapidoCms = async (dossier: string): Promise<Publication> => {
  const script = ScriptSchema.parse(lireJson(join(dossier, 'script.json')));
  const cheminPublication = join(dossier, 'publication.json');
  const publication: Publication = existsSync(cheminPublication)
    ? PublicationSchema.parse(lireJson(cheminPublication))
    : {};

  const sortie = join(dossier, 'out');
  const base = `rapidocrm-tuto-${script.meta.module.toLowerCase()}-V${String(script.meta.numero).padStart(2, '0')}-${script.meta.slug}`;

  const medias: Media[] = [
    { cle: 'video_url', fichier: join(sortie, 'master-16x9.mp4'), suffixe: '', obligatoire: true },
    { cle: 'video_vertical_url', fichier: join(sortie, 'master-9x16.mp4'), suffixe: '-vertical', obligatoire: false },
    { cle: 'thumbnail_url', fichier: join(sortie, 'thumb-16x9.jpg'), suffixe: '-thumb', obligatoire: true },
    { cle: 'thumbnail_vertical_url', fichier: join(sortie, 'thumb-9x16.jpg'), suffixe: '-thumb-vertical', obligatoire: false },
  ];

  for (const media of medias) {
    if (!existsSync(media.fichier)) {
      if (media.obligatoire) {
        throw new Error(`Fichier manquant, publication impossible : ${media.fichier}`);
      }
      continue;
    }
  }

  const empreintes: Record<string, string> = { ...(publication.rapidocms?.empreintes ?? {}) };
  const liens: Record<string, string> = {};

  for (const media of medias) {
    if (!existsSync(media.fichier)) continue;
    const marque = empreinte(media.fichier);
    const dejaEnLigne = publication.rapidocms?.[media.cle];

    // Idempotence : même fichier + lien déjà valide = pas de réupload.
    if (dejaEnLigne && empreintes[media.cle] === marque && (await repond(dejaEnLigne))) {
      discret(`   ${media.cle} — inchangé, réupload évité`);
      liens[media.cle] = dejaEnLigne;
      continue;
    }

    const extension = media.fichier.endsWith('.mp4') ? '.mp4' : '.jpg';
    const nom = `${base}${media.suffixe}${extension}`;
    etape(`Dépôt de ${nom}`);

    const reponse = await avecReessais(() =>
      Promise.resolve(
        appelMcp(
          dossier,
          'RapidoCMS',
          'upload_file_tool',
          {
            chemin_local: media.fichier,
            nom_fichier: nom,
            consigne:
              "Dépose ce fichier dans la bibliothèque RapidoCMS et retourne " +
              '{"url": "<lien AWS public>"}. Si l\'outil d\'upload porte un autre nom, ' +
              'inspecte les outils réellement disponibles et adapte-toi.',
          },
          ReponseUploadSchema,
          media.cle,
        ),
      ),
    );

    if (!(await repond(reponse.url))) {
      throw new Error(
        `Le lien retourné pour ${nom} ne répond pas correctement : ${reponse.url}`,
      );
    }
    liens[media.cle] = reponse.url;
    empreintes[media.cle] = marque;
    info(`   ${media.cle} → ${reponse.url}`);
  }

  const resultat: Publication = PublicationSchema.parse({
    ...publication,
    rapidocms: {
      video_url: liens.video_url ?? publication.rapidocms?.video_url,
      video_vertical_url: liens.video_vertical_url ?? publication.rapidocms?.video_vertical_url,
      thumbnail_url: liens.thumbnail_url ?? publication.rapidocms?.thumbnail_url,
      thumbnail_vertical_url:
        liens.thumbnail_vertical_url ?? publication.rapidocms?.thumbnail_vertical_url,
      empreintes,
      publie_le: new Date().toISOString(),
    },
  });
  ecrireJson(cheminPublication, resultat);
  return resultat;
};

/** Vérifie qu'une URL répond en 200 avec un content-type cohérent. */
export const repond = async (url: string): Promise<boolean> => {
  try {
    const reponse = await fetch(url, { method: 'HEAD' });
    if (!reponse.ok) return false;
    const type = reponse.headers.get('content-type') ?? '';
    if (url.endsWith('.mp4')) return type.includes('video');
    if (url.endsWith('.jpg') || url.endsWith('.jpeg')) return type.includes('image');
    return true;
  } catch {
    return false;
  }
};

/** 3 tentatives, délai croissant, puis on s'arrête en nommant le fichier fautif. */
const avecReessais = async <T>(action: () => Promise<T>): Promise<T> => {
  let derniere: unknown;
  for (const attente of [0, 2000, 5000]) {
    if (attente) await new Promise((r) => setTimeout(r, attente));
    try {
      return await action();
    } catch (e) {
      if ((e as Error).name === 'DemandeEnAttente') throw e; // le pont, pas une panne
      derniere = e;
    }
  }
  throw derniere;
};
