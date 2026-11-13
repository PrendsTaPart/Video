<?php
// Données de démonstration FICTIVES pour filmer RapidoCRM en local.
// Usage : php demo-crm.php /chemin/vers/rapido-crm/database/database.sqlite
// N'écrit que dans la base SQLite locale (ignorée par git) — aucun fichier du dépôt n'est modifié.
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$now = date('Y-m-d H:i:s');
$ins = function (string $table, array $row) use ($db, $now) {
    $row += ['created_at' => $now, 'updated_at' => $now];
    $cols = array_keys($row);
    $st = $db->prepare("insert into $table (" . implode(',', $cols) . ') values (' . implode(',', array_fill(0, count($cols), '?')) . ')');
    $st->execute(array_values($row));
    return (int) $db->lastInsertId();
};
$ago = fn (int $days) => date('Y-m-d H:i:s', strtotime("-$days days"));

$companyId = $ins('companies', ['nom' => 'Studio Lumière', 'siret' => '12345678900011', 'ville' => 'Bordeaux', 'email' => 'contact@studio-lumiere.test', 'telephone' => '05 00 00 00 00']);
$pwd = password_hash('Demo-Rapido-2026', PASSWORD_BCRYPT);
$admin = $ins('users', ['nom' => 'Martin', 'prenom' => 'Léa', 'role' => 'admin', 'email' => 'demo@rapido.test', 'password' => $pwd, 'company_id' => $companyId, 'disponible' => 1, 'email_verified_at' => $now, 'fonction' => 'Gérante']);
foreach ([['Bernard', 'Karim'], ['Petit', 'Sophie'], ['Roux', 'Yanis']] as [$n, $p]) {
    $ins('users', ['nom' => $n, 'prenom' => $p, 'role' => 'commercial', 'email' => strtolower($p) . '@studio-lumiere.test', 'password' => $pwd, 'company_id' => $companyId, 'disponible' => 1]);
}
// Abonnement Premium actif
$abo = $db->query("select id from abonnements_crm order by prix_mensuel desc limit 1")->fetchColumn();
if (!$abo) {
    $abo = $ins('abonnements_crm', ['nom' => 'Premium', 'prix_mensuel' => 99, 'prix_annuel' => 999]);
}
$ins('abonnement_user_crm', ['user_id' => $admin, 'abonnement_id' => $abo, 'date_expiration' => date('Y-m-d H:i:s', strtotime('+1 year'))]);

