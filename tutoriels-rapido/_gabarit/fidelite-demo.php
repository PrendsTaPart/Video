<?php
// Programme de fidélité FICTIF déjà actif (avec cartes clients) pour filmer CRM26
// (copie de tournage /home/user/rapido-crm-film, jamais le dépôt). Le second programme est créé à l'écran.
// Usage : php fidelite-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->exec('delete from cartes_fidelite where company_id = 1');
$db->exec('delete from programme_fidelites where company_id = 1');
$ent = $db->query("select id from entreprises where company_id = 1 and nom = 'Café Mériadeck'")->fetchColumn()
    ?: $db->query('select id from entreprises where company_id = 1 order by id limit 1')->fetchColumn();
$now = date('Y-m-d H:i:s', time() - 40 * 86400);
$db->prepare('insert into programme_fidelites (company_id, entreprise_id, images, couleurs, textes, conditions, created_at, updated_at) values (1, ?, ?, ?, ?, ?, ?, ?)')
    ->execute([$ent, '[]',
        json_encode(['fond' => '#FFFFFF', 'titre' => '#2E6B30', 'sous_titre' => '#474747', 'bouton_fond' => '#4CAF50', 'bouton_texte' => '#FFFFFF']),
        json_encode(['titre' => 'Votre 10e café est offert !', 'sous_titre' => 'Tapez votre numéro pour cumuler vos points', 'bouton' => 'Je cumule'], JSON_UNESCAPED_UNICODE),
        json_encode(['telephone' => true, 'email' => false]), $now, $now]);
$prog = $db->lastInsertId();
$clients = [['Camille Durand', 80, 1], ['Hugo Martin', 45, 0], ['Inès Lefebvre', 120, 2], ['Lucas Moreau', 30, 0], ['Chloé Garnier', 95, 1], ['Nathan Roux', 15, 0]];
foreach ($clients as $i => [$nom, $pts, $gains]) {
    $t = date('Y-m-d H:i:s', time() - (35 - $i * 5) * 86400);
    $db->prepare('insert into cartes_fidelite (company_id, nom_client, points, gains_offerts, actif, created_at, updated_at, programme_fidelite_id) values (1, ?, ?, ?, ?, ?, ?, ?)')
        ->execute([$nom, $pts, $gains, $i === 5 ? 0 : 1, $t, $t, $prog]);
}
file_put_contents(__DIR__ . '/../CRM26/lien-cartes.txt', "/fidelite/cartes?programme=$prog\n");
file_put_contents(__DIR__ . '/../CRM26/lien-tablette.txt', "/fidelite/consulter?entreprise=$ent\n");
echo "Programme de fidélité de démo prêt (#$prog)\n";
