FROM postgis/postgis:18-3.6-alpine

RUN apt-get update \
    && apt-get install -y --no-install-recommends postgresql-$PG_MAJOR-pgvector \
    && rm -rf /var/lib/apt/lists/*

