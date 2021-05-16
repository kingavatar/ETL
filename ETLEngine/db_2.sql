drop database if exists employee;
create database employee;
use employee;
create table employee(id int,salary float,location varchar(255));
insert into employee values(1,100,"Bengaluru");
insert into employee values(2,200,"Bezawada");
insert into employee values(3,300,"Chennai");
create table manager(id int,super_id int,name varchar(255));
insert into manager values(1,1,"m1");
insert into manager values(2,2,"m2");
insert into manager values(3,3,"m3");
create table query(id int);

drop database if exists datawarehouse;
create database if not exists datawarehouse;
use datawarehouse;
create table datawarehouse(id_1 int,salary_1 float,location_1 varchar(255));
create table datawarehouse1(id_1 int,salary_1 float,location_1 varchar(255),name_1 varchar(255));

drop database if exists airbase;
create database airbase;
create table temp(id int);
