<?php
// Données fictives pour CRM27 (jeux concours v2). Copie de tournage uniquement. Rejouable (php artisan tinker).
// Retire le jeu créé lors d'une prise précédente et prépare un jeu « Roue du printemps » avec des parties fictives,
// pour l'écran Résultats. Le tirage passe par JeuService::jouer() (le même que la page publique).
use App\Models\CompanyGame;
use App\Models\User;
use App\Services\JeuService;
use Illuminate\Support\Facades\DB;

$s = app(JeuService::class);
$auteur = User::where('email', 'demo@rapido.test')->firstOrFail();
foreach (CompanyGame::where('company_id', $auteur->company_id)->whereIn('name', ['Carte à gratter de Noël', 'Roue du printemps'])->get() as $j) {
    DB::table('jeu_participations')->where('game_id', $j->id)->delete();
    DB::table('jeu_vues')->where('game_id', $j->id)->delete();
    DB::table('game_components')->where('game_id', $j->id)->delete();
    $j->forceDelete();
}
mt_srand(27);
$jeu = $s->creer($auteur, ['name' => 'Roue du printemps', 'type_jeu' => 'roue']);
$noms = ['Camille Martin', 'Hugo Bernard', 'Léa Petit', 'Lucas Robert', 'Chloé Richard', 'Nathan Durand', 'Manon Moreau', 'Théo Laurent', 'Inès Simon', 'Jules Michel', 'Sarah Lefèvre', 'Adam Garcia'];
foreach ($noms as $i => $nom) {
    foreach (range(1, 3) as $v) {
        $s->compterVue($jeu, ['source' => ['qr', 'site', 'instagram'][$i % 3], 'appareil' => $i % 2 ? 'mobile' : 'ordinateur', 'visiteur' => 'v'.$i.$v]);
    }
    $email = strtolower(str_replace([' ', 'é', 'è', 'ï', 'ô'], ['.', 'e', 'e', 'i', 'o'], $nom)).'@exemple.test';
    $s->jouer($jeu, ['nom' => $nom, 'email' => $email, 'consentement' => '1'], ['source' => ['qr', 'site', 'instagram'][$i % 3], 'appareil' => $i % 2 ? 'mobile' : 'ordinateur']);
}
echo 'Jeux prêts : '.$jeu->fresh()->vues.' vues, '.DB::table('jeu_participations')->where('game_id', $jeu->id)->count()." parties\n";
