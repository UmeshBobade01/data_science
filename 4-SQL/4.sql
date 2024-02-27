--Data Types
--boolean(True and False)
--char(char,varchara and text)
--numeric(integer and floting point number)
--temporal(date,time,timestamp and interval)
--UUID(Universely Unique Identifiers)
--array(stores an array of strings,numbers,etc)
--json
--Hstore key value pair
--speacial types such as network address and geometric data

--postgresql.org/docs/current/datatype.html


--primary key and foreign keys
--primary key is column or group of columns used to identify a row uniquely in a table
--foreign key is a field or grp of fields in atable that identifies a row in a another table
--foreign key in a table that references to the primary key of other table
--table that contains the foreign key ia called referencing table or child table
select * from payment


--constraints
--1.go to constraints  2.right click and select properties  3.goto columns  4.find referenced table
--used to prevent invalid data from being entered into database
--ensures accuracy and reliability of data
--two types
--1.column constraints
--most common column consgtraints
--NOT NULL{column can not have NULL value}
--UNIQUE{all values in column are different}
--PRIMARY KEY
--FOREIGN KEY
--check{ensures that all values in a column satisfy certain condition}
--EXCLUSION{ensures that if any two rows are compared on the specified column or expression using the specifeid column}
--2. table constraints
--CHECK(condition){to check condition when inseerting or updating data}
--REFERENCES{to constraints the value  stored in column that must exist in a column in another table}
--UNIQUE(column_list){forces values stored in the columns listed to be unique}
--PRIMARY KEY(column_list){allow yo to define multiple primary key}


--CREATE
--syntax:
--		CREATE TABLE table_name(column_name TYPE column_constraints,column_name TYPE column_constraints,table_constraints) inherits existing_table_name
--example:
--		CREATE TABLE players(player_id SERIAL PRIMARY KEY,age SMALLINT NOT NULL)
--serial will create a sequence object and set the next value generated by the sequence as the default value for the column
--no nedd to insert serial data type

create table account(
	user_id serial primary key,
	username varchar(50) unique not null,
	password varchar(50) not null,
	email varchar(50) unique not null,
	created_on timestamp not null,
	last_login timestamp)

create table job(job_id serial primary key,job_name varchar(200) unique not null)

create table account_job(u_id integer references account(user_id),j_id integer references job(job_id),hire_date timestamp)


--INSERT
--allows to add records/rows into table
--syntax:
--		INSERT INTO table(col1,col2,....) VALUES (val1,val2,....),(val1,val2,....),....

insert into account(username,password,email,created_on)
values ('Umesh','UKB','umesh@gmail.com',current_timestamp)
insert into account(username,password,email,created_on)
values ('Yash','YAC','yash@gmail.com',current_timestamp)
insert into account(username,password,email,created_on)
values ('Tejax','TCD','tejax@gmail.com',current_timestamp)
insert into account(username,password,email,created_on)
values ('Aryan','AHK','rn@gmail.com',current_timestamp),('Vikzz','VVB','vikzz@gmail.com',current_timestamp)
select * from account

insert into job(job_name) values ('Data Scientist')
insert into job(job_name) values ('Data Analyst')
insert into job(job_name) values ('Developer'),('Professor')
select * from job

insert into account_job(j_id,u_id,hire_date) values (2,2,current_timestamp),(3,4,current_timestamp),(4,5,current_timestamp),(5,6,current_timestamp)
select * from account_job


--UPDATE
--alllows to change values of the columns in a table
--syntax:
--		UPDATE table SET col1 = val1,col2,val2,.... WHERE condition
--example:
--		UPDATE account SET last_login = current_timestamp WHERE last_login is NULL

UPDATE account SET last_login = current_timestamp
--without any condition all the records in the column gets updated

UPDATE account SET last_login = current_timestamp WHERE last_login is NULL
select * from account

--update using another table's column(UPDATE join)
/*	UPDATE table1
	SET original_col = table2.new_col
	from table2
	where table1.id = table2.id  */

--RETURNING will return the specified columns after returning keyword
update account set last_login = created_on returning user_id,last_login

select * from job
select * from account_job
update account_job set hire_date = account.created_on from account where account_job.u_id = account.user_id 


--DELETE
--used to delete records
--syntax:
--		delete from table where condition

select * from account
select * from job
select * from account_job

delete from account_job where u_id in (4,5,6)
delete from job where job_id in (3,4,5)
delete from account where user_id in (4,5,6)


--ALTER
--allows to change an existing table structure. IT allows the following operations:
--add,drop,/rename colummns
--changing column ata type
--set default value for column
--add check constraints
--rename table
--syntax:
--		ALTER TABLE table_name action
--add column -> ALTER TABLE table_name ADD COLUMN new_col TYPE
--drop column -> ALTER TABLE table_name DROP COLUMN col_name
--changing constraints -> ALTER TABLE table_name ALTER COLUMN col_name SET DEFAULT value
--alter constraints -> ALTER TABLE table_name ALTER COLUMN col_name DROP NOT NULL

create table info(info_id serial primary key,title varchar(500) not null,person varchar(50) not null unique)
select * from info

alter table info rename to new_info
select * from new_info

alter table new_info rename column person to people

insert into new_info(title) values ('some_new_title')
--gives error as we not assigned vale to people which having a constraints as not null

--remove the constraints
alter table new_info alter column people drop not null
--now we can add title keeping people column null
insert into new_info(title) values ('some_new_title')

select * from new_info

