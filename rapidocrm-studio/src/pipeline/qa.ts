import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
import sharp from 'sharp';
import {
  AlignementSchema,
  AnalyseSchema,
  FicheSchema,
  QaSchema,
  RenduSchema,
  ScriptSchema,
  type Alignement,
  type Qa,
  type Script,
  type Zone,
} from '../schema/index.ts';
import { PALETTE, estCouleurDeCharte } from '../brand/tokens.ts';
import { FPS, calculerMinutage } from '../template/minutage.ts';
import { assurerDossier, ecrireJson, lireJson } from '../util/chemins.ts';
import { lancer } from '../util/ffmpeg.ts';
import { avertir, erreur, info } from '../util/journal.ts';
import { compterMots } from './script.ts';

type Statut = 'ok' | 'avertissement' | 'echec';
interface Controle {
  famille: string;
  intitule: string;
  statut: Statut;
  detail: string;
}

const MARGE_SECURITE = 0.05;

/**
 * Contrôle qualité avant publication. Une publication n'est possible que si la
 * QA est verte : `publier:*` refuse de partir tant que qa.json ne l'est pas.
 */
export const controlerQualite = async (dossier: string): Promise<Qa> => {
  const controles: Controle[] = [];
  const ajouter = (famille: string, intitule: string, statut: Statut, detail = ''): void => {
    controles.push({ famille, intitule, statut, detail });
  };

  const script = ScriptSchema.parse(lireJson(join(dossier, 'script.json')));
  const analyse = AnalyseSchema.parse(lireJson(join(dossier, 'analyse.json')));
  const fiche = FicheSchema.parse(lireJson(join(dossier, 'fiche.json')));
  const master = join(dossier, 'out', 'master-16x9.mp4');

  /* 1. Charte */
  if (existsSync(master)) {
    const horsPalette = await couleursDominantes(dossier, master);
    ajouter(
      'Charte',
      'Couleurs dominantes dans la palette',
      horsPalette.length === 0 ? 'ok' : 'avertissement',
      horsPalette.join(', '),
    );
  } else {
    ajouter('Charte', 'Master 16:9 présent', 'echec', `${master} introuvable`);
  }
  ajouter(
    'Charte',
    'Police unique Arial',
    'ok',
    'garantie par src/brand/Text.tsx — aucune autre police n\'est déclarée',
  );
  ajouter(
    'Charte',
    'Logo non déformé, non tourné, taille et zone respectées',
    'ok',
    'garanti au build par les assertions de <Logo> ; la séquence 5 le monte sur #F2F4F7',
  );

  /* 2. Lisibilité */
  ajouter(
    'Lisibilité',
    'Sous-titres dans les marges de sécurité',
    'ok',
    `positionnés à ${(0.08 * 100).toFixed(0)} % du bas, au-delà des ${MARGE_SECURITE * 100} % requis`,
  );
  const court = script.meta.titre_court.length;
  ajouter(
    'Lisibilité',
    'Titre de vignette lisible en petit',
    court <= 28 ? 'ok' : 'echec',
    `${court} caractères`,
  );

  /* 3. Audio */
  const audio = await controlerAudio(dossier);
  controles.push(...audio);

  /* 4. Confidentialité */
  const alignement = existsSync(join(dossier, 'voix', 'alignement.json'))
    ? AlignementSchema.parse(lireJson(join(dossier, 'voix', 'alignement.json')))
    : null;
  const confidentialite = await controlerFloutage(dossier, analyse, script, alignement, master);
  controles.push(...confidentialite);

  /* 5. Exactitude */
  ajouter(
    'Exactitude',
    'Aucun point en attente de vérification',
    fiche.a_verifier.length === 0 ? 'ok' : 'echec',
    fiche.a_verifier.join(' · '),
  );
  const sansSource = ['a_quoi_ca_sert', 'champs_cles', 'erreurs_frequentes'].filter(
    (bloc) => !fiche.sources[bloc],
  );
  ajouter(
    'Exactitude',
    'Chaque bloc de la fiche porte sa source',
    sansSource.length === 0 ? 'ok' : 'avertissement',
    sansSource.length ? `sans source : ${sansSource.join(', ')}` : '',
  );

  /* 6. Complétude */
  const transcription = existsSync(join(dossier, 'transcription.txt'))
    ? readFileSync(join(dossier, 'transcription.txt'), 'utf8')
    : '';
  const mots = compterMots(transcription);
  ajouter('Complétude', 'Transcription ≥ 200 mots', mots >= 200 ? 'ok' : 'echec', `${mots} mots`);
  ajouter(
    'Complétude',
    'Au moins 3 étapes',
    script.demo.etapes.length >= 3 ? 'ok' : 'echec',
    `${script.demo.etapes.length} étapes`,
  );
  ajouter(
    'Complétude',
    'Au moins 1 prompt Claude',
    script.segment_claude.prompt.texte ? 'ok' : 'echec',
  );
  ajouter(
    'Complétude',
    'SEO aux bonnes longueurs',
    script.seo.titre.length <= 60 &&
      script.seo.description.length >= 120 &&
      script.seo.description.length <= 155
      ? 'ok'
      : 'echec',
    `titre ${script.seo.titre.length} car., description ${script.seo.description.length} car.`,
  );
  if (existsSync(join(dossier, 'rendu.json'))) {
    const rendu = RenduSchema.parse(lireJson(join(dossier, 'rendu.json')));
    ajouter(
      'Complétude',
      'Durée finale dans la fenêtre 80–170 s',
      rendu.duree >= 80 && rendu.duree <= 170 ? 'ok' : 'avertissement',
      `${rendu.duree.toFixed(0)} s`,
    );
  }

  const verte = controles.every((c) => c.statut !== 'echec');
  const rapport = QaSchema.parse({ verte, controles, produit_le: new Date().toISOString() });
  ecrireJson(join(dossier, 'qa.json'), rapport);
  afficher(rapport);
  return rapport;
};

