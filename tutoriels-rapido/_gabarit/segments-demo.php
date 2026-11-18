<?php
// Données fictives pour CRM21 (segments). Copie de tournage uniquement. Rejouable.
// Scores d'engagement variés pour que le compteur en direct change à chaque condition ; anciens segments de démonstration retirés.
use Illuminate\Support\Facades\DB;

$cid = 1;
foreach (DB::table('contacts')->where('company_id', $cid)->where('id', '>', 5)->pluck('id') as $id) {
    DB::table('contacts')->where('id', $id)->update(['score_engagement' => ($id * 37) % 95]);
}
$ids = DB::table('segments')->where('company_id', $cid)->where('nom', 'like', 'Prospects chauds de Bordeaux%')->pluck('id');
DB::table('segment_contacts')->whereIn('segment_id', $ids)->delete();
DB::table('segments')->whereIn('id', $ids)->delete();
echo 'Segments prêts ('.DB::table('contacts')->where('company_id', $cid)->where('score_engagement', '>=', 50)->count()." contacts au score ≥ 50)\n";
