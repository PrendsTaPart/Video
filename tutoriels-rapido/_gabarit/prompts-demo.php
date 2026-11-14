<?php
// Prompts FICTIFS pour filmer CRM40 (copie de tournage /home/user/rapido-crm-film, jamais le dépôt) :
// remet « mes prompts » du compte de démo à deux modèles personnels.
// Usage : php prompts-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->exec("delete from mes_prompts_crm where user_id = 1");
$j = fn ($n) => date('Y-m-d H:i:s', strtotime("-$n days 10:00"));
foreach ([['Invitation portes ouvertes', "Rédige une invitation chaleureuse aux portes ouvertes du [date] pour [nom du client], avec le programme et un lien d'inscription.", 6],
          ['SMS rappel de rendez-vous', "Rédige un SMS de 160 caractères pour rappeler à [nom du client] son rendez-vous du [date] à [heure].", 2]] as [$t, $p, $a]) {
    $db->prepare("insert into mes_prompts_crm (user_id, type, titre, prompt, created_at, updated_at) values (1, 'text', ?, ?, ?, ?)")->execute([$t, $p, $j($a), $j($a)]);
}
// Crédit IA du compte de démo (sinon : « Désolé vous n'avez plus de crédit »)
$db->exec("delete from credit_user_crm where user_id = 1");
$db->prepare("insert into credit_user_crm (user_id, credit, date_expiration, created_at, updated_at) values (1, 5, ?, ?, ?)")->execute([date('Y-m-d H:i:s', strtotime('+1 year')), $j(0), $j(0)]);
echo "mes prompts : " . $db->query("select count(*) from mes_prompts_crm where user_id = 1")->fetchColumn() . "\n";
