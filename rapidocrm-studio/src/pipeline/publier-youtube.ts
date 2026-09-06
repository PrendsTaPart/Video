import { existsSync } from 'node:fs';
import { join } from 'node:path';
import { z } from 'zod';
import {
  PublicationSchema,
  RenduSchema,
  ScriptSchema,
  type Publication,
  type Rendu,
  type Script,
} from '../schema/index.ts';
import { appelMcp } from '../mcp/pont.ts';
import { ecrireJson, lireJson } from '../util/chemins.ts';
import { discret, etape, info } from '../util/journal.ts';

const StatutChaineSchema = z.object({
  connectee: z.boolean(),
  chaines: z
    .array(z.object({ id: z.string(), nom: z.string(), active: z.boolean().default(false) }))
    .default([]),
});

const PublicationVideoSchema = z.object({
  video_id: z.string(),
  url: z.string().url().optional(),
  statut: z.string().default('en_cours'),
});

const StatutVideoSchema = z.object({
  statut: z.string(),
  url: z.string().url().optional(),
  erreur: z.string().optional(),
});

// academie.rapidosoftware.com n'a pas d'enregistrement DNS : les liens de
// description pointaient dans le vide. Le domaine servi par l'Académie est
// tutoriel.rapido-crm.com, et une page s'y ouvre sous /tutoriel/<slug>.
const URL_ACADEMIE = 'https://tutoriel.rapido-crm.com';
const URL_ESSAI = 'https://crm.rapidosoftware.com';

/** Étape 8 — publication sur la chaîne YouTube RapidoCRM. */
export const publierYoutube = async (dossier: string): Promise<Publication> => {
  const script = ScriptSchema.parse(lireJson(join(dossier, 'script.json')));
  const rendu = RenduSchema.parse(lireJson(join(dossier, 'rendu.json')));
  const cheminPublication = join(dossier, 'publication.json');
  const publication: Publication = existsSync(cheminPublication)
    ? PublicationSchema.parse(lireJson(cheminPublication))
    : {};

  const lienAws = publication.rapidocms?.video_url;
  if (!lienAws) {
    throw new Error(
      'Aucun lien AWS dans publication.json : lancez `npm run publier:cms` avant YouTube ' +
        '(publish_video attend une URL publique).',
    );
  }

  if (publication.youtube?.url) {
    discret(`   déjà publié : ${publication.youtube.url}`);
    return publication;
  }

  // 1. Chaîne connectée ?
  const statut = appelMcp(
    dossier,
    'YouTube',
    'get_channel_status',
    { consigne: 'Retourne {"connectee": bool, "chaines": [{id, nom, active}]}.' },
    StatutChaineSchema,
    'statut-chaine',
  );
  if (!statut.connectee) {
    throw new Error('Aucune chaîne YouTube connectée au MCP. Connectez la chaîne RapidoCRM.');
  }
  const rapidocrm = statut.chaines.find((c) => /rapidocrm/i.test(c.nom));
  if (rapidocrm && !rapidocrm.active) {
    appelMcp(
      dossier,
      'YouTube',
      'switch_channel',
      { channel_id: rapidocrm.id },
      z.object({}).passthrough(),
      'switch',
    );
  }

  // 2 + 3. Publication avec les métadonnées construites depuis script.json.
  etape('Publication YouTube');
  const publie = appelMcp(
    dossier,
    'YouTube',
    'publish_video',
    {
      video_url: lienAws,
      titre: script.seo.youtube_titre,
      description: descriptionYoutube(script, rendu),
      tags: tags(script),
      thumbnail_url: publication.rapidocms?.thumbnail_url,
      playlist: `RapidoCRM — ${script.meta.module}`,
      creer_playlist_si_absente: true,
      visibilite: 'public',
      categorie: 'Science et technologie',
      langue: 'fr',
    },
    PublicationVideoSchema,
    'publication',
  );

  // 4. Suivi jusqu'à la mise en ligne.
  let url = publie.url;
  if (!url) {
    const suivi = appelMcp(
      dossier,
      'YouTube',
      'get_video_status',
      {
        video_id: publie.video_id,
        consigne:
          'Interroge le statut jusqu\'à publication effective, puis retourne ' +
          '{"statut": "...", "url": "https://youtu.be/..."}. En cas d\'échec, utilise ' +
          'retry_video plutôt que de republier depuis zéro.',
      },
      StatutVideoSchema,
      'suivi',
    );
    if (suivi.erreur) {
      throw new Error(`Publication YouTube en échec : ${suivi.erreur} (retry_video conseillé)`);
    }
    url = suivi.url;
  }
  if (!url) throw new Error('Publication YouTube sans URL retournée.');

  const resultat = PublicationSchema.parse({
    ...publication,
    youtube: { url, video_id: publie.video_id, publie_le: new Date().toISOString() },
  });
  ecrireJson(cheminPublication, resultat);
  info(`   YouTube → ${url}`);
  return resultat;
};

/** Description : promesse, à quoi ça sert, chapitres, prompt Claude, liens. */
export const descriptionYoutube = (script: Script, rendu: Rendu): string =>
  [
    script.hook.promesse,
    '',
    script.intro.texte,
    '',
    'Chapitres',
    ...rendu.chapitres_youtube.map((c) => `${c.timecode} ${c.titre}`),
    '',
    'Le prompt Claude de ce tutoriel',
    script.segment_claude.prompt.texte,
    '',
    `La page du tutoriel : ${URL_ACADEMIE}/tutoriel/${script.meta.slug}`,
    `Essayer RapidoCRM : ${URL_ESSAI}`,
    `Tous les modules : ${URL_ACADEMIE}`,
  ].join('\n');

export const tags = (script: Script): string[] => [
  ...script.seo.youtube_tags,
  'RapidoCRM',
  'CRM français',
  'tutoriel CRM',
  script.meta.module,
];
