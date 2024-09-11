create database final_project;

create table final_project.client (
    id int primary key auto_increment,
    name varchar(30) not null ,
    family varchar(30) not null ,
    birth_date date ,
    gender varchar(20) not null ,
    nationality varchar(30) not null ,
    national_id int not null unique
);
create table final_project.room(
    id int primary key auto_increment,
    bed varchar(5) not null ,
    tv varchar(5) not null ,
    refrigerator varchar(5) not null ,
    room_service varchar(5) not null ,
    kitchen varchar(5) not null ,
    phone varchar(5) not null

);
alter table final_project.client add column start_date date;
alter table final_project.client add column end_date date;