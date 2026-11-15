// Données de démonstration (fictives) des tutoriels RHV2-07 à RHV2-10, créées par l'API du produit
// comme le ferait un utilisateur : poste ATS publié + une candidature, réunion de projet planifiée.
// Usage : node seed_v2_ui.cjs http://127.0.0.1:8000
const { chromium } = require('playwright');
const BASE = process.argv[2] || 'http://127.0.0.1:8000';
const pdf = (text) => {
  const stream = 'BT /F1 11 Tf 40 780 Td 14 TL\n' + text.split('\n').map((l) => `(${l.replace(/[()\\]/g, (c) => '\\' + c)}) Tj T*`).join('\n') + '\nET';
  const objs = ['<< /Type /Catalog /Pages 2 0 R >>', '<< /Type /Pages /Kids [3 0 R] /Count 1 >>',
    '<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>',
    `<< /Length ${Buffer.byteLength(stream, 'latin1')} >>\nstream\n${stream}\nendstream`, '<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>'];
  let out = '%PDF-1.4\n'; const off = [];
  objs.forEach((o, i) => { off.push(Buffer.byteLength(out, 'latin1')); out += `${i + 1} 0 obj\n${o}\nendobj\n`; });
  const x = Buffer.byteLength(out, 'latin1');
  out += `xref\n0 ${objs.length + 1}\n0000000000 65535 f \n` + off.map((o) => String(o).padStart(10, '0') + ' 00000 n \n').join('') + `trailer\n<< /Size ${objs.length + 1} /Root 1 0 R >>\nstartxref\n${x}\n%%EOF`;
  return Buffer.from(out, 'latin1');
};
(async () => {
  const b = await chromium.launch(); const p = await (await b.newContext()).newPage();
  await p.goto(BASE + '/login'); await p.fill('input[name=email]', 'camille@studio-demo.test'); await p.fill('input[name=password]', 'Demo-Tuto-2026!');
  await Promise.all([p.waitForNavigation(), p.click('button[type=submit]')]);
  await p.goto(BASE + '/dashboard'); await p.waitForTimeout(1500);
  const r = await p.evaluate(async () => {
    const ax = window.axios; const out = {};
    await ax.put('/api/ats/career-page', { slug: 'studio-demo', enabled: true, privacy_notice: 'Vos données servent uniquement à étudier votre candidature et sont supprimées après six mois. Vous pouvez demander leur suppression à tout moment.', retention_months: 6 });
    const job = (await ax.post('/api/ats/jobs', { title: 'Chargé de communication événementielle', location: 'Lyon', contract_type: 'CDI', summary: 'Préparer et animer la présence de Studio Démo sur les salons professionnels.', skills_required: ['Réseaux sociaux', 'Organisation'], skills_bonus: ['Photo'], criteria: [{ label: 'Organisation d\'événements', weight: 3 }, { label: 'Rédaction', weight: 2 }] })).data.job;
    await ax.post(`/api/ats/jobs/${job.id}/submit`); await ax.post(`/api/ats/jobs/${job.id}/publish`);
    out.job = job;
    const opts = (await ax.get('/api/meet/options')).data;
    const proj = opts.projects.find((x) => x.name.startsWith('Salon'));
    const rap = opts.agents.find((a) => a.slug === 'rapporteur');
    const plan = opts.agents.find((a) => a.slug === 'planificateur-editorial');
    const people = opts.humans.filter((h) => ['Hugo', 'Inès'].some((n) => h.name.startsWith(n))).map((h) => h.id);
    const s = new Date(); s.setDate(s.getDate() - 1); s.setHours(10, 0, 0, 0); const e = new Date(s.getTime() + 3600e3);
    const m = (await ax.post('/api/meet', { title: 'Point de lancement du salon', project_id: proj.id, template_key: 'lancement_projet', agenda: 'Objectifs · Périmètre · Rôles · Jalons · Risques',
      starts_at: s.toISOString(), ends_at: e.toISOString(), timezone: 'Europe/Paris', participants: people, agents: [{ user_id: rap.id, meeting_role: 'rapporteur' }, { user_id: plan.id, meeting_role: 'expert' }], creation_key: 'tuto-rhv2-07-' + Date.now() })).data;
    out.meeting = m.id;
    return out;
  });
  // Candidature déposée par la vraie page carrière publique.
  const job = r.job;
  await p.context().clearCookies();
  await p.goto(`${BASE}/carrieres/studio-demo/${job.slug}`); await p.waitForTimeout(800);
  await p.fill('input[name=first_name]', 'Léa'); await p.fill('input[name=last_name]', 'Fictive'); await p.fill('input[name=email]', 'lea.fictive@exemple.test');
  await p.setInputFiles('input[name=cv]', { name: 'cv-lea-fictive.pdf', mimeType: 'application/pdf', buffer: pdf("Léa Fictive\nlea.fictive@exemple.test\n5 ans d'expérience en organisation d'événements\nRéseaux sociaux, organisation, photo\nLangues : français, anglais\nSalons professionnels à Lyon et Paris") });
  await p.check('input[name=consent]').catch(() => {});
  await Promise.all([p.waitForLoadState('networkidle'), p.click('button[type=submit]')]);
  console.log(JSON.stringify({ job: job.id, slug: job.slug, meeting: r.meeting, after: p.url() }));
  await b.close();
})().catch((e) => { console.error(e.response?.data || e); process.exit(1); });
