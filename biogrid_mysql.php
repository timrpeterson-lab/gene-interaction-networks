<?php
$servername = "localhost";
$username = "root";
$password = "";
$db = "bio-testing";

try {
    $conn = new PDO("mysql:host=$servername;dbname=".$db, $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION );
  
    echo "Connected successfully"; 
}
catch(PDOException $e)
{
    echo "Connection failed: " . $e->getMessage();
}


//ini_set('memory_limit', '134217728');
ini_set('memory_limit','1G');

echo 'foo';

$query = 'SELECT `Official Symbol Interactor A` as gene_A, `Official Symbol Interactor B` as gene_B from `bio-testing`.Biogrid where `Pubmed ID` = "28514442" and `Score` > 0.98; ';


$sth = $conn->prepare($query);
$sth->execute();
$result = $sth->fetchAll();

$time_start = microtime(true);


$db = 'crispri';
try {
    $conn = new PDO("mysql:host=$servername;dbname=".$db, $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION );
  
    echo "Connected successfully"; 
}
catch(PDOException $e)
{
    echo "Connection failed: " . $e->getMessage();
}


$query = 'SELECT `SELECT gene, `t avg3 average phenotype of strongest 3` as tau from `crispri`.aln; ';


$sth = $conn->prepare($query);
$sth->execute();
$results_ALN = $sth->fetchAll();




echo 'foo1';
//$disease = 'cancer';
foreach($result as $row){

echo 'foo2';

$arr_exclude = ['was',"impact",'trap','ighv(iii)6', "its", 'protease', 'polymerase'];

    if(in_array(strtolower($row['name']), $arr_exclude)) continue;

    //ini_set('memory_limit', '-1');
    $query2 = 'SELECT pmid FROM publications WHERE match(abstract) against("+'.str_replace(["-", "@"], ["", ""],$row['name']).'" IN BOOLEAN MODE);';
    //$result = $conn->query($query);

    $sth2 = $conn->prepare($query2);
    echo 'foo2a: '.$query2;
    $sth2->execute();
    echo 'foo2b';
    /* Fetch all of the values in form of a numeric array */
    $result2 = $sth2->fetchAll();
    echo 'foo2c';

    if(count($result2) > 0){

        echo 'foo3: '.$row['id'];

        foreach($result2 as $row2){
            $query3 = 'INSERT into '.$insert_db_table.' (gene_id,alias_id,pmid) values ("'.$row['gene_id'].'",'.$row['id'].', "'.$row2['pmid'].'")';
            //$result = $conn->query($query);

            $sth3 = $conn->prepare($query3);
            $sth3->execute();
            echo 'insert '.$insert_db_table.':'.$row['id']."\n";        
        }
    }
    else{
        //ACTG1P1

        echo 'foo4: '.$row['id'];
        $query3 = 'INSERT into aliases_orphans (gene_id,id,citation_count) values ("'.$row['gene_id'].'",'.$row['id'].', 0)';
        //$result = $conn->query($query);

        $sth3 = $conn->prepare($query3);
        $sth3->execute();     

        echo 'insert aliases_orphans:'.$row['id']."\n";     
    }


    echo 'foo5: '.$row['id'];

    $time_end = microtime(true);
    $time = $time_end - $time_start;

    echo "- in $time seconds\n";

    /* Fetch all of the values in form of a numeric array */
    //$result3 = $sth->fetchAll();
}


$conn = null;

 ?>








output = []

for row_ALN in results_ALN:

  gene = row_ALN['gene'].lower()

  tau = row_ALN['tau']

  for row in results:

  	gene_A = row['gene_A'].lower()

  	if gene_A == gene:

		gene_B = row['gene_B'].lower()	  	

		output.append([gene, tau, gene_B])

print(output)

for row_ALN in results_ALN:

	gene = row_ALN['gene'].lower()

	for row in output:

		if row[2] == gene:

  			row[3] = row_ALN['tau']


#gene tau gene_B tau_B

with open('biogrid-tau-ppi.csv','wb') as file:
    for line in output:
        file.write(str(line[0])+","+str(line[1])+str(line[2])+","+str(line[3]))
        file.write('\n')

?>
