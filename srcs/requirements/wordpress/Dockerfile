FROM alpine:3.22

RUN apk add --no-cache \
    php83-fpm \
    php83-json \
    php83-mysqli \
    php83-dom \
    php83-xml \
    php83-mbstring \
    php83-curl \
    php83-zip \
    wget unzip

RUN wget -q https://wordpress.org/latest.zip -O /tmp/wp.zip \
    && unzip -q /tmp/wp.zip -d /var/www/ \
    && rm /tmp/wp.zip \
    && addgroup -S wordpress && adduser -S -G wordpress wordpress \
    && chown -R wordpress:wordpress /var/www/wordpress

RUN mkdir -p /var/log/php83 && chown -R wordpress:wordpress /var/log/php83

RUN sed -i 's/listen = 127.0.0.1:9000/listen = 0.0.0.0:9000/' /etc/php83/php-fpm.d/www.conf

USER wordpress

COPY conf/wp-config.php /var/www/wordpress/wp-config.php

WORKDIR /var/www/wordpress

EXPOSE 9000
ENTRYPOINT ["php-fpm83", "-F"]