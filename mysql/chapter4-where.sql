-- 使用where子句
SELECT prod_name, prod_price FROM Products WHERE prod_price = 3.49;

-- WHERE子句操作符：=,<>,!=,<,<=,!<,>,>=,!>,BETWEEN,IS NULL
SELECT prod_name, prod_price FROM Products WHERE prod_price < 10;
SELECT prod_name, prod_price FROM Products WHERE prod_price <= 10;

-- 不匹配检查, 不是所有的DBMS都支持 <> 和 !=
SELECT vend_id, prod_name FROM Products WHERE vend_id <> 'DLL01';
SELECT vend_id, prod_name FROM Products WHERE vend_id != 'DLL01';

-- 范围检查
SELECT prod_name, prod_price FROM Products WHERE prod_price BETWEEN 5 AND 10;

-- 空值检查
SELECT *FROM Customers;
SELECT cust_name, cust_email FROM CUSTOMERS WHERE cust_email IS NULL;