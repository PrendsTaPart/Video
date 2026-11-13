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
http.createServer((req, res) => {
    let body = '';
    req.on('data', (c) => (body += c));
    req.on('end', () => {
        let p = {};
        try { p = JSON.parse(body || '{}'); } catch (e) { /* ignore */ }
        const out = { resultats: fake(p.speciality || p.secteur || p.query, p.city || p.ville) };
        setTimeout(() => { res.writeHead(200, { 'content-type': 'application/json' }); res.end(JSON.stringify(out)); }, 1600);
    });
}).listen(port, '127.0.0.1', () => console.log('mock n8n sur', port));
