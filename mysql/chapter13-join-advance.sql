-- 使用表的别名
SELECT cust_name, cust_contact FROM Customers AS C, Orders AS O, OrderItems AS OI
	WHERE C.cust_id = O.cust_id AND OI.order_num = O.order_num AND prod_id = 'RGAN01';
    
-- 自联结
-- 例如要给Jim 同一公司的所有顾客发送一封信件。
-- 使用子查询实现
SELECT cust_id, cust_name, cust_contact FROM Customers WHERE cust_name = (
	SELECT cust_name FROM Customers WHERE cust_contact = 'Jim Jones');
-- 使用联结
SELECT c1.cust_id, c1.cust_name, c1.cust_contact FROM Customers AS c1, Customers AS c2
	WHERE c1.cust_name = c2.cust_name AND c2.cust_contact = 'Jim Jones';
    
-- 自然联结
SELECT c.*, o.order_num, o.order_date, oi.prod_id, oi.quantity, oi.item_price
	FROM Customers AS c, Orders AS o, OrderItems AS oi 
		WHERE c.cust_id = o.cust_id AND oi.order_num = o.order_num AND prod_id = 'RGAN01';
        
-- 外联结，使用关键字：OUTER JOINI...ON,联结包含了那些在相关表中没有关联行的行，叫外联结
-- 一般的内联结语法
SELECT Customers.cust_id, Orders.order_num FROM Customers INNER JOIN Orders
	ON Customers.cust_id = Orders.cust_id;
-- 外联结写法，必须使用LEFT或者RIGHT，表示关联左边或者右边的所有行
SELECT Customers.cust_id, Orders.order_num FROM Customers LEFT OUTER JOIN Orders
	ON Customers.cust_id = Orders.cust_id;
SELECT Customers.cust_id, Orders.order_num FROM Customers RIGHT OUTER JOIN Orders
	ON Orders.cust_id = Customers.cust_id;
    
-- 使用带聚集函数的联结
SELECT Customers.cust_id, COUNT(Orders.order_num) AS num_ord FROM Customers INNER JOIN Orders
	ON Customers.cust_id = Orders.cust_id GROUP BY Customers.cust_id;
    
SELECT Customers.cust_id, COUNT(Orders.order_num) AS num_ord FROM Customers LEFT OUTER JOIN Orders
	ON Customers.cust_id = Orders.cust_id GROUP BY Customers.cust_id;
