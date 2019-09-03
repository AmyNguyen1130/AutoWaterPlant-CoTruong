<?php
$password = $_GET["password"];
 if($password === "cotruong"){
        system("gpio -g mode 17 out");
        system("gpio -g write 17 1");
        system("gpio -g mode 18 out");
        system("gpio -g write 18 0");
        echo("dung");    
}else{
        system("gpio -g mode 18 out");
        system("gpio -g write 18 1");
        system("gpio -g mode 17 out");
        system("gpio -g write 17 0");
        echo("sai");
}

?>


