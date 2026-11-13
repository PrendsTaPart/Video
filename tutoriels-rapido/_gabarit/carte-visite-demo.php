<?php
// Modèles de carte de visite FICTIFS (Studio Lumière) pour filmer CRM30
// (copie de tournage /home/user/rapido-crm-film, jamais le dépôt). Usage : php carte-visite-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->exec("delete from mes_templates_crm where user_id = 1 and type = 'Carte de visite'");
$now = date('Y-m-d H:i:s');
$carte = fn ($fond, $accent, $texte) => '<div class="cv"><div class="logo">STUDIO<br><b>LUMIÈRE</b></div><div class="id"><h1>Léa Martin</h1><p class="role">Photographe · Fondatrice</p>'
    . '<p>06 12 34 56 78</p><p>lea@studio-lumiere.test</p><p>1 quai des Chartrons, Bordeaux</p></div></div>';
$css = fn ($fond, $accent, $texte) => ".cv{width:560px;height:320px;border-radius:22px;background:$fond;color:$texte;display:flex;align-items:center;gap:36px;padding:36px;box-sizing:border-box;font-family:Arial,sans-serif;box-shadow:0 18px 40px rgba(0,0,0,.18)}"
    . ".logo{width:130px;height:130px;border-radius:50%;background:$accent;color:#fff;display:flex;align-items:center;justify-content:center;text-align:center;font-size:12px;letter-spacing:1px;line-height:1.5}"
    . ".id h1{margin:0 0 4px;font-size:30px}.id .role{color:$accent;font-weight:bold;margin:0 0 14px}.id p{margin:4px 0;font-size:15px}";
foreach ([['Carte claire', '#FFFFFF', '#4CAF50', '#2B2B2B'], ['Carte nuit', '#1F2433', '#7E57C2', '#FFFFFF']] as [$nom, $f, $a, $t]) {
    $db->prepare("insert into mes_templates_crm (user_id, name, type, description, html, css, created_at, updated_at) values (1, ?, 'Carte de visite', 'Modèle de démo', ?, ?, ?, ?)")
        ->execute([$nom, json_encode($carte($f, $a, $t)), json_encode($css($f, $a, $t)), $now, $now]);
}
echo "Cartes de visite de démo prêtes\n";
