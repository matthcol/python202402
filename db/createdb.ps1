#!/bin/bash
${TAG}='latest'
${POSTGRES_USER}='citymngr'
${POSTGRES_PASSWORD}='password'
${POSTGRES_PORT}=5432
${POSTGRES_DB}='dbcity'
${CONTAINER_NAME}="pg_${POSTGRES_DB}"
${DATA_VOLUME_NAME}="data_pg_${POSTGRES_DB}"


# create data volume storing the data
docker volume create $DATA_VOLUME_NAME

# create container PostgreSQL with its data in previous volume
docker run -p ${POSTGRES_PORT}:5432 `
	-e "POSTGRES_USER=$POSTGRES_USER" `
	-e "POSTGRES_PASSWORD=$POSTGRES_PASSWORD" `
	-e "POSTGRES_DB=$POSTGRES_DB" `
	-v $PWD/sql:/docker-entrypoint-initdb.d `
	-v ${DATA_VOLUME_NAME}:/var/lib/postgresql/data `
	--name $CONTAINER_NAME `
	-d postgres:$TAG
