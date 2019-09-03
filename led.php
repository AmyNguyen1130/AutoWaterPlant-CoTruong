<?php   
        for( $i = 0; $i<100 ;$i++){
        system("gpio -g mode 18 out");
        system("gpio -g write 18 0");
        system("gpio -g mode 17 out");
        system("gpio -g write 17 1");
        sleep(0.3);
        system("gpio -g mode 17 out");
        system("gpio -g write 17 0");
        system("gpio -g mode 18 out");
        system("gpio -g write 18 1");
        sleep(0.3);
        system("gpio -g mode 18 out");
        system("gpio -g write 18 0");
        system("gpio -g mode 22 out");
        system("gpio -g write 22 1");
        sleep(0.5);
        system("gpio -g mode 22 out");
        system("gpio -g write 22 0");
        system("gpio -g mode 27 out");
        system("gpio -g write 27 1");
                sleep(0.5);
        system("gpio -g mode 27 out");
        system("gpio -g write 27 0");
        system("gpio -g mode 23 out");
        system("gpio -g write 23 1");

        sleep(0.3);
        system("gpio -g mode 23 out");
        system("gpio -g write 23 0");
        system("gpio -g mode 27 out");
        system("gpio -g write 27 1");
        sleep(0.3);
        system("gpio -g mode 27 out");
        system("gpio -g write 27 0");
        system("gpio -g mode 22 out");
        system("gpio -g write 22 1");
        sleep(0.3);
        system("gpio -g mode 22 out");
        system("gpio -g write 22 0");
        system("gpio -g mode 18 out");
        system("gpio -g write 18 1");
        sleep(0.5);

}
	 system("gpio -g mode 18 out");
        system("gpio -g write 18 0");
       
?>
