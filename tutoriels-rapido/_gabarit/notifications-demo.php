<?php
// Notifications FICTIVES pour filmer CRM41 (copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// Léa (id 1) : trois notifications non lues et une déjà lue, du type de celles que RapidoCRM envoie.
// Usage : php notifications-demo.php <database.sqlite>
date_default_timezone_set('Africa/Tunis'); // fuseau de config/app.php
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->exec("delete from notifications where user_id = 1");
$il = fn ($m) => date('Y-m-d H:i:s', strtotime("-$m minutes"));
$liste = [
    ["Le commercial Yanis Moreau a été ajouté à votre équipe.", 4320, true],
    ["Nouvelle tâche pour vous : « Préparer la démo Atelier Garonne » — échéance le 17/11/2026 à 10:00.", 1440, false],
    ["Le devis #5 a été signé.", 130, false],
    ["Lotus Lounge vient d'ouvrir le devis n°3.", 12, false],
];
foreach ($liste as [$texte, $min, $lue]) {
    $db->prepare("insert into notifications (user_id, contenu, readed_at, created_at, updated_at) values (1, ?, ?, ?, ?)")
        ->execute([$texte, $lue ? $il($min - 30) : null, $il($min), $il($min)]);
}
echo "notifications : " . $db->query("select count(*) from notifications where user_id = 1")->fetchColumn() . "\n";
