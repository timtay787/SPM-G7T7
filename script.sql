-- create SBRP_DB
drop schema if exists SBRP_DB;
create schema SBRP_DB;
use SBRP_DB;

-- create staff table
-- 0 = staff, 1 = HR, 2 = manager/director
create table SBRP_DB.staff
(Staff_ID int not null primary key,
Staff_FName varchar(50) not null,
Staff_LName varchar(50) not null,
Dept varchar(50) not null,
Country varchar(50) not null,
Email varchar(50) not null,
Access_Rights int not null);

-- insert data into staff table
INSERT INTO SBRP_DB.staff VALUES
(001, 'Jacob', 'Scott', 'Sales', 'Malaysia', 'jacobscott@gmail.com', 0),
(002, 'Darryl', 'Lee', 'Finance', 'Malaysia', 'darryllee@gmail.com', 0),
(003, 'Megan', 'Tan', 'IT', 'Malaysia', 'megantan@gmail.com', 0),
(004, 'Jasmine', 'Khoo', 'HR', 'Malaysia', 'jasminekhoo@gmail.com', 1),
(005, 'Derek', 'Tan', 'Sales', 'Malaysia', 'derektan@gmail.com', 2);


-- create role_skill table
create table SBRP_DB.role_skill
(Role_Name varchar(20) not null,
Skill_Name varchar(50) not null,
constraint role_skill_pk primary key (Role_Name, Skill_Name));

-- insert data into role_skill table
INSERT INTO SBRP_DB.role_skill VALUES
('Engin. Op. Planning', 'Electrical/Mechanical Engineering'),
('Account Manager', 'Accounting'),
('Account Manager', 'Marketing'),
('Account Manager', 'Customer Relationship Management'),
('IT Team', 'Java'),
('IT Team', 'C++'),
('IT Team', 'Python'),
('Finance Executive', 'Financial Analysis'),
('Finance Executive', 'Financial Auditing'),
('Finance Executive', 'Accounting'),
('Finance Executive', 'Excel'),
('HR Admin Team', 'Word'),
('HR Admin Team', 'Powerpoint'),
('HR Admin Team', 'Excel');


-- create staff_skill table
create table SBRP_DB.staff_skill
(Staff_ID int not null,
Skill_Name varchar(50) not null,
constraint staff_skill_pk primary key (Staff_ID, Skill_Name),
constraint staff_skill_fk foreign key (Staff_ID) references staff(Staff_ID));

-- insert data into staff_skill table
INSERT INTO SBRP_DB.staff_skill VALUES
(001, 'Word'),
(001, 'Powerpoint'),
(001, 'Excel'),
(001, 'Java'),
(001, 'C++'),
(001, 'Python'),
(001, 'Accouting'),
(001, 'Customer Relationship Management'),
(001, 'Marketing'),
(002, 'Word'),
(002, 'Powerpoint'),
(002, 'Excel'),
(002, 'Financial Analysis'),
(002, 'Financial Auditing'),
(002, 'Accounting'),
(003, 'Java'),
(003, 'C++'),
(003, 'Python'),
(003, 'Word'),
(003, 'Powerpoint'),
(003, 'Excel'),
(003, 'Electrical/Mechanical Engineering');