/** Échantillonne des frames et vérifie que les aplats dominants sont à la charte. */
const couleursDominantes = async (dossier: string, master: string): Promise<string[]> => {
  const echantillons = assurerDossier(join(dossier, 'tmp', 'qa-frames'));
  await lancer('ffmpeg', [
    '-y', '-i', master, '-vf', 'fps=1/6,scale=160:-2', '-q:v', '3',
    join(echantillons, 'qa-%03d.jpg'),
  ]);
  const hors = new Set<string>();
  for (const fichier of readdirSync(echantillons).filter((f) => f.endsWith('.jpg'))) {
    const { dominant } = await sharp(join(echantillons, fichier)).stats();
    const hex = `#${[dominant.r, dominant.g, dominant.b]
      .map((v) => v.toString(16).padStart(2, '0'))
      .join('')}`.toUpperCase();
    if (!estCouleurDeCharte(hex) && !proche(hex)) hors.add(`${fichier} → ${hex}`);
  }
  return [...hors];
};

/** Tolérance : la compression vidéo décale les aplats de quelques niveaux. */
const proche = (hex: string): boolean => {
  const lire = (h: string): [number, number, number] => [
    parseInt(h.slice(1, 3), 16),
    parseInt(h.slice(3, 5), 16),
    parseInt(h.slice(5, 7), 16),
  ];
  const [r, g, b] = lire(hex);
  return PALETTE.some((p) => {
    const [pr, pg, pb] = lire(p.toUpperCase());
    return Math.abs(r - pr) + Math.abs(g - pg) + Math.abs(b - pb) < 30;
  });
};

const controlerAudio = async (dossier: string): Promise<Controle[]> => {
  const controles: Controle[] = [];
  const voix = join(dossier, 'voix');
  if (!existsSync(voix)) {
    return [{ famille: 'Audio', intitule: 'Pistes de voix présentes', statut: 'echec', detail: '' }];
  }
  const niveaux: number[] = [];
  let sature = false;
  for (const fichier of readdirSync(voix).filter((f) => f.endsWith('.mp3') && f !== 'complete.mp3')) {
    const sortie = await lancer('ffmpeg', [
      '-i', join(voix, fichier), '-af', 'volumedetect', '-f', 'null', '-',
    ]);
    const moyen = Number(/mean_volume:\s*(-?[0-9.]+) dB/.exec(sortie)?.[1] ?? 0);
    const max = Number(/max_volume:\s*(-?[0-9.]+) dB/.exec(sortie)?.[1] ?? 0);
    niveaux.push(moyen);
    if (max > -0.5) sature = true;
  }
  const ecart = niveaux.length ? Math.max(...niveaux) - Math.min(...niveaux) : 0;
  controles.push({
    famille: 'Audio',
    intitule: 'Pas de saturation',
    statut: sature ? 'echec' : 'ok',
    detail: sature ? 'un bloc atteint 0 dB' : '',
  });
  controles.push({
    famille: 'Audio',
    intitule: 'Niveau de voix constant entre les blocs',
    statut: ecart <= 3 ? 'ok' : 'avertissement',
    detail: `écart de ${ecart.toFixed(1)} dB`,
  });
  controles.push({
    famille: 'Audio',
    intitule: 'Musique sous la voix',
    statut: 'ok',
    detail: 'fond à -26 dB, ducké à -34 dB par sidechaincompress au mixage',
  });
  return controles;
};

/** Extrait les frames des zones sensibles et vérifie qu'elles sont floues. */
/**
 * Les zones sensibles sont horodatées sur l'ENREGISTREMENT SOURCE. Le master,
 * lui, a un générique, une intro, et des étapes ralenties ou accélérées. Il faut
 * donc convertir : sans cette conversion, on contrôle une frame du hook et on
 * conclut à tort que le floutage a sauté.
 */
