<?php
// Segments FICTIFS pour filmer CRM21 (copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// À lancer depuis la copie : php artisan tinker --execute="require '<ce fichier>';"
use App\Models\Segment;
$defs = [
    ['Commerçants bordelais', 'Commerces et restaurants de Bordeaux à relancer avant les fêtes.', 'actif', 'haute', '#4CAF50',
        ['operateur_global' => 'ET', 'groupes' => [['operateur' => 'ET', 'conditions' => [
            ['champ' => 'ville', 'op' => 'contient', 'valeur' => 'bordeaux'],
            ['champ' => 'secteur_activite', 'op' => '=', 'valeur' => 'Commerce']]]]]],
    ['Hôtels et tourisme', 'Établissements touristiques : offre portraits d\'équipe.', 'actif', 'normale', '#03A9F5',
        ['operateur_global' => 'ET', 'groupes' => [['operateur' => 'ET', 'conditions' => [
            ['champ' => 'secteur_activite', 'op' => '=', 'valeur' => 'Tourisme']]]]]],
    ['Clients VIP', 'Liste fixe des meilleurs clients, choisis à la main.', 'statique', 'haute', '#7E57C2', null],
];
foreach ($defs as [$nom, $desc, $type, $prio, $couleur, $criteres]) {
    Segment::withTrashed()->where('company_id', 1)->where('nom', $nom)->forceDelete();
    $s = Segment::create(['company_id' => 1, 'nom' => $nom, 'description' => $desc, 'type' => $type, 'priorite' => $prio,
        'couleur' => $couleur, 'criteres' => $criteres, 'actif' => true, 'cree_par' => 1]);
    if ($criteres) { $s->recalculer(); }
}
echo "Segments de démo prêts\n";
