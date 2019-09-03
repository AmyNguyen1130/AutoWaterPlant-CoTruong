<?php
	system("gpio -g mode 17 out");
	system("gpio -g write 17 0");
	system("gpio -g mode 18 out");
        system("gpio -g write 18 1");

?>
<html>
<body>
	<form method="GET" action="ledPHP.php">
		<button type="submit">BACK</button>
	</form>
</body>
</html>

