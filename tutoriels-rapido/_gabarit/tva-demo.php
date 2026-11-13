<?php
// Taux de TVA de démo pour filmer CRM11+ (copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// Usage : php tva-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$now = date('Y-m-d H:i:s');
foreach ([['TVA réduite', 5.5], ['TVA intermédiaire', 10], ['TVA normale', 20]] as $i => [$nom, $p]) {
    if ($db->query("select count(*) from tvas where company_id = 1 and nom = " . $db->quote($nom))->fetchColumn()) continue;
    $t = date('Y-m-d H:i:s', time() - (10 - $i));
    $db->prepare('insert into tvas (nom, pourcentage, company_id, created_at, updated_at) values (?, ?, 1, ?, ?)')->execute([$nom, $p, $t, $t]);
}
echo "TVA de démo prêtes\n";
