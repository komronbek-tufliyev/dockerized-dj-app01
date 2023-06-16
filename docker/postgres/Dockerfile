FROM postgres:13.3-alpine

USER postgres

RUN chmod 777 /var/lib/postgresql/data

RUN initdb -D /var/lib/postgresql/data

RUN echo "host all  all 0.0.0.0/0 md5" >> /var/lib/postgresql/data/pg_hba.conf

RUN echo "listen_addresses='*'" >> /var/lib/postgresql/data/postgresql.conf

COPY initdb.sql /docker-entrypoint-initdb.d/

EXPOSE 5432

RUN echo "host all  all 0.0.0.0/0 md5" >> /var/lib/postgresql/data/pg_hba.conf
