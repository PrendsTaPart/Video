<?php
// Données fictives pour CRM17 (campagnes e-mail). Copie de tournage uniquement. Rejouable (php artisan tinker).
// Un modèle d'e-mail de la société et le segment « Prospects chauds de Bordeaux » (s'il n'existe pas déjà).
use Illuminate\Support\Facades\DB;

DB::table('campagne_email')->where('company_id', 1)->where('created_at', '>=', now()->startOfDay())->delete();
$html = '<h2 style="color:#2e7d32">Le printemps arrive chez Studio Lumière</h2>'
    .'<p>Bonjour {prenom},</p><p>Jusqu’au 30 avril, profitez de <strong>20 % sur votre shooting photo</strong> et repartez avec vos images retouchées sous 48 heures.</p>'
    .'<p><a href="https://studio-lumiere.exemple.test/printemps" style="display:inline-block;background:#2e7d32;color:#fff;padding:12px 24px;border-radius:8px;text-decoration:none">Je réserve mon créneau</a></p>'
    .'<p>À très vite,<br>L’équipe Studio Lumière</p>';
DB::table('template_emails')->updateOrInsert(['company_id' => 1, 'nom' => 'Offre de printemps'], ['contenu' => $html, 'categorie' => 'Marketing', 'image' => null, 'created_at' => now(), 'updated_at' => now()]);
if (! DB::table('segments')->where('company_id', 1)->where('nom', 'Prospects chauds de Bordeaux')->exists()) {
    DB::table('segments')->insert([
        'company_id' => 1, 'nom' => 'Prospects chauds de Bordeaux', 'type' => 'actif', 'priorite' => 'normale', 'actif' => 1, 'nombre_contacts' => 12,
        'criteres' => json_encode(['operateur_global' => 'ET', 'groupes' => [['operateur' => 'ET', 'conditions' => [['champ' => 'ville', 'op' => '=', 'valeur' => 'Bordeaux'], ['champ' => 'score_engagement', 'op' => '>=', 'valeur' => '50']]]]]),
        'created_at' => now(), 'updated_at' => now(),
    ]);
}
echo 'E-mails prêts : '.DB::table('template_emails')->where('company_id', 1)->count()." modèle(s)\n";
