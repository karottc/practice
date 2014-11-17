-- 多条SELECT查询返回一个结果集
-- 在多个SELECT 之间用UNION连接
-- 单条SELECT语句
SELECT cust_name, cust_contact, cust_email FROM Customers WHERE cust_state IN ('IL', 'IN','MI');
SELECT cust_name, cust_contact, cust_email FROM Customers WHERE cust_name = 'Fun4All';
-- 上面的语句使用UNION, UNION中的每个查询必须包含相同的列、表达式或聚集函数，但他们可以不以相同的次序列出
SELECT cust_name, cust_contact, cust_email FROM Customers WHERE cust_state IN ('IL', 'IN','MI')
UNION
SELECT cust_name, cust_contact, cust_email FROM Customers WHERE cust_name = 'Fun4All';

-- 对于UNION的组合查询，只能使用一条 ORDER BY 子句
SELECT cust_name, cust_contact, cust_email FROM Customers WHERE cust_state IN ('IL','IN','MI')
UNION
SELECT cust_name, cust_contact, cust_email FROM Customers WHERE cust_name = 'Fun4All'
	ORDER BY cust_name, cust_contact;
