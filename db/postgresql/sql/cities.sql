create table city(
    id serial constraint pk_city PRIMARY KEY,
    insee_code char(5), 
    city_code varchar(50), 
    zip_code char(5), 
    label varchar(50) not null, 
    latitude double precision, 
    longitude double precision,
    department_name varchar(30), 
    department_number varchar(3), 
    region_name varchar(30),
    region_geojson_name varchar(30)
);