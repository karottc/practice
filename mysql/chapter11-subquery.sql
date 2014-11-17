-- 结合多个表，使用子查询

SELECT cust_id FROM Orders WHERE order_num IN (SELECT order_num FROM OrderItems WHERE prod_id = 'RGAN01');

-- 使用子查询的SELECT语句只能查询单个列
SELECT cust_name, cust_contact FROM Customers WHERE cust_id IN (
	SELECT cust_id FROM Orders WHERE order_num IN (
		SELECT order_num FROM OrderItems WHERE prod_id = 'RGAN01'));
        
-- 作为计算字段使用子查询
SELECT cust_name, cust_state, (
	SELECT COUNT(*) FROM Orders WHERE Orders.cust_id = Customers.cust_id) 
    AS orders FROM Customers ORDER BY cust_name;