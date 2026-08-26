import type { Alignement, Script } from '../schema/index.ts';

export const FPS = 30;

export interface Minutage {
  hook: { debut: number; duree: number };
  titre: { debut: number; duree: number };
  demo: { debut: number; duree: number; etapes: { debut: number; duree: number }[] };
  claude: { debut: number; duree: number };
  punchline: { debut: number; duree: number };
  total: number;
}

const enFrames = (secondes: number): number => Math.max(1, Math.round(secondes * FPS));

/**
 * Le minutage suit la voix off quand elle existe, et retombe sur les durées
 * annoncées dans le script sinon (mode Preview).
 */
export const calculerMinutage = (script: Script, alignement: Alignement | null): Minutage => {
  const dureeBloc = (id: string, defaut: number): number => {
    const bloc = alignement?.blocs.find((b) => b.id === id);
    return bloc ? bloc.duree : defaut;
  };

  const hookDuree = enFrames(dureeBloc('hook', script.hook.duree));
  const titreDuree = enFrames(dureeBloc('intro', script.intro.duree));

  let curseur = hookDuree + titreDuree;
  const demoDebut = curseur;
  const etapes = script.demo.etapes.map((etape) => {
    const defaut = Math.max(2, etape.fin_source - etape.debut_source);
    const duree = enFrames(dureeBloc(`etape-${String(etape.numero).padStart(2, '0')}`, defaut));
    const bloc = { debut: curseur, duree };
    curseur += duree;
    return bloc;
  });
  const demoDuree = curseur - demoDebut;

  const claudeDebut = curseur;
  const claudeDuree = enFrames(dureeBloc('claude', script.segment_claude.duree));
  curseur += claudeDuree;

  const punchlineDebut = curseur;
  const punchlineDuree = enFrames(dureeBloc('punchline', script.punchline.duree));
  curseur += punchlineDuree;

  return {
    hook: { debut: 0, duree: hookDuree },
    titre: { debut: hookDuree, duree: titreDuree },
    demo: { debut: demoDebut, duree: demoDuree, etapes },
    claude: { debut: claudeDebut, duree: claudeDuree },
    punchline: { debut: punchlineDebut, duree: punchlineDuree },
    total: curseur,
  };
};
