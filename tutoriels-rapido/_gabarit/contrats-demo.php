<?php
// Données fictives pour CRM15 (contrats v2). Copie de tournage uniquement. Rejouable (php artisan tinker).
// Contrats de démonstration créés par ContratService (le même que l'écran et les outils MCP) :
// un contrat à signer dont le lien signé est écrit dans CRM15/lien-signature.txt, un signé, un vu, un refusé.
use App\Models\ContratUserCrm;
use App\Models\User;
use App\Services\ContratService;
use Illuminate\Support\Facades\DB;

$s = app(ContratService::class);
$auteur = User::where('email', 'demo@rapido.test')->firstOrFail();
$titres = ['Maintenance du site 2027', 'Accompagnement réseaux sociaux', 'Contrat de prestation photo', 'Abonnement fidélité 2027'];
foreach (ContratUserCrm::where('company_id', $auteur->company_id)->whereIn('titre', $titres)->get() as $c) {
    DB::table('contrat_evenements')->where('contrat_id', $c->id)->delete();
    $c->forceDelete();
}
$contenu = fn (string $objet) => '<h2>'.$objet.'</h2><p>Entre <strong>Studio Lumière</strong> et <strong>[$nom$]</strong>.</p>'
    .'<h3>Article 1 — Objet</h3><p>Le prestataire assure '.mb_strtolower($objet).' pendant douze mois.</p>'
    .'<h3>Article 2 — Prix</h3><p>Le prix est fixé à 150 € HT par mois, payable à réception de facture.</p>'
    .'<h3>Article 3 — Durée et reconduction</h3><p>Le contrat est reconduit tacitement, sauf résiliation avec un préavis de trente jours.</p>';
$base = ['debut' => now()->toDateString(), 'fin' => now()->addYear()->toDateString(), 'montant' => 1800, 'reconduction_tacite' => true, 'preavis_jours' => 30];
$aSigner = $s->creer($auteur, $base + ['entreprise_id' => 1, 'titre' => 'Maintenance du site 2027', 'contenu' => $contenu('La maintenance du site internet')]);
$signe = $s->creer($auteur, $base + ['entreprise_id' => 6, 'titre' => 'Accompagnement réseaux sociaux', 'contenu' => $contenu('L’accompagnement sur les réseaux sociaux')]);
$png = 'data:image/png;base64,'.base64_encode(base64_decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII='));
$s->marquerVu($signe, '203.0.113.10', 'Mozilla/5.0 (démo)');
$s->signer($signe, ['nom' => 'Hélène Garonne', 'consentement' => '1', 'signature' => $png], '203.0.113.10', 'Mozilla/5.0 (démo)');
$vu = $s->creer($auteur, $base + ['entreprise_id' => 3, 'titre' => 'Contrat de prestation photo', 'contenu' => $contenu('La prestation photo')]);
$s->marquerVu($vu, '203.0.113.11', 'Mozilla/5.0 (démo)');
$refuse = $s->creer($auteur, $base + ['entreprise_id' => 2, 'titre' => 'Abonnement fidélité 2027', 'contenu' => $contenu('L’abonnement au programme de fidélité')]);
$s->refuser($refuse, 'Nous préférons attendre la rentrée.', '203.0.113.12', 'Mozilla/5.0 (démo)');
file_put_contents('/home/user/video/tutoriels-rapido/CRM15/lien-signature.txt', $s->lienSignature($aSigner));
file_put_contents('/home/user/video/tutoriels-rapido/CRM15/contrat-id.txt', (string) $aSigner->id);
file_put_contents('/home/user/video/tutoriels-rapido/CRM15/contrat-url.txt', route('admin.contrats.show', $aSigner->id));
echo 'Contrats prêts : à signer #'.$aSigner->id.', signé #'.$signe->id.', vu #'.$vu->id.', refusé #'.$refuse->id."\n";
