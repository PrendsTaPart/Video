<?php
// Données de démonstration FICTIVES pour filmer RapidoCMS en local.
// Usage : php demo-cms.php /chemin/vers/rapido-cms/database/database.sqlite
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$now = date('Y-m-d H:i:s');
$ins = function (string $table, array $row) use ($db, $now) {
    $cols = array_column($db->query("pragma table_info($table)")->fetchAll(PDO::FETCH_ASSOC), 'name');
    $row += ['created_at' => $now, 'updated_at' => $now];
    $row = array_intersect_key($row, array_flip($cols));
    $st = $db->prepare("insert into $table (" . implode(',', array_keys($row)) . ') values (' . implode(',', array_fill(0, count($row), '?')) . ')');
    $st->execute(array_values($row));
    return (int) $db->lastInsertId();
};
$companyId = $ins('companies', ['nom' => 'Studio Lumière', 'siret' => '12345678900011', 'ville' => 'Bordeaux', 'adresse' => '1 quai des Chartrons', 'code_postal' => '33000', 'email' => 'contact@studio-lumiere.test', 'site_web' => 'https://studio-lumiere.test']);
$ins('users', ['nom' => 'Martin', 'prenom' => 'Léa', 'role' => 'admin', 'email' => 'demo@rapido.test', 'password' => password_hash('Demo-Rapido-2026', PASSWORD_BCRYPT), 'company_id' => $companyId, 'email_verified_at' => $now, 'fonction' => 'Gérante', 'disponible' => 1]);
$plan = $db->query('select * from abonnements_cms order by prix_mensuel desc limit 1')->fetch(PDO::FETCH_ASSOC) ?: ['id' => null, 'nom' => 'Premium', 'prix_mensuel' => 99];
$ins('abonnement_user_cms', ['entreprise_id' => $companyId, 'abonnement_id' => $plan['id'], 'nom' => $plan['nom'], 'type' => 'mensuel', 'prix' => $plan['prix_mensuel'],
    'stockage_go_disponible' => $plan['stockage_go_disponible'] ?? 10, 'carte_digitale' => $plan['carte_digitale'] ?? 10, 'comptes_reseaux' => $plan['comptes_reseaux'] ?? 10,
    'visuels' => $plan['visuels'] ?? 1, 'chatbot' => $plan['chatbot'] ?? 1, 'plannification' => $plan['plannification'] ?? 1, 'statistiques' => $plan['statistiques'] ?? 1,
    'requetes_ia' => $plan['requetes_ia'] ?? 100, 'is_legacy' => 1, 'date_expiration' => date('Y-m-d H:i:s', strtotime('+1 year'))]);
$ins('credit_user_cms', ['entreprise_id' => $companyId, 'credit' => 25, 'date_expiration' => date('Y-m-d H:i:s', strtotime('+1 year'))]);
echo "Données de démonstration RapidoCMS créées : company #$companyId, demo@rapido.test / Demo-Rapido-2026\n";
