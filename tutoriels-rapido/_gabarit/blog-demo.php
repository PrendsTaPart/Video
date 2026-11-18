<?php
// Données fictives pour CRM77 (blog). Copie de tournage uniquement. Rejouable.
// Supprime l'article tourné, donne des statistiques de lecture à l'article « séminaire » et un commentaire en attente.
use App\Models\Article;
use App\Models\User;
use Illuminate\Support\Facades\DB;

$u = User::where('email', 'demo@rapido.test')->firstOrFail();
$cid = $u->company_id;
Article::where('company_id', $cid)->where('slug', 'like', 'traiteur-mariage%')->get()->each(function ($a) {
    DB::table('article_commentaires')->where('article_id', $a->id)->delete();
    $a->delete();
});
$s = Article::where('company_id', $cid)->where('slug', 'comment-choisir-son-traiteur-pour-un-seminaire')->firstOrFail();
$s->forceFill(['vues' => 240, 'lectures_mesurees' => 180, 'lectures_completes' => 117, 'temps_lecture_total' => 180 * 172,
    'clics_liens' => 41, 'clics_cta' => 26, 'leads' => 9, 'commentaires_actifs' => true])->save();
DB::table('article_commentaires')->where('article_id', $s->id)->delete();
DB::table('article_commentaires')->insert([
    ['company_id' => $cid, 'article_id' => $s->id, 'nom' => 'Claire Fontaine', 'email' => 'claire.fontaine@exemple.test',
        'contenu' => 'Merci pour ces conseils ! Le point sur la dégustation nous a beaucoup aidés pour notre séminaire de juin.',
        'statut' => 'en_attente', 'empreinte_ip' => hash('sha256', 'demo'), 'created_at' => now()->subHours(3), 'updated_at' => now()->subHours(3)],
]);
echo "Blog prêt : article {$s->id} avec statistiques et un commentaire en attente\n";