--removing column
--allowsfor the complete removal of a column in a table
--automatically removes all of its indexes and constraints involving the column
--it will not remove columns used in views,triggers or stored procedures

--remove all dependencies
--ALTER TABLE table_name DROP COLUMN col_name CASCADE

--check for existence to avoid error
-- ALTER TABLE table_name DROP COLUMN IF EXISTS col_name

--drop multiple columns
--ALTER TABLE table_name DROP COLUMN col1 DROP COLUMN col2

select * from new_info

ALTER TABLE new_info DROP COLUMN people
--if above query executed again it will give error
--to avoid this  use 'if exists' 
ALTER TABLE new_info DROP COLUMN if exists people


--CHECK
--allows to create more customised constraints that adhere to a certain condition
--syntax:
--		create table table_name(

create table employees(emp_id serial primary key,first_name varchar(50) not null,last_name varchar(50) not null,
birthdate date check (birthdate > '1900-01-01'),hire_date date check (hire_date > birthdate),salary integer check (salary > 0))

insert into employees(first_name,last_name,birthdate,hire_date,salary)
values ('Jose','Portilla','1999-11-03','2010-01-01',648464)

insert into employees(first_name,last_name,birthdate,hire_date,salary)
values ('Sammy','wills','1999-11-03','2010-01-01',500000)

select * from employees


--				database used >>> dvdrental			--

--CASE
--we can use case statement to only execute SQL code when certain condition are met(similar to if-else condition)
--syntax:
--		case
--			when condition1 then result1
--			when condition2 then result2
--			else some_other_result
--		end

select * from customer

select customer_id,
case when (customer_id <= 100) then 'Premium' when (customer_id between 100 and 200) then 'Plus' else 'Normal' end  as subscription
from customer

select customer_id,
case customer_id when 2 then 'Winner' when 5 then 'Second place' else 'Normal' end  as raffle_result
from customer

select * from film
select rental_rate from film

select
sum(case rental_rate when 0.99 then 1 else 0 end) as bargains,
sum(case rental_rate when 2.99 then 1 else 0 end) as regular,
sum(case rental_rate when 4.99 then 1 else 0 end) as premium
from film


--VIEWS
--instead of having to perform the same query again and again as  a starting point,
--you can create a VIEWnto quickly see this query with simple call
--view is a database object that is of a stored query
--view can be accessed as a virtual table in postgresql
--view can not store data physically, it simply stores query
--you can also update and alter the views


select * from customer

select first_name,last_name,address from customer join address
on customer.address_id = address.address_id
--creating view
create view customer_info as select first_name,last_name,address from customer join address
on customer.address_id = address.address_id
--display view
select * from customer_info

--changing the current view
create or replace view customer_info as select first_name,last_name,address,district from customer join address
on customer.address_id = address.address_id
--display view after change
select * from customer_info

--rename view
alter view customer_info rename to c_info
select * from c_info

--drop view
drop view if exists c_info


--			database used >>> testme			--

--IMPORTING AND EXPORTING DATA
--this functionality of pgadmin allows to import data from a .csv file to an already existing table
--you must have to edit your file to be compatible with SQL because all files will not get accepted due to variation in formatting,
--macros,data types,etc.
--reference link ->> postgresql.org/docs/12/sql-copy.html
--must give appropriate file path while importing file for that confirm the file location in properties
--IMPORT command does not create table it assumes that table is already created

--import file
--1.go to database into which you have to import file or create table
--2.go to into which you want to import data
--3. right click on table and choose import/export
--4. give file path, set header as TRUE, give dilimiter as comma, give qoute as single qoute

create table simple(a integer,b integer,c integer)
select * from simple


--			SQL Practise			--

--create table countries with columns contaning name,id,region_id
create table countries(country_id varchar(3),country_name varchar(50),region_id decimal(10,0))
select * from countries
--import data from csv file
select * from countries

--create table duplicate of above table
create table dup_countries as select * from countries
select * from dup_countries

--create table countries and set constraints as not null
create table if not exists countries(country_id varchar(3) not null,country_name varchar(50) not null,region_id decimal(10,0) not null)

--create table jobs including columns id,
create table job(job_id integer primary key,title varchar(50) not null,min_salary integer,max_salary integer check(max_salary<=25000))
select * from job

--create table countries with columns contaning name,id,region_id country_name not contains italy,india and china
create table if not exists countries(country_id integer,
									 country_name varchar(50) check (country_name in ('India','Italy','China')),
									 region_id integer)

--create table countries where country_id is not duplicated
create table if not exists countries(country_id integer primary key,country_name varchar(50),region_id integer)

--create table job including columns job_id,job_title,min_salary,max_salary
--job_title is blank by default and min_salary is 8000 by dafault
--max_salary can be null if not entered
create table job(job_id integer primary key,title varchar(50) default(''),min_salary integer default(8000),max_salary integer)
select * from job

--table not contain duplicate value for country_id which is a key field
create table if not exists countries(country_id integer primary key,country_name varchar(50),region_id integer)

--country_id should be auto incremented and unique
create table if not exists countries(country_id serial primary key,country_name varchar(50),region_id integer)

--country_id and region_id should be unique and not null
create table if not exists countries(country_id integer primary key,country_name varchar(50),region_id integer unique not null)

--
create table job_history(
	employee_id integer primary key,
	start_date date not null,
	end_date date not null,
	job_id integer not null,
	department_id integer default null,
	foreign key (job_id) references job(job_id)
	)
select * from job_history