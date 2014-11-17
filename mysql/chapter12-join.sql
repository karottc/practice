-- 可以用WHERE 来表示联结
SELECT vend_name, prod_name, prod_price FROM Vendors, Products WHERE Vendors.vend_id = Products.vend_id;
-- 上面这种方式也叫内联结，同时可以使用 INNER JOIN...ON来表示
SELECT vend_name, prod_name, prod_price FROM Vendors INNER JOIN Products ON Vendors.vend_id = Products.vend_id;

-- 联结多个表
SELECT prod_name, vend_name, prod_price, quantity FROM OrderItems, Products, Vendors 
	WHERE Products.vend_id = Vendors.vend_id AND OrderItems.prod_id = Products.prod_id AND order_num = 20007;
    
-- 对比于子查询和联结查询
SELECT cust_name, cust_contact FROM Customers WHERE cust_id IN (
	SELECT cust_id FROM Orders WHERE order_num IN (
		SELECT order_num FROM OrderItems WHERE prod_id = 'RGAN01'));
        
SELECT cust_name, cust_contact FROM Customers, Orders, OrderItems 
	WHERE Customers.cust_id = Orders.cust_id AND OrderItems.order_num = Orders.order_num AND prod_id = 'RGAN01';