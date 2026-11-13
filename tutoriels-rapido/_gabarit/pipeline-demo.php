<?php
// Pipeline FICTIF pour filmer CRM07 (base SQLite de la copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// Le bouton « créer » du pipeline ne fonctionne pas dans RapidoCRM (élément #pipelineError absent de la page) :
// on crée donc le pipeline comme le ferait PipelineController::store (mêmes 8 étapes par défaut).
// Usage : php pipeline-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$now = date('Y-m-d H:i:s');
foreach ($db->query("select id from pipelines where nom = 'Prospection boulangeries'")->fetchAll(PDO::FETCH_COLUMN) as $old) {
    $db->exec("delete from pipeline_historique where pipeline_prospect_id in (select id from pipeline_prospects where pipeline_id = $old)");
    $db->exec("delete from pipeline_prospects where pipeline_id = $old");
    $db->exec("delete from pipeline_etapes where pipeline_id = $old");
    $db->exec("delete from pipelines where id = $old");
}
$db->prepare('insert into pipelines (company_id, nom, description, est_defaut, actif, ordre, created_at, updated_at) values (1, ?, ?, 1, 1, 1, ?, ?)')
    ->execute(['Prospection boulangeries', 'Boulangeries et pâtisseries de Bordeaux', $now, $now]);
$pid = (int) $db->lastInsertId();
$etapes = [
    ['Nouveau Prospect', '#6C757D', 10, 'normal'], ['Qualification', '#007BFF', 20, 'normal'], ['Contact établi', '#17A2B8', 40, 'normal'],
    ['Envoi de proposition', '#FFC107', 60, 'normal'], ['Négociation', '#FD7E14', 75, 'normal'], ['Décision en attente', '#6F42C1', 85, 'normal'],
    ['Fermé - Gagné', '#28A745', 100, 'gagne'], ['Fermé - Perdu', '#DC3545', 0, 'perdu'],
];
$ids = [];
foreach ($etapes as $i => [$nom, $couleur, $proba, $type]) {
    $db->prepare('insert into pipeline_etapes (pipeline_id, nom, couleur, probabilite, type, actif, ordre, created_at, updated_at) values (?, ?, ?, ?, ?, 1, ?, ?, ?)')
        ->execute([$pid, $nom, $couleur, $proba, $type, $i + 1, $now, $now]);
    $ids[] = (int) $db->lastInsertId();
}
$entreprises = $db->query('select id, nom from entreprises where company_id = 1 and deleted_at is null order by id limit 9')->fetchAll(PDO::FETCH_ASSOC);
$repartition = [0, 0, 1, 1, 2, 3, 4, 5, 6];
$montants = [1800, 2400, 950, 3200, 1500, 4100, 2700, 1200, 3600];
foreach ($entreprises as $k => $e) {
    $et = $ids[$repartition[$k] ?? 0];
    $db->prepare('insert into pipeline_prospects (pipeline_id, etape_id, company_id, prospect_type, prospect_id, titre, montant, devise, probabilite, actif, entree_etape_at, created_at, updated_at) values (?, ?, 1, ?, ?, ?, ?, ?, ?, 1, ?, ?, ?)')
        ->execute([$pid, $et, 'App\\Models\\Entreprise', $e['id'], $e['nom'] . ' — offre fidélité', $montants[$k], 'EUR', $etapes[$repartition[$k] ?? 0][2], $now, $now, $now]);
}
echo "Pipeline de démo créé (#$pid, " . count($entreprises) . " prospects)\n";
