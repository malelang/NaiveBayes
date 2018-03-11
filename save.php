<?php

$edad = $_POST['edad'];
$genero = $_POST['genero'];
$sanguinea =$_POST['sanguinea'];
$colesterol =$_POST['colesterol'];
$sodio =$_POST['sodio'];
$potasio =$_POST['potasio'];


//$command = escapeshellcmd('D:\xampp\htdocs\mineria\test.py');
//$output = shell_exec($command);
//echo $output;

$command = 'python test.py ' . $edad .' '. $genero.' '. $sanguinea.' '. $colesterol.' '. $sodio.' '. $potasio;
$output = passthru($command);
echo $output;

header("Location: list.php");
exit;


?>
