-- Note: I have restructred the database such that the staff, role and skill tables have their own databases
-- the staff_roles and staff_skill tables can be found in the staff database
-- the role_skill table can be found in the role database

-- create Staff_DB
drop schema if exists Staff_DB;
create schema Staff_DB;
use Staff_DB;

-- create staff_details table
create table Staff_DB.staff_details
(Staff_ID int not null primary key,
Staff_FName varchar(50) not null,
Staff_LName varchar(50) not null,
Dept varchar(50) not null,
Email varchar(50) not null,
Phone varchar(20) not null,
Biz_address varchar(255) not null,
Sys_role ENUM('staff', 'hr', 'manager', 'inactive') not null);

-- insert data into staff_details table
INSERT INTO Staff_DB.staff_details VALUES
(001, 'Jacob', 'Scott', 'Sales', 'jacobscott@gmail.com', '+65 1234 5678', '81 VICTORIA STREET, SINGAPORE 123456', 'staff'),
(002, 'Darryl', 'Lee', 'Finance', 'darryllee@gmail.com', '+65 1234 5679', '81 VICTORIA STREET, SINGAPORE 123457', 'staff'),
(003, 'Megan', 'Tan', 'IT', 'megantan@gmail.com', '+65 1234 5680', '81 VICTORIA STREET, SINGAPORE 123458', 'staff'),
(004, 'Jasmine', 'Khoo', 'HR', 'jasminekhoo@gmail.com', '+65 1234 5681', '81 VICTORIA STREET, SINGAPORE 123459', 'hr'),
(005, 'Derek', 'Lim', 'Finance', 'dereklim@gmail.com', '+65 1234 5682', '81 VICTORIA STREET, SINGAPORE 123460', 'manager'),
(006, 'Irene', 'Yeo', 'Sales', 'ireneyeo@gmail.com', '+65 1234 5683', '81 VICTORIA STREET, SINGAPORE 123461', 'manager'),
(007, 'Tiffany', 'Yap', 'HR', 'tiffanyyap@gmail.com', '+65 1234 5684', '81 VICTORIA STREET, SINGAPORE 123462', 'manager'),
(008, 'Daniel', 'Heng', 'IT', 'danielheng@gmail.com', '+65 1234 5685', '81 VICTORIA STREET, SINGAPORE 123463', 'manager');


-- create staff_reporting_officer table
create table Staff_DB.staff_reporting_officer
(Staff_ID int not null,
RO_ID int not null,
constraint staff_reporting_officer_pk primary key (Staff_ID, RO_ID),
constraint staff_reporting_officer_fk foreign key (Staff_ID) references staff_details(Staff_ID),
constraint staff_reporting_officer_fk2 foreign key (RO_ID) references staff_details(Staff_ID));

-- insert data into staff_reporting_officer table
INSERT INTO Staff_DB.staff_reporting_officer VALUES
(001, 006),
(002, 005),
(003, 008),
(004, 007);


-- create staff_roles table
create table Staff_DB.staff_roles
(Staff_ID int not null,
Staff_Role int not null,
Role_Type ENUM('primary', 'secondary') not null,
SR_status ENUM('active', 'inactive') not null,
constraint staff_roles_pk primary key (Staff_ID, Staff_Role),
constraint staff_roles_fk foreign key (Staff_ID) references staff_details(Staff_ID)
-- constraint staff_roles_fk2 foreign key (Staff_Role) references role_details(Role_ID)
);

-- insert data into staff_roles table
INSERT INTO Staff_DB.staff_roles VALUES
(001, 002, "primary", "active"),
(001, 014, "secondary", "active"),
(002, 014, "primary", "active"),
(003, 015, "primary", "active"),
(004, 010, "primary", "active"),
(005, 013, "primary", "active"),
(006, 001, "primary", "active"),
(007, 020, "primary", "active"),
(008, 022, "primary", "active");


-- create staff_skill table
-- Note: I did not add a constraint for SS_Status because I'm assuming it's possible for a staff to have
-- an inactive skill while the skill itself is listed as active in skill details. For instance, if the
-- staff's listed skill is no longer seen as valid by HR or management. Will clarify with prof.
create table Staff_DB.staff_skill
(Staff_ID int not null,
Skill_ID int not null,
SS_Status ENUM('active', 'unverified', 'in-progress') not null,
constraint staff_skill_pk primary key (Staff_ID, Skill_ID),
constraint staff_skill_fk foreign key (Staff_ID) references staff_details(Staff_ID)
-- constraint staff_skill_fk2 foreign key (Skill_ID) references skill_details(Skill_ID)
);

