<?php
// Données fictives pour CRM18 (campagnes SMS). Copie de tournage uniquement. Rejouable (php artisan tinker).
// Deux modèles de SMS de la société et le jeu « Roue du printemps » (joueurs avec téléphone, via jeux-demo.php).
use Illuminate\Support\Facades\DB;

require '/home/user/video/tutoriels-rapido/_gabarit/jeux-demo.php';
DB::table('campagne_sms')->where('company_id', 1)->where('created_at', '>=', now()->startOfDay())->delete();
foreach ([
    ['Lot à retirer', 'Bonjour {prenom}, votre lot de la Roue du printemps vous attend en boutique jusqu’au 30 avril. À très vite !'],
    ['Rappel de rendez-vous', 'Bonjour {prenom}, petit rappel : votre rendez-vous est prévu demain. Répondez à ce SMS pour le déplacer.'],
] as [$nom, $contenu]) {
    DB::table('template_sms')->updateOrInsert(['company_id' => 1, 'nom' => $nom], ['contenu' => $contenu, 'categorie' => 'Marketing', 'image' => null, 'created_at' => now(), 'updated_at' => now()]);
}
echo 'SMS prêts : '.DB::table('template_sms')->where('company_id', 1)->count()." modèles\n";
