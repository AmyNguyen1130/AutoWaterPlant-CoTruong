<?php
$number = $_GET["number"];

for($i = 0; $i < $number; $i++){
	system("gpio -g mode 17 out");
        system("gpio -g write 17 1");
	sleep(2);
	system("gpio -g mode 17 out");
        system("gpio -g write 17 0");
	sleep(2);
}
?>

