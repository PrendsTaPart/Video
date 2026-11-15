<?php
// Formulaires FICTIFS pour filmer CRM24, CRM46 et CRM47 (copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// - « Demande de devis site web » (type client, lien fixe /f/demo-devis-studio-lumiere) avec trois réponses passées ;
// - design par défaut (CRM46 le personnalise à l'écran) ;
// - retire « Demande de devis » créé pendant une prise précédente de CRM24.
// Usage : php formulaires-demo.php <database.sqlite>
date_default_timezone_set('Africa/Tunis'); // fuseau de config/app.php
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$slug = 'demo-devis-studio-lumiere';
$ids = $db->query("select id from forms_crm where user_id = 1 and (slug = '$slug' or nom = 'Demande de devis')")->fetchAll(PDO::FETCH_COLUMN);
foreach ($ids as $id) {
    $db->exec("delete from formulaire_reponses where form_id = $id");
    $db->exec("delete from clique_form_crm where form_id = $id");
    $db->exec("delete from forms_crm where id = $id");
}
$db->exec("delete from entreprises where email in ('bonjour@lepetitzinc.exemple.test', 'contact@floralies.exemple.test', 'hello@velocite.exemple.test', 'contact@cafedesarts.exemple.test')");
$il = fn ($j) => date('Y-m-d H:i:s', strtotime("-$j days 10:15"));
$champs = serialize(['nom', 'email', 'telephone', 'domaine', 'description']);
$db->prepare("insert into forms_crm (user_id, company_id, entreprise_id, nom, slug, vue, click, type, lien, champs, design, created_at, updated_at) values (1, 1, null, 'Demande de devis site web', ?, 37, 3, 'client', ?, ?, null, ?, ?)")
    ->execute([$slug, 'http://127.0.0.1:8124/f/' . $slug, $champs, $il(12), $il(12)]);
$formId = $db->lastInsertId();
// Option « design » (CRM47) : le design personnalisé dans CRM46, assorti au site fictif
if (($argv[2] ?? '') === 'design') {
    $design = ['titre' => 'Parlons de votre projet', 'sous_titre' => 'Devis gratuit, réponse sous 24 h.', 'couleur_principale' => '#7e57c2',
        'couleur_fond' => '#ffffff', 'couleur_texte' => '#1f2937', 'police' => 'Poppins', 'arrondi' => 16, 'texte_bouton' => 'Recevoir mon devis',
        'message_merci' => 'Merci ! Nous revenons vers vous sous 24 h.', 'afficher_logo' => false, 'url_redirection' => ''];
    $db->prepare("update forms_crm set design = ? where id = ?")->execute([json_encode($design, JSON_UNESCAPED_UNICODE), $formId]);
}
$reponses = [
    ['Le Petit Zinc', 'bonjour@lepetitzinc.exemple.test', '05 56 12 34 56', 'Restauration', 'Site avec menu et réservation en ligne.', 9, 'iframe'],
    ['Les Floralies', 'contact@floralies.exemple.test', '05 56 98 76 54', 'Fleuriste', 'Boutique en ligne pour les bouquets.', 5, 'page'],
    ['Vélocité', 'hello@velocite.exemple.test', '06 11 22 33 44', 'Réparation de vélos', 'Prise de rendez-vous en ligne.', 2, 'iframe'],
];
foreach ($reponses as [$nom, $email, $tel, $domaine, $desc, $j, $origine]) {
    $db->prepare("insert into entreprises (user_id, company_id, nom, email, telephone, domaine, description, created_at, updated_at) values (1, 1, ?, ?, ?, ?, ?, ?, ?)")
        ->execute([$nom, $email, $tel, $domaine, $desc, $il($j), $il($j)]);
    $entId = $db->lastInsertId();
    $donnees = json_encode(['nom' => $nom, 'email' => $email, 'telephone' => $tel, 'domaine' => $domaine, 'description' => $desc], JSON_UNESCAPED_UNICODE);
    $db->prepare("insert into formulaire_reponses (company_id, form_id, donnees, entreprise_id, origine, doublon, created_at, updated_at) values (1, ?, ?, ?, ?, 0, ?, ?)")
        ->execute([$formId, $donnees, $entId, $origine, $il($j), $il($j)]);
}
$db->exec("delete from notifications where user_id = 1 and contenu like 'Nouvelle réponse au formulaire%'");
// Adresse de la page Design, lue par la scène « goto_file » de CRM47 (épisode et essai à blanc)
foreach (['/home/user/video/tutoriels-rapido/CRM47', '/tmp/claude-0/CRM47-test'] as $dossier) {
    if (is_dir($dossier)) {
        file_put_contents("$dossier/lien-design.txt", "/formulaires/$formId/design");
        file_put_contents("$dossier/lien-reponses.txt", "/formulaires/$formId/reponses");
    }
}
echo "formulaire $formId : 3 réponses\n";
