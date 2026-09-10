import { createInterface } from 'node:readline/promises';
import { existsSync } from 'node:fs';
import { join } from 'node:path';
import { ScriptSchema } from '../schema/index.ts';
import { DemandeEnAttente } from '../mcp/pont.ts';
import { lireJson } from '../util/chemins.ts';
import { avertir, chronometrer, consigner, info } from '../util/journal.ts';
import { analyser } from './analyse.ts';
import { construireFiche } from './fiche.ts';
import { construireScript, ecrireScriptMd, verifierScript } from './script.ts';
import { genererVoix } from './voix.ts';
import { rendre } from './rendu.ts';
import { genererVignettes } from './vignette.ts';
import { publierRapidoCms } from './publier-rapidocms.ts';
import { publierYoutube } from './publier-youtube.ts';
import { publierSite } from './publier-site.ts';
import { controlerQualite, exigerQaVerte } from './qa.ts';

export const ETAPES = [
  'analyse',
  'fiche',
  'script',
  'voix',
  'rendu',
  'vignette',
  'publier:cms',
  'publier:youtube',
  'publier:site',
] as const;
export type NomEtape = (typeof ETAPES)[number];

export interface OptionsTuto {
  from?: NomEtape;
  to?: NomEtape;
  dryRun?: boolean;
  force?: boolean;
  /** Mode série : prend le premier hook / la première punchline proposés. */
  autoHook?: boolean;
  autoPunchline?: boolean;
}

const dansLaPlage = (etape: NomEtape, options: OptionsTuto): boolean => {
  const i = ETAPES.indexOf(etape);
  const debut = options.from ? ETAPES.indexOf(options.from) : 0;
  const fin = options.to ? ETAPES.indexOf(options.to) : ETAPES.length - 1;
  return i >= debut && i <= fin;
};

/**
 * La chaîne complète. Une étape déjà faite est sautée sauf --force ; --from et
 * --to permettent de reprendre au milieu ; --dry-run fait tout sauf les trois
 * publications.
 *
 * Deux points d'arrêt ne sont JAMAIS contournés, même en mode série :
 * après l'écriture du script, et après le rendu de prévisualisation.
 */
export const orchestrer = async (dossier: string, options: OptionsTuto = {}): Promise<void> => {
  consigner(dossier, `--- tuto ${JSON.stringify(options)}`);

  try {
    if (dansLaPlage('analyse', options)) {
      await chronometrer(dossier, 'Analyse de l\'enregistrement', () =>
        analyser(dossier, { force: options.force }),
      );
    }

    if (dansLaPlage('fiche', options)) {
      await chronometrer(dossier, 'Fiche fonctionnelle (MCP RapidoCRM)', () =>
        construireFiche(dossier, { force: options.force }),
      );
    }

    if (dansLaPlage('script', options)) {
      await chronometrer(dossier, 'Rédaction du script', () =>
        construireScript(dossier, { force: options.force }),
      );
      await pointDArret1(dossier, options);
    }

    if (dansLaPlage('voix', options)) {
      await chronometrer(dossier, 'Voix off ElevenLabs', () =>
        genererVoix(dossier, { force: options.force }),
      );
    }

    if (dansLaPlage('rendu', options)) {
      await chronometrer(dossier, 'Rendu de prévisualisation', () =>
        rendre(dossier, { format: '16x9', preview: true, force: true }),
      );
      await pointDArret2(dossier);
      await chronometrer(dossier, 'Rendu final', () =>
        rendre(dossier, { format: 'tous', force: options.force }),
      );
    }

    if (dansLaPlage('vignette', options)) {
      await chronometrer(dossier, 'Vignettes', () => genererVignettes(dossier));
    }

    if (options.dryRun) {
      avertir('--dry-run : les trois publications sont sautées.');
      await controlerQualite(dossier);
      return;
    }

    await chronometrer(dossier, 'Contrôle qualité', () => controlerQualite(dossier));
    await exigerQaVerte(dossier);

    if (dansLaPlage('publier:cms', options)) {
      await chronometrer(dossier, 'Publication bibliothèque RapidoCMS', () =>
        publierRapidoCms(dossier),
      );
    }
    if (dansLaPlage('publier:youtube', options)) {
      await chronometrer(dossier, 'Publication YouTube', () => publierYoutube(dossier));
    }
    if (dansLaPlage('publier:site', options)) {
      await chronometrer(dossier, 'Publication du site', () => publierSite(dossier));
    }
  } catch (e) {
    if (e instanceof DemandeEnAttente) {
      info('');
      avertir(e.message);
      info('');
      info('  La chaîne reprendra où elle s\'est arrêtée à la prochaine exécution.');
      return;
    }
    throw e;
  }
};

/** Point d'arrêt 1 — relecture de script.md, choix du hook et de la punchline. */
const pointDArret1 = async (dossier: string, options: OptionsTuto): Promise<void> => {
  const script = ScriptSchema.parse(lireJson(join(dossier, 'script.json')));
  ecrireScriptMd(dossier, script);
  const analyse = lireJson<never>(join(dossier, 'analyse.json'));
  verifierScript(script, analyse);

  info('');
  info('  ── Point d\'arrêt 1 : relecture du script ──');
  info(`  Fichier : ${join(dossier, 'script.md')}`);
  info('');
  info(`  Hook retenu      : ${script.hook.texte}`);
  script.hook.alternatives.forEach((a, i) => info(`    ${i + 2}. ${a}`));
  info('');
  info(`  Punchline retenue: ${script.punchline.texte}`);
  script.punchline.alternatives.forEach((a, i) => info(`    ${i + 2}. ${a}`));
  info('');

  if (options.autoHook && options.autoPunchline) {
    info('  --auto-hook et --auto-punchline : les choix proposés sont conservés.');
    return;
  }
  await attendreValidation(
    '  Relisez script.md, corrigez-le si besoin, puis appuyez sur Entrée pour continuer ' +
      '(Ctrl+C pour arrêter). ',
  );
};

/** Point d'arrêt 2 — visionnage de la prévisualisation. */
const pointDArret2 = async (dossier: string): Promise<void> => {
  const preview = join(dossier, 'out', 'preview-16x9.mp4');
  info('');
  info('  ── Point d\'arrêt 2 : prévisualisation ──');
  info(`  Fichier : ${preview}${existsSync(preview) ? '' : ' (introuvable !)'}`);
  info('');
  await attendreValidation('  Regardez la vidéo, puis Entrée pour lancer le rendu final. ');
};

const attendreValidation = async (question: string): Promise<void> => {
  if (!process.stdin.isTTY) {
    throw new Error(
      'Point d\'arrêt atteint hors terminal interactif. Ces deux arrêts ne sont jamais ' +
        'contournés : relancez la commande depuis un terminal.',
    );
  }
  const rl = createInterface({ input: process.stdin, output: process.stdout });
  await rl.question(question);
  rl.close();
};
