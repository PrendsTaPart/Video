import { existsSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { z } from 'zod';
import { AnalyseSchema, FicheSchema, type Analyse, type Fiche } from '../schema/index.ts';
import { appelMcp } from '../mcp/pont.ts';
import { ecrireJson, lireJson } from '../util/chemins.ts';
import { avertir, discret, info } from '../util/journal.ts';

/** Inventaire des outils exposés par le MCP RapidoCRM. */
const InventaireSchema = z.object({
  outils: z.array(
    z.object({
      nom: z.string(),
      description: z.string().default(''),
      parametres: z
        .array(
          z.object({
            nom: z.string(),
            type: z.string().default('string'),
            obligatoire: z.boolean().default(false),
            valeurs_autorisees: z.array(z.string()).default([]),
            description: z.string().default(''),
          }),
        )
        .default([]),
    }),
  ),
});
export type Inventaire = z.infer<typeof InventaireSchema>;

export interface OptionsFiche {
  force?: boolean;
  /** Mots-clés servant à repérer les outils MCP liés à la fonctionnalité. */
  motsCles?: string[];
}

/**
 * Étape 2 — compréhension métier via le MCP RapidoCRM.
 *
 * But : produire une fiche fiable AVANT le script, pour ne jamais inventer une
 * fonctionnalité. Chaque bloc de la fiche porte sa source ; ce qui n'a pas pu
 * être vérifié va dans `a_verifier`, jamais dans une affirmation.
 */
export const construireFiche = async (
  dossier: string,
  options: OptionsFiche = {},
): Promise<Fiche> => {
  const cible = join(dossier, 'fiche.json');
  if (existsSync(cible) && !options.force) {
    discret('   fiche.json déjà présent — étape sautée (--force pour refaire)');
    return FicheSchema.parse(lireJson(cible));
  }

  const analyse = AnalyseSchema.parse(lireJson(join(dossier, 'analyse.json')));

  // 1 + 2. Inventaire réel des outils MCP (lecture seule).
  const inventaire = appelMcp(
    dossier,
    'RapidoCRM',
    'inventaire_outils',
    {
      consigne:
        'Liste les outils du serveur MCP RapidoCRM avec, pour chacun, son nom, sa ' +
        'description et le schéma de ses paramètres (nom, type, obligatoire, valeurs ' +
        'autorisées). Aucune écriture dans le CRM.',
    },
    InventaireSchema,
    'inventaire',
  );

  const motsCles = options.motsCles ?? motsClesDepuisAnalyse(analyse);
  const pertinents = inventaire.outils.filter((o) =>
    motsCles.some(
      (m) =>
        o.nom.toLowerCase().includes(m) || o.description.toLowerCase().includes(m),
    ),
  );
  info(
    `   ${pertinents.length} outil(s) MCP pertinent(s) : ` +
      (pertinents.map((o) => o.nom).join(', ') || '(aucun)'),
  );

  // 3. Croisement analyse ↔ schémas réels : les étapes observées doivent
  //    correspondre à des champs qui existent vraiment.
  const divergences = croiser(analyse, pertinents);
  for (const d of divergences) avertir(d);

  // 4. Rédaction : travail de modèle, cadré par une consigne écrite sur disque.
  const consigne = join(dossier, 'fiche-demande.md');
  ecrireJson(join(dossier, 'fiche-outils.json'), { outils: pertinents, divergences });
  writeFileSync(consigne, consigneFiche(analyse, pertinents, divergences), 'utf8');

  if (!existsSync(cible)) {
    throw new Error(
      `Rédaction de la fiche requise.\n` +
        `  Outils MCP retenus : ${join(dossier, 'fiche-outils.json')}\n` +
        `  Consigne           : ${consigne}\n` +
        `  Claude Code : écris ${cible} selon FicheSchema, puis relance.`,
    );
  }

  const fiche = FicheSchema.parse(lireJson(cible));
  verifierTracabilite(fiche, pertinents);
  return fiche;
};

const motsClesDepuisAnalyse = (analyse: Analyse): string[] => {
  const mots = new Set<string>();
  for (const e of analyse.etapes) {
    for (const mot of e.titre.toLowerCase().split(/[^a-zàâäéèêëîïôöùûüç]+/)) {
      if (mot.length > 4) mots.add(mot.replace(/s$/, ''));
    }
  }
  for (const ecran of analyse.ecrans) {
    const mot = ecran.nom.toLowerCase().split(' ')[0];
    if (mot && mot.length > 4) mots.add(mot.replace(/s$/, ''));
  }
  return [...mots];
};

/** Signale les écarts entre ce qu'on voit à l'écran et les schémas réels. */
const croiser = (
  analyse: Analyse,
  outils: Inventaire['outils'],
): string[] => {
  const champs = new Set(
    outils.flatMap((o) => o.parametres.map((p) => p.nom.toLowerCase())),
  );
  const ecarts: string[] = [];
  for (const action of analyse.actions) {
    if (action.type !== 'saisie' && action.type !== 'selection') continue;
    const cible = action.cible.toLowerCase();
    const connu = [...champs].some((c) => cible.includes(c) || c.includes(cible.split(' ')[0] ?? ''));
    if (!connu) {
      ecarts.push(
        `Divergence : « ${action.cible} » (${action.t.toFixed(1)}s) ne correspond à ` +
          'aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.',
      );
    }
  }
  return ecarts;
};

const consigneFiche = (
  analyse: Analyse,
  outils: Inventaire['outils'],
  divergences: string[],
): string => `# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne \`sources\` pour chaque bloc, par exemple
\`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}\`.
Ce que tu ne peux pas vérifier va dans \`a_verifier\` — jamais dans une affirmation.

## Étapes observées à l'écran

${analyse.etapes.map((e) => `- ${e.numero}. ${e.titre} (${e.debut.toFixed(1)}s → ${e.fin.toFixed(1)}s)`).join('\n')}

## Outils MCP retenus

${outils.map((o) => `- \`${o.nom}\` — ${o.description || 'sans description'}\n  paramètres : ${o.parametres.map((p) => `${p.nom}${p.obligatoire ? '*' : ''}`).join(', ') || '(aucun)'}`).join('\n') || '(aucun outil ne correspond — dis-le dans a_verifier)'}

