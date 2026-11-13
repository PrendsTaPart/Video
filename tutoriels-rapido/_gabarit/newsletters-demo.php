<?php
// Modèles de newsletter FICTIFS pour filmer CRM19 (copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// Usage : php newsletters-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$now = date('Y-m-d H:i:s');
$bloc = fn ($couleur, $titre, $intro, $points, $cta) => '<div style="font-family:Arial,sans-serif;max-width:600px;margin:auto;background:#ffffff;border-radius:12px;overflow:hidden">'
    . '<div style="background:' . $couleur . ';color:#fff;padding:28px 24px"><p style="margin:0;font-size:12px;letter-spacing:2px">STUDIO LUMIÈRE · BORDEAUX</p><h1 style="margin:8px 0 0;font-size:26px">' . $titre . '</h1></div>'
    . '<div style="padding:24px;color:#333;font-size:15px;line-height:1.6"><p>' . $intro . '</p><ul>' . implode('', array_map(fn ($p) => '<li>' . $p . '</li>', $points)) . '</ul>'
    . '<p style="text-align:center;margin-top:24px"><a style="background:' . $couleur . ';color:#fff;padding:12px 22px;border-radius:24px;text-decoration:none">' . $cta . '</a></p></div>'
    . '<div style="background:#f3f4f7;color:#888;font-size:11px;padding:14px;text-align:center">Studio Lumière — 1 quai des Chartrons, Bordeaux · Se désinscrire</div></div>';
$modeles = [
    ['Les nouveautés du mois', $bloc('#4CAF50', 'Les nouveautés de novembre', 'Ce mois-ci au studio :', ['Nouveau fond lumineux pour les portraits d\'équipe', 'Séances photo culinaires pour les restaurants', 'Livraison des images en 7 jours au lieu de 10'], 'Réserver une séance')],
    ['Offre de fin d\'année', $bloc('#7E57C2', '-15 % jusqu\'au 20 décembre', 'Pour finir l\'année en beauté, profitez de -15 % sur :', ['Les portraits d\'équipe', 'Les photos produits', 'Les reportages d\'événements'], 'J\'en profite')],
    ['Invitation portes ouvertes', $bloc('#03A9F5', 'Portes ouvertes le 16 novembre', 'Venez découvrir le studio de 17 h à 20 h :', ['Démonstrations d\'éclairage', 'Portrait offert à chaque visiteur', 'Verre de l\'amitié'], 'Je m\'inscris')],
];
foreach ($modeles as [$nom, $html]) {
    $db->prepare('delete from template_newsletters where company_id = 1 and nom = ?')->execute([$nom]);
    $db->prepare('insert into template_newsletters (company_id, nom, contenu, created_at, updated_at) values (1, ?, ?, ?, ?)')->execute([$nom, $html, $now, $now]);
}
// Les newsletters de démo déjà envoyées portaient « Démo » pour seul contenu.
$db->prepare("update campagne_newsletter set contenu = ? where company_id = 1 and contenu = 'Démo'")->execute([$modeles[0][1]]);
echo "Newsletters de démo prêtes\n";
// La liste de la campagne newsletter lit « Mes templates » (mes_templates_crm, type newsletter),
// html/css encodés en JSON : on y range les mêmes modèles, avec une vignette locale.
$dossier = '/home/user/rapido-crm-film/public/assets/img/demo';
@mkdir($dossier, 0777, true);
foreach ($modeles as $i => [$nom, $html]) {
    $db->prepare("delete from mes_templates_crm where user_id = 1 and type = 'newsletter' and name = ?")->execute([$nom]);
    $vignette = "/assets/img/demo/newsletter-" . ($i + 1) . ".png";
    file_put_contents("$dossier/newsletter-" . ($i + 1) . ".html", '<html><body style="margin:0;background:#eef0f4;padding:24px">' . $html . '</body></html>');
    $db->prepare("insert into mes_templates_crm (user_id, name, type, description, html, css, image, created_at, updated_at) values (1, ?, 'newsletter', ?, ?, ?, ?, ?, ?)")
        ->execute([$nom, 'Modèle de démo', json_encode($html), json_encode('body{background:#eef0f4;padding:24px}'), $vignette, $now, $now]);
}
echo "Mes templates newsletter prêts\n";
