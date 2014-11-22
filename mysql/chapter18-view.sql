-- 视图是虚拟表
-- 创建视图 CREATE VIEW; 删除视图：DROP VIEW viewname
/*
CREATE VIEW ProductCustomers AS SELECT cust_name, cust_contact, prod_id 
	FROM Customers, Orders, OrderItems WHERE Customers.cust_id = Orders.cust_id
		AND OrderItems.order_num = Orders.order_num;
*/

SELECT cust_name, cust_contact FROM Productcustomers WHERE prod_id = 'RGAN01';

/*
CREATE VIEW OrderItemxExpanded AS SELECT order_num, prod_id, quantity, item_price,
	quantity*item_price AS expanded_price FROM OrderItems;
*/
    
SELECT *FROM OrderItemxExpanded WHERE order_num = 20008;