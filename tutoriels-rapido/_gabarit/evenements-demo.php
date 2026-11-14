<?php
// Événements FICTIFS pour filmer CRM32 (copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// Trois événements (deux actifs, un passé), créneaux et rendez-vous réservés par des entreprises de démo (@exemple.test).
// Usage : php evenements-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$now = date('Y-m-d H:i:s');
$db->exec("delete from event_schedule_bookings where event_schedule_id in (select s.id from event_schedules s join events e on e.id = s.event_id where e.user_id in (select id from users where company_id = 1))");
$db->exec("delete from event_schedules where event_id in (select id from events where user_id in (select id from users where company_id = 1))");
$db->exec("delete from events where user_id in (select id from users where company_id = 1)");
// identifiants stables pour le tournage (1, 2, 3) quand il ne reste aucun événement
foreach (['events', 'event_schedules', 'event_schedule_bookings'] as $t) {
    if (! $db->query("select count(*) from $t")->fetchColumn()) {
        $db->exec("delete from sqlite_sequence where name = '$t'");
    }
}
$evenements = [
    // nom, début (jours), fin (jours), durée, type, statut, couleur, adresse / lien, user
    ['Démonstration RapidoCRM', 2, 16, '30 min', 'Visioconférence', 1, '#4CAF50', 'https://meet.exemple.test/demo-rapido', 1],
    ['Portes ouvertes de l\'atelier', 5, 6, '1 heure', 'Présentiel', 1, '#7E57C2', '12 quai des Chartrons, Bordeaux', 2],
    ['Atelier fidélité commerçants', -20, -18, '2 heures', 'Présentiel', 0, '#FF9800', '3 place Pey-Berland, Bordeaux', 1],
];
$entreprises = $db->query("select id, nom from entreprises where company_id = 1 order by id limit 8")->fetchAll(PDO::FETCH_ASSOC);
$slug = fn ($s) => trim(preg_replace('/[^a-z0-9]+/', '', strtolower(iconv('UTF-8', 'ASCII//TRANSLIT', $s))));
$k = 0;
foreach ($evenements as $i => [$nom, $deb, $fin, $duree, $type, $statut, $couleur, $lieu, $user]) {
    $db->prepare("insert into events (user_id, nom, date_debut, date_fin, duree, type, statut, couleur, lien_meet, adresse, telephone, template_email_id, form_crm_id, created_at, updated_at)
        values (?, ?, date('now', ?), date('now', ?), ?, ?, ?, ?, ?, ?, '05 56 00 00 00', 1, 3, datetime('now', ?), ?)")
        ->execute([$user, $nom, "$deb days", "$fin days", $duree, $type, $statut, $couleur, $type === 'Visioconférence' ? $lieu : null, $type === 'Visioconférence' ? null : $lieu, '-' . (10 - $i) . ' days', $now]);
    $eid = $db->lastInsertId();
    foreach ([0, 1, 2] as $j) {
        foreach (['09:30', '11:00', '14:30', '16:00'] as $h) {
            $db->prepare("insert into event_schedules (event_id, jour, heure_debut, created_at, updated_at) values (?, date('now', ?), ?, ?, ?)")
                ->execute([$eid, ($deb + $j) . ' days', $h, $now, $now]);
            $sid = $db->lastInsertId();
            // quelques créneaux réservés
            if (($j + strlen($h) + $i) % 3 === 0 && $k < 12) {
                $e = $entreprises[$k % count($entreprises)]; $k++;
                // statuts réels : en_attente, realise, annule ; l'événement passé a ses rendez-vous réalisés
                $etat = $statut ? (['en_attente', 'en_attente', 'annule', 'en_attente'][$k % 4]) : 'realise';
                $db->prepare("insert into event_schedule_bookings (event_schedule_id, nom_entreprise, email_entreprise, commentaire, statut, entreprise_id, created_at, updated_at) values (?, ?, ?, ?, ?, ?, ?, ?)")
                    ->execute([$sid, $e['nom'], 'contact@' . $slug($e['nom']) . '.exemple.test', 'Intéressé par le programme de fidélité.', $etat, $e['id'], $now, $now]);
            }
        }
    }
}
echo "événements : " . $db->query("select count(*) from events where user_id in (select id from users where company_id = 1)")->fetchColumn()
   . ", réservations : " . $db->query("select count(*) from event_schedule_bookings")->fetchColumn() . "\n";
// Modèles d'e-mail de la catégorie « Événements » (l'assistant ne propose que ceux-là)
$db->exec("delete from template_emails where company_id = 1 and categorie = 'Événements'");
foreach ([['Invitation à un événement', "<p>Bonjour,</p><p>Nous serions ravis de vous accueillir. Choisissez votre créneau en un clic.</p>"],
          ['Confirmation de rendez-vous', "<p>Bonjour,</p><p>Votre rendez-vous est bien enregistré. À très bientôt !</p>"]] as [$nom, $html]) {
    $db->prepare("insert into template_emails (company_id, nom, contenu, categorie, created_at, updated_at) values (1, ?, ?, 'Événements', ?, ?)")->execute([$nom, $html, $now, $now]);
}
$tpl = $db->query("select id from template_emails where company_id = 1 and categorie = 'Événements' order by id limit 1")->fetchColumn();
$db->exec("update events set template_email_id = $tpl where user_id in (select id from users where company_id = 1)");
