<?php
// Données fictives pour CRM28 (sondages v2). Copie de tournage uniquement. Rejouable (php artisan tinker).
// Retire le sondage créé lors d'une prise précédente et prépare « Satisfaction après livraison » avec des réponses
// fictives (pour l'écran Résultats). Les réponses passent par SondageService::repondre(), comme la page publique.
use App\Models\SondageCompanie;
use App\Models\User;
use App\Services\SondageService;
use Illuminate\Support\Facades\DB;

$s = app(SondageService::class);
$auteur = User::where('email', 'demo@rapido.test')->firstOrFail();
foreach (SondageCompanie::where('company_id', $auteur->company_id)->whereIn('name', ['Avis après rendez-vous', 'Satisfaction après livraison'])->get() as $x) {
    DB::table('sondage_soumissions')->where('sondage_id', $x->id)->delete();
    DB::table('sondage_vues')->where('sondage_id', $x->id)->delete();
    DB::table('sondage_reponse')->where('sondage_id', $x->id)->delete();
    $x->forceDelete();
}
$sondage = $s->creer($auteur, ['name' => 'Satisfaction après livraison']);
$s->enregistrerQuestions($sondage, [
    ['cle' => 'nps', 'type' => 'nps', 'titre' => 'Quelle est la probabilité que vous nous recommandiez à un proche ?', 'obligatoire' => true],
    ['cle' => 'connu', 'type' => 'choix_unique', 'titre' => 'Comment nous avez-vous connus ?', 'choix' => ['Bouche-à-oreille', 'Instagram', 'Site web', 'Salon'], 'obligatoire' => true],
    ['cle' => 'pourquoi', 'type' => 'texte_long', 'titre' => 'Qu’est-ce qui explique votre note ?', 'obligatoire' => false],
]);
mt_srand(28);
$notes = [10, 9, 9, 10, 8, 7, 9, 10, 6, 9, 10, 4, 9, 8];
$textes = ['Livraison rapide et soignée.', 'Très bon accueil, je recommande.', 'Un peu d’attente au téléphone.', 'Parfait du début à la fin.', '', 'Produit conforme, emballage à revoir.'];
foreach ($notes as $i => $n) {
    $s->compterVue($sondage, 'vue', ['source' => ['email', 'qr', 'site'][$i % 3], 'appareil' => $i % 2 ? 'mobile' : 'ordinateur']);
    $s->compterVue($sondage, 'debut', ['source' => ['email', 'qr', 'site'][$i % 3], 'appareil' => $i % 2 ? 'mobile' : 'ordinateur']);
    $s->repondre($sondage, ['nps' => $n, 'connu' => ['Bouche-à-oreille', 'Instagram', 'Site web', 'Salon'][$i % 4], 'pourquoi' => $textes[$i % count($textes)]], [], ['source' => ['email', 'qr', 'site'][$i % 3], 'appareil' => $i % 2 ? 'mobile' : 'ordinateur']);
}
foreach (range(1, 4) as $v) {
    $s->compterVue($sondage, 'vue', ['source' => 'site', 'appareil' => 'mobile']);
}
echo 'Sondages prêts : '.DB::table('sondage_soumissions')->where('sondage_id', $sondage->id)->count()." réponses\n";
