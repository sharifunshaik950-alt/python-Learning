--customers
create table customers(customerid int primary key,
customername varchar(100) not null,
email varchar (100) not null,
city varchar(50) not null,
registrationdate date not null);
  
  --products--
  create table products(productid int primary key,
  productname varchar(50) not null,
  category varchar (50) not null,
  unitprice decimal(10,2) not null,
  stockquantity int not null);

  --orders--
create table orders(orderid int primary key,
customerid int,
orderdate date not null,
orderstatus varchar(50) not null,
 foreign key (customerid) references customers (customerid));

 --orderdetails--
 create table orderdetails(orderdetailid int primary key,
 orderid int,
 productid int,
 quality varchar(50) not null,
 unitprice decimal(10,2) not null,
 foreign key (orderid) references orders (orderid),
 foreign key (productid) references products (productid));

 ---part2--
 insert into customers values(1,'raju','raju@gmail.com','hydrabad','2001-jan-1');
 insert into customers values(2,'ravi','ravi@gmail.com','benguluru','2002-feb-4');
 insert into customers values(3,'raju','raju@gmail.com','hydrabad','2001-jan-1');
 insert into customers values(4,'raju','raju@gmail.com','hydrabad','2001-jan-1');
 insert into customers values(5,'raju','raju@gmail.com','hydrabad','2001-jan-1');
 insert into customers values(6,'raju','raju@gmail.com','hydrabad','2001-jan-1');
 insert into customers values(7,'raju','raju@gmail.com','hydrabad','2001-jan-1');
 insert into customers values(8,'raju','raju@gmail.com','hydrabad','2001-jan-1');
 insert into customers values(9,'raju','raju@gmail.com','hydrabad','2001-jan-1');
 insert into customers values(10,'raju','raju@gmail.com','hydrabad','2001-jan-1');
 insert into customers values(11,'raju','raju@gmail.com','hydrabad','2001-jan-1');
 select * from customers;
 delete from customers;
 
 insert into customers values(1,'raju','raju@gmail.com','hydrabad','2001-jan-1');
 insert into customers values(2,'giri','girigmail.com','benguluru','2005-jun-3');
 insert into customers values(3,'somu','somugmail.com','pune','2006-dec-10');
insert into customers values(4,'raji','rajigmail.com','maharastra','2015-may-19');
insert into customers values(5,'sanju','sanjugmail.com','mubai','2018-april-15');
insert into customers values(6,'kirthi','kirthigmail.com','delhi','2010-mar-9');
insert into customers values(7,'ramu','ramugmail.com','gujarat','2004-feb-17');
insert into customers values(8,'manju','manjugmail.com','kerala','2000-jan-5');
insert into customers values(9,'manu','manugmail.com','tirupati','2016-oct-20');
insert into customers values(10,'sonu','sonugmail.com','channai','2007-july-30');
insert into customers values(11,'muni','munigmail.com','vizag','2021-dec-20');
insert into customers values(12,'monu','monugmail.com','vijayawada','2022-oct-9');
insert into customers values(13,'pandu','pandugmail.com','addanki','2017-july-25');
insert into customers values(14,'roja','rojagmail.com','narasaraopeta','2012-jun-15');
insert into customers values(15,'mari','marigmail.com','channai','2007-july-30');
select* from customers;
 

 insert into products values(101,'smartphone','electronic',15000,30); 
 insert into products values(102,'laptop','electronic',55000,20);
 insert into products values(103,'tv','electronic',10000,10);
 insert into products values(104,'smartwatch','electronic',12000,15);
 insert into products values(105,'headphones','electronic',15000,200);

insert into products values(106,'dress','appreal',1000,200);
insert into products values(107,'kurtha','appreal',1500,400);
insert into products values(108,'jacket','appreal',5000,200);
insert into products values(109,'frogs','appreal',1500,30);  
insert into products values(110,'lahanga','appreal',6000,100);

insert into products values(111,'sofa','home',5000,100);
insert into products values(112,'dainingtable','home',18000,150);
insert into products values(113,'dressingtable','home',7000,70);
insert into products values(114,'doublekhat','home',35000,40);
insert into products values(115,'chair','home',2500,80);

insert into products values(116,'pondscream','beauty',100,40);
insert into products values(117,'perfum','beauty',200,50);
insert into products values(118,'facewash','beauty',300,100);
insert into products values(119,'bodyloation','beauty',150,60);
insert into products values(120,'shampoo','beauty',500,300);
select * from products;

 INSERT INTO Orders VALUES (1,1,'2024-05-01','Completed');
INSERT INTO Orders VALUES (2,2,'2024-05-02','Completed');
INSERT INTO Orders VALUES (3,3,'2024-05-03','Pending');
INSERT INTO Orders VALUES (4,4,'2024-05-04','Completed');
INSERT INTO Orders VALUES (5,5,'2024-05-05','Cancelled');
INSERT INTO Orders VALUES (6,6,'2024-05-06','Completed');
INSERT INTO Orders VALUES (7,7,'2024-05-07','Pending');
INSERT INTO Orders VALUES (8,8,'2024-05-08','Completed');
INSERT INTO Orders VALUES (9,9,'2024-05-09','Completed');
INSERT INTO Orders VALUES (10,10,'2024-05-10','Pending');
INSERT INTO Orders VALUES (11,11,'2024-05-11','Completed');
INSERT INTO Orders VALUES (12,12,'2024-05-12','Completed');
INSERT INTO Orders VALUES (13,13,'2024-05-13','Pending');
INSERT INTO Orders VALUES (14,14,'2024-05-14','Completed');
INSERT INTO Orders VALUES (15,15,'2024-05-15','Completed');

 select count (*) as  totalorderds from orders;
 INSERT INTO Orders VALUES (16,1,'2024-05-16','Completed');
INSERT INTO Orders VALUES (17,2,'2024-05-17','Completed');
INSERT INTO Orders VALUES (18,3,'2024-05-18','Completed');
INSERT INTO Orders VALUES (19,4,'2024-05-19','Pending');
INSERT INTO Orders VALUES (20,5,'2024-05-20','Completed');
INSERT INTO Orders VALUES (21,6,'2024-05-21','Completed');
INSERT INTO Orders VALUES (22,7,'2024-05-22','Completed');
INSERT INTO Orders VALUES (23,8,'2024-05-23','Pending');
INSERT INTO Orders VALUES (24,9,'2024-05-24','Completed');
INSERT INTO Orders VALUES (25,10,'2024-05-25','Completed');
INSERT INTO Orders VALUES (26,11,'2024-05-26','Pending');
INSERT INTO Orders VALUES (27,12,'2024-05-27','Completed');
INSERT INTO Orders VALUES (28,13,'2024-05-28','Completed');
INSERT INTO Orders VALUES (29,14,'2024-05-29','Completed');
INSERT INTO Orders VALUES (30,15,'2024-05-30','Pending');


--part3--
UPDATE Products
SET UnitPrice = UnitPrice + (UnitPrice * 15/100)
WHERE Category='electronics';


 select distinct Category
from Products;

UPDATE Products
SET UnitPrice = UnitPrice + (UnitPrice * 15/100)
WHERE Category='electronic';








