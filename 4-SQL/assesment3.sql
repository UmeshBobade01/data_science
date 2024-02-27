--assesment 3
--create teacher table
create table teachers(teacher_id serial primary key, first_name varchar(50) not null, last_name varchar(50) not null,
homeroom_number int, department varchar(50) not null, email varchar(50) unique not null, phone varchar(50) unique not null)
select * from teachers

--create student table
create table students(student_id serial primary key, first_name varchar(50) not null, last_name varchar(50) not null,
homeroom_number int, phone varchar(50) unique not null, email varchar(50) unique not null, graduation_year varchar(50) not null)
select * from students

--insert value into teachers table
insert into teachers(first_name,last_name,homeroom_number, department, email, phone)
values ('Chandrashekhar','Gogte',5,'Biology','Chandrashekhar.gogte@gmail.com','7775554321')
select * from teachers

--insert value into students table
insert into students(first_name,last_name,homeroom_number,email, phone,graduation_year)
values ('Rahul','Galande',5,'Rahul.galande@gmail.com','7775554321','2023')
select * from students


alter table students drop column homeroom_number
alter table teachers drop column homeroom_number