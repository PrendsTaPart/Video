<?php
// Tunnel de vente FICTIF pour filmer CRM57 : créé comme le ferait Claude avec l'outil MCP creer_tunnel_de_vente
// (même service, TunnelVenteService). Copie de tournage uniquement. Rejouable : supprime d'abord le tunnel de démo.
// Usage : php artisan tinker puis require '/home/user/video/tutoriels-rapido/_gabarit/tunnel-demo.php';
$u = App\Models\User::where('email', 'demo@rapido.test')->first();
$cid = $u->company_id;
$nomProduit = 'Coaching sportif à domicile (démo)';
$siteIds = DB::table('sites')->where('company_id', $cid)->where('nom', 'Coach Bastien (démo)')->pluck('id');
DB::table('site_vues')->whereIn('site_id', $siteIds)->delete();
DB::table('site_pages')->whereIn('site_id', $siteIds)->delete();
DB::table('sites')->whereIn('id', $siteIds)->delete();
$seq = DB::table('sequences')->where('company_id', $cid)->where('nom', 'Tunnel — '.$nomProduit)->pluck('id');
DB::table('sequence_etapes')->whereIn('sequence_id', $seq)->delete();
DB::table('sequences')->whereIn('id', $seq)->delete();
DB::table('lead_magnets')->where('company_id', $cid)->where('titre', '5 séances à faire chez soi')->delete();
DB::table('offres')->where('company_id', $cid)->where('nom', $nomProduit)->delete();

$r = app(App\Services\TunnelVenteService::class)->creer($cid, $u->id, [
    'nom_site' => 'Coach Bastien (démo)', 'marque' => 'Coach Bastien', 'couleur' => '#ef6c00',
    'produit' => ['nom' => $nomProduit, 'description' => 'Huit séances avec un coach, chez vous, en un mois.', 'prix_ttc' => 49],
    'lead_magnet' => ['titre' => '5 séances à faire chez soi', 'type' => 'guide', 'promesse' => 'Cinq séances de 20 minutes, sans matériel.',
        'benefices' => ['Des séances courtes', 'Sans matériel', 'Pour tous les niveaux']],
    'emails' => [
        ['delai_jours' => 1, 'objet' => 'Votre première séance', 'message' => "Bonjour [\$prenom-\$],\n\nAvez-vous testé la première séance du guide ?"],
        ['delai_jours' => 3, 'objet' => 'Trois erreurs à éviter', 'message' => "Bonjour [\$prenom-\$],\n\nVoici trois erreurs fréquentes quand on s'entraîne seul."],
        ['delai_jours' => 5, 'objet' => 'Passer à la vitesse supérieure', 'message' => "Bonjour [\$prenom-\$],\n\nEnvie d'un coach à vos côtés ? {lien_vente}"],
    ],
    'page_vente' => ['titre' => 'Un coach chez vous, pendant un mois', 'sous_titre' => 'Huit séances adaptées à votre niveau.', 'bouton' => 'Je réserve mon mois',
        'avantages' => [['titre' => 'À domicile', 'texte' => 'Pas de salle, pas de trajet.'], ['titre' => 'Sur mesure', 'texte' => 'Un programme selon votre niveau.'], ['titre' => 'Suivi', 'texte' => 'Un bilan à la fin du mois.']]],
]);
echo 'tunnel de démo : '.json_encode(array_keys($r), JSON_UNESCAPED_UNICODE)."\n";
