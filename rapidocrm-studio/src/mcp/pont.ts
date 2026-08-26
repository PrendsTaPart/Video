import { existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
import type { z } from 'zod';
import { assurerDossier, ecrireJson, fichierExiste, lireJson } from '../util/chemins.ts';

/**
 * Pont MCP.
 *
 * Les serveurs MCP (RapidoCRM, RapidoCMS, YouTube, RapidoCMS tutoriels) sont des
 * outils de Claude Code, pas des dépendances Node : un `tsx` lancé en CLI ne peut
 * pas les appeler lui-même. Le pipeline dépose donc une DEMANDE sur le disque,
 * Claude Code exécute l'appel MCP et écrit la RÉPONSE à côté, que zod valide.
 *
 *   mcp/<serveur>.<outil>.<cle>.demande.json   ← écrit par le pipeline
 *   mcp/<serveur>.<outil>.<cle>.reponse.json   ← écrit par Claude Code
 *
 * Tant que la réponse manque, `DemandeEnAttente` est levée : le CLI l'affiche
 * proprement et s'arrête. Relancer la même commande reprend là où on en était.
 */

export type Serveur = 'RapidoCRM' | 'RapidoCMS' | 'YouTube' | 'RapidoCMS tutoriels';

export class DemandeEnAttente extends Error {
  constructor(
    readonly serveur: Serveur,
    readonly outil: string,
    readonly chemin: string,
    readonly parametres: Record<string, unknown>,
  ) {
    super(
      `Appel MCP requis — ${serveur} › ${outil}\n` +
        `  Demande écrite dans : ${chemin}\n` +
        `  Réponse attendue    : ${chemin.replace('.demande.json', '.reponse.json')}\n` +
        `  Claude Code : exécute l'outil « ${outil} » du serveur « ${serveur} » avec les ` +
        `paramètres de la demande, écris le résultat brut dans le fichier de réponse, ` +
        `puis relance la commande.`,
    );
    this.name = 'DemandeEnAttente';
  }
}

const nettoyer = (s: string): string => s.replace(/[^a-zA-Z0-9_-]+/g, '-').toLowerCase();

export const dossierMcp = (dossierTuto: string): string =>
  assurerDossier(join(dossierTuto, 'mcp'));

/**
 * Demande un appel MCP. Retourne la réponse déjà déposée, ou lève
 * `DemandeEnAttente` après avoir écrit la demande.
 */
export const appelMcp = <T>(
  dossierTuto: string,
  serveur: Serveur,
  outil: string,
  parametres: Record<string, unknown>,
  schema: z.ZodType<T, z.ZodTypeDef, unknown>,
  cle = 'default',
): T => {
  const base = join(
    dossierMcp(dossierTuto),
    `${nettoyer(serveur)}.${nettoyer(outil)}.${nettoyer(cle)}`,
  );
  const reponse = `${base}.reponse.json`;

  if (fichierExiste(reponse)) {
    const brut = lireJson<unknown>(reponse);
    const analyse = schema.safeParse(brut);
    if (!analyse.success) {
      throw new Error(
        `Réponse MCP invalide dans ${reponse} :\n${analyse.error.issues
          .map((i) => `  · ${i.path.join('.')} — ${i.message}`)
          .join('\n')}`,
      );
    }
    return analyse.data;
  }

  const demande = `${base}.demande.json`;
  ecrireJson(demande, {
    serveur,
    outil,
    parametres,
    demande_le: new Date().toISOString(),
    consigne:
      'Exécute cet outil MCP, puis écris son résultat (JSON brut) dans le fichier ' +
      '.reponse.json portant le même nom.',
  });
  throw new DemandeEnAttente(serveur, outil, demande, parametres);
};

/** Toutes les demandes MCP encore sans réponse pour un tutoriel. */
export const demandesEnAttente = (dossierTuto: string): string[] => {
  const dossier = join(dossierTuto, 'mcp');
  if (!existsSync(dossier)) return [];
  return readdirSync(dossier)
    .filter((f) => f.endsWith('.demande.json'))
    .filter((f) => !existsSync(join(dossier, f.replace('.demande.json', '.reponse.json'))))
    .map((f) => join(dossier, f));
};
