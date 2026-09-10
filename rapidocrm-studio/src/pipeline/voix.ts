import { createHash } from 'node:crypto';
import { copyFileSync, existsSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';
import {
  AlignementSchema,
  ScriptSchema,
  type Alignement,
  type BlocVoix,
  type Script,
} from '../schema/index.ts';
import { assurerDossier, ecrireJson, lireJson } from '../util/chemins.ts';
import { dureeAudio, lancer } from '../util/ffmpeg.ts';
import { avertir, discret, etape, info } from '../util/journal.ts';
import { pourLaVoix } from './prononciation.ts';

const REGLAGES = { stability: 0.45, similarity_boost: 0.8, style: 0.35 } as const;
const MODELE = 'eleven_multilingual_v2';
const SILENCE = 0.2; // 200 ms en tête et en queue
const LUFS = -16;

/**
 * La voix de RapidoCRM Académie — « Enrick - Calm French Narrator », validée sur
 * V01 et commune aux 172 tutoriels. ELEVENLABS_VOICE_ID peut la surcharger pour
 * un essai, mais la valeur par défaut est la référence de la série : on ne la
 * redéduit jamais d'un autre projet du dépôt.
 */
export const VOIX_SERIE = '0xHziZolI8Tp6rLtUqh2';

/**
 * Cache mutualisé entre tous les tutoriels. Une phrase identique d'une vidéo à
 * l'autre — « Copiez ce prompt, collez-le… », une punchline reprise — n'est
 * synthétisée qu'une fois : la clé est l'empreinte de la voix et du texte.
 */
const DOSSIER_CACHE = join('assets', 'voix-cache');
const cleCache = (voix: string, texte: string): string =>
  createHash('sha256').update(`${voix}\u0000${texte}`).digest('hex').slice(0, 32);

interface BlocSource {
  id: string;
  texte: string;
}

export interface OptionsVoix {
  force?: boolean;
}

/** Découpe le script en blocs : une piste par bloc, recalable indépendamment. */
export const blocsDuScript = (script: Script): BlocSource[] => [
  { id: 'hook', texte: `${script.hook.texte} ${script.hook.promesse}` },
  { id: 'intro', texte: script.intro.texte },
  ...script.demo.etapes.map((e) => ({
    id: `etape-${String(e.numero).padStart(2, '0')}`,
    texte: e.voix,
  })),
  { id: 'claude', texte: script.segment_claude.voix },
  { id: 'punchline', texte: script.punchline.texte },
];

/**
 * Étape 4 — voix off ElevenLabs.
 * Sorties : voix/*.mp3, voix/complete.mp3, voix/alignement.json,
 * transcription.txt, transcription-chapitres.json
 */
export const genererVoix = async (
  dossier: string,
  options: OptionsVoix = {},
): Promise<Alignement> => {
  const script = ScriptSchema.parse(lireJson(join(dossier, 'script.json')));
  const dossierVoix = assurerDossier(join(dossier, 'voix'));
  const cheminManifest = join(dossierVoix, 'manifest.json');
  const manifest: Record<string, string> = existsSync(cheminManifest)
    ? lireJson(cheminManifest)
    : {};

  const cle = process.env.ELEVENLABS_API_KEY;
  const voix = process.env.ELEVENLABS_VOICE_ID ?? VOIX_SERIE;

  const blocs = blocsDuScript(script);
  const resultats: BlocVoix[] = [];
  let curseur = 0;

  for (const bloc of blocs) {
    const texteVoix = pourLaVoix(bloc.texte);
    const empreinte = createHash('sha256').update(texteVoix).digest('hex').slice(0, 16);
    const fichier = join(dossierVoix, `${bloc.id}.mp3`);
    const alignementBloc = join(dossierVoix, `${bloc.id}.alignement.json`);

    // Cache mutualisé : la même phrase, dans une autre vidéo, est déjà payée.
    const cache = join(DOSSIER_CACHE, `${cleCache(voix, texteVoix)}.mp3`);
    const cacheAlignement = cache.replace(/\.mp3$/, '.alignement.json');
    if (!existsSync(fichier) && existsSync(cache)) {
      assurerDossier(dossierVoix);
      copyFileSync(cache, fichier);
      if (existsSync(cacheAlignement)) copyFileSync(cacheAlignement, alignementBloc);
      manifest[bloc.id] = empreinte;
      ecrireJson(cheminManifest, manifest);
      discret(`   ${bloc.id} — repris du cache mutualisé, synthèse évitée`);
    }

    // Cache : les crédits ElevenLabs sont comptés.
    const inchange = manifest[bloc.id] === empreinte && existsSync(fichier);
    // Piste déposée à la main ou générée hors pipeline : on la prend telle
    // quelle plutôt que d'échouer, et on l'inscrit au manifeste.
    const fournie = !inchange && existsSync(fichier) && !cle;

    if (inchange && !options.force) {
      discret(`   ${bloc.id} — inchangé, régénération évitée`);
    } else if (fournie && !options.force) {
      avertir(
        `${bloc.id} — piste déjà présente et pas de clé ElevenLabs : le fichier ` +
          'existant est utilisé tel quel.',
      );
      manifest[bloc.id] = empreinte;
      ecrireJson(cheminManifest, manifest);
    } else {
      if (!cle || !voix) {
        throw new Error(
          'ELEVENLABS_API_KEY et ELEVENLABS_VOICE_ID sont requis pour générer la voix ' +
            `(bloc « ${bloc.id} » à produire). Voir .env.example.`,
        );
      }
      etape(`Synthèse du bloc ${bloc.id}`);
      const { audio, mots } = await synthetiser(cle, voix, texteVoix);
      writeFileSync(fichier, audio);
      await normaliser(fichier);
      ecrireJson(alignementBloc, mots);
      manifest[bloc.id] = empreinte;
      ecrireJson(cheminManifest, manifest);
    }

    // Le cache se remplit quelle que soit l'origine de la piste : synthèse,
    // reprise, ou fichier déposé à la main.
    if (!existsSync(cache)) {
      assurerDossier(DOSSIER_CACHE);
      copyFileSync(fichier, cache);
      if (existsSync(alignementBloc)) copyFileSync(alignementBloc, cacheAlignement);
    }

    const duree = await dureeAudio(fichier);
    const mots = existsSync(alignementBloc)
      ? lireJson<{ mot: string; debut: number; fin: number }[]>(alignementBloc)
      : repartirUniformement(bloc.texte, duree);

    resultats.push({
      id: bloc.id,
      fichier: `voix/${bloc.id}.mp3`,
      debut: curseur,
      duree,
      texte: bloc.texte,
      mots,
    });
    curseur += duree;
  }

  // 5. Piste maîtresse : les blocs bout à bout, aux bons timecodes.
  await assembler(dossierVoix, resultats);

  const alignement: Alignement = AlignementSchema.parse({
    duree_totale: curseur,
    blocs: resultats,
  });
  ecrireJson(join(dossierVoix, 'alignement.json'), alignement);

  // 6. Transcription pour le SEO du site + chapitres horodatés.
  writeFileSync(
    join(dossier, 'transcription.txt'),
    resultats.map((b) => b.texte.trim()).join('\n\n'),
    'utf8',
  );
  ecrireJson(join(dossier, 'transcription-chapitres.json'), chapitres(script, resultats));

  info(`   voix : ${curseur.toFixed(1)} s sur ${resultats.length} blocs`);
  return alignement;
};

/** Synthèse + alignement mot à mot fourni par l'API. */
const synthetiser = async (
  cle: string,
  voix: string,
  texte: string,
): Promise<{ audio: Buffer; mots: { mot: string; debut: number; fin: number }[] }> => {
  const client = new ElevenLabsClient({ apiKey: cle });
  const reponse = (await client.textToSpeech.convertWithTimestamps(voix, {
    text: texte,
    modelId: MODELE,
    voiceSettings: REGLAGES,
  })) as unknown as {
    audioBase64: string;
    alignment?: {
      characters: string[];
      characterStartTimesSeconds: number[];
      characterEndTimesSeconds: number[];
    };
  };

  const audio = Buffer.from(reponse.audioBase64, 'base64');
  const mots = reponse.alignment
    ? motsDepuisCaracteres(
        reponse.alignment.characters,
        reponse.alignment.characterStartTimesSeconds,
        reponse.alignment.characterEndTimesSeconds,
      )
    : [];
  return { audio, mots };
};

/**
 * Regroupe l'alignement caractère par caractère en mots.
 *
 * Les balises SSML sont écartées. `pourLaVoix` ajoute une pause finale
 * `<break time="0.4s" />` : ElevenLabs la renvoie dans l'alignement, caractère
 * par caractère comme le reste du texte, et elle se retrouvait brûlée dans les
 * sous-titres — « facture n'est pas réglée. <break time="0.4s" /> ». Une balise
 * n'est jamais prononcée, elle n'a donc rien à faire dans un sous-titre.
 */
export const motsDepuisCaracteres = (
  caracteres: string[],
  debuts: number[],
  fins: number[],
): { mot: string; debut: number; fin: number }[] => {
  const mots: { mot: string; debut: number; fin: number }[] = [];
  let courant = '';
  let debut = 0;
  let dansBalise = false;
  caracteres.forEach((c, i) => {
    if (c === '<') {
      if (courant) {
        mots.push({ mot: courant, debut, fin: fins[i - 1] ?? debut });
        courant = '';
      }
      dansBalise = true;
      return;
    }
    if (dansBalise) {
      if (c === '>') dansBalise = false;
      return;
    }
    if (/\s/.test(c)) {
      if (courant) {
        mots.push({ mot: courant, debut, fin: fins[i - 1] ?? debut });
        courant = '';
      }
      return;
    }
    if (!courant) debut = debuts[i] ?? 0;
    courant += c;
  });
  if (courant) {
    mots.push({ mot: courant, debut, fin: fins[fins.length - 1] ?? debut });
  }
  return mots;
};

/** Repli quand l'API n'a pas rendu d'alignement : répartition au prorata. */
const repartirUniformement = (
  texte: string,
  duree: number,
): { mot: string; debut: number; fin: number }[] => {
  const mots = texte.trim().split(/\s+/).filter(Boolean);
  const pas = duree / Math.max(1, mots.length);
  return mots.map((mot, i) => ({ mot, debut: i * pas, fin: (i + 1) * pas }));
};

/** -16 LUFS + 200 ms de silence en tête et en queue. */
const normaliser = async (fichier: string): Promise<void> => {
  const temporaire = `${fichier}.tmp.mp3`;
  await lancer('ffmpeg', [
    '-y', '-i', fichier,
    '-af',
    `loudnorm=I=${LUFS}:TP=-1.5:LRA=11,adelay=${SILENCE * 1000}|${SILENCE * 1000},apad=pad_dur=${SILENCE}`,
    '-b:a', '192k',
    temporaire,
  ]);
  const { renameSync } = await import('node:fs');
  renameSync(temporaire, fichier);
};

/** voix/complete.mp3 — les blocs concaténés dans l'ordre. */
const assembler = async (dossierVoix: string, blocs: BlocVoix[]): Promise<void> => {
  const liste = join(dossierVoix, 'blocs.txt');
  writeFileSync(
    liste,
    blocs.map((b) => `file '${join(dossierVoix, `${b.id}.mp3`)}'`).join('\n'),
    'utf8',
  );
  await lancer('ffmpeg', [
    '-y', '-f', 'concat', '-safe', '0', '-i', liste,
    '-c:a', 'libmp3lame', '-b:a', '192k',
    join(dossierVoix, 'complete.mp3'),
  ]);
};

/** Format attendu par le MCP du site. */
const chapitres = (
  script: Script,
  blocs: BlocVoix[],
): { timestamp_secondes: number; titre: string; texte: string }[] => {
  const titre = (id: string): string => {
    if (id === 'hook') return 'Le problème';
    if (id === 'intro') return 'Ce qu\'on va faire';
    if (id === 'claude') return 'Faites-le avec Claude';
    if (id === 'punchline') return 'À retenir';
    const numero = Number(id.replace('etape-', ''));
    return script.demo.etapes.find((e) => e.numero === numero)?.titre ?? id;
  };
  return blocs.map((b) => ({
    timestamp_secondes: Math.round(b.debut),
    titre: titre(b.id),
    texte: b.texte.trim(),
  }));
};
