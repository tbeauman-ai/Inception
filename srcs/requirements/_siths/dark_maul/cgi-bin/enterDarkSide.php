#!/usr/bin/php-cgi
<?php
header("Set-Cookie: side=sith; Path=/; HttpOnly; SameSite=Lax");
header("Content-Type: text/html");
echo '<meta http-equiv="refresh" content="0; url=/">';
?>