--			assignment 4 			--

--Write a query to find the addresses (location_id, street_address, city, state_province, country_name) of all the departments.

create table locations(location_id integer primary key,street_address varchar(50),postal_code integer,city varchar(50),
						state_province varchar(50),country_id integer,foreign key (country_id) references countries(country_id))

create table countries(country_id integer primary key,country_name varchar(50),region_id integer unique not null)
