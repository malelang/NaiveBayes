<?php

$cruces = $_POST['cruces'];



$command = 'python combinar.py ' . $cruces;
$output = passthru($command);
echo $output;

$command = 'python ideapymod1.py ';
$output = passthru($command);
echo $output;

$command = 'python ideapymod2.py ';
$output = passthru($command);
echo $output;

$command = 'python ideapymod3.py ';
$output = passthru($command);
echo $output;

$command = 'python prediccion1.py ';
$output = passthru($command);
echo $output;

$command = 'python prediccion2.py ';
$output = passthru($command);
echo $output;

$command = 'python prediccion3.py ';
$output = passthru($command);
echo $output;

$command = 'python calculofinal.py ';
$output = passthru($command);
echo $output;

header("Location: results.php");
exit;


?>