-- insert data into staff_skill table
-- Note: Only came up with data for the first 3 staff members, please feel free to add more if needed
INSERT INTO Staff_DB.staff_skill VALUES
(001, 001, 'active'),
(001, 002, 'active'),
(001, 003, 'active'),
(001, 004, 'active'),
(001, 005, 'active'),
(001, 006, 'active'),
(001, 007, 'active'),
(001, 008, 'active'),
(001, 011, 'active'),
(001, 009, 'unverified'),
(001, 010, 'unverified'),
(002, 001, 'active'),
(002, 002, 'active'),
(002, 003, 'active'),
(002, 008, 'active'),
(002, 009, 'active'),
(002, 010, 'active'),
(003, 001, 'active'),
(003, 002, 'active'),
(003, 003, 'active'),
(003, 004, 'active'),
(003, 005, 'active'),
(003, 006, 'active'),
(003, 011, 'active');


-- create Role_DB
drop schema if exists Role_DB;
create schema Role_DB;
use Role_DB;

-- create role_details table
create table Role_DB.role_details
(Role_ID int not null primary key,
Role_Name varchar(50) not null,
Role_Desc varchar(50000) not null,
Role_Status ENUM('active', 'inactive') not null);

-- insert data into role_details table
-- Not sure if we needed to include directorial roles but I added them in anyway
INSERT INTO Role_DB.role_details VALUES
(001, 'Sales Manager', 'Provides leadership to the sales team. Motivates and encourages sales team to ensure quotas are met. Reviews and analyzes sales and operational records and reports; uses data to project sales, determine profitability and targets, and identify potential new markets.', 'active'),
(002, 'Sales Account Manager', "Serves as the liason between the Allinone and its customers. Addresses customers' needs and concerns as quickly and effectively as possible to develop and maintain strong relationships.", 'active'),
(003, 'Admin Team', 'Provides administrative support to the employees of Allinone. Duties may include fielding telephone calls, receiving and directing visitors, word processing, creating spreadsheets and presentations, and filing.', 'active'),
(004, 'System Solutioning Developer', '...', 'active'),
(005, 'System Solutioning Support Team', '...', 'active'),
(006, 'Senior Engineer', 'Designs, tests, maintains and repairs the equipment and processes used in production and other industries. Also provides guidance to junior Engineers.', 'active'),
(007, 'Junior Engineer', 'Designs, tests, maintains and repairs the equipment and processes used in production and other industries.', 'active'),
(008, 'Call Centre Agent', '...', 'active'),
(009, 'Operation Planning Team', '...', 'active'),
(010, 'Human Resource Team', '...', 'active'),
(011, 'Learning and Development Team', '...', 'active'),
(012, 'Consultant', 'Advises our clients about their options, and help them find ways to utilize print solutions to reach their goals and managing their jobs throughout the production process.', 'active'),
(013, 'Finance Manager', '...', 'active'),
(014, 'Finance Excecutive', '...', 'active'),
(015, 'Information Technology Team', '...', 'active'),
(016, 'Sales Director', '...', 'active'),
(017, 'Consultancy Division Director', '...', 'active'),
(018, 'System Solutioning Director', '...', 'active'),
(019, 'Engineering Operation Division Director', '...', 'active'),
(020, 'Human Resources and Admin Director', '...', 'active'),
(021, 'Finance Director', '...', 'active'),
(022, 'Information Technology Director', '...', 'active'),
(023, 'Moral Support Professional', '...', 'inactive');


-- create role_skill table
create table Role_DB.role_skill
(Role_ID int not null,
Skill_ID int not null,
constraint role_skill_pk primary key (Role_ID, Skill_ID),
constraint role_skill_fk foreign key (Role_ID) references role_details(Role_ID)
-- constraint role_skill_fk2 foreign key (Skill_ID) references skill_details(Skill_ID)
);

-- insert data into role_skill table
-- Note: I only came up with data for the first 5 roles, please feel free to add more if needed
INSERT INTO Role_DB.role_skill VALUES
(001, 007),
(001, 008),
(001, 011),
(001, 013),
(002, 007),
(002, 008),
(002, 011),
(003, 001),
(003, 002),
(003, 003),
(004, 004),
(004, 005),
(004, 006),
(004, 012),
(005, 004),
(005, 005),
(005, 006),
(005, 012);


-- create Skill_DB
drop schema if exists Skill_DB;
create schema Skill_DB;
use Skill_DB;


-- create skill_details table
create table Skill_DB.skill_details
(Skill_ID int not null primary key,
Skill_Name varchar(50) not null,
Skill_Status ENUM('active', 'inactive') not null);

