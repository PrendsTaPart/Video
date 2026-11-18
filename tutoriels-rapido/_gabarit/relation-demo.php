<?php
// Données fictives pour CRM90 (centre d'aide et répartition des prospects). Copie de tournage uniquement. Rejouable.
use App\Models\Connaissance;
use App\Models\Contact;
use App\Models\Ticket;
use Illuminate\Support\Facades\DB;

$cid = 1;
// Demandes et contacts créés par les tournages précédents du centre d'aide
$ids = Ticket::where('company_id', $cid)->where('canal', 'site')->where('id', '>', 20)->pluck('id');
DB::table('ticket_messages')->whereIn('ticket_id', $ids)->delete();
Ticket::whereIn('id', $ids)->delete();
Contact::where('company_id', $cid)->where('source_canal', 'centre_aide')->get()->each->delete();
// Questions fréquentes du centre d'aide
Connaissance::where('company_id', $cid)->where('source', 'faq')->delete();
$cs = app(\App\Services\ConnaissanceService::class);
foreach ([
    ['Quels sont vos délais de livraison d’un site ?', 'Un site vitrine est livré en trois à quatre semaines après validation de la maquette. Une boutique en ligne demande six à huit semaines.'],
    ['Comment demander un devis ?', 'Remplissez le formulaire de devis en ligne : vous recevez une proposition détaillée sous 48 heures, sans engagement.'],
    ['Quels sont vos horaires ?', 'Nous sommes ouverts du lundi au vendredi, de 9 h à 18 h, et le samedi matin sur rendez-vous.'],
] as [$q, $r]) {
    $cs->ajouterFaq($cid, ['question' => $q, 'reponse' => $r]);
}
// Répartition désactivée au départ (elle est réglée pendant le tutoriel)
DB::table('repartition_reglages')->where('company_id', $cid)->delete();
echo "Relation client prête\n";
