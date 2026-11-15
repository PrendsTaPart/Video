<?php
// Remise à zéro pour filmer CRM63 (séquences de prospection). Copie de tournage uniquement.
// Supprime les séquences de la société de démo (CRM63 en crée une pendant le tournage) puis rejoue les scores de démo,
// pour que la cible « Prospects chauds (score) » contienne un contact. Usage : php artisan tinker puis require ce fichier.
$u = App\Models\User::where('email', 'demo@rapido.test')->first();
$ids = DB::table('sequences')->where('company_id', $u->company_id)->pluck('id');
DB::table('sequence_journal')->whereIn('inscription_id', DB::table('sequence_inscriptions')->whereIn('sequence_id', $ids)->pluck('id'))->delete();
DB::table('sequence_inscriptions')->whereIn('sequence_id', $ids)->delete();
DB::table('sequence_etapes')->whereIn('sequence_id', $ids)->delete();
DB::table('sequences')->whereIn('id', $ids)->delete();
echo $ids->count()." séquence(s) supprimée(s)\n";
require __DIR__.'/score-demo.php';