-- insert data into skill_details table
-- Note: please feel free to add to the list of skills if needed
INSERT INTO Skill_DB.skill_details VALUES
(001, 'Word', 'active'),
(002, 'Excel', 'active'),
(003, 'Powerpoint', 'active'),
(004, 'Java', 'active'),
(005, 'C++', 'active'),
(006, 'Python', 'active'),
(007, 'Marketing', 'active'),
(008, 'Accounting', 'active'),
(009, 'Fiancial Analysis', 'active'),
(010, 'Financial Auditing', 'active'),
(011, 'Customer Relationship Management', 'active'),
(012, 'Content Creation', 'active'),
(013, 'Team Leadership', 'active');



-- create role_listing DB
drop schema if exists role_listing_DB;
create schema role_listing_DB;
use role_listing_DB;

-- create role_listing table
-- Note: Role_Listing_Source = Hiring Manager
-- Note: Country and Career_Level are not required by the technical_doc, I added them because they were
-- in the front-end draft
-- Note: When a role listing has not been updated since its posting, use Role_Listing_Updater = 000 and
-- a blank string for Role_Listing_ts_update
create table role_listing_DB.role_listings
(Role_Listing_ID int not null auto_increment primary key,
Role_ID int not null,
Role_Listing_Desc varchar(50000) not null,
Role_Listing_Source int not null,
Role_Listing_Open date not null,
Role_Listing_Close date not null,
Role_Listing_Creator int not null,
Role_Listing_ts_create timestamp default current_timestamp,
-- Country varchar(50) not null,
-- Career_Level ENUM('Entry', 'Intermediate', 'First-level Mgmt', 'Middle-level Mgmt', 'Senior Mgmt') not null,
Role_Listing_Updater int,
Role_Listing_ts_update timestamp default current_timestamp);

-- insert data into role_listings table
INSERT INTO role_listing_DB.role_listings VALUES
-- (001, 002, 'Responsibilities for this role include:', 006, '2023-09-01', '2024-02-01', 003, timestamp("2023-09-01"), 'Malaysia', 'Entry', 003, timestamp("2023-09-05")),
-- (002, 014, 'Responsibilities for this role include:', 005, '2023-09-01', '2024-02-01', 003, timestamp("2023-09-01"), 'Malaysia', 'Entry', 003, timestamp("2023-09-02")),
-- (003, 015, 'Responsibilities for this role include:', 008, '2023-09-01', '2024-02-01', 003, timestamp("2023-09-01"), 'Malaysia', 'Entry', 000, '');

(001, 002, 'Responsibilities for this role include:', 006, '2023-09-01', '2024-02-01', 003, timestamp("2023-09-01"), 003, timestamp("2023-09-05")),
(002, 014, 'Responsibilities for this role include:', 005, '2023-09-01', '2024-02-01', 003, timestamp("2023-09-01"), 003, timestamp("2023-09-02")),
(003, 015, 'Responsibilities for this role include:', 008, '2023-09-01', '2024-02-01', 003, timestamp("2023-09-01"), 000, '');

-- create candidate table
create table role_listing_DB.candidates
(candidate_id int not null,
role_listing_id int not null,
constraint candidate_pk primary key (candidate_id, role_listing_id),
constraint candidate_fk foreign key (role_listing_id) references role_listings(Role_Listing_ID));

-- insert data into candidates table
INSERT INTO role_listing_DB.candidates VALUES
(001, 002),
(002, 001),
(003, 001);


-- create application_DB
drop schema if exists application_DB;
create schema application_DB;
use application_DB;

-- -- create application table
-- create table application_DB.role_application
-- (role_app_id int not null auto_increment primary key,
-- role_listing_id int not null,
-- staff_id int not null,
-- role_app_status ENUM('applied', 'withdrawn') not null,
-- role_app_ts_create timestamp default current_timestamp);

-- -- insert data into role_application table
-- INSERT INTO application_DB.role_application VALUES
-- (001, 002, 001, 'applied', timestamp("2023-09-27")),
-- (002, 001, 002, 'applied', timestamp("2023-09-27")),
-- (003, 001, 003, 'applied', timestamp("2023-09-27"));

-- create application table
create table application_DB.role_application
(role_app_id int not null auto_increment primary key,
role_listing_id int not null,
staff_id int not null,
role_app_status ENUM('applied', 'withdrawn') not null,
role_app_ts_create timestamp default current_timestamp,
reason_for_application varchar(50000));

-- insert data into role_application table
INSERT INTO application_DB.role_application VALUES
(001, 002, 001, 'applied', timestamp("2023-09-27"), 'I am interested in this role because...'),
(002, 001, 002, 'applied', timestamp("2023-09-27"), 'I am interested in this role because...'),
(003, 001, 003, 'applied', timestamp("2023-09-27"), 'I am interested in this role because...');
