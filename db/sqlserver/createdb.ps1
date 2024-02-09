#!/bin/bash
# ${TAG}='2022-latest'
# ${MSSQL_SA_PASSWORD}='Passw@rd'
# ${MSSQL_PORT}=1433
# ${MSSQL_DB}='dbcity'
# ${CONTAINER_NAME}="mssql_${MSSQL_DB}"
# ${DATA_VOLUME_NAME}="data_mssql_${MSSQL_DB}"


# create data volume storing the data
# docker volume create $DATA_VOLUME_NAME

# create container PostgreSQL with its data in previous volume
# docker run -p ${MSSQL_PORT}:1433 `
# 	-e "ACCEPT_EULA=Y" `
# 	-e "MSSQL_PID=Developer" `
# 	-e "MSSQL_SA_PASSWORD=$MSSQL_SA_PASSWORD" `
# 	--name $CONTAINER_NAME `
# 	-d 'mcr.microsoft.com/mssql/server':$TAG

docker run -p 1433:1433 `
	-e "ACCEPT_EULA=Y" `
	-e "MSSQL_PID=Developer" `
	-e "MSSQL_SA_PASSWORD=Passw@rd" `
	--name mssql-dbcity `
	-d 'mcr.microsoft.com/mssql/server:2022-latest'