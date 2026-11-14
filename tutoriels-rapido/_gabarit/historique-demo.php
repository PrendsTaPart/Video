<?php
// Historique FICTIF pour filmer CRM38 (copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// Donne aux devis de démo une date de début (création) et une date de fin (validité 30 jours).
// Usage : php historique-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$n = $db->exec("update devis set date_debut = date(created_at), date_fin = date(created_at, '+30 days') where date_debut is null");
echo "devis datés : $n\n";
