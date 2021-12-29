drop table if exists books;
drop table if exists customers;
drop table if exists sales;
drop view if exists sales_view;

create table books(
   id integer not null primary key,
   title varchar(50),
   author varchar(50),
   isbn varchar(14),
   price decimal(10,2)
);
create table customers(
   id integer not null primary key,
   first_name varchar(20),
   last_name varchar(30),
   sex char(1)
);
create table sales(
   id integer not null primary key,
   book_id integer references books(id),
   customer_id integer references customers(id)
);

insert into books (title,author,isbn,price) values
   ('The Cat in the Hat','Dr. Seuss','978-0375834929',5.47);
insert into books (title,author,isbn,price) values
   ('Green Eggs and Ham','Dr. Seuss','978-0375834950',6.83);
insert into books (title,author,isbn,price) values
   ('Go, Dog Go','P.D. Eastman','978-0394800202',8.16);
insert into books (title,author,isbn,price) values
   ('Prey','Michael Crichton','978-0061703089',8.69);
insert into books (title,author,isbn,price) values
   ('State of Fear','Michael Crichton','978-0061782664',8.86);
   
insert into customers (first_name,last_name,sex) values
   ('Jane','Doe','f');
insert into customers (first_name,last_name,sex) values
   ('John','Doe','m');
insert into customers (first_name,last_name,sex) values
   ('Bill','Gates','m');
insert into customers (first_name,last_name,sex) values
   ('Ada','Lovelace','f');
   
create view sales_view as
   select books.id as book_id, books.title, books.author,
   books.isbn, books.price, customers.id as customer_id,
   customers.first_name, customers.last_name,
   customers.sex, sales.id as sales_id from
   books join sales on books.id=sales.book_id
   join customers on sales.customer_id=customers.id;
   
insert into sales (book_id,customer_id) values (1,1);
insert into sales (book_id,customer_id) values (3,1);
insert into sales (book_id,customer_id) values (4,1);
insert into sales (book_id,customer_id) values (1,2);
insert into sales (book_id,customer_id) values (2,2);
insert into sales (book_id,customer_id) values (5,2);
insert into sales (book_id,customer_id) values (1,3);
insert into sales (book_id,customer_id) values (2,3);
insert into sales (book_id,customer_id) values (5,3);
insert into sales (book_id,customer_id) values (2,4);
insert into sales (book_id,customer_id) values (3,4);
insert into sales (book_id,customer_id) values (4,4);
insert into sales (book_id,customer_id) values (5,4);
