import { existsSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import { z } from 'zod';
import {
  FicheSchema,
  PublicationSchema,
  RenduSchema,
  ScriptSchema,
  type Fiche,
  type Publication,
  type Script,
} from '../schema/index.ts';
import { appelMcp } from '../mcp/pont.ts';
import { ecrireJson, lireJson } from '../util/chemins.ts';
import { etape, info } from '../util/journal.ts';
import { compterMots } from './script.ts';
import { repond } from './publier-rapidocms.ts';

const Ok = z.object({}).passthrough();
const ReponseTutoriel = z.object({
  id: z.union([z.string(), z.number()]).optional(),
  url: z.string().url().optional(),
}).passthrough();

/**
 * Étape 9 — remplissage et publication de la page sur le site.
 * Il n'y a AUCUNE validation admin : ce que ce script publie est immédiatement
 * en ligne. Les contrôles ci-dessous sont donc bloquants.
 */
export const publierSite = async (dossier: string): Promise<Publication> => {
  const script = ScriptSchema.parse(lireJson(join(dossier, 'script.json')));
  const fiche = FicheSchema.parse(lireJson(join(dossier, 'fiche.json')));
  const rendu = RenduSchema.parse(lireJson(join(dossier, 'rendu.json')));
  const publication = PublicationSchema.parse(lireJson(join(dossier, 'publication.json')));

  const transcription = readFileSync(join(dossier, 'transcription.txt'), 'utf8');
  const chapitres = lireJson<{ timestamp_secondes: number; titre: string; texte: string }[]>(
    join(dossier, 'transcription-chapitres.json'),
  );

  await controlerAvantPublication(script, fiche, publication, transcription);

  const cleApi = process.env.RAPIDO_ACADEMIE_API_KEY;
  if (!cleApi) {
    throw new Error(
      'RAPIDO_ACADEMIE_API_KEY manquante : le MCP « RapidoCMS tutoriels » exige une clé ' +
        "d'API générée dans /admin/parametres.",
    );
  }
  const commun = { cle_api: cleApi, slug: script.meta.slug };

  // 1. Fiche
  etape('creer_tutoriel');
  const tutoriel = appelMcp(
    dossier,
    'RapidoCMS tutoriels',
    'creer_tutoriel',
    {
      ...commun,
      module: script.meta.module_slug ?? script.meta.module,
      numero: script.meta.numero,
      titre: script.meta.titre,
      titre_court: script.meta.titre_court,
      accroche: script.hook.promesse,
      explication: explication(script),
      // Le schéma de `creer_tutoriel` nomme le corps d'une étape « texte »,
      // pas « description » : une clé inconnue est rejetée à la validation.
      etapes: script.demo.etapes.map((e) => ({ titre: e.titre, texte: e.voix })),
      a_quoi_ca_sert: fiche.a_quoi_ca_sert,
      prerequis: fiche.prerequis,
    },
    ReponseTutoriel,
    'creer',
  );

  const appels: [string, Record<string, unknown>][] = [
    // 2. Vignette
    ['enregistrer_vignette', { ...commun, thumbnail_url: publication.rapidocms?.thumbnail_url }],
    // 3. Vidéo
    [
      'enregistrer_video',
      {
        ...commun,
        video_url: publication.rapidocms?.video_url,
        duree_secondes: Math.round(rendu.duree),
      },
    ],
    // 5. YouTube
    ['enregistrer_youtube', { ...commun, youtube_url: publication.youtube?.url }],
    // 6. Transcription
    [
      'enregistrer_transcription',
      {
        ...commun,
        transcription,
        // Côté Académie, un chapitre porte « debut », pas « timestamp_secondes ».
        chapitres: chapitres.map((c) => ({
          debut: c.timestamp_secondes,
          titre: c.titre,
          texte: c.texte,
        })),
      },
    ],
    // 7. Astuces
    [
      'ajouter_astuces',
      {
        ...commun,
        // « contenu » dans la fiche, « texte » côté Académie.
        astuces: fiche.astuces.map((a) => ({
          titre: a.titre,
          texte: a.contenu,
          niveau: a.niveau,
        })),
      },
    ],
    // 8. Cas d'usage
    [
      'ajouter_cas_usage',
      {
        ...commun,
        // L'Académie attend quatre champs, dont « action » — ce qu'on fait —
        // et « resultat », que la fiche appelle « resultat_attendu ». Sans
        // action rédigée, le titre du cas la tient : il est déjà écrit à
        // l'infinitif (« Mettre son offre au catalogue »).
        cas_usage: fiche.cas_usage.map((c) => ({
          titre: c.titre,
          contexte: c.contexte,
          action: c.action || c.titre,
          resultat: c.resultat_attendu,
        })),
      },
    ],
    // 9. Prompts Claude
    [
      'ajouter_prompts',
      {
        ...commun,
        prompts: [
          {
            titre: fiche.prompt_claude.titre,
            texte: script.segment_claude.prompt.texte,
            variables: script.segment_claude.prompt.variables,
            outil_mcp: script.segment_claude.prompt.outil_mcp || fiche.prompt_claude.outil_mcp,
          },
        ],
      },
    ],
    // 10. SEO
    [
      'enregistrer_seo',
      {
        ...commun,
        seo_titre: script.seo.titre,
        seo_description: script.seo.description,
        seo_mots_cles: script.seo.mots_cles,
        seo_og_image: publication.rapidocms?.thumbnail_url,
      },
    ],
    // 11. Agent IA de la page
    [
      'configurer_agent_tutoriel',
      {
        ...commun,
        // Le schéma de l'Académie nomme ces deux champs « agent_instructions »
        // et « agent_outils_mcp ». Envoyés sous « instructions » et
        // « outils_autorises », ils étaient ignorés : la mise à jour ne portait
        // sur aucune colonne et le serveur échouait sur son propre résultat
        // vide (« Cannot coerce the result to a single JSON object »), sans
        // que `updated_at` bouge.
        agent_instructions: instructionsAgent(script, fiche),
        agent_outils_mcp: fiche.outils_mcp.map((o) => o.nom),
      },
    ],
  ];

  // 4. Vidéo avatar, si elle existe pour ce tutoriel.
  const avatar = join(dossier, 'out', 'avatar.mp4');
  if (existsSync(avatar) && publication.rapidocms?.video_vertical_url) {
    appels.splice(3, 0, [
      'enregistrer_video_avatar',
      { ...commun, video_avatar_url: publication.rapidocms.video_vertical_url },
    ]);
  }

  for (const [outil, parametres] of appels) {
    etape(outil);
    appelMcp(dossier, 'RapidoCMS tutoriels', outil, parametres, Ok, outil);
  }

  // 12. Mise en ligne immédiate.
  etape('publier_tutoriel');
  const publie = appelMcp(
    dossier,
    'RapidoCMS tutoriels',
    'publier_tutoriel',
    { ...commun },
    ReponseTutoriel,
    'publier',
  );

  const url = publie.url ?? tutoriel.url;
  if (!url) throw new Error("Publication effectuée mais aucune URL de page retournée.");
  if (!(await repond(url))) {
    throw new Error(`La page publiée ne répond pas : ${url}`);
  }

  const resultat = PublicationSchema.parse({
    ...publication,
    site: {
      url,
      tutoriel_id: publie.id ?? tutoriel.id,
      publie_le: new Date().toISOString(),
    },
  });
  ecrireJson(join(dossier, 'publication.json'), resultat);

  info('');
  info('  Récapitulatif');
  info(`    Page       : ${url}`);
  info(`    YouTube    : ${publication.youtube?.url ?? '—'}`);
  info(`    AWS        : ${publication.rapidocms?.video_url ?? '—'}`);
  info(`    Durée      : ${Math.round(rendu.duree)} s`);
  info(`    Transcription : ${compterMots(transcription)} mots`);
  return resultat;
};

/** Contrôles bloquants avant publication — la page part en ligne sans validation. */
export const controlerAvantPublication = async (
  script: Script,
  fiche: Fiche,
  publication: Publication,
  transcription: string,
): Promise<void> => {
  const manques: string[] = [];

  const video = publication.rapidocms?.video_url;
  const youtube = publication.youtube?.url;
  if (!video) manques.push('video_url absent (npm run publier:cms)');
  else if (!(await repond(video))) manques.push(`video_url ne répond pas : ${video}`);
  if (!youtube) manques.push('youtube_url absent (npm run publier:youtube)');
  else if (!(await repond(youtube))) manques.push(`youtube_url ne répond pas : ${youtube}`);
  if (!publication.rapidocms?.thumbnail_url) manques.push('thumbnail_url absent');

  const mots = compterMots(transcription);
  // Même plancher que la QA, recalé sur le format court : 140 mots.
  if (mots < 140) manques.push(`transcription de ${mots} mots, minimum 140`);
  if (script.seo.titre.length > 60) manques.push('seo_titre dépasse 60 caractères');
  if (script.seo.description.length < 120 || script.seo.description.length > 155) {
    manques.push(
      `seo_description de ${script.seo.description.length} caractères, attendu 120–155`,
    );
  }
  if (script.demo.etapes.length < 3) manques.push('moins de 3 étapes');
  if (!script.segment_claude.prompt.texte) manques.push('aucun prompt Claude');
  if (!fiche.a_quoi_ca_sert.trim()) manques.push('a_quoi_ca_sert vide');
  if (!explication(script).trim()) manques.push('explication vide');

  if (manques.length > 0) {
    throw new Error(
      `Publication refusée — ${manques.length} contrôle(s) en échec :\n` +
        manques.map((m) => `  · ${m}`).join('\n'),
    );
  }
};

/** Le « comment ça marche » de la page, rédigé depuis les étapes du script. */
const explication = (script: Script): string =>
  [
    script.intro.texte,
    '',
    ...script.demo.etapes.map((e) => `${e.numero}. ${e.titre} — ${e.voix}`),
    '',
    script.segment_claude.voix,
  ].join('\n');

const instructionsAgent = (script: Script, fiche: Fiche): string =>
  [
    `Tu accompagnes un utilisateur sur « ${script.meta.titre} » (module ${script.meta.module_slug ?? script.meta.module}).`,
    `À quoi ça sert : ${fiche.a_quoi_ca_sert}`,
    `Pour qui : ${fiche.pour_qui}`,
    '',
    'Étapes du tutoriel :',
    ...script.demo.etapes.map((e) => `- ${e.numero}. ${e.titre}`),
    '',
    'Erreurs fréquentes à rappeler :',
    ...fiche.erreurs_frequentes.map((e) => `- ${e}`),
    '',
    'Vouvoie, phrases courtes, zéro jargon non expliqué. N\'affirme rien sur ' +
      'RapidoCRM qui ne figure pas dans ce tutoriel ou dans les outils autorisés.',
  ].join('\n');
