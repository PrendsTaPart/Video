<?php
// Jeu de démonstration LOCAL pour l'épisode 8 — base SQLite jetable, aucune donnée réelle.
require '/home/user/rapido-rh/vendor/autoload.php';
$app = require '/home/user/rapido-rh/bootstrap/app.php';
$app->make(Illuminate\Contracts\Console\Kernel::class)->bootstrap();
use Illuminate\Support\Facades\DB; use Illuminate\Support\Facades\Hash;
$now=now(); $d=fn($n)=>now()->startOfDay()->addDays($n)->toDateString();
$pw=Hash::make('demo-locale-2026');
$owner=DB::table('users')->insertGetId(['last_name'=>'(démo)','first_name'=>'Michael','email'=>'michael@demo.local','is_owner'=>1,'role_id'=>1,'password'=>$pw,'hours_worked'=>0,'leave_days'=>0,'currency'=>'EUR','status'=>1,'created_at'=>$now,'updated_at'=>$now]);
$co=DB::table('companies')->insertGetId(['name'=>'BraindCode · DÉMO','email'=>'contact@demo.local','owner_id'=>$owner,'trial_started_at'=>$now,'trial_ends_at'=>now()->addDays(30),'is_trial_used'=>1,'city'=>'Démo','created_at'=>$now,'updated_at'=>$now]);
DB::table('users')->where('id',$owner)->update(['company_id'=>$co]);
$dep=[];foreach([['Développement','Applications et MCP'],['Produit','Cahiers des charges et tests'],['Contenu','Vidéos, BD et réseaux']] as [$n,$ds])$dep[$n]=DB::table('departments')->insertGetId(['name'=>$n,'description'=>$ds,'company_id'=>$co,'created_at'=>$now,'updated_at'=>$now]);
DB::table('users')->where('id',$owner)->update(['department_id'=>$dep['Produit']]);
$u=[];foreach([['Sarah','Développement',2],['Yanis','Développement',3],['Inès','Produit',3],['Karim','Contenu',3],['Léa','Contenu',3]] as [$p,$dn,$r])
 $u[$p]=DB::table('users')->insertGetId(['last_name'=>'(démo)','first_name'=>$p,'email'=>strtolower(iconv('UTF-8','ASCII//TRANSLIT',$p)).'@demo.local','is_owner'=>0,'role_id'=>$r,'password'=>$pw,'company_id'=>$co,'department_id'=>$dep[$dn],'hours_worked'=>0,'leave_days'=>0,'currency'=>'EUR','status'=>1,'created_at'=>$now,'updated_at'=>$now]);
$P=[
 ['FoodEatUp · Daily Brief','Extension : anomalies de la veille et priorités du jour.',$u['Sarah'],-12,18,2,[
   ['Brancher le MCP FoodEatUp (lecture)','Sarah',1,0,-1],['Écran « priorités du jour »','Yanis',0,0,1],['Règles d\'alerte HACCP','Inès',0,1,3],['Tests de bout en bout','Inès',0,1,6],['Cahier des charges validé','Michael',2,1,-6]]],
 ['RapidoCMS · Bibliothèque v2','Recherche et tri des médias.',$u['Yanis'],-20,10,1,[
   ['Filtre par type de média','Yanis',1,1,2],['Correction du tri par date','Sarah',0,0,0],['Documentation utilisateur','Léa',0,2,8],['Migration des miniatures','Yanis',2,1,-3]]],
 ['Série vidéo « Mon quotidien avec l\'IA »','Un épisode par jour.',$owner,-15,45,1,[
   ['Épisode 8 : RapidoRH','Karim',1,0,0],['Miniatures de la semaine','Léa',0,1,2],['Sous-titres épisodes 11 à 15','Karim',0,1,4],['Script épisode 16','Michael',0,2,5],['Épisode 10 publié en brouillon','Léa',2,1,-2]]],
];
foreach($P as [$name,$desc,$pm,$s,$e,$size,$tasks]){
 $pid=DB::table('projects')->insertGetId(['name'=>$name,'description'=>$desc,'start_date'=>$d($s),'end_date'=>$d($e),'company_id'=>$co,'project_manager_id'=>$pm,'status'=>0,'size'=>$size,'created_at'=>$now,'updated_at'=>$now]);
 $members=array_unique(array_merge([$pm,$owner],array_map(fn($t)=>$t[1]==='Michael'?$owner:$u[$t[1]],$tasks)));
 foreach($members as $m) DB::table('project_user')->insert(['project_id'=>$pid,'user_id'=>$m,'created_at'=>$now,'updated_at'=>$now]);
 $tl=[];foreach(['À faire','En cours','Terminé'] as $i=>$n)$tl[$i]=DB::table('task_lists')->insertGetId(['name'=>$n,'is_default'=>1,'order'=>$i,'project_id'=>$pid,'created_at'=>$now,'updated_at'=>$now]);
 foreach($tasks as [$t,$who,$st,$prio,$due]){$aid=$who==='Michael'?$owner:$u[$who];
  $tid=DB::table('tasks')->insertGetId(['title'=>$t,'description'=>'Tâche de démonstration','due_date'=>$d($due),'status'=>$st,'priority'=>$prio,'assigned_to'=>$aid,'tasklist_id'=>$tl[$st],'created_at'=>$now,'updated_at'=>$now]);
  if(\Schema::hasTable('task_users')) DB::table('task_users')->insert(['task_id'=>$tid,'user_id'=>$aid,'created_at'=>$now,'updated_at'=>$now]);}
}
echo "ok company=$co owner=$owner\n";
