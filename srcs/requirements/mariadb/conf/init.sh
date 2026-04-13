#!/bin/sh
echo "DB_NAME = ${DB_NAME}"
echo "DB_USER = ${DB_USER}"
mkdir -p /run/mysqld
chown -R mysql:mysql /run/mysqld

if [ ! -d "/var/lib/mysql/mysql" ]; then
    mysql_install_db --user=mysql --datadir=/var/lib/mysql
fi

mysqld --user=mysql & MYSQL_PID=$!

until mysqladmin ping --silent; do
    sleep 1
done

mysql -u root << EOF
CREATE DATABASE IF NOT EXISTS ${DB_NAME};
CREATE USER IF NOT EXISTS '${DB_USER}'@'%' IDENTIFIED BY '${DB_PASSWORD}';
GRANT ALL PRIVILEGES ON ${DB_NAME}.* TO '${DB_USER}'@'%';
FLUSH PRIVILEGES;
EOF

mysqladmin shutdown
wait $MYSQL_PID

exec mysqld --user=mysql 