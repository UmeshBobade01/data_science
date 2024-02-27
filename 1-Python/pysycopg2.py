""" connecting python to database using psycopg2"""

#psycopg2 is used to establish connection between PostgreSQL database to the python
import psycopg2 as pg

#to establish connection first create connection function
conn = pg.connect(database="dvdrental",user="postgres",host="localhost",password="1710",port=5432)

#cursor method is used to perform difeerent operation on table like SELECT,INSERT,UPDATE,DELETE,CREATE
cur = conn.cursor()

#pass in a postgreSQL query as a string
cur.execute("select * from payment")

#fetch the first record
cur.fetchone()

#fetch any number of records
cur.fetchmany(100)

#to fetch all records
cur.fetchall()

#
data = cur.fetchmany(10)

#close the connection
conn.commit()

#close cursor
cur.close()

###########################################################################

#create table courses in database testme
conn = pg.connect(database="testme",user="postgres",password="1710")
cur = conn.cursor()

#creating table
cur.execute("""create table courses(course_id serial primary key,
            course_name varchar(50) unique not null,
            instructor varchar(50) not null,
            topic varchar(50) not null)""")

conn.commit()
cur.close()

###########################################################################

#inseerting values into table
import psycopg2 as pg
conn = pg.connect(database="testme",user="postgres",password="1710")
cur = conn.cursor()


cur.execute("""insert into courses(course_name,instructor,topic)
            values ('Introduction to SQL','Ram','Julia'),
            ('Analysing survey data in Python','Sham','Python'),
            ('Introduction to ChatGPT','Ganesh','Theory'),
            ('Introduction to statistics in R','Ramesh','R'),
            ('Hypothesis Testing in Python','Jayesh','Python')""")


conn.commit()
cur.close()

###########################################################################

#selecting rows of table by storing in other variable

#establish connection
conn = pg.connect(database="testme",user="postgres",password="1710")
cur = conn.cursor()

#fetch records
cur.execute("select * from courses")
rows = cur.fetchall()

#close connection and cursor
conn.commit()
cur.close()

#display
for i in rows:
    print(i)

###########################################################################

#no of courses teach by each instructor
conn = pg.connect(database="testme",user="postgres",password="1710")
cur = conn.cursor()

cur.execute("select instructor,count(*) from courses group by instructor")
rows = cur.fetchall()

conn.commit()
cur.close()

for i in rows:
    print(i)

###########################################################################

#select records order by course instructor
conn = pg.connect(database="testme",user="postgres",password="1710")
cur = conn.cursor()

cur.execute("select * from courses order by instructor")
rows = cur.fetchall()

conn.commit()
cur.close()

for i in rows:
    print(i)

###########################################################################

#create table
conn = pg.connect(database="testme",user="postgres",password="1710")
cur = conn.cursor()

cur.execute("""create table courses1(course_id integer,
            course_duration varchar(50) not null,
            course_fees integer not null,
            course_admin varchar(50) not null,
            foreign key (course_id) references courses(course_id))""")

conn.commit()
cur.close()

#insert records
conn = pg.connect(database="testme",user="postgres",password="1710")
cur = conn.cursor()

cur.execute("""insert into courses1(course_id,course_duration,course_fees,course_admin)
            values (1,'30 days',10000,'umesh'),
            (2,'20 days',15000,'yash'),
            (3,'40 days',25000,'umesh'),
            (4,'25 days',12000,'tejax'),
            (5,'15 days',7000,'yash')""")

conn.commit()
cur.close()

#fetching records using group by clause

conn = pg.connect(database="testme",user="postgres",password="1710")
cur = conn.cursor()

cur.execute("""select course_name,instructor,course_duration,course_fees
            from courses join courses1
            on courses.course_id = courses1.course_id""")

rows = cur.fetchall()
conn.commit()
cur.close()

#display records
for i in rows:
    print(i)

######################################################################