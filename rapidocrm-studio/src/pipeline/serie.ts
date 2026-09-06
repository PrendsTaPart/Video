import { existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
import { z } from 'zod';
import { ScriptSchema, type Script } from '../schema/index.ts';
import { appelMcp } from '../mcp/pont.ts';
import { ecrireJson, fichierExiste, lireJson, racineContenu } from '../util/chemins.ts';
import { avertir, discret, info } from '../util/journal.ts';

const IncompletsSchema = z.object({
  tutoriels: z.array(
    z.object({
      module: z.string(),
      numero: z.number(),
      slug: z.string().default(''),
      manquant: z.array(z.string()).default([]),
    }),
  ),
});

export interface ElementFile {
  module: string;
  numero: number;
  dossier: string;
  manquant: string[];
}

/**
 * File de production : ce qui reste à faire, croisé avec les enregistrements
 * réellement présents dans content/.
 */
export const construireFile = (
  dossierPivot: string,
  module: string,
  limite?: number,
): ElementFile[] => {
  const incomplets = appelMcp(
    dossierPivot,
    'RapidoCMS tutoriels',
    'tutoriels_incomplets',
    {
      module,
      consigne:
        'Retourne les tutoriels du module encore incomplets, avec ce qui manque sur ' +
        'chacun (vidéo, transcription, SEO…).',
    },
    IncompletsSchema,
    `incomplets-${module}`,
  );

  const base = join(racineContenu(), module);
  const dossiers = existsSync(base) ? readdirSync(base) : [];

  const file: ElementFile[] = [];
  for (const tuto of incomplets.tutoriels) {
    const prefixe = `V${String(tuto.numero).padStart(2, '0')}`;
    const dossier = dossiers.find((d) => d.startsWith(prefixe));
    if (!dossier) {
      discret(`   ${prefixe} — pas de dossier dans content/, ignoré`);
      continue;
    }
    const chemin = join(base, dossier);
    if (!fichierExiste(join(chemin, 'source.mp4'))) {
      discret(`   ${prefixe} — pas de source.mp4, ignoré`);
      continue;
    }
    file.push({ module: tuto.module, numero: tuto.numero, dossier: chemin, manquant: tuto.manquant });
  }
  return limite ? file.slice(0, limite) : file;
};

/* ─────────────────── Cohérence de série ─────────────────── */

export interface Incoherence {
  gravite: 'alerte' | 'info';
  message: string;
}

/** Contrôles transverses sur l'ensemble d'un module — et du catalogue. */
export const verifierCoherenceSerie = (module: string): Incoherence[] => {
  const base = join(racineContenu(), module);
  const scripts = chargerScripts(base);
  const incoherences: Incoherence[] = [];

  // Aucun hook dupliqué dans le module.
  const hooks = new Map<string, string[]>();
  for (const [chemin, script] of scripts) {
    const cle = normaliser(script.hook.texte);
    hooks.set(cle, [...(hooks.get(cle) ?? []), chemin]);
  }
  for (const [, endroits] of hooks) {
    if (endroits.length > 1) {
      incoherences.push({
        gravite: 'alerte',
        message: `Hook dupliqué dans ${module} : ${endroits.join(', ')}`,
      });
    }
  }

  // Aucune punchline dupliquée sur tout le catalogue.
  const catalogue = chargerScripts(racineContenu(), true);
  const punchlines = new Map<string, string[]>();
  for (const [chemin, script] of catalogue) {
    const cle = normaliser(script.punchline.texte);
    punchlines.set(cle, [...(punchlines.get(cle) ?? []), chemin]);
  }
  for (const [, endroits] of punchlines) {
    if (endroits.length > 1) {
      incoherences.push({
        gravite: 'alerte',
        message: `Punchline dupliquée sur le catalogue : ${endroits.join(', ')}`,
      });
    }
  }

  // Prompts Claude du module qui se répètent à l'identique.
  const prompts = new Map<string, string[]>();
  for (const [chemin, script] of scripts) {
    const cle = normaliser(script.segment_claude.prompt.texte);
    prompts.set(cle, [...(prompts.get(cle) ?? []), chemin]);
  }
  for (const [, endroits] of prompts) {
    if (endroits.length > 1) {
      incoherences.push({
        gravite: 'alerte',
        message: `Prompt Claude identique dans ${module} : ${endroits.join(', ')}`,
      });
    }
  }

  // Durées homogènes : écart de plus de 40 % à la médiane du module.
  const durees = scripts
    .map(([chemin, script]) => {
      const rendu = join(chemin, '..', 'rendu.json');
      return existsSync(rendu)
        ? ([chemin, lireJson<{ duree: number }>(rendu).duree] as [string, number])
        : null;
    })
    .filter((x): x is [string, number] => x !== null);
  if (durees.length >= 3) {
    const triees = [...durees].sort((a, b) => a[1] - b[1]);
    const mediane = triees[Math.floor(triees.length / 2)]![1];
    for (const [chemin, duree] of durees) {
      if (Math.abs(duree - mediane) / mediane > 0.4) {
        incoherences.push({
          gravite: 'info',
          message: `${chemin} dure ${duree.toFixed(0)}s, à plus de 40 % de la médiane du module (${mediane.toFixed(0)}s)`,
        });
      }
    }
  }

  // Vocabulaire : chaque script est confronté au glossaire du catalogue.
  incoherences.push(...verifierGlossaire(scripts));

  return incoherences;
};

const chargerScripts = (racine: string, recursif = false): [string, Script][] => {
  if (!existsSync(racine)) return [];
  const resultats: [string, Script][] = [];
  const parcourir = (dossier: string, profondeur: number): void => {
    for (const entree of readdirSync(dossier, { withFileTypes: true })) {
      const chemin = join(dossier, entree.name);
      if (entree.isDirectory() && profondeur < 3) parcourir(chemin, profondeur + 1);
      else if (entree.name === 'script.json') {
        try {
          resultats.push([chemin, ScriptSchema.parse(lireJson(chemin))]);
        } catch {
          avertir(`script.json illisible : ${chemin}`);
        }
      }
    }
  };
  parcourir(racine, recursif ? 0 : 1);
  return resultats;
};

const normaliser = (texte: string): string =>
  texte.toLowerCase().replace(/[^a-zà-ÿ0-9 ]/g, '').replace(/\s+/g, ' ').trim();

/* ─────────────────── Glossaire ─────────────────── */

interface Glossaire {
  /** terme normalisé → forme canonique retenue */
  termes: Record<string, string>;
}

const cheminGlossaire = (): string => join(racineContenu(), 'glossaire.json');

export const chargerGlossaire = (): Glossaire =>
  existsSync(cheminGlossaire()) ? lireJson<Glossaire>(cheminGlossaire()) : { termes: {} };

/**
 * Alimente le glossaire au fil des scripts et signale toute variation de nom
 * d'un même élément d'interface d'une vidéo à l'autre.
 */
export const verifierGlossaire = (scripts: [string, Script][]): Incoherence[] => {
  const glossaire = chargerGlossaire();
  const incoherences: Incoherence[] = [];

  for (const [chemin, script] of scripts) {
    const termes = [
      ...script.demo.etapes.map((e) => e.annotation),
      ...script.demo.etapes.map((e) => e.titre),
    ].filter(Boolean);

    for (const terme of termes) {
      const cle = normaliser(terme);
      if (!cle) continue;
      const connu = glossaire.termes[cle];
      if (!connu) {
        glossaire.termes[cle] = terme;
      } else if (connu !== terme) {
        incoherences.push({
          gravite: 'alerte',
          message:
            `Vocabulaire : « ${terme} » dans ${chemin} alors que le glossaire retient ` +
            `« ${connu} ». Un même élément d'interface se nomme pareil partout.`,
        });
      }
    }
  }

  ecrireJson(cheminGlossaire(), glossaire);
  return incoherences;
};

/* ─────────────────── Tableau de bord ─────────────────── */

export interface Compteurs {
  fait: number;
  enCours: number;
  restant: number;
  tempsMoyen: number;
  creditsElevenLabs: number;
}

export const tableauDeBord = (compteurs: Compteurs): void => {
  info('');
  info('  ┌─ Production ────────────────────────────');
  info(`  │ fait      : ${compteurs.fait}`);
  info(`  │ en cours  : ${compteurs.enCours}`);
  info(`  │ restant   : ${compteurs.restant}`);
  info(`  │ moyenne   : ${compteurs.tempsMoyen.toFixed(1)} min / vidéo`);
  info(`  │ ElevenLabs: ~${compteurs.creditsElevenLabs} caractères consommés`);
  info('  └─────────────────────────────────────────');
  info('');
};

/** Caractères envoyés à ElevenLabs pour un tutoriel (approximation du crédit). */
export const creditsConsommes = (dossier: string): number => {
  const manifest = join(dossier, 'voix', 'manifest.json');
  if (!existsSync(manifest)) return 0;
  const script = join(dossier, 'script.json');
  if (!existsSync(script)) return 0;
  const s = ScriptSchema.parse(lireJson(script));
  return [
    s.hook.texte,
    s.hook.promesse,
    s.intro.texte,
    ...s.demo.etapes.map((e) => e.voix),
    s.segment_claude.voix,
    s.punchline.texte,
  ].join(' ').length;
};
