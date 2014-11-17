-- UPDATE一定要使用WHERE子句
-- UPDATE子句一般由三部分组成：1.要更新的表；2.列名和它们的新值；3.确定要更新哪些行的过滤条件
-- UPDATE Customers SET cust_email='kim@thetoystore.com' WHERE cust_id='1000000005';
SELECT cust_email FROM Customers WHERE cust_id='1000000005';
-- 更新多个列
-- SELECT cust_contact,cust_email FROM Customers WHERE cust_id='1000000006';
-- UPDATE Customers SET cust_contact='Sam roberts',cust_email='sam@toyland.com' WHERE cust_id='1000000006';
SELECT cust_contact,cust_email FROM Customers WHERE cust_id='1000000006';

-- DELETE 数据
-- DELETE FROM Customers WHERE cust_id='1000000006';