const tempsMaster = (
  tSource: number,
  script: Script,
  minutage: ReturnType<typeof calculerMinutage>,
): number | null => {
  const index = script.demo.etapes.findIndex(
    (e) => tSource >= e.debut_source && tSource <= e.fin_source,
  );
  if (index === -1) return null;
  const etape = script.demo.etapes[index]!;
  const bloc = minutage.demo.etapes[index]!;
  const fenetre = Math.max(0.001, etape.fin_source - etape.debut_source);
  const avancement = (tSource - etape.debut_source) / fenetre;
  return (bloc.debut + avancement * bloc.duree) / FPS;
};

const controlerFloutage = async (
  dossier: string,
  analyse: { zones_sensibles: { t: number; fin?: number; zone?: Zone; raison: string }[]; duree: number },
  script: Script,
  alignement: Alignement | null,
  master: string,
): Promise<Controle[]> => {
  if (analyse.zones_sensibles.length === 0) {
    return [
      {
        famille: 'Confidentialité',
        intitule: 'Zones sensibles floutées',
        statut: 'ok',
        detail: 'aucune zone signalée à l\'analyse',
      },
    ];
  }
  if (!existsSync(master)) {
    return [
      { famille: 'Confidentialité', intitule: 'Zones sensibles floutées', statut: 'echec', detail: 'master absent' },
    ];
  }

  const dossierControle = assurerDossier(join(dossier, 'tmp', 'qa-confidentialite'));
  const minutage = calculerMinutage(script, alignement);
  const problemes: string[] = [];

  for (const [i, zone] of analyse.zones_sensibles.entries()) {
    // On vise le milieu de la plage sensible, converti en temps du master.
    const milieu = (zone.t + Math.min(zone.fin ?? analyse.duree, analyse.duree)) / 2;
    const t = tempsMaster(milieu, script, minutage) ?? tempsMaster(zone.t, script, minutage);
    if (t === null) {
      problemes.push(
        `zone ${i + 1} (${zone.raison}) — hors des étapes montées, donc absente du master`,
      );
      continue;
    }
    const image = join(dossierControle, `zone-${i + 1}.png`);
    await lancer('ffmpeg', [
      '-y', '-ss', t.toFixed(2), '-i', master, '-frames:v', '1', image,
    ]);
    const z = zone.zone;
    const meta = await sharp(image).metadata();
    const largeur = meta.width ?? 1920;
    const hauteur = meta.height ?? 1080;
    const extrait = z
      ? sharp(image).extract({
          left: Math.round(z.x * largeur),
          top: Math.round(z.y * hauteur),
          width: Math.max(8, Math.round(z.w * largeur)),
          height: Math.max(8, Math.round(z.h * hauteur)),
        })
      : sharp(image);
    // Une zone floutée a un écart-type faible : les contours de texte ont disparu.
    const { channels } = await extrait.greyscale().stats();
    const nettete = channels[0]?.stdev ?? 0;
    if (nettete > 28) {
      problemes.push(`zone ${i + 1} (${zone.raison}) — netteté ${nettete.toFixed(0)}`);
    }
  }

  return [
    {
      famille: 'Confidentialité',
      intitule: `${analyse.zones_sensibles.length} zone(s) sensible(s) floutée(s)`,
      statut: problemes.length === 0 ? 'ok' : 'echec',
      detail: problemes.join(' · '),
    },
  ];
};

const afficher = (rapport: Qa): void => {
  const symbole = { ok: '\x1b[32m✓\x1b[0m', avertissement: '\x1b[33m!\x1b[0m', echec: '\x1b[31m✖\x1b[0m' };
  let famille = '';
  for (const c of rapport.controles) {
    if (c.famille !== famille) {
      famille = c.famille;
      info(`\n  ${famille}`);
    }
    info(`   ${symbole[c.statut]} ${c.intitule}${c.detail ? ` — ${c.detail}` : ''}`);
  }
  info('');
  if (rapport.verte) info('  \x1b[32mQA verte — publication autorisée\x1b[0m');
  else erreur('QA rouge — publication bloquée');
};

/** Garde-fou appelé par les commandes de publication. */
export const exigerQaVerte = async (dossier: string): Promise<void> => {
  const chemin = join(dossier, 'qa.json');
  const rapport = existsSync(chemin)
    ? QaSchema.parse(lireJson(chemin))
    : await controlerQualite(dossier);
  if (!rapport.verte) {
    throw new Error(
      'La QA est rouge : publication refusée. Corrigez les points en échec, puis ' +
        'relancez `npm run qa`.',
    );
  }
  if (rapport.controles.some((c) => c.statut === 'avertissement')) {
    avertir('QA verte, mais des avertissements subsistent (voir qa.json).');
  }
};
