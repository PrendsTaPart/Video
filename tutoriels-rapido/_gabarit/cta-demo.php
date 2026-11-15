<?php
// CTA FICTIFS pour filmer CRM48 et CRM49 (copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// - retire « Offre de rentrée » créé pendant une prise précédente de CRM48 ;
// - « Prendre rendez-vous » : encart glissant avec test A/B et 30 jours de vues / clics / fermetures réalistes
//   (version B gagnante), sur plusieurs pages, sources et appareils.
// Usage : php cta-demo.php <database.sqlite>
date_default_timezone_set('Africa/Tunis'); // fuseau de config/app.php
mt_srand(2026);
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
foreach ($db->query("select id from cta_crm where company_id = 1 and nom = 'Offre de rentrée'")->fetchAll(PDO::FETCH_COLUMN) as $id) {
    $db->exec("delete from cta_evenements where cta_id = $id");
    $db->exec("delete from cta_crm where id = $id");
}
$id = $db->query("select id from cta_crm where company_id = 1 and nom = 'Prendre rendez-vous'")->fetchColumn();
$design = ['titre' => 'Un projet de site ?', 'texte' => 'Parlons-en 15 minutes, sans engagement.', 'texte_bouton' => 'Prendre rendez-vous',
    'couleur_bouton' => '#4caf50', 'couleur_texte_bouton' => '#ffffff', 'couleur_fond' => '#ffffff', 'couleur_texte' => '#1f2937', 'position' => 'bas_droite', 'arrondi' => 12];
$regles = ['declencheur' => 'defilement', 'delai_secondes' => 5, 'defilement_pourcent' => 40, 'frequence' => 'jours', 'frequence_jours' => 7,
    'appareils' => 'tous', 'urls_incluses' => '', 'urls_exclues' => "/merci\n/mentions-legales", 'date_debut' => null, 'date_fin' => null];
$b = ['active' => true, 'texte' => '', 'texte_bouton' => 'Réserver mon créneau', 'couleur_bouton' => '#7e57c2'];
$db->prepare("update cta_crm set format = 'slide_in', actif = 1, design = ?, regles = ?, variante_b = ? where id = ?")
    ->execute([json_encode($design, JSON_UNESCAPED_UNICODE), json_encode($regles, JSON_UNESCAPED_UNICODE), json_encode($b, JSON_UNESCAPED_UNICODE), $id]);
$db->exec("delete from cta_evenements where cta_id = $id");
$pages = ['https://studio-lumiere.exemple.test/tarifs' => 40, 'https://studio-lumiere.exemple.test/' => 30, 'https://studio-lumiere.exemple.test/realisations' => 20, 'https://studio-lumiere.exemple.test/blog/site-restaurant' => 10];
$sources = ['Google' => 45, 'direct' => 25, 'Instagram' => 15, 'Facebook' => 10, 'LinkedIn' => 5];
$appareils = ['mobile' => 58, 'ordinateur' => 36, 'tablette' => 6];
$tirer = function (array $poids) { $t = mt_rand(1, array_sum($poids)); foreach ($poids as $k => $p) { if (($t -= $p) <= 0) { return $k; } } return array_key_first($poids); };
$ins = $db->prepare("insert into cta_evenements (company_id, cta_id, type, variante, page_url, source, appareil, visiteur, created_at, updated_at) values (1, ?, ?, ?, ?, ?, ?, ?, ?, ?)");
$vues = 0; $clics = 0;
$db->beginTransaction();
for ($j = 29; $j >= 0; $j--) {
    $n = 9 + (int) round(6 * sin($j / 3)) + mt_rand(0, 6) + (29 - $j) / 6;
    for ($i = 0; $i < $n; $i++) {
        $v = mt_rand(0, 1) ? 'a' : 'b';
        $quand = date('Y-m-d H:i:s', strtotime("-$j days " . mt_rand(8, 21) . ':' . str_pad((string) mt_rand(0, 59), 2, '0', STR_PAD_LEFT)));
        $vid = 'demo' . $j . '_' . $i;
        $page = $tirer($pages); $source = $tirer($sources); $app = $tirer($appareils);
        $ins->execute([$id, 'vue', $v, $page, $source, $app, $vid, $quand, $quand]); $vues++;
        $tauxClic = ($v === 'b' ? 0.21 : 0.12) + ($page === 'https://studio-lumiere.exemple.test/tarifs' ? 0.06 : 0);
        if (mt_rand(0, 999) / 1000 < $tauxClic) { $ins->execute([$id, 'clic', $v, $page, $source, $app, $vid, $quand, $quand]); $clics++; }
        elseif (mt_rand(0, 9) < 3) { $ins->execute([$id, 'fermeture', $v, $page, $source, $app, $vid, $quand, $quand]); }
    }
}
$db->commit();
$db->prepare("update cta_crm set vue = ?, click = ? where id = ?")->execute([$vues, $clics, $id]);
echo "CTA $id : $vues vues, $clics clics\n";
