#!/bin/sh
echo "DB_NAME = ${DB_NAME}"
echo "DB_USER = ${DB_USER}"
mkdir -p /run/mysqld
chown -R mysql:mysql /run/mysqld

if [ ! -d "/var/lib/mysql/mysql" ]; then
    mysql_install_db --user=mysql --datadir=/var/lib/mysql
fi

exec mysqld --user=mysql --port=3306 --bind-address=0.0.0.0 --skip-networking=0

mysqld --user=mysql --bootstrap << EOF
FLUSH PRIVILEGES;
CREATE DATABASE IF NOT EXISTS ${DB_NAME__};
CREATE USER IF NOT EXISTS '${DB_USER__}'@'%' IDENTIFIED BY '${DB_PASSWORD__}';
GRANT ALL PRIVILEGES ON ${DB_NAME__}.* TO '${DB_USER__}'@'%';
FLUSH PRIVILEGES;
EOF

exec mysqld --user=mysql