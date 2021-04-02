drop database employee;
create database employee;
use employee;
create table employee(id int,salary float,location varchar(255));
insert into employee values(1,100,"Bengaluru");
insert into employee values(2,200,"Bezawada");
insert into employee values(3,300,"Chennai");

drop database datawarehouse;
use datawarehouse;
create table datawarehouse(id_1 int,salary_1 float,location_1 varchar(255));


