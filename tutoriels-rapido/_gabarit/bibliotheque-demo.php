<?php
// Bibliothèque FICTIVE pour filmer CRM58 (partage suivi et statistiques). Copie de tournage uniquement. Rejouable :
// supprime les fichiers de démo et leurs téléchargements, recrée trois PDF (dompdf) et un historique de téléchargements simulé.
// Usage : php artisan tinker puis require '/home/user/video/tutoriels-rapido/_gabarit/bibliotheque-demo.php';
use Illuminate\Support\Facades\Storage;
$u = App\Models\User::where('email', 'demo@rapido.test')->first();
$cid = $u->company_id;
$noms = ['Plaquette Studio Lumière 2026', 'Catalogue des prestations', 'Guide : bien choisir son site'];
$ids = DB::table('bibliotheque_crm')->where('company_id', $cid)->whereIn('nom', $noms)->pluck('id');
DB::table('bibliotheque_telechargements')->whereIn('fichier_id', $ids)->delete();
DB::table('bibliotheque_crm')->whereIn('id', $ids)->delete();
$disque = App\Support\MediaUrl::disqueEcriture();
$creer = function (string $nom, array $plus) use ($u, $cid, $disque) {
    $html = '<h1 style="font-family:sans-serif;color:#2e7d32">'.e($nom).'</h1><p style="font-family:sans-serif">Document fictif de démonstration — Studio Lumière, agence web à Lyon.</p>';
    $pdf = Barryvdh\DomPDF\Facade\Pdf::loadHTML($html)->output();
    $fichier = Illuminate\Support\Str::slug($nom).'-demo.pdf';
    Storage::disk($disque)->put('rapidosoftware/bibliotheque/'.$fichier, $pdf);
    return DB::table('bibliotheque_crm')->insertGetId($plus + ['user_id' => $u->id, 'company_id' => $cid, 'file' => $fichier, 'nom' => $nom, 'type' => 'text',
        'taille' => strlen($pdf), 'vues' => 0, 'telechargements' => 0, 'partage_actif' => 0, 'acces' => 'libre', 'created_at' => now()->subDays(12), 'updated_at' => now()]);
};
$plaquette = $creer($noms[0], ['dossier' => 'Commercial']);
$catalogue = $creer($noms[1], ['dossier' => 'Commercial', 'partage_actif' => 1, 'acces' => 'libre', 'slug' => 'catalogue-prestations-demo', 'vues' => 32, 'telechargements' => 14]);
$guide = $creer($noms[2], ['dossier' => 'Marketing', 'partage_actif' => 1, 'acces' => 'email', 'slug' => 'guide-choisir-site-demo', 'vues' => 21, 'telechargements' => 9,
    'description' => 'Les 7 questions à se poser avant de refaire son site.']);
$sources = ['lien', 'lien', 'cta', 'site', 'email', 'formulaire'];
$appareils = ['mobile', 'ordinateur', 'mobile', 'tablette'];
foreach ([[$catalogue, 14], [$guide, 9]] as [$id, $n]) {
    for ($i = 0; $i < $n; $i++) {
        DB::table('bibliotheque_telechargements')->insert(['company_id' => $cid, 'fichier_id' => $id, 'source' => $sources[$i % 6], 'appareil' => $appareils[$i % 4],
            'referent' => $i % 3 ? 'https://www.google.com/' : null, 'visiteur' => 'demo-'.$id.'-'.($i % 7), 'email' => $id === $guide ? 'prospect'.$i.'@exemple.test' : null,
            'created_at' => now()->subDays($i % 12)->subHours($i)]);
    }
}
echo "bibliothèque de démo : 3 fichiers, 23 téléchargements\n";
