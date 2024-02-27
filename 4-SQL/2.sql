--select all records
select * from film

--select particular column
select first_name,last_name,email from customer

--distinct is used find unique values from table with respect to particular column
--select distinct or unique values
select distinct first_name from customer
select distinct release_year from film
select distinct rating from film


--count function is used to find out the number of records which satisfies a certain condition
--find out number of rows
select count(*) from film
select count(amount) from payment
--count with distinct
select count(distinct(amount)) from payment


--where is used to select records for specific condition
--it acts like a filter
select * from customer where first_name = 'Jay'
select * from film where rental_rate > 3
select * from actor where first_name = 'Tom'


--boolean operators
--AND operator is used for two or more conditions and returrns true if all conditions are true
select * from actor where first_name = 'Tom' and last_name = 'Miranda'
select * from film where rental_rate > 4 and replacement_cost >= 19.99
select * from film where rental_rate > 4 and replacement_cost >= 19.99 and rating = 'R'
select title from film where rental_rate > 4 and replacement_cost >= 19.99 and rating = 'R'
select count(title) from film where rental_rate > 4 and replacement_cost >= 19.99 and rating = 'R'
select count(*) from film where rental_rate > 4 and replacement_cost >= 19.99 and rating = 'R'

--OR operator returns true if any one conditions are true
select * from actor where first_name = 'Tom' or last_name = 'Miranda'
select count(*) from film where rating = 'R' or rating = 'PG-13'

--NOT operator returns the records which are false(not true)
select * from actor where not first_name = 'Tom'
select * from film where rating <> 'R'
select * from film where rating != 'R'


--precedence
--from-->>where-->>select
--Operator precedence ==> () >> */ >> +- >> NOT >> AND >> OR
--if operators have same prcedence then the operators are evaluted directionally from left to right or right to left


--Challenge no.1
--find out email of customer named as Nancy Thomas
select email from customer where first_name = 'Nancy' and last_name = 'Thomas'

--Challenge no.2
--find outn description of movie 'Outlaw Hanky'
select description from film where title = 'Outlaw Hanky'

--Challenge no.3
--find out phone number of with given address
select phone from address where address = '259 Ipoh Drive'


--Order By--
--used to sort records based on particular column in asceding or descending order
--write at the end of query
--basic syntax => **select (columns) from (table) order by (column_name) ASC/DESC**
-- you can also sort table by multiple columns in case their are duplicates values in any column
select * from customer order by first_name asc
select * from customer order by first_name desc
select * from customer order by store_id,first_name,last_name

--LIMIT
--used to select limited number of records from table
--shows the records from top
select * from payment order by payment_date desc limit 5
select * from payment where amount <> 0.00 order by payment_date desc limit 5
select customer_id from payment order by payment_date asc limit 50


--Challenge no.4
--find out title of 5 shortest films
select title,length from film order by length limit 5

--Challenge no.5
--find out 5 shortest films less than or equal to 50 
select title,length from film where length <=50 order by length limit 5


--BETWEEN operator
--used to print records for value in some range
--date should be in format "YYYY-MM-DD"
select * from payment where amount between 8 and 9
select * from payment where amount not between 8 and 9
select * from payment where payment_date between '2007-02-01' and '2007-02-15' order by payment_date


--IN operator
--used to chedeck the value in list of multiple options
--syntax ==>> value in(op1,op2,.....,opn)
--e.g. select color from table where color in ('blue','red')
select distinct(amount) from payment order by amount
select * from payment where amount in (0.00,2.99,5.99,9.99,8.99) order by amount
select count(*) from payment where amount in (0.99,1.98,1.99)
select count(*) from payment where amount not in (0.99,1.98,1.99)
select * from customer where first_name in ('John','Jake','Julie')
select * from customer where first_name not in ('John','Jake','Julie')


--LIKE
--used to find the records with matching pattern for particular value
-- % ==>> matches any sequence of characters
-- _ ==>> matches single character

