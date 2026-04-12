FROM alpine:3.22

RUN apk add --no-cache mariadb mariadb-client

COPY conf/init.sh /init.sh
COPY conf/my.cnf /etc/my.cnf.d/my.cnf
RUN chmod +x /init.sh

EXPOSE 3306

ENTRYPOINT ["/init.sh"]