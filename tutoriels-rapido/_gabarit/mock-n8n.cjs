// Remplaçant LOCAL des webhooks n8n de RapidoCRM, pour filmer la prospection avec des données FICTIVES.
// Usage : node mock-n8n.cjs 8199   puis dans rapido-crm/.env (local, ignoré par git) :
//   N8N_MAPS_WEBHOOK=http://127.0.0.1:8199/maps
//   N8N_PROSPECT_WEBHOOK=http://127.0.0.1:8199/prospect
//   N8N_ENTREPRISE_WEBHOOK=http://127.0.0.1:8199/entreprise
const http = require('http');
const port = +(process.argv[2] || 8199);
const noms = ['Le Fournil Gourmand', 'Boulangerie des Capucins', 'Maison Dorée', 'Au Pain de Saint-Michel', 'La Mie des Chartrons',
    'Boulangerie du Jardin Public', 'L\'Épi Bordelais', 'Pains & Merveilles', 'Le Pétrin de Bacalan', 'Fournée Chartronnaise',
    'La Tradition du Pont', 'Douceurs de la Bastide'];
const rues = ['rue Sainte-Catherine', 'cours Victor Hugo', 'rue Notre-Dame', 'place du Marché', 'cours de l\'Intendance', 'quai Richelieu'];
const fake = (speciality, city) => noms.map((n, i) => ({
    nom: speciality && !/boulang/i.test(speciality) ? `${n.replace(/Boulangerie|Fournil|Pain[s]?|Mie|Pétrin|Fournée/, speciality)}` : n,
    adresse: `${12 + i * 7} ${rues[i % rues.length]}, 3300${i % 9} ${city || 'Bordeaux'}`,
    code_postal: `3300${i % 9}`,
    ville: city || 'Bordeaux',
    telephone: `05 56 00 ${String(10 + i).padStart(2, '0')} ${String(40 + i * 3).padStart(2, '0')}`,
    site_web: `https://exemple-${i + 1}.test`,
    domaine: speciality || 'Boulangerie',
    note: (4.2 + (i % 8) / 10).toFixed(1),
}));
// /entreprise : recherche par nom ou SIRET → une fiche légale (SIRET, NAF, dirigeant) ; /prospect : sociétés d'un secteur.
const siretDe = (i) => String(91234567800011 + i * 1010);
const legal = (r, i) => Object.assign({}, r, { siret: siretDe(i), code_naf: '10.71C', naf: '10.71C', dirigeant: ['Claire Martin', 'Hugo Bernard', 'Inès Moreau', 'Paul Laurent'][i % 4], effectif: ['3 à 5', '6 à 9', '10 à 19'][i % 3] });
http.createServer((req, res) => {
    let body = '';
    req.on('data', (c) => (body += c));
    req.on('end', () => {
        let p = {};
        try { p = JSON.parse(body || '{}'); } catch (e) { /* ignore */ }
        let resultats;
        if (req.url.startsWith('/entreprise')) {
            const base = fake('', 'Bordeaux').map(legal);
            const q = (p.nom || '').toLowerCase();
            const hit = base.find((r) => (p.siret && r.siret === p.siret) || (q && r.nom.toLowerCase().includes(q))) || legal(Object.assign(fake('', 'Bordeaux')[0], { nom: p.nom || 'Le Fournil Gourmand' }), 0);
            if (p.siret) hit.siret = p.siret;
            resultats = [hit];
        } else if (req.url.startsWith('/prospect')) {
            resultats = fake(p.specialite || '', 'Bordeaux').map(legal).slice(0, Math.min(+p.nombre || 8, 8));
        } else {
            resultats = fake(p.speciality || p.secteur || p.query, p.city || p.ville);
        }
        setTimeout(() => { res.writeHead(200, { 'content-type': 'application/json' }); res.end(JSON.stringify({ resultats })); }, 1600);
    });
}).listen(port, '127.0.0.1', () => console.log('mock n8n sur', port));
