<?php
// Opportunités FICTIVES restées sans mouvement, pour filmer CRM45 (copie de tournage uniquement).
// À lancer après pipeline-demo.php : vieillit l'entrée en étape de trois opportunités.
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$pid = (int) $db->query("select id from pipelines where nom = 'Prospection boulangeries'")->fetchColumn();
$prospects = $db->query("select id from pipeline_prospects where pipeline_id = $pid order by id")->fetchAll(PDO::FETCH_COLUMN);
foreach ([1 => 21, 3 => 17, 5 => 26] as $rang => $jours) {
    if (! isset($prospects[$rang])) continue;
    $date = date('Y-m-d H:i:s', strtotime("-$jours days"));
    $db->prepare('update pipeline_prospects set entree_etape_at = ?, updated_at = ? where id = ?')->execute([$date, $date, $prospects[$rang]]);
}
$db->exec("update pipeline_etapes set jours_inactivite = null where pipeline_id = $pid");
echo "Opportunités inactives de démo prêtes\n";
