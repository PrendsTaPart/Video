#!/usr/bin/env -S npx tsx
import { copyFileSync, existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
import { Command } from 'commander';
import { DemandeEnAttente, demandesEnAttente } from '../mcp/pont.ts';
import { analyser } from '../pipeline/analyse.ts';
import { construireFiche } from '../pipeline/fiche.ts';
import { construireScript } from '../pipeline/script.ts';
import { genererVoix } from '../pipeline/voix.ts';
import { copierAssetsPartages, rendre, type Format } from '../pipeline/rendu.ts';
import { assurerLogos, cheminLogo, installerLogoComplet, LOGOS, type NomLogo } from '../brand/logos.ts';
import { ECRANS, ecranPour } from '../brand/ecrans.ts';
import { genererVignettes, vignettesEnLot } from '../pipeline/vignette.ts';
import { publierRapidoCms } from '../pipeline/publier-rapidocms.ts';
import { publierYoutube } from '../pipeline/publier-youtube.ts';
import { publierSite } from '../pipeline/publier-site.ts';
import { controlerQualite, exigerQaVerte } from '../pipeline/qa.ts';
import { orchestrer, type NomEtape } from '../pipeline/orchestrer.ts';
import {
  construireFile,
  creditsConsommes,
  tableauDeBord,
  verifierCoherenceSerie,
} from '../pipeline/serie.ts';
import { regenerer, SEQUENCES, type NomSequence } from '../pipeline/regenerer.ts';
import {
  assurerDossier,
  dossierTutoriel,
  racineContenu,
  racineProjet,
  resoudreParModule,
} from '../util/chemins.ts';
import { avertir, erreur, info } from '../util/journal.ts';

const programme = new Command();
programme
  .name('rapidocrm-studio')
  .description('Chaîne de production des tutoriels vidéo de RapidoCRM Académie');

programme
  .command('analyse')
  .argument('<chemin>')
  .option('--force')
  .option('--accepter-longue', 'analyser un enregistrement de plus de 4 minutes')
  .action(async (chemin, o) => {
    await analyser(dossierTutoriel(chemin), { force: o.force, accepterLongue: o.accepterLongue });
  });

programme
  .command('fiche')
  .argument('<chemin>')
  .option('--force')
  .action(async (chemin, o) => {
    await construireFiche(dossierTutoriel(chemin), { force: o.force });
  });

programme
  .command('script')
  .argument('<chemin>')
  .option('--force')
  .action(async (chemin, o) => {
    await construireScript(dossierTutoriel(chemin), { force: o.force });
  });

programme
  .command('voix')
  .argument('<chemin>')
  .option('--force')
  .action(async (chemin, o) => {
    await genererVoix(dossierTutoriel(chemin), { force: o.force });
  });

programme
  .command('rendu')
  .argument('<chemin>')
  .option('--format <format>', '16x9 | 9x16 | tous', 'tous')
  .option('--preview', 'rendu 720p CRF 30 pour valider vite')
  .option('--force')
  .action(async (chemin, o) => {
    await rendre(dossierTutoriel(chemin), {
      format: o.format as Format,
      preview: o.preview,
      force: o.force,
    });
  });

programme
  .command('vignette')
  .argument('<chemin>')
  .action(async (chemin) => {
    await genererVignettes(dossierTutoriel(chemin));
  });

programme
  .command('vignettes-lot')
  .argument('<module>')
  .action(async (module) => {
    const base = join(racineContenu(), module);
    const dossiers = readdirSync(base)
      .map((d) => join(base, d))
      .filter((d) => existsSync(join(d, 'script.json')));
    await vignettesEnLot(dossiers);
  });

programme
  .command('publier-cms')
  .argument('<chemin>')
  .action(async (chemin) => {
    const dossier = dossierTutoriel(chemin);
    await exigerQaVerte(dossier);
    await publierRapidoCms(dossier);
  });

programme
  .command('publier-youtube')
  .argument('<chemin>')
  .action(async (chemin) => {
    const dossier = dossierTutoriel(chemin);
    await exigerQaVerte(dossier);
    await publierYoutube(dossier);
  });

programme
  .command('publier-site')
  .argument('<chemin>')
  .action(async (chemin) => {
    const dossier = dossierTutoriel(chemin);
    await exigerQaVerte(dossier);
    await publierSite(dossier);
  });

programme
  .command('qa')
  .argument('<chemin>')
  .action(async (chemin) => {
    const rapport = await controlerQualite(dossierTutoriel(chemin));
    if (!rapport.verte) process.exitCode = 1;
  });

programme
  .command('tuto')
  .argument('<module>')
  .argument('<numero>')
  .option('--from <etape>')
  .option('--to <etape>')
  .option('--dry-run', 'tout sauf les trois publications')
  .option('--force')
  .action(async (module, numero, o) => {
    const dossier = resoudreParModule(module, Number(numero));
    await orchestrer(dossier, {
      from: o.from as NomEtape | undefined,
      to: o.to as NomEtape | undefined,
      dryRun: o.dryRun,
      force: o.force,
    });
  });

programme
  .command('serie')
  .requiredOption('--module <module>')
  .option('--limite <n>', 'nombre maximum de tutoriels à traiter')
  .option('--auto-hook', 'prendre le premier hook proposé')
  .option('--auto-punchline', 'prendre la première punchline proposée')
  .action(async (o) => {
    const pivot = join(racineContenu(), o.module);
    const file = construireFile(pivot, o.module, o.limite ? Number(o.limite) : undefined);
    info(`  ${file.length} tutoriel(s) à produire dans ${o.module}`);

    let fait = 0;
    let credits = 0;
    const debut = Date.now();

    for (const element of file) {
      info('');
      info(`▸ ${element.module} V${String(element.numero).padStart(2, '0')} — manque : ${element.manquant.join(', ') || '(tout)'}`);
      try {
        await orchestrer(element.dossier, {
          autoHook: o.autoHook,
          autoPunchline: o.autoPunchline,
        });
        fait += 1;
        credits += creditsConsommes(element.dossier);
      } catch (e) {
        erreur(`${element.dossier} — ${(e as Error).message}`);
      }
      tableauDeBord({
        fait,
        enCours: 1,
        restant: file.length - fait,
        tempsMoyen: fait ? (Date.now() - debut) / 60000 / fait : 0,
        creditsElevenLabs: credits,
      });
    }

    info('  Cohérence de série');
    const incoherences = verifierCoherenceSerie(o.module);
    if (incoherences.length === 0) info('   ✓ rien à signaler');
    for (const i of incoherences) {
      if (i.gravite === 'alerte') avertir(i.message);
      else info(`   · ${i.message}`);
    }
  });

programme
  .command('regenerer')
  .requiredOption('--sequence <nom>', SEQUENCES.join(' | '))
  .requiredOption('--module <module>')
  .option('--republier', 'republier les nouveaux fichiers après le rendu')
  .action(async (o) => {
    if (!SEQUENCES.includes(o.sequence as NomSequence)) {
      throw new Error(`Séquence inconnue : ${o.sequence} (attendu : ${SEQUENCES.join(', ')})`);
    }
    await regenerer(o.module, o.sequence as NomSequence, { republier: o.republier });
  });

programme
  .command('preparer-assets')
  .description('Copie logos et images du présentateur dans public/ (avant Remotion Studio)')
  .action(async () => {
    const racinePublic = assurerDossier(join(racineProjet(), 'public'));
    await assurerLogos();
    for (const nom of Object.keys(LOGOS) as NomLogo[]) {
      const destination = join(assurerDossier(join(racinePublic, 'logos')), `${nom}.png`);
      if (!existsSync(destination)) copyFileSync(cheminLogo(nom), destination);
    }
    installerLogoComplet(racinePublic);
    copierAssetsPartages(racinePublic);
    info(`  Assets prêts dans ${racinePublic}`);
  });

programme
  .command('ecrans')
  .description('Liste la banque d\'écrans RapidoCRM et ce à quoi chacun se rattache')
  .option('--pour <titre>', 'montre l\'écran retenu pour un titre de tutoriel')
  .option('--module <module>', 'module du tutoriel, utilisé avec --pour', '')
  .action((o) => {
    if (o.pour) {
      for (const cadrage of ['capture', 'mockup'] as const) {
        const choix = ecranPour(o.module, o.pour, cadrage);
        info(`  ${cadrage.padEnd(8)} → ${choix ? `${choix.nom} — ${choix.titre}` : '(aucun)'}`);
      }
      return;
    }
    let module = '';
    for (const ecran of [...ECRANS].sort((a, b) => a.module.localeCompare(b.module))) {
      if (ecran.module !== module) {
        module = ecran.module;
        info(`\n  ${module}`);
      }
      info(`   · ${ecran.nom.padEnd(30)} ${ecran.cadrage.padEnd(8)} ${ecran.titre}`);
    }
    info('');
  });

programme
  .command('mcp-file')
  .description('Liste les demandes MCP en attente de réponse')
  .argument('<chemin>')
  .action((chemin) => {
    const attentes = demandesEnAttente(dossierTutoriel(chemin));
    if (attentes.length === 0) info('  Aucune demande MCP en attente.');
    for (const a of attentes) info(`  · ${a}`);
  });

programme.parseAsync(process.argv).catch((e) => {
  if (e instanceof DemandeEnAttente) {
    avertir(e.message);
    process.exitCode = 2;
    return;
  }
  erreur((e as Error).message);
  process.exitCode = 1;
});
