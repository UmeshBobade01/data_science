--		SQL exercise 1		--


--Q1. How can you retrieve all the information from the cd.facilities table?

select * from cd.facilities


--Q2. You want to print out a list of all of the facilities and their cost to members.
--	  How would you retrieve a list of only facility names and costs?

select name,membercost from cd.facilities


--Q3. How can you produce a list of facilities that charge a fee to members?

select name,membercost from cd.facilities where membercost>0


--Q4. How can you produce a list of facilities that charge a fee to members, and that fee is less than 1/50th of the monthly maintenance cost?
--    Return the facid, facility name, member cost, and monthly maintenance of the facilities in question.

select facid,name,membercost,monthlymaintenance from cd.facilities where membercost<0.02*monthlymaintenance and membercost>0


--Q5. How can you produce a list of all facilities with the word 'Tennis' in their name?

select * from cd.facilities where name ilike '%tennis%'


--Q6. How can you retrieve the details of facilities with ID 1 and 5? Try to do it without using the OR operator.

select * from cd.facilities where facid in (1,5)


--Q7. How can you produce a list of members who joined after the start of September 2012?
--	  Return the memid, surname, firstname, and joindate of the members in question.

select * from cd.members
select memid,surname,firstname,joindate from cd.members where joindate >= '2012-09-01'


--Q8. How can you produce an ordered list of the first 10 surnames in the members table? The list must not contain duplicates.

select distinct(surname) from cd.members order by surname limit 10


--Q9. You'd like to get the signup date of your last member. How can you retrieve this information?

select max(joindate) from cd.members


--Q10. Produce a count of the number of facilities that have a cost to guests of 10 or more.

select count(*) from cd.facilities where guestcost > 10


--Q11. Produce a list of the total number of slots booked per facility in the month of September 2012.
--	   Produce an output table consisting of facility id and slots, sorted by the number of slots.

select * from cd.bookings
select facid,sum(slots) as Total_slots from cd.bookings where starttime >= '2012-09-01' group by facid order by Total_slots


--Q12. Produce a list of facilities with more than 1000 slots booked.
--	   Produce an output table consisting of facility id and total slots, sorted by facility id.

select facid,sum(slots) from cd.bookings group by facid having sum(slots)>1000 order by facid

--Q13. How can you produce a list of the start times for bookings for tennis courts, for the date '2012-09-21'?
--	   Return a list of start time and facility name pairings, ordered by the time.

select cd.bookings.starttime,cd.facilities.name
from cd.facilities join cd.bookings
on cd.facilities.facid = cd.bookings.facid
where cd.facilities.name like 'Tennis Court%' and date(cd.bookings.starttime) = '2012-09-21'
order by starttime


--Q14. How can you produce a list of the start times for bookings by members named 'David Farrell'?

select cd.bookings.starttime
from cd.bookings join cd.members
on cd.members.memid = cd.bookings.memid
where cd.members.firstname = 'David' and cd.members.surname = 'Farrell'
