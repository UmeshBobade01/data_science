--assesment

--Question 1
select customer_id,sum(amount) from payment where staff_id = 2 group by customer_id having sum(amount)>110

--Question 2
select count(*) from film where title ilike 'j%'

--Question 3
select customer_id from customer where first_name like 'E%' and address_id<500 order by customer_id desc limit 1