${divergences.length ? `## Divergences à traiter\n\n${divergences.map((d) => `- ${d}`).join('\n')}\n` : ''}
## Rappels de fond

- \`a_quoi_ca_sert\` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- \`prompt_claude\` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- \`erreurs_frequentes\` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : \`src/schema/index.ts\` → \`FicheSchema\`.
`;

const verifierTracabilite = (fiche: Fiche, outils: Inventaire['outils']): void => {
  if (fiche.a_verifier.length > 0) {
    avertir(
      `fiche.json contient ${fiche.a_verifier.length} point(s) à vérifier — ` +
        'la publication sera bloquée par la QA tant qu\'ils ne sont pas levés :\n' +
        fiche.a_verifier.map((a) => `     · ${a}`).join('\n'),
    );
  }
  const connus = new Set(outils.map((o) => o.nom));
  for (const outil of fiche.outils_mcp) {
    if (connus.size > 0 && !connus.has(outil.nom)) {
      throw new Error(
        `fiche.json cite l'outil MCP « ${outil.nom} », absent de l'inventaire réel ` +
          'du serveur RapidoCRM. Un outil ne s\'invente pas.',
      );
    }
  }
  if (fiche.prompt_claude.outil_mcp && connus.size > 0 && !connus.has(fiche.prompt_claude.outil_mcp)) {
    throw new Error(
      `Le prompt Claude vise l'outil « ${fiche.prompt_claude.outil_mcp} », qui n'existe ` +
        'pas dans le MCP RapidoCRM.',
    );
  }
};
