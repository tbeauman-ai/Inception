<?php

define('DB_NAME', getenv('DB_NAME__'));
define('DB_USER', getenv('DB_USER__'));
define('DB_PASSWORD',  getenv('DB_PASSWORD__'));
define('DB_HOST', getenv('DB_HOST__'));
define('DB_CHARSET', 'utf8');


define('AUTH_KEY', getenv('AUTH_KEY__'));
define('SECURE_AUTH_KEY', getenv('SECURE_AUTH_KEY__'));
define('LOGGED_IN_KEY', getenv('LOGGED_IN_KEY__'));
define('NONCE_KEY', getenv('NONCE_KEY__'));
define('AUTH_SALT', getenv('AUTH_SALT__'));
define('SECURE_AUTH_SALT', getenv('SECURE_AUTH_SALT__'));
define('LOGGED_IN_SALT', getenv('LOGGED_IN_SALT__'));
define('NONCE_SALT', getenv('NONCE_SALT__'));

$table_prefix = 'wp_';
define('WP_DEBUG', true);

if (!defined('ABSPATH'))
    define('ABSPATH', dirname(__FILE__) . '/');

require_once(ABSPATH . 'wp-settings.php');