select * from customer where first_name like 'J%'
--not work for 'j%' so use ilike
select * from customer where first_name ilike 'j%'
select count(*) from customer where first_name like 'J%'

select * from customer where first_name like 'J%' and last_name ilike 's%'

select * from customer
where first_name like 'A%' and last_name not like 'B%'
order by last_name


--Challenge no.6
--amount greater than 5
select count(*) from payment where amount > 5.00

--challenge no.7
--actor name stating with P
select count(*) from actor where first_name like 'P%'


--challenge no.8
--find out count of unique districts
select count(distinct(district)) from address

--Challenge no.9
--name of distinct districts
select distinct(district) from address

--Challenge no.10
--count of films with rating 'R' and replacement cost between 5 & 15
select count(*) from film where rating = 'R' and replacement_cost between 5 and 15

--Challenge no.11
--count of films where title contains 'Truman'
select count(*) from film where title like '%Truman%'


--Most Common Aggregate Functions:

--	AVG() - returns average value
select avg(replacement_cost) from film
--round function is used to round up the result upto specified digits after decimal point
select round(avg(replacement_cost),2) from film
select round(avg(replacement_cost),4) from film


--	COUNT() - returns number of values
select count(*) from film

--	MAX() - returns maximum value
select max(replacement_cost) from film

--	MIN() - returns minimum value
select min(replacement_cost) from film

--	SUM() - returns the sum of all values
select sum(replacement_cost) from film

--GROUP BY
--allow us to use aggregate columns per some category
--group by syntax:
--		select category_col agg(data_col) from table group by category col

select rating,count(rating) from film group by rating
select customer_id from payment group by customer_id order by customer_id
select customer_id,sum(amount) from payment group by customer_id order by customer_id
select customer_id,sum(amount) from payment group by customer_id order by sum(amount) desc
select customer_id,staff_id,sum(amount) from payment group by staff_id,customer_id
select date(payment_date),sum(amount) from payment group by date(payment_date)
select date(payment_date),sum(amount) from payment group by date(payment_date) order by sum(amount) desc


--challeng no.12
--find out number of payments handled by each staff member
select staff_id,count(*) from payment group by staff_id

--challenge no.13
--to find average replacement cost for each type of movie rating
select rating,avg(replacement_cost) from film group by rating

--challenge no.14
--find out the top 5 customers who spend more amount
select customer_id,sum(amount) from payment group by customer_id order by sum(amount) desc limit 5


--HAVING clause
--allows us to filter data after aplying aggregate function
--filter like WHERE(used before group by) but always used after GROUP BY

select * from payment
select customer_id,sum(amount) from payment where customer_id not in (184,87,477) group by customer_id
select customer_id,sum(amount) from payment group by customer_id having sum(amount)>100

select * from customer
select store_id,count(*) from customer group by store_id
select store_id,count(*) from customer group by store_id having count(*)>300
select store_id,count(customer_id) from customer group by store_id having count(*)>300


--challenge no.15
--select customers with payments 40 or more
select customer_id,count(*) from payment group by customer_id having count(*)>=40

--challenge no.16
--customers who made payments grater than 100$ to sytaff 2
select customer_id,sum(amount) from payment where staff_id = 2 group by customer_id having sum(amount)>100


--Joins

--left join
select film.film_id,title,inventory_id,store_id
from film left join inventory
on inventory.film_id = film.film_id
where inventory.film_id is null

--right join
--same as left join only the tables are switched
--syntax:-
/*	select * from tableA right outer join tableB
	on tableA.col_match = tableB.col_match*/

--challenge
--find out emails of customers live in California
select * from address
select address.district,customer.email from 
customer join address
on customer.address_id = address.address_id
where address.district = 'California'

--challenge
select title,first_name,last_name
from actor  join film_actor on actor.actor_id = film_actor.actor_id join film on film_actor.film_id = film.film_id
----------------------first two tables join------------------------ resulted join is again joined with third table
where actor.first_name = 'Nick' and actor.last_name = 'Wahlberg'