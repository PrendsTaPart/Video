import { existsSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import {
  AnalyseSchema,
  FicheSchema,
  ScriptSchema,
  type Analyse,
  type Fiche,
  type Script,
} from '../schema/index.ts';
import { ecrireJson, lireJson } from '../util/chemins.ts';
import { avertir, discret, info } from '../util/journal.ts';

export const DEBIT_MOTS_MINUTE = 150;
// Format court : les scripts sont volontairement resserrés, un tutoriel de
// quatre étapes tient en une minute. Même recalage que la QA et que
// `controlerAvantPublication`.
const CIBLE_MIN = 55;
const CIBLE_MAX = 150;

export const compterMots = (texte: string): number =>
  texte.trim().split(/\s+/).filter(Boolean).length;

export const dureeParole = (texte: string): number =>
  (compterMots(texte) / DEBIT_MOTS_MINUTE) * 60;

export interface OptionsScript {
  force?: boolean;
}

/**
 * Étape 3 — rédaction du script. Entrées : analyse.json + fiche.json.
 * Sortie : script.json (source unique du rendu) + script.md (relecture humaine).
 */
export const construireScript = async (
  dossier: string,
  options: OptionsScript = {},
): Promise<Script> => {
  const cible = join(dossier, 'script.json');
  if (existsSync(cible) && !options.force) {
    discret('   script.json déjà présent — étape sautée (--force pour refaire)');
    const script = ScriptSchema.parse(lireJson(cible));
    ecrireScriptMd(dossier, script);
    verifierScript(script, AnalyseSchema.parse(lireJson(join(dossier, 'analyse.json'))));
    return script;
  }

  const analyse = AnalyseSchema.parse(lireJson(join(dossier, 'analyse.json')));
  const fiche = FicheSchema.parse(lireJson(join(dossier, 'fiche.json')));

  const consigne = join(dossier, 'script-demande.md');
  writeFileSync(consigne, consigneScript(analyse, fiche), 'utf8');
  ecrireJson(join(dossier, 'script-squelette.json'), squelette(analyse, fiche, dossier));

  throw new Error(
    `Rédaction du script requise.\n` +
      `  Squelette : ${join(dossier, 'script-squelette.json')}\n` +
      `  Consigne  : ${consigne}\n` +
      `  Claude Code : écris ${cible} selon ScriptSchema (3 hooks et 3 punchlines ` +
      'proposés dans `alternatives`), puis relance.',
  );
};

/** Pré-remplit ce qui se déduit mécaniquement de l'analyse et de la fiche. */
const squelette = (analyse: Analyse, fiche: Fiche, dossier: string) => ({
  meta: {
    module: dossier.split('/').slice(-2)[0] ?? '',
    numero: Number(/V(\d+)/.exec(dossier)?.[1] ?? 1),
    titre: fiche.fonctionnalite,
    titre_court: fiche.fonctionnalite.slice(0, 28),
    slug: fiche.fonctionnalite
      .toLowerCase()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-|-$/g, ''),
  },
  demo: {
    etapes: analyse.etapes.map((e) => ({
      numero: e.numero,
      titre: e.titre,
      voix: '',
      debut_source: e.debut,
      fin_source: e.fin,
      zone_focus: e.zone_focus,
      annotation: e.titre,
    })),
  },
  segment_claude: {
    accroche: 'Ou demandez-le simplement.',
    voix: "Vous n'avez pas envie de cliquer ? Copiez ce prompt, collez-le dans Claude, et c'est fait.",
    prompt: {
      texte: fiche.prompt_claude.texte,
      variables: fiche.prompt_claude.variables,
      outil_mcp: fiche.prompt_claude.outil_mcp,
    },
  },
});

const consigneScript = (analyse: Analyse, fiche: Fiche): string => `# Rédaction du script

## Ton — à respecter strictement

Français, vouvoiement, phrases courtes, rythme vif. Ludique sans être puéril.
Compréhensible d'un débutant total **et** utile à un expert : le débutant suit
les étapes, l'expert apprend les astuces et le prompt Claude.
Zéro jargon non expliqué — un mot technique (segment, workflow, webhook) est
défini en cinq mots à sa première occurrence.
Jamais « il suffit de », jamais « c'est très simple » : ça culpabilise celui qui
bloque. On dit **ce que ça change** pour l'utilisateur avant de dire où cliquer.

## Fabrication

- **Hook** : une question ou un constat qui pointe la douleur — jamais une
  description de fonctionnalité. Propose **3 alternatives** dans \`hook.alternatives\`.
- **Punchline** : courte, imagée, tournée vers le bénéfice — jamais un slogan
  générique. Propose **3 alternatives** dans \`punchline.alternatives\`.
- **Débit 150 mots/minute** : la voix de chaque étape doit tenir dans sa fenêtre
  vidéo (\`fin_source − debut_source\`). Si la voix déborde, on **ralentit la vidéo
  source** au rendu, on n'accélère jamais la voix.
- **Durée cible 55 à 150 s.** Si ça dépasse, on coupe dans la démo — jamais dans
  le hook ni dans la punchline.

## Matière disponible

À quoi ça sert : ${fiche.a_quoi_ca_sert}
Pour qui : ${fiche.pour_qui}
Prompt Claude : ${fiche.prompt_claude.texte}

Étapes observées :
${analyse.etapes.map((e) => `- ${e.numero}. ${e.titre} — fenêtre ${(e.fin - e.debut).toFixed(1)}s, soit ~${Math.floor(((e.fin - e.debut) / 60) * 150)} mots`).join('\n')}

Astuces : ${fiche.astuces.map((a) => a.titre).join(' · ') || '(aucune)'}
Erreurs fréquentes : ${fiche.erreurs_frequentes.join(' · ') || '(aucune)'}

## SEO

\`seo.titre\` ≤ 60 caractères · \`seo.description\` entre 120 et 155 caractères ·
\`seo.youtube_titre\` ≤ 70 caractères, au format « <Titre> — RapidoCRM ».

Schéma : \`src/schema/index.ts\` → \`ScriptSchema\`.
`;

