import { existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
import { racineContenu } from '../util/chemins.ts';
import { avertir, etape, info } from '../util/journal.ts';
import { rendre } from './rendu.ts';
import { genererVignettes } from './vignette.ts';
import { publierRapidoCms } from './publier-rapidocms.ts';
import { publierYoutube } from './publier-youtube.ts';
import { publierSite } from './publier-site.ts';

export const SEQUENCES = ['hook', 'titre', 'demo', 'claude', 'punchline'] as const;
export type NomSequence = (typeof SEQUENCES)[number];

/**
 * Régénération en masse : re-rend les vidéos d'un module après un changement du
 * template (par exemple l'animation du logo, séquence 5), puis republie les
 * nouveaux fichiers. On ne repasse ni par l'analyse ni par la voix off.
 */
export const regenerer = async (
  module: string,
  sequence: NomSequence,
  options: { republier?: boolean } = {},
): Promise<void> => {
  const base = join(racineContenu(), module);
  if (!existsSync(base)) throw new Error(`Module inconnu : ${module}`);

  const dossiers = readdirSync(base)
    .map((d) => join(base, d))
    .filter((d) => existsSync(join(d, 'script.json')) && existsSync(join(d, 'voix', 'alignement.json')));

  info(
    `  ${dossiers.length} tutoriel(s) à re-rendre dans ${module} ` +
      `(séquence « ${sequence} » modifiée)`,
  );
  avertir(
    'Remotion rend la composition entière : la séquence ciblée sert à tracer le motif ' +
      'du changement, pas à limiter le rendu.',
  );

  for (const dossier of dossiers) {
    etape(dossier);
    await rendre(dossier, { format: 'tous', force: true });
    await genererVignettes(dossier);

    if (options.republier) {
      await publierRapidoCms(dossier);
      await publierYoutube(dossier);
      await publierSite(dossier);
    }
  }
};
