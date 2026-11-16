<?php
// Remise à zéro pour filmer CRM56 (lead magnets) : supprime le lead magnet de démo créé pendant le tournage.
// Copie de tournage uniquement. Usage : php artisan tinker puis require ce fichier.
$u = App\Models\User::where('email', 'demo@rapido.test')->first();
$n = DB::table('lead_magnets')->where('company_id', $u->company_id)->where('titre', "10 idées de menus d'hiver")->delete();
echo $n." lead magnet(s) de démo supprimé(s)\n";
