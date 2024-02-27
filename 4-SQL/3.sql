----------advanced SQL----------

--TIME -> contains only time
--DATE -> contains only date
--TIMESTAMP -> contains date and time
--TIMESTAMPZ -> contains date,time,timezone
show all
select timeofday()
select current_date

--extract()
--allow us to extract or obtain a sub component of a date value
--like year,month,day,week,quarter
--example::  extract(year from date_col)

--age()
--calculates and returns the current age given a timestamp
--example:: age(date_col)

--to_char()
--convert datatypes into text
--useful for timstamp formatting
--example::  to_char(date_col,'mm-dd-yyyy')

select * from payment
--extract
select extract(year from payment_date) as myyear from payment
select extract(month from payment_date) as paymonth from payment
select extract(quarter from payment_date) as paymonth from payment

--age
select age(payment_date) from payment

--to_char
select to_char(payment_date,'mm/dd/yyyy') from payment


--challenge
select distinct(to_char(payment_date,'MONTH')) from payment

--challenge
--no. of payments made on monday
--DOW is used for day of week where days are starting with index 0=sunday
select count(*) from payment where extract(dow from payment_date) = 1


--mathematical operators and functions

select * from film

select rental_rate/replacement_cost from film
select rental_rate+replacement_cost from film
select rental_rate-replacement_cost from film
select rental_rate*replacement_cost from film
select rental_rate%replacement_cost from film
select |/rental_rate from film
select ||/rental_rate from film
select @rental_rate from film

select round(rental_rate/replacement_cost,2) from film
select round(rental_rate/replacement_cost,2)*100 from film
select round(rental_rate/replacement_cost,2)*100 as percent_cost from film
select 0.1*replacement_cost as deposit from film


--string operations
select * from customer
select length(first_name) from customer
select first_name || ' ' ||last_name as full_name from customer
select upper(first_name) || ' ' || upper(last_name) as full_name from customer
select left(first_name,1) ||last_name || '@gmail.com' from customer
select lower(left(first_name,1)) || lower(last_name) || '@gmail.com' as custom_email from customer


--subquery
--query inside query
--subquery can operate on seperate table
--syntax:-
--		select column_name from Table1 where exists (select column_name from table1)

select * from film
select avg(rental_rate) from film 
select title,rental_rate from film where rental_rate > (select avg(rental_rate) from film)

select * from rental
select * from inventory
select * from rental where return_date between '2005-05-29' and '2005-05-30'

--find out film_id whose return_date is between '2005-05-29' and '2005-05-30'
select inventory.film_id from rental join inventory on inventory.inventory_id = rental.inventory_id
where return_date between '2005-05-29' and '2005-05-30'

select film_id,title from film where film_id 
in(select inventory.film_id from rental join inventory on inventory.inventory_id = rental.inventory_id
where return_date between '2005-05-29' and '2005-05-30')


