$clients = ['Maison Lafitte', 'Lotus Lounge', 'Clover Bistro', 'Petal & Plate', 'Fournil des Chartrons', 'Atelier Garonne', 'Café Mériadeck', 'Boulangerie Saint-Pierre', 'Le Comptoir Bleu', 'Pain & Co', 'Hôtel des Quais', 'Épicerie Victor'];
$ents = [];
foreach ($clients as $i => $nom) {
    $ents[] = $ins('entreprises', ['nom' => $nom, 'ville' => 'Bordeaux', 'domaine' => 'Restauration', 'email' => 'contact@' . preg_replace('/[^a-z]/', '', strtolower($nom)) . '.test', 'user_id' => $admin, 'company_id' => $companyId, 'created_at' => $ago(60 - $i * 4)]);
}
$prenoms = ['Camille', 'Hugo', 'Inès', 'Lucas', 'Manon', 'Nathan', 'Chloé', 'Théo', 'Jade', 'Louis', 'Emma', 'Arthur', 'Léna', 'Jules', 'Zoé', 'Adam', 'Alice', 'Noah', 'Rose', 'Paul', 'Nina', 'Tom', 'Lou', 'Sacha', 'Mia', 'Gabin', 'Anna', 'Malo'];
foreach ($prenoms as $i => $p) {
    $ins('contacts', ['prenom' => $p, 'nom' => 'Démo', 'email' => strtolower($p) . '@exemple.test', 'entreprise_id' => $ents[$i % count($ents)], 'company_id' => $companyId]);
}
foreach (['Site vitrine' => 1200, 'Maintenance mensuelle' => 49, 'Shooting photo' => 450, 'Carte NFC' => 25, 'Campagne réseaux' => 690] as $nom => $prix) {
    $ins('offres', ['nom' => $nom, 'prix_ht' => $prix, 'tva' => 20, 'user_id' => $admin, 'company_id' => $companyId]);
}
$money = fn (float $ht) => ['remise' => 0, 'total_ht' => $ht, 'total_tva' => round($ht * 0.2, 2), 'total_ttc' => round($ht * 1.2, 2)];
foreach ([2400, 1788, 980, 3600, 1250, 640, 2150, 1490] as $i => $ht) {
    $ins('devis', ['entreprise_id' => $ents[$i], 'user_id' => $admin, 'company_id' => $companyId, 'statut' => $i < 5 ? 1 : 0, 'created_at' => $ago(40 - $i * 4)] + $money($ht));
}
foreach ([2400, 1788, 3600, 1250, 980, 450, 690] as $i => $ht) {
    $ins('factures', ['entreprise_id' => $ents[$i], 'user_id' => $admin, 'company_id' => $companyId, 'statut' => $i < 5 ? 1 : 0, 'created_at' => $ago(30 - $i * 3)] + $money($ht));
}
foreach ([320, 89, 1450, 240] as $i => $ht) {
    $ins('depenses', ['entreprise_id' => $ents[$i], 'user_id' => $admin, 'company_id' => $companyId, 'statut' => 1] + array_diff_key($money($ht), ['remise' => 0]));
}
// Activité marketing des 7 derniers jours (courbes du tableau de bord)
for ($d = 6; $d >= 0; $d--) {
    for ($k = 0; $k < [14, 22, 18, 30, 26, 35, 41][6 - $d]; $k++) {
        $ins('emails', ['entreprise_id' => $ents[$k % 12], 'user_id' => $admin, 'destinataire' => 'client' . $k . '@exemple.test', 'sujet' => 'Votre offre automne', 'contenu' => 'Démo', 'created_at' => $ago($d)]);
    }
    for ($k = 0; $k < [6, 9, 5, 12, 10, 14, 17][6 - $d]; $k++) {
        $ins('sms', ['entreprise_id' => $ents[$k % 12], 'user_id' => $admin, 'numero' => '0600000000', 'message' => 'Démo', 'created_at' => $ago($d)]);
    }
    if ($d % 2 === 0) {
        $ins('campagne_newsletter', ['cible' => 'Clients fidèles', 'date_envoi' => $ago($d), 'contenu' => 'Démo', 'company_id' => $companyId, 'created_at' => $ago($d)]);
    }
}
foreach (['Démo RapidoCRM — Lotus Lounge', 'Point devis — Maison Lafitte', 'Signature — Clover Bistro', 'Shooting — Petal & Plate', 'Bilan trimestriel', 'Rendez-vous salon'] as $i => $t) {
    $ins('rendez_vous', ['titre' => $t, 'entreprise_id' => $ents[$i], 'date_debut' => date('Y-m-d H:i:s', strtotime('+' . ($i + 1) . ' days 10:00')), 'date_fin' => date('Y-m-d H:i:s', strtotime('+' . ($i + 1) . ' days 11:00')), 'type' => 'visio', 'mode_envoi' => 'email', 'user_id' => $admin]);
}
// Réglages fictifs de l'entreprise (évite la fenêtre d'accueil « à compléter ») — chiffrés comme le fait l'application :
// à lancer ensuite : php artisan tinker --execute='$c=App\Models\Company::find(1); foreach(["password"=>"demo-imap","stripe_secret"=>"sk_test_demo","sms_id"=>"demo-sms"] as $k=>$v){$c->$k=Illuminate\Support\Facades\Crypt::encryptString($v);} $c->saveQuietly();'
$db->exec("update companies set banque='Banque Démo', switch='DEMOFRPP', iban='FR7600000000000000000000000', host='imap.exemple.test', port=993, encryption='ssl', adresse='1 quai des Chartrons', code_postal='33000', site_web='https://studio-lumiere.test' where id=$companyId");
echo "Données de démonstration créées : company #$companyId, admin demo@rapido.test\n";
