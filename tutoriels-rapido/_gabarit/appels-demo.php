<?php
// Appels FICTIFS de l'agent vocal pour filmer CRM09 (copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// Usage : php appels-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->exec("delete from agent_vocal_appels where conversation_id like 'demo-%'");
$ents = $db->query('select id, nom from entreprises where company_id = 1 and deleted_at is null order by id limit 6')->fetchAll(PDO::FETCH_ASSOC);
$cfg = $db->query('select id from agent_vocal_configs order by id desc limit 1')->fetchColumn() ?: null;
$t = fn ($m, $r, $s) => ['role' => $r, 'message' => $m, 'time_in_call_secs' => $s];
$appels = [
    ['sortant', 'termine', 'rdv_pris', 214, "Intéressée par une séance photo d'équipe pour son site. Rendez-vous fixé jeudi à 10 h.", [
        $t("Bonjour, ici l'assistant de Studio Lumière. Je vous appelle au sujet des portraits d'équipe pour votre site, auriez-vous deux minutes ?", 'agent', 2),
        $t("Oui, justement, on refait notre site en ce moment.", 'user', 9),
        $t("Parfait ! Nous proposons une séance sur place d'une heure, avec quinze photos retouchées. Voulez-vous fixer un rendez-vous pour en parler ?", 'agent', 14),
        $t("Jeudi matin, ce serait possible ?", 'user', 27),
        $t("Jeudi à 10 h, c'est noté. Vous recevrez une confirmation par SMS. Belle journée !", 'agent', 31),
    ]],
    ['sortant', 'termine', 'interesse', 156, "Intéressé, souhaite recevoir les tarifs par e-mail avant de décider.", [
        $t("Bonjour, ici l'assistant de Studio Lumière, je vous appelle pour nos séances photo professionnelles.", 'agent', 2),
        $t("Envoyez-moi vos tarifs par mail, je regarderai.", 'user', 11),
        $t("Bien sûr, je vous les envoie aujourd'hui. Merci pour votre temps !", 'agent', 16),
    ]],
    ['sortant', 'termine', 'a_rappeler', 48, "Gérant absent. Rappeler mardi après 14 h.", []],
    ['entrant', 'termine', 'rdv_pris', 187, "Appel entrant : demande de séance photo famille. Rendez-vous pris samedi à 15 h.", []],
    ['sortant', 'termine', 'pas_interesse', 62, "Travaille déjà avec un photographe. Ne pas relancer avant six mois.", []],
    ['sortant', 'echec', 'a_rappeler', 0, 'Pas de réponse : messagerie.', []],
];
$now = time();
foreach ($appels as $i => [$dir, $statut, $res, $duree, $resume, $tr]) {
    $e = $ents[$i % max(1, count($ents))] ?? ['id' => null];
    $quand = date('Y-m-d H:i:s', $now - ($i + 1) * 5400);
    $db->prepare('insert into agent_vocal_appels (company_id, user_id, entreprise_id, config_id, conversation_id, telephone, statut, duree_secondes, cout_credits, resume_ia, resultat, ended_at, created_at, updated_at, transcript_json, direction) values (1, 1, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
        ->execute([$e['id'], $cfg, 'demo-' . ($i + 1), '05 56 00 1' . $i . ' 4' . $i, $statut, $duree, round($duree / 60, 2), $resume, $res, $quand, $quand, $quand, $tr ? json_encode($tr, JSON_UNESCAPED_UNICODE) : null, $dir]);
}
echo count($appels) . " appels de démo créés\n";
