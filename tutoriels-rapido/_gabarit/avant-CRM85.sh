#!/usr/bin/env bash
# CRM85 (analyse de réunion) : repart d'un écran vide (réunions, tâches, contacts et rendez-vous créés par une prise précédente retirés).
cd /home/user/rapido-crm-film && php artisan tinker --execute='
$cid = App\Models\User::where("email", "demo@rapido.test")->value("company_id");
foreach (App\Models\Reunion::where("company_id", $cid)->get() as $r) { app(App\Services\ReunionService::class)->supprimer($r); }
App\Models\Tache::where("company_id", $cid)->where("description", "like", "Issue de la réunion%")->delete();
App\Models\Contact::where("company_id", $cid)->where("source_canal", "reunion")->delete();
$rv = App\Models\RendezVous::where("titre", "like", "Suivi — %")->pluck("id");
App\Models\RendezVousUser::whereIn("rendez_vous_id", $rv)->delete(); App\Models\RendezVous::whereIn("id", $rv)->delete();
echo "CRM85 prêt\n";'