/** Contrôles de fabrication : débit, fenêtres, durée totale. */
export const verifierScript = (script: Script, analyse: Analyse): string[] => {
  const alertes: string[] = [];

  for (const etape of script.demo.etapes) {
    const fenetre = etape.fin_source - etape.debut_source;
    const parole = dureeParole(etape.voix);
    if (parole > fenetre * 1.45) {
      alertes.push(
        `Étape ${etape.numero} « ${etape.titre} » : ${parole.toFixed(1)}s de voix pour ` +
          `${fenetre.toFixed(1)}s de vidéo. Le ralenti maximum est 0,7× — raccourcissez le texte.`,
      );
    } else if (parole > fenetre) {
      alertes.push(
        `Étape ${etape.numero} : la voix (${parole.toFixed(1)}s) déborde de la fenêtre ` +
          `(${fenetre.toFixed(1)}s) — la vidéo sera ralentie à ${(fenetre / parole).toFixed(2)}×.`,
      );
    }
    if (etape.fin_source > analyse.duree + 0.5) {
      alertes.push(
        `Étape ${etape.numero} pointe au-delà de la fin de l'enregistrement.`,
      );
    }
  }

  const total =
    dureeParole(script.hook.texte + ' ' + script.hook.promesse) +
    dureeParole(script.intro.texte) +
    script.demo.etapes.reduce((s, e) => s + Math.max(dureeParole(e.voix), e.fin_source - e.debut_source), 0) +
    dureeParole(script.segment_claude.voix) +
    dureeParole(script.punchline.texte);

  info(`   durée estimée : ${total.toFixed(0)} s`);
  if (total < CIBLE_MIN || total > CIBLE_MAX) {
    alertes.push(
      `Durée estimée ${total.toFixed(0)}s, hors cible ${CIBLE_MIN}–${CIBLE_MAX}s. ` +
        'Coupez dans la démo, jamais dans le hook ni la punchline.',
    );
  }
  for (const a of alertes) avertir(a);
  return alertes;
};

/** script.md — relecture et correction à la main avant le rendu. */
export const ecrireScriptMd = (dossier: string, script: Script): void => {
  const lignes = [
    `# ${script.meta.titre}`,
    '',
    `Module **${script.meta.module}** · V${String(script.meta.numero).padStart(2, '0')} · \`${script.meta.slug}\``,
    '',
    '## Hook',
    '',
    `> ${script.hook.texte}`,
    `> ${script.hook.promesse}`,
    '',
    ...(script.hook.alternatives.length
      ? ['**Alternatives proposées :**', ...script.hook.alternatives.map((a, i) => `${i + 1}. ${a}`), '']
      : []),
    '## Intro',
    '',
    script.intro.texte,
    '',
    '## Démo',
    '',
    ...script.demo.etapes.flatMap((e) => [
      `### ${e.numero}. ${e.titre}`,
      '',
      `_${e.debut_source.toFixed(1)}s → ${e.fin_source.toFixed(1)}s · ${compterMots(e.voix)} mots · ~${dureeParole(e.voix).toFixed(1)}s_`,
      '',
      e.voix,
      '',
    ]),
    '## Faites-le avec Claude',
    '',
    `**${script.segment_claude.accroche}**`,
    '',
    script.segment_claude.voix,
    '',
    '```',
    script.segment_claude.prompt.texte,
    '```',
    '',
    `Résultat affiché : **${script.segment_claude.resultat_affiche.titre}** — ${script.segment_claude.resultat_affiche.lignes.join(' · ')}`,
    '',
    '## Punchline',
    '',
    `> ${script.punchline.texte}`,
    '',
    ...(script.punchline.alternatives.length
      ? ['**Alternatives proposées :**', ...script.punchline.alternatives.map((a, i) => `${i + 1}. ${a}`), '']
      : []),
    '## SEO',
    '',
    `- Titre : ${script.seo.titre} _(${script.seo.titre.length} car.)_`,
    `- Description : ${script.seo.description} _(${script.seo.description.length} car.)_`,
    `- Mots-clés : ${script.seo.mots_cles.join(', ')}`,
    `- YouTube : ${script.seo.youtube_titre} _(${script.seo.youtube_titre.length} car.)_`,
    '',
  ];
  writeFileSync(join(dossier, 'script.md'), lignes.join('\n'), 'utf8');
};
