<?php
// Aligne les domaines d'activité des clients FICTIFS sur la liste officielle de RapidoCRM
// (Technologie, Santé, Éducation, Finance, Commerce, Transport, Tourisme, Agriculture) :
// les données de prospection de démo portaient « Restauration » / « Boulangerie », absents
// de cette liste, et les campagnes ciblées par domaine touchaient 0 personne.
// Copie de tournage /home/user/rapido-crm-film uniquement. Usage : php domaines-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$n = $db->exec("update entreprises set domaine = 'Tourisme' where company_id = 1 and lower(nom) like '%hôtel%'");
$n += $db->exec("update entreprises set domaine = 'Commerce' where company_id = 1 and (domaine is null or domaine not in ('Technologie','Santé','Éducation','Finance','Commerce','Transport','Tourisme','Agriculture'))");
echo "$n client(s) réaligné(s) sur les domaines officiels\n";
