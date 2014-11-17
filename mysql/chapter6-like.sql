-- 用通配符进行过滤
-- 要在搜索中使用通配符，必须使用 LIKE 操作符
-- % 表示任何字符出现任意次数, % 不会匹配NULL
SELECT prod_id, prod_name FROM Products WHERE prod_name LIKE 'Fish%';
SELECT prod_id, prod_name FROM Products WHERE prod_name LIKE '%bean bag%';
SELECT prod_id, prod_name FROM Products WHERE prod_name LIKE 'F%y';

-- _通配符，它值匹配单个字符，
SELECT prod_id, prod_name FROM Products WHERE prod_name LIKE '__ inch teddy bear';

-- [] 通配符用来指定字符集，必须匹配指定位置的一个字符, mysql 只能通过正则表达式来
SELECT cust_contact FROM Customers WHERE cust_contact LIKE '[JM]%' ORDER BY cust_contact;
SELECT cust_contact FROM Customers WHERE cust_contact REGEXP '^[JM]' ORDER BY cust_contact; -- MYSQL用法

-- 可以使用 ^ 来表示取反
SELECT cust_contact FROM Customers WHERE cust_contact LIKE '^[JM]%' ORDER BY cust_contact;