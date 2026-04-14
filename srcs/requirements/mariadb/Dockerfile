FROM alpine:3.22

RUN apk add --no-cache mariadb mariadb-client
RUN sed -i 's/skip-networking//' /etc/my.cnf.d/mariadb-server.cnf

COPY conf/init.sh /init.sh
RUN chmod +x /init.sh

EXPOSE 3306

ENTRYPOINT ["./init.sh"]