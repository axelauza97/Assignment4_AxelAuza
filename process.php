<?php
    if ($_SERVER["REQUEST_METHOD"] == "GET") {
        $a = escapeshellarg($_GET['a']);
        $b = escapeshellarg($_GET['b']);
        $c = escapeshellarg($_GET['c']);
        $d = escapeshellarg($_GET['d']);
        $e = escapeshellarg($_GET['e']);
        
        // Execute Python script with passed arguments
        $command = escapeshellcmd("python3 /var/www/html/data_management.py $a $b $c $d $e");
        $output = shell_exec($command);
        
        // Display Python script output
        echo $output;
    }
?>
