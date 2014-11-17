-- insert 完整的行
-- INSERT INTO Customers VALUES('1000000006','Toy Land','123 Any Street','New York','NY','1111','USA',NULL,NULL);
-- 一种比上面语句更安全的做法：
-- INSERT INTO Customers(cust_id,cust_name,cust_address,cust_city,cust_state,cust_zip,cust_country,cust_contact,cust_email) VALUES('1000000006','Toy Land','123 Any Street','New York','NY','1111','USA',NULL,NULL);
-- 上面这种写法，可以只提供某些列的值

-- 将一个表合并到另一个表中
-- INSERT INTO Customers(cust_id,cust_contact,cust_email,cust_name,cust_address,cust_city,cust_state,cust_zip,cust_country)
--	SELECT cust_id,cust_contact,cust_email,cust_name,cust_address,cust_city,cust_state,cust_zip,cust_country FROM CustNew;

-- 将一个表内容复制到一个全新的表（运行中创建的表），使用 SELECT INTO
-- SELECT * INTO CustCopy FROM Customers;
-- MYSQL用法如下
CREATE TABLE CustCopy AS SELECT * FROM Customers;