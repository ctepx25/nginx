<HTML>
<?php
#ini_set('display_errors', 'On');

$cwd = getcwd();
$command=$_GET['command'];
$output = shell_exec("cd /home/ubuntu/lambda/;sudo -S sed -i 's/VERSION=1/VERSION=2/g' /home/ubuntu/lambda/docker-compose.yml;sudo -S docker-compose -f docker-compose.yml up --build -d");  
echo $output 
?>
</HTML